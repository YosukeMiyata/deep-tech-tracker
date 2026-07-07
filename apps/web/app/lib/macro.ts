import type { SectorDataBundle } from "~/lib/sector-data";

export interface WstsPoint {
  month: string;
  value: number;
  yoy_pct: number;
}

export interface MacroData {
  last_updated: string;
  source_url: string;
  cycle_note: string;
  wsts: {
    label: string;
    unit: string;
    series: WstsPoint[];
  };
  capex?: {
    label: string;
    unit: string;
    as_of: string;
    items: { company: string; value: number; yoy_pct: number; note: string }[];
  };
}

export function macroData(data: SectorDataBundle): MacroData {
  return data.macro as MacroData;
}

export function monthLabel(ym: string): string {
  const [, m] = ym.split("-");
  return m ? `${Number(m)}月` : ym;
}

export function wstsRecent(data: SectorDataBundle, count = 6): WstsPoint[] {
  const m = macroData(data);
  return m.wsts?.series?.slice(-count) ?? [];
}
