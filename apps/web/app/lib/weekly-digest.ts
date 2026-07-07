import type { SectorDataBundle } from "~/lib/sector-data";

export interface WeeklyDigest {
  updated: string;
  week_start?: string;
  week_end?: string;
  title: string;
  body: string;
}

export function weeklyDigest(data: SectorDataBundle): WeeklyDigest {
  return data.weeklyDigest as WeeklyDigest;
}

export function digestWeekLabel(data: SectorDataBundle): string {
  const d = weeklyDigest(data);
  if (!d.week_start || !d.week_end) {
    return d.updated;
  }
  const [, sm, sd] = d.week_start.split("-");
  const [, em, ed] = d.week_end.split("-");
  if (!sm || !em) {
    return d.week_start;
  }
  if (sm === em) {
    return `${Number(sm)}/${Number(sd)}〜${Number(ed)}`;
  }
  return `${Number(sm)}/${Number(sd)}〜${Number(em)}/${Number(ed)}`;
}
