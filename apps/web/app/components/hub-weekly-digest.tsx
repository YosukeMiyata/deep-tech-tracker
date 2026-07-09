interface HubDigest {
  title: string;
  body: string;
  updated: string;
}

export function WeeklyDigest({ digest }: { digest: HubDigest }) {
  return (
    <section className="relative mt-3 overflow-hidden rounded-card border-2 border-copper/45 bg-gradient-to-br from-copper-soft/55 via-card to-panel2 px-4 py-4 shadow-[inset_0_1px_0_rgba(232,176,75,0.2)] md:px-6 md:py-6 lg:px-7 lg:py-7">
      <div className="type-meta font-mono">{digest.updated} 更新</div>
      <h2 className="mt-2 font-bold font-serif text-[18px] md:text-[22px]">{digest.title}</h2>
      <p className="mt-3 text-[14px] text-ink-2 leading-relaxed md:text-[16px]">{digest.body}</p>
    </section>
  );
}
