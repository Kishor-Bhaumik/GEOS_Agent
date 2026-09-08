import sys
import re

def swap_to_vtk(input_path, output_path):
    with open(input_path) as f:
        content = f.read()
    new_content = re.sub(r'<Silo(\s+name="[^"]+"\s*/>)', r'<VTK\1', content)
    if new_content == content:
        print("WARNING: no Silo output block found or replacement failed")
    with open(output_path, 'w') as f:
        f.write(new_content)
    print(f"Wrote {output_path}")

if __name__ == "__main__":
    swap_to_vtk(sys.argv[1], sys.argv[2])
