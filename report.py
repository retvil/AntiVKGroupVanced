"""Export scan + operation results as JSON and HTML reports.

Best-effort: a failure to write a report never blocks the main operation.
"""

import html
import json
import os
from datetime import datetime
from pathlib import Path


def _timestamp() -> str:
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


def export_json(findings: list[str], profile: str, version: str,
                path: str | os.PathLike) -> Path:
    """Write scan findings to a JSON file. Returns the written path."""
    out = Path(path)
    out.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "app": version,
        "profile": profile,
        "generated": datetime.now().isoformat(timespec="seconds"),
        "findings_count": len(findings),
        "findings": findings,
    }
    out.write_text(json.dumps(payload, ensure_ascii=False, indent=2),
                   encoding="utf-8")
    return out


def export_html(findings: list[str], profile: str, version: str,
                path: str | os.PathLike) -> Path:
    """Write scan findings to a simple HTML file. Returns the written path."""
    out = Path(path)
    out.parent.mkdir(parents=True, exist_ok=True)
    rows = "\n".join(
        f"    <li>{html.escape(f)}</li>" for f in findings
    ) or "    <li><em>no findings</em></li>"
    doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Report — {html.escape(version)} ({html.escape(profile)})</title>
<style>
  body {{ font-family: "Segoe UI", sans-serif; margin: 24px; color: #1f2937; }}
  h1 {{ font-size: 20px; }}
  .meta {{ color: #6b7280; font-size: 12px; margin-bottom: 16px; }}
  ul {{ padding-left: 20px; }}
  li {{ margin: 4px 0; word-break: break-all; }}
</style>
</head>
<body>
<h1>{html.escape(version)} — {html.escape(profile)} report</h1>
<div class="meta">Generated: {datetime.now().isoformat(timespec="seconds")} · {len(findings)} finding(s)</div>
<ul>
{rows}
</ul>
</body>
</html>
"""
    out.write_text(doc, encoding="utf-8")
    return out


def default_report_dir() -> Path:
    """%APPDATA%\\<App>\\reports — created on demand."""
    import backup

    base = backup.BASE_DIR / "reports"
    base.mkdir(parents=True, exist_ok=True)
    return base


def default_report_paths() -> tuple[Path, Path]:
    """(json, html) paths inside the default reports dir."""
    d = default_report_dir()
    stamp = _timestamp()
    return d / f"report_{stamp}.json", d / f"report_{stamp}.html"
