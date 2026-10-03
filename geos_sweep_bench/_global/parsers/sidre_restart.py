#!/usr/bin/env python3
"""Format-level Sidre/Conduit restart HDF5 inspector (GEOS Restart output).

Sidre stores arrays under a dataset named '__values__' inside a group named after
the field. Groups themselves often have dtype '|V1' and no numeric payload.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

import h5py
import numpy as np


def _walk_datasets(group: h5py.Group, prefix: str = ""):
    try:
        keys = list(group.keys())
    except Exception:
        return
    for k in keys:
        try:
            item = group.get(k)
        except Exception:
            continue
        if item is None:
            continue
        path = f"{prefix}/{k}" if prefix else str(k)
        if isinstance(item, h5py.Dataset):
            yield path, item
        elif isinstance(item, h5py.Group):
            yield from _walk_datasets(item, path)


def list_numeric_fields(path: str | Path, leaf_name: str = "__values__") -> dict[str, dict[str, Any]]:
    path = Path(path)
    out: dict[str, dict[str, Any]] = {}
    with h5py.File(path, "r") as f:
        for pth, ds in _walk_datasets(f):
            if not pth.endswith(leaf_name):
                continue
            if ds.shape is None:
                continue
            if not np.issubdtype(ds.dtype, np.number):
                continue
            arr = np.array(ds[()], dtype=float)
            finite = arr[np.isfinite(arr)]
            field = pth[: -len(leaf_name)].rstrip("/")
            info: dict[str, Any] = {
                "path": pth,
                "field": field,
                "shape": list(arr.shape),
                "dtype": str(ds.dtype),
                "n": int(arr.size),
            }
            if finite.size:
                info["min"] = float(finite.min())
                info["max"] = float(finite.max())
                info["mean"] = float(finite.mean())
            out[field] = info
    return out


def field_array(path: str | Path, field_suffix: str) -> np.ndarray | None:
    """Return the first '__values__' array whose field path endswith field_suffix."""
    path = Path(path)
    with h5py.File(path, "r") as f:
        for pth, ds in _walk_datasets(f):
            if pth.endswith(field_suffix + "/__values__") or pth.endswith(field_suffix):
                if isinstance(ds, h5py.Dataset) and ds.shape is not None:
                    return np.array(ds[()])
    return None
