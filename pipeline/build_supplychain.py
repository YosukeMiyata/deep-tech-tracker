#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""process_map.py から data/{sector}/supplychain.json (/{sector}/map ページ用) を生成する。

- ステージ構成・説明・初期topicは本ファイルの STAGE_META で定義
- steps は pipeline/maps/{sector}/process_map.py の PROCESS_MAP から自動変換
  (equip/material はそのまま、groups は stocks に変換)
- 既存 supplychain.json に手動更新済みの topic があれば温存する
- semi は手作りの完成版があるためデフォルト対象外(--theme semi で明示指定時のみ)

使い方:
  python3 pipeline/build_supplychain.py            # defense/ai-dc/space/nuclear
  python3 pipeline/build_supplychain.py --theme defense
"""

from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAPS = ROOT / "pipeline" / "maps"
DATA = ROOT / "data"

# sector(dataディレクトリ名) → mapsモジュールディレクトリ名
SECTORS = {
    "defense": "defense",
    "ai-dc": "ai_dc",
    "space": "space",
    "nuclear": "nuclear",
    "semi": "semi",
}

# ステージ定義: sources = PROCESS_MAP の stage 値、reassign = 工程名→このステージへ強制移動
STAGE_META = {
    "defense": [
        {"id": "rd", "num": "STAGE 1", "name": "研究開発(R&D)",
         "desc": "次世代装備の概念設計・試作・技術実証。AI/自律化・極超音速・電磁戦など新領域の開発競争。",
         "topic": "無人機・AI・スタンドオフ防衛に予算重点。防衛装備庁の研究開発費は過去最大水準。",
         "sources": ["rd"]},
        {"id": "procure", "num": "STAGE 2", "name": "調達・契約",
         "desc": "政府調達・長期契約・国際共同開発。防衛費増額の恩恵が最初に通過する関門。",
         "topic": "防衛費GDP比2%への増額が調達を下支え。GCAP(次期戦闘機)の日英伊分担が進展。",
         "sources": ["procure"]},
        {"id": "mfg", "num": "STAGE 3", "name": "製造・統合",
         "desc": "戦闘機・艦艇・車両・弾薬の製造とシステム統合。国内サプライチェーン強靭化の主戦場。",
         "topic": "弾薬・火工品の増産投資が進行。ドローンの国産化と量産体制づくりが新戦線。",
         "sources": ["mfg"]},
        {"id": "deploy", "num": "STAGE 4", "name": "配備・作戦システム",
         "desc": "C4ISR・サイバー・宇宙領域を含む配備と作戦基盤。ソフトウェアとデータの比重が上昇。",
         "topic": "サイバー・宇宙領域の予算比重が上昇。官民のセキュリティ需要が拡大。",
         "sources": ["deploy"]},
        {"id": "sustain", "num": "STAGE 5", "name": "サステインメント(MRO)",
         "desc": "整備・補給・後方支援。装備品のライフサイクルコストの大半を占める安定収益領域。",
         "topic": "稼働率向上と部品供給網の強靭化が課題。MRO長期契約の獲得競争。",
         "sources": ["sustain"]},
    ],
    "ai-dc": [
        {"id": "compute", "num": "STAGE 1", "name": "AI半導体・サーバー製造",
         "desc": "GPU/アクセラレータとAIサーバーの設計・製造。CapExサイクルの起点。",
         "topic": "NVIDIA Vera Rubin量産開始でODM各社の受注が拡大。",
         "sources": ["design"]},
        {"id": "build", "num": "STAGE 2", "name": "DC建設・設備工事",
         "desc": "データセンターの建屋・電気・空調工事。国内はゼネコン・サブコンの独壇場。",
         "topic": "苫小牧・石狩など地方立地が加速。建設費高騰と電力確保がボトルネック。",
         "sources": ["build"]},
        {"id": "power", "num": "STAGE 3", "name": "電力・電源",
         "desc": "受電・変電・非常用電源から電力調達(PPA)まで。AI電力問題の主戦場。",
         "topic": "原子力PPA・ガスタービン争奪戦。日本は原発再稼働とDC誘致が連動するテーマに。",
         "sources": ["power"]},
        {"id": "network", "num": "STAGE 4", "name": "ネットワーク・光接続",
         "desc": "DC内外を結ぶスイッチ・光モジュール・ケーブル。帯域需要は生成AIで急拡大。",
         "topic": "800G/1.6T光モジュールへの移行が進行。CPO(光電融合)実用化前夜。",
         "sources": ["network"]},
        {"id": "operate", "num": "STAGE 5", "name": "運用・クラウド",
         "desc": "ハイパースケーラー・国内キャリア・GPUクラウドの運用レイヤー。",
         "topic": "国内AI計算基盤の整備が政策支援で進む。GPUクラウド新興の設備投資が続く。",
         "sources": ["operate"]},
    ],
    "space": [
        {"id": "launch", "num": "STAGE 1", "name": "ロケット・打ち上げ",
         "desc": "輸送手段の確保が宇宙ビジネスの入口。材料・部品の国産サプライチェーンも含む。",
         "topic": "H3の商業受注拡大。米新興(Firefly等)の上場で打ち上げ競争が激化。",
         "sources": ["launch"]},
        {"id": "orbit", "num": "STAGE 2", "name": "衛星製造・軌道上",
         "desc": "衛星の製造・コンステレーション構築・軌道上サービス(デブリ除去等)。",
         "topic": "小型SARコンステレーション増強が続く。デブリ除去の実証が商用化へ前進。",
         "sources": ["orbit"]},
        {"id": "ground", "num": "STAGE 3", "name": "地上局・運用",
         "desc": "衛星を運用する地上インフラ。地上局の共有・仮想化が進むレイヤー。",
         "topic": "地上局のクラウド化・共有サービスが拡大。",
         "sources": ["ground"]},
        {"id": "service", "num": "STAGE 4", "name": "衛星通信・サービス",
         "desc": "通信・放送・測位などの衛星サービス。防衛需要との二面性を持つ。",
         "topic": "D2D(衛星-スマホ直接通信)の商用化競争が本格化。",
         "sources": ["service"]},
        {"id": "data", "num": "STAGE 5", "name": "データ利用・応用",
         "desc": "衛星データの解析・防災・気象・地理空間情報。宇宙の価値が地上ビジネスに変わる出口。",
         "topic": "防災・安全保障用途で官需が拡大。SAR画像解析の民間利用が広がる。",
         "sources": [], "reassign": ["衛星データ利用"]},
    ],
    "nuclear": [
        {"id": "fuel", "num": "STAGE 1", "name": "核燃料サイクル",
         "desc": "ウラン採掘・転換・濃縮・成型加工。地政学で供給網が再編中の川上。",
         "topic": "ウラン価格は高止まり。濃縮能力の西側回帰(脱ロシア)が進む。",
         "sources": ["fuel"]},
        {"id": "build", "num": "STAGE 2", "name": "新設・建設",
         "desc": "原子炉の新増設・建て替え。重電メーカーとプラントエンジの主戦場。",
         "topic": "エネルギー基本計画で建て替えが明記。国内の新設議論が再始動。",
         "sources": ["build"], "exclude": ["次世代炉・核融合"]},
        {"id": "operate", "num": "STAGE 3", "name": "運転・再稼働",
         "desc": "既設炉の運転・定期検査・再稼働対応。バルブ・保守工事の安定需要。",
         "topic": "再稼働が着実に進展。DC電力需要が原子力の追い風に。",
         "sources": ["operate"]},
        {"id": "decom", "num": "STAGE 4", "name": "廃炉・バックエンド",
         "desc": "廃止措置・除染・中間貯蔵・最終処分。数十年続く長期市場。",
         "topic": "廃炉ビジネスの市場化が進む。中間貯蔵・処分地の議論も動く。",
         "sources": ["decom"]},
        {"id": "next", "num": "STAGE 5", "name": "次世代炉・核融合",
         "desc": "SMR・高温ガス炉・核融合。AIデータセンターの電力需要が投資を加速させる新戦線。",
         "topic": "核融合スタートアップへの投資が拡大。ITER関連調達・国内実証も進む。",
         "sources": [], "reassign": ["次世代炉・核融合"]},
    ],
    # semi は手作り版が正。再生成したい場合のみ --theme semi で(既存topicは温存される)。
    "semi": [
        {"id": "front", "num": "STAGE 1", "name": "前工程(ウェハー・露光・成膜)",
         "desc": "シリコンウェハー上に回路を形成する工程。装置と材料で日本勢の世界シェアが高い領域。",
         "topic": "", "sources": ["front"]},
        {"id": "package", "num": "STAGE 2", "name": "先端パッケージング(CoWoS等)",
         "desc": "複数チップを高密度に接続する工程。AI半導体のボトルネックとして注目度が急上昇。",
         "topic": "", "sources": ["back"]},
        {"id": "maker", "num": "STAGE 3", "name": "メーカー・設計",
         "desc": "半導体メーカー・ファブレス・EDAのレイヤー。",
         "topic": "", "sources": ["maker", "design"]},
        {"id": "facility", "num": "STAGE 4", "name": "ファシリティ・商社",
         "desc": "工場インフラ・ガス供給・商社などの周辺レイヤー。",
         "topic": "", "sources": ["facility"]},
    ],
}

SUPPLYCHAIN_THEMES = ("defense", "ai-dc", "space", "nuclear")


def load_process_map(module_dir: str):
    path = MAPS / module_dir / "process_map.py"
    spec = importlib.util.spec_from_file_location(f"_sc_{module_dir}", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.PROCESS_MAP


def load_theme_codes(sector: str) -> set:
    themes = json.loads((DATA / sector / "themes.json").read_text(encoding="utf-8"))
    codes = set()
    for m in themes["macro"]:
        for sub in m["subs"]:
            codes |= {u["symbol"] for u in sub["us"]}
            codes |= {r["code"] for r in sub["jp"]}
            codes |= {r["code"] for r in sub.get("solo", [])}
    return codes


def convert_step(entry: dict) -> list[dict]:
    """PROCESS_MAP の1エントリを SupplyStep のリストに変換する。"""
    if "groups" in entry:
        return [
            {"name": f"{entry['name']}: {g['label']}", "stocks": list(g["stocks"])}
            for g in entry["groups"]
        ]
    step = {"name": entry["name"]}
    if entry.get("equip"):
        step["equip"] = list(entry["equip"])
    if entry.get("material"):
        step["material"] = list(entry["material"])
    return [step]


def build_sector(sector: str) -> list[str]:
    module_dir = SECTORS[sector]
    pmap = load_process_map(module_dir)
    meta = STAGE_META[sector]
    out_path = DATA / sector / "supplychain.json"

    # 手動更新済み topic の温存
    old_topics: dict[str, str] = {}
    if out_path.exists():
        try:
            old = json.loads(out_path.read_text(encoding="utf-8"))
            old_topics = {s.get("id"): s.get("topic", "") for s in old.get("stages", [])}
        except Exception:
            pass

    # 工程名→強制移動先ステージid
    reassign: dict[str, str] = {}
    for st in meta:
        for name in st.get("reassign", []):
            reassign[name] = st["id"]

    stages_out = []
    for st in meta:
        steps: list[dict] = []
        for entry in pmap:
            target = reassign.get(entry["name"])
            in_sources = entry.get("stage") in st.get("sources", [])
            excluded = entry["name"] in st.get("exclude", [])
            if target == st["id"] or (target is None and in_sources and not excluded):
                steps.extend(convert_step(entry))
        topic = old_topics.get(st["id"], "") or st["topic"]
        stages_out.append({
            "id": st["id"], "num": st["num"], "name": st["name"],
            "desc": st["desc"], "topic": topic, "steps": steps,
        })

    payload = {
        "_schema": ("stages: サプライチェーン順のステージ。steps は pipeline/maps/*/process_map.py "
                    "から build_supplychain.py が自動生成。topic(今週の論点)は手動更新可(再生成でも温存)。"),
        "stages": stages_out,
    }
    out_path.write_text(json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8")

    # 検証: 銘柄マスタに無いコードを警告
    theme_codes = load_theme_codes(sector)
    used = set()
    for st in stages_out:
        for step in st["steps"]:
            used |= set(step.get("equip", [])) | set(step.get("material", [])) | set(step.get("stocks", []))
    unknown = sorted(used - theme_codes)
    n_steps = sum(len(s["steps"]) for s in stages_out)
    print(f"wrote {out_path.relative_to(ROOT)} ({len(stages_out)} ステージ / {n_steps} 工程 / 銘柄 {len(used)})")
    if unknown:
        print(f"  warning: themes.json に無いコード: {', '.join(unknown)}")
    return unknown


def build_for_theme(theme: str) -> None:
    if theme not in SECTORS:
        return
    if theme == "semi":
        return
    build_sector(theme)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--theme", default="all", help="all / defense / ai-dc / space / nuclear / semi")
    args = ap.parse_args()
    if args.theme == "all":
        targets = list(SUPPLYCHAIN_THEMES)
    else:
        targets = [args.theme]
    for sector in targets:
        print(f"=== {sector} ===")
        build_sector(sector)


if __name__ == "__main__":
    main()
