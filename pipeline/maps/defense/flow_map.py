# -*- coding: utf-8 -*-
"""
フロービジュアル定義: 防衛バリューチェーン 5ステージ
① 研究開発(R&D)
② 調達・契約
③ 製造・統合
④ 配備・作戦展開
⑤ サステインメント(MRO)

各ステージ = {key, name, icon, color, desc, visual, steps:[...]}
各工程(step) = {name, icon, desc, roles:[{label, codes:[...]}], visual(任意)}
"""

FLOW = [
    {
        "key": "rd",
        "name": "① 研究開発(R&D)",
        "icon": "🔬",
        "color": "#8E44AD",
        "desc": "次世代装備の概念設計・試作・技術実証。AI/自律化・極超音速・電磁戦など新領域の開発競争。",
        "visual": "lab",
        "steps": [
            {
                "name": "防衛研究・コンサル",
                "icon": "📖",
                "desc": "防衛政策・技術ロードマップ・試験設計",
                "roles": [
                    {"label": "研究・コンサル", "codes": ["3636", "BAH", "LDOS"]},
                    {"label": "防衛AI・データ", "codes": ["PLTR", "SAIC"]},
                ],
            },
            {
                "name": "センサー・誘導技術",
                "icon": "👁️",
                "desc": "レーダー・EO/IR・慣性制御の先行開発",
                "roles": [
                    {"label": "センサー", "codes": ["6965", "6758", "6235", "MRCY"]},
                    {"label": "日本防衛エレクトロニクス", "codes": ["6503", "7711", "6724"]},
                ],
            },
            {
                "name": "試験・シミュレーション",
                "icon": "🎮",
                "desc": "デジタルツイン・作戦訓練・試験評価",
                "roles": [
                    {"label": "シミュレータ", "codes": ["CAE", "LMT", "BA", "7011"]},
                    {"label": "極超音速・新技術", "codes": ["KTOS", "RTX"]},
                ],
            },
        ],
    },
    {
        "key": "procure",
        "name": "② 調達・契約",
        "icon": "📋",
        "color": "#D4AC0D",
        "desc": "政府調達(FMS/直接契約)・多国間共同開発・長期サプライ契約。国防予算の配分が株価の先行指標。",
        "visual": "contract",
        "steps": [
            {
                "name": "政府調達・Prime契約",
                "icon": "🏛️",
                "desc": "主要防衛契約者との大型調達",
                "roles": [
                    {"label": "米国プライム", "codes": ["LMT", "RTX", "NOC", "GD", "BA", "HII"]},
                    {"label": "日本防衛三社", "codes": ["7011", "7012", "7013"]},
                ],
            },
            {
                "name": "C4ISR・サイバー調達",
                "icon": "🛡️",
                "desc": "指揮統制・通信・サイバー防衛",
                "roles": [
                    {"label": "米国IT防衛", "codes": ["LDOS", "SAIC", "CACI", "PLTR"]},
                    {"label": "日本システム", "codes": ["6701", "6702", "9692", "4687"]},
                ],
            },
            {
                "name": "国際連携・商社",
                "icon": "🤝",
                "desc": "FMS・技術移転・装備輸出",
                "roles": [
                    {"label": "商社・連携", "codes": ["8058", "8002", "2768"]},
                    {"label": "F-35共同開発", "codes": ["LMT", "7011", "7013"]},
                ],
            },
        ],
    },
    {
        "key": "mfg",
        "name": "③ 製造・統合",
        "icon": "🏭",
        "color": "#4A6FA5",
        "desc": "プラットフォーム組立・ミサイル・電子機器・材料部品の統合。F-35のような国際分散生産が典型。",
        "visual": "factory",
        "steps": [
            {
                "name": "プラットフォーム組立",
                "icon": "✈️",
                "desc": "戦闘機・艦艇・地上車両の製造",
                "roles": [
                    {"label": "航空", "codes": ["LMT", "NOC", "BA", "7011", "7012"]},
                    {"label": "艦艇", "codes": ["HII", "GD", "7011", "7012"]},
                    {"label": "地上", "codes": ["GD", "OSK", "6301", "6208"]},
                ],
            },
            {
                "name": "ミサイル・弾薬",
                "icon": "🚀",
                "desc": "誘導兵器・推進剤・火工品",
                "roles": [
                    {"label": "ミサイル", "codes": ["RTX", "LMT", "NOC", "7011"]},
                    {"label": "火工品・原料", "codes": ["4272", "4025", "4045", "6366"]},
                ],
            },
            {
                "name": "電子・UAS・宇宙",
                "icon": "📡",
                "desc": "レーダー・通信・無人機・衛星",
                "roles": [
                    {"label": "電子・EW", "codes": ["LHX", "RTX", "MRCY", "6503", "6701"]},
                    {"label": "UAS", "codes": ["AVAV", "KTOS", "TXT", "7011"]},
                    {"label": "宇宙", "codes": ["RKLB", "BKSY", "7013", "LMT"]},
                ],
            },
            {
                "name": "材料・F-35サプライチェーン",
                "icon": "⚙️",
                "desc": "チタン・複合材・精密部品",
                "roles": [
                    {"label": "米国材料", "codes": ["HWM", "HXL", "CRS", "ATI", "HEI", "TDG"]},
                    {"label": "日本部品", "codes": ["6324", "6479", "6345", "6807", "5727", "3401"]},
                ],
            },
        ],
    },
    {
        "key": "deploy",
        "name": "④ 配備・作戦展開",
        "icon": "🌍",
        "color": "#C0392B",
        "desc": "基地建設・輸送・初期展開・衛星運用。地政学リスクが高まるほど配備関連需要が増加。",
        "visual": "deploy",
        "steps": [
            {
                "name": "基地・インフラ建設",
                "icon": "🏗️",
                "desc": "防衛施設・通信インフラ・電力",
                "roles": [
                    {"label": "建設・EPC", "codes": ["1414", "1951", "1950", "6330"]},
                    {"label": "物流", "codes": ["KBR", "6383"]},
                ],
            },
            {
                "name": "通信・衛星運用",
                "icon": "🛰️",
                "desc": "作戦通信・ISR衛星・宇宙防衛",
                "roles": [
                    {"label": "衛星通信", "codes": ["IRDM", "VSAT", "LHX", "6701"]},
                    {"label": "ISR", "codes": ["BKSY", "NOC", "LMT"]},
                ],
            },
            {
                "name": "無人機作戦展開",
                "icon": "🛸",
                "desc": "偵察・攻撃UASの前线配備",
                "roles": [
                    {"label": "UAS", "codes": ["AVAV", "KTOS", "NOC", "7011"]},
                ],
            },
        ],
    },
    {
        "key": "sustain",
        "name": "⑤ サステインメント(MRO)",
        "icon": "🔧",
        "color": "#6B8E4E",
        "desc": "整備・部品供給・寿命周期管理・継続訓練。装備の半分以上のコストがここで発生。",
        "visual": "maintain",
        "steps": [
            {
                "name": "MRO・部品供給",
                "icon": "🔩",
                "desc": "航空機・艦艇の定期整備と部品",
                "roles": [
                    {"label": "MRO", "codes": ["HEI", "TDG", "WWD", "7011", "7012"]},
                    {"label": "精密部品", "codes": ["6471", "6473", "6479", "6324"]},
                ],
            },
            {
                "name": "IT支援・サイバー維持",
                "icon": "💻",
                "desc": "システム更新・サイバー防衛運用",
                "roles": [
                    {"label": "防衛IT", "codes": ["LDOS", "SAIC", "6702", "9692"]},
                ],
            },
            {
                "name": "訓練・人材・ETF",
                "icon": "📈",
                "desc": "継続訓練と国防予算ベータ",
                "roles": [
                    {"label": "訓練", "codes": ["CAE", "BAH", "7011"]},
                    {"label": "防衛ETF", "codes": ["ITA", "XAR", "PPA", "SHLD", "DFEN"]},
                ],
            },
        ],
    },
]


def resolve_flow(all_symbols):
    """銘柄コードを{code,name,market}に解決してフロントに渡す形にする"""
    out = []
    for stage in FLOW:
        st = {
            "key": stage["key"],
            "name": stage["name"],
            "icon": stage["icon"],
            "color": stage["color"],
            "desc": stage["desc"],
            "visual": stage.get("visual"),
            "steps": [],
        }
        for step in stage["steps"]:
            roles = []
            for role in step["roles"]:
                items = []
                for code in role["codes"]:
                    if code in all_symbols:
                        nm, mkt = all_symbols[code]
                        items.append({"code": code, "name": nm, "market": mkt})
                if items:
                    roles.append({"label": role["label"], "items": items})
            st["steps"].append({
                "name": step["name"],
                "icon": step["icon"],
                "desc": step["desc"],
                "roles": roles,
                "visual": step.get("visual"),
            })
        out.append(st)
    return out

# ===== v3 追加ステップ (2026-07-08) =====
_V3_FLOW_STEPS = {
    "mfg": [
        {
            "name": "無人機・空モビリティ",
            "icon": "🛩️",
            "desc": "UAS/UUV・eVTOLの開発製造",
            "roles": [
                {"label": "米国UAS", "codes": ["AVAV", "KTOS", "RCAT", "ONDS"]},
                {"label": "国産ドローン", "codes": ["6232", "278A", "218A"]},
                {"label": "eVTOL", "codes": ["ACHR", "JOBY"]},
            ],
        },
        {
            "name": "火工品・陸上装備",
            "icon": "🧨",
            "desc": "火薬・弾薬部材・小銃・特装車",
            "roles": [
                {"label": "火工品", "codes": ["4274", "4275", "4272", "6208"]},
                {"label": "火砲・特機", "codes": ["5631", "6203", "7224"]},
            ],
        },
    ],
    "deploy": [
        {
            "name": "サイバー防衛",
            "icon": "🔐",
            "desc": "ネットワーク防護・ゼロトラスト・監視",
            "roles": [
                {"label": "グローバル", "codes": ["CRWD", "PANW", "FTNT", "ZS"]},
                {"label": "国内セキュリティ", "codes": ["4704", "3692", "4288"]},
            ],
        },
    ],
    "sustain": [
        {
            "name": "防護装備・商社",
            "icon": "🧤",
            "desc": "個人防護具・装備品商流・後方支援",
            "roles": [
                {"label": "防護装備", "codes": ["7963", "7980"]},
                {"label": "防衛商社", "codes": ["8001", "8020", "8031", "8053"]},
            ],
        },
    ],
}
for _st in FLOW:
    _st["steps"].extend(_V3_FLOW_STEPS.get(_st["key"], []))
