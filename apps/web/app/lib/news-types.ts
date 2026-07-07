export interface RelatedStock {
  code: string;
  name: string;
  direction: "up" | "down" | "flat";
}

export interface NewsItem {
  id: string;
  date: string;
  title: string;
  summary: string;
  sentiment: number;
  tags: string[];
  geo: boolean;
  impact_chain: string[];
  related_stocks: RelatedStock[];
  source_url: string;
}

export interface TimelineItem {
  date: string;
  tone: "pos" | "neg" | "neu";
  title: string;
  body: string;
  tags?: string[];
}

export interface GlossaryTerm {
  en: string;
  jp: string;
  body: string;
  why: string;
  tags?: string[];
}
