import { Link } from "react-router";
import { WeeklyDigest } from "~/components/hub-weekly-digest";
import { Card, SectionTitle } from "~/components/section";
import { Sparkline } from "~/components/sparkline";
import { fmtPct, pctColor } from "~/lib/data";
import { HUB_WEEKLY, hubSectorSummaries } from "~/lib/sector-data";
import { SECTORS, sectorBasePath } from "~/lib/sectors";

export function meta() {
  return [{ title: "Deep Tech Tracker" }];
}

export default function HubHome() {
  const summaries = hubSectorSummaries();

  return (
    <main className="app-container pt-[18px] md:pt-8 ">
      <section className="mb-8">
        <div className="text-[10px] text-ink-2 tracking-[0.16em] md:text-[12px]">
          DEEP TECH TRACKER
        </div>
        <h1 className="mt-2 font-bold font-serif text-[22px] leading-[1.35] md:text-[32px] lg:text-[36px]">
          半導体・防衛・AI DC・宇宙・原子力
          <span className="text-copper"> 5テーマ</span>
          トラッカー
        </h1>
        <p className="mt-3 max-w-2xl text-[14px] text-ink-2 leading-relaxed md:text-[16px]">
          価格データ(数字) × ニュース解説(文脈)を統合した Deep Tech
          投資リサーチハブ。各セクターは独立したトラッカー(テーマ騰落・米日連動・マップ・用語辞典)を備えます。
        </p>
      </section>

      <WeeklyDigest digest={HUB_WEEKLY} />

      <SectionTitle title="5セクター" note="タップして各テーマトラッカーへ" />
      <div className="grid gap-3 md:grid-cols-2 lg:gap-4">
        {SECTORS.map((s) => {
          const summary = summaries.find((x) => x.id === s.id);
          const top = summary?.topTheme;
          const bench = summary?.benchmark;
          return (
            <Link key={s.id} to={sectorBasePath(s.id)} className="group block">
              <Card className="transition-colors group-hover:border-copper/40">
                <div className="flex items-start justify-between gap-3">
                  <div>
                    <div className="text-[10px] text-ink-2 tracking-[0.12em]">{s.subtitle}</div>
                    <div
                      className="mt-1 font-bold text-[17px] md:text-[19px]"
                      style={{ color: s.color }}
                    >
                      {s.name}
                    </div>
                    <div className="type-meta mt-1 font-mono">
                      {summary?.lastUpdated ?? "—"} 時点
                    </div>
                  </div>
                  {top?.spark?.length ? <Sparkline values={top.spark} /> : null}
                </div>
                {top ? (
                  <div className="type-body-sm mt-3 flex flex-wrap gap-x-4 gap-y-1 font-mono">
                    <span>
                      注目: <b>{top.name}</b>
                    </span>
                    <span className={pctColor(top.ytd_pct)}>YTD {fmtPct(top.ytd_pct)}</span>
                    {bench ? (
                      <span className={pctColor(bench.ytd_pct)}>
                        {s.benchmark.name} {fmtPct(bench.ytd_pct)}
                      </span>
                    ) : null}
                  </div>
                ) : null}
                <div className="type-meta mt-3 text-copper">トラッカーを開く →</div>
              </Card>
            </Link>
          );
        })}
      </div>

      <section className="mt-10 type-body-sm text-ink-2">
        <b className="text-ink-2">免責事項</b>
        :本サイトは公開情報の整理・ニュース論調の分析を提供するものであり、金融商品取引法上の投資助言ではありません。投資判断はご自身の責任でお願いします。
        <br />
        <br />
        データソース:株価=Stooq / Yahoo Finance / ヘッドライン=RSS / 分析ニュース=手動編集
      </section>
    </main>
  );
}
