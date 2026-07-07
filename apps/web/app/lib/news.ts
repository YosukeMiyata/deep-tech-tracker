import type { GlossaryTerm, NewsItem, TimelineItem } from "~/lib/news-types";
import type { SectorDataBundle } from "~/lib/sector-data";

export type { GlossaryTerm, NewsItem, RelatedStock, TimelineItem } from "~/lib/news-types";

export function newsItems(data: SectorDataBundle): NewsItem[] {
  return data.newsItems;
}

export function timelineItems(data: SectorDataBundle): TimelineItem[] {
  return data.timelineItems;
}

export function glossaryTerms(data: SectorDataBundle): GlossaryTerm[] {
  return data.glossaryTerms;
}

export function themeNames(data: SectorDataBundle): Map<string, string> {
  return new Map(data.themesMaster.macro.map((m) => [m.key, m.name]));
}

export function anchorDate(data: SectorDataBundle): string {
  return data.themesPerf.last_updated;
}

function daysBefore(anchor: string, days: number): string {
  const d = new Date(`${anchor}T00:00:00Z`);
  d.setUTCDate(d.getUTCDate() - days);
  return d.toISOString().slice(0, 10);
}

function average(values: number[]): number | null {
  if (values.length === 0) {
    return null;
  }
  return values.reduce((a, b) => a + b, 0) / values.length;
}

export function recentNews(data: SectorDataBundle, days: number): NewsItem[] {
  const from = daysBefore(anchorDate(data), days);
  return newsItems(data).filter((n) => n.date > from);
}

export function weeklySentiment(data: SectorDataBundle) {
  const ad = anchorDate(data);
  const weekAgo = daysBefore(ad, 7);
  const twoWeeksAgo = daysBefore(ad, 14);
  const thisWeek = newsItems(data).filter((n) => n.date > weekAgo);
  const prevWeek = newsItems(data).filter((n) => n.date > twoWeeksAgo && n.date <= weekAgo);
  const score = average(thisWeek.map((n) => n.sentiment));
  const prev = average(prevWeek.map((n) => n.sentiment));
  return {
    score,
    delta: score !== null && prev !== null ? score - prev : null,
    count: thisWeek.length,
  };
}

export function verdictLabel(score: number | null): string {
  if (score === null) {
    return "今週の分析ニュースなし";
  }
  if (score >= 1.2) {
    return "強気(ポジティブ優勢)";
  }
  if (score >= 0.5) {
    return "やや強気";
  }
  if (score > -0.5) {
    return "中立(強気と警戒が拮抗)";
  }
  if (score > -1.2) {
    return "やや弱気";
  }
  return "弱気(警戒優勢)";
}

export function themeSentiments(data: SectorDataBundle): {
  key: string;
  name: string;
  score: number | null;
}[] {
  const weekAgo = daysBefore(anchorDate(data), 7);
  const recent = newsItems(data).filter((n) => n.date > weekAgo);
  return data.themesMaster.macro.map((m) => {
    const scores = recent.filter((n) => n.tags.includes(m.key)).map((n) => n.sentiment);
    return { key: m.key, name: m.name, score: average(scores) };
  });
}

export type WeeklySentimentPoint = { weekStart: string; avg: number | null; count: number };

export function weeklySentimentSeries(data: SectorDataBundle, weeks = 12): WeeklySentimentPoint[] {
  const ad = anchorDate(data);
  const anchor = new Date(`${ad}T00:00:00Z`);
  const monOffset = (anchor.getUTCDay() + 6) % 7;
  const currentMonday = new Date(anchor);
  currentMonday.setUTCDate(anchor.getUTCDate() - monOffset);

  const out: WeeklySentimentPoint[] = [];
  for (let w = weeks - 1; w >= 0; w--) {
    const start = new Date(currentMonday);
    start.setUTCDate(currentMonday.getUTCDate() - w * 7);
    const end = new Date(start);
    end.setUTCDate(start.getUTCDate() + 7);
    const s = start.toISOString().slice(0, 10);
    const e = end.toISOString().slice(0, 10);
    const items = newsItems(data).filter((n) => n.date >= s && n.date < e);
    out.push({
      weekStart: s,
      avg: items.length > 0 ? items.reduce((a, b) => a + b.sentiment, 0) / items.length : null,
      count: items.length,
    });
  }
  return out;
}

export function weeklyThemeSentimentSeries(
  data: SectorDataBundle,
  themeKey: string | null,
  weeks = 12,
): WeeklySentimentPoint[] {
  const ad = anchorDate(data);
  const anchor = new Date(`${ad}T00:00:00Z`);
  const monOffset = (anchor.getUTCDay() + 6) % 7;
  const currentMonday = new Date(anchor);
  currentMonday.setUTCDate(anchor.getUTCDate() - monOffset);

  const out: WeeklySentimentPoint[] = [];
  for (let w = weeks - 1; w >= 0; w--) {
    const start = new Date(currentMonday);
    start.setUTCDate(currentMonday.getUTCDate() - w * 7);
    const end = new Date(start);
    end.setUTCDate(start.getUTCDate() + 7);
    const s = start.toISOString().slice(0, 10);
    const e = end.toISOString().slice(0, 10);
    let items = newsItems(data).filter((n) => n.date >= s && n.date < e);
    if (themeKey) {
      items = items.filter((n) => n.tags.includes(themeKey));
    }
    out.push({
      weekStart: s,
      avg: items.length > 0 ? items.reduce((a, b) => a + b.sentiment, 0) / items.length : null,
      count: items.length,
    });
  }
  return out;
}

export function featuredNews(data: SectorDataBundle, count = 3): NewsItem[] {
  const twoWeeksAgo = daysBefore(anchorDate(data), 14);
  const recent = newsItems(data).filter((n) => n.date > twoWeeksAgo);
  const pool = recent.length >= count ? recent : newsItems(data);
  return pool
    .slice()
    .sort((a, b) => Math.abs(b.sentiment) - Math.abs(a.sentiment) || b.date.localeCompare(a.date))
    .slice(0, count);
}

export function shortDate(date: string): string {
  const [, m, d] = date.split("-");
  if (!m) {
    return date;
  }
  return d ? `${Number(m)}/${Number(d)}` : `${Number(m)}月`;
}
