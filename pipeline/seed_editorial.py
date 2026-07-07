#!/usr/bin/env python3
"""各セクターの編集コンテンツ初期セットを生成(ローンチ用)。"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SEED = {
    "defense": {
        "glossary": [
            {"en": "F-35", "jp": "F-35", "body": "米国主導のステルス多用途戦闘機。", "why": "日本・各国の調達・サプライチェーンが防衛株全体のセンチメントに効く。", "tags": ["platforms"]},
            {"en": "AUKUS", "jp": "オーカス", "body": "米英豪の安全保障枠組み。", "why": "潜水艦・ミサイル・サイバー関連の長期需要期待。", "tags": ["budget_policy"]},
        ],
        "news": [
            {"id": "def-001", "date": "2026-07-01", "title": "防衛費増額トレンドの継続", "summary": "主要国で防衛予算拡大が続き、プラットフォーム・電子・ミサイル各社の受注期待が高まっている。", "sentiment": 0.8, "tags": ["budget_policy"], "geo": True, "impact_chain": ["予算増", "受注拡大"], "related_stocks": [], "source_url": ""},
        ],
        "supplychain": {"stages": [{"id": "rd", "num": "1", "name": "研究開発", "desc": "次期装備の設計", "topic": "無人機・極超音速", "steps": []}]},
    },
    "ai-dc": {
        "glossary": [
            {"en": "Blackwell", "jp": "Blackwell", "body": "NVIDIA次世代GPUアーキテクチャ。", "why": "AI DC CapExサイクルの先行指標。", "tags": ["gpu_accel"]},
            {"en": "PUE", "jp": "PUE", "body": "データセンター電力使用効率。", "why": "冷却・電源設備投資の必要性を左右。", "tags": ["cooling"]},
        ],
        "news": [
            {"id": "aidc-001", "date": "2026-07-01", "title": "ハイパースケーラーCapEx継続", "summary": "GPU/サーバー/ネットワーク/冷却の全レイヤーに投資が集中。", "sentiment": 1.0, "tags": ["capex_cycle"], "geo": False, "impact_chain": ["CapEx", "GPU需要"], "related_stocks": [], "source_url": ""},
        ],
        "supplychain": {"stages": [{"id": "gpu", "num": "1", "name": "GPU層", "desc": "AI計算の中核", "topic": "Blackwell世代", "steps": []}]},
    },
    "space": {
        "glossary": [
            {"en": "LEO", "jp": "低軌道", "body": "低地球軌道。衛星コンステレーションの主戦場。", "why": "打ち上げコスト低下で商用宇宙の成長ドライバー。", "tags": ["launch"]},
        ],
        "news": [
            {"id": "sp-001", "date": "2026-07-01", "title": "小型ロケット・衛星需要の拡大", "summary": "商用LEOコンステレーションが打ち上げ・部品・地上局各社を牽引。", "sentiment": 0.6, "tags": ["commercial"], "geo": False, "impact_chain": ["LEO", "打ち上げ需要"], "related_stocks": [], "source_url": ""},
        ],
        "supplychain": {"stages": [{"id": "launch", "num": "1", "name": "打ち上げ", "desc": "ロケット・射場", "topic": "再利用ロケット", "steps": []}]},
    },
    "nuclear": {
        "glossary": [
            {"en": "SMR", "jp": "小型モジュール炉", "body": "Small Modular Reactor。", "why": "次世代原子力の成長テーマ。建設・設備・燃料各社に波及。", "tags": ["smr"]},
        ],
        "news": [
            {"id": "nu-001", "date": "2026-07-01", "title": "再稼働・新設議論の継続", "summary": "脱炭素とエネルギー安全保障の両立で原子力関連株に注目。", "sentiment": 0.5, "tags": ["policy_nuclear"], "geo": True, "impact_chain": ["政策", "設備投資"], "related_stocks": [], "source_url": ""},
        ],
        "supplychain": {"stages": [{"id": "fuel", "num": "1", "name": "燃料サイクル", "desc": "ウラン・加工", "topic": "ウラン価格", "steps": []}]},
    },
}


def write_json(path: Path, obj: dict) -> None:
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    for sector, content in SEED.items():
        d = ROOT / "data" / sector
        write_json(d / "glossary.json", {"terms": content["glossary"]})
        write_json(d / "news.json", {"items": content["news"]})
        write_json(d / "supplychain.json", content["supplychain"])
        write_json(
            d / "weekly_digest.json",
            {
                "title": f"{sector} 週次解説(初版)",
                "body": "Deep Tech Tracker ローンチに伴う初期コンテンツです。週次で更新します。",
                "updated": "2026-07-07",
                "week_start": "2026-07-07",
                "week_end": "2026-07-13",
            },
        )
        write_json(d / "events.json", {"items": []})
        write_json(d / "timeline.json", {"items": []})
        write_json(
            d / "macro.json",
            {
                "last_updated": "2026-07-07",
                "source_url": "",
                "cycle_note": "手動更新(初版)",
                "wsts": {"label": "業界指標", "unit": "—", "series": []},
            },
        )
        print(f"seeded {sector}")


if __name__ == "__main__":
    main()
