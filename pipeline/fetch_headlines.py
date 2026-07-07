#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""RSS からセクター関連ヘッドラインを取得し data/{theme}/headlines.json を生成する。

実行例:
  python3 pipeline/fetch_headlines.py --theme semi
  python3 pipeline/fetch_headlines.py --theme all
"""

from __future__ import annotations

import argparse
import email.utils
import hashlib
import json
import re
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from headlines_config import HEADLINE_CONFIG  # noqa: E402
from theme_config import SECTOR_IDS, data_dir  # noqa: E402

KEEP_DAYS = 14
MAX_ITEMS = 72
UA = (
    "Mozilla/5.0 (compatible; deep-tech-tracker; +https://github.com/YosukeMiyata/deep-tech-tracker)"
)


def _http_get(url: str, timeout: int = 30) -> bytes:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": UA, "Accept": "application/rss+xml, application/xml, text/xml, */*"},
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read()


def _parse_pub_date(raw: str | None) -> datetime | None:
    if not raw:
        return None
    raw = raw.strip()
    try:
        dt = email.utils.parsedate_to_datetime(raw)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.astimezone(timezone.utc)
    except (TypeError, ValueError):
        pass
    for fmt in ("%Y-%m-%dT%H:%M:%S%z", "%Y-%m-%d"):
        try:
            dt = datetime.strptime(raw[: len(fmt) + 2], fmt)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            return dt.astimezone(timezone.utc)
        except ValueError:
            continue
    return None


def _clean_title(title: str) -> str:
    title = re.sub(r"\s+", " ", title).strip()
    # Google News: "記事タイトル - 媒体名"
    title = re.sub(
        r"\s+[-–—]\s+(日本経済新聞|Reuters|ロイター|Bloomberg\.com|Bloomberg|CNBC|WSJ|The Wall Street Journal|日刊工業新聞|東洋経済オンライン|東洋経済)\s*$",
        "",
        title,
    )
    return title


def _is_noise(title: str) -> bool:
    lower = title.lower()
    return "stock price & latest news" in lower or lower.startswith("scia.pk")


def _matches_keywords(text: str, keywords: tuple[str, ...]) -> bool:
    lower = text.lower()
    return any(kw in text or kw in lower for kw in keywords)


def _item_id(url: str, title: str) -> str:
    digest = hashlib.sha256(f"{url}|{title}".encode()).hexdigest()[:16]
    return f"hl-{digest}"


def _append_item(
    out: list[dict],
    *,
    title: str,
    url: str,
    source: str,
    require_keywords: bool,
    pub_raw: str | None,
    keywords: tuple[str, ...],
) -> None:
    title = _clean_title(title)
    url = url.strip()
    if not title or not url:
        return
    if _is_noise(title):
        return
    if require_keywords and not _matches_keywords(title, keywords):
        return
    pub = _parse_pub_date(pub_raw)
    out.append(
        {
            "id": _item_id(url, title),
            "date": pub.strftime("%Y-%m-%d") if pub else date.today().isoformat(),
            "title": title,
            "url": url,
            "source": source,
            "published_at": pub.isoformat() if pub else None,
        }
    )


def _parse_rss2(root: ET.Element, source: str, require_keywords: bool, keywords: tuple[str, ...]) -> list[dict]:
    channel = root.find("channel")
    if channel is None:
        channel = root

    out: list[dict] = []
    for item in channel.findall(".//item"):
        title_el = item.find("title")
        link_el = item.find("link")
        pub_el = item.find("pubDate")
        if title_el is None or link_el is None:
            continue
        _append_item(
            out,
            title="".join(title_el.itertext()).strip(),
            url="".join(link_el.itertext()).strip(),
            source=source,
            require_keywords=require_keywords,
            pub_raw="".join(pub_el.itertext()).strip() if pub_el is not None else None,
            keywords=keywords,
        )
    return out


def _parse_rdf(root: ET.Element, source: str, require_keywords: bool, keywords: tuple[str, ...]) -> list[dict]:
    ns = {
        "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "rss": "http://purl.org/rss/1.0/",
        "dc": "http://purl.org/dc/elements/1.1/",
    }
    out: list[dict] = []
    for item in root.findall(".//rss:item", ns):
        title = (item.findtext("rss:title", default="", namespaces=ns) or "").strip()
        url = (item.findtext("rss:link", default="", namespaces=ns) or "").strip()
        pub_raw = (item.findtext("dc:date", default="", namespaces=ns) or "").strip() or None
        _append_item(
            out,
            title=title,
            url=url,
            source=source,
            require_keywords=require_keywords,
            pub_raw=pub_raw,
            keywords=keywords,
        )
    return out


def _parse_feed(xml_bytes: bytes, source: str, require_keywords: bool, keywords: tuple[str, ...]) -> list[dict]:
    root = ET.fromstring(xml_bytes)
    if root.tag.endswith("RDF") or root.find("{http://purl.org/rss/1.0/}item") is not None:
        return _parse_rdf(root, source, require_keywords, keywords)
    return _parse_rss2(root, source, require_keywords, keywords)


def fetch_all(theme: str) -> tuple[list[dict], list[str]]:
    cfg = HEADLINE_CONFIG[theme]
    feeds = cfg["feeds"]
    keywords = tuple(cfg["keywords"])
    merged: list[dict] = []
    notes: list[str] = []
    for source, url, require_keywords in feeds:
        try:
            xml_bytes = _http_get(url)
            items = _parse_feed(xml_bytes, source, require_keywords, keywords)
            merged.extend(items)
            notes.append(f"{source}: {len(items)}件")
        except Exception as exc:
            notes.append(f"{source}: 失敗 ({exc})")
            print(f"** {source}: {exc}", file=sys.stderr)
    return merged, notes


def dedupe_and_trim(items: list[dict], *, today: date) -> list[dict]:
    cutoff = today - timedelta(days=KEEP_DAYS)
    seen: set[str] = set()
    unique: list[dict] = []

    def sort_key(row: dict) -> tuple[str, str]:
        return (row.get("published_at") or row["date"], row["id"])

    for row in sorted(items, key=sort_key, reverse=True):
        try:
            row_date = date.fromisoformat(row["date"])
        except ValueError:
            continue
        if row_date < cutoff:
            continue
        key = re.sub(r"\?.*$", "", row["url"].rstrip("/"))
        norm_title = re.sub(r"\W+", "", row["title"].lower())
        dedupe_key = f"{key}|{norm_title}"
        if dedupe_key in seen:
            continue
        seen.add(dedupe_key)
        unique.append(row)
        if len(unique) >= MAX_ITEMS:
            break
    return unique


def build_payload(items: list[dict], notes: list[str], theme: str) -> dict:
    now = datetime.now(timezone.utc)
    feeds = HEADLINE_CONFIG[theme]["feeds"]
    return {
        "_schema": (
            "id: 安定ID / date: YYYY-MM-DD / title: 見出し / url: 原文リンク / "
            "source: 媒体名 / published_at: ISO8601(任意)"
        ),
        "fetched_at": now.isoformat(),
        "theme": theme,
        "sources": [name for name, _, _ in feeds],
        "fetch_notes": notes,
        "items": items,
    }


def run_theme(theme: str) -> int:
    items, notes = fetch_all(theme)
    trimmed = dedupe_and_trim(items, today=date.today())
    if not trimmed:
        print(f"** [{theme}] ヘッドライン0件 — 既存ファイルを維持", file=sys.stderr)
        return 1

    out_path = data_dir(theme) / "headlines.json"
    payload = build_payload(trimmed, notes, theme)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {theme}/headlines.json ({len(trimmed)} items)")
    print("; ".join(notes))
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--theme", default="semi", choices=[*SECTOR_IDS, "all"])
    args = ap.parse_args()
    themes = list(SECTOR_IDS) if args.theme == "all" else [args.theme]
    rc = 0
    for theme in themes:
        if run_theme(theme) != 0:
            rc = 1
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
