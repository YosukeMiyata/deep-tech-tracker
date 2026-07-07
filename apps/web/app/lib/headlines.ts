import type { SectorDataBundle } from "~/lib/sector-data";

export interface HeadlineItem {
  id: string;
  date: string;
  title: string;
  url: string;
  source: string;
  published_at?: string | null;
}

export function headlineItems(data: SectorDataBundle): HeadlineItem[] {
  const raw = data.headlines as { items?: HeadlineItem[] };
  return (raw.items ?? [])
    .slice()
    .sort((a, b) => b.date.localeCompare(a.date) || b.id.localeCompare(a.id));
}

export function recentHeadlines(
  data: SectorDataBundle,
  days: number,
  count?: number,
): HeadlineItem[] {
  const items = headlineItems(data);
  const anchor = items[0]?.date ?? new Date().toISOString().slice(0, 10);
  const from = daysBefore(anchor, days);
  const filtered = items.filter((h) => h.date > from);
  return count ? filtered.slice(0, count) : filtered;
}

function daysBefore(anchor: string, days: number): string {
  const d = new Date(`${anchor}T00:00:00Z`);
  d.setUTCDate(d.getUTCDate() - days);
  return d.toISOString().slice(0, 10);
}

export function shortDate(date: string): string {
  const [, m, d] = date.split("-");
  return m && d ? `${Number(m)}/${Number(d)}` : date;
}
