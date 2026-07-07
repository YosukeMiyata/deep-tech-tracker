import type { SectorDataBundle } from "~/lib/sector-data";
import type { ThemeSummaryRow } from "~/lib/theme-summary-types";

/** ベンチマーク年初来騰落率 */
export function benchmarkYtdPct(data: SectorDataBundle, symbol: string): number | null {
  const ix = data.indices.find((i) => i.id === symbol);
  return ix?.ytd_pct ?? null;
}

/** 累積騰落率系列の直近2点から前日比を算出 */
export function themeDayPct(series: [string, number][]): number | null {
  if (series.length < 2) {
    return null;
  }
  const prev = series.at(-2)?.[1];
  const curr = series.at(-1)?.[1];
  if (prev === undefined || curr === undefined) {
    return null;
  }
  return ((1 + curr / 100) / (1 + prev / 100) - 1) * 100;
}

/** ホーム用: マクロテーマの騰落サマリー(年初来順) */
export function themeSummaryRows(
  data: SectorDataBundle,
  benchmarkSymbol: string,
): ThemeSummaryRow[] {
  const detailByKey = new Map(data.themesDetail.themes.map((t) => [t.key, t]));
  const benchYtd = benchmarkYtdPct(data, benchmarkSymbol);
  return data.themesPerf.themes
    .map((t) => {
      const detail = detailByKey.get(t.key);
      const ytdPct = t.ytd_pct;
      return {
        key: t.key,
        name: t.name,
        color: t.color,
        dayPct: detail ? themeDayPct(detail.series) : null,
        ytdPct,
        benchmarkAlpha:
          ytdPct !== null && benchYtd !== null ? Math.round((ytdPct - benchYtd) * 10) / 10 : null,
        volRatio: t.vol_ratio,
        spark: t.spark,
      };
    })
    .sort((a, b) => (b.ytdPct ?? -1e9) - (a.ytdPct ?? -1e9));
}
