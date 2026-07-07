# 半導体 vs AIデータセンター 重複整理

## 方針

**両方に載せる（クロスリファレンス）** を基本とする。投資家の視点が異なるため:

- **半導体**: チップ設計・製造・材料のサプライチェーン
- **AI DC**: データセンター設備・運用・CapEx サイクル

同一銘柄が両セクターに登場しても問題ない。`note`（連動理由）をセクターごとに書き分ける。

## 重複サブテーマ

| 半導体 macro/sub | AI DC macro/sub | 整理 |
|-----------------|-----------------|------|
| datacenter / サーバーOEM | server_oem / サーバーOEM | AI DC 側を DC インフラ視点に |
| datacenter / AI向け電源 | power_dc / DC電源 | AI DC 側を施設電源・PUE 視点 |
| datacenter / 液冷・冷却 | cooling / 液冷 | AI DC 側をラック/施設冷却 |
| compute / GPU | gpu_accel / GPU | 半導体=設計/製造, AI DC=需要/CapEx |
| memory / HBM | memory_ai / HBM | 半導体=製造装置/材料, AI DC=AI需要 |
| optical / CPO | optical_dc / CPO | 半導体=デバイス, AI DC=DC内接続 |
| metals / 銅接続 | power_dc / 銅配線 | AI DC=DC配線需要 |

## 半導体のみに残す

- SPE（製造装置全般）
- ウェハー・フォトマスク・EUV
- ファブ設備
- 受動部品（MLCC 等）

## AI DC のみに置く

- クラウド・ハイパースケーラー（AMZN, MSFT, GOOGL）
- データセンター REIT（EQIX, DLR）
- 浸漬冷却・ラック液冷 integrator
- CapEx サイクル指標

## 重複銘柄（代表例）

| 銘柄 | 半導体テーマ | AI DC テーマ |
|------|-------------|-------------|
| NVDA | compute/GPU | gpu_accel |
| AVGO | compute, optical | gpu_accel, networking |
| MU | memory/HBM | memory_ai/HBM |
| 8035 | spe, memory | — (半導体のみ) |
| EQIX | — | capex_cycle/DC REIT |
| VRT | datacenter/電源 | power_dc/UPS |

## 実装

- `pipeline/themes/semi.py` — 現行維持
- `pipeline/themes/ai-dc.py` — DC 視点の taxonomy を新規定義
- 検索タグで `AI DC` / `半導体` を区別
