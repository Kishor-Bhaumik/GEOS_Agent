#!/usr/bin/env python3
"""Format-level VTK UnstructuredGrid reader (GEOS .vtu / .pvd collections)."""
from __future__ import annotations

from pathlib import Path
from typing import Any

import numpy as np

try:
    import vtk
    from vtk.util.numpy_support import vtk_to_numpy
except ImportError as e:  # pragma: no cover
    raise ImportError("vtk is required to parse GEOS VTK output") from e


def read_vtu(path: str | Path) -> dict[str, Any]:
    path = Path(path)
    reader = vtk.vtkXMLUnstructuredGridReader()
    reader.SetFileName(str(path))
    reader.Update()
    ug = reader.GetOutput()

    time = None
    fd = ug.GetFieldData()
    tarr = fd.GetArray("TIME")
    if tarr is not None:
        time = float(vtk_to_numpy(tarr).ravel()[0])

    def _arrays(attr) -> dict[str, np.ndarray]:
        out = {}
        for i in range(attr.GetNumberOfArrays()):
            arr = attr.GetArray(i)
            if arr is None:
                continue
            out[arr.GetName()] = np.array(vtk_to_numpy(arr))
        return out

    cell_data = _arrays(ug.GetCellData())
    point_data = _arrays(ug.GetPointData())

    pts_vtk = ug.GetPoints()
    points = (
        np.array(vtk_to_numpy(pts_vtk.GetData()), dtype=float)
        if pts_vtk is not None
        else np.zeros((0, 3), dtype=float)
    )

    ncells = ug.GetNumberOfCells()
    centroids = np.zeros((ncells, 3), dtype=float)
    for i in range(ncells):
        cell = ug.GetCell(i)
        pts = [ug.GetPoint(cell.GetPointId(j)) for j in range(cell.GetNumberOfPoints())]
        centroids[i] = np.mean(pts, axis=0)

    summary = {}
    for name, a in cell_data.items():
        summary[name] = {
            "shape": list(a.shape),
            "dtype": str(a.dtype),
            "min": float(np.nanmin(a)) if a.size else None,
            "max": float(np.nanmax(a)) if a.size else None,
        }
    return {
        "path": str(path),
        "time": time,
        "npoints": int(ug.GetNumberOfPoints()),
        "ncells": int(ncells),
        "points": points,
        "centroids": centroids,
        "cell_data": cell_data,
        "point_data": point_data,
        "cell_data_summary": summary,
    }


def read_pvd(path: str | Path) -> list[dict[str, Any]]:
    """Read a .pvd collection.

    Each frame includes `vtu` (first region, backward compatible) and `vtus`
    (map of region name -> rank_0.vtu path).
    """
    import xml.etree.ElementTree as ET

    path = Path(path)
    root = ET.parse(path).getroot()
    collection = root.find("Collection")
    frames = []
    for ds in collection.findall("DataSet"):
        t = float(ds.attrib["timestep"])
        rel = ds.attrib["file"]
        vtm = path.parent / rel
        if vtm.suffix == ".vtu":
            vtus = [vtm]
        else:
            vtus = sorted(vtm.parent.glob(f"{vtm.stem}/**/rank_0.vtu"))
            if not vtus:
                vtus = sorted(vtm.parent.glob(f"{vtm.stem}/**/*.vtu"))
        regions = {p.parent.name: str(p) for p in vtus}
        first = vtus[0] if vtus else None
        frames.append({
            "timestep": t,
            "vtm": str(vtm),
            "vtu": str(first) if first else None,
            "vtus": regions,
        })
    return frames
