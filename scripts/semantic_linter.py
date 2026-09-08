"""
Semantic linter for GEOS XML decks.

xmllint / XSD validation only checks grammar (are tags and attributes
allowed). It does NOT check that names referenced across blocks actually
resolve - e.g. a solver's targetRegions pointing at a region that was
never declared. That class of error is schema-valid and passes xmllint,
but GEOS dies on it at initialization. This linter catches those before
we ever launch the binary.
"""
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field


@dataclass
class LintIssue:
    severity: str
    code: str
    message: str
    bad_value: str = None
    valid_candidates: list = None


@dataclass
class LintResult:
    issues: list = field(default_factory=list)

    @property
    def has_errors(self):
        return any(i.severity == "error" for i in self.issues)

    def add(self, severity, code, message, bad_value=None, valid_candidates=None):
        self.issues.append(
            LintIssue(severity, code, message, bad_value, valid_candidates)
        )

    def report(self):
        if not self.issues:
            return "No issues found."
        lines = []
        for i in self.issues:
            lines.append(f"[{i.severity.upper()}] {i.code}: {i.message}")
        return "\n".join(lines)


def _parse_name_list(raw):
    if raw is None:
        return []
    cleaned = raw.strip().lstrip("{").rstrip("}").strip()
    if not cleaned:
        return []
    return [x.strip() for x in cleaned.split(",")]


def lint_deck(xml_path):
    result = LintResult()
    try:
        tree = ET.parse(xml_path)
    except ET.ParseError as e:
        result.add("error", "E_XML_PARSE", f"XML parse error: {e}")
        return result

    root = tree.getroot()

    region_names = set()
    for region in root.findall(".//ElementRegions/*"):
        name = region.get("name")
        if name:
            region_names.add(name)

    constitutive_names = set()
    constitutive_block = root.find("Constitutive")
    if constitutive_block is not None:
        for model in constitutive_block:
            name = model.get("name")
            if name:
                constitutive_names.add(name)

    discretization_names = set()
    for nm in root.findall(".//NumericalMethods/*/*"):
        name = nm.get("name")
        if name:
            discretization_names.add(name)

    geometry_set_names = {"all", "xneg", "xpos", "yneg", "ypos", "zneg", "zpos"}
    for geo in root.findall(".//Geometry/*"):
        name = geo.get("name")
        if name:
            geometry_set_names.add(name)

    solver_names = set()
    solvers_block = root.find("Solvers")
    if solvers_block is not None:
        for solver in solvers_block:
            name = solver.get("name")
            if name:
                solver_names.add(name)

    output_names = set()
    outputs_block = root.find("Outputs")
    if outputs_block is not None:
        for out in outputs_block:
            name = out.get("name")
            if name:
                output_names.add(name)

    if solvers_block is not None:
        for solver in solvers_block:
            target_regions = _parse_name_list(solver.get("targetRegions"))
            for tr in target_regions:
                if tr not in region_names:
                    result.add(
                        "error", "E_REGION_REF",
                        f"Solver '{solver.get('name')}' targetRegions references "
                        f"'{tr}', which is not declared in <ElementRegions>. "
                        f"Declared regions: {sorted(region_names)}",
                        bad_value=tr, valid_candidates=sorted(region_names),
                    )

            disc = solver.get("discretization")
            if disc and disc not in discretization_names:
                result.add(
                    "error", "E_DISCRETIZATION_REF",
                    f"Solver '{solver.get('name')}' discretization='{disc}' "
                    f"not found in <NumericalMethods>. "
                    f"Declared: {sorted(discretization_names)}",
                    bad_value=disc, valid_candidates=sorted(discretization_names),
                )

    for region in root.findall(".//ElementRegions/*"):
        materials = _parse_name_list(region.get("materialList"))
        for m in materials:
            if m not in constitutive_names:
                result.add(
                    "error", "E_MATERIAL_REF",
                    f"ElementRegion '{region.get('name')}' materialList references "
                    f"'{m}', which is not declared in <Constitutive>. "
                    f"Declared: {sorted(constitutive_names)}",
                    bad_value=m, valid_candidates=sorted(constitutive_names),
                )

    events_block = root.find("Events")
    if events_block is not None:
        for event in events_block:
            target = event.get("target")
            if target is None:
                continue
            parts = [p for p in target.strip("/").split("/") if p]
            if len(parts) != 2:
                result.add(
                    "warning", "W_EVENT_TARGET_FORM",
                    f"Event '{event.get('name')}' target='{target}' does not "
                    f"look like '/Solvers/<name>' or '/Outputs/<name>'."
                )
                continue
            block, name = parts
            if block == "Solvers" and name not in solver_names:
                result.add(
                    "error", "E_EVENT_TARGET_REF",
                    f"Event '{event.get('name')}' targets Solvers/'{name}', "
                    f"which is not declared. Declared solvers: {sorted(solver_names)}",
                    bad_value=name, valid_candidates=sorted(solver_names),
                )
            elif block == "Outputs" and name not in output_names:
                result.add(
                    "error", "E_EVENT_TARGET_REF",
                    f"Event '{event.get('name')}' targets Outputs/'{name}', "
                    f"which is not declared. Declared outputs: {sorted(output_names)}",
                    bad_value=name, valid_candidates=sorted(output_names),
                )

    for fs in root.findall(".//FieldSpecifications/*"):
        set_names = _parse_name_list(fs.get("setNames"))
        for sn in set_names:
            if sn not in geometry_set_names:
                result.add(
                    "warning", "W_SETNAME_REF",
                    f"FieldSpecification '{fs.get('name')}' setNames references "
                    f"'{sn}', not found in <Geometry> (or 'all'). This may be a "
                    f"mesh-generated set (e.g. 'source'/'sink' from InternalMesh "
                    f"boundaries) which this linter cannot verify - check manually."
                )

    for perm in root.findall(".//ConstantPermeability"):
        raw = perm.get("permeabilityComponents")
        if raw:
            try:
                vals = [float(v) for v in _parse_name_list(raw)]
                for v in vals:
                    if abs(v) > 1e-8:
                        result.add(
                            "warning", "W_UNIT_MAGNITUDE",
                            f"Permeability component {v} in '{perm.get('name')}' "
                            f"looks too large for m^2 (typical rock: 1e-11 to 1e-19). "
                            f"Check for a units mistake (e.g. mD instead of m^2)."
                        )
            except ValueError:
                pass

    return result


if __name__ == "__main__":
    import sys
    result = lint_deck(sys.argv[1])
    print(result.report())
    sys.exit(1 if result.has_errors else 0)
