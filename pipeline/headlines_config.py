# -*- coding: utf-8 -*-
"""セクター別 RSS / キーワード設定。"""

from __future__ import annotations

import urllib.parse


def _gnews(query: str, *, hl: str, gl: str, ceid: str) -> str:
    return (
        "https://news.google.com/rss/search?q="
        + urllib.parse.quote(query)
        + f"&hl={hl}&gl={gl}&ceid={ceid}"
    )


def _feeds(ja_query: str, en_query: str) -> list[tuple[str, str, bool]]:
    return [
        ("日経", _gnews(f"{ja_query} when:7d site:nikkei.com", hl="ja", gl="JP", ceid="JP:ja"), True),
        ("Bloomberg", _gnews(f"{en_query} when:7d site:bloomberg.com", hl="en-US", gl="US", ceid="US:en"), True),
        ("Reuters", _gnews(f"{en_query} when:7d site:reuters.com", hl="en-US", gl="US", ceid="US:en"), True),
        ("CNBC", _gnews(f"{en_query} when:7d site:cnbc.com", hl="en-US", gl="US", ceid="US:en"), True),
        ("WSJ", _gnews(f"{en_query} when:7d site:wsj.com", hl="en-US", gl="US", ceid="US:en"), True),
        ("日刊工業", _gnews(f"{ja_query} when:7d site:nikkan.co.jp", hl="ja", gl="JP", ceid="JP:ja"), True),
        ("東洋経済", _gnews(f"{ja_query} when:7d site:toyokeizai.net", hl="ja", gl="JP", ceid="JP:ja"), True),
    ]


HEADLINE_CONFIG: dict[str, dict] = {
    "semi": {
        "feeds": _feeds("半導体", "semiconductor") + [
            ("日経xTECH", "https://xtech.nikkei.com/rss/index.rdf", True),
            ("ITmedia", "https://rss.itmedia.co.jp/rss/2.0/tf_electronics.xml", False),
            ("EE Times Japan", "https://rss.itmedia.co.jp/rss/2.0/eetimes.xml", False),
            ("DigiTimes", "https://www.digitimes.com/rss/daily.xml", True),
            ("SemiEngineering", "https://semiengineering.com/feed/", False),
            ("Tom's Hardware", "https://www.tomshardware.com/feeds/tag/semiconductors", False),
        ],
        "keywords": (
            "半導体", "semiconductor", "chip", "foundry", "hbm", "gpu", "asml", "tsmc", "nvidia",
        ),
    },
    "defense": {
        "feeds": _feeds("防衛", "defense") + [
            ("SpaceNews", "https://spacenews.com/feed/", False),
        ],
        "keywords": (
            "防衛", "defense", "defence", "military", "missile", "fighter", "F-35", "AUKUS", "drone",
        ),
    },
    "ai-dc": {
        "feeds": _feeds("データセンター AI", "AI data center") + [
            ("Tom's Hardware", "https://www.tomshardware.com/feeds/tag/artificial-intelligence", False),
        ],
        "keywords": (
            "データセンター", "data center", "AI", "GPU", "hyperscaler", "NVIDIA", "Blackwell", "liquid cooling",
        ),
    },
    "space": {
        "feeds": _feeds("宇宙", "space") + [
            ("SpaceNews", "https://spacenews.com/feed/", False),
        ],
        "keywords": (
            "宇宙", "space", "satellite", "rocket", "launch", "SpaceX", "衛星", "ロケット",
        ),
    },
    "nuclear": {
        "feeds": _feeds("原子力", "nuclear power") + [],
        "keywords": (
            "原子力", "nuclear", "uranium", "SMR", "再稼働", "ウラン", "原発",
        ),
    },
}
