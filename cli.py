"""CLI entry point for non-interactive (script/Intune) usage.

Usage examples:
    python main.py --scan-only
    python main.py --apply --yes --apply-policy google
    python main.py --restore
    python main.py --install-watchdog google
    python main.py --remove-watchdog
    python main.py --report C:\\reports\\out.json

Exit codes: 0 success, 1 failure, 2 findings-only (scan found items).
"""

import argparse
import sys


def _print_translated(key: str, *args) -> None:
    """Print a UI-string via the current app language (en default for CLI)."""
    import translations

    text = translations.t("en", key)
    if args:
        try:
            text = text.format(*args)
        except (IndexError, KeyError):
            text = f"{text} {args}"
    print(text)


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="antibrand-vanced",
        description="Remove the brand's browser/search hijack vectors "
                    "and lock the default search engine.",
    )
    p.add_argument("--scan-only", action="store_true",
                   help="Run the scan and print findings; make no changes.")
    p.add_argument("--apply", action="store_true",
                   help="Perform removal + policy application (destructive).")
    p.add_argument("--apply-policy", metavar="ENGINE",
                   help="Apply the hard policy for ENGINE only "
                        "(e.g. google, bing, duckduckgo).")
    p.add_argument("--yes", action="store_true",
                   help="Auto-confirm all prompts (required for --apply).")
    p.add_argument("--consent-user-data", action="store_true",
                   help="Also remove items that contain user data "
                        "(Disk files, cookies, extensions).")
    p.add_argument("--restore", action="store_true",
                   help="Restore the last backup session (registry/tasks/files).")
    p.add_argument("--install-watchdog", metavar="ENGINE",
                   help="Create a daily scheduled task that re-applies ENGINE policy.")
    p.add_argument("--remove-watchdog", action="store_true",
                   help="Remove the watchdog scheduled task.")
    p.add_argument("--report", metavar="PATH",
                   help="Write JSON findings report to PATH.")
    p.add_argument("--html-report", metavar="PATH",
                   help="Write HTML findings report to PATH.")
    p.add_argument("--list-engines", action="store_true",
                   help="Print available search engines and exit.")
    return p


def _cmd_scan(profile: str) -> list[str]:
    import mailru_detect

    return mailru_detect.scan_all(profile)


def _cmd_apply(args) -> int:
    import app
    import backup
    import mailru_detect
    import policies
    import engines

    backup.start_session()
    # Kill product processes first
    import psutil
    for proc in psutil.process_iter(["name"]):
        try:
            name = (proc.info.get("name") or "").lower()
            if name in {'agent.exe', 'vk_messenger.exe', 'mailru_cloud.exe'}:
                proc.kill()
        except Exception:
            pass

    # Removal of selected findings (excluding user-data unless consented)
    findings = _cmd_scan(args.profile)
    if args.consent_user_data:
        selected = findings
    else:
        selected = [f for f in findings if not f.startswith(mailru_detect.CONSENT_PREFIXES)]
    removed, failed = mailru_detect.remove_selected(selected)
    print(f"removed: {len(removed)} failed: {len(failed)}")

    # Apply policy
    if args.apply_policy:
        engine = engines.get_engine(args.apply_policy)
        applied, pfailed = policies.apply_chromium(
            engine, list(policies.CHROMIUM_POLICY_PATHS))
        ff_applied, ff_failed = policies.apply_firefox(engine)
        applied += ff_applied
        pfailed += ff_failed
        print(f"policy applied: {len(applied)} failed: {len(pfailed)}")
        for f in pfailed:
            print(f"  policy-fail: {f}")
    return 1 if (failed or pfailed) else 0


def _cmd_restore() -> int:
    import restore

    result = restore.restore()
    print(f"restored: reg={result['reg']} tasks={result['tasks']} files={result['files']}")
    for e in result["errors"]:
        print(f"  restore-err: {e}")
    return 1 if result["errors"] and result["reg"] + result["tasks"] + result["files"] == 0 else 0


def _cmd_watchdog(args) -> int:
    import watchdog

    if args.install_watchdog:
        try:
            task = watchdog.install(args.install_watchdog)
            print(f"watchdog installed: {task} (engine={args.install_watchdog})")
            return 0
        except Exception as exc:
            print(f"watchdog install failed: {exc}")
            return 1
    elif args.remove_watchdog:
        watchdog.remove()
        print("watchdog removed")
        return 0
    return 0


def _cmd_report(args) -> int:
    import report

    findings = _cmd_scan(args.profile)
    if args.report:
        p = report.export_json(findings, args.profile, "1.2", args.report)
        print(f"report: {p}")
    if args.html_report:
        p = report.export_html(findings, args.profile, "1.2", args.html_report)
        print(f"html-report: {p}")
    for f in findings:
        print(f"finding: {f}")
    return 2 if findings else 0


def main(profile: str, argv: list[str] | None = None) -> int:
    """Run the CLI. ``profile`` is profiles.VANCED or profiles.EXTENDED."""
    parser = build_parser()
    args = parser.parse_args(argv)
    args.profile = profile

    if args.list_engines:
        import engines
        for name in engines.ENGINE_NAMES:
            print(name)
        return 0

    # profile is set by the caller (main.py / main_extended.py)
    if args.scan_only:
        return _cmd_report(args)

    if args.apply:
        if not args.yes:
            print("--apply requires --yes")
            return 1
        return _cmd_apply(args)

    if args.restore:
        return _cmd_restore()

    if args.install_watchdog or args.remove_watchdog:
        return _cmd_watchdog(args)

    # no action flags: just help
    parser.print_help()
    return 0
