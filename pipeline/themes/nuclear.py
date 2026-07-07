# -*- coding: utf-8 -*-
"""
原子力電力テーマトラッカー — 銘柄マスタ
マクロテーマ → サブテーマ → 米国株 / 連動日本株 / 日本単独テーマ。

★ ここだけ編集すれば銘柄・テーマを足せる ★
  us  : [シンボル, 表示名]            (米国: ティッカー)
  jp  : [証券コード, 表示名, 連動理由]  (連動日本株 — 本セクターは連動分析 off)
  solo: [証券コード, 表示名, 内容]      (日本単独テーマ: 主に solo で登録)

注意: 原子力は各国規制・政策が独立するため linkage は無効。solo 中心。
"""

MACRO = [
    {
        "key": "construction",
        "name": "原子力建設",
        "color": "#E8B04B",
        "subs": [
            {
                "name": "原子力新設・EPC",
                "us": [
                    ["BWXT", "BWX Technologies"],
                    ["GEV", "GE Vernova"],
                    ["EMR", "Emerson Electric"],
                ],
                "jp": [],
                "solo": [
                    ["7011", "三菱重工業", "原子炉EPC・プレッシャー容器"],
                    ["1963", "日揮ホールディングス", "原子力プラントEPC"],
                    ["6330", "東洋エンジニアリング", "原子力設計・建設"],
                    ["1801", "大成建設", "原子力土木・建築"],
                    ["1721", "コムシスホールディングス", "原子力関連設備工事"],
                    ["2768", "双日", "原子力プラント関連商社"],
                ],
            },
            {
                "name": "原子炉設計・増設",
                "us": [
                    ["SMR", "NuScale Power"],
                    ["OKLO", "Oklo"],
                    ["NNE", "Nano Nuclear Energy"],
                ],
                "jp": [],
                "solo": [
                    ["6501", "日立製作所", "ABWR・BWR設計"],
                    ["6502", "東芝", "BWR・PWR設計"],
                    ["7011", "三菱重工業", "APWR・次世代炉"],
                ],
            },
            {
                "name": "土木・基礎・容器",
                "us": [
                    ["BWXT", "BWX Technologies"],
                ],
                "jp": [],
                "solo": [
                    ["5631", "日本製鋼所", "原子炉圧力容器・鍛造"],
                    ["5713", "住友金属鉱山", "原子力関連特殊材料"],
                    ["1801", "大成建設", "耐震・基礎土木"],
                    ["5401", "日本製鉄", "原子炉構造用鋼材"],
                    ["5411", "JFEホールディングス", "原子力用特殊鋼"],
                    ["5706", "三井金属", "ジルコニウム合金"],
                ],
            },
        ],
    },
    {
        "key": "operation",
        "name": "運転・再稼働",
        "color": "#3FA7D6",
        "subs": [
            {
                "name": "既設炉運転",
                "us": [
                    ["CEG", "Constellation Energy"],
                    ["VST", "Vistra"],
                    ["EXC", "Exelon"],
                    ["NEE", "NextEra Energy"],
                    ["PCG", "PG&E"],
                ],
                "jp": [],
                "solo": [
                    ["9501", "東京電力HD", "柏崎刈羽・福島第一(廃炉中)"],
                    ["9502", "中部電力", "浜松・知多・奥濃羽"],
                    ["9503", "関西電力", "高浜・大飯・美浜"],
                    ["9508", "九州電力", "玄海・川内・玄海増設"],
                ],
            },
            {
                "name": "再稼働・寿命延長",
                "us": [
                    ["CEG", "Constellation Energy"],
                    ["DUK", "Duke Energy"],
                    ["SO", "Southern Company"],
                ],
                "jp": [],
                "solo": [
                    ["9503", "関西電力", "高浜・大飯再稼働"],
                    ["9502", "中部電力", "浜松再稼働"],
                    ["9509", "北陸電力", "志賀再稼働"],
                    ["9504", "中国電力", "島根再稼働"],
                ],
            },
            {
                "name": "O&M・保守",
                "us": [
                    ["BWXT", "BWX Technologies"],
                    ["EMR", "Emerson Electric"],
                ],
                "jp": [],
                "solo": [
                    ["6501", "日立製作所", "原子力保守・I&C"],
                    ["6361", "荏原製作所", "原子炉冷却ポンプ"],
                    ["6841", "横河電機", "原子力計装・制御"],
                    ["6502", "東芝", "原子力保守サービス"],
                    ["6370", "栗田工業", "原子力向け超純水"],
                    ["6368", "オルガノ", "超純水製造装置"],
                ],
            },
            {
                "name": "安全規制・検査",
                "us": [],
                "jp": [],
                "solo": [
                    ["6951", "日本電子", "放射線計測・検査"],
                    ["6841", "横河電機", "原子力安全計装"],
                    ["5333", "日本ガイシ", "原子炉用セラミックス"],
                ],
            },
        ],
    },
    {
        "key": "fuel",
        "name": "核燃料サイクル",
        "color": "#9D7CF0",
        "subs": [
            {
                "name": "濃縮・変換",
                "us": [
                    ["LEU", "Centrus Energy"],
                    ["CCJ", "Cameco"],
                    ["UEC", "Uranium Energy"],
                ],
                "jp": [],
                "solo": [
                    ["4005", "住友化学", "ウラン変換・核燃料関連"],
                ],
            },
            {
                "name": "燃料加工・製造",
                "us": [
                    ["BWXT", "BWX Technologies"],
                    ["CCJ", "Cameco"],
                    ["LEU", "Centrus Energy"],
                ],
                "jp": [],
                "solo": [
                    ["5713", "住友金属鉱山", "核燃料関連材料"],
                    ["8058", "三菱商事", "ウラン・核燃料取引"],
                    ["8002", "丸紅", "ウラン資源開発"],
                ],
            },
            {
                "name": "再処理・後処理",
                "us": [
                    ["BWXT", "BWX Technologies"],
                ],
                "jp": [],
                "solo": [
                    ["6330", "東洋エンジニアリング", "再処理施設設計"],
                    ["1963", "日揮ホールディングス", "核燃料サイクル施設"],
                ],
            },
        ],
    },
    {
        "key": "smr",
        "name": "SMR・次世代炉",
        "color": "#5BE39B",
        "subs": [
            {
                "name": "SMR・小型炉",
                "us": [
                    ["SMR", "NuScale Power"],
                    ["NNE", "Nano Nuclear Energy"],
                    ["OKLO", "Oklo"],
                    ["BWXT", "BWX Technologies"],
                ],
                "jp": [],
                "solo": [
                    ["7011", "三菱重工業", "SRZ-1200・次世代炉"],
                    ["6501", "日立製作所", "BWRX-300(SMR)"],
                    ["6502", "東芝", "SMR開発"],
                ],
            },
            {
                "name": "次世代炉(ナトリウム・高温ガス)",
                "us": [
                    ["OKLO", "Oklo"],
                    ["BWXT", "BWX Technologies"],
                    ["GEV", "GE Vernova"],
                ],
                "jp": [],
                "solo": [
                    ["7011", "三菱重工業", "HTGR研究"],
                    ["6330", "東洋エンジニアリング", "次世代炉設計"],
                ],
            },
        ],
    },
    {
        "key": "equipment",
        "name": "原子力設備",
        "color": "#F0A85B",
        "subs": [
            {
                "name": "タービン・発電設備",
                "us": [
                    ["GEV", "GE Vernova"],
                    ["HON", "Honeywell"],
                ],
                "jp": [],
                "solo": [
                    ["7011", "三菱重工業", "原子炉タービン"],
                    ["6501", "日立製作所", "原子力タービン・発電"],
                    ["6361", "荏原製作所", "原子炉冷却・給水ポンプ"],
                    ["6504", "富士電機", "原子力発電設備"],
                    ["5334", "日本特殊陶業", "原子炉用セラミックス"],
                ],
            },
            {
                "name": "計装・制御(I&C)",
                "us": [
                    ["BWXT", "BWX Technologies"],
                    ["EMR", "Emerson Electric"],
                    ["HON", "Honeywell"],
                ],
                "jp": [],
                "solo": [
                    ["6841", "横河電機", "原子力計装システム"],
                    ["6502", "東芝", "原子力I&C"],
                    ["6501", "日立製作所", "原子力制御システム"],
                    ["6951", "日本電子", "原子力計測・検査"],
                    ["6645", "オムロン", "原子力向け制御機器"],
                ],
            },
            {
                "name": "配管・ポンプ・バルブ",
                "us": [
                    ["EMR", "Emerson Electric"],
                ],
                "jp": [],
                "solo": [
                    ["6361", "荏原製作所", "原子炉用ポンプ"],
                    ["6490", "日本ピラー工業", "原子炉配管用シール"],
                    ["6407", "CKD", "原子力向けバルブ"],
                    ["1963", "日揮ホールディングス", "原子力配管・配管工事"],
                    ["5801", "古河電工", "原子力ケーブル"],
                ],
            },
        ],
    },
    {
        "key": "decommission",
        "name": "廃炉・後処理",
        "color": "#8FA0B8",
        "subs": [
            {
                "name": "廃炉・解体",
                "us": [
                    ["BWXT", "BWX Technologies"],
                ],
                "jp": [],
                "solo": [
                    ["6501", "日立製作所", "廃炉・解体技術"],
                    ["6502", "東芝", "福島廃炉・ロボット"],
                    ["7011", "三菱重工業", "廃炉エンジニアリング"],
                    ["6301", "小松製作所", "廃炉解体ロボット"],
                ],
            },
            {
                "name": "放射性廃棄物",
                "us": [],
                "jp": [],
                "solo": [
                    ["1721", "コムシスホールディングス", "放射性廃棄物管理施設"],
                    ["1963", "日揮ホールディングス", "廃棄物処理施設"],
                    ["5713", "住友金属鉱山", "放射性廃棄物容器材料"],
                    ["5802", "住友電工", "原子力ケーブル・廃炉関連"],
                    ["8053", "住友商事", "廃炉・放射性廃棄物関連"],
                ],
            },
        ],
    },
    {
        "key": "utilities",
        "name": "電力・ユーティリティ",
        "color": "#7CC8F0",
        "subs": [
            {
                "name": "原子力保有電力(関東)",
                "us": [],
                "jp": [],
                "solo": [
                    ["9501", "東京電力HD", "原子力保有(柏崎刈羽)"],
                ],
            },
            {
                "name": "原子力保有電力(関西・中部)",
                "us": [],
                "jp": [],
                "solo": [
                    ["9503", "関西電力", "原子力主力(高浜・大飯)"],
                    ["9502", "中部電力", "浜松・知多"],
                ],
            },
            {
                "name": "原子力保有電力(その他)",
                "us": [
                    ["CEG", "Constellation Energy"],
                    ["VST", "Vistra"],
                    ["PEG", "Public Service Enterprise"],
                    ["ETR", "Entergy"],
                    ["WEC", "WEC Energy"],
                    ["XEL", "Xcel Energy"],
                ],
                "jp": [],
                "solo": [
                    ["9508", "九州電力", "玄海・川内"],
                    ["9506", "北海道電力", "泊"],
                    ["9504", "中国電力", "島根"],
                    ["9507", "四国電力", "伊方"],
                    ["9509", "北陸電力", "志賀"],
                ],
            },
        ],
    },
    {
        "key": "uranium",
        "name": "ウラン・資源",
        "color": "#D98C5F",
        "subs": [
            {
                "name": "ウラン鉱山・採掘",
                "us": [
                    ["CCJ", "Cameco"],
                    ["UEC", "Uranium Energy"],
                    ["UUUU", "Energy Fuels"],
                    ["DNN", "Denison Mines"],
                    ["NXE", "NexGen Energy"],
                    ["URG", "Ur-Energy"],
                    ["UROY", "Uranium Royalty"],
                ],
                "jp": [],
                "solo": [
                    ["5713", "住友金属鉱山", "ウラン・資源開発"],
                    ["8058", "三菱商事", "ウラン資源"],
                ],
            },
            {
                "name": "ウランETF・バスケット",
                "us": [
                    ["URA", "Global X Uranium ETF"],
                    ["NLR", "VanEck Uranium+Nuclear ETF"],
                    ["URNM", "Sprott Uranium Miners ETF"],
                    ["URNJ", "Sprott Junior Uranium Miners ETF"],
                ],
                "jp": [],
                "solo": [],
            },
        ],
    },
    {
        "key": "policy_nuclear",
        "name": "政策・規制",
        "color": "#A8B89F",
        "subs": [
            {
                "name": "再稼働政策・脱炭素",
                "us": [
                    ["CEG", "Constellation Energy"],
                    ["VST", "Vistra"],
                    ["GEV", "GE Vernova"],
                    ["PEG", "Public Service Enterprise"],
                ],
                "jp": [],
                "solo": [
                    ["9503", "関西電力", "再稼働政策受益者"],
                    ["6501", "日立製作所", "脱炭素・原子力再評価"],
                    ["5802", "住友電工", "原子力関連送配電"],
                    ["8058", "三菱商事", "原子力・ウラン政策連動"],
                ],
            },
            {
                "name": "原子力ETF・指数",
                "us": [
                    ["URA", "Global X Uranium ETF"],
                    ["NLR", "VanEck Uranium+Nuclear ETF"],
                    ["CEG", "Constellation Energy"],
                    ["ED", "Consolidated Edison"],
                ],
                "jp": [],
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
