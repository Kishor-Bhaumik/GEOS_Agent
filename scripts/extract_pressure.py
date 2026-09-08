import sys
import pyvista as pv

def extract_pressure(vtu_path, field="pressure"):
    mesh = pv.read(vtu_path)
    x = mesh.cell_centers().points[:, 0]
    p = mesh.cell_data[field]
    for xi, pi in sorted(zip(x, p)):
        print(f"x={xi:.4f}  pressure={pi:.6f}")

if __name__ == "__main__":
    extract_pressure(sys.argv[1])
