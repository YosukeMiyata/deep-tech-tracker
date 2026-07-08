# -*- coding: utf-8 -*-
"""
フロービジュアル定義: 宇宙産業の4ステージ
① 打ち上げ(Launch)
② 軌道(Satellites)
③ 地上(Ground)
④ サービス・探査(Services)

各ステージ = {key, name, icon, color, desc, visual, steps:[...]}
"""

FLOW = [
    {
        "key": "launch",
        "name": "① 打ち上げ(Launch)",
        "icon": "🚀",
        "color": "#6B5CE7",
        "desc": "ロケットでペイロードを宇宙へ。再利用化でコスト革命が進行中。",
        "visual": "rocket",
        "steps": [
            {
                "name": "再利用ロケット",
                "icon": "♻️",
                "desc": "Electron/Neutron等、回収・再使用で打ち上げコスト低減",
                "roles": [
                    {"label": "打ち上げ", "codes": ["RKLB", "SPCE"]},
                    {"label": "日本連動", "codes": ["7011", "7012"]},
                ],
            },
            {
                "name": "政府・大型打ち上げ",
                "icon": "🏛️",
                "desc": "SLS/Artemis/Vulcan等、大型ペイロード・国家プロジェクト",
                "roles": [
                    {"label": "プライム", "codes": ["LMT", "BA", "NOC"]},
                    {"label": "日本", "codes": ["7011", "7012"]},
                ],
            },
            {
                "name": "推進・構造部品",
                "icon": "🔥",
                "desc": "エンジン・フェアリング・分離機構",
                "roles": [
                    {"label": "推進", "codes": ["LMT", "NOC", "BA", "BWXT", "7011", "7012"]},
                    {"label": "構造・材料", "codes": ["TDG", "HXL", "ATRO", "HON", "3407", "4204"]},
                ],
            },
        ],
    },
    {
        "key": "orbit",
        "name": "② 軌道(Satellites)",
        "icon": "🛰️",
        "color": "#8B7CF6",
        "desc": "LEO/MEO/GEO軌道上の衛星。通信・観測・防衛が3大用途。",
        "visual": "orbit",
        "steps": [
            {
                "name": "通信衛星・コンステレーション",
                "icon": "📡",
                "desc": "Starlink/Kuiper/Iridium等、低軌道大量衛星",
                "roles": [
                    {"label": "衛星運用", "codes": ["IRDM", "SATS", "GSAT", "ASTS", "VSAT", "AMZN"]},
                    {"label": "日本", "codes": ["9412", "9432"]},
                ],
            },
            {
                "name": "地球観測・レーダー",
                "icon": "🌍",
                "desc": "光学/SAR衛星で地球を常時監視",
                "roles": [
                    {"label": "観測衛星", "codes": ["PL", "BKSY", "SPIR", "SATL"]},
                    {"label": "日本", "codes": ["402A"]},
                ],
            },
            {
                "name": "衛星製造・防衛",
                "icon": "🏭",
                "desc": "衛星バス製造と軍事衛星",
                "roles": [
                    {"label": "製造(米)", "codes": ["LHX", "BA", "NOC", "RTX", "LMT", "KTOS"]},
                    {"label": "製造(日)", "codes": ["6701", "6702", "6503"]},
                    {"label": "防衛", "codes": ["LMT", "RTX", "LDOS", "6502", "7011"]},
                ],
            },
        ],
    },
    {
        "key": "ground",
        "name": "③ 地上(Ground)",
        "icon": "📶",
        "color": "#5B9BD5",
        "desc": "衛星とユーザーを繋ぐ地上局・通信網・データ分析。",
        "visual": "ground",
        "steps": [
            {
                "name": "地上局・衛星通信",
                "icon": "📡",
                "desc": "アンテナ・地上局ネットワーク",
                "roles": [
                    {"label": "地上局", "codes": ["GILT", "VSAT", "IRDM", "KTOS"]},
                    {"label": "日本", "codes": ["9432", "6701"]},
                ],
            },
            {
                "name": "衛星データ・分析",
                "icon": "📊",
                "desc": "画像・気象・船舶データの加工配信",
                "roles": [
                    {"label": "データ", "codes": ["PL", "BKSY", "SPIR", "RDW"]},
                    {"label": "日本", "codes": ["402A"]},
                ],
            },
        ],
    },
    {
        "key": "service",
        "name": "④ サービス・探査",
        "icon": "🌙",
        "color": "#E8B04B",
        "desc": "軌道上サービス、月面探査、商用宇宙の新領域。",
        "visual": "explore",
        "steps": [
            {
                "name": "軌道上サービス",
                "icon": "🔧",
                "desc": "軌道上製造・輸送・デブリ対策",
                "roles": [
                    {"label": "サービス", "codes": ["RDW", "RKLB", "ASTS", "LUNR"]},
                    {"label": "部品", "codes": ["6103", "6779", "6962", "6724", "HEI"]},
                ],
            },
            {
                "name": "月面・深宇宙探査",
                "icon": "🌙",
                "desc": "Artemis/月面着陸/火星探査",
                "roles": [
                    {"label": "探査(米)", "codes": ["BA", "LMT", "LUNR", "NOC"]},
                    {"label": "探査(日)", "codes": ["9348", "7011"]},
                ],
            },
            {
                "name": "日本宇宙産業",
                "icon": "🇯🇵",
                "desc": "H3・準天頂・宇宙スタートアップ",
                "roles": [
                    {"label": "打ち上げ", "codes": ["7011", "7012"]},
                    {"label": "通信", "codes": ["9412", "9432", "9434"]},
                    {"label": "新興", "codes": ["9348", "402A", "6103", "6724"]},
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
