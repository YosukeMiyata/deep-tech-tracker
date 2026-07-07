import { createContext, useContext } from "react";
import type { SectorDataBundle } from "~/lib/sector-data";
import type { SectorMeta } from "~/lib/sectors";

export interface SectorContextValue {
  sector: SectorMeta;
  data: SectorDataBundle;
}

const SectorContext = createContext<SectorContextValue | null>(null);

export function SectorProvider({
  value,
  children,
}: {
  value: SectorContextValue;
  children: React.ReactNode;
}) {
  return <SectorContext.Provider value={value}>{children}</SectorContext.Provider>;
}

export function useSector(): SectorContextValue {
  const ctx = useContext(SectorContext);
  if (!ctx) {
    throw new Error("useSector must be used within SectorProvider");
  }
  return ctx;
}

export function useSectorOptional(): SectorContextValue | null {
  return useContext(SectorContext);
}
