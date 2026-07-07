# -*- coding: utf-8 -*-
"""
原子力 工程マップ定義（燃料｜建設｜運転｜廃炉 の4カラム対比）
各工程: {"stage","name","desc","equip":[codes],"material":[codes]}
  stage: fuel/build/operate/decom
"""

ALIAS = {}

PROCESS_MAP = [
    {
        "stage": "fuel",
        "name": "核燃料サイクル",
        "icon": "☢️",
        "desc": "ウラン採掘から燃料製造・再処理まで",
        "groups": [
            {"label": "ウラン採掘", "stocks": ["CCJ", "UEC", "UUUU", "DNN", "NXE", "5713"]},
            {"label": "濃縮・変換", "stocks": ["LEU", "4005"]},
            {"label": "燃料加工", "stocks": ["BWXT", "6330", "1963"]},
        ],
    },
    {
        "stage": "build",
        "name": "① 原子炉設計・ライセンス",
        "icon": "📐",
        "desc": "炉型設計・安全審査・ライセンス取得",
        "equip": ["6501", "6502", "7011", "6330", "SMR", "OKLO", "NNE"],
        "material": [],
    },
    {
        "stage": "build",
        "name": "② 建設・EPC",
        "icon": "🏗️",
        "desc": "原子力プラント建設請負",
        "equip": ["7011", "1963", "6330", "1801", "1721", "BWXT", "GEV"],
        "material": ["5631"],
    },
    {
        "stage": "build",
        "name": "③ 圧力容器・土木",
        "icon": "⚙️",
        "desc": "原子炉容器・耐震基礎・配管",
        "equip": ["5631", "1801", "5713", "1963"],
        "material": [],
    },
    {
        "stage": "operate",
        "name": "④ 発電・運転",
        "icon": "⚡",
        "desc": "原子力発電所の運転・電力販売",
        "equip": ["9501", "9502", "9503", "9508", "9506", "9504", "9507", "9509", "CEG", "VST", "EXC"],
        "material": [],
    },
    {
        "stage": "operate",
        "name": "⑤ タービン・発電設備",
        "icon": "🔧",
        "desc": "原子炉熱を電力に変換",
        "equip": ["7011", "6501", "6361", "6504", "GEV"],
        "material": [],
    },
    {
        "stage": "operate",
        "name": "⑥ 計装・制御(I&C)",
        "icon": "🎛️",
        "desc": "原子炉の監視・制御・安全系",
        "equip": ["6841", "6502", "6501", "6951", "BWXT"],
        "material": [],
    },
    {
        "stage": "operate",
        "name": "⑦ 保守・O&M",
        "icon": "🔩",
        "desc": "定期点検・部品交換・寿命延長",
        "equip": ["6501", "6361", "6841", "6490", "6407", "1963"],
        "material": [],
    },
    {
        "stage": "decom",
        "name": "⑧ 廃炉・解体",
        "icon": "♻️",
        "desc": "使用済み炉の停止・解体",
        "equip": ["6501", "6502", "7011", "6301", "BWXT"],
        "material": [],
    },
    {
        "stage": "decom",
        "name": "⑨ 放射性廃棄物",
        "icon": "📦",
        "desc": "低・中・高レベル廃棄物の管理",
        "equip": ["1721", "1963", "5713", "5802"],
        "material": [],
    },
    {
        "stage": "operate",
        "name": "◆ SMR・次世代炉",
        "icon": "🔬",
        "desc": "小型モジュール炉・次世代炉開発",
        "equip": ["SMR", "OKLO", "NNE", "7011", "6501", "6502", "6330", "BWXT"],
        "material": [],
    },
]
