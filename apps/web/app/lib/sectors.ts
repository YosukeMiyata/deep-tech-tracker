import siteConfig from "../../../../config/site.json";

export interface SectorMeta {
  id: string;
  slug: string;
  name: string;
  shortName: string;
  subtitle: string;
  color: string;
  benchmark: { symbol: string; name: string };
  probe: { code: string; market: string; name: string };
  linkage: { enabled: boolean; threshold_pct: number };
  sentimentViz: "wafer" | "grid";
}

export const SITE = siteConfig.site;
export const SECTORS = siteConfig.sectors as SectorMeta[];
export const SECTOR_BY_ID = new Map(SECTORS.map((s) => [s.id, s]));
export const SECTOR_IDS = SECTORS.map((s) => s.id);

export function isValidSector(id: string | undefined): id is string {
  return !!id && SECTOR_BY_ID.has(id);
}

export function sectorBasePath(id: string): string {
  return `/${id}`;
}

export function sectorTabs(id: string) {
  const base = sectorBasePath(id);
  return [
    { to: base, icon: "◉", label: "ホーム", end: true },
    { to: `${base}/news`, icon: "▤", label: "ニュース" },
    { to: `${base}/themes`, icon: "↗", label: "テーマ" },
    { to: `${base}/map`, icon: "⬡", label: "マップ" },
    { to: `${base}/learn`, icon: "✎", label: "学ぶ" },
  ];
}
