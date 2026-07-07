# テーマ別ベンチマーク・米日連動方針

## ベンチマーク指数

| セクター | 指数 | ティッカー | 用途 |
|----------|------|-----------|------|
| 半導体 | PHLX Semiconductor | `^SOX` | YTD α、ホーム指数パネル |
| 防衛 | iShares US Aerospace & Defense | `ITA` | 同上 |
| AI DC | VanEck Semiconductor (proxy) | `SMH` | GPU/半導体需要 proxy |
| 宇宙 | Procure Space | `UFO` | 宇宙関連 basket |
| 原子力 | Global X Uranium | `URA` | ウラン・原子力 basket |

設定: [`config/site.json`](../../config/site.json) の `sectors[].benchmark`

## カナリア銘柄（Stooq 死活監視）

| セクター | 銘柄 | 理由 |
|----------|------|------|
| semi | 8035 東京エレクトロン | semi-tracker 実績 |
| defense | 7011 三菱重工業 | 防衛最大手 |
| ai-dc | NVDA | AI DC 代表 |
| space | RKLB Rocket Lab | 宇宙 pure play |
| nuclear | 6501 日立製作所 | 原子力事業保有 |

## 米日連動方針

| セクター | 連動分析 | 理由 |
|----------|---------|------|
| 半導体 | **有効** | US 半導体 → JP 装置/材料の連動が明確 |
| 防衛 | **有効** | F-35 等 US 防衛 → JP サプライヤー |
| AI DC | **有効** | NVDA 等 US → JP 装置/材料 |
| 宇宙 | **有効** | SpaceX/NASA 等 → JP 部品（限定的） |
| 原子力 | **無効** | 各国規制・政策が独立。solo 中心 |

### 連動定義（semi-tracker 踏襲）

- US テーマ（構成銘柄等ウェイト平均）が前日 **+2% 以上**
- 翌営業日の JP 連動株（`jp` 分類）リターンを集計
- 陽性率・平均リターン（n≥5）

### サブテーマ別の連動適用

| セクター | 連動 `jp` を多く使う | `solo` 中心 |
|----------|---------------------|-------------|
| 防衛 | platforms, intl_partners | budget_policy, cyber |
| AI DC | gpu_accel, memory_ai, optical_dc | cloud, capex_cycle |
| 宇宙 | components, japan_space | launch (US中心), policy |
| 原子力 | — | 全般（連動分析 off） |

## データディレクトリ

```
data/
├── hub/                    # ハブ共通
│   └── weekly_digest.json
├── semi/                   # 半導体（semi-tracker 移植）
├── defense/
├── ai-dc/
├── space/
└── nuclear/
```

各セクター配下の JSON（semi-tracker 同様）:

```
themes.json, themes_perf.json, themes_detail.json
prices.json, indices.json
linkage.json, linkage_top.json
process.json, flow.json
headlines.json, news.json, events.json
weekly_digest.json, macro.json, supplychain.json
glossary.json, timeline.json, timeline_stats.json
stock_tags.json, update_report.json
```

パイプライン実行:

```sh
python3 pipeline/build_master.py --theme semi
python3 pipeline/update_prices.py --theme semi
python3 pipeline/fetch_headlines.py --theme defense
python3 pipeline/update_all.py   # 全セクター一括
```
