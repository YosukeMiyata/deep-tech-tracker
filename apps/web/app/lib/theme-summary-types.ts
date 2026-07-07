export interface ThemeSummaryRow {
  key: string;
  name: string;
  color: string;
  dayPct: number | null;
  ytdPct: number | null;
  benchmarkAlpha: number | null;
  volRatio: number | null;
  spark: number[];
}
