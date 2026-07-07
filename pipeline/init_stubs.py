#!/usr/bin/env python3
"""価格未取得セクター向けに最小限のスタブ JSON を生成する。"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SECTORS = ("defense", "ai-dc", "space", "nuclear")


def load_themes(sector: str) -> dict:
    return json.loads((ROOT / "data" / sector / "themes.json").read_text(encoding="utf-8"))


def stub_perf(sector: str) -> dict:
    themes = load_themes(sector)
    return {
        "last_updated": "2026-07-01",
        "note": "スタブ(初回パイプライン実行前)",
        "themes": [
            {
                "key": m["key"],
                "name": m["name"],
                "color": m["color"],
                "ytd_pct": None,
                "vol_ratio": None,
                "spark": [],
                "n_stocks": sum(
                    len(sub.get("jp", [])) + len(sub.get("solo", []))
                    for sub in m["subs"]
                ),
                "n_ok": 0,
            }
            for m in themes["macro"]
        ],
    }


def stub_detail(sector: str) -> dict:
    themes = load_themes(sector)
    return {
        "last_updated": "2026-07-01",
        "note": "スタブ",
        "themes": [
            {"key": m["key"], "name": m["name"], "color": m["color"], "ytd_pct": None, "series": [], "subs": []}
            for m in themes["macro"]
        ],
    }


def write(path: Path, obj: dict) -> None:
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def main() -> None:
    benchmarks = {
        "defense": ("ITA", "ITA指数"),
        "ai-dc": ("SMH", "SMH指数"),
        "space": ("UFO", "UFO指数"),
        "nuclear": ("URA", "URA指数"),
    }
    for sector in SECTORS:
        d = ROOT / "data" / sector
        d.mkdir(parents=True, exist_ok=True)
        sym, name = benchmarks[sector]
        write(d / "themes_perf.json", stub_perf(sector))
        write(d / "themes_detail.json", stub_detail(sector))
        write(d / "indices.json", {"last_updated": "2026-07-01", "indices": []})
        write(d / "linkage.json", {"last_updated": "2026-07-01", "method": "", "themes": {}})
        write(d / "linkage_top.json", {"last_updated": "2026-07-01", "method": "", "rows": []})
        write(d / "timeline_stats.json", {"last_updated": "2026-07-01", "reactions": {}})
        write(d / "prices.json", {"last_updated": "2026-07-01", "quotes": {}})
        write(d / "headlines.json", {"last_updated": "2026-07-01", "items": []})
        write(d / "news.json", {"items": []})
        write(d / "events.json", {"items": []})
        write(d / "timeline.json", {"items": []})
        write(d / "weekly_digest.json", {"title": f"{sector} 初回セットアップ", "body": "パイプライン初回実行後に更新されます。", "updated": "2026-07-01"})
        write(d / "macro.json", {"note": "手動更新", "items": []})
        write(d / "glossary.json", {"terms": []})
        write(d / "supplychain.json", {"stages": [], "topic": ""})
        print(f"stubbed {sector}")

    hub = ROOT / "data" / "hub"
    hub.mkdir(parents=True, exist_ok=True)
    write(
        hub / "weekly_digest.json",
        {
            "title": "Deep Tech 5テーマ横断 — 初回セットアップ",
            "body": "半導体・防衛・AIデータセンター・宇宙・原子力電力の5セクターを横断する週次解説はここに掲載します。",
            "updated": "2026-07-01",
        },
    )
    print("stubbed hub")


if __name__ == "__main__":
    main()
