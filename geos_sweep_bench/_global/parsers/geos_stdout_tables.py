#!/usr/bin/env python3
"""Parse GEOS TableTextFormatter blocks from a solver stdout log.

Reusable across decks: finds titled ASCII tables (min/average/max statistics,
CFL lines, solver summary tables) without assuming a particular physics.
"""
from __future__ import annotations

import re
from pathlib import Path
from typing import Any


_TITLE = re.compile(r"^\|\s*(.+?)\s*\|$")
_CFL = re.compile(
    r"^(?P<name>\S+) \(time (?P<time>[0-9.eE+-]+) s\): Max (?P<kind>.+?) CFL number: (?P<value>[0-9.eE+-]+)"
)


def _clean(cell: str) -> str:
    return " ".join(cell.strip().split())


def parse_stdout_tables(path: str | Path) -> dict[str, Any]:
    text = Path(path).read_text(errors="replace")
    lines = text.splitlines()
    tables: list[dict[str, Any]] = []
    cfl: list[dict[str, Any]] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        m = _CFL.search(line.strip())
        if m:
            cfl.append({
                "name": m.group("name"),
                "time": float(m.group("time")),
                "kind": m.group("kind").strip(),
                "value": float(m.group("value")),
            })
            i += 1
            continue
        if line.startswith("|") and set(line.strip()) <= set("|- ") and "---" in line:
            # possible table: scan upward for title row
            i += 1
            continue
        i += 1

    # region-statistics tables: title contains "(time <t> s)"
    time_title = re.compile(
        r"^\|\s*(?P<title>.+?) \(time (?P<time>[0-9.eE+-]+) s\):\s*\|$"
    )
    i = 0
    while i < len(lines):
        m = time_title.match(lines[i].rstrip())
        if not m:
            i += 1
            continue
        title = m.group("title").strip()
        t = float(m.group("time"))
        # consume until a row of only dashes/pipes ends the table (a full-width dash line
        # with no interior spaces as cells, after header)
        block = [lines[i]]
        i += 1
        while i < len(lines):
            block.append(lines[i])
            stripped = lines[i].strip()
            if stripped.startswith("|") and re.fullmatch(r"\|-+\|?", stripped.replace(" ", "")):
                # closing rule: a line that is almost all dashes after we have seen data
                if len(block) > 6:
                    i += 1
                    break
            if not stripped.startswith("|") and len(block) > 6:
                break
            i += 1
        rows = _parse_stat_block(block)
        tables.append({"title": title, "time": t, "rows": rows, "raw_n_lines": len(block)})
    return {"path": str(path), "tables": tables, "cfl": cfl}


def _parse_stat_block(block: list[str]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    pending_name = None
    pending_phase = None
    for line in block:
        if not line.startswith("|"):
            continue
        parts = [p.strip() for p in line.strip().strip("|").split("|")]
        if not parts or set("".join(parts)) <= set("- "):
            continue
        if "statistics" in parts[0].lower() and "min" in "".join(parts).lower():
            continue
        # 4-col: name, min, avg, max
        if len(parts) >= 4 and parts[0] and any(ch.isdigit() for ch in "".join(parts[1:])):
            rows.append({
                "quantity": parts[0],
                "phase": "",
                "min": parts[1],
                "average": parts[2] if parts[2] != "/" else "",
                "max": parts[3],
                "value": parts[3] if len(parts) == 4 and not parts[1].replace(".", "").replace("e", "").replace("E", "").replace("-", "").replace("+", "").isdigit() else parts[-1],
            })
            continue
        # wrapped phase rows: first col empty or quantity, second is phase name, last is value
        if len(parts) >= 2:
            name = parts[0]
            if name:
                pending_name = name
            phase = parts[1] if len(parts) > 1 else ""
            val = parts[-1]
            if pending_name and (phase or val) and not set(val) <= set("- "):
                rows.append({
                    "quantity": pending_name,
                    "phase": phase,
                    "min": "",
                    "average": "",
                    "max": "",
                    "value": val,
                })
    return rows


def region_series(parsed: dict[str, Any], title_substr: str, quantity_substr: str, phase: str = "") -> list[tuple[float, float]]:
    out = []
    for tab in parsed.get("tables") or []:
        if title_substr not in tab["title"]:
            continue
        for row in tab["rows"]:
            if quantity_substr.lower() not in row["quantity"].lower():
                continue
            if phase and row.get("phase", "").lower() != phase.lower():
                continue
            raw = row.get("average") or row.get("value") or row.get("max")
            try:
                out.append((float(tab["time"]), float(raw)))
            except (TypeError, ValueError):
                continue
    return out
