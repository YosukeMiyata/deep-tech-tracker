# -*- coding: utf-8 -*-
"""
AIデータセンターテーマトラッカー — 銘柄マスタ
DCインフラ視点: GPU需要・サーバー・ネットワーク・光接続・冷却・電源・CapExサイクル。
半導体製造装置(SPE)・ウェハー工程は semi セクター側。ここは需要/施設/運用に焦点。

★ ここだけ編集すれば銘柄・テーマを足せる ★
  us  : [シンボル, 表示名]            (米国: ティッカー)
  jp  : [証券コード, 表示名, 連動理由]  (連動日本株)
  solo: [証券コード, 表示名, 内容]      (日本単独テーマ: 米国に明確な対応なし/日本が高シェア)
"""

MACRO = [
    {
        "key": "gpu_accel",
        "name": "GPU・アクセラレータ",
        "color": "#5BE39B",
        "subs": [
            {
                "name": "GPU・AIアクセラレータ",
                "us": [
                    ["NVDA", "NVIDIA"],
                    ["AMD", "AMD"],
                    ["ARM", "Arm"],
                ],
                "jp": [
                    ["6857", "アドバンテスト", "AI GPU向けテスト需要(半導体側連動)"],
                ],
                "solo": [],
            },
            {
                "name": "カスタムASIC・XPU",
                "us": [
                    ["AVGO", "Broadcom"],
                    ["MRVL", "Marvell"],
                    ["GOOGL", "Alphabet"],
                    ["META", "Meta"],
                    ["AMZN", "Amazon"],
                    ["MSFT", "Microsoft"],
                    ["INTC", "Intel"],
                ],
                "jp": [
                    ["6526", "ソシオネクスト", "北米DC向けカスタムSoC設計"],
                ],
                "solo": [],
            },
            {
                "name": "AI半導体・DC連動ETF",
                "us": [
                    ["SMH", "VanEck半導体ETF"],
                    ["SOXX", "iShares半導体ETF"],
                    ["BOTZ", "Global Xロボティクス&AI ETF"],
                    ["IGV", "iSharesソフトウェアETF"],
                ],
                "jp": [],
                "solo": [
                    ["200A", "グローバルX 半導体関連-日本株式ETF"],
                ],
            },
        ],
    },
    {
        "key": "server_oem",
        "name": "サーバー・OEM",
        "color": "#7CC8F0",
        "subs": [
            {
                "name": "AIサーバーOEM",
                "us": [
                    ["SMCI", "Super Micro"],
                    ["DELL", "Dell Technologies"],
                    ["HPE", "Hewlett Packard Enterprise"],
                    ["HPQ", "HP Inc"],
                    ["NTAP", "NetApp"],
                ],
                "jp": [],
                "solo": [],
            },
            {
                "name": "ODM・白箱サーバー",
                "us": [
                    ["WDC", "Western Digital"],
                    ["STX", "Seagate"],
                    ["NTNX", "Nutanix"],
                ],
                "jp": [
                    ["6702", "富士通", "AI向けサーバー・PRIMERGY"],
                    ["6701", "NEC", "AIサーバー・DC向けシステム"],
                ],
                "solo": [],
            },
            {
                "name": "ラック統合・AI Pod",
                "us": [
                    ["VRT", "Vertiv"],
                    ["SMCI", "Super Micro"],
                    ["ETN", "Eaton"],
                    ["NVDA", "NVIDIA"],
                    ["NTNX", "Nutanix"],
                ],
                "jp": [
                    ["6501", "日立製作所", "日立エナジー(ラック電源・HVDC)"],
                ],
                "solo": [],
            },
        ],
    },
    {
        "key": "networking",
        "name": "DCネットワーク",
        "color": "#3FA7D6",
        "subs": [
            {
                "name": "データセンタースイッチ",
                "us": [
                    ["ANET", "Arista Networks"],
                    ["CSCO", "Cisco"],
                    ["AVGO", "Broadcom"],
                    ["HPE", "HPE(旧Juniper)"],
                    ["CIEN", "Ciena"],
                    ["FFIV", "F5 Networks"],
                ],
                "jp": [
                    ["6702", "富士通", "DC向けネットワーク機器"],
                    ["6701", "NEC", "Open RAN・DCスイッチ"],
                ],
                "solo": [],
            },
            {
                "name": "SmartNIC/DPU/CXL",
                "us": [
                    ["ALAB", "Astera Labs"],
                    ["CRDO", "Credo Technology"],
                    ["MRVL", "Marvell"],
                    ["AMD", "AMD"],
                    ["NVDA", "NVIDIA"],
                    ["INTC", "Intel"],
                ],
                "jp": [],
                "solo": [],
            },
            {
                "name": "DC間接続(DCI)",
                "us": [
                    ["CIEN", "Ciena"],
                    ["GLW", "Corning"],
                    ["FN", "Fabrinet"],
                    ["LITE", "Lumentum"],
                    ["COHR", "Coherent"],
                ],
                "jp": [
                    ["6701", "NEC", "DC間光伝送・DCI"],
                    ["6702", "富士通", "DC間ネットワーク"],
                    ["5803", "フジクラ", "DC間光ファイバー"],
                ],
                "solo": [],
            },
            {
                "name": "DC配線・コネクタ",
                "us": [
                    ["APH", "Amphenol"],
                    ["TEL", "TE Connectivity"],
                    ["BDC", "Belden"],
                    ["GLW", "Corning"],
                ],
                "jp": [
                    ["5802", "住友電工", "DC向け電力・光ケーブル"],
                    ["5805", "SWCC", "電力ケーブル・DC配線"],
                    ["6834", "精工技研", "光コネクタ・DC光配線"],
                ],
                "solo": [],
            },
        ],
    },
    {
        "key": "optical_dc",
        "name": "光接続(DC向け)",
        "color": "#E8B04B",
        "subs": [
            {
                "name": "CPO・光スイッチ",
                "us": [
                    ["AVGO", "Broadcom"],
                    ["MRVL", "Marvell"],
                    ["COHR", "Coherent"],
                    ["LITE", "Lumentum"],
                    ["MTSI", "MACOM"],
                ],
                "jp": [
                    ["9432", "NTT", "IOWN・DC光電融合"],
                    ["4062", "イビデン", "光電融合パッケージ基板"],
                ],
                "solo": [],
            },
            {
                "name": "光トランシーバ",
                "us": [
                    ["LITE", "Lumentum"],
                    ["COHR", "Coherent"],
                    ["AAOI", "Applied Optoelectronics"],
                    ["CIEN", "Ciena"],
                    ["FN", "Fabrinet"],
                ],
                "jp": [
                    ["6702", "富士通", "光トランシーバ・光伝送"],
                    ["6777", "santec HD", "光部品・波長可変光源"],
                ],
                "solo": [],
            },
            {
                "name": "光ファイバー・ケーブル",
                "us": [
                    ["GLW", "Corning"],
                    ["TEL", "TE Connectivity"],
                ],
                "jp": [
                    ["5803", "フジクラ", "高密度光ファイバー・DC配線"],
                    ["5801", "古河電工", "多芯光ファイバー・DC光配線"],
                    ["5802", "住友電工", "光ファイバー・融着接続"],
                    ["6703", "OKI", "光通信インフラ"],
                ],
                "solo": [],
            },
        ],
    },
    {
        "key": "cooling",
        "name": "冷却・熱管理",
        "color": "#6EE7F0",
        "subs": [
            {
                "name": "液冷・CDU",
                "us": [
                    ["VRT", "Vertiv"],
                    ["MOD", "Modine"],
                    ["SMCI", "Super Micro"],
                    ["NVT", "nVent"],
                    ["TT", "Trane Technologies"],
                ],
                "jp": [
                    ["6367", "ダイキン工業", "Chilldyne買収・負圧式液冷"],
                    ["6584", "三桜工業", "液体冷却配管・CDU部品"],
                    ["6516", "山洋電気", "液冷ポンプ・ファン"],
                ],
                "solo": [],
            },
            {
                "name": "浸漬・ダイレクト液冷",
                "us": [
                    ["VRT", "Vertiv"],
                    ["MOD", "Modine"],
                    ["CARR", "Carrier"],
                ],
                "jp": [
                    ["6367", "ダイキン工業", "液冷・浸漬冷却"],
                    ["6490", "日本ピラー工業", "冷却配管シール・継手"],
                ],
                "solo": [],
            },
            {
                "name": "CRAC/空調・排熱",
                "us": [
                    ["CARR", "Carrier"],
                    ["TT", "Trane Technologies"],
                    ["JCI", "Johnson Controls"],
                    ["FIX", "Comfort Systems"],
                ],
                "jp": [
                    ["6458", "新晃工業", "大型空調機・DC空調増産"],
                    ["1969", "高砂熱学工業", "DC空調・冷却設備工事"],
                    ["6363", "酉島製作所", "冷却水循環ポンプ"],
                    ["6594", "ニデック", "冷却ファン・精密モーター"],
                ],
                "solo": [],
            },
        ],
    },
    {
        "key": "power_dc",
        "name": "DC電源・配電",
        "color": "#F0A85B",
        "subs": [
            {
                "name": "UPS・ラック電源",
                "us": [
                    ["VRT", "Vertiv"],
                    ["ETN", "Eaton"],
                    ["GEV", "GE Vernova"],
                    ["BE", "Bloom Energy"],
                    ["MPWR", "Monolithic Power"],
                ],
                "jp": [
                    ["6504", "富士電機", "UPS・受配電・DC電源"],
                    ["6707", "サンケン電気", "高効率電源・DC向け"],
                    ["6674", "GSユアサ", "大容量UPS・蓄電池"],
                ],
                "solo": [],
            },
            {
                "name": "変圧器・受配電",
                "us": [
                    ["POWL", "Powell Industries"],
                    ["GEV", "GE Vernova"],
                    ["ETN", "Eaton"],
                    ["HUBB", "Hubbell"],
                ],
                "jp": [
                    ["6622", "ダイヘン", "変圧器・受配電(北米DC向け急拡)"],
                    ["6501", "日立製作所", "日立エナジー(変圧器・HVDC)"],
                    ["6503", "三菱電機", "受配電・SiCパワー"],
                    ["6504", "富士電機", "変圧器・UPS"],
                ],
                "solo": [],
            },
            {
                "name": "銅配線・母線",
                "us": [
                    ["APH", "Amphenol"],
                    ["MLI", "Mueller Industries"],
                    ["BDC", "Belden"],
                    ["FCX", "Freeport-McMoRan"],
                    ["COPX", "Global X 銅ETF"],
                ],
                "jp": [
                    ["5801", "古河電工", "銅線・DC配線"],
                    ["5803", "フジクラ", "銅線・電力ケーブル"],
                    ["5706", "三井金属", "極薄電解銅箔・DC配線"],
                    ["5016", "JX金属", "銅製錬・DC配線材料"],
                ],
                "solo": [],
            },
        ],
    },
    {
        "key": "memory_ai",
        "name": "AI向けメモリ",
        "color": "#F0593C",
        "subs": [
            {
                "name": "HBM・高帯域メモリ(需要側)",
                "us": [
                    ["MU", "Micron"],
                    ["NVDA", "NVIDIA"],
                    ["AMD", "AMD"],
                ],
                "jp": [
                    ["285A", "キオクシア", "AI向けSSD・NAND(メモリ階層)"],
                ],
                "solo": [],
            },
            {
                "name": "DRAM・CXLメモリ",
                "us": [
                    ["MU", "Micron"],
                    ["SNDK", "SanDisk"],
                    ["WDC", "Western Digital"],
                ],
                "jp": [],
                "solo": [],
            },
            {
                "name": "SSD・HDD・ストレージ",
                "us": [
                    ["WDC", "Western Digital"],
                    ["STX", "Seagate"],
                    ["SNDK", "SanDisk"],
                    ["NTAP", "NetApp"],
                ],
                "jp": [
                    ["285A", "キオクシア", "AI向けSSD・NAND"],
                    ["6526", "ソシオネクスト", "ストレージコントローラ設計"],
                ],
                "solo": [],
            },
        ],
    },
    {
        "key": "cloud",
        "name": "クラウド・ハイパースケーラー",
        "color": "#9D7CF0",
        "subs": [
            {
                "name": "ハイパースケーラー",
                "us": [
                    ["AMZN", "Amazon"],
                    ["MSFT", "Microsoft"],
                    ["GOOGL", "Alphabet"],
                    ["META", "Meta"],
                    ["ORCL", "Oracle"],
                    ["CRM", "Salesforce"],
                ],
                "jp": [],
                "solo": [],
            },
            {
                "name": "GPUクラウド・Neocloud",
                "us": [
                    ["CRWV", "CoreWeave"],
                    ["NBIS", "Nebius"],
                    ["IREN", "IREN(旧Iris Energy)"],
                    ["CORZ", "Core Scientific"],
                    ["APLD", "Applied Digital"],
                ],
                "jp": [],
                "solo": [],
            },
            {
                "name": "国内DC・クラウド",
                "us": [],
                "jp": [
                    ["3778", "さくらインターネット", "GPUクラウド・政府クラウド"],
                    ["3774", "IIJ", "DC運営・クラウド"],
                    ["3905", "データセクション", "AI・DC関連"],
                    ["9432", "NTT", "DC・IOWN・国内クラウド"],
                ],
                "solo": [],
            },
        ],
    },
    {
        "key": "edge_ai",
        "name": "エッジAI",
        "color": "#8FA0B8",
        "subs": [
            {
                "name": "エッジ推論SoC",
                "us": [
                    ["QCOM", "Qualcomm"],
                    ["ARM", "Arm"],
                    ["INTC", "Intel"],
                    ["NVDA", "NVIDIA"],
                    ["AMD", "AMD"],
                ],
                "jp": [
                    ["6723", "ルネサス", "エッジAI MCU・SoC"],
                ],
                "solo": [],
            },
            {
                "name": "エッジサーバー・ゲートウェイ",
                "us": [
                    ["HPE", "Hewlett Packard Enterprise"],
                    ["DELL", "Dell Technologies"],
                    ["CSCO", "Cisco"],
                    ["ANET", "Arista Networks"],
                ],
                "jp": [
                    ["6702", "富士通", "エッジAIサーバー"],
                    ["6701", "NEC", "エッジコンピューティング"],
                ],
                "solo": [],
            },
            {
                "name": "MEC・5Gエッジ",
                "us": [
                    ["ERIC", "Ericsson"],
                    ["NOK", "Nokia"],
                    ["CSCO", "Cisco"],
                    ["QCOM", "Qualcomm"],
                ],
                "jp": [
                    ["9432", "NTT", "5G MEC・エッジDC"],
                    ["6701", "NEC", "Open RAN・MEC"],
                ],
                "solo": [],
            },
        ],
    },
    {
        "key": "capex_cycle",
        "name": "CapExサイクル",
        "color": "#A8B89F",
        "subs": [
            {
                "name": "DC REIT・コロケーション",
                "us": [
                    ["EQIX", "Equinix"],
                    ["DLR", "Digital Realty"],
                    ["AMT", "American Tower"],
                    ["CCI", "Crown Castle"],
                    ["IRM", "Iron Mountain"],
                ],
                "jp": [],
                "solo": [],
            },
            {
                "name": "DC建設・電気工事",
                "us": [
                    ["PWR", "Quanta Services"],
                    ["FIX", "Comfort Systems"],
                    ["IESC", "IES Holdings"],
                    ["EME", "EMCOR Group"],
                    ["MYRG", "MYR Group"],
                ],
                "jp": [
                    ["1942", "関電工", "電気工事・DC建設"],
                    ["1944", "きんでん", "電気工事・DC建設"],
                    ["1961", "三機工業", "空調・電気設備工事"],
                    ["6366", "千代田化工建設", "DC EPC・プラント"],
                ],
                "solo": [],
            },
            {
                "name": "CapExサイクル・ETF",
                "us": [
                    ["XLRE", "Real Estate Select Sector ETF"],
                    ["VNQ", "Vanguard REIT ETF"],
                    ["SRVR", "Pacer Data & Infrastructure ETF"],
                    ["DTCR", "Global X Data Center ETF"],
                ],
                "jp": [],
                "solo": [
                    ["1343", "NEXT FUNDS 東証REIT ETF"],
                ],
            },
            {
                "name": "DC運用・監視",
                "us": [
                    ["DDOG", "Datadog"],
                    ["NET", "Cloudflare"],
                    ["AKAM", "Akamai"],
                    ["SNOW", "Snowflake"],
                    ["MDB", "MongoDB"],
                ],
                "jp": [
                    ["4689", "Zホールディングス", "クラウド・AI基盤"],
                    ["4751", "サイバーエージェント", "AI/DCワークロード"],
                ],
                "solo": [],
            },
        ],
    },
]


def all_symbols():
    """全ユニーク銘柄を {sym: (name, market)} で返す。"""
    out = {}
    for m in MACRO:
        for sub in m["subs"]:
            for s, n in sub["us"]:
                out[s] = (n, "us")
            for row in sub["jp"]:
                out[row[0]] = (row[1], "jp")
            for row in sub["solo"]:
                out[row[0]] = (row[1], "jp")
    return out
