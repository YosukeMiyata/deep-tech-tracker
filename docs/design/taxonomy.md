# 5テーマ Taxonomy 草案

## 概要

Deep Tech Tracker は5つの独立セクター（ハブ型）で構成する。各セクター内は semi-tracker と同様 **マクロテーマ → サブテーマ → 銘柄(us/jp/solo)** の3階層。

| セクター | slug | マクロ数(目標) | サブ数(目標) | 銘柄数(目標) |
|----------|------|----------------|--------------|--------------|
| 半導体 | `semi` | 12 | 59 | ~280 |
| 防衛 | `defense` | 10 | 28 | ~120 |
| AIデータセンター | `ai-dc` | 10 | 32 | ~150 |
| 宇宙 | `space` | 9 | 24 | ~100 |
| 原子力電力 | `nuclear` | 9 | 22 | ~90 |

---

## 1. 半導体 (`semi`)

semi-tracker からそのまま移植。12マクロ:

| key | 名称 |
|-----|------|
| memory | メモリ・ストレージ |
| optical | 光接続 |
| package | 先端パッケージング・基板 |
| spe | 半導体製造装置(SPE) |
| compute | 計算半導体 |
| analog_power | アナログ・電源 |
| passive | 受動部品 |
| datacenter | データセンター |
| materials | 半導体材料 |
| subsystem | サブシステム |
| facility | 半導体ファブ |
| metals | 銅・貴金属(川上資源) |

---

## 2. 防衛 (`defense`)

| key | 名称 | サブテーマ例 |
|-----|------|-------------|
| platforms | 防衛プラットフォーム | 戦闘機, 艦艇, 装甲車, 無人機 |
| electronics | 防衛電子・センサー | レーダー, EW, 通信, 画像処理 |
| missiles | ミサイル・弾薬 | 巡航ミサイル, 防空, 誘導弾部品 |
| cyber | サイバー防衛 | SOC/SIEM, ゼロトラスト, 政府向け |
| space_defense | 宇宙防衛 | 早期警戒, 衛星コンステレーション |
| shipbuilding | 造船・海洋 | 潜水艦, 護衛艦, 海洋監視 |
| logistics | 防衛物流・支援 | 輸送機, 整備, C4I |
| materials_def | 防衛材料・部品 | 複合材料, 特殊鋼, 光学部品 |
| intl_partners | 国際防衛連携 | F-35サプライチェーン, AUKUS関連 |
| budget_policy | 予算・政策連動 | 防衛費増, 安保関連ETF |

---

## 3. AIデータセンター (`ai-dc`)

半導体の `datacenter` / `compute` / `optical` と重複する銘柄あり（[overlap-matrix.md](./overlap-matrix.md) 参照）。

| key | 名称 | サブテーマ例 |
|-----|------|-------------|
| gpu_accel | GPU・アクセラレータ | NVIDIA, AMD, カスタムASIC |
| server_oem | サーバー・OEM | Supermicro, Dell, HPE |
| networking | DCネットワーク | スイッチ, NIC, DPU |
| optical_dc | 光接続(DC向け) | CPO, 光トランシーバ |
| cooling | 冷却・電源効率 | 液冷, 浸漬冷却, UPS |
| power_dc | DC電源・配電 | 高効率電源, 銅配線 |
| memory_ai | AI向けメモリ | HBM, CXL, SSD |
| cloud | クラウド・ハイパースケーラー | AWS/Azure/GCP関連 |
| edge_ai | エッジAI | 推論向けSoC, エッジサーバー |
| capex_cycle | CapExサイクル | データセンターREIT, 建設 |

---

## 4. 宇宙 (`space`)

| key | 名称 | サブテーマ例 |
|-----|------|-------------|
| launch | ロケット・打ち上げ | 再利用ロケット, 小型ロケット |
| satellites | 衛星製造・運用 | 通信衛星, 地球観測, コンステレーション |
| ground | 地上局・サービス | 地上局, 衛星データ分析 |
| components | 宇宙部品・材料 | 推進, 構造, 放射線耐性 |
| defense_space | 防衛宇宙 | 早期警戒, 軍事衛星 |
| commercial | 商用宇宙サービス | 宇宙輸送, 軌道上サービス |
| exploration | 探査・深宇宙 | 月面, 火星, 探査機 |
| policy | 規制・政策 | 宇宙法, 軌道デブリ規制 |
| japan_space | 日本宇宙産業 | H3, 準天頂, 宇宙ビジネス |

---

## 5. 原子力電力 (`nuclear`)

| key | 名称 | サブテーマ例 |
|-----|------|-------------|
| construction | 原子力建設 | 新設, 増設, EPC |
| operation | 運転・再稼働 | 既設炉, 再稼働関連 |
| fuel | 核燃料サイクル | 濃縮, 燃料加工, 再処理 |
| smr | SMR・次世代炉 | 小型モジュール炉, ナトリウム炉 |
| equipment | 原子力設備 | タービン, 計装, 配管 |
| decommission | 廃炉・後処理 | 廃炉, 放射性廃棄物 |
| utilities | 電力・ユーティリティ | 原子力保有電力, 送配電 |
| uranium | ウラン・資源 | ウラン鉱山, 燃料供給 |
| policy_nuclear | 政策・規制 | 再稼働政策, 脱炭素連動 |

---

## ファイル対応

| セクター | 銘柄マスタ | 工程マップ | フロー図 | タグ |
|----------|-----------|-----------|---------|------|
| semi | `pipeline/themes/semi.py` | `pipeline/maps/semi/process_map.py` | `pipeline/maps/semi/flow_map.py` | `pipeline/tags/semi.py` |
| defense | `pipeline/themes/defense.py` | `pipeline/maps/defense/` | `pipeline/maps/defense/` | `pipeline/tags/defense.py` |
| ai-dc | `pipeline/themes/ai-dc.py` | `pipeline/maps/ai-dc/` | `pipeline/maps/ai-dc/` | `pipeline/tags/ai-dc.py` |
| space | `pipeline/themes/space.py` | `pipeline/maps/space/` | `pipeline/maps/space/` | `pipeline/tags/space.py` |
| nuclear | `pipeline/themes/nuclear.py` | `pipeline/maps/nuclear/` | `pipeline/maps/nuclear/` | `pipeline/tags/nuclear.py` |
