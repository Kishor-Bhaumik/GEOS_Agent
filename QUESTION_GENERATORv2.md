# GEOS Sweep Benchmark — Hard Question Generation and No-Tool Evaluation Protocol (v3)

## 0. Purpose

This file is the execution contract for a Cursor CLI controller agent. Execute it.
Do not summarise or explain it.

A question is GOOD (accepted) when the no-tool model gets it WRONG.

Every rule in this file is written for ANY GEOS deck and any physics (flow,
poromechanics, solid mechanics, fractures, thermal, waves, ...). Where CO2 or flow
details appear, they are examples only.

---

## 1. Configuration

All counts and limits below are variables. Refer to them by name. Never treat a number
in this file as fixed. Substitute configured values into prompts before sending them.

```text
PROTOCOL_VERSION           = 3
RUN_TAG                    = v3_run1     # change for every new experiment on the same deck

D                          = /home/kbhau001/codes/GEOS/geos_sweep_bench_v2
GEOS_ROOT                   = /home/kbhau001/codes/GEOS
INPUT_XML                  = inputFiles/thermoPoromechanicsFractures/ThermoPoroElastic_conforming_smoke.xml

GEOS_LINUX                 = /home/kbhau001/codes/GEOS/build-conda-geos-release/bin/geosx
GEOS_MACOS                 = <SET WHEN RUNNING ON MACOS>
CONDA_ENV                  = geos

AGENT_MODEL                = grok-4.7-high   # controller, generation, judge, diagnosis, everything except no tool model
NO_TOOL_MODEL              = gpt-5.6-sol            # no-tool solver ONLY

QUESTIONS_PER_PASS         = 15
MIN_INCORRECT_TO_VALIDATE  = 10
MAX_PASSES                 = 2
TOLERANCE_PERCENT          = 1.0      # starting value; may be revised in Pass 2 (Section 14)
MAX_QUESTIONS_PER_TEMPLATE = 2

MAX_SIMULATIONS_PER_PASS   = 1000     # sweep + pilots + refinement, all launches counted
REFINEMENT_RESERVE_RUNS    = 50       # kept free from the main sweep for refinement
PARALLEL_JOBS              = 28
MAX_FAILED_RUN_PERCENT     = 5

NO_TOOL_PARALLEL_JOBS      = 15
MAX_NO_TOOL_RERUNS         = 1
```

If `INPUT_XML` or the GEOS path for the current OS is still a placeholder, stop and
report it.

---

## 2. Non-negotiable rules

1. **Everything is written inside `D`.** No file, folder, log, script or output may be
   created anywhere else, including anywhere else in `GEOS_ROOT`. The GEOS repository
   is read-only.
2. **Never modify the original deck** or any file it includes. Work only on copies.
3. All GEOS and Python work runs in the `CONDA_ENV` conda environment:
   ```bash
   source "$(conda info --base)/etc/profile.d/conda.sh"
   conda activate geos
   export PYTHONDONTWRITEBYTECODE=1
   ```
   Never use system Python. Never use `sudo`. Install a missing package only inside
   `geos` (`python -m pip install <pkg>`) and append the package and version to
   `D/_global/environment/requirements_added.txt`.
4. **Every GEOS run gets its own new output directory.** Never reuse, share or
   overwrite an output directory. Never parse a generic `output/` shared by runs.
5. **All simulations in a pass use the same solver and time-stepping settings.** Sweep
   runs, pilots and refinement runs differ only in the swept inputs (and, where needed,
   output-recording frequency). Never change tolerances, time-step controls, or
   solver settings for individual runs to make them converge.
6. **The simulations are ground truth.** Every true answer must be traceable to
   specific runs. Never estimate, extrapolate, or invent a value.
7. **The no-tool model sees its fixed prompt, one question, and a read-only copy of the original deck** (Section 11).
   That copy is the original input XML, the XML files it includes, and the property tables and mesh files those point to.
   It does not see the swept case, the answer, any other question, the sweep table, simulation outputs, or the GEOS source.
8. Every question is frozen (text + SHA256) before any model answers it. A frozen
   question is never edited.
9. Never fabricate results, provenance, costs or tool-call counts. If a value is not
   available, record `null`.
10. The launch model must equal `AGENT_MODEL`. At startup, read the model reported in
    your own session; if it differs from `AGENT_MODEL`, stop and report.
11. **Reuse scripts; one command per stage.** Before writing any script, look in
    `D/_global/scripts/`. If a suitable script exists, run it. If you must write a new
    one, make it generic (not tied to one deck or question), save it there, and reuse
    it on later decks. Each mechanical stage (build + launch sweep, extract table,
    refinement bisection, freeze + verify, launch no-tool sessions, judge, finish)
    runs as ONE command, not one tool call per run or per question.
12. **Keep controller context small.** Never print a whole file, log, trace, CSV, or
    HDF5 dump. Every command prints at most ~50 lines (use `head`, `tail -n`, `wc`,
    or a Python summary). When waiting on a long job, wait inside one command
    (e.g. a loop with `sleep` that exits when the job is done or after a long
    interval) instead of checking repeatedly with separate tool calls.


---

## 3. Workspace layout

```text
D/
├── GEOS_SWEEP_BENCH.md            this protocol
├── _global/
│   ├── controller_logs/           launch-command logs (created by the user)
│   ├── environment/
│   │   ├── environment.json
│   │   └── requirements_added.txt
│   ├── pricing.json
│   ├── scripts/                   reusable scripts (verify.py, controller_cost.py, ...)
│   ├── parsers/                   reusable, format-level output readers
│   │   └── parser_registry.json
│   └── no_tool_workspaces/        one folder per no-tool run, containing only the original deck and its dependencies
│
└── decks/<deck_slug>/<RUN_TAG>/
    ├── source/                    copy of deck + included decks + property/data files
    │   └── source_manifest.json
    ├── exploration/
    │   ├── baseline/              input.xml, command.txt, stdout.log, stderr.log, run.json, output/
    │   ├── output_manifest.json
    │   └── deck_summary.md
    ├── pass1/
    │   ├── design.md              categories + sweep design
    │   ├── sweep/
    │   │   ├── sweep_config.json
    │   │   ├── template.xml
    │   │   ├── run_sweep.sh
    │   │   ├── extract_table.py
    │   │   ├── pilot/
    │   │   ├── runs/run_0001/ ... each: input.xml, run.json, output/   (stdout.log, stderr.log only if the run failed). Deleted at finish.
    │   │   ├── refine/<Qid>/ref_01/ ...   refinement runs (same layout as runs; observables.json is kept at finish)
    │   │   ├── sweep_table.csv
    │   │   ├── failed_runs.csv
    │   │   └── sweep_readme.md    compact provenance of how the sweep was built
    │   ├── generation/            prompt.txt, trace.jsonl, questions.json, cost.json (no copies of inputs)
    │   ├── questions/Q01 ... Q15/
    │   │   ├── question.txt       exact frozen text
    │   │   ├── answer_key.json       true answer + provenance (never shown to no-tool)
    │   │   ├── no_tool_trace.jsonl   (+ no_tool_trace_tryN.jsonl only if a contaminated try was discarded)
    │   │   ├── judge_trace.jsonl
    │   │   └── result.json         hash, verify results, tool check, answer text, verdict
    │   ├──pass_summary.csv
    │   └── pass_totals.csv
    ├── memory_A.md                only if Pass 1 does not validate; deleted at the end
    ├── diagnosis.md               only if Pass 2 runs
    ├── pass2/                     same layout as pass1, only if needed
    └── deck_result.json           VALIDATED or REJECTED
```

`deck_slug` = XML filename stem + `__` + first 8 hex characters of its SHA256,
e.g. `co2_hybrid_1d__a1b2c3d4`. All work of this experiment lives under
`decks/<deck_slug>/<RUN_TAG>/`; never read or reuse results from a different
`RUN_TAG`.

**Isolation rule:** every no-tool run gets its own new folder
`D/_global/no_tool_workspaces/<deck_slug>__<RUN_TAG>__p<pass>__<Qid>__try<n>/`. It must
be empty before the deck copy is placed in it. Copy in only the original input XML, the
XML files it includes, and the property tables and mesh files those point to. Do not copy
the GEOS source, other decks, `sweep_table.csv`, answer keys, or any output file.

---

## 4. Workflow overview

```text
0. Setup        create D tree, record environment
1. Explore      read deck + included decks + data files, copy to source/
2. Baseline     run once; if it fails, fix the working copy
3. Inspect      inventory baseline outputs, write deck_summary.md

── PASS p (p = 1, then 2 only if needed) ──
4. Design       categories + sweep axes (incl. a structural axis where possible)
5. Pilot        2–3 corner runs; fix if any fails
6. Sweep        ≤ MAX_SIMULATIONS_PER_PASS − REFINEMENT_RESERVE_RUNS runs, in parallel
7. Table        extract sweep_table.csv, write sweep_readme.md
8. Generate     one AGENT_MODEL call writes QUESTIONS_PER_PASS questions + answer keys
9. Refine       extra runs to pin threshold / timing / optimisation answers
10. Verify      script checks (verify.py) + agent review; rewrite failures; freeze
11. No-tool     one fresh isolated NO_TOOL_MODEL session per question, run in parallel;
                free tool-call check
12. Judge       one AGENT_MODEL call per question; script computes error fields
13. Decide      INCORRECT count ≥ MIN_INCORRECT_TO_VALIDATE → VALIDATED → step 15
                otherwise, if p < MAX_PASSES → step 14; else → REJECTED → step 15

14. Memory A + Diagnosis → Pass 2

15. Finish      deck_result.json, delete memory_A.md, summary tables, stop
```

---

## 5. Stage 0 — Setup

1. Create the directory tree under `D` for this `RUN_TAG`.
2. Detect the OS once. Linux → `GEOS_LINUX`, macOS → `GEOS_MACOS`. Confirm the
   binary exists and is executable.
3. Record in `D/_global/environment/environment.json`: OS, hostname, timestamp, GEOS
   binary path, GEOS git commit (read-only `git -C GEOS_ROOT rev-parse HEAD`), Python
   version, conda env, Cursor CLI version, `AGENT_MODEL`, `NO_TOOL_MODEL`, the model
   your own session reports, `PROTOCOL_VERSION`, `RUN_TAG`.
4. Confirm `D/_global/pricing.json` exists (Section 17).
5. Apply resume logic (Section 19) before doing any new work.

---

## 6. Stage 1 — Explore the deck

1. Read the entire target XML.
2. Find every file it depends on and read those too:
   - `<Included>` / `<File>` entries (other XML decks), followed recursively;
   - every data file referenced by name: property tables, function tables, mesh files,
     and similar.
3. Copy the deck and all dependencies into `source/`, keeping relative layout. GEOS
   finds many data files by **bare filename**, so every such file must sit in the same
   directory as any deck copy that uses it — in `source/`, `baseline/`, `pilot/`, every
   sweep run and every refinement run.
4. Write `source_manifest.json`: every file, its original path, SHA256, what it is, and
   whether it holds **numeric table values** or only **model settings** (e.g. a
   correlation name plus a grid, from which GEOS computes values internally).
5. Understand: physics and solver stack, mesh and discretisation, constitutive models,
   all material parameters, initial and boundary conditions, sources and loads, events
   and time stepping, output and history collectors, and any behaviour defined by GEOS
   source code rather than by the XML. You may read GEOS source (read-only).
6. Note the valid range of every table or model input (e.g. a property table covering
   1–15 MPa).
7. Build the **deck keyword list**: every XML element name, attribute name, and
   name-like attribute value (model names, solver names, region names, function names)
   in the deck and its included files. Save it as `source/deck_keywords.json`. It is
   used by `verify.py` (Section 10).

---

## 7. Stage 2 — Baseline health check

Run the unchanged working copy exactly once:

```bash
<GEOS_BIN> -i <ABS_PATH>/exploration/baseline/input.xml -o <ABS_PATH>/exploration/baseline/output
```

Save `command.txt`, `stdout.log`, `stderr.log`, and `run.json` (start/end time, wall
time, exit code, input SHA256, command, output dir).

If it fails:
- read the error from the **top** of the log (`head`), not the bottom — GEOS prints the
  real parse error first and a long stack trace after it;
- fix the **working copy** (never the original), record every change and the reason in
  `exploration/baseline/fixes.md`, and rerun in a new directory
  (`baseline_retry_01/`, ...);
- if it cannot be fixed, stop and write `deck_result.json` with status
  `DECK_BASELINE_FAILED`.

Do not rerun a successful baseline.

---

## 8. Stage 3 — Inspect baseline outputs

1. Recursively inventory every output file: path, format, size, purpose, parser used,
   inspected yes/no → `output_manifest.json`.
2. For each file, understand at a high level what quantities it holds: variable names,
   array shapes, time values, mesh info, min/max. Do not dump full arrays.
3. **Parsers:** first search `D/_global/parsers/`. If none fits, write a generic,
   reusable, format-level parser (not tied to one question), save it there and register
   it in `parser_registry.json`.
   - Example (HDF5 TimeHistory): each field has a matching `"<field> Time"` dataset;
     its time array has shape (n,1) — `ravel()` it; multi-component fields list
     components in deck order.
4. Write `deck_summary.md`: physical system, key parameters, solver/time structure,
   mesh, source-dependent behaviour, outputs and variables, baseline runtime, observed
   behaviour and ranges, **where and when things actually happen** (e.g. how far a
   front, disturbance, or deformation zone travels by the end time), promising
   nonlinearities, obvious analytical shortcuts to avoid, and candidate **structural
   axes** (Section 9).

---

## 9. Stages 4–7 — Design, pilot, sweep, table (per pass)

### 4. Design

Using `deck_summary.md` (and, in Pass 2, `diagnosis.md`), the controller designs:

**Categories.** The agent invents its own categories for this deck and splits the
`QUESTIONS_PER_PASS` questions across them however it judges best. Categories must be
scientifically distinct, not wording variants.

Question types that tend to defeat a no-tool model (starting point; adapt per deck):
- **Magnitude** — how large is a quantity at a stated place and time;
- **Threshold** — the highest/lowest input that keeps an output below/above a limit;
- **Timing** — when an event first happens (arrival, crossing, peak, onset);
- **Optimisation** — which input value maximises an output under constraints;
- **Inverse** — given an observed output, what input produced it;
- **Quantitative reasoning** — a yes/no or which-is-larger conclusion that only the
  numbers can decide (rules in Section 10).

Avoid: pure "why/mechanism" questions; questions a linear model, superposition,
symmetry, a steady-state or fully-developed assumption, or a textbook closed form
solves by hand.

Known model weaknesses to target: magnitude precision, extrapolating assumed scalings
(linear, inverse-proportional, steady-state) where the true response is nonlinear or
transient, timing of events, and quantifying nonlinear effects.

**Template limit.** A *template* is defined only by the observable (the quantity asked
for) and the question type (magnitude, threshold, timing, optimisation, inverse,
reasoning or any other type). Questions that differ only in location, time, parameter
values, or category name belong to the same template. At most
`MAX_QUESTIONS_PER_TEMPLATE` questions may share a template.

**Sweep.** One shared sweep per pass serves all categories. The agent chooses the
swept parameters, ranges, grid density, and recorded observables, within
`MAX_SIMULATIONS_PER_PASS − REFINEMENT_RESERVE_RUNS` runs (pilots included).

**Structural axis.** Where the deck supports it, the sweep must include at least one
structural axis: a change in the *type* of scenario, not only in parameter values.
The agent decides what is meaningful for this deck's physics. Examples:
- flow: fixed-pressure vs fixed-rate boundary; constant vs front-/back-loaded schedule;
- poromechanics: drained vs undrained loading; loading rate or history;
- solid mechanics: monotonic vs cyclic loading; displacement vs traction control;
- thermal: insulated vs fixed-temperature boundary; heating schedule;
- waves: source type or position; layered vs uniform medium;
- any deck: uniform vs layered properties; early vs late observation windows.

The structural change must keep the deck valid (pilots check this) and must remain
describable in a few sentences. If the deck supports no sensible structural axis,
state this and the reason in `design.md` and rely on the template limit for variety.

Check before running:
- inputs stay inside every table's or model's valid range, at every sweep point;
- something actually happens at the locations and times the questions will ask about;
- the template records only the numbers named in this design (a pressure, a
  rate, a plume height, a cell count, a fracture length, a slip, or whatever
  this deck's questions need), at the times the questions ask about. Do not
  record the full reservoir field or restart files in sweep, pilot, or
  refinement runs. If a number can only be computed from the full field,
  compute it while building `sweep_table.csv` and then delete the field file.
  Time-history HDF5 files are field files too. Once their numbers are in
  `sweep_table.csv`, delete every `*.hdf5` in that run, including files kept for a
  cited question or a refinement run.

**Time-step resolution.** If any question will ask for a time (arrival, crossing, peak,
onset), the simulation time step near that event must be at most half the timing
tolerance. For example, an event near 10⁸ s with a 1% tolerance needs steps of at most
5×10⁵ s. If the deck's own step is coarser, set a finer fixed time step in the template.
The same time stepping applies to every run in the pass (pilots, sweep and refinement),
and the question states it. Measure the run time on the pilot runs and choose the
number of sweep runs accordingly.

Write `design.md`: categories, templates, sweep axes (marking the structural axis),
ranges, grid, planned observables, run count, refinement reserve, and why this design
should defeat the no-tool model.

### 5. Pilot

Run 2–3 pilots at the most extreme corners of the grid (the hardest cases) in
`sweep/pilot/`, covering every structural option. If any fails, fix the template and
rerun pilots in new directories. Do not start the full sweep until pilots pass.

### 6. Sweep

- Build `template.xml` with placeholders; generate one `input.xml` per run into
  `runs/run_NNNN/`, copying required data files alongside.
- **sed trap:** if a placeholder appears more than once on a line, use `s/.../.../g`.
  Otherwise GEOS fails with `Input string validation failed`.
- **Time-varying inputs** (e.g. a two-stage source or load): use a `TableFunction` with
  `interpolation="lower"` referenced by `functionName`. (Flow example: a negative
  `scale` on a source means injection.)
- Run in parallel:
  ```bash
  export OMP_NUM_THREADS=1
  xargs -P "$PARALLEL_JOBS" -I{} bash -c 'run_one {}' < joblist.txt
  ```
- Each run writes ONE `run.json`: run ID, swept parameter values, exact command,
  start/end time, wall time, exit code, input SHA256, output directory.
  Do not write separate `command.txt` or `params.json` files.
- Capture stdout/stderr while the run executes. If it succeeds, delete both logs.
  If it fails, keep both logs and copy the first error line into `failed_runs.csv`.
- Failed runs:
  - record them in `failed_runs.csv` with parameters and the first error line;
  - if failed runs ≤ `MAX_FAILED_RUN_PERCENT` of the sweep: continue without them;
  - if more: stop the pass, diagnose the setup, fix the template, and rerun the sweep
    in fresh directories (preserve the failed attempt).
- Total launches in the pass (pilots + sweep + refinement, failed ones included) must
  not exceed `MAX_SIMULATIONS_PER_PASS`.

### 7. Table and provenance

- `extract_table.py` reads each successful run's own output directory and writes
  `sweep_table.csv`: one row per run, the swept parameters (including structural
  options), the recorded observables, and the run ID.
- Before parsing a run, confirm the output belongs to that run (path and timestamps).
- `sweep_readme.md` (compact): what was varied and over what grid, what was held
  fixed, what each column means and how it was extracted, runs attempted/succeeded/
  failed, total wall time, and the exact commands to rebuild the table.

Pass 2 may reuse the Pass 1 table in addition to its own new runs.

---

## 10. Stages 8–10 — Generate, refine, verify, freeze

### 8. Generate

Make ONE separate `AGENT_MODEL` call (its own `agent -p` invocation with
`--output-format stream-json`, so its cost is isolated). Workspace: the current
pass directory. Pass it the PATHS (do not copy the files into `generation/`) of: `deck_summary.md`,
`design.md`, `sweep_readme.md`, `sweep_table.csv`, `failed_runs.csv`,
`source_manifest.json`, and any data file that holds numeric tables. Include the
rules below in the prompt. In Pass 2 also pass `diagnosis.md`. It must not see
`memory_A.md` directly.

The generation call must NEVER read `sweep_table.csv` (or any file larger than
~50 KB) into its context. It inspects the table only with short Python commands in
the `geos` environment that print at most ~50 lines each (column list, value
ranges, filtered rows, brackets). Keep the call's total prompt tokens below the
long-context threshold in `pricing.json`.

The generation call may read ONLY the files whose paths it was given, plus
`GEOS_SWEEP_BENCH.md` for the question rules. It must not search or read any other
deck, any other `RUN_TAG`, `_global/`, or any file elsewhere in `GEOS_ROOT`.
The prompt must contain the exact JSON fields listed below, so the call has no
reason to look for an example or a schema.

It returns, for each of the `QUESTIONS_PER_PASS` questions:
- `question_text`;
- `category`, `question_type`, `observable`, `template_id`;
- `answer_type`: `numeric` or `reasoning`;
- `true_value` + units (numeric) or `true_statement` (reasoning), from the table;
- `tolerance_type` (`relative` or `absolute`) and `tolerance_value` (Section 10 rule 4);
- `needs_refinement`: true for threshold, timing, and optimisation answers whose value
  lies between grid points or output samples; plus the bracket from the table;
- provenance: which runs, columns and selection rule decide the answer;
- for reasoning questions: the `naive_conclusion` (what the obvious mechanism or
  scaling argument predicts) and why the simulation contradicts it;
- hardness rationale: which shortcut it blocks and why a no-tool model should miss it.

### Question content rules

A question MUST:
1. **State only what the original deck does not already contain:**
   - every swept value that differs from the original deck, with units
   - the requested quantity: what, where, when, units, sign convention, and tie rule
   - the tolerance (rule 2)
   - for a search question, the search range as a continuous interval (minimum and maximum only)

   The mesh, materials, initial and boundary conditions, sources, schedules, time stepping, and any other number already written in the original deck or its dependencies stay in those files. Do not copy them into the question.
2. **State the tolerance** for numeric answers, as a relative percentage or as an
   absolute amount with units (rule 4).
3. Ask about a place and time where something actually happens.
4. **Tolerance type.** Use a relative tolerance of `TOLERANCE_PERCENT` by default.
   If the true value is close to zero — below 10% of that quantity's full range across
   the sweep — use an absolute tolerance equal to `TOLERANCE_PERCENT` of that full range
   instead (e.g. a saturation ranging 0–1 → ±0.01). State it in the question.
5. Have its true answer **away from the edges** of the swept range.
6. Never rely on a failed run, or on a grid point adjacent (along any swept axis) to a
   failed run.
7. **Reasoning questions must be decided by the numbers.** Their yes/no or
   which-is-larger conclusion must be one where the obvious mechanism or scaling
   argument gives the WRONG conclusion. Achieve this by setting the decision threshold
   close to the true value (e.g. "does doubling X increase Y by more than 0.5%?" when
   the true increase is 0.9% and the naive argument predicts ~0%). If the naive
   argument gives the right conclusion, the question is too easy — rewrite it.
8. Read like a normal PhD-level scientific problem.
9. **Observed values** given in a question (e.g. in inverse questions) that come
   directly from simulation output with many digits (for example
   0.26419505410848054) are rounded to 4 significant figures, as a real measurement
   would be reported.
10. **Search intervals** (threshold, inverse, optimisation): the stated interval must
    lie inside the swept range and contain exactly one answer. Place the true answer
    off-centre: its distance from the interval midpoint must be at least 20% of the
    interval width, and at least 5% of the width from either end. Across the pass,
    put some answers in the lower part of their interval and some in the upper part.

A question MUST NOT:
- state or hint at governing equations, constitutive-law formulas, discretisation,
  time integration, solver methods or tolerances, flux/upwinding conventions, or how
  the requested quantity is computed;
- **contain any GEOS keyword or internal name**: no XML element or attribute names, no
  model, solver, region, or function names from the deck, no CamelCase class-style
  names (e.g. write "Span–Wagner equation of state", never `SpanWagnerCO2Density`);
- mention GEOS, XML, simulators, simulation software, file names, paths, hashes,
  output formats, or run IDs;
- say or imply that a simulation or search is needed;
- **list candidate values or options** for the answer (no "choose from 10.0, 10.6,
  11.2 ..."); comparing two or more fully specified cases stated as inputs is allowed;
- contain the answer, or leak it through the stated values;
- depend on the sweep table, answer keys, or simulation outputs. Relying on the original deck and its dependencies is allowed;
- ask for a number that is already written in the original deck or its dependencies.

**Implementation-determined choices:** a modelling or numerical choice written in the original deck or its dependencies is visible to the no-tool model. A choice that exists only in the GEOS source is not. The simulation result is the truth. A no-tool answer that assumes a different hidden choice is a legitimate failure.

### 9. Refine

For every question with `needs_refinement = true`, the true value must be known to
within its tolerance, not just to grid resolution.

- **Input-type answers** (threshold, optimisation, inverse on a continuous input):
  start from the bracket in the table (the two neighbouring grid values between which
  the answer lies). Run bisection simulations inside the bracket, one run per step,
  until the bracket width is at most half the tolerance at the answer. The true value
  is the midpoint of the final bracket.
- **Time-type answers** (arrival, crossing, peak time): the recorded output interval
  must be at most half the tolerance at the answer. If it is coarser, rerun that case
  with finer output recording only (same time-step settings, rule 2.5). If the event
  time falls between recorded samples, use linear interpolation between them and
  record this in the provenance. Interpolation is allowed only when the time step
  already meets the time-step resolution rule (Section 9); it must never be used to
  claim a precision the time step does not have. If the time step is too coarse,
  rewrite the question.
- Refinement runs follow every sweep rule: own directory under
  `sweep/refine/<Qid>/`, same template and solver settings, same `run.json` and log rules as sweep runs,
  recorded in `failed_runs.csv` if they fail, counted in the pass budget.
- If a refinement run fails, or the reserve would be exceeded, rewrite the question
  (different case or type) instead of freezing an unrefined answer.

Record in `answer_key.json`: the final bracket, its width, the refinement run IDs, and
the resulting true value.

### 10. Verify and freeze

**Script checks.** Use (or write if missing) `D/_global/scripts/verify.py` (reusable across decks) and run it
on every question. It records the results in the question's `result.json` (`verify` block) and checks mechanically:

Before reusing a script from `D/_global/scripts/`, check that it writes only the
files in the Section 3 layout. If it also writes old files (`answer.txt`,
`verify.json`, `tool_check.json`, `prompt.txt`, `trace_try1.jsonl`, `judge.json`,
`raw.json`, `stderr.log`), update the script so it stops writing them. Do not
leave both layouts on disk.

```text
[ ] true value recomputed from the scalar columns of sweep_table.csv matches the answer key
    (the field file may already have been deleted; if not, the script value wins;
    if nothing reproduces, rewrite)
[ ] no provenance run is failed or adjacent to a failed run
[ ] answer not at an edge of the swept range
[ ] refinement: final bracket width / output interval <= half the tolerance
[ ] timing answers: simulation time step near the event <= half the tolerance
[ ] tolerance type follows rule 4 (near-zero → absolute)
[ ] question text contains no entry of deck_keywords.json
[ ] question text contains no CamelCase class-style token
[ ] question text contains no "GEOS", "XML", file names, paths, or run IDs
[ ] template count <= MAX_QUESTIONS_PER_TEMPLATE across the pass, counting templates
    by (observable, question type) only, ignoring category, location, and time
[ ] observed values in the question have at most 4 significant figures
    (input tables copied from the deck are exempt)
[ ] reasoning questions have a naive_conclusion that differs from the true conclusion
[ ] search-interval answers: |answer − midpoint| >= 0.20 × width, and >= 0.05 × width
    from each end; answers are not all on the same side across the pass

```

**Agent review** (things a script cannot judge):

Check each question against every rule in "Question content rules" and the "Avoid"
list in Section 9 that a script cannot test: swept differences and the requested quantity stated, requested quantity precise, no hints or leakage, something
happens at the asked place and time, not solvable by a hand shortcut, and for
reasoning questions the naive argument really gives the wrong conclusion. Also
confirm at least one question uses the structural axis, if the sweep has one.

If a question fails any check, **rewrite it now** (same slot) and check again. No model
has seen it, so nothing is contaminated. A rewrite may be done by the controller or by
a further generation call; log any extra call's cost to generation.

When it passes: save `question.txt` (exact text) and `answer_key.json`, write the
SHA256 of `question.txt` into `result.json`, mark `FROZEN`.

Aim for exactly `QUESTIONS_PER_PASS` frozen questions. If the deck genuinely cannot
support that many valid questions, freeze fewer and record the shortfall; never
fabricate a question.

---

## 11. Stage 11 — No-tool solving

For each frozen question, one fresh, separate session. Never `--resume`. Never put two
questions in one session. Nothing from other questions, the sweep, memory or answer
keys may reach it.

Run the sessions **in parallel**, up to `NO_TOOL_PARALLEL_JOBS` at once. Each session
has its own workspace folder (Section 3) containing only the original deck and its dependencies, and its own trace file, so parallel
sessions cannot see each other.

```bash
agent -p --trust --mode ask \
  --model "$NO_TOOL_MODEL" \
  --workspace <its own folder under D/_global/no_tool_workspaces/> \
  --output-format stream-json \
  "<NO_TOOL_PROMPT>"
```

Launch each from inside that folder and write its trace to the question's
`no_tool_trace.jsonl`. If a call fails for a technical reason (network, rate limit),
retry it; this does not count as a rerun.

### No-tool prompt (use verbatim; append only the question text)

```text
instructions : You are the solver in a scientific reasoning evaluation. You may read only the files in this workspace. Those files are the original deck: its input XML, the XML files it includes, and the property tables and mesh files those point to. Use them to learn the setup. You MUST NOT: edit, create, or delete any file; read any file outside this workspace; access the GEOS source, other decks, sweep tables, answer keys, or simulation outputs; execute shell or terminal commands; run GEOS, Python, or any other program; use web search or external documentation; use MCP, plugins, subagents, connectors, or any other external tool. Do not run a simulation. Solve the question using the original deck and your own reasoning. Swept values that differ from the original deck are stated in the question. If an exact numerical answer cannot be derived, give your best scientific estimate and distinguish what is known from what is estimated.

here are the questions: 

<exact frozen question text>
```

Nothing else is added: no category, no hint, no tolerance beyond what the question
itself states, no mention of a benchmark.

### Free tool-call check (script, no model call)

After each session, a script counts every event with `"type":"tool_call"` in the trace
and records `tool_calls_attempted` and `tool_calls_successful` in `result.json`.

A read of a file inside the workspace is valid. Any other tool call, including a denied or failed one, contaminates the answer. Discard it and rerun once (up to `MAX_NO_TOOL_RERUNS`) in a new folder with a fresh copy of the original deck, renaming the contaminated trace to `no_tool_trace_tryN.jsonl`. Still contaminated means status `NO_TOOL_EVAL_FAILED`. The question is excluded from the pass count (neither CORRECT nor INCORRECT). Record it.

Save the final answer text in `result.json` (`no_tool.answer_text`).

---

## 12. Stage 12 — Judge

For each valid no-tool answer, one separate `AGENT_MODEL` call. Give it: the frozen
question, `answer_key.json` (true answer + provenance), and the no-tool answer.

### Judge prompt

```text
You are judging a no-tool model's answer to a scientific question against a fixed,
simulation-derived true answer. The true answer is final; do not change it.

Return JSON:
{
  "verdict": "CORRECT" or "INCORRECT",
  "no_tool_estimate": <number the answer commits to as its final value, or null>,
  "estimate_units": "<units>",
  "no_tool_conclusion": "<its yes/no or which-is-larger conclusion, reasoning questions only>",
  "reasoning_sound": true or false,
  "decisive_comparison": "<one or two sentences>",
  "key_discrepancy": "<the main error, or null>"
}

Rules:
- Numeric question: extract the single final value the answer commits to. If it gives
  a range and no single value, use the midpoint and say so. If it gives no value,
  no_tool_estimate = null and verdict = INCORRECT.
- A refusal or a claim that the answer cannot be determined = INCORRECT.
- A correct final value reached by materially wrong reasoning (coincidence) = INCORRECT.
- Reasoning question: compare the conclusion with the true statement on substance, not
  wording. Correct conclusion with sound reasoning = CORRECT; otherwise INCORRECT.
  If the question also requires supporting numbers, each must meet its tolerance.
- An answer that assumes a modelling or numerical choice different from the one that
  produced the true answer, and therefore differs, is INCORRECT.
```

### Scripted fields (the script, not the judge, applies the tolerance)

For numeric questions a script computes, from `no_tool_estimate` (converted to the
question's units) and `true_value`:

```text
relative_error_percent = 100 * (estimate - true) / |true|
absolute_error         = estimate - true
error_sign             = "over" | "under" | "exact"
within_tolerance       = |error| <= tolerance   (relative or absolute, per the question)
```

Final verdict for numeric questions: `CORRECT` only if `within_tolerance` is true AND
the judge's `reasoning_sound` is true; otherwise `INCORRECT`. For reasoning questions
the numeric fields are `null` (unless supporting numbers were requested) and the
judge's verdict stands.

**Flag `correct_value_wrong_reasoning`** = true when the answer's value is within
tolerance (numeric) or its conclusion matches the truth (reasoning), but
`reasoning_sound` is false. The verdict stays `INCORRECT`; the flag makes such cases
visible in every summary.

Accepted = `INCORRECT`. Rejected = `CORRECT`.

Save the judge's trace to `judge_trace.jsonl` and write its JSON into the question's `result.json` (Section 18).

---

## 13. Stage 13 — Decide

Let `n_incorrect` = INCORRECT verdicts among valid questions of this pass.

- `n_incorrect >= MIN_INCORRECT_TO_VALIDATE` → deck `VALIDATED`. Go to Finish.
  Do not run another pass and do not write Memory A.
- Otherwise, if this pass < `MAX_PASSES` → Memory A and Diagnosis (Stage 14), then the
  next pass.
- Otherwise → deck `REJECTED`. Go to Finish.

---

## 14. Stage 14 — Memory A and Diagnosis (only if Pass 1 does not validate)

### Memory A

Write `memory_A.md` (compact) from the Pass 1 results. For every question:
- verdict, error and sign (numeric), `correct_value_wrong_reasoning` flag;
- how the no-tool model got its answer: reasoning route, assumptions, scaling laws,
  approximations, analogies;
- if CORRECT: the shortcut that let it succeed without simulation;
- if INCORRECT: what resisted prompt-only reasoning and in which direction it erred.

Then a short pass-level section: recurring shortcuts, what worked, the error
distribution (count within tolerance, spread, sign balance), and **question-design
flaws found** (e.g. an answer known only to coarse resolution, an obvious reasoning
conclusion, too many similar questions).

No chain-of-thought, no copied answers.

### Diagnosis

Write `diagnosis.md`, reading `memory_A.md`. Follow this order strictly.

**Step 1 — Shortcut analysis (primary).** Read the full no-tool answer of every
question it got CORRECT. For each: how did it get the answer, what shortcut, scaling,
symmetry, approximation or known result did it use, and what type of reasoning was it.
Group the shortcuts.

**Step 2 — Redesign.** From the shortcuts and the design flaws, decide how to make the
questions harder: which parameters or structural options to sweep instead or in
addition, which ranges, which observables, which question types and categories to
change, so that each identified shortcut no longer works. The Pass 1 simulations were
correct; the change is in what is swept and asked, not a correction of the results.

**Step 3 — Tolerance (secondary, only after Step 2).** Look at the error distribution
of the Pass 1 numeric questions:
- most answers landed well inside the tolerance → tighten `TOLERANCE_PERCENT` for
  Pass 2;
- otherwise → keep it.
State the evidence (the error values) for the choice. Tolerance must never be the only
change.

The controller may decide whether any re-exploration of the deck is needed; the
baseline is never rerun if it succeeded.

Pass 2 starts a new `pass2/` directory, a new budget of `MAX_SIMULATIONS_PER_PASS`, and
new questions. Pass 2 may reuse Pass 1's sweep table.

---

## 15. Stage 15 — Finish

1. Write `deck_result.json`: status (`VALIDATED` / `REJECTED` / `DECK_BASELINE_FAILED`),
   `PROTOCOL_VERSION`, `RUN_TAG`, passes run, per-pass counts (generated, valid,
   correct, incorrect, `correct_value_wrong_reasoning`, no-tool-failed), accepted
   question IDs, final tolerance, total simulations (sweep and refinement separately),
   total wall time, cost totals by stage and by model.
2. **Delete `memory_A.md`** if it exists. No memory carries over to another deck.
3. Delete this run's folders under `D/_global/no_tool_workspaces/`. They hold only copies of the original deck. Also delete any
   `__pycache__` folders, and any temporary or scratch files the controller created
   (e.g. `*_tmp*`). Keep the question files, traces, `deck_result.json`, `sweep_table.csv`, `sweep_readme.md`, `failed_runs.csv`, `design.md`, `deck_summary.md`, `source/`, and the generation files.
4. After those files exist, delete the per-run copies. For the baseline and every pilot, sweep, and refinement run, delete `input.xml`, `run.json`, `stdout.log`, `stderr.log`, and the `output/` folder, including every `*.hdf5`. For a refinement run, keep `observables.json`. The swept numbers are already in `sweep_table.csv`, the failed-run errors are already in `failed_runs.csv`, the baseline findings are already in `deck_summary.md`, and each refinement measurement is already in that question's `answer_key.json`.
5. Update pass_summary.csv and pass_totals.csv.
6. Stop.

---

## 16. Local summary tables

Write two CSV files per pass; never upload anything. Update both after each stage
that changes them.

**pass_summary.csv — one row per question**
```text
deck_slug, run_tag, pass, category_name, question_id, question_type, template_id,
answer_type, verdict, accepted, correct_value_wrong_reasoning,
true_value, no_tool_estimate, relative_error_percent, absolute_error, error_sign,
tolerance_type, tolerance_value, refined, no_tool_valid,
no_tool_estimated_api_cost_usd, judge_estimated_api_cost_usd,
no_tool_wall_time_s, judge_wall_time_s
```

**pass_totals.csv — one row per pass, plus a deck-total row**
```text
deck_slug, run_tag, pass, questions_generated, questions_valid, questions_accepted,
questions_correct_value_wrong_reasoning, deck_status,
sweep_runs, refinement_runs, sweep_failed_runs, sweep_wall_time_s,
generation_estimated_api_cost_usd, no_tool_estimated_api_cost_usd,
judge_estimated_api_cost_usd, diagnosis_estimated_api_cost_usd,
grok_estimated_api_cost_usd, sol_estimated_api_cost_usd,
total_estimated_api_cost_usd, total_wall_time_s
```

## 17. Cost accounting

Costs are **estimated API list-price costs**, not what the user pays. Always name
them `*_estimated_api_cost_usd`.

For every model call, save the raw `stream-json` trace first, then read from its
usage data: `inputTokens`, `outputTokens`, `cacheReadTokens`, `cacheWriteTokens`,
duration, and the reported model. Price each call with the rates of the model that
made it.

Rates (USD per 1M tokens) are in `D/_global/pricing.json`. It is experiment
configuration: do not change it. If it is missing, stop and report.

```text
cost = inputTokens/1e6 * input + outputTokens/1e6 * output
     + cacheReadTokens/1e6 * cache_read + cacheWriteTokens/1e6 * cache_write
```

For Grok, compare the call with that model's `long_context_threshold_prompt_tokens`
in `pricing.json`. For `grok-4.7-high` the threshold is on input tokens only. If
the input exceeds it, use the `long_context` rates for every token of that call.
For `cursor-grok-4.6-high`, the threshold is on input + cache read + cache write.

If a model has no pricing row, record cost as `null` and continue.

**Cost buckets:**
| Bucket | Model | Level |
|---|---|---|
| controller | AGENT_MODEL | deck (this launch session) |
| generation | AGENT_MODEL | pass (batch; not split per question) |
| no_tool | NO_TOOL_MODEL | per question |
| judge | AGENT_MODEL | per question |
| diagnosis | AGENT_MODEL | deck (only if Pass 2 runs) |

The controller cannot read its own session's final usage while running. Log
controller cost as `null` in deck_result.json and Use (or write if missing) `D/_global/scripts/controller_cost.py`,
which parses the launch log in `D/_global/controller_logs/` after the run and prints the
controller cost.

GEOS compute is not API cost; track it as run counts and wall time only.

---

## 18. `result.json` per question

```json
{
  "question_id": "Q07",
  "deck_slug": "",
  "deck_sha256": "",
  "protocol_version": 3,
  "run_tag": "",
  "pass": 1,
  "category_name": "",
  "question_type": "",
  "template_id": "",
  "answer_type": "numeric",
  "question_sha256": "",
  "status": "ACCEPTED | REJECTED | NO_TOOL_EVAL_FAILED",
  "models": { "no_tool": "", "judge": "", "no_tool_reported": "", "judge_reported": "" },
  "truth": {
    "true_value": null, "units": "", "true_statement": null,
    "tolerance_type": "relative", "tolerance_value": null,
    "refined": false,
    "refinement": { "final_bracket": null, "bracket_width": null, "runs": [] },
    "provenance": { "table": "sweep_table.csv", "runs": [], "columns": [],
                    "selection_rule": "" },
    "naive_conclusion": null
  },
   "verify": { "all_script_checks_passed": true, "failed_checks": [], "rewrites": 0 },
  "no_tool": {
    "valid": true, "reruns": 0, "tool_calls_attempted": 0,
    "no_tool_estimate": null, "usage": {}, "estimated_api_cost_usd": null,
    "answer_text": "",
    "wall_time_seconds": null
    
  },
  "judge": {
    "verdict": "INCORRECT", "reasoning_sound": null,
    "correct_value_wrong_reasoning": false,
    "relative_error_percent": null, "absolute_error": null,
    "error_sign": null, "within_tolerance": null,
    "decisive_comparison": "", "key_discrepancy": "",
    "usage": {}, "estimated_api_cost_usd": null, "wall_time_seconds": null
  },
  "accepted": true
}
```

---

## 19. Resume and interruption

The workflow must be resumable. Before any work, scan
`decks/<deck_slug>/<RUN_TAG>/` and continue at the earliest unfinished step. Never
repeat finished work:

- `deck_result.json` exists → the deck is finished; do nothing and stop. Missing
  `output/` folders of pruned runs are expected and must never be rerun.
- Per-run `input.xml`, `run.json`, logs, and `output/` deleted at finish are expected. Never rerun those simulations.
- successful baseline exists → do not rerun;
- `sweep_table.csv` exists and `sweep_readme.md` confirms completion → do not rerun the
  sweep; rerun only runs missing a result;
- refinement complete for a question → do not rerun it;
- question frozen → never regenerate or edit it;
- no-tool answer valid → do not rerun;
- judge done → do not rejudge;

If an existing record under this `RUN_TAG` has a different `protocol_version`, stop
and report; the user must choose a new `RUN_TAG`.

**Usage-limit failure:** if a model call fails because a Cursor usage limit is reached,
save all state, record `USAGE_LIMIT_REACHED` with the stage in
`D/_global/controller_logs/interruptions.json`, and stop cleanly. The next launch
resumes.

**Other unexpected technical errors:** diagnose, repair, record the error and the fix,
continue. Never weaken a rule, change a frozen question, or fabricate a result to get
past an error. Stop only if it cannot be fixed within the rules.

---
## Appendix — How the user launches this

Once, before the first launch (skip if the folder already exists):

```bash
mkdir -p /home/kbhau001/codes/GEOS/geos_sweep_bench_v2/_global/controller_logs
```

Save this file as `/home/kbhau001/codes/GEOS/geos_sweep_bench_v2/GEOS_SWEEP_BENCH.md`,
set `INPUT_XML` and `RUN_TAG` in Section 1, then:

```bash
cd /home/kbhau001/codes/GEOS
conda activate geos
agent -p --force --trust --model grok-4.7-high \
  --workspace /home/kbhau001/codes/GEOS \
  --output-format stream-json \
  "Read /home/kbhau001/codes/GEOS/geos_sweep_bench_v2/GEOS_SWEEP_BENCH.md completely and execute the workflow exactly as specified. Treat it as the authoritative experiment protocol. Continue autonomously through the full experiment unless the protocol itself requires stopping. Do not merely summarize or explain the file; execute it." \
  2> /home/kbhau001/codes/GEOS/geos_sweep_bench_v2/_global/controller_logs/controller_err.log \
  | tee /home/kbhau001/codes/GEOS/geos_sweep_bench_v2/_global/controller_logs/controller_$(date +%Y%m%d_%H%M%S).jsonl
```
