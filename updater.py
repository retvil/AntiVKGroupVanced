"""Lightweight update check against the GitHub releases API.

No third-party deps: uses urllib. Best-effort — any failure (offline,
non-standard hosts, timeouts) returns None so the GUI can silently skip.
"""

import json
import re
import urllib.request

LATEST_RELEASE_URL = "https://api.github.com/repos/retvil/AntiVKGroupVanced/releases/latest"
_USER_AGENT = "AntiVKGroupVanced/1.2"


def fetch_latest_version() -> str | None:
    """Return the latest release tag (e.g. 'v1.3.0') or None when offline."""
    try:
        req = urllib.request.Request(
            LATEST_RELEASE_URL, headers={"User-Agent": _USER_AGENT, "Accept": "application/vnd.github+json"}
        )
        with urllib.request.urlopen(req, timeout=6) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        tag = (data.get("tag_name") or "").strip()
        return tag or None
    except (OSError, ValueError, TimeoutError):
        return None


def _parse(tag_or_version: str) -> tuple[int, int, int]:
    m = re.match(r"v?(\d+)\.(\d+)\.(\d+)", tag_or_version)
    if not m:
        return (0, 0, 0)
    return (int(m.group(1)), int(m.group(2)), int(m.group(3)))


def is_newer(latest_tag: str | None, current_version: str) -> bool:
    """True when `latest_tag` (e.g. 'v1.3.0') is greater than current_version ('1.2.0')."""
    if not latest_tag:
        return False
    return _parse(latest_tag) > _parse(current_version)
