#!/usr/bin/env python3
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

AUDIT = Path.home() / ".codex/skills/skill-audit/eval/run.py"
ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    if not AUDIT.is_file():
        print("missing skill-audit eval", file=sys.stderr)
        return 1
    return subprocess.call([sys.executable, str(AUDIT), "--target", str(ROOT)])


if __name__ == "__main__":
    sys.exit(main())
