"""
Curated anchor index - lightweight "retrieval" for the first NL->deck
prototype. Just filename + a one-line description per deck, handed to the
LLM so it can pick the closest match.
"""

ANCHOR_DECKS = [
    {
        "filename": "incompressible_1d.xml",
        "relpath": "inputFiles/singlePhaseFlow/incompressible_1d.xml",
        "description": (
            "1D single-phase flow, 10m domain, incompressible fluid "
            "(compressibility=0), fixed pressure boundary conditions at "
            "both ends (source and sink), single timestep to steady state."
        ),
    },
    {
        "filename": "compressible_1d.xml",
        "relpath": "inputFiles/singlePhaseFlow/compressible_1d.xml",
        "description": (
            "1D single-phase flow, 10m domain, compressible fluid, fixed "
            "pressure boundary conditions at both ends, transient (20 "
            "timesteps, not yet at steady state by t=1.0)."
        ),
    },
    {
        "filename": "compressible_1d_2solids.xml",
        "relpath": "inputFiles/singlePhaseFlow/compressible_1d_2solids.xml",
        "description": (
            "1D single-phase flow, 10m domain split into two different "
            "rock materials (0-5m and 5-10m), compressible fluid, fixed "
            "pressure boundary conditions at both ends."
        ),
    },
    {
        "filename": "sourceFlux_1d.xml",
        "relpath": "inputFiles/singlePhaseFlow/sourceFlux_1d.xml",
        "description": (
            "1D single-phase flow, 10m domain, compressible fluid, "
            "uniform initial pressure, fixed pressure at one end (sink), "
            "mass injection via SourceFlux at the other end (source) "
            "instead of a pressure BC."
        ),
    },
    {
        "filename": "thermalViscosity_1d.xml",
        "relpath": "inputFiles/singlePhaseFlow/thermalViscosity_1d.xml",
        "description": (
            "1D single-phase flow, ~20m domain, compressible fluid with "
            "temperature-dependent viscosity, coupled thermal transport, "
            "fixed pressure and temperature boundary conditions at both ends."
        ),
    },
    {
        "filename": "symmetric_permeability_base.xml",
        "relpath": "geosagent/eval/decks/symmetric_permeability_base.xml",
        "description": (
            "1D single-phase flow, 10m domain split into two sections with "
            "IDENTICAL compressibility, porosity, and permeability by default. "
            "Section A uses permeability model rockPerm, Section B uses a "
            "SEPARATE permeability model rockPerm2 (same default value) - "
            "edit rockPerm2's permeabilityComponents to test permeability "
            "sensitivity in Section B without affecting Section A. Fixed "
            "pressure boundary conditions at both ends."
        ),
    },
]


def format_anchor_list_for_prompt():
    lines = []
    for d in ANCHOR_DECKS:
        lines.append(f"- {d['filename']}: {d['description']}")
    return "\n".join(lines)


def get_anchor_by_filename(filename):
    for d in ANCHOR_DECKS:
        if d["filename"] == filename:
            return d
    raise KeyError(f"Unknown anchor filename: {filename}")
