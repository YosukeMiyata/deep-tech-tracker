#!/usr/bin/env python3
"""全セクターの株価更新 + ヘッドライン取得を順次実行。"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from theme_config import SECTOR_IDS  # noqa: E402


def main() -> None:
    root = Path(__file__).resolve().parent
    for theme in SECTOR_IDS:
        print(f"\n========== {theme} ==========")
        r = subprocess.run([sys.executable, str(root / "update_prices.py"), "--theme", theme], check=False)
        if r.returncode != 0:
            print(f"!! {theme} 株価更新失敗 (exit {r.returncode})", file=sys.stderr)
            sys.exit(r.returncode)
        subprocess.run(
            [sys.executable, str(root / "fetch_headlines.py"), "--theme", theme],
            check=False,
        )


if __name__ == "__main__":
    main()
