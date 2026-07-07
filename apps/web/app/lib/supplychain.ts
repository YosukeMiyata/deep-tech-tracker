import { newsItems } from "~/lib/news";
import type { SectorDataBundle } from "~/lib/sector-data";

export interface SupplyStep {
  name: string;
  equip?: string[];
  material?: string[];
  stocks?: string[];
}

export interface SupplyStage {
  id: string;
  num: string;
  name: string;
  desc: string;
  topic: string;
  steps: SupplyStep[];
}

export function stages(data: SectorDataBundle): SupplyStage[] {
  return (data.supplychain.stages ?? []) as SupplyStage[];
}

export function codeNames(data: SectorDataBundle): Map<string, string> {
  const map = new Map<string, string>();
  for (const m of data.themesMaster.macro) {
    for (const sub of m.subs) {
      for (const u of sub.us) {
        map.set(u.symbol, u.name);
      }
      for (const row of [...sub.jp, ...sub.solo]) {
        map.set(row.code, row.name);
      }
    }
  }
  return map;
}

export function stockName(data: SectorDataBundle, code: string): string {
  return codeNames(data).get(code) ?? code;
}

function stageCodes(stage: SupplyStage): Set<string> {
  const codes = new Set<string>();
  for (const step of stage.steps) {
    for (const code of [...(step.equip ?? []), ...(step.material ?? []), ...(step.stocks ?? [])]) {
      codes.add(code);
    }
  }
  return codes;
}

export function stageNewsCount(data: SectorDataBundle, stage: SupplyStage): number {
  const codes = stageCodes(stage);
  const anchor = data.themesPerf.last_updated;
  const from = daysBefore(anchor, 7);
  return newsItems(data)
    .filter((n) => n.date >= from)
    .filter((n) => n.related_stocks.some((s) => codes.has(s.code))).length;
}

function daysBefore(anchor: string, days: number): string {
  const d = new Date(`${anchor}T00:00:00Z`);
  d.setUTCDate(d.getUTCDate() - days);
  return d.toISOString().slice(0, 10);
}
