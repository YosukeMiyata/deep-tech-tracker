import type {
  IndexStat,
  LinkageTop,
  ThemeDetail,
  ThemePerf,
  ThemesDetail,
  ThemesPerf,
} from "~/lib/data-types";
import type { GlossaryTerm, NewsItem, TimelineItem } from "~/lib/news-types";
import aiDcEvents from "../../../../data/ai-dc/events.json";
import aiDcFlow from "../../../../data/ai-dc/flow.json";
import aiDcGlossary from "../../../../data/ai-dc/glossary.json";
import aiDcHeadlines from "../../../../data/ai-dc/headlines.json";
// ai-dc
import aiDcIndices from "../../../../data/ai-dc/indices.json";
import aiDcLinkage from "../../../../data/ai-dc/linkage.json";
import aiDcLinkageTop from "../../../../data/ai-dc/linkage_top.json";
import aiDcMacro from "../../../../data/ai-dc/macro.json";
import aiDcNews from "../../../../data/ai-dc/news.json";
import aiDcPrices from "../../../../data/ai-dc/prices.json";
import aiDcProcess from "../../../../data/ai-dc/process.json";
import aiDcStockTags from "../../../../data/ai-dc/stock_tags.json";
import aiDcSupplychain from "../../../../data/ai-dc/supplychain.json";
import aiDcThemes from "../../../../data/ai-dc/themes.json";
import aiDcThemesDetail from "../../../../data/ai-dc/themes_detail.json";
import aiDcThemesPerf from "../../../../data/ai-dc/themes_perf.json";
import aiDcTimeline from "../../../../data/ai-dc/timeline.json";
import aiDcTimelineStats from "../../../../data/ai-dc/timeline_stats.json";
import aiDcWeekly from "../../../../data/ai-dc/weekly_digest.json";
import defenseEvents from "../../../../data/defense/events.json";
import defenseFlow from "../../../../data/defense/flow.json";
import defenseGlossary from "../../../../data/defense/glossary.json";
import defenseHeadlines from "../../../../data/defense/headlines.json";
// defense
import defenseIndices from "../../../../data/defense/indices.json";
import defenseLinkage from "../../../../data/defense/linkage.json";
import defenseLinkageTop from "../../../../data/defense/linkage_top.json";
import defenseMacro from "../../../../data/defense/macro.json";
import defenseNews from "../../../../data/defense/news.json";
import defensePrices from "../../../../data/defense/prices.json";
import defenseProcess from "../../../../data/defense/process.json";
import defenseStockTags from "../../../../data/defense/stock_tags.json";
import defenseSupplychain from "../../../../data/defense/supplychain.json";
import defenseThemes from "../../../../data/defense/themes.json";
import defenseThemesDetail from "../../../../data/defense/themes_detail.json";
import defenseThemesPerf from "../../../../data/defense/themes_perf.json";
import defenseTimeline from "../../../../data/defense/timeline.json";
import defenseTimelineStats from "../../../../data/defense/timeline_stats.json";
import defenseWeekly from "../../../../data/defense/weekly_digest.json";
// hub
import hubWeekly from "../../../../data/hub/weekly_digest.json";
import nuclearEvents from "../../../../data/nuclear/events.json";
import nuclearFlow from "../../../../data/nuclear/flow.json";
import nuclearGlossary from "../../../../data/nuclear/glossary.json";
import nuclearHeadlines from "../../../../data/nuclear/headlines.json";
// nuclear
import nuclearIndices from "../../../../data/nuclear/indices.json";
import nuclearLinkage from "../../../../data/nuclear/linkage.json";
import nuclearLinkageTop from "../../../../data/nuclear/linkage_top.json";
import nuclearMacro from "../../../../data/nuclear/macro.json";
import nuclearNews from "../../../../data/nuclear/news.json";
import nuclearPrices from "../../../../data/nuclear/prices.json";
import nuclearProcess from "../../../../data/nuclear/process.json";
import nuclearStockTags from "../../../../data/nuclear/stock_tags.json";
import nuclearSupplychain from "../../../../data/nuclear/supplychain.json";
import nuclearThemes from "../../../../data/nuclear/themes.json";
import nuclearThemesDetail from "../../../../data/nuclear/themes_detail.json";
import nuclearThemesPerf from "../../../../data/nuclear/themes_perf.json";
import nuclearTimeline from "../../../../data/nuclear/timeline.json";
import nuclearTimelineStats from "../../../../data/nuclear/timeline_stats.json";
import nuclearWeekly from "../../../../data/nuclear/weekly_digest.json";
import semiEvents from "../../../../data/semi/events.json";
import semiFlow from "../../../../data/semi/flow.json";
import semiGlossary from "../../../../data/semi/glossary.json";
import semiHeadlines from "../../../../data/semi/headlines.json";
// semi
import semiIndices from "../../../../data/semi/indices.json";
import semiLinkage from "../../../../data/semi/linkage.json";
import semiLinkageTop from "../../../../data/semi/linkage_top.json";
import semiMacro from "../../../../data/semi/macro.json";
import semiNews from "../../../../data/semi/news.json";
import semiPrices from "../../../../data/semi/prices.json";
import semiProcess from "../../../../data/semi/process.json";
import semiStockTags from "../../../../data/semi/stock_tags.json";
import semiSupplychain from "../../../../data/semi/supplychain.json";
import semiThemes from "../../../../data/semi/themes.json";
import semiThemesDetail from "../../../../data/semi/themes_detail.json";
import semiThemesPerf from "../../../../data/semi/themes_perf.json";
import semiTimeline from "../../../../data/semi/timeline.json";
import semiTimelineStats from "../../../../data/semi/timeline_stats.json";
import semiWeekly from "../../../../data/semi/weekly_digest.json";
import spaceEvents from "../../../../data/space/events.json";
import spaceFlow from "../../../../data/space/flow.json";
import spaceGlossary from "../../../../data/space/glossary.json";
import spaceHeadlines from "../../../../data/space/headlines.json";
// space
import spaceIndices from "../../../../data/space/indices.json";
import spaceLinkage from "../../../../data/space/linkage.json";
import spaceLinkageTop from "../../../../data/space/linkage_top.json";
import spaceMacro from "../../../../data/space/macro.json";
import spaceNews from "../../../../data/space/news.json";
import spacePrices from "../../../../data/space/prices.json";
import spaceProcess from "../../../../data/space/process.json";
import spaceStockTags from "../../../../data/space/stock_tags.json";
import spaceSupplychain from "../../../../data/space/supplychain.json";
import spaceThemes from "../../../../data/space/themes.json";
import spaceThemesDetail from "../../../../data/space/themes_detail.json";
import spaceThemesPerf from "../../../../data/space/themes_perf.json";
import spaceTimeline from "../../../../data/space/timeline.json";
import spaceTimelineStats from "../../../../data/space/timeline_stats.json";
import spaceWeekly from "../../../../data/space/weekly_digest.json";

export interface SectorDataBundle {
  themesPerf: ThemesPerf;
  linkageTop: LinkageTop;
  themesDetail: ThemesDetail;
  indices: IndexStat[];
  timelineReactions: Record<string, Record<string, number>>;
  themesMaster: typeof semiThemes;
  newsItems: NewsItem[];
  timelineItems: TimelineItem[];
  glossaryTerms: GlossaryTerm[];
  events: typeof semiEvents;
  macro: typeof semiMacro;
  weeklyDigest: typeof semiWeekly;
  headlines: typeof semiHeadlines;
  supplychain: typeof semiSupplychain;
  prices: typeof semiPrices;
  linkage: typeof semiLinkage;
  process: typeof semiProcess;
  flow: typeof semiFlow;
  stockTags: typeof semiStockTags;
}

function bundle(
  themesPerf: unknown,
  linkageTop: unknown,
  themesDetail: unknown,
  indices: unknown,
  timelineStats: unknown,
  themesMaster: unknown,
  news: unknown,
  timeline: unknown,
  glossary: unknown,
  events: unknown,
  macro: unknown,
  weekly: unknown,
  headlines: unknown,
  supplychain: unknown,
  prices: unknown,
  linkage: unknown,
  process: unknown,
  flow: unknown,
  stockTags: unknown,
): SectorDataBundle {
  return {
    themesPerf: themesPerf as ThemesPerf,
    linkageTop: linkageTop as LinkageTop,
    themesDetail: themesDetail as ThemesDetail,
    indices: (indices as { indices: IndexStat[] }).indices,
    timelineReactions: (timelineStats as { reactions: Record<string, Record<string, number>> })
      .reactions,
    themesMaster: themesMaster as typeof semiThemes,
    newsItems: ((news as { items: NewsItem[] }).items ?? [])
      .slice()
      .sort((a, b) => b.date.localeCompare(a.date)),
    timelineItems: (timeline as { items: TimelineItem[] }).items,
    glossaryTerms: (glossary as { terms: GlossaryTerm[] }).terms,
    events: events as typeof semiEvents,
    macro: macro as typeof semiMacro,
    weeklyDigest: weekly as typeof semiWeekly,
    headlines: headlines as typeof semiHeadlines,
    supplychain: supplychain as typeof semiSupplychain,
    prices: prices as typeof semiPrices,
    linkage: linkage as typeof semiLinkage,
    process: process as typeof semiProcess,
    flow: flow as typeof semiFlow,
    stockTags: stockTags as typeof semiStockTags,
  };
}

export const SECTOR_DATA: Record<string, SectorDataBundle> = {
  semi: bundle(
    semiThemesPerf,
    semiLinkageTop,
    semiThemesDetail,
    semiIndices,
    semiTimelineStats,
    semiThemes,
    semiNews,
    semiTimeline,
    semiGlossary,
    semiEvents,
    semiMacro,
    semiWeekly,
    semiHeadlines,
    semiSupplychain,
    semiPrices,
    semiLinkage,
    semiProcess,
    semiFlow,
    semiStockTags,
  ),
  defense: bundle(
    defenseThemesPerf,
    defenseLinkageTop,
    defenseThemesDetail,
    defenseIndices,
    defenseTimelineStats,
    defenseThemes,
    defenseNews,
    defenseTimeline,
    defenseGlossary,
    defenseEvents,
    defenseMacro,
    defenseWeekly,
    defenseHeadlines,
    defenseSupplychain,
    defensePrices,
    defenseLinkage,
    defenseProcess,
    defenseFlow,
    defenseStockTags,
  ),
  "ai-dc": bundle(
    aiDcThemesPerf,
    aiDcLinkageTop,
    aiDcThemesDetail,
    aiDcIndices,
    aiDcTimelineStats,
    aiDcThemes,
    aiDcNews,
    aiDcTimeline,
    aiDcGlossary,
    aiDcEvents,
    aiDcMacro,
    aiDcWeekly,
    aiDcHeadlines,
    aiDcSupplychain,
    aiDcPrices,
    aiDcLinkage,
    aiDcProcess,
    aiDcFlow,
    aiDcStockTags,
  ),
  space: bundle(
    spaceThemesPerf,
    spaceLinkageTop,
    spaceThemesDetail,
    spaceIndices,
    spaceTimelineStats,
    spaceThemes,
    spaceNews,
    spaceTimeline,
    spaceGlossary,
    spaceEvents,
    spaceMacro,
    spaceWeekly,
    spaceHeadlines,
    spaceSupplychain,
    spacePrices,
    spaceLinkage,
    spaceProcess,
    spaceFlow,
    spaceStockTags,
  ),
  nuclear: bundle(
    nuclearThemesPerf,
    nuclearLinkageTop,
    nuclearThemesDetail,
    nuclearIndices,
    nuclearTimelineStats,
    nuclearThemes,
    nuclearNews,
    nuclearTimeline,
    nuclearGlossary,
    nuclearEvents,
    nuclearMacro,
    nuclearWeekly,
    nuclearHeadlines,
    nuclearSupplychain,
    nuclearPrices,
    nuclearLinkage,
    nuclearProcess,
    nuclearFlow,
    nuclearStockTags,
  ),
};

export function getSectorData(sectorId: string): SectorDataBundle {
  const data = SECTOR_DATA[sectorId];
  if (!data) {
    throw new Error(`Unknown sector: ${sectorId}`);
  }
  return data;
}

export const HUB_WEEKLY = hubWeekly;

/** ハブ横断: 各セクターの YTD トップテーマ */
export function hubSectorSummaries() {
  return Object.entries(SECTOR_DATA).map(([id, data]) => {
    const top = data.themesPerf.themes.find((t) => t.ytd_pct !== null) ?? data.themesPerf.themes[0];
    const benchmark = data.indices[0];
    return {
      id,
      lastUpdated: data.themesPerf.last_updated,
      topTheme: top as ThemePerf | undefined,
      benchmark,
    };
  });
}

export function chartColors(themes: ThemePerf[]): Record<string, string> {
  const out: Record<string, string> = {};
  for (const t of themes) {
    out[t.key] = t.color;
  }
  return out;
}
