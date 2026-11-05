"""AntiBaiduExtended entry point - removal of every Baidu product.

With flags -> CLI mode (non-interactive, for scripts/Intune); without -> GUI.
"""

import sys

import app
import cli
import profiles

if __name__ == "__main__" and len(sys.argv) > 1:
    sys.exit(cli.main(profiles.EXTENDED, sys.argv[1:]))

app.run(profiles.EXTENDED)
