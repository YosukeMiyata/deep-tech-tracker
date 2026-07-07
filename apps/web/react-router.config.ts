import type { Config } from "@react-router/dev/config";

const sectors = ["semi", "defense", "ai-dc", "space", "nuclear"];
const sectorRoutes = sectors.flatMap((s) => [
  `/${s}`,
  `/${s}/news`,
  `/${s}/themes`,
  `/${s}/map`,
  `/${s}/learn`,
]);

export default {
  ssr: false,
  basename: "/deep-tech-tracker/",
  prerender: ["/", ...sectorRoutes],
} satisfies Config;
