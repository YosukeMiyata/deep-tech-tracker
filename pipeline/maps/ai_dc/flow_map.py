# -*- coding: utf-8 -*-
"""
フロービジュアル定義: AIデータセンター 5ステージ(氷山概念)
① GPU層(海面の上)
② ストレージ層
③ ネットワーク層
④ 電源層
⑤ 冷却層(海面下の土台)

各ステージ = {key, name, icon, color, desc, visual, steps:[...]}
各工程(step) = {name, icon, desc, roles:[{label, codes:[...]}], visual(任意)}
"""

FLOW = [
    {
        "key": "gpu",
        "name": "① GPU層(海面の上)",
        "icon": "⛰️",
        "color": "#5BE39B",
        "desc": "AIの「顔」。投資家の目が最も集まるCapExの起点。GPU/ASIC→AIサーバー→Pod統合。",
        "visual": "surface",
        "steps": [
            {
                "name": "GPU・AIアクセラレータ",
                "icon": "🧠",
                "desc": "NVIDIA/AMD GPU、ハイパースケーラー自社ASIC",
                "roles": [
                    {"label": "GPU", "codes": ["NVDA", "AMD"]},
                    {"label": "カスタムASIC", "codes": ["AVGO", "MRVL", "GOOGL", "META", "AMZN", "MSFT"]},
                ],
            },
            {
                "name": "AIサーバーOEM",
                "icon": "🖥️",
                "desc": "GPU搭載ラックサーバー・ストレージ一体型",
                "roles": [
                    {"label": "サーバーOEM", "codes": ["SMCI", "DELL", "HPE", "HPQ"]},
                    {"label": "ストレージ一体", "codes": ["PSTG", "NTAP", "WDC"]},
                ],
            },
            {
                "name": "AI Pod・ラック統合",
                "icon": "📦",
                "desc": "GB200 NVL72等。GPU+ネットワーク+電源+冷却の一体Pod",
                "roles": [
                    {"label": "Pod統合", "codes": ["NVDA", "SMCI", "VRT"]},
                    {"label": "日本連動", "codes": ["6501", "6702"]},
                ],
            },
        ],
    },
    {
        "key": "storage",
        "name": "② ストレージ層(記憶)",
        "icon": "📚",
        "color": "#F0593C",
        "desc": "GPUへデータを供給する「食材倉庫」。HBM→DRAM→SSD/HDDの階層構造。",
        "visual": "layers",
        "steps": [
            {
                "name": "HBM・高帯域メモリ",
                "icon": "🔥",
                "desc": "GPU直結メモリ。CapEx増加の先行指標(需要側視点)",
                "roles": [
                    {"label": "HBM/DRAM", "codes": ["MU", "SNDK"]},
                    {"label": "GPU需要", "codes": ["NVDA", "AMD"]},
                ],
            },
            {
                "name": "DRAM・CXL",
                "icon": "💾",
                "desc": "ホストメモリ拡張・CXLメモリプール",
                "roles": [
                    {"label": "DRAM", "codes": ["MU", "WDC"]},
                    {"label": "CXL/DPU", "codes": ["ALAB", "AMD", "INTC"]},
                ],
            },
            {
                "name": "SSD・HDD・AIストレージ",
                "icon": "🗄️",
                "desc": "学習データセット・チェックポイント保存",
                "roles": [
                    {"label": "フラッシュ/SSD", "codes": ["WDC", "SNDK", "PSTG", "NTAP"]},
                    {"label": "HDD(ニアライン)", "codes": ["STX", "WDC"]},
                    {"label": "日本NAND", "codes": ["285A", "6526"]},
                ],
            },
        ],
    },
    {
        "key": "network",
        "name": "③ ネットワーク層(神経網)",
        "icon": "🕸️",
        "color": "#3FA7D6",
        "desc": "数千GPUをAll-to-All接続。スイッチ→光→CPOの3段階で帯域と電力効率を両立。",
        "visual": "mesh",
        "steps": [
            {
                "name": "スイッチ・DPU",
                "icon": "🔀",
                "desc": "400G/800Gスパインリーフ・SmartNIC",
                "roles": [
                    {"label": "スイッチ", "codes": ["ANET", "CSCO", "AVGO", "JNPR"]},
                    {"label": "DPU/CXL", "codes": ["ALAB", "CRDO", "MRVL", "NVDA", "AMD"]},
                ],
            },
            {
                "name": "光接続(CPO/トランシーバ)",
                "icon": "🌈",
                "desc": "電気→光変換。CPOでラック内電力を削減",
                "roles": [
                    {"label": "CPO/光IC", "codes": ["AVGO", "MRVL", "COHR", "LITE", "MTSI"]},
                    {"label": "光トランシーバ", "codes": ["LITE", "COHR", "AAOI", "CIEN", "FN"]},
                    {"label": "日本光部品", "codes": ["5803", "5801", "4062", "9432"]},
                ],
            },
            {
                "name": "光ファイバー・配線",
                "icon": "🧵",
                "desc": "DC内・DC間の高密度光配線",
                "roles": [
                    {"label": "光ファイバー", "codes": ["GLW", "5803", "5801", "5802"]},
                    {"label": "コネクタ・配線", "codes": ["APH", "TEL", "BDC", "6834", "6703"]},
                ],
            },
        ],
    },
    {
        "key": "power",
        "name": "④ 電源層(心臓)",
        "icon": "⚡",
        "color": "#F0A85B",
        "desc": "1GPU=数百W〜kW級。MW級受配電→UPS→ラックPSU→銅配線。PUE改善の主戦場。",
        "visual": "power",
        "steps": [
            {
                "name": "受配電・変圧器",
                "icon": "🏭",
                "desc": "グリッドからDCへのMW級電力供給",
                "roles": [
                    {"label": "変圧器・受配電", "codes": ["GEV", "ETN", "POWL", "HUBB", "BE"]},
                    {"label": "日本変圧器", "codes": ["6622", "6501", "6504", "6503"]},
                ],
            },
            {
                "name": "UPS・ラック電源",
                "icon": "🔋",
                "desc": "停電対策・高効率PSU",
                "roles": [
                    {"label": "UPS/電源", "codes": ["VRT", "ETN", "MPWR"]},
                    {"label": "日本電源", "codes": ["6504", "6707", "6674"]},
                ],
            },
            {
                "name": "銅配線・母線",
                "icon": "🔗",
                "desc": "GPUラック間の大電流配線。銅需要の構造的増",
                "roles": [
                    {"label": "配線・コネクタ", "codes": ["APH", "MLI", "BDC", "FCX", "COPX"]},
                    {"label": "日本銅・ケーブル", "codes": ["5801", "5803", "5706", "5016", "5802", "5805"]},
                ],
            },
        ],
    },
    {
        "key": "cooling",
        "name": "⑤ 冷却層(海面下・土台)",
        "icon": "🧊",
        "color": "#6EE7F0",
        "desc": "AIの正体は巨大な氷山。GPUの熱暴走を防ぐ生命維持装置。液冷→浸漬→空冷のハイブリッド。",
        "visual": "iceberg",
        "steps": [
            {
                "name": "液冷・CDU",
                "icon": "💧",
                "desc": "ラック内ダイレクト液冷・CDU(冷却液分配)",
                "roles": [
                    {"label": "液冷/CDU", "codes": ["VRT", "MOD", "SMCI", "NVT", "TT"]},
                    {"label": "日本液冷", "codes": ["6367", "6584", "6516", "6490"]},
                ],
            },
            {
                "name": "浸漬・ダイレクト液冷",
                "icon": "🌊",
                "desc": "浸漬冷却・負圧式液冷など次世代方式",
                "roles": [
                    {"label": "浸漬/液冷", "codes": ["VRT", "MOD", "CARR"]},
                    {"label": "日本液冷", "codes": ["6367", "6490"]},
                ],
            },
            {
                "name": "CRAC/空調・排熱",
                "icon": "❄️",
                "desc": "施設全体の空調・冷却塔・ポンプ",
                "roles": [
                    {"label": "空調/HVAC", "codes": ["CARR", "TT", "JCI", "FIX"]},
                    {"label": "日本空調・ポンプ", "codes": ["6458", "1969", "6363", "6594"]},
                ],
            },
            {
                "name": "DC建設・CapEx(土台)",
                "icon": "🏗️",
                "desc": "冷却を含む施設全体のCapExサイクル",
                "roles": [
                    {"label": "建設・電気工事", "codes": ["PWR", "FIX", "IESC", "EME", "MYRG"]},
                    {"label": "REIT・コロ", "codes": ["EQIX", "DLR", "AMT", "CCI"]},
                    {"label": "日本建設", "codes": ["1942", "1944", "1961", "6366"]},
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
            st["steps"].append(
                {
                    "name": step["name"],
                    "icon": step["icon"],
                    "desc": step["desc"],
                    "roles": roles,
                    "visual": step.get("visual"),
                }
            )
        out.append(st)
    return out
