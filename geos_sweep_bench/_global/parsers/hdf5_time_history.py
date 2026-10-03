#!/usr/bin/env python3
"""Generic HDF5 TimeHistory reader for GEOS PackCollection / TimeHistory output.

Each field has a matching "<field> Time" dataset whose time array has shape (n, 1);
ravel() it. phaseVolumeFraction has shape (time, cell, phase), phases in deck order.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

import h5py
import numpy as np


def _to_str(x) -> str:
    if isinstance(x, bytes):
        return x.decode("utf-8")
    return str(x)


def list_datasets(path: str | Path) -> list[str]:
    names: list[str] = []

    def walk(g, prefix=""):
        for k in g:
            item = g[k]
            p = f"{prefix}/{k}" if prefix else k
            if isinstance(item, h5py.Dataset):
                names.append(p)
            else:
                walk(item, p)

    with h5py.File(path, "r") as f:
        walk(f)
    return names


def read_time_history(path: str | Path) -> dict[str, Any]:
    path = Path(path)
    fields: dict[str, dict[str, Any]] = {}
    with h5py.File(path, "r") as f:
        datasets = {}

        def walk(g, prefix=""):
            for k in g:
                item = g[k]
                p = f"{prefix}/{k}" if prefix else k
                if isinstance(item, h5py.Dataset):
                    datasets[p] = np.array(item)
                else:
                    walk(item, p)

        walk(f)

    time_keys = {k[: -len(" Time")]: k for k in datasets if k.endswith(" Time")}
    for field, tkey in time_keys.items():
        data = datasets[field]
        t = np.ravel(datasets[tkey]).astype(float)
        fields[field] = {
            "time": t,
            "data": data,
            "shape": list(data.shape),
        }
    leftover = {}
    leftover_arrays = {}
    for k, v in datasets.items():
        if k in time_keys.values() or k in fields:
            continue
        leftover[k] = {"shape": list(v.shape), "dtype": str(v.dtype)}
        leftover_arrays[k] = v
    return {
        "path": str(path),
        "fields": fields,
        "other_datasets": leftover,
        "other_arrays": leftover_arrays,
    }


def field_at_time(hist: dict, field: str, t: float, rtol: float = 1e-9, atol: float = 1e-12) -> np.ndarray:
    f = hist["fields"][field]
    times = f["time"]
    idx = int(np.argmin(np.abs(times - t)))
    if not np.isclose(times[idx], t, rtol=rtol, atol=atol):
        raise ValueError(f"time {t} not in {field} Time array (nearest {times[idx]})")
    return f["data"][idx]


def first_crossing(times: np.ndarray, values: np.ndarray, threshold: float, side: str = "above") -> float | None:
    """First time values cross threshold. Linear interpolation between samples."""
    v = np.ravel(values).astype(float)
    t = np.ravel(times).astype(float)
    if side == "above":
        hit = v >= threshold
    else:
        hit = v <= threshold
    if not np.any(hit):
        return None
    i = int(np.argmax(hit))
    if i == 0:
        return float(t[0])
    t0, t1 = t[i - 1], t[i]
    v0, v1 = v[i - 1], v[i]
    if v1 == v0:
        return float(t1)
    frac = (threshold - v0) / (v1 - v0)
    frac = min(max(frac, 0.0), 1.0)
    return float(t0 + frac * (t1 - t0))
