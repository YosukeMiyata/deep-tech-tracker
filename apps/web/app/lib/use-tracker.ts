import { useMemo } from "react";
import { useSector } from "~/lib/sector-context";
import { createTracker } from "~/lib/tracker";

export function useTracker() {
  const { data } = useSector();
  return useMemo(() => createTracker(data), [data]);
}
