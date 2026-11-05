"""AntiVKGroupVanced entry point — Baidu Browser + Baidu Search removal.

With flags -> CLI mode (non-interactive, for scripts/Intune):
    python main.py --scan-only
    python main.py --apply --yes --apply-policy google
    python main.py --restore
    python main.py --install-watchdog google
    python main.py --help

Without flags -> GUI.
"""

import sys

import app
import cli
import profiles

if __name__ == "__main__" and len(sys.argv) > 1:
    sys.exit(cli.main(profiles.VANCED, sys.argv[1:]))

app.run(profiles.VANCED)
