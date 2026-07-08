# -*- coding: utf-8 -*-
"""
宇宙 工程マップ定義（打ち上げ｜軌道｜地上 の3カラム対比）
各工程: {"stage","name","desc","equip":[codes],"material":[codes]}
  stage: launch/orbit/ground/service
"""

ALIAS = {}

PROCESS_MAP = [
    {
        "stage": "launch",
        "name": "打ち上げ事業者",
        "icon": "🚀",
        "desc": "ロケットでペイロードを宇宙へ運ぶ主体",
        "groups": [
            {"label": "商用再利用", "stocks": ["RKLB", "SPCE"]},
            {"label": "政府・大型", "stocks": ["LMT", "BA", "NOC"]},
            {"label": "日本", "stocks": ["7011", "7012"]},
        ],
    },
    {
        "stage": "launch",
        "name": "① 推進・エンジン",
        "icon": "🔥",
        "desc": "ロケットを加速させる推進系",
        "equip": ["7011", "7012", "LMT", "NOC", "BA", "BWXT"],
        "material": ["3407", "4204", "HXL"],
    },
    {
        "stage": "launch",
        "name": "② 構造・分離機構",
        "icon": "🔩",
        "desc": "フェアリング・段間分離・耐熱",
        "equip": ["TDG", "ATRO", "HON", "6103"],
        "material": ["HXL", "3407"],
    },
    {
        "stage": "orbit",
        "name": "③ 衛星製造・バス",
        "icon": "🛰️",
        "desc": "衛星本体(バス)とペイロードの製造",
        "equip": ["LHX", "BA", "NOC", "RTX", "LMT", "KTOS", "6701", "6702", "6503"],
        "material": ["6779", "6962", "6724", "HEI"],
    },
    {
        "stage": "orbit",
        "name": "④ 通信・観測ペイロード",
        "icon": "📡",
        "desc": "通信・地球観測・レーダー等のミッション機器",
        "equip": ["IRDM", "SATS", "GSAT", "ASTS", "VSAT", "PL", "BKSY", "SPIR", "SATL", "9412"],
        "material": ["402A", "AMZN"],
    },
    {
        "stage": "orbit",
        "name": "⑤ 防衛衛星・早期警戒",
        "icon": "🛡️",
        "desc": "軍事衛星・ミサイル防衛・SSA",
        "equip": ["LMT", "RTX", "NOC", "LHX", "LDOS", "7011"],
        "material": [],
    },
    {
        "stage": "ground",
        "name": "⑥ 地上局・衛星通信",
        "icon": "📶",
        "desc": "衛星と地上を繋ぐアンテナ・通信網",
        "equip": ["GILT", "VSAT", "IRDM", "KTOS", "9432", "6701"],
        "material": [],
    },
    {
        "stage": "ground",
        "name": "⑦ データ分析・サービス",
        "icon": "📊",
        "desc": "衛星データの加工・配信・分析",
        "equip": ["PL", "BKSY", "SPIR", "RDW", "402A"],
        "material": [],
    },
    {
        "stage": "service",
        "name": "⑧ 軌道上サービス",
        "icon": "🔧",
        "desc": "軌道上製造・輸送・デブリ対策",
        "equip": ["RDW", "RKLB", "LUNR", "ASTS", "464A"],
        "material": [],
    },
    {
        "stage": "service",
        "name": "⑨ 探査・深宇宙",
        "icon": "🌙",
        "desc": "月面・火星・深宇宙ミッション",
        "equip": ["BA", "LMT", "LUNR", "464A", "7011"],
        "material": [],
    },
]

# ===== v3 追加工程 (2026-07-08) =====
PROCESS_MAP.extend([
    {
        "stage": "launch",
        "name": "ロケット材料・部品(日本)",
        "icon": "🧱",
        "desc": "チタン・炭素繊維・慣性センサ・宇宙用コネクタ",
        "equip": ["7721", "6807", "6965"],
        "material": ["5726", "3402", "3401"],
    },
    {
        "stage": "orbit",
        "name": "新興衛星・軌道上サービス",
        "icon": "🛰️",
        "desc": "SAR衛星・デブリ除去・月輸送の新興勢",
        "equip": ["9348", "464A", "186A", "290A", "VOYG", "KRMN", "FLY"],
        "material": [],
    },
    {
        "stage": "service",
        "name": "衛星データ利用",
        "icon": "🗺️",
        "desc": "衛星画像解析・気象・地理空間情報",
        "equip": ["2667", "4825", "PL", "BKSY"],
        "material": [],
    },
])
