"""Extended-edition scans: whole Mail.ru / VK Group products beyond the messengers.

Covers Store (Appx) applications — VK, Mail.ru, ICQ, TamTam, VK Play, My.com
GameCenter — and product install directories under Program Files\\Mail.Ru and
Program Files\\VK that are not the messengers themselves.
"""

import os
import re
import shutil
import subprocess
from pathlib import Path

import backup

PRODUCT_PROCESS_MARKERS: tuple[str, ...] = (
    "mail.ru", "mailru", "magent", "icq", "tamtam",
    "vkontakte", "vkmessenger", "vkplay", "my.com", "mygames", "облако",
)

# Exact process names that alone identify a product (short names like vk.exe
# are too generic to match as substrings).
_PRODUCT_PROCESS_NAMES: frozenset[str] = frozenset({
    "vk.exe", "icq.exe", "tamtam.exe", "cloud.exe",
    "magent.exe", "mailruagent.exe", "vkmessenger.exe",
})


def is_product_process(name: str | None) -> bool:
    """True if a process belongs to any Mail.ru / VK product (Extended kill scope).

    Covers Mail.ru Agent (magent.exe), VK Messenger (vkmessenger.exe),
    Облако Mail.ru (cloud.exe), ICQ, TamTam, VK Play and Store apps.
    """
    lowered = (name or "").lower()
    return lowered in _PRODUCT_PROCESS_NAMES or any(
        marker in lowered for marker in PRODUCT_PROCESS_MARKERS
    )

_STORE_APPS_PS = (
    "[Console]::OutputEncoding=[Text.Encoding]::UTF8;"
    "Get-AppxPackage | Where-Object { $_.Name -match "
    "'mail\\.?ru|vkontakte|^vk$|icq|tamtam|vkplay|mygames|my\\.com' }"
    " | ForEach-Object { \"$($_.Name)|$($_.PackageFullName)\" }"
)


def _parse_appx_output(text: str) -> list[tuple[str, str]]:
    """Parse 'Name|PackageFullName' lines produced by the Appx scan script."""
    result = []
    for line in text.splitlines():
        line = line.strip()
        if "|" in line and line != "|":
            name, _, full_name = line.partition("|")
            if name and full_name:
                result.append((name, full_name))
    return result


def scan_store_apps() -> list[str]:
    """Mail.ru / VK Store (Appx) applications installed for the current user."""
    try:
        proc = subprocess.run(
            ["powershell", "-NoProfile", "-Command", _STORE_APPS_PS],
            capture_output=True, timeout=120,
        )
    except (OSError, subprocess.SubprocessError):
        return []
    text = proc.stdout.decode("utf-8", errors="replace")
    return [
        f"Store app: {name} ({full_name})"
        for name, full_name in _parse_appx_output(text)
    ]


def remove_store_app(finding: str) -> bool:
    """Uninstall one Store app by its package full name.

    Args:
        finding: a "Store app: Name (PackageFullName)" finding string.

    Returns:
        True if Remove-AppxPackage reported success.
    """
    full_name = finding[len("Store app: "):].rsplit(" (", 1)[0].rstrip(")")
    escaped = full_name.replace("'", "''")
    script = (
        "[Console]::OutputEncoding=[Text.Encoding]::UTF8;"
        f"Remove-AppxPackage -Package '{escaped}'"
    )
    try:
        proc = subprocess.run(
            ["powershell", "-NoProfile", "-Command", script],
            capture_output=True, timeout=180,
        )
    except (OSError, subprocess.SubprocessError):
        return False
    return proc.returncode == 0


# Messenger install subdirectory names excluded from product-dir scans
# (they are reported by mailru_detect.scan_install_paths instead).
_MESSENGER_INSTALL_DIRS: frozenset[str] = frozenset({"agent", "magent"})

# %LOCALAPPDATA%\Programs prefixes treated as Mail.ru / VK products.
_LOCAL_PROGRAMS_PREFIXES: tuple[str, ...] = (
    "mail.ru", "mailru", "vk", "icq", "tamtam", "my.com", "mygames", "vkplay",
)


def scan_product_dirs() -> list[str]:
    """Non-messenger Mail.ru / VK product directories.

    Covers Program Files\\Mail.Ru\\* and Program Files\\VK\\* (everything
    except the Agent subdirectory) and per-user installs under
    %LOCALAPPDATA%\\Programs (VK Play, My.com GameCenter, ICQ desktop apps
    live there). The messenger install paths are reported by
    mailru_detect.scan_install_paths as "Install path: ..."; everything
    else is reported here.
    """
    found = []
    for base in (
        r"C:\Program Files\Mail.Ru",
        r"C:\Program Files (x86)\Mail.Ru",
        r"C:\Program Files\VK",
        r"C:\Program Files (x86)\VK",
    ):
        if not os.path.isdir(base):
            continue
        for entry in os.listdir(base):
            path = os.path.join(base, entry)
            if os.path.isdir(path) and entry.lower() not in _MESSENGER_INSTALL_DIRS:
                found.append(f"Product dir: {path}")
    local_programs = os.path.join(os.environ.get("LOCALAPPDATA", ""), "Programs")
    if os.path.isdir(local_programs):
        for entry in os.listdir(local_programs):
            low = entry.lower()
            if not any(low.startswith(p) for p in _LOCAL_PROGRAMS_PREFIXES):
                continue
            path = os.path.join(local_programs, entry)
            if not os.path.isdir(path):
                continue
            if low in ("mail.ru", "mailru", "vk"):
                for sub in os.listdir(path):
                    sub_path = os.path.join(path, sub)
                    if os.path.isdir(sub_path) and sub.lower() not in _MESSENGER_INSTALL_DIRS:
                        found.append(f"Product dir: {sub_path}")
            else:
                found.append(f"Product dir: {path}")
    return found


def scan_local_data_dirs() -> list[str]:
    """Non-messenger Mail.ru / VK data directories under %LOCALAPPDATA%.

    The Agent / VK Messenger install directories are reported by
    mailru_detect.scan_install_paths; other subdirectories (updater caches,
    game launchers, VK Play data) belong to other products. These hold user
    data, so the finding is consent-gated.
    """
    found = []
    local = Path(os.environ.get("LOCALAPPDATA", ""))
    for base_name in ("Mail.Ru", "VK"):
        base = local / base_name
        if not base.is_dir():
            continue
        for entry in sorted(base.iterdir()):
            if entry.is_dir() and entry.name.lower() not in _MESSENGER_INSTALL_DIRS:
                found.append(f"Local data: {entry}")
    return found


def remove_local_data(finding: str) -> bool:
    """Delete one non-messenger local data directory (exported to backup first)."""
    target = finding[len("Local data: "):]
    backup.export_dir(target)
    try:
        shutil.rmtree(target, ignore_errors=False)
        return True
    except OSError:
        return False


def remove_product_dir(finding: str) -> bool:
    """Delete one non-messenger product directory (exported to backup first)."""
    target = finding[len("Product dir: "):]
    backup.export_dir(target)
    try:
        shutil.rmtree(target, ignore_errors=False)
        return True
    except OSError:
        return False
