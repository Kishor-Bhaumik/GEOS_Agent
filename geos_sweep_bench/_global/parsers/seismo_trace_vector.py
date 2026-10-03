#!/usr/bin/env python3
"""Read a 3-component receiver trace written as three concatenated blocks.

Each block is ASCII rows of: sample_index time value.
Blocks are x, then y, then z, with the same time column.
"""
from __future__ import annotations

from pathlib import Path

import numpy as np


def read_seismo_vector(path: str | Path) -> dict:
    arr = np.loadtxt(path)
    if arr.ndim != 2 or arr.shape[1] < 3:
        raise ValueError(f"unexpected trace shape in {path}")
    if arr.shape[0] % 3 != 0:
        raise ValueError(f"trace length not divisible by 3: {path}")
    n = arr.shape[0] // 3
    time = arr[:n, 1].astype(float)
    blocks = [arr[i * n : (i + 1) * n, 2].astype(float) for i in range(3)]
    if not (np.allclose(time, arr[n : 2 * n, 1]) and np.allclose(time, arr[2 * n :, 1])):
        raise ValueError(f"component time axes differ: {path}")
    return {"time": time, "x": blocks[0], "y": blocks[1], "z": blocks[2]}
