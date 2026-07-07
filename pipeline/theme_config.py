# -*- coding: utf-8 -*-
"""Deep Tech Tracker — セクター設定ローダー。"""

from __future__ import annotations

import importlib
import json
from pathlib import Path
from types import ModuleType

ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "config" / "site.json"

# slug (URL/data dir) → Python module suffix
SECTOR_IDS = ("semi", "defense", "ai-dc", "space", "nuclear")
MODULE_SUFFIX = {
    "semi": "semi",
    "defense": "defense",
    "ai-dc": "ai_dc",
    "space": "space",
    "nuclear": "nuclear",
}


def slug_to_module(sector_id: str) -> str:
    if sector_id not in MODULE_SUFFIX:
        raise KeyError(f"unknown sector: {sector_id}")
    return MODULE_SUFFIX[sector_id]


def load_site_config() -> dict:
    return json.loads(CONFIG_PATH.read_text(encoding="utf-8"))


def sector_config(sector_id: str) -> dict:
    for s in load_site_config()["sectors"]:
        if s["id"] == sector_id:
            return s
    raise KeyError(f"unknown sector: {sector_id}")


def data_dir(sector_id: str) -> Path:
    return ROOT / "data" / sector_id


def load_theme_module(sector_id: str) -> ModuleType:
    mod = slug_to_module(sector_id)
    return importlib.import_module(f"themes.{mod}")


def load_map_module(sector_id: str, map_name: str) -> ModuleType:
    mod = slug_to_module(sector_id)
    return importlib.import_module(f"maps.{mod}.{map_name}")
