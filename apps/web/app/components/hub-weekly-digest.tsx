interface HubDigest {
  title: string;
  body: string;
  updated: string;
}

export function WeeklyDigest({ digest }: { digest: HubDigest }) {
  return (
    <section className="mb-8 rounded-card border border-line bg-card px-4 py-5 md:px-6 md:py-7">
      <div className="type-meta font-mono">{digest.updated} 更新</div>
      <h2 className="mt-2 font-bold font-serif text-[18px] md:text-[22px]">{digest.title}</h2>
      <p className="mt-3 text-[14px] text-ink-2 leading-relaxed md:text-[16px]">{digest.body}</p>
    </section>
  );
}
