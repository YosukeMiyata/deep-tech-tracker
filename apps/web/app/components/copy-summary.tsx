import { useState } from "react";
import { fmtPct } from "~/lib/data";
import { macroData } from "~/lib/macro";
import { anchorDate, featuredNews, verdictLabel, weeklySentiment } from "~/lib/news";
import { useSector } from "~/lib/sector-context";
import type { SectorDataBundle } from "~/lib/sector-data";
import type { SectorMeta } from "~/lib/sectors";
import { benchmarkYtdPct, themeSummaryRows } from "~/lib/theme-summary";
import { weeklyDigest } from "~/lib/weekly-digest";

function buildSummary(data: SectorDataBundle, sector: SectorMeta): string {
  const weekly = weeklySentiment(data);
  const digest = weeklyDigest(data);
  const benchmarkYtd = benchmarkYtdPct(data, sector.benchmark.symbol);
  const benchmarkName = sector.benchmark.name;
  const lines: string[] = [
    `# ${sector.name}テーマトラッカー データサマリー(基準日 ${anchorDate(data)})`,
    "",
    `## 今週変わったこと(${digest.week_start}〜${digest.week_end})`,
    digest.title,
    digest.body,
    "",
    `## 週間センチメント`,
    `スコア: ${weekly.score === null ? "データなし" : weekly.score.toFixed(1)} / ±2.0(${verdictLabel(weekly.score)}、分析ニュース ${weekly.count}本)`,
  ];
  for (const ix of data.indices) {
    lines.push(
      "",
      `## ${ix.name}(${ix.date})`,
      `終値 ${ix.last} / 前日 ${fmtPct(ix.chg_pct)} / 年初来 ${fmtPct(ix.ytd_pct)}`,
    );
  }
  const macro = macroData(data);
  lines.push("", "## マクロ(サイクル)", macro.cycle_note);
  const lastWsts = macro.wsts.series.at(-1);
  if (lastWsts) {
    lines.push(
      `WSTS直近(${lastWsts.month}): ${lastWsts.value}${macro.wsts.unit} / 前年比 ${fmtPct(lastWsts.yoy_pct, 1)}`,
    );
  }
  if (macro.capex) {
    lines.push("", `## CapEx ガイダンス(${macro.capex.as_of})`);
    for (const c of macro.capex.items) {
      lines.push(`- ${c.company}: ${c.value}B$ / YoY ${fmtPct(c.yoy_pct, 0)} — ${c.note}`);
    }
  }
  lines.push(
    "",
    `## テーマ別 年初来・${benchmarkName}比α(${benchmarkName} YTD ${fmtPct(benchmarkYtd, 1)})`,
  );
  for (const t of themeSummaryRows(data, sector.benchmark.symbol)) {
    lines.push(
      `- ${t.name}: YTD ${fmtPct(t.ytdPct)} / α ${fmtPct(t.benchmarkAlpha, 0)}${t.volRatio !== null ? ` / 出来高 ${t.volRatio.toFixed(2)}×` : ""}`,
    );
  }
  lines.push("", `## 米国テーマ → 翌日の日本株(${data.linkageTop.method})`);
  if (data.linkageTop.rows.length === 0) {
    lines.push("- 直近の営業日に +2% 超で上昇した米国テーマなし");
  }
  for (const r of data.linkageTop.rows) {
    lines.push(
      `- ${r.theme}(前日 ${fmtPct(r.us_avg)})→ ${r.name}: 陽性率 ${r.rate}% / 平均 ${fmtPct(r.avg, 2)}(n=${r.n})`,
    );
  }
  lines.push("", "## 注目ニュース");
  for (const n of featuredNews(data)) {
    lines.push(
      `- [${n.date}] ${n.title}(スコア ${n.sentiment > 0 ? "+" : ""}${n.sentiment.toFixed(1)})`,
    );
  }
  lines.push(
    "",
    "---",
    "上記は個人向け半導体株情報サイトの自動生成データです(投資助言ではありません)。",
    "このデータを踏まえて質問に答えてください。",
  );
  return lines.join("\n");
}

export function CopySummary() {
  const { data, sector } = useSector();
  const [copied, setCopied] = useState(false);

  const copy = async () => {
    try {
      await navigator.clipboard.writeText(buildSummary(data, sector));
      setCopied(true);
      setTimeout(() => setCopied(false), 2500);
    } catch {
      // クリップボード非対応環境では何もしない
    }
  };

  return (
    <div className="card-surface mt-6 border-dashed text-center md:mt-10">
      <button
        type="button"
        onClick={copy}
        className="type-list-primary rounded-full bg-gradient-to-br from-down to-[#5B9279] px-5 py-2 font-bold text-white focus-visible:outline-2 focus-visible:outline-copper focus-visible:outline-offset-2 md:px-7 md:py-3"
      >
        {copied ? "コピーしました ✓" : "AI分析用サマリーをコピー"}
      </button>
      <p className="type-body-sm mt-3">
        本日の全データをテキスト化します。Claude などの AI
        に貼り付けて「このデータで注目すべき点は?」のように質問できます。
      </p>
    </div>
  );
}
