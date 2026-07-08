# -*- coding: utf-8 -*-
"""
AIデータセンター 工程マップ定義（設備｜運用 の2カラム対比)
DCバリューチェーン: 設計 → 建設 → 電源/冷却 → ネットワーク → 運用

各工程: {"stage","name","desc","equip":[codes],"material":[codes]}
  または groups: [{"label","stocks":[codes]}]
  stage: design / build / power / network / operate
"""

ALIAS = {}

PROCESS_MAP = [
    {
        "stage": "design",
        "name": "AI DCの主体",
        "icon": "🏛️",
        "desc": "CapExを決めるハイパースケーラー・GPUクラウド・REIT",
        "groups": [
            {"label": "ハイパースケーラー", "stocks": ["AMZN", "MSFT", "GOOGL", "META", "ORCL"]},
            {"label": "GPUクラウド", "stocks": ["CRWV", "NBIS", "IREN", "CORZ"]},
            {"label": "DC REIT", "stocks": ["EQIX", "DLR", "AMT", "CCI"]},
        ],
    },
    {
        "stage": "design",
        "name": "① 設計・アーキテクチャ",
        "icon": "✏️",
        "desc": "GPU/サーバー構成・PUE目標・液冷/空冷選定",
        "equip": ["NVDA", "SMCI", "VRT", "ANET", "ALAB"],
        "material": ["6526", "6702", "6701"],
    },
    {
        "stage": "design",
        "name": "② AI Pod・ラック設計",
        "icon": "🖥️",
        "desc": "GB200 NVL72等のラックスケールAI Pod",
        "equip": ["NVDA", "SMCI", "DELL", "HPE", "VRT"],
        "material": ["6501", "6622"],
    },
    {
        "stage": "build",
        "name": "③ DC建設・電気工事",
        "icon": "🏗️",
        "desc": "サイト選定・建物・電気配線・接地",
        "equip": ["PWR", "FIX", "IESC", "EME", "MYRG"],
        "material": ["1942", "1944", "1961", "6366"],
    },
    {
        "stage": "build",
        "name": "④ サーバー・ストレージ導入",
        "icon": "📦",
        "desc": "GPUサーバー・JBOD/JBOF・AI向けストレージ",
        "equip": ["SMCI", "DELL", "HPE", "P", "NTAP", "WDC", "STX"],
        "material": ["285A", "6526"],
    },
    {
        "stage": "power",
        "name": "⑤ 受配電・変圧器",
        "icon": "⚡",
        "desc": "MW級電力をDCへ供給する受配電設備",
        "equip": ["GEV", "ETN", "POWL", "HUBB", "BE"],
        "material": ["6622", "6501", "6504", "6503"],
    },
    {
        "stage": "power",
        "name": "⑥ UPS・ラック電源",
        "icon": "🔋",
        "desc": "停電対策・高効率PSU・SiC/GaN電源",
        "equip": ["VRT", "ETN", "MPWR", "6707"],
        "material": ["6674", "6504"],
    },
    {
        "stage": "power",
        "name": "⑦ 銅配線・母線",
        "icon": "🔗",
        "desc": "GPUラック間の大電流配線・バスバー",
        "equip": ["APH", "MLI", "BDC", "FCX"],
        "material": ["5801", "5803", "5706", "5016", "5802", "5805"],
    },
    {
        "stage": "power",
        "name": "⑧ 冷却・液冷(CDU)",
        "icon": "❄️",
        "desc": "kW/GPU級の排熱。液冷・浸漬・空冷のハイブリッド",
        "equip": ["VRT", "MOD", "CARR", "TT", "JCI", "NVT"],
        "material": ["6367", "6584", "6516", "6458", "1969", "6363", "6490"],
    },
    {
        "stage": "network",
        "name": "⑨ スイッチ・DPU",
        "icon": "🕸️",
        "desc": "400G/800Gスイッチ・SmartNIC・CXL",
        "equip": ["ANET", "CSCO", "AVGO", "ALAB", "CRDO", "MRVL", "NVDA"],
        "material": ["6702", "6701"],
    },
    {
        "stage": "network",
        "name": "⑩ 光接続(CPO/トランシーバ)",
        "icon": "🌈",
        "desc": "ラック間・スパインリーフの光相互接続",
        "equip": ["LITE", "COHR", "AAOI", "CIEN", "AVGO", "MRVL", "MTSI"],
        "material": ["5803", "5801", "5802", "GLW", "6703", "4062", "9432"],
    },
    {
        "stage": "network",
        "name": "⑪ 光ファイバー・配線",
        "icon": "🧵",
        "desc": "DC内・DC間の高密度光配線",
        "equip": ["GLW", "COMM", "TEL", "APH"],
        "material": ["5803", "5801", "5802", "6834"],
    },
    {
        "stage": "operate",
        "name": "⑫ DC運営・コロ",
        "icon": "🏢",
        "desc": "コロケーション・GPUクラウド運用",
        "equip": ["EQIX", "DLR", "CRWV", "NBIS", "3778", "3774"],
        "material": ["3905", "9432"],
    },
    {
        "stage": "operate",
        "name": "◆ GPU・メモリ(需要ドライバ)",
        "icon": "🧠",
        "desc": "CapExサイクルの起点。HBM/DRAM/SSD需要",
        "equip": ["NVDA", "AMD", "MU", "AVGO"],
        "material": ["285A"],
    },
    {
        "stage": "operate",
        "name": "◆ エッジAI展開",
        "icon": "📡",
        "desc": "クラウド推論の延長。MEC・エッジサーバー",
        "equip": ["QCOM", "ARM", "HPE", "DELL", "ERIC", "NOK"],
        "material": ["6723", "6701", "9432"],
    },
]
