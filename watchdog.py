"""Policy watchdog: a daily Windows scheduled task that re-applies the
default-search policy, so a re-hijack cannot survive until the next manual
run.

The task runs the installed EXE (or python main.py) with the
--apply-policy <engine> flag. Install/remove are best-effort; failures are
reported, never fatal.
"""

import json
import os
import subprocess
import sys
from pathlib import Path

# Task namespace under \AntiVKGroup\PolicyWatch (brand-specific, set per repo)
TASK_NAME = r"\AntiVKGroup\PolicyWatch"

# State file: %APPDATA%\<App>\watchdog.json  {"engine": "google", "task": TASK_NAME}
STATE_FILE = Path(os.environ.get("APPDATA", "")) / "AntiVKGroupVanced" / "watchdog.json"


def is_installed() -> bool:
    try:
        proc = subprocess.run(
            ["schtasks", "/query", "/tn", TASK_NAME], capture_output=True, timeout=15
        )
        return proc.returncode == 0
    except (OSError, subprocess.SubprocessError):
        return False


def _exe_path() -> str:
    """Prefer the frozen EXE so a daily task works without Python."""
    if getattr(sys, "frozen", False):
        return sys.executable
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "main.py")


def install(engine_name: str) -> str:
    """Create the daily task. Returns the task id."""
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(
        json.dumps({"engine": engine_name, "task": TASK_NAME}), encoding="utf-8"
    )
    exe = _exe_path()
    if exe.endswith(".py"):
        cmd = f'"{sys.executable}" "{exe}" --apply-policy {engine_name} --yes'
    else:
        cmd = f'"{exe}" --apply-policy {engine_name} --yes'
    args = [
        "schtasks", "/create", "/tn", TASK_NAME,
        "/tr", cmd,
        "/sc", "daily", "/st", "03:00",
        "/f",
    ]
    proc = subprocess.run(args, capture_output=True, text=True, timeout=60)
    if proc.returncode != 0:
        raise RuntimeError((proc.stderr or proc.stdout).strip()[:300])
    return TASK_NAME


def remove() -> None:
    try:
        subprocess.run(["schtasks", "/delete", "/tn", TASK_NAME, "/f"],
                       capture_output=True, timeout=60)
    except (OSError, subprocess.SubprocessError):
        pass
    try:
        STATE_FILE.unlink(missing_ok=True)
    except OSError:
        pass


def state() -> dict | None:
    try:
        if STATE_FILE.is_file():
            return json.loads(STATE_FILE.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        pass
    return None
