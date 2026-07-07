# -*- coding: utf-8 -*-
"""
防衛 工程マップ定義（装備｜材料 の2カラム対比）
防衛バリューチェーン: R&D → 調達 → 製造 → 配備 → サステインメント

各工程: {"stage","name","icon","desc","equip":[codes],"material":[codes]}
  または groups: [{"label","stocks":[codes]}]
  stage: rd / procure / mfg / deploy / sustain
"""

ALIAS = {}

PROCESS_MAP = [
    {
        "stage": "rd",
        "name": "防衛産業の主体",
        "icon": "🏛️",
        "desc": "プラットフォーム統合・主要契約者(Prime)",
        "groups": [
            {"label": "米国プライム", "stocks": ["LMT", "RTX", "NOC", "GD", "BA", "HII", "LHX"]},
            {"label": "日本防衛三社", "stocks": ["7011", "7012", "7013"]},
        ],
    },
    {
        "stage": "rd",
        "name": "① 研究開発(R&D)",
        "icon": "🔬",
        "desc": "新装備の概念設計・試作・技術開発",
        "equip": ["3636", "LDOS", "SAIC", "PLTR", "KTOS", "CAE"],
        "material": ["6965", "6758", "6235"],
    },
    {
        "stage": "rd",
        "name": "② 試験・シミュレーション",
        "icon": "🎯",
        "desc": "デジタルツイン・訓練・作戦シミュレーション",
        "equip": ["CAE", "LMT", "BA", "7011"],
        "material": ["3636"],
    },
    {
        "stage": "procure",
        "name": "③ 調達・契約",
        "icon": "📋",
        "desc": "政府調達・長期契約・国際共同開発",
        "equip": ["BAH", "LDOS", "KBR", "8058", "8002", "2768"],
        "material": [],
    },
    {
        "stage": "procure",
        "name": "④ C4ISR・サイバー基盤",
        "icon": "🛡️",
        "desc": "指揮統制・通信・サイバー防衛システム",
        "equip": ["LDOS", "SAIC", "CACI", "PLTR", "6701", "6702", "9692"],
        "material": ["3774"],
    },
    {
        "stage": "mfg",
        "name": "⑤ プラットフォーム製造",
        "icon": "✈️",
        "desc": "戦闘機・艦艇・車両の組立",
        "equip": ["LMT", "NOC", "BA", "GD", "HII", "7011", "7012", "6301", "OSK"],
        "material": ["SPR", "HEI", "TDG"],
    },
    {
        "stage": "mfg",
        "name": "⑥ ミサイル・弾薬製造",
        "icon": "🚀",
        "desc": "誘導兵器・推進剤・火工品",
        "equip": ["RTX", "LMT", "NOC", "7011", "7013"],
        "material": ["4272", "4025", "4045"],
    },
    {
        "stage": "mfg",
        "name": "⑦ 電子・センサー製造",
        "icon": "📡",
        "desc": "レーダー・通信・EO/IR・電子戦",
        "equip": ["LHX", "RTX", "MRCY", "DRS", "6503", "6701", "6807"],
        "material": ["6965", "6758", "7711"],
    },
    {
        "stage": "mfg",
        "name": "⑧ 無人機・宇宙システム",
        "icon": "🛸",
        "desc": "UAS/UUV・衛星・ロケット",
        "equip": ["AVAV", "KTOS", "NOC", "RKLB", "BKSY", "7013", "7011"],
        "material": ["6335", "4021"],
    },
    {
        "stage": "mfg",
        "name": "⑨ 材料・部品(サプライチェーン)",
        "icon": "⚙️",
        "desc": "チタン・複合材・精密部品・F-35連携",
        "equip": ["6324", "6479", "6471", "6345", "5932"],
        "material": ["HWM", "HXL", "CRS", "ATI", "5727", "5726", "3401", "5480", "5471"],
    },
    {
        "stage": "deploy",
        "name": "⑩ 配備・展開",
        "icon": "🌍",
        "desc": "基地建設・輸送・初期展開",
        "equip": ["KBR", "LDOS", "1414", "1951", "1950", "6330"],
        "material": ["6383"],
    },
    {
        "stage": "deploy",
        "name": "⑪ 宇宙・衛星運用",
        "icon": "🛰️",
        "desc": "ISR衛星・通信衛星・宇宙防衛",
        "equip": ["LMT", "NOC", "LHX", "IRDM", "VSAT", "BKSY"],
        "material": [],
    },
    {
        "stage": "sustain",
        "name": "⑫ MRO・サステインメント",
        "icon": "🔧",
        "desc": "整備・部品供給・寿命周期管理",
        "equip": ["HEI", "TDG", "WWD", "7011", "7012", "LDOS", "SAIC"],
        "material": ["6473", "6471"],
    },
    {
        "stage": "sustain",
        "name": "⑬ 後方支援・訓練",
        "icon": "📚",
        "desc": "継続的訓練・シミュレータ・人材支援",
        "equip": ["CAE", "BAH", "KBR", "7011", "3636"],
        "material": [],
    },
    {
        "stage": "sustain",
        "name": "◆ 防衛ETF・政策連動",
        "icon": "📈",
        "desc": "国防予算・地政学リスクのベータ",
        "equip": ["ITA", "XAR", "PPA", "SHLD", "DFEN", "2561", "2562"],
        "material": [],
    },
]
