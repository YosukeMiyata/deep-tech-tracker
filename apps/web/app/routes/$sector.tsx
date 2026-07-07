import type { ReactNode } from "react";
import { NavLink, Outlet, useParams } from "react-router";
import { HomeHeaderMenu, HomeSectionNavBar } from "~/components/home-header-menu";
import { SectorProvider } from "~/lib/sector-context";
import { getSectorData } from "~/lib/sector-data";
import { isValidSector, SECTOR_BY_ID, sectorTabs } from "~/lib/sectors";

function DesktopNavLink({
  to,
  icon,
  label,
  end,
}: {
  to: string;
  icon: string;
  label: string;
  end?: boolean;
}) {
  return (
    <NavLink
      to={to}
      end={end}
      className={({ isActive }) =>
        `flex items-center gap-1.5 rounded-lg px-3 py-2 text-[13px] transition-colors md:px-4 md:py-2.5 md:text-[15px] lg:text-[16px] ${
          isActive
            ? "bg-copper-soft font-bold text-copper"
            : "text-ink-2 hover:bg-panel2/60 hover:text-ink"
        }`
      }
    >
      <span className="text-[15px] leading-none">{icon}</span>
      {label}
    </NavLink>
  );
}

export default function SectorLayout() {
  const { sector: sectorId } = useParams();
  if (!isValidSector(sectorId)) {
    throw new Response("Not Found", { status: 404 });
  }
  const sector = SECTOR_BY_ID.get(sectorId)!;
  const data = getSectorData(sectorId);
  const tabs = sectorTabs(sectorId);

  return (
    <SectorProvider value={{ sector, data }}>
      <header className="sticky top-0 z-30 border-line border-b bg-paper/95 backdrop-blur-md">
        <div className="app-container py-4 md:py-6">
          <div className="flex items-center gap-2.5 md:gap-4">
            <div className="min-w-0 flex-1">
              <NavLink
                to="/"
                className="text-[10px] text-ink-2 tracking-[0.16em] hover:text-copper md:text-[12px]"
              >
                ← DEEP TECH TRACKER
              </NavLink>
              <div className="mt-1 text-[10px] text-ink-2 tracking-[0.16em] md:text-[12px]">
                {sector.subtitle}
              </div>
              <h1 className="mt-1 font-bold font-serif text-[19px] leading-[1.4] tracking-[0.02em] md:text-[24px] lg:text-[26px]">
                {sector.name}
                <span style={{ color: sector.color }} className="mx-1">
                  テーマ
                </span>
                トラッカー
              </h1>
              <p className="mt-1 font-mono text-[10px] text-faint sm:hidden">
                {data.themesPerf.last_updated} 時点
              </p>
            </div>
            <div className="hidden shrink-0 font-mono text-[11px] text-faint sm:block md:text-[13px]">
              {data.themesPerf.last_updated} 時点
            </div>
            <HomeHeaderMenu />
          </div>
          <nav
            className="-mx-1 mt-3 hidden items-center gap-0.5 overflow-x-auto md:flex [-ms-overflow-style:none] [scrollbar-width:none] [&::-webkit-scrollbar]:hidden"
            aria-label="セクターナビゲーション"
          >
            {tabs.map((tab) => (
              <DesktopNavLink key={tab.to} {...tab} />
            ))}
          </nav>
        </div>
        <HomeSectionNavBar />
      </header>

      <main className="app-container pt-[18px] pb-10 md:pt-8 md:pb-16">
        <Outlet />
      </main>

      <SectorMobileNav tabs={tabs} />

      <footer className="app-container type-body-sm pb-5 md:pb-24">
        <b className="text-ink-2">免責事項</b>
        :本サイトは公開情報の整理・ニュース論調の分析を提供するものであり、金融商品取引法上の投資助言ではありません。投資判断はご自身の責任でお願いします。
      </footer>
    </SectorProvider>
  );
}

function SectorMobileNav({
  tabs,
}: {
  tabs: { to: string; icon: string; label: string; end?: boolean }[];
}) {
  return (
    <nav
      className="fixed inset-x-0 bottom-0 z-40 flex gap-px border-line border-t bg-line pt-px pb-[env(safe-area-inset-bottom)] md:hidden"
      aria-label="セクターナビゲーション"
    >
      {tabs.map((tab) => (
        <NavLink
          key={tab.to}
          to={tab.to}
          end={tab.end}
          className={({ isActive }) =>
            `flex flex-1 flex-col items-center gap-0.5 bg-paper px-2 py-2.5 text-[11px] ${
              isActive ? "font-bold text-copper" : "text-ink-2"
            }`
          }
        >
          <span className="text-[18px] leading-none">{tab.icon}</span>
          {tab.label}
        </NavLink>
      ))}
    </nav>
  );
}

export function ErrorBoundary({ error }: { error: unknown }) {
  const message = error instanceof Error ? error.message : "不明なエラーが発生しました";
  return (
    <main className="app-container pt-[18px] md:pt-6">
      <h1 className="mb-2 font-bold font-serif text-[17px] md:text-[20px]">エラー</h1>
      <p className="text-[13px] text-ink-2 md:text-[15px]">{message as ReactNode}</p>
    </main>
  );
}
