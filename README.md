# Deep Tech Tracker

半導体・防衛・AIデータセンター・宇宙・原子力電力の **5セクター** を束ねるハブ型 Deep Tech 投資リサーチサイト。

- ベース: [semi-tracker](https://github.com/yuyu5555-bit/semi-tracker) のアーキテクチャを拡張
- 各セクター: semi-tracker 相当の全機能(7ビュートラッカー・米日連動・工程/フロー・サプライチェーン・用語辞典・マクロ指標)

## 構成

```
apps/web/           フロントエンド (React 19 / React Router v7 SSG)
pipeline/           データパイプライン (Python 3.12)
  themes/           セクター別銘柄マスタ (semi, defense, ai_dc, space, nuclear)
  maps/             セクター別工程/フロー定義
  tags/             セクター別検索タグ
data/
  hub/              ハブ共通データ
  semi/ ... nuclear/  セクター別 JSON
config/site.json    サイト・セクター設定
docs/design/        設計ドキュメント (taxonomy, benchmarks, overlap)
```

## サイト構成

| レイヤ | パス | 内容 |
|--------|------|------|
| ハブ | `/` | 5セクターカード・横断サマリー |
| セクター | `/{sector}` | ホーム(weekly digest, テーマ騰落, センチメント…) |
| | `/{sector}/news` | ヘッドライン・イベント・分析ニュース |
| | `/{sector}/themes` | 7ビュートラッカー |
| | `/{sector}/map` | サプライチェーンマップ |
| | `/{sector}/learn` | 用語辞典 |

セクター slug: `semi`, `defense`, `ai-dc`, `space`, `nuclear`

## 開発

```sh
pnpm install
pnpm dev          # http://localhost:5173/deep-tech-tracker/
pnpm build
pnpm typecheck
```

## データパイプライン

```sh
# 銘柄マスタ → themes.json / process.json / flow.json
python3 pipeline/build_master.py --theme all

# 株価取得・集計 (ネットワーク必要)
python3 pipeline/update_prices.py --theme semi
python3 pipeline/update_prices.py --theme all

# ヘッドライン RSS
python3 pipeline/fetch_headlines.py --theme all

# 全セクター一括
python3 pipeline/update_all.py
```

## 銘柄・テーマの追加

`pipeline/themes/{sector}.py` の `MACRO` を編集 → `python3 pipeline/build_master.py --theme {sector}`

## デプロイ

GitHub Pages (`/deep-tech-tracker/`)。`update-data.yml` が平日に全セクターの株価+headlines を更新。

## 免責

投資助言ではありません。投資判断はご自身の責任でお願いします。
