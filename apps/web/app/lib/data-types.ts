export interface ThemePerf {
  key: string;
  name: string;
  color: string;
  ytd_pct: number | null;
  vol_ratio: number | null;
  spark: number[];
  n_stocks: number;
  n_ok: number;
}

export interface ThemesPerf {
  last_updated: string;
  note: string;
  themes: ThemePerf[];
}

export interface LinkageRow {
  theme: string;
  us_avg: number | null;
  trig_level: number;
  code: string;
  name: string;
  rate: number;
  avg: number;
  n: number;
}

export interface LinkageTop {
  last_updated: string;
  method: string;
  rows: LinkageRow[];
}

export interface StockStat {
  code: string;
  name: string;
  ytd_pct: number | null;
  chg_pct: number | null;
  vol_ratio: number | null;
}

export interface SubDetail {
  name: string;
  ytd_pct: number | null;
  stocks: StockStat[];
}

export interface ThemeDetail {
  key: string;
  name: string;
  color: string;
  ytd_pct: number | null;
  series: [string, number][];
  subs: SubDetail[];
}

export interface ThemesDetail {
  last_updated: string;
  note: string;
  themes: ThemeDetail[];
}

export interface IndexStat {
  id: string;
  name: string;
  last: number;
  date: string;
  chg_pct: number | null;
  ytd_pct: number | null;
  spark: number[];
}

/** 出来高急増の段階(v1 の 2倍/3倍/5倍を踏襲) */
export function volTier(volRatio: number | null): number | null {
  if (volRatio === null) {
    return null;
  }
  if (volRatio >= 5) {
    return 5;
  }
  if (volRatio >= 3) {
    return 3;
  }
  if (volRatio >= 2) {
    return 2;
  }
  return null;
}

/** 騰落率の表示形式(日本市場の慣習: 全角マイナス) */
export function fmtPct(v: number | null | undefined, digits = 1): string {
  if (v === null || v === undefined) {
    return "—";
  }
  return `${v >= 0 ? "+" : "−"}${Math.abs(v).toFixed(digits)}%`;
}

export function pctColor(v: number | null | undefined): string {
  if (v === null || v === undefined) {
    return "text-neutral";
  }
  return v >= 0 ? "text-up" : "text-down";
}
