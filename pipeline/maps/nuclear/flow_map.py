# -*- coding: utf-8 -*-
"""
フロービジュアル定義: 原子力の4ステージ
① 燃料サイクル(Fuel)
② 建設(Construction)
③ 運転(Operation)
④ 廃炉(Decommission)

各ステージ = {key, name, icon, color, desc, visual, steps:[...]}
"""

FLOW = [
    {
        "key": "fuel",
        "name": "① 燃料サイクル(Fuel)",
        "icon": "☢️",
        "color": "#9D7CF0",
        "desc": "ウラン採掘→濃縮→燃料加工→使用→再処理。原子力の川上。",
        "visual": "cycle",
        "steps": [
            {
                "name": "ウラン採掘・資源",
                "icon": "⛏️",
                "desc": "カザフスタン・カナダ等のウラン鉱山",
                "roles": [
                    {"label": "鉱山(米)", "codes": ["CCJ", "UEC", "UUUU", "DNN", "NXE", "URG"]},
                    {"label": "日本", "codes": ["5713"]},
                    {"label": "ETF", "codes": ["URA", "NLR", "URNM"]},
                ],
            },
            {
                "name": "濃縮・燃料加工",
                "icon": "🧪",
                "desc": "ウラン濃縮と燃料ペレット製造",
                "roles": [
                    {"label": "濃縮(米)", "codes": ["LEU", "BWXT"]},
                    {"label": "日本", "codes": ["4005"]},
                ],
            },
            {
                "name": "再処理・後処理",
                "icon": "♻️",
                "desc": "使用済み燃料の再処理・廃棄物管理",
                "roles": [
                    {"label": "施設", "codes": ["6330", "1963", "BWXT"]},
                ],
            },
        ],
    },
    {
        "key": "build",
        "name": "② 建設(Construction)",
        "icon": "🏗️",
        "color": "#E8B04B",
        "desc": "原子炉設計・EPC・圧力容器。新設とSMRが焦点。",
        "visual": "build",
        "steps": [
            {
                "name": "原子炉設計",
                "icon": "📐",
                "desc": "BWR/PWR/APWR/SMR等の炉型設計",
                "roles": [
                    {"label": "日本", "codes": ["6501", "6502", "7011", "6330"]},
                    {"label": "SMR(米)", "codes": ["SMR", "OKLO", "NNE"]},
                ],
            },
            {
                "name": "EPC・建設",
                "icon": "🏗️",
                "desc": "原子力プラント建設請負",
                "roles": [
                    {"label": "EPC(日)", "codes": ["7011", "1963", "6330", "1801", "1721"]},
                    {"label": "設備(米)", "codes": ["BWXT", "GEV"]},
                ],
            },
            {
                "name": "圧力容器・土木",
                "icon": "⚙️",
                "desc": "原子炉容器・耐震基礎",
                "roles": [
                    {"label": "容器・材料", "codes": ["5631", "5713", "1801"]},
                ],
            },
        ],
    },
    {
        "key": "operate",
        "name": "③ 運転(Operation)",
        "icon": "⚡",
        "color": "#3FA7D6",
        "desc": "原子力発電所の運転・保守・再稼働。脱炭素の基荷電源。",
        "visual": "operate",
        "steps": [
            {
                "name": "原子力保有電力",
                "icon": "⚡",
                "desc": "原子力発電所を保有する電力会社",
                "roles": [
                    {"label": "関東", "codes": ["9501"]},
                    {"label": "関西・中部", "codes": ["9503", "9502"]},
                    {"label": "その他(日)", "codes": ["9508", "9506", "9504", "9507", "9509"]},
                    {"label": "米国", "codes": ["CEG", "VST", "EXC", "DUK", "SO"]},
                ],
            },
            {
                "name": "発電・計装設備",
                "icon": "🎛️",
                "desc": "タービン・I&C・ポンプ等の原子力設備",
                "roles": [
                    {"label": "タービン", "codes": ["7011", "6501", "6361", "6504", "GEV"]},
                    {"label": "計装・制御", "codes": ["6841", "6502", "6951", "BWXT"]},
                    {"label": "配管・ポンプ", "codes": ["6490", "6407", "1963"]},
                ],
            },
            {
                "name": "SMR・次世代炉",
                "icon": "🔬",
                "desc": "小型モジュール炉・ナトリウム炉等",
                "roles": [
                    {"label": "SMR(米)", "codes": ["SMR", "OKLO", "NNE", "BWXT"]},
                    {"label": "SMR(日)", "codes": ["7011", "6501", "6502", "6330"]},
                ],
            },
        ],
    },
    {
        "key": "decom",
        "name": "④ 廃炉(Decommission)",
        "icon": "♻️",
        "color": "#8FA0B8",
        "desc": "使用済み炉の停止・解体・放射性廃棄物管理。",
        "visual": "decom",
        "steps": [
            {
                "name": "廃炉・解体",
                "icon": "🔧",
                "desc": "原子炉の停止・解体・除染",
                "roles": [
                    {"label": "廃炉(日)", "codes": ["6501", "6502", "7011", "6301"]},
                    {"label": "廃炉(米)", "codes": ["BWXT"]},
                ],
            },
            {
                "name": "放射性廃棄物",
                "icon": "📦",
                "desc": "低・中・高レベル廃棄物の管理・処理",
                "roles": [
                    {"label": "処理施設", "codes": ["1721", "1963", "5713", "5802"]},
                ],
            },
            {
                "name": "政策・ETF",
                "icon": "📋",
                "desc": "再稼働政策・脱炭素連動・指数",
                "roles": [
                    {"label": "政策受益者", "codes": ["9503", "6501", "5802"]},
                    {"label": "ETF", "codes": ["URA", "NLR", "CEG", "VST"]},
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
