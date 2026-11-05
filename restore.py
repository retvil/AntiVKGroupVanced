"""Restore the most recent backup session.

Pairs with backup.py: every destructive run exports registry keys (.reg),
files and scheduled-task XML into %APPDATA%\\<App>\\backup\\<stamp>\\.
restore() replays that session:

- .reg files  -> reg import
- task_*.xml  -> re-register via schtasks /create /xml
- files/      -> copied back when the original path is recorded in
  files\\manifest.json (see backup.record_file)

All steps are best-effort and report per-item results.
"""

import json
import os
import re
import shutil
import subprocess
from pathlib import Path

BASE_DIR = Path(os.environ.get("APPDATA", "")) / "AntiVKGroupVanced"
BACKUP_ROOT = BASE_DIR / "backup"


def list_sessions() -> list[Path]:
    """Backup session folders, newest last."""
    if not BACKUP_ROOT.is_dir():
        return []
    sessions = [p for p in BACKUP_ROOT.iterdir() if p.is_dir()]
    return sorted(sessions, key=lambda p: p.name)


def last_session() -> Path | None:
    sessions = list_sessions()
    return sessions[-1] if sessions else None


def _import_reg(reg_file: Path) -> bool:
    try:
        proc = subprocess.run(
            ["reg", "import", str(reg_file)], capture_output=True, timeout=60
        )
        return proc.returncode == 0
    except (OSError, subprocess.SubprocessError):
        return False


def _task_name_from_xml(xml_file: Path) -> str | None:
    head = xml_file.read_text(encoding="utf-8", errors="replace")[:4000]
    if re.search(r'xmlns="Microsoft\.Windows\.TaskScheduler\.\d+"', head):
        m = re.search(r"^\s*<Task[^>]*\sName=\"([^\"]+)\"", head, re.M)
        if m:
            return m.group(1)
    m = re.search(r"<TaskName>([^<]+)</TaskName>", head)
    return m.group(1) if m else None


def _recreate_task(xml_file: Path) -> bool:
    name = _task_name_from_xml(xml_file)
    if not name:
        return False
    try:
        proc = subprocess.run(
            ["schtasks", "/create", "/tn", name, "/xml", str(xml_file)],
            capture_output=True, timeout=60,
        )
        return proc.returncode == 0
    except (OSError, subprocess.SubprocessError, UnicodeDecodeError):
        return False


def restore(session_dir: Path | None = None) -> dict:
    """Replay a backup session.

    Returns {'reg': n, 'tasks': n, 'files': n, 'errors': [...], 'session': str}.
    """
    src = session_dir or last_session()
    result = {
        "reg": 0,
        "tasks": 0,
        "files": 0,
        "errors": [],
        "session": str(src) if src else None,
    }
    if src is None or not src.is_dir():
        result["errors"].append("no backup session found")
        return result

    manifest = src / "files" / "manifest.json"
    manifest_map: dict[str, str] = {}
    if manifest.is_file():
        try:
            manifest_map = json.loads(manifest.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            manifest_map = {}

    for reg_file in sorted(src.glob("*.reg")):
        if _import_reg(reg_file):
            result["reg"] += 1
        else:
            result["errors"].append(f"reg import failed: {reg_file.name}")

    for xml_file in sorted(src.glob("task_*.xml")):
        if _recreate_task(xml_file):
            result["tasks"] += 1
        else:
            result["errors"].append(f"task recreate failed: {xml_file.name}")

    files_root = src / "files"
    if files_root.is_dir():
        for f in sorted(files_root.rglob("*")):
            if not f.is_file() or f.name == "manifest.json":
                continue
            rel = f.relative_to(files_root).as_posix()
            target = manifest_map.get(rel)
            if not target:
                continue
            try:
                dest = Path(target)
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(f, dest)
                result["files"] += 1
            except OSError as exc:
                result["errors"].append(f"file copy failed {rel}: {exc}")

    try:
        import backup

        backup.log_action(
            f"restore: session={src.name} reg={result['reg']} "
            f"tasks={result['tasks']} files={result['files']} "
            f"errors={len(result['errors'])}"
        )
    except Exception:
        pass
    return result


def has_backup() -> bool:
    return last_session() is not None
