import { anchorDate, themeNames } from "~/lib/news";
import type { SectorDataBundle } from "~/lib/sector-data";

export type EventKind = "earnings" | "regulation" | "industry" | "macro";

export interface CalendarEvent {
  date: string;
  kind: EventKind;
  title: string;
  body: string;
  tags: string[];
  source_url?: string;
}

export const KIND_LABEL: Record<EventKind, string> = {
  earnings: "決算",
  regulation: "規制",
  industry: "業界",
  macro: "マクロ",
};

export const KIND_CLASS: Record<EventKind, string> = {
  earnings: "bg-copper text-paper",
  regulation: "bg-down text-paper",
  industry: "bg-cyan text-paper",
  macro: "bg-faint text-paper",
};

export const WEEKDAY_LABELS = ["月", "火", "水", "木", "金", "土", "日"] as const;

export function calendarEvents(data: SectorDataBundle): CalendarEvent[] {
  return (data.events.items as CalendarEvent[])
    .slice()
    .sort((a, b) => a.date.localeCompare(b.date));
}

function daysAfter(anchor: string, days: number): string {
  const d = new Date(`${anchor}T00:00:00Z`);
  d.setUTCDate(d.getUTCDate() + days);
  return d.toISOString().slice(0, 10);
}

export function upcomingEvents(data: SectorDataBundle, horizonDays = 14): CalendarEvent[] {
  const ad = anchorDate(data);
  const until = daysAfter(ad, horizonDays);
  return calendarEvents(data).filter((e) => e.date >= ad && e.date <= until);
}

export interface CalendarCell {
  date: string;
  day: number;
  isPast: boolean;
  isAnchor: boolean;
  events: CalendarEvent[];
}

export function twoWeekCalendarGrid(data: SectorDataBundle): {
  weeks: CalendarCell[][];
  rangeLabel: string;
} {
  const anchorDateStr = anchorDate(data);
  const anchor = new Date(`${anchorDateStr}T00:00:00Z`);
  const monOffset = (anchor.getUTCDay() + 6) % 7;
  const gridStart = new Date(anchor);
  gridStart.setUTCDate(anchor.getUTCDate() - monOffset);

  const byDate = new Map<string, CalendarEvent[]>();
  for (const e of upcomingEvents(data, 14)) {
    const list = byDate.get(e.date) ?? [];
    list.push(e);
    byDate.set(e.date, list);
  }

  const weeks: CalendarCell[][] = [];
  for (let w = 0; w < 2; w++) {
    const row: CalendarCell[] = [];
    for (let d = 0; d < 7; d++) {
      const cell = new Date(gridStart);
      cell.setUTCDate(gridStart.getUTCDate() + w * 7 + d);
      const date = cell.toISOString().slice(0, 10);
      row.push({
        date,
        day: cell.getUTCDate(),
        isPast: date < anchorDateStr,
        isAnchor: date === anchorDateStr,
        events: byDate.get(date) ?? [],
      });
    }
    weeks.push(row);
  }

  const gridEnd = new Date(gridStart);
  gridEnd.setUTCDate(gridStart.getUTCDate() + 13);
  const rangeLabel = `${eventDateLabel(gridStart.toISOString().slice(0, 10))}〜${eventDateLabel(gridEnd.toISOString().slice(0, 10))}`;

  return { weeks, rangeLabel };
}

export function eventDateLabel(date: string): string {
  const [, m, d] = date.split("-");
  return m && d ? `${Number(m)}/${Number(d)}` : date;
}

export function eventWeekdayLabel(date: string): string {
  const d = new Date(`${date}T00:00:00Z`);
  return WEEKDAY_LABELS[(d.getUTCDay() + 6) % 7];
}

export function isEventAnchorDay(data: SectorDataBundle, date: string): boolean {
  return date === anchorDate(data);
}

export function eventsGroupedByDate(
  events: CalendarEvent[],
): { date: string; events: CalendarEvent[] }[] {
  const map = new Map<string, CalendarEvent[]>();
  for (const e of events) {
    const list = map.get(e.date) ?? [];
    list.push(e);
    map.set(e.date, list);
  }
  return [...map.entries()]
    .sort(([a], [b]) => a.localeCompare(b))
    .map(([date, dayEvents]) => ({ date, events: dayEvents }));
}

export function eventThemeName(data: SectorDataBundle, key: string): string {
  return themeNames(data).get(key) ?? key;
}
