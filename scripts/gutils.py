"""
Shared utilities for the GEOS agent eval/extraction pipeline.

Key lesson encoded here: GEOS output directory structure is NOT fixed.
Output block name (siloOutput/vtkOutput/...), mesh name, and region name
all vary per deck. Never hardcode a path pattern - always discover it.
"""
import glob
import os
import re
from collections import defaultdict


def find_vtu_files(output_dir):
    """
    Recursively find all .vtu files under output_dir and group them by
    timestep index (the zero-padded numeric directory, e.g. '000010').

    Returns: dict[str, list[str]]  e.g. {'000000': [...], '000010': [...]}
    """
    all_vtu = glob.glob(os.path.join(output_dir, "**", "*.vtu"), recursive=True)
    if not all_vtu:
        raise FileNotFoundError(
            f"No .vtu files found under {output_dir}. "
            f"Check that the deck's Outputs block uses VTK (not Silo), "
            f"and that the run actually completed."
        )

    groups = defaultdict(list)
    step_pattern = re.compile(r"(\d{6})")  # matches the 6-digit timestep folder
    for path in all_vtu:
        parts = path.split(os.sep)
        step_id = None
        for part in parts:
            if step_pattern.fullmatch(part):
                step_id = part
                break
        if step_id is None:
            step_id = "unknown"
        groups[step_id].append(path)

    return dict(groups)


def latest_timestep(vtu_groups):
    """Given the dict from find_vtu_files, return the key of the latest timestep."""
    numeric_keys = [k for k in vtu_groups if k.isdigit()]
    if not numeric_keys:
        raise ValueError("No numeric timestep folders found in vtu_groups.")
    return max(numeric_keys, key=lambda k: int(k))


def extract_field_profile(vtu_paths, field_name, coord_index=0):
    """
    Read one or more .vtu files (multiple files = multiple regions at the
    same timestep, as in spf_003) and return merged, sorted (x, value) arrays.

    coord_index: 0 for x, 1 for y, 2 for z cell-center coordinate.
    """
    import numpy as np
    import pyvista as pv

    xs, vals = [], []
    for path in vtu_paths:
        mesh = pv.read(path)
        if field_name not in mesh.cell_data:
            available = list(mesh.cell_data.keys())
            raise KeyError(
                f"Field '{field_name}' not found in {path}. "
                f"Available fields: {available}"
            )
        centers = mesh.cell_centers().points[:, coord_index]
        values = mesh.cell_data[field_name]
        xs.extend(centers.tolist())
        vals.extend(np.asarray(values).tolist())

    order = np.argsort(xs)
    xs_sorted = np.asarray(xs)[order]
    vals_sorted = np.asarray(vals)[order]
    return xs_sorted, vals_sorted


def interpolate_at_x(xs_sorted, vals_sorted, x_query):
    """
    Linear interpolation of a 1D profile at x_query.
    Raises if x_query falls outside the profile's range (extrapolation
    is a silent-error risk we don't want in this pipeline).
    """
    import numpy as np

    if x_query < xs_sorted[0] or x_query > xs_sorted[-1]:
        raise ValueError(
            f"x_query={x_query} is outside the profile range "
            f"[{xs_sorted[0]}, {xs_sorted[-1]}]. Refusing to extrapolate."
        )
    return float(np.interp(x_query, xs_sorted, vals_sorted))


def get_qoi_at_x(output_dir, field_name, x_query, timestep=None, coord_index=0):
    """
    High-level convenience function tying the above together:
    find files -> pick timestep -> extract profile -> interpolate.
    """
    groups = find_vtu_files(output_dir)
    step = timestep if timestep is not None else latest_timestep(groups)
    xs, vals = extract_field_profile(groups[step], field_name, coord_index)
    value = interpolate_at_x(xs, vals, x_query)
    return {
        "timestep_used": step,
        "x_query": x_query,
        "field": field_name,
        "value": value,
        "n_source_files": len(groups[step]),
    }
