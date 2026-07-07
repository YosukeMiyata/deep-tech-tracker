#!/usr/bin/env python3
"""工程マップ・フロー図 JSON を themes 銘柄マスタから生成する。"""

from __future__ import annotations

import argparse
import importlib
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from theme_config import SECTOR_IDS, data_dir, slug_to_module  # noqa: E402


def resolve_codes(codes: list[str], symbols: dict[str, tuple[str, str]], alias: dict) -> list[dict]:
    out: list[dict] = []
    seen: set[str] = set()
    for raw in codes:
        code = alias.get(raw, raw)
        if code in symbols and code not in seen:
            name, market = symbols[code]
            out.append({"code": code, "name": name, "market": market})
            seen.add(code)
    return out


def build_process(process_map: list, symbols: dict, alias: dict) -> list[dict]:
    proc: list[dict] = []
    for step in process_map:
        item: dict = {
            "stage": step["stage"],
            "name": step["name"],
            "desc": step.get("desc", ""),
            "icon": step.get("icon", ""),
        }
        if "groups" in step:
            item["groups"] = [
                {"label": g["label"], "stocks": resolve_codes(g["stocks"], symbols, alias)}
                for g in step["groups"]
            ]
        else:
            item["equip"] = resolve_codes(step.get("equip", []), symbols, alias)
            item["material"] = resolve_codes(step.get("material", []), symbols, alias)
        proc.append(item)
    return proc


def build_maps_payload(theme: str) -> tuple[dict, dict]:
    mod_name = slug_to_module(theme)
    theme_mod = importlib.import_module(f"themes.{mod_name}")
    process_mod = importlib.import_module(f"maps.{mod_name}.process_map")
    flow_mod = importlib.import_module(f"maps.{mod_name}.flow_map")

    symbols = theme_mod.all_symbols()
    alias = getattr(process_mod, "ALIAS", {})
    process_payload = {
        "source": f"pipeline/maps/{mod_name}/process_map.py",
        "steps": build_process(process_mod.PROCESS_MAP, symbols, alias),
    }
    flow_payload = {
        "source": f"pipeline/maps/{mod_name}/flow_map.py",
        "stages": flow_mod.resolve_flow(symbols),
    }
    return process_payload, flow_payload


def build_for_theme(theme: str) -> None:
    process_payload, flow_payload = build_maps_payload(theme)
    out_dir = data_dir(theme)
    out_dir.mkdir(parents=True, exist_ok=True)
    process_path = out_dir / "process.json"
    flow_path = out_dir / "flow.json"
    process_path.write_text(json.dumps(process_payload, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    flow_path.write_text(json.dumps(flow_payload, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    n_proc = len(process_payload["steps"])
    n_flow = len(flow_payload["stages"])
    print(f"wrote {theme}/process.json ({n_proc} 工程)")
    print(f"wrote {theme}/flow.json ({n_flow} ステージ)")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--theme", default="semi", choices=SECTOR_IDS)
    args = parser.parse_args()
    build_for_theme(args.theme)


if __name__ == "__main__":
    main()
