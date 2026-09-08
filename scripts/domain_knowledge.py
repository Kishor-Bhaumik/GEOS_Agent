"""
Domain-knowledge retrieval: instead of hand-writing a physics-fact lookup
table per physics family (which cannot scale to GEOS's full solver set),
this reads the solver's OWN documentation directly from the GEOS repo.
"""
import glob
import os
import re
import xml.etree.ElementTree as ET


KNOWN_SOLVER_TAGS = {
    "SinglePhaseFVM", "CompositionalMultiphaseFVM", "SolidMechanicsLagrangianFEM",
    "SinglePhasePoromechanics", "MultiphasePoromechanics", "LaplaceFEM",
    "PhaseFieldFracture", "SinglePhaseHybridFVM", "SinglePhaseWell",
}


def get_solver_name(deck_path):
    tree = ET.parse(deck_path)
    root = tree.getroot()
    solvers_block = root.find("Solvers")
    if solvers_block is None:
        return None
    for child in solvers_block:
        tag = child.tag
        if tag in KNOWN_SOLVER_TAGS:
            return tag
    return solvers_block[0].tag if len(solvers_block) else None


def find_solver_doc(solver_name, geos_root):
    if not solver_name:
        return None
    search_root = os.path.join(geos_root, "src", "coreComponents", "physicsSolvers")
    candidates = glob.glob(
        os.path.join(search_root, "**", "docs", "*.rst"), recursive=True
    )
    for path in candidates:
        if os.path.splitext(os.path.basename(path))[0].lower() == solver_name.lower():
            return path
    for path in candidates:
        try:
            with open(path, errors="ignore") as f:
                content = f.read()
            if solver_name in content:
                return path
        except OSError:
            continue
    return None


def extract_governing_equations_section(rst_path, max_chars=3000):
    with open(rst_path, errors="ignore") as f:
        content = f.read()

    match = re.search(
        r"Governing Equations.*?(?=\n[A-Z][a-zA-Z ]+\n-{3,}\n|\Z)",
        content, re.DOTALL,
    )
    section = match.group(0) if match else content

    if len(section) > max_chars:
        section = section[:max_chars] + "\n... [truncated]"
    return section.strip()


def get_domain_knowledge(deck_path, geos_root):
    solver_name = get_solver_name(deck_path)
    doc_path = find_solver_doc(solver_name, geos_root)
    if doc_path is None:
        return None
    return {
        "solver_name": solver_name,
        "doc_path": doc_path,
        "excerpt": extract_governing_equations_section(doc_path),
    }
