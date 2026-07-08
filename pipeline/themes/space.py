# -*- coding: utf-8 -*-
"""
宇宙テーマトラッカー — 銘柄マスタ
マクロテーマ → サブテーマ → 米国株 / 連動日本株 / 日本単独テーマ。

★ ここだけ編集すれば銘柄・テーマを足せる ★
  us  : [シンボル, 表示名]            (米国: ティッカー)
  jp  : [証券コード, 表示名, 連動理由]  (連動日本株)
  solo: [証券コード, 表示名, 内容]      (日本単独テーマ)
"""

MACRO = [
    {
        "key": "launch",
        "name": "ロケット・打ち上げ",
        "color": "#6B5CE7",
        "subs": [
            {
                "name": "再利用ロケット",
                "us": [
                    ["RKLB", "Rocket Lab"],
                    ["BA", "Boeing"],
                ],
                "jp": [
                    ["7011", "三菱重工業", "H3ロケット・打ち上げサービス"],
                    ["7012", "川崎重工業", "ロケットエンジン部品・構造"],
                ],
                "solo": [],
            },
            {
                "name": "政府・大型打ち上げ",
                "us": [
                    ["LMT", "Lockheed Martin"],
                    ["NOC", "Northrop Grumman"],
                    ["BA", "Boeing"],
                ],
                "jp": [
                    ["7011", "三菱重工業", "H3・大型ロケット共同開発"],
                    ["7012", "川崎重工業", "第一級エンジン部品"],
                ],
                "solo": [],
            },
            {
                "name": "打ち上げインフラ・整備",
                "us": [
                    ["RKLB", "Rocket Lab"],
                    ["SPCE", "Virgin Galactic"],
                    ["KTOS", "Kratos Defense"],
                    ["AIR", "AAR Corp"],
                    ["MNTS", "Momentus"],
                ],
                "jp": [
                    ["6103", "オーヴァル", "打ち上げ関連精密部品"],
                    ["6728", "アルバック", "宇宙試験用真空装置"],
                ],
                "solo": [
                    ["7011", "三菱重工業", "種子島・打ち上げ場インフラ"],
                ],
            },
        ],
    },
    {
        "key": "satellites",
        "name": "衛星製造・運用",
        "color": "#8B7CF6",
        "subs": [
            {
                "name": "通信衛星・コンステレーション",
                "us": [
                    ["IRDM", "Iridium"],
                    ["SATS", "EchoStar"],
                    ["GSAT", "Globalstar"],
                    ["ASTS", "AST SpaceMobile"],
                    ["VSAT", "Viasat"],
                    ["AMZN", "Amazon(Kuiper)"],
                    ["GOOGL", "Alphabet"],
                    ["SES", "SES SA"],
                ],
                "jp": [
                    ["9412", "スカパーJSAT", "衛星放送・通信衛星運用"],
                    ["9432", "NTT", "衛星通信・準天頂連携"],
                    ["9433", "KDDI", "衛星通信・IoT"],
                ],
                "solo": [],
            },
            {
                "name": "地球観測・レーダー",
                "us": [
                    ["PL", "Planet Labs"],
                    ["BKSY", "BlackSky"],
                    ["SPIR", "Spire Global"],
                    ["SATL", "Satellogic"],
                ],
                "jp": [
                    ["402A", "スペースシフト", "SAR衛星・地球観測"],
                ],
                "solo": [],
            },
            {
                "name": "衛星製造・システム",
                "us": [
                    ["LHX", "L3Harris"],
                    ["BA", "Boeing"],
                    ["NOC", "Northrop Grumman"],
                    ["RTX", "RTX"],
                    ["LMT", "Lockheed Martin"],
                    ["KTOS", "Kratos Defense"],
                    ["TXT", "Textron"],
                ],
                "jp": [
                    ["6701", "NEC", "衛星バス・地上システム"],
                    ["6702", "富士通", "衛星搭載コンピュータ"],
                    ["6503", "三菱電機", "衛星通信・観測ペイロード"],
                    ["6501", "日立製作所", "衛星関連システム"],
                ],
                "solo": [],
            },
        ],
    },
    {
        "key": "ground",
        "name": "地上局・サービス",
        "color": "#5B9BD5",
        "subs": [
            {
                "name": "地上局・衛星通信",
                "us": [
                    ["GILT", "Gilat Satellite"],
                    ["VSAT", "Viasat"],
                    ["IRDM", "Iridium"],
                    ["KTOS", "Kratos Defense"],
                    ["ESE", "ESCO Technologies"],
                ],
                "jp": [
                    ["9432", "NTT", "衛星通信インフラ"],
                    ["6701", "NEC", "地上局システム"],
                    ["6806", "ヒロセ電機", "衛星用コネクタ"],
                ],
                "solo": [],
            },
            {
                "name": "衛星データ・分析",
                "us": [
                    ["PL", "Planet Labs"],
                    ["BKSY", "BlackSky"],
                    ["SPIR", "Spire Global"],
                    ["RDW", "Redwire"],
                    ["PLTR", "Palantir"],
                    ["CACI", "CACI International"],
                ],
                "jp": [
                    ["402A", "スペースシフト", "衛星データ活用"],
                ],
                "solo": [],
            },
        ],
    },
    {
        "key": "components",
        "name": "宇宙部品・材料",
        "color": "#4ECDC4",
        "subs": [
            {
                "name": "推進・エンジン",
                "us": [
                    ["LMT", "Lockheed Martin"],
                    ["NOC", "Northrop Grumman"],
                    ["BA", "Boeing"],
                    ["BWXT", "BWX Technologies"],
                ],
                "jp": [
                    ["7011", "三菱重工業", "ロケットエンジン"],
                    ["7012", "川崎重工業", "エンジン部品・タービン"],
                ],
                "solo": [],
            },
            {
                "name": "構造材料・複合材",
                "us": [
                    ["TDG", "TransDigm"],
                    ["HXL", "Hexcel"],
                    ["ATRO", "Astronics"],
                    ["HON", "Honeywell"],
                    ["WWD", "Woodward"],
                    ["PSN", "Parsons"],
                ],
                "jp": [
                    ["3407", "旭化成", "炭素繊維・複合材"],
                    ["4204", "積水化学工業", "宇宙向け樹脂・シール"],
                    ["6988", "日東電工", "宇宙向け粘着テープ"],
                ],
                "solo": [],
            },
            {
                "name": "宇宙エレクトロニクス・部品",
                "us": [
                    ["HEI", "HEICO"],
                    ["TDG", "TransDigm"],
                    ["HON", "Honeywell"],
                    ["GE", "GE Aerospace"],
                    ["MOG-A", "Moog"],
                    ["HWM", "Howmet Aerospace"],
                ],
                "jp": [
                    ["6779", "日本電波工業", "水晶デバイス・衛星用発振器"],
                    ["6962", "大真空", "水晶振動子・衛星用"],
                    ["6724", "セイコーエプソン", "GNSS用タイミングデバイス"],
                    ["6103", "オーヴァル", "衛星用精密部品"],
                    ["7912", "大日本印刷", "衛星用電子部材"],
                    ["6504", "富士電機", "衛星電源・インバータ"],
                ],
                "solo": [],
            },
        ],
    },
    {
        "key": "defense_space",
        "name": "防衛宇宙",
        "color": "#4A7C59",
        "subs": [
            {
                "name": "ミサイル防衛・早期警戒",
                "us": [
                    ["LMT", "Lockheed Martin"],
                    ["RTX", "RTX"],
                    ["NOC", "Northrop Grumman"],
                    ["LDOS", "Leidos"],
                    ["BAH", "Booz Allen Hamilton"],
                    ["SAIC", "SAIC"],
                ],
                "jp": [
                    ["7011", "三菱重工業", "弾道ミサイル防衛"],
                    ["6504", "富士電機", "早期警戒レーダー"],
                ],
                "solo": [],
            },
            {
                "name": "軍事衛星・ペイロード",
                "us": [
                    ["LHX", "L3Harris"],
                    ["LMT", "Lockheed Martin"],
                    ["NOC", "Northrop Grumman"],
                    ["BA", "Boeing"],
                    ["RTX", "RTX"],
                ],
                "jp": [
                    ["6701", "NEC", "防衛衛星システム"],
                    ["6503", "三菱電機", "防衛衛星ペイロード"],
                ],
                "solo": [],
            },
        ],
    },
    {
        "key": "commercial",
        "name": "商用宇宙サービス",
        "color": "#E8B04B",
        "subs": [
            {
                "name": "サブオービタル・宇宙観光",
                "us": [
                    ["SPCE", "Virgin Galactic"],
                    ["RKLB", "Rocket Lab"],
                    ["AVAV", "AeroVironment"],
                ],
                "jp": [],
                "solo": [],
            },
            {
                "name": "軌道上サービス・製造",
                "us": [
                    ["RDW", "Redwire"],
                    ["RKLB", "Rocket Lab"],
                    ["ASTS", "AST SpaceMobile"],
                    ["SIDU", "Sidus Space"],
                ],
                "jp": [
                    ["6103", "オーヴァル", "軌道上製造向け部品"],
                ],
                "solo": [],
            },
            {
                "name": "宇宙輸送・物流",
                "us": [
                    ["LUNR", "Intuitive Machines"],
                    ["RDW", "Redwire"],
                    ["RKLB", "Rocket Lab"],
                ],
                "jp": [
                    ["9348", "ispace", "月面輸送・着陸"],
                ],
                "solo": [],
            },
        ],
    },
    {
        "key": "exploration",
        "name": "探査・深宇宙",
        "color": "#9D7CF0",
        "subs": [
            {
                "name": "月面・Artemis/NASA",
                "us": [
                    ["BA", "Boeing"],
                    ["LMT", "Lockheed Martin"],
                    ["LUNR", "Intuitive Machines"],
                    ["RKLB", "Rocket Lab"],
                ],
                "jp": [
                    ["9348", "ispace", "月面着陸ミッション"],
                ],
                "solo": [],
            },
            {
                "name": "深宇宙・火星探査",
                "us": [
                    ["BA", "Boeing"],
                    ["LMT", "Lockheed Martin"],
                    ["NOC", "Northrop Grumman"],
                ],
                "jp": [],
                "solo": [
                    ["9348", "ispace", "深宇宙探査ビジョン"],
                    ["7011", "三菱重工業", "HTV-X・宇宙ステーション"],
                ],
            },
        ],
    },
    {
        "key": "policy",
        "name": "規制・政策",
        "color": "#A8B89F",
        "subs": [
            {
                "name": "宇宙ETF・指数",
                "us": [
                    ["UFO", "Procure Space ETF"],
                    ["ARKX", "ARK Space ETF"],
                    ["ROKT", "SPDR S&P Kensho Final Frontiers"],
                ],
                "jp": [],
                "solo": [],
            },
            {
                "name": "軌道デブリ・宇宙規制",
                "us": [
                    ["LHX", "L3Harris"],
                    ["LDOS", "Leidos"],
                    ["PL", "Planet Labs"],
                ],
                "jp": [],
                "solo": [
                    ["402A", "スペースシフト", "デブリ監視SAR"],
                ],
            },
        ],
    },
    {
        "key": "japan_space",
        "name": "日本宇宙産業",
        "color": "#F08CC0",
        "subs": [
            {
                "name": "H3・打ち上げ",
                "us": [],
                "jp": [],
                "solo": [
                    ["7011", "三菱重工業", "H3ロケット・JAXA打ち上げ"],
                    ["7012", "川崎重工業", "LE-9エンジン"],
                ],
            },
            {
                "name": "準天頂・衛星通信",
                "us": [],
                "jp": [],
                "solo": [
                    ["9412", "スカパーJSAT", "衛星放送・通信"],
                    ["9432", "NTT", "準天頂衛星システム(QZSS)"],
                    ["9434", "ソフトバンク", "衛星通信・宇宙事業"],
                    ["6723", "ルネサス", "宇宙向け耐放射線半導体"],
                    ["6334", "明治電機工業", "航空宇宙用モーター"],
                ],
            },
            {
                "name": "宇宙スタートアップ・新興",
                "us": [],
                "jp": [],
                "solo": [
                    ["9348", "ispace", "月面探査"],
                    ["402A", "スペースシフト", "SAR衛星"],
                    ["6103", "オーヴァル", "衛星部品"],
                    ["6724", "セイコーエプソン", "GNSSタイミング"],
                    ["5801", "古河電工", "宇宙用ケーブル・光ファイバ"],
                    ["7911", "TOPPAN", "衛星用フォトマスク"],
                ],
            },
            {
                "name": "地上試験・真空・計測",
                "us": [
                    ["BRKR", "Bruker"],
                    ["KEYS", "Keysight"],
                ],
                "jp": [
                    ["6728", "アルバック", "宇宙試験用真空"],
                    ["6841", "横河電機", "衛星試験計測"],
                ],
                "solo": [
                    ["6754", "アンリツ", "衛星通信試験"],
                ],
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

# =====================================================================
# ★ v3 追加 (2026-07-08) — 宇宙セクター拡充
#   新興宇宙(日本)/衛星データ利用/宇宙材料・部品(日本)/新興宇宙(米国)
#   注意: 新しい銘柄コード(464A, 186A, 290A等)は特に update_prices.py での検証必須
# =====================================================================
_V3_NEW_SUBS = {
    "japan_space": [
        {
            "name": "新興宇宙(日本)",
            "us": [],
            "jp": [],
            "solo": [
                ["9348", "ispace", "月着陸船・月輸送サービス"],
                ["464A", "QPSホールディングス", "小型SAR衛星コンステレーション(旧QPS研究所)"],
                ["186A", "アストロスケールHD", "スペースデブリ除去・軌道上サービス"],
                ["290A", "Synspective", "小型SAR衛星・解析サービス"],
            ],
        },
        {
            "name": "衛星データ利用(日本)",
            "us": [],
            "jp": [],
            "solo": [
                ["2667", "イメージ・ワン", "衛星画像販売・GEOソリューション"],
                ["4825", "ウェザーニューズ", "気象衛星データ活用・民間気象最大手"],
            ],
        },
    ],
    "components": [
        {
            "name": "宇宙材料・部品(日本)",
            "us": [],
            "jp": [
                ["5726", "大阪チタニウム", "ロケット・航空機向けスポンジチタン"],
                ["3402", "東レ", "ロケット・衛星向け炭素繊維"],
                ["3401", "帝人", "アラミド・炭素繊維(宇宙防衛用途)"],
                ["7721", "東京計器", "ジャイロ・慣性センサ"],
                ["6807", "日本航空電子工業", "宇宙用コネクタ・慣性計測"],
                ["6965", "浜松ホトニクス", "宇宙用光センサ・イメージセンサ"],
            ],
            "solo": [],
        },
    ],
    "commercial": [
        {
            "name": "新興宇宙(米国)",
            "us": [["VOYG", "Voyager Technologies"], ["KRMN", "Karman Holdings"], ["FLY", "Firefly Aerospace"]],
            "jp": [],
            "solo": [],
        },
    ],
}
for _m in MACRO:
    _m["subs"].extend(_V3_NEW_SUBS.get(_m["key"], []))