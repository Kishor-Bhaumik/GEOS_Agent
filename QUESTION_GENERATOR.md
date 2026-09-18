**\*\*# GEOS Adversarial Scientific Question Generation and Evaluation
Protocol\*\***

**\*\*## 0. Purpose\*\***

This file is the execution contract for a Cursor CLI controller that
generates and evaluates hard scientific questions from a GEOS XML deck.

The objective is **\*\*\\\*\\\*adaptive adversarial question
discovery\\\*\\\*\*\***:

1\\. inspect one GEOS deck and its baseline outputs;

2\\. generate scientifically meaningful, self-contained scientific
questions whose exact answers may require numerical simulation, solver
behavior, discretization effects, nonlinear/coupled physics, or
controlled parameter searches to establish reliably; GEOS files and
outputs are private reference evidence, not information the question
asks the solver to retrieve;

3\\. test each question with the same underlying model under a strict
**\*\*\\\*\\\*no-tool\\\*\\\*\*\*** condition;

4\\. solve the same frozen question independently with a
**\*\*\\\*\\\*tool-enabled GEOS agent\\\*\\\*\*\***;

5\\. verify the tool-enabled reference answer from saved evidence;

6\\. compare the no-tool answer with the tool-enabled reference answer;

7\\. keep questions for which the no-tool model fails in a
scientifically meaningful way;

8\\. update compact adaptive memory so later questions become harder;

9\\. log provenance, runtime, token usage, estimated provider-API cost,
simulation count, tool calls, retries, answers, and acceptance status
locally and in Weights & Biases.

This is an experimental workflow. Execute it. Do not merely describe
what could be done.

\\---

**\*\*# 1. Configuration\*\***

Edit these values before a run.

\\\`\\\`\\\`text

N\\\_CATEGORIES = 5

QUESTIONS\\\_PER\\\_CATEGORY = 5

TOTAL\\\_ATTEMPTED\\\_CANDIDATES = N\\\_CATEGORIES \\\*
QUESTIONS\\\_PER\\\_CATEGORY

CONDA\\\_ENV = geos

D = /home/codes/GEOS/geos\\\_question

INPUT\\\_XML =
/home/codes/GEOS/inputFiles/singlePhaseFlow/incompressible\\\_1d.xml

GEOS\\\_LINUX = /home/codes/GEOS/build-conda-geos-release/bin/geosx

GEOS\\\_MACOS = /home/codes/GEOS/build-macOS\\\_arm-release/bin/geosx

WANDB\\\_PROJECT = geos-adversarial-questions

WANDB\\\_ENTITY = \\\<use current configured entity unless explicitly
set\>

EVAL\\\_MODEL = \\\<set gpt-5.6-sol

GENERATOR\\\_MODEL = EVAL\\\_MODEL

NO\\\_TOOL\\\_MODEL = EVAL\\\_MODEL

TOOL\\\_SOLVER\\\_MODEL = EVAL\\\_MODEL

JUDGE\\\_MODEL = EVAL\\\_MODEL

MAX\\\_TECHNICAL\\\_RETRIES = 2

WANDB\\\_UPLOAD\\\_RAW\\\_SIMULATION\\\_OUTPUTS = false

\\\`\\\`\\\`

**\*\*### Required interpretation of\*\*** \\\`N\\\` **\*\*and\*\***
\\\`P\\\`

\\- \\\`N\\\_CATEGORIES = 5\\\` means create exactly five question
categories if five scientifically valid categories can be supported by
the deck.

\\- \\\`QUESTIONS\\\_PER\\\_CATEGORY = 5\\\` means attempt exactly five
candidate questions in each category.

\\- With the default values, the experiment attempts exactly
**\*\*\\\*\\\*25 candidate questions\\\*\\\*\*\***.

\\- Rejected questions are **\*\*\\\*\\\*not replaced\\\*\\\*\*\***.

\\- Do not continue generating until five accepted questions are
obtained.

\\- If a category cannot support scientifically valid questions, do not
fabricate them. Record the affected candidate slots as generation
failures rather than inventing meaningless questions.

**\*\*### Same-model rule\*\***

Unless explicitly overridden by the experimenter:

\\\`\\\`\\\`text

GENERATOR\\\_MODEL = NO\\\_TOOL\\\_MODEL = TOOL\\\_SOLVER\\\_MODEL =
JUDGE\\\_MODEL = EVAL\\\_MODEL

\\\`\\\`\\\`

Use the same model identity and the same reasoning/effort/context
configuration for the no-tool and tool-enabled solving conditions. The
intended experimental difference is access to tools and GEOS, not model
capability.

Record the exact requested model configuration and the model name
reported by Cursor.

\\---

**\*\*# 2. Non-negotiable experimental rules\*\***

1\\. **\*\*\\\*\\\*Never modify the original XML deck.\\\*\\\*\*\***

2\\. The original deck is explored with GEOS **\*\*\\\*\\\*exactly once
per deck version\\\*\\\*\*\***.

3\\. Baseline exploration happens **\*\*\\\*\\\*before question
generation\\\*\\\*\*\***.

4\\. Before question generation, inventory and inspect **\*\*\\\*\\\*all
baseline-generated output files at a high level\\\*\\\*\*\***.

5\\. Do not rerun the unchanged baseline deck during candidate
generation.

6\\. Additional GEOS runs are allowed only when needed to solve a frozen
candidate question.

7\\. Every candidate question must be frozen before either solver is
evaluated on it.

8\\. The no-tool solver must use a strict **\*\*\\\*\\\*prompt-level
no-tool instruction\\\*\\\*\*\*** and must not make any external tool
call.

9\\. Every no-tool invocation must use \\\`--output-format
stream-json\\\`, and the controller must validate the complete trace.
Any trace containing a \\\`"type":"tool\\\_call"\\\` event is
contaminated and invalid.

10\\. The tool-enabled reference solver must solve independently and
must not see the no-tool answer before its own answer is frozen and
verified.

11\\. Verification must use evidence already produced while solving. Do
**\*\*\\\*\\\*not\\\*\\\*\*\*** rerun simulations merely to repeat or
confirm them.

12\\. The no-tool answer is judged only after the tool-enabled reference
answer has been frozen.

13\\. Adaptive memory is intentional. Update it after every attempted
candidate.

14\\. Keep records of both no-tool successes and failures.

15\\. All files, subfolders, scripts, outputs, logs, and benchmark
products created by this workflow must live under \\\`D\\\`.

16\\. All GEOS and Python work must occur in the \\\`geos\\\` conda
environment.

17\\. Do not use pseudocode as a substitute for execution. Run the
actual commands and save the actual evidence.

18\\. Never guess a metric that the infrastructure does not expose. Use
\\\`null\\\`/\\\`unavailable\\\`.

19\\. Never silently use stale output from another question or
simulation.

20\\. Never overwrite evidence from a previous candidate.

21\\. **\*\*Every frozen benchmark question must be self-contained as a
scientific problem.\*\*** The no-tool solver must receive the physical
setup needed to make a scientifically defensible attempt.

22\\. **\*\*Never expose internal benchmark provenance in the scientific
question.\*\*** The question must not mention or rely on XML/deck
filenames, repository paths, SHA/hash values, VTU/VTM/HDF5/Silo/restart
files, parser files, output filenames, run IDs, or hidden GEOS
artifacts.

23\\. **\*\*Do not make lack of file/tool access the hardness
mechanism.\*\*** A candidate is invalid if the obvious correct no-tool
response is merely that an inaccessible file, deck, source tree, or
simulation output is required.

24\\. GEOS source, XML files, simulation outputs, and repository
artifacts are **\*\*private ground-truth resources for the reference
solver\*\***. They may be used to generate and verify the answer, but
must not be named as evidence the benchmark solver is expected to
retrieve.

25\\. Difficulty must come from science/numerics: transient evolution,
nonlinear/coupled behavior, discretization effects, competing
mechanisms, thresholds, parameter interactions, trajectory dependence,
counterfactual changes, or search/optimization.

26\\. Before freezing, apply the **\*\*hidden-evidence test\*\***: if
removing all references to local files/repository artifacts makes the
question impossible to attempt scientifically, mark it
\`QUESTION_INVALID\` before no-tool/reference evaluation.

27\\. An \`ABSTAIN\` caused primarily by missing hidden
file/output/repository access is **\*\*not a meaningful scientific
failure\*\*** and must never be accepted.

\\---

**\*\*# 3. Workspace layout\*\***

Use a layout that already supports multiple GEOS decks in future
experiments.

\\\`\\\`\\\`text

D/

├── \\\_global/

│ ├── environment/

│ │ ├── environment.json

│ │ └── requirements\\\_added.txt

│ ├── pricing/

│ │ └── provider\\\_pricing.json

│ ├── parsers/

│ │ ├── parser\\\_registry.json

│ │ └── ...

│ └── no\\\_tool\\\_preflight/

│ └── \\\<model\\\_and\\\_config\\\_slug\>/

│ ├── preflight\\\_prompt.txt

│ ├── raw\\\_trace.jsonl

│ └── result.json

│

└── decks/

    └── \\\<deck\\\_slug>/

        ├── source/

        │   ├── original.xml

        │   └── source\\\_manifest.json

        │

        ├── exploration/

        │   ├── baseline/

        │   │   ├── input.xml

        │   │   ├── command.txt

        │   │   ├── stdout.log

        │   │   ├── stderr.log

        │   │   ├── run.json

        │   │   └── output/

        │   ├── output\\\_manifest.json

        │   └── deck\\\_summary.md

        │

        ├── memory/

        │   └── adaptive\\\_memory.md

        │

        ├── categories/

        │   ├── categories.json

        │   ├── categories.md

        │   └── generation\\\_log/

        │

        ├── candidates/

        │   ├── C01/

        │   │   ├── Q001/

        │   │   │   ├── question/

        │   │   │   ├── generation/

        │   │   │   ├── no\\\_tool/

        │   │   │   ├── reference/

        │   │   │   ├── judge/

        │   │   │   ├── result.json

        │   │   │   └── question.tex

        │   │   └── ...

        │   └── ...

        │

        ├── accepted/

        │   └── accepted\\\_questions.tex

        │

        └── summary/

            ├── candidates.jsonl

            ├── candidates.csv

            ├── costs.csv

            └── final\\\_summary.json

\\\`\\\`\\\`

Use a deterministic \\\`deck\\\_slug\\\` derived from the XML filename
plus a short SHA256 prefix.

Example:

\\\`\\\`\\\`text

incompressible\\\_1d\\\_\\\_a1b2c3d4

\\\`\\\`\\\`

A modified original XML is a new deck version and therefore gets a new
deck hash/version. Never silently reuse exploration from a different XML
hash.

\\---

**\*\*# 4. Environment initialization\*\***

Before doing any scientific work:

1\\. Resolve and validate:

\\- \\\`D\\\`

\\- \\\`INPUT\\\_XML\\\`

\\- GEOS executable for the current operating system

\\- conda installation

\\- \\\`geos\\\` environment

\\- Cursor CLI

\\- Python

\\- W&B authentication

2\\. Create the directory structure under \\\`D\\\`.

3\\. Copy the original XML to the deck \\\`source/\\\` directory.

4\\. Compute and store its SHA256.

5\\. Record:

\\- OS;

\\- hostname;

\\- timestamp;

\\- GEOS executable path;

\\- GEOS git commit if the directory is a Git repository;

\\- Python version;

\\- conda environment;

\\- Cursor CLI version;

\\- exact model configuration.

For shell execution, initialize conda explicitly when necessary:

\\\`\\\`\\\`bash

source "\$(conda info --base)/etc/profile.d/conda.sh"

conda activate geos

\\\`\\\`\\\`

Never use system Python for benchmark parser dependencies.

If a Python package is genuinely required and missing:

\\\`\\\`\\\`bash

python -m pip install \\\<package\>

\\\`\\\`\\\`

Only install it inside the active \\\`geos\\\` environment.

After installation, append the exact installed package and version to:

\\\`\\\`\\\`text

D/\\\_global/environment/requirements\\\_added.txt

\\\`\\\`\\\`

Do not use \\\`sudo\\\`.

Do not modify the system Python environment.

\\---

**\*\*# 5. Select the GEOS executable\*\***

Detect the OS once.

**\*\*### Linux\*\***

Use:

\\\`\\\`\\\`text

GEOS\\\_LINUX

\\\`\\\`\\\`

**\*\*### macOS ARM\*\***

Use:

\\\`\\\`\\\`text

GEOS\\\_MACOS

\\\`\\\`\\\`

Construct commands as:

\\\`\\\`\\\`bash

\\\<GEOS\\\_BIN\> -i \\\<ABSOLUTE\\\_INPUT\\\_XML\> -o
\\\<ABSOLUTE\\\_OUTPUT\\\_DIRECTORY\>

\\\`\\\`\\\`

Do not hard-code \\\`output\\\` as a shared directory.

Every simulation must have its own output directory.

\\---

**\*\*# 6. Stage A --- one-time deck exploration\*\***

**\*\*## A1. Read the XML\*\***

Before running GEOS:

\\- read the entire XML deck;

\\- understand the solver stack;

\\- identify mesh/discretization;

\\- identify constitutive models;

\\- identify materials and parameters;

\\- identify boundary/initial conditions;

\\- identify events/timesteps;

\\- identify requested outputs/history collectors;

\\- identify any source-code-defined model whose behavior is not fully
specified by the XML.

Save a concise structured summary, but do not yet generate candidate
questions.

**\*\*## A2. Run the unchanged baseline exactly once\*\***

Create:

\\\`\\\`\\\`text

\\\<deck\>/exploration/baseline/

\\\`\\\`\\\`

Copy the original XML into it.

Run the original deck exactly once.

Save:

\\\`\\\`\\\`text

command.txt

stdout.log

stderr.log

run.json

output/

\\\`\\\`\\\`

\\\`run.json\\\` must include at least:

\\\`\\\`\\\`json

{

"start\\\_time": null,

"end\\\_time": null,

"wall\\\_time\\\_seconds": null,

"exit\\\_code": null,

"input\\\_xml\\\_sha256": null,

"command": null,

"output\\\_directory": null

}

\\\`\\\`\\\`

If the baseline GEOS run fails, stop. Do not generate questions from an
unsuccessful baseline.

**\*\*## A3. Baseline exploration is idempotent\*\***

If exploration already exists:

\\- verify the XML SHA256 matches;

\\- verify the baseline run completed successfully;

\\- verify the output manifest exists.

If all are valid, reuse them.

Do **\*\*\\\*\\\*not\\\*\\\*\*\*** rerun the baseline.

\\---

**\*\*# 7. Stage B --- baseline output discovery and high-level
inspection\*\***

This must happen **\*\*\\\*\\\*before question generation\\\*\\\*\*\***.

**\*\*## B1. Inventory every generated output\*\***

Recursively enumerate every file created by the baseline simulation.

For each file record:

\\\`\\\`\\\`text

relative path

extension / format

size

purpose if identifiable

parser used

whether successfully inspected

\\\`\\\`\\\`

Save:

\\\`\\\`\\\`text

exploration/output\\\_manifest.json

\\\`\\\`\\\`

**\*\*## B2. Understand all outputs at a high level\*\***

"Read all outputs" means:

\\- account for every generated output file;

\\- identify its format;

\\- inspect enough metadata/content to understand what scientific
quantities it contains;

\\- identify available variables/fields;

\\- identify timesteps/time values if applicable;

\\- identify array dimensions/shapes;

\\- identify mesh/topology information if present;

\\- compute only lightweight summaries when useful, such as
min/max/count;

\\- understand which outputs are likely useful for future questions.

It does **\*\*\\\*\\\*not\\\*\\\*\*\*** mean dumping every value of a
huge VTU/HDF5/Silo file into model context.

The goal is high-level scientific understanding, not exhaustive baseline
analysis.

**\*\*## B3. Parser reuse\*\***

Before writing a new parser:

1\\. search \\\`D/\\\_global/parsers/\\\`;

2\\. search existing benchmark scripts under \\\`D\\\`;

3\\. check whether a suitable existing Python reader can parse the
format.

If a parser exists:

\\- execute it on the actual output file;

\\- save its output/summary.

If no suitable parser exists:

\\- create a **\*\*\\\*\\\*generic reusable parser for that file
format\\\*\\\*\*\***, not a one-off parser tied to one question;

\\- save it under \\\`D/\\\_global/parsers/\\\`;

\\- register it in:

\\\`\\\`\\\`text

D/\\\_global/parsers/parser\\\_registry.json

\\\`\\\`\\\`

Possible format families include, but are not limited to:

\\\`\\\`\\\`text

.vtu

.vtm

.pvd

.vtk

.csv

.h5 / .hdf5

Silo

GEOS history output

restart output

\\\`\\\`\\\`

Do not assume one library can read every format.

If a package is missing, install only what is necessary inside
\\\`geos\\\`, record its version, and retry.

**\*\*## B4. Produce\*\*** \\\`deck\\\_summary.md\\\`

After XML and baseline-output inspection, create:

\\\`\\\`\\\`text

exploration/deck\\\_summary.md

\\\`\\\`\\\`

It should concisely capture:

\\- what physical system the deck models;

\\- important parameters;

\\- solver/time structure;

\\- mesh/discretization;

\\- source-code-dependent components;

\\- output types and variables;

\\- baseline run duration/status;

\\- high-level ranges or behavior that may help question generation;

\\- promising sources of nontrivial questions;

\\- obvious analytical shortcuts to avoid.

Do not put future ground-truth answers into adaptive memory.

\\---

**\*\*# 8. Stage C --- no-tool runner validation\*\***

This stage is mandatory before the first candidate is evaluated.

The no-tool condition is implemented as **\*\*\\\*\\\*strict prompt
restriction + complete Cursor trace validation\\\*\\\*\*\***. Cursor may
technically expose tools to the model, so the scientific safeguard is
that the model is explicitly instructed not to use or attempt any tool
and every run is checked afterward for tool-call events.

**\*\*## C1. Tested Cursor no-tool invocation\*\***

Use a fresh Cursor CLI session in \\\`--mode ask\\\` with an isolated
workspace and \\\`stream-json\\\` output. Do not resume a tool-enabled
session.

Template:

\\\`\\\`\\\`bash

agent -p \\\\

\\--trust \\\\

\\--mode ask \\\\

\\--workspace \\\<isolated\\\_no\\\_tool\\\_workspace\> \\\\

\\--output-format stream-json \\\\

"\\\<NO\\\_TOOL\\\_PROMPT\\\_WITH\\\_FROZEN\\\_QUESTION\>"

\\\`\\\`\\\`

\\\`agent -p\\\` still technically exposes Cursor tools. Therefore the
prompt and trace validator below are both mandatory. Do not describe
this condition as tools being physically absent from Cursor. Describe it
as a **\*\*\\\*\\\*prompt-restricted, trace-validated no-tool
condition\\\*\\\*\*\***.

**\*\*## C2. Isolated no-tool workspace\*\***

Create an isolated directory under:

\\\`\\\`\\\`text

D/\\\_global/no\\\_tool\\\_preflight/\\\<model\\\_and\\\_config\\\_slug\>/workspace/

\\\`\\\`\\\`

It must contain no GEOS repository, source, simulation output, parser,
memory, benchmark answer, or other task evidence.

Actual benchmark questions must be passed directly as prompt text. The
no-tool model must not need to read a question file.

Use a fresh no-tool session for every candidate. Do not \\\`--resume\\\`
a previous tool-enabled or no-tool session.

**\*\*## C3. Tested technical preflight\*\***

Run a preflight once per exact no-tool model/configuration and again
whenever the Cursor version, model configuration, or no-tool prompt
changes materially.

Create a sentinel file outside the isolated workspace containing a newly
generated random secret string. Ask the model for the exact content
while giving it the same strict no-tool instruction used for benchmark
questions.

The tested behavior is considered a pass only if:

1\\. the sentinel secret is not retrieved;

2\\. the model states that the content cannot be determined without
inspecting the file;

3\\. the complete \\\`stream-json\\\` trace contains
**\*\*\\\*\\\*zero\\\*\\\*\*\*** \\\`"type":"tool\\\_call"\\\` events;

4\\. no external resource is accessed.

Save the complete preflight trace and the exact prompt.

Important experimental observation: permission rules that blocked
\\\`Read\\\` and \\\`Shell\\\` were not sufficient because Cursor could
still retrieve file content through \\\`Grep\\\`. Therefore permission
configuration alone must not be treated as proof of a no-tool condition.
The accepted mechanism for this workflow is the strict no-tool prompt
plus trace validation.

**\*\*## C4. Per-question trace validation\*\***

For every no-tool candidate run, parse the complete \\\`stream-json\\\`
trace and count every event where:

\\\`\\\`\\\`text

"type":"tool\\\_call"

\\\`\\\`\\\`

Record both:

\\\`\\\`\\\`text

no\\\_tool\\\_tool\\\_calls\\\_attempted

no\\\_tool\\\_tool\\\_calls\\\_successful

\\\`\\\`\\\`

For a **\*\*\\\*\\\*valid\\\*\\\*\*\*** no-tool run, both must be:

\\\`\\\`\\\`text

0

\\\`\\\`\\\`

The stricter rule is intentional: even a denied or failed tool attempt
contaminates the prompt-only no-tool condition.

If any tool-call event appears:

\\- set \\\`no\\\_tool\\\_contaminated = true\\\`;

\\- discard that response from scientific comparison;

\\- retry only as a technical retry, up to
\\\`MAX\\\_TECHNICAL\\\_RETRIES\\\`;

\\- do not count the retry as a new candidate;

\\- if all technical retries contain tool calls, mark the candidate
\\\`NO\\\_TOOL\\\_EVAL\\\_FAILED\\\`;

\\- do not replace that candidate with a new question.

The controller must never silently accept a no-tool response without
validating its trace.

**\*\*# 9. Stage D --- two-level adaptive memory\*\***

Adaptive adversarial generation is an explicit research objective.

Use two distinct memories with different scopes.

**\*\*## Memory A --- current-deck question-level memory\*\***

Use:

\`\`\`text

`<deck>`{=html}/memory/memory_A.md

\`\`\`

Memory A is specific to the current XML deck.

After every candidate is judged, inspect the **entire no-tool answer**
and reason about why the no-tool model succeeded, partially succeeded,
failed, or found a shortcut.

For each attempted question, store only a compact high-level lesson:

-   what made the question easy or answerable without GEOS/tools;
-   what analytical shortcut, symmetry, scaling law, monotonicity,
    interpolation, approximation, or pattern the no-tool solver
    exploited;
-   what part of the question genuinely required simulation/tool
    evidence, if any;
-   what should be changed in the next question from this same deck.

Do not store chain-of-thought. Do not turn Memory A into an answer
cache. Avoid exact ground-truth numbers unless essential to describe a
generic failure mode.

**Within the same XML deck, candidate generation sees Memory A only. It
must not read Memory B.**

Memory A accumulates across all categories/questions of the current deck
and is updated after every attempted candidate.

**\*\*## Memory B --- persistent cross-deck compact memory\*\***

Memory B is a compact transferable summary distilled from a completed
deck's Memory A.

It should capture only general lessons that are useful for future XML
decks, such as:

-   question structures that strong no-tool models solve too easily;
-   recurring analytical shortcuts;
-   question mechanisms that genuinely depend on simulation,
    discretization, solver behavior, spatial patterns, counterfactual
    interactions, or regime changes;
-   ambiguity patterns to avoid;
-   general guidance for making future questions harder without making
    them artificial.

Memory B must not contain deck-specific answers, exact values, file
paths, or question-by-question detail.

When a **new XML deck** is introduced, use the accumulated Memory B as
prior cross-deck guidance during initial deck/category design. Then
create a fresh empty Memory A for that new deck.

After generation begins on that new deck, later candidate generation
again uses **only that deck's Memory A**.

Conceptually:

\`\`\`text

NEW DECK ↓ read persistent Memory B for initial deck/category design ↓
create fresh Memory A ↓ Q001 → analyze full no-tool answer → update
Memory A ↓ Q002 reads Memory A only → update Memory A ↓ ... ↓ finish
deck ↓ distill Memory A into compact persistent Memory B

\`\`\`

Memory A answers: **What shortcuts are working on this particular
deck?**

Memory B answers: **What general lessons should transfer to future
decks?**

------------------------------------------------------------------------

**\*\*# 10. Stage E --- category generation\*\***

Generate exactly \\\`N\\\_CATEGORIES\\\` distinct scientific hardness
categories when the deck supports them.

Category generation happens after the one-time deck exploration. For a
new XML deck, category design may read persistent Memory B as cross-deck
guidance. It must not import another deck's Memory A.

Category generation happens after:

\\\`\\\`\\\`text

XML inspection

\\+ one baseline run

\\+ high-level inspection of all baseline outputs

\\+ persistent Memory B read for cross-deck guidance when this is a new
deck

\\\`\\\`\\\`

Do not run additional GEOS simulations merely to invent categories.

Each category must contain:

\\\`\\\`\\\`json

{

"category\\\_id": "C01",

"name": "",

"hardness\\\_mechanism": "",

"why\\\_no\\\_tool\\\_is\\\_expected\\\_to\\\_struggle": "",

"reference\\\_evidence\\\_expected": "",

"common\\\_shortcuts\\\_to\\\_avoid": ""

}

\\\`\\\`\\\`

Possible mechanisms include:

\\- GEOS source-code-dependent behavior;

\\- exact simulation-output-dependent quantities;

\\- parameter threshold/search problems;

\\- solver/timestep/convergence-dependent behavior;

\\- discretization/mesh-dependent behavior;

\\- coupled-physics counterfactuals;

\\- optimization/extremum search;

\\- counterexample discovery;

\\- trajectory-dependent first-crossing/peak questions.

These are examples, not mandatory fixed categories.

Categories should be scientifically distinct, not five wording variants
of the same task.

**\*\*## Category-generation quality rule\*\***

The category generator should seek questions for which the exact answer
depends on information/computation unavailable to a prompt-only model.

Do not claim in advance that failure is guaranteed.

Failure is established empirically by the no-tool evaluation.

Log category-generation cost separately as deck-level overhead.

\\---

**\*\*# 11. Stage F --- candidate generation\*\***

For each category \\\`C01 ... CN\\\`, create exactly:

\\\`\\\`\\\`text

Q001 ... Q00P

\\\`\\\`\\\`

Each slot is one attempted candidate.

Rejected candidates are not replaced.

**\*\*## F1. Generate one candidate at a time\*\***

Before generating candidate \\\`Qi\\\`:

1\\. read the current category definition;

2\\. read \\\`deck\\\_summary.md\\\`;

3\\. read the current adaptive memory;

4\\. read only the baseline-output summaries needed for context;

5\\. do not inspect the future no-tool answer;

6\\. do not run GEOS during the generation call.

Use a separate model invocation for candidate generation so its token
usage and cost can be attributed to that question.

**\*\*## F2. Candidate question requirements\*\***

A good candidate must be:

\\- scientifically meaningful;

\\- self-contained enough to understand the task;

\\- unambiguous;

\\- reproducibly answerable by the tool-enabled GEOS agent;

\\- exact about requested quantities, units, locations, times,
thresholds, or optimization criteria;

\\- difficult because of scientific/numerical dependence, not because of
deliberately confusing prose;

\\- free of the final answer;

\\- free of baseline-output leakage that trivially reveals the answer;

\\- resistant to obvious textbook/steady-state shortcuts when possible;

\- preferably based on ordering/ranking, counterfactual outcomes, regime
transitions, spatial patterns, or discretization/solver behavior rather
than merely demanding a highly precise scalar numerical answer.

\\- written like a normal scientific/PhD-level problem rather than a
repository or file-retrieval task;

\\- explicit about scientifically relevant geometry, material/fluid
properties, initial/boundary/loading conditions, parameter changes,
time/location, units, and requested quantity whenever needed for a
defensible attempt.

The scientific question MUST NOT mention XML/deck filenames, repository
paths, hashes/SHA values, VTU/VTM/HDF5/Silo/restart files, output
filenames, logs, parsers, run IDs, or internal GEOS artifacts.

The scientific question MUST NOT ask the solver to retrieve, inspect,
reconstruct, or report values from a hidden simulation/output file. A
question is not self-contained merely because it identifies a hidden
deck by filename or hash.

Avoid questions that are merely:

\\- direct copy/paste lookups from XML;

\\- arbitrary file-index trivia with no scientific meaning;

\\- analytically trivial from the stated numbers;

\\- ambiguous about "largest", "smallest", "first", "maximum",
tolerance, location, or time;

\\- dependent on undefined relative error near zero;

\\- impossible even for the tool-enabled agent to verify.

Source-code dependence is allowed and useful.

Simulation dependence is allowed and useful.

Questions may require multiple GEOS runs to solve.

**\*\*## F3. Freeze the question\*\***

Once a candidate passes the generation sanity check:

\\- save the exact text;

\\- compute its SHA256;

\\- mark it \\\`FROZEN\\\`;

\\- do not rewrite it after seeing either solver's answer.

If a formatting/ambiguity defect is caught
**\*\*\\\*\\\*before\\\*\\\*\*\*** freezing, a technical rewrite is
allowed within the same candidate slot.

Once frozen, the slot counts as one attempted candidate.

\\---

**\*\*# 12. Generator prompt template\*\***

Use the following intent for each candidate-generation call.

\\\`\\\`\\\`text

You are generating one candidate scientific benchmark question from a
GEOS deck.

You are given:

1\\. a frozen high-level summary of the XML deck;

2\\. a high-level inventory/summary of the one baseline simulation's
outputs;

3\\. one hardness-category definition;

4\\. compact adaptive memory from previous candidates.

Generate exactly one scientifically meaningful question for this
category.

The question should be designed so that its exact answer is likely to
depend

on GEOS source implementation, numerical simulation, discretization,
solver

trajectory, or a controlled multi-run search that a prompt-only model
cannot

directly access.

Do not run GEOS while generating the question.

Do not solve the question.

Do not include the answer.

Write the final question as a self-contained scientific problem. Include
the physical setup and all scientifically relevant information a domain
expert would reasonably need to attempt it.

NEVER mention XML/deck filenames, repository paths, SHA/hash values,
VTU/VTM/HDF5/Silo/restart files, output filenames, logs, parsers, run
IDs, or other internal benchmark artifacts in the candidate question.

NEVER ask the solver to retrieve or reconstruct a value from an
inaccessible file or simulation output. GEOS files/source/outputs are
private resources for the reference solver only.

The hardness mechanism must be scientific or numerical, not lack of file
access. Prefer counterfactuals, nonlinear/transient behavior,
discretization effects, coupled mechanisms, thresholds, parameter
interactions, trajectory-dependent events, or controlled searches.

Do not mention that the question was designed to make an LLM fail.

Do not say "you must use GEOS" inside the scientific question unless
that is

intrinsically part of the task.

Do not use intentionally confusing wording.

Avoid shortcuts and easy patterns recorded in the current deck's Memory
A.

Return a structured result containing:

\\- candidate question text;

\\- scientific objective;

\\- hardness mechanism;

\\- why the answer is expected to require unavailable
evidence/computation;

\\- what evidence the reference agent should be able to use to verify
it;

\\- ambiguity/shortcut self-check.

The controller will freeze the question before evaluation.

\\\`\\\`\\\`

Save the exact generation prompt, raw Cursor trace, model response,
usage, duration, and calculated cost.

\\---

**\*\*# 13. Stage G --- no-tool solving\*\***

The no-tool solver receives:

\\\`\\\`\\\`text

NO GEOS repository

NO XML file access unless XML text is intentionally embedded in the
frozen question

NO source-code access

NO simulation outputs

NO shell

NO file read

NO file write

NO web

NO MCP

NO plugins

NO subagents

NO external tools

\\\`\\\`\\\`

It receives only:

1\\. its internal model knowledge;

2\\. the exact frozen question text;

3\\. the experimental no-tool instruction below.

**\*\*## No-tool prompt template\*\***

Use this tested instruction verbatim except for insertion of the frozen
question:

\\\`\\\`\\\`text

You are the no-tool solver in a scientific reasoning evaluation.

You must answer using ONLY your internal model knowledge and information
explicitly written in this prompt.

You MUST NOT use or attempt to use any external tool or capability, even
if tools are available to you.

Specifically, do NOT:

\\- read, search, grep, glob, inspect, create, or edit files;

\\- access any repository or source code;

\\- access the GEOS repository, GEOS source code, or simulation outputs;

\\- use Read, Grep, Glob, Search, or similar tools;

\\- execute shell or terminal commands;

\\- run GEOS, Python, or any other program;

\\- use web search or external documentation;

\\- use MCP, plugins, subagents, connectors, or any other external tool.

Do not make any tool call.

Solve the frozen scientific question using only your own reasoning and
the information explicitly provided below. Do not refuse merely because
tools are unavailable.

The frozen question is intended to be self-contained scientifically.
Attempt the scientific problem directly. If an exact numerical answer
cannot be derived analytically, give your best scientific reasoning,
prediction, derivation, or estimate from the stated setup. Clearly
distinguish what is known from what is estimated or uncertain. Do not
treat the absence of repository or simulation-file access as the answer
unless the question itself is invalid.

Return only your scientific answer and reasoning.

\\--- FROZEN QUESTION ---

\\\<question text\>

\\--- END QUESTION ---

\\\`\\\`\\\`

**\*\*## No-tool contamination rule\*\***

If the trace contains **\*\*\\\*\\\*any\\\*\\\*\*\***
\\\`"type":"tool\\\_call"\\\` event, the run is invalid even if the tool
was denied, failed, or the final answer looks reasonable.

A contaminated no-tool answer must never be used in acceptance/rejection
analysis.

\\---

**\*\*# 14. Stage H --- independent tool-enabled reference solving\*\***

The reference solver receives the **\*\*\\\*\\\*same frozen scientific
question\\\*\\\*\*\***.

It receives full access to:

\\- GEOS repository;

\\- GEOS source;

\\- terminal/shell;

\\- Python;

\\- reusable parsers;

\\- question workspace;

\\- ability to create modified XML copies;

\\- ability to run the simulations scientifically necessary to solve the
question, while avoiding brute-force or redundant runs.

It must **\*\*\\\*\\\*not receive the no-tool answer\\\*\\\*\*\***
before its reference answer is frozen and verified.

If the controller ran the no-tool condition first, hold the no-tool
response outside the reference solver's visible question workspace until
the tool-enabled answer is frozen.

**\*\*## Tool-enabled reference prompt template\*\***

\\\`\\\`\\\`text

You are the reference scientific solver for a GEOS benchmark.

Solve the frozen scientific question independently and establish the

reference answer using the GEOS repository, source code, numerical
simulation,

generated outputs, and analysis tools whenever necessary.

Do not guess a GEOS-specific quantity when it can be established from
actual

source code, simulation output, or a controlled search.

Important rules:

1\\. Solve independently. You have not been given the no-tool model's
answer.

2\\. Never modify the original XML deck.

3\\. Work only with copied/derived XML files inside this question's
workspace.

4\\. Activate the \\\`geos\\\` conda environment before GEOS/Python
execution.

5\\. Every GEOS run must use its own simulation subdirectory and output
directory.

6\\. Preserve the exact XML used for every simulation.

7\\. Preserve the exact GEOS command, stdout, stderr, exit code, and
runtime.

8\\. Use existing reusable parsers when possible.

9\\. If a required parser does not exist, create a reusable format-level
parser,

not a one-question parser.

10\\. If source implementation is relevant, inspect the actual
implementation.

11\\. If the task is a threshold, optimization, counterexample, or
parameter

    search, run the simulations necessary to establish the answer.

12\\. Do not reuse stale outputs from another run.

13\\. After solving, verify the answer from the evidence already
produced.

14\\. Do not repeat simulations solely for verification.

15\\. Additional simulations are allowed only if they are necessary
because the

    scientific solution itself is incomplete or a discovered error must be fixed.

Return a structured result containing:

\\- final reference answer;

\\- units and numerical precision where relevant;

\\- concise scientific reasoning;

\\- exact evidence used;

\\- source files/lines when source-dependent;

\\- simulation IDs/output files/variables when simulation-dependent;

\\- concise reproduction procedure;

\\- uncertainty/limitations;

\\- verification checklist result.

\\\`\\\`\\\`

\\---

**\*\*# 15. Simulation execution protocol for a candidate\*\***

Every reference-solver GEOS execution must live under:

\\\`\\\`\\\`text

reference/simulations/sim\\\_001/

reference/simulations/sim\\\_002/

...

\\\`\\\`\\\`

Each simulation directory must contain:

\\\`\\\`\\\`text

input.xml

command.txt

stdout.log

stderr.log

run.json

output/

\\\`\\\`\\\`

Never reuse a previous simulation's output directory.

Before each run:

\\\`\\\`\\\`text

\\- confirm copied XML exists;

\\- confirm original XML has not changed;

\\- confirm output directory is new/empty;

\\- activate conda environment;

\\- record command.

\\\`\\\`\\\`

After each run:

\\\`\\\`\\\`text

\\- record exit code;

\\- record wall time;

\\- record output manifest;

\\- increment simulation\\\_runs for the candidate.

\\\`\\\`\\\`

If a run fails and must be corrected/retried:

\\- preserve the failed run directory;

\\- create a new simulation ID;

\\- increment retry count;

\\- do not overwrite the failed evidence.

\\---

**\*\*# 16. Tool-enabled reference finalization\*\***

There is no separate reference-verification stage.

The independently produced tool-enabled answer is treated as the
reference answer for the benchmark run.

Before exposing the no-tool answer to the judge:

-   freeze the tool-enabled final answer;
-   save the simulation/tool artifacts already produced during solving;
-   save a concise high-level scientific summary of how the answer was
    obtained;
-   record the number of simulations, tool calls, runtime, and cost;
-   do not rerun simulations solely to verify or reconfirm the result.

The high-level summary should state, as relevant:

-   what parameter(s) or setup(s) were changed;
-   what GEOS runs or controlled comparisons were performed;
-   what scientific quantity, field, location, trajectory, ordering,
    threshold, or solver behavior was examined;
-   how that evidence led to the final answer.

Do not save chain-of-thought as the benchmark explanation.

If the tool-enabled solver itself fails to produce a final answer, mark
`REFERENCE_FAILED`. Do not invent or repair the answer using the no-tool
response.

------------------------------------------------------------------------

**\*\*# 17. Stage I --- no-tool/reference comparison\*\***

Only after the tool-enabled reference answer has been frozen may the
evaluator see both answers.

Use a separate judge call whose cost is logged.

**\*\*## Judge prompt template\*\***

\\\`\\\`\\\`text

You are evaluating a no-tool model response against a tool-enabled GEOS
reference

solution.

The reference solution is already frozen. Do not change it based

on the no-tool response.

Compare:

1\\. the exact frozen scientific question;

2\\. the no-tool answer and reasoning;

3\\. the tool-enabled reference answer and concise evidence.

Classify the no-tool response as exactly one of:

CORRECT

PARTIALLY\\\_CORRECT

INCORRECT

ABSTAIN

Use scientific reasoning, not string matching.

Consider both the requested final answer and the reasoning.

If the numerical answer is close only by coincidence but the
interpretation

or scientific reasoning is materially wrong, do not mark it fully
correct.

If the answer and the essential reasoning are correct, mark CORRECT even
if

wording differs.

For PARTIALLY\\\_CORRECT, additionally decide:

meaningful\\\_failure = true \| false

A meaningful failure is a discrepancy that matters for the scientific
task,

An \`ABSTAIN\` is meaningful only when the question is scientifically
self-contained and the model fails to make a defensible scientific
prediction/derivation from the stated setup. If abstention is primarily
caused by withheld necessary scientific information or a request for
inaccessible file/repository/output contents, classify the question as
\`QUESTION_INVALID\`; do not count it as model failure.

for example:

\\- wrong GEOS implementation;

\\- wrong threshold/extremum;

\\- wrong timestep/location/element;

\\- wrong interpretation;

\\- materially wrong numerical value;

\\- unsupported claim presented as exact when the question requires an
exact

simulation-defined result.

Return:

\\- verdict;

\\- meaningful\\\_failure;

\\- concise decisive comparison;

\\- key discrepancy, if any.

\\\`\\\`\\\`

\\---

**\*\*# 18. Acceptance / rejection policy\*\***

After judging:

**\*\*### Accept\*\***

Accept the candidate into the final benchmark if:

\\\`\\\`\\\`text

verdict = INCORRECT

\\\`\\\`\\\`

or:

\\\`\\\`\\\`text

verdict = ABSTAIN

AND question_self_contained = true

AND abstention_is_scientifically_meaningful = true

\\\`\\\`\\\`

or:

\\\`\\\`\\\`text

verdict = PARTIALLY\\\_CORRECT

AND meaningful\\\_failure = true

\\\`\\\`\\\`

**\*\*### Reject\*\***

Reject if:

\\\`\\\`\\\`text

verdict = CORRECT

\\\`\\\`\\\`

or:

\\\`\\\`\\\`text

verdict = PARTIALLY\\\_CORRECT

AND meaningful\\\_failure = false

\\\`\\\`\\\`

**\*\*### Invalid/unresolved\*\***

Do not accept if:

\\\`\\\`\\\`text

NO\\\_TOOL\\\_EVAL\\\_FAILED

REFERENCE\\\_FAILED

REFERENCE\\\_UNVERIFIED

QUESTION\\\_INVALID

\\\`\\\`\\\`

Do not generate a replacement candidate for that slot.

Keep every rejected/invalid candidate's artifacts and metrics.

\\---

**\*\*# 19. Memory A update after every candidate and Memory B
distillation\*\***

After every verdict, update the current deck's Memory A.

Use the **full no-tool answer** as the evidence for this analysis, but
save only compact high-level conclusions.

For each candidate record:

1.  whether the no-tool model succeeded, partially succeeded, failed, or
    abstained;
2.  why it was able or unable to answer without GEOS/tools;
3.  the shortcut or approximation it exploited, if any;
4.  what made the question too easy;
5.  what mechanism genuinely resisted prompt-only reasoning;
6.  concise guidance for the next candidate from this same XML deck.

The next candidate-generation call must read the updated **Memory A
only**.

Do not show Memory B to later questions from the same deck.

After all candidate slots for the XML deck are complete, distill the
accumulated Memory A into compact **Memory B**. Memory B keeps only
transferable cross-deck lessons and becomes prior guidance when a future
XML deck is introduced.

------------------------------------------------------------------------

**\*\*# 20. Cost accounting\*\***

Cursor CLI does not need to report a dollar cost directly.

For every model invocation, capture Cursor's token usage and compute
**\*\*\\\*\\\*estimated provider API cost\\\*\\\*\*\*** using the
verified provider pricing table below.

Do not use Cursor subscription/credit pricing.

**\*\*## Required usage fields\*\***

Capture when available:

\\\`\\\`\\\`text

inputTokens

outputTokens

cacheReadTokens

cacheWriteTokens

\\\`\\\`\\\`

Also capture:

\\\`\\\`\\\`text

duration\\\_ms

duration\\\_api\\\_ms

requested\\\_model

reported\\\_model

session\\\_id

request\\\_id

\\\`\\\`\\\`

Use \\\`stream-json\\\` when useful because it preserves model
initialization, tool events, and the final usage object.

Save the raw trace before parsing metrics.

**\*\*## Verified provider pricing\*\***

USD per 1 million tokens:

\\\`\\\`\\\`json

{

"gpt-5.6-sol": {

    "input": 5.00,

    "output": 30.00,

    "cache\\\_read": 0.50,

    "cache\\\_write": 6.25

},

"gpt-5.6-sol-pro": {

    "input": 2.50,

    "output": 15.00,

    "cache\\\_read": 0.25,

    "cache\\\_write": 3.125

},

"gpt-5.6-terra": {

    "input": 2.50,

    "output": 15.00,

    "cache\\\_read": 0.25,

    "cache\\\_write": 3.125

},

"gpt-5.6-luna": {

    "input": 1.00,

    "output": 6.00,

    "cache\\\_read": 0.10,

    "cache\\\_write": 1.25

},

"gpt-5.6-luna-pro": {

    "input": 1.00,

    "output": 6.00,

    "cache\\\_read": 0.10,

    "cache\\\_write": 1.25

},

"claude-opus-5": {

    "input": 5.00,

    "output": 25.00,

    "cache\\\_read": 0.50,

    "cache\\\_write": 6.25

},

"claude-opus-4-8": {

    "input": 5.00,

    "output": 25.00,

    "cache\\\_read": 0.50,

    "cache\\\_write": 6.25

},

"claude-opus-4-6": {

    "input": 5.00,

    "output": 25.00,

    "cache\\\_read": 0.50,

    "cache\\\_write": 6.25

},

"claude-sonnet-4-6": {

    "input": 3.00,

    "output": 15.00,

    "cache\\\_read": 0.30,

    "cache\\\_write": 3.75

},

"claude-haiku-4-5": {

    "input": 1.00,

    "output": 5.00,

    "cache\\\_read": 0.10,

    "cache\\\_write": 1.25

}

}

\\\`\\\`\\\`

Treat this table as experiment configuration.

Do not silently alter it.

If a requested model has no pricing row, stop and request a verified
rate rather than guessing.

**\*\*## Cost formula\*\***

For one Cursor/model invocation:

\\\`\\\`\\\`text

estimated\\\_api\\\_cost\\\_usd =

    inputTokens      / 1,000,000 \\\* input\\\_rate

\\+ outputTokens / 1,000,000 \\\* output\\\_rate

\\+ cacheReadTokens / 1,000,000 \\\* cache\\\_read\\\_rate

\\+ cacheWriteTokens / 1,000,000 \\\* cache\\\_write\\\_rate

\\\`\\\`\\\`

Store component costs separately.

**\*\*## Per-candidate cost buckets\*\***

For every candidate record:

\\\`\\\`\\\`text

question\\\_generation

no\\\_tool\\\_solving

tool\\\_solving

comparison\\\_judgment

\\\`\\\`\\\`

For each bucket store:

\\\`\\\`\\\`text

calls

input\\\_tokens

output\\\_tokens

cache\\\_read\\\_tokens

cache\\\_write\\\_tokens

input\\\_cost\\\_usd

output\\\_cost\\\_usd

cache\\\_read\\\_cost\\\_usd

cache\\\_write\\\_cost\\\_usd

estimated\\\_api\\\_cost\\\_usd

wall\\\_time\\\_seconds

\\\`\\\`\\\`

Then compute:

\\\`\\\`\\\`text

candidate\\\_estimated\\\_api\\\_cost\\\_usd =

    generation\\\_cost

\\+ no\\\_tool\\\_cost

\\+ tool\\\_solving\\\_cost

\\+ judgment\\\_cost

\\\`\\\`\\\`

Also report the three primary research costs explicitly:

\\\`\\\`\\\`text

question\\\_generation\\\_estimated\\\_api\\\_cost\\\_usd

no\\\_tool\\\_solving\\\_estimated\\\_api\\\_cost\\\_usd

tool\\\_solving\\\_estimated\\\_api\\\_cost\\\_usd

\\\`\\\`\\\`

Do not merge them.

Category-generation and one-time exploration costs are deck-level
overhead and should be logged separately rather than arbitrarily divided
across questions.

If multiple calls are needed inside one bucket, sum them.

If resumed-session usage is cumulative rather than per-call, compute
deltas to prevent double counting. Prefer fresh one-shot invocations
when possible.

\\\`outputTokens\\\` should be costed exactly as reported by Cursor,
including any reasoning tokens included in that field.

\\---

**\*\*# 21. Runtime, tool-call, simulation, and retry metrics\*\***

For every candidate record:

\\\`\\\`\\\`text

question\\\_generation\\\_wall\\\_time\\\_seconds

no\\\_tool\\\_wall\\\_time\\\_seconds

tool\\\_solving\\\_wall\\\_time\\\_seconds

judgment\\\_wall\\\_time\\\_seconds

question\\\_generation\\\_tool\\\_calls

no\\\_tool\\\_tool\\\_calls

tool\\\_solving\\\_tool\\\_calls

judgment\\\_tool\\\_calls

simulation\\\_runs

retry\\\_attempts

\\\`\\\`\\\`

Definitions:

**\*\*###\*\*** \\\`simulation\\\_runs\\\`

Increment once for every actual \\\`geosx\\\` process launch for that
candidate.

Failed GEOS launches still count.

**\*\*###\*\*** \\\`tool\\\_calls\\\`

Count actual external tool invocations visible in Cursor's execution
trace.

For a valid no-tool run:

\\\`\\\`\\\`text

no\\\_tool\\\_tool\\\_calls\\\_attempted = 0

no\\\_tool\\\_tool\\\_calls\\\_successful = 0

\\\`\\\`\\\`

A denied or failed tool call still counts as an attempted tool call and
invalidates that no-tool response.

If the current Cursor output format does not expose a trustworthy
tool-call count, use:

\\\`\\\`\\\`text

null

\\\`\\\`\\\`

Do not estimate it.

**\*\*###\*\*** \\\`retry\\\_attempts\\\`

Count explicit controller-level retries caused by:

\\- failed model invocation;

\\- malformed structured response;

\\- failed/incorrect simulation setup;

\\- parser failure requiring a corrected rerun;

\\- invalid no-tool contamination.

Do not count normal internal model reasoning as a retry.

\\---

**\*\*# 22.\*\*** \\\`result.json\\\` **\*\*schema\*\***

Each candidate must have a machine-readable record similar to:

\\\`\\\`\\\`json

{

"question\\\_id": "C03\\\_Q004",

"deck\\\_slug": "",

"deck\\\_sha256": "",

"category\\\_id": "C03",

"candidate\\\_index": 4,

"question\\\_sha256": "",

"question\\\_status": "FROZEN",

"models": {

    "generator": "",

    "no\\\_tool": "",

    "tool\\\_solver": "",

    "judge": ""

},

"no\\\_tool": {

    "run\\\_valid": true,

    "tool\\\_calls": 0,

    "answer\\\_path": "",

    "usage": {},

    "estimated\\\_api\\\_cost\\\_usd": null,

    "wall\\\_time\\\_seconds": null

},

"reference": {

    "answer\\\_path": "",

    "simulation\\\_runs": 0,

    "tool\\\_calls": null,

    "retry\\\_attempts": 0,

    "usage": {},

    "estimated\\\_api\\\_cost\\\_usd": null,

    "wall\\\_time\\\_seconds": null

},

"judge": {

    "verdict": "INCORRECT",

    "meaningful\\\_failure": true,

    "reason": ""

},

"generation": {

    "usage": {},

    "estimated\\\_api\\\_cost\\\_usd": null,

    "wall\\\_time\\\_seconds": null

},

"costs": {

    "question\\\_generation\\\_estimated\\\_api\\\_cost\\\_usd": null,

    "no\\\_tool\\\_solving\\\_estimated\\\_api\\\_cost\\\_usd": null,

    "tool\\\_solving\\\_estimated\\\_api\\\_cost\\\_usd": null,

    "comparison\\\_judgment\\\_estimated\\\_api\\\_cost\\\_usd": null,

    "candidate\\\_estimated\\\_api\\\_cost\\\_usd": null

},

"acceptance": {

    "accepted": true,

    "reason": ""

}

}

\\\`\\\`\\\`

Extend the schema as needed, but do not remove core provenance fields.

\\---

**\*\*# 23. W&B logging\*\***

Every attempted candidate must be represented in W&B.

**\*\*## Recommended organization\*\***

Use:

\\\`\\\`\\\`text

project = WANDB\\\_PROJECT

group = \\\<deck\\\_slug\>

run name =
\\\<deck\\\_slug\>\\\_\\\_\\\<category\\\_id\>\\\_\\\_\\\<question\\\_id\>

job\\\_type = candidate\\\_evaluation

\\\`\\\`\\\`

Tags should include:

\\\`\\\`\\\`text

deck\\\_slug

category\\\_id

accepted/rejected

model

verdict

\\\`\\\`\\\`

**\*\*## Log candidate metrics\*\***

At minimum:

\\\`\\\`\\\`text

accepted

verdict

meaningful\\\_failure

simulation\\\_runs

retry\\\_attempts

question\\\_generation\\\_wall\\\_time\\\_seconds

no\\\_tool\\\_wall\\\_time\\\_seconds

tool\\\_solving\\\_wall\\\_time\\\_seconds

judgment\\\_wall\\\_time\\\_seconds

question\\\_generation\\\_tool\\\_calls

no\\\_tool\\\_tool\\\_calls

tool\\\_solving\\\_tool\\\_calls

judgment\\\_tool\\\_calls

question\\\_generation\\\_input\\\_tokens

question\\\_generation\\\_output\\\_tokens

question\\\_generation\\\_cache\\\_read\\\_tokens

question\\\_generation\\\_cache\\\_write\\\_tokens

question\\\_generation\\\_estimated\\\_api\\\_cost\\\_usd

no\\\_tool\\\_input\\\_tokens

no\\\_tool\\\_output\\\_tokens

no\\\_tool\\\_cache\\\_read\\\_tokens

no\\\_tool\\\_cache\\\_write\\\_tokens

no\\\_tool\\\_solving\\\_estimated\\\_api\\\_cost\\\_usd

tool\\\_solving\\\_input\\\_tokens

tool\\\_solving\\\_output\\\_tokens

tool\\\_solving\\\_cache\\\_read\\\_tokens

tool\\\_solving\\\_cache\\\_write\\\_tokens

tool\\\_solving\\\_estimated\\\_api\\\_cost\\\_usd

judgment\\\_estimated\\\_api\\\_cost\\\_usd

candidate\\\_estimated\\\_api\\\_cost\\\_usd

\\\`\\\`\\\`

**\*\*## Log candidate artifacts\*\***

Upload a compact W&B artifact containing:

\\\`\\\`\\\`text

frozen question

generator output

no-tool answer

reference answer

tool-enabled solution summary

judge result

result.json

reproduction procedure

simulation manifest

command logs

relevant parser/extraction evidence

\\\`\\\`\\\`

By default, do not upload huge raw GEOS output directories unless:

\\\`\\\`\\\`text

WANDB\\\_UPLOAD\\\_RAW\\\_SIMULATION\\\_OUTPUTS = true

\\\`\\\`\\\`

All raw outputs must still remain locally under \\\`D\\\`.

If W&B is not authenticated/configured, do not silently skip logging.
Stop before candidate generation and report the configuration problem.

Never print or store API keys in benchmark logs.

\\---


**W&B master experiment tables**

In addition to individual candidate runs, maintain deck-level W&B tables so the experiment status can be understood without opening each question run.

### Question-level master table

Maintain one row per attempted question with at least these columns:

```text
xml_deck
deck_slug
category_id
category_name
question_id
candidate_index
status
no_tool_verdict
accepted
rejection_or_failure_reason
question_generation_cost_usd
no_tool_cost_usd
tool_agent_cost_usd
judge_cost_usd
total_question_cost_usd
geos_simulation_runs
```

Interpret `status` using explicit values such as:

```text
ACCEPTED
REJECTED
GENERATION_FAILED
NO_TOOL_EVAL_FAILED
REFERENCE_FAILED
JUDGE_FAILED
QUESTION_INVALID
```

`accepted` is a boolean and must not be used as a synonym for successful pipeline execution.

The cost columns must remain separate:

- `question_generation_cost_usd`: model/API cost for generating the candidate;
- `no_tool_cost_usd`: prompt-only solver model/API cost;
- `tool_agent_cost_usd`: tool-enabled GEOS solver model/API cost;
- `judge_cost_usd`: comparison/judgment model/API cost;
- `total_question_cost_usd`: sum of the four costs above.

Do not include GEOS compute time itself as API cost. Track GEOS executions separately in `geos_simulation_runs`.

### Deck/category summary table

Also maintain a compact aggregate table with one row per XML deck and category:

```text
xml_deck
deck_slug
category_id
category_name
questions_planned
questions_generated
questions_evaluated
questions_accepted
questions_rejected
questions_failed
total_geos_simulation_runs
generation_cost_usd
no_tool_cost_usd
tool_agent_cost_usd
judge_cost_usd
total_cost_usd
```

Include a deck-total row aggregating all categories for that XML deck.

Update both W&B tables after every attempted candidate so the current state is visible directly from the W&B project. The tables are the primary human-readable experiment overview; the experiment does not require progress/loss curves.

The tables must make it possible to answer at a glance:

- which XML/deck is being evaluated;
- which category each question belongs to;
- how many questions were planned and generated;
- which individual questions were accepted, rejected, invalid, or failed;
- how many questions in each category were accepted/rejected/failed;
- no-tool and tool-agent cost for each individual question;
- total cost and GEOS simulation count per question, category, and deck.


**\*\*# 24. LaTeX benchmark output\*\***

For every **\*\*\\\*\\\*accepted\\\*\\\*\*\*** candidate, write a
concise LaTeX entry.

Each accepted question must include:

1\\. question ID and category;

2\\. frozen scientific question;

3\\. verified answer;

4\\. concise high-level solution/reproduction procedure;

5\\. only the information needed for another researcher to reproduce the
result.

The reproduction description should say things such as:

\\- which XML parameter(s) were changed;

\\- which GEOS runs/search were performed;

\\- which output variable/file was inspected;

\\- which criterion selected the final result.

Do not dump raw logs into the LaTeX.

Do not include long chain-of-thought-style reasoning.

Append accepted entries to:

\\\`\\\`\\\`text

\\\<deck\>/accepted/accepted\\\_questions.tex

\\\`\\\`\\\`

Also keep each candidate's own:

\\\`\\\`\\\`text

question.tex

\\\`\\\`\\\`

Rejected candidates should remain in the machine-readable archive but
should not be added to \\\`accepted\\\_questions.tex\\\`.

\\---

**\*\*# 25. Candidate workflow state machine\*\***

For every candidate slot, execute this order:

\\\`\\\`\\\`text

READ CURRENT DECK MEMORY A

        ↓

GENERATE CANDIDATE

        ↓

STATIC SANITY CHECK

        ↓

FREEZE QUESTION

        ↓

RUN STRICT NO-TOOL SOLVER

        ↓

HOLD NO-TOOL RESPONSE AWAY FROM REFERENCE SOLVER

        ↓

RUN INDEPENDENT TOOL-ENABLED REFERENCE SOLVER

        ↓

EXPOSE BOTH ANSWERS TO JUDGE

        ↓

CLASSIFY NO-TOOL RESPONSE

        ↓

ACCEPT / REJECT / INVALID

        ↓

SAVE RESULT.JSON

        ↓

LOG TO W&B

        ↓

ANALYZE FULL NO-TOOL ANSWER AND UPDATE MEMORY A

        ↓

MOVE TO NEXT CANDIDATE

\\\`\\\`\\\`

Never change the frozen question after either solver has seen it.

\\---

**\*\*# 26. Static candidate sanity check before freezing\*\***

Before either solver sees a question, check:

\\\`\\\`\\\`text

\[ \] Scientifically meaningful

\[ \] Self-contained scientific setup: a domain expert can make a
defensible attempt from the question text alone

\[ \] Contains no XML/deck filename, repository path, SHA/hash,
VTU/VTM/HDF5/Silo/restart filename, output path, parser/log/run ID, or
other internal benchmark artifact

\[ \] Does not ask the solver to retrieve/reconstruct hidden file or
simulation-output contents

\[ \] Hardness comes from scientific/numerical reasoning rather than
unavailable file/tool access

\[ \] If all repository/file references were removed, the scientific
task would still be well-defined and attemptable

\[ \] Unambiguous

\[ \] Units defined where needed

\[ \] Search range/domain defined where needed

\[ \] "first"/"largest"/"smallest"/"maximum" semantics precise

\[ \] Tie behavior defined where needed

\[ \] Time/location definition precise

\[ \] No answer leakage

\[ \] No obvious contradiction

\[ \] Tool-enabled solver has a realistic solution path

\[ \] Not a trivial direct XML lookup unless source-code behavior is the
point

\[ \] Not obviously reducible to a simple analytical shortcut already
known from memory

\\\`\\\`\\\`

If a defect is caught before freezing, revise within the same
candidate-generation slot.

Do not run GEOS merely to perform this sanity check.

\\---

**\*\*# 27. Handling source-code-dependent questions\*\***

Implementation-sensitive questions are valid only when the
**\*\*question itself is phrased scientifically and is
self-contained\*\***. Local source code is private evidence for the
reference solver; the benchmark question must not ask the no-tool solver
to inspect, identify, quote, or know a hidden source file.

Examples include questions whose exact answer depends on:

\\- actual constitutive-law implementation;

\\- component conventions;

\\- caps/clamping;

\\- history dependence;

\\- derivatives/Jacobian behavior;

\\- hidden defaults;

\\- internal field transformations.

The no-tool model may still answer from training-time memory. That is
allowed.

The experiment measures whether it is correct.

The reference solver must verify source-dependent claims against the
actual local GEOS implementation used in the experiment.

Save file paths and concise line/function evidence.

\\---

**\*\*# 28. Handling simulation-dependent questions\*\***

For simulation-defined answers:

\\- the benchmark question must state the scientific setup and requested
observable without referring to hidden simulation files;

\\- simulation output is private reference evidence, not part of the
question's retrieval task;

\\- report actual simulated values, not continuum approximations;

\\- preserve the exact XML used;

\\- preserve the exact output;

\\- identify variable and time/location;

\\- state numerical precision appropriately;

\\- if the question needs a search, preserve the search sequence.

A no-tool model is allowed to estimate.

The judge decides whether the estimate satisfies the actual scientific
question.

\\---

**\*\*# 29. Handling parameter searches and optimization\*\***

If a candidate asks for:

\\- a threshold;

\\- smallest/largest parameter;

\\- first crossing;

\\- maximum/minimum over a grid;

\\- counterexample;

\\- optimal configuration;

the reference solver must use an explicit search procedure sufficient to
support the claimed answer.

Save:

\\\`\\\`\\\`text

search domain

tested parameter values

simulation IDs

extracted metric

selection criterion

stopping condition

ties

\\\`\\\`\\\`

Do not claim global optimality outside the specified search domain.

\\---

**\*\*# 30. Avoiding stale-output errors\*\***

Before parsing any simulation:

\\- confirm the parser points to that simulation's own output directory;

\\- confirm file timestamps/manifest correspond to the run;

\\- never parse a shared generic \\\`output/\\\` directory;

\\- never overwrite an earlier run;

\\- store simulation ID in extracted-result metadata.

This rule is mandatory.

\\---

**\*\*# 30A. Unexpected technical error recovery\*\***

If an unexpected technical error occurs that is not explicitly covered
by this protocol:

1\. diagnose the error using available controller/reference tools and
logs;

2\. attempt a technically appropriate repair;

3\. do not weaken or bypass any experimental-validity requirement;

4\. do not fabricate simulation results, provenance, or ground truth;

5\. record the error, diagnosis, repair, and retry count;

6\. continue after successful recovery;

7\. stop only if the error cannot be repaired without violating the
protocol.

This authority applies to technical execution, not to changing a frozen
question or relaxing self-containment, no-tool, or
reference-independence rules.

---

**\*\*# 31. Final deck-level summary\*\***

After exactly:

\\\`\\\`\\\`text

N\\\_CATEGORIES \\\* QUESTIONS\\\_PER\\\_CATEGORY

\\\`\\\`\\\`

candidate slots have been processed, stop.

Create \\\`final\\\_summary.json\\\` containing at least:

\\\`\\\`\\\`text

deck

deck\\\_sha256

model/configuration

N\\\_CATEGORIES

QUESTIONS\\\_PER\\\_CATEGORY

attempted\\\_candidates

accepted\\\_candidates

rejected\\\_candidates

invalid\\\_candidates

counts by category

counts by verdict

no-tool failure rate

no-tool abstention rate

total GEOS simulation runs

total retries

total question-generation cost

total no-tool-solving cost

total tool-solving cost

total judgment cost

total estimated API cost

mean/median cost per candidate

mean/median simulations per accepted candidate

mean/median tool-solving wall time

accepted question IDs

rejected question IDs

invalid question IDs

\\\`\\\`\\\`

Also create:

\\\`\\\`\\\`text

summary/candidates.csv

summary/costs.csv

\\\`\\\`\\\`

Do not generate replacement questions after the planned candidate slots
are exhausted.

\\---

**\*\*# 32. Failure policy\*\***

**\*\*## Baseline failure\*\***

If the one-time original baseline simulation fails:

\\\`\\\`\\\`text

STOP

\\\`\\\`\\\`

Do not generate questions.

**\*\*## Parser failure\*\***

Attempt to fix/create the parser without rerunning GEOS.

Only rerun GEOS if the actual simulation output is missing/corrupt and
the run itself therefore did not produce usable evidence.

**\*\*## No-tool contamination\*\***

Retry the no-tool invocation up to \\\`MAX\\\_TECHNICAL\\\_RETRIES\\\`.

If technical isolation still fails:

\\\`\\\`\\\`text

candidate status = NO\\\_TOOL\\\_EVAL\\\_FAILED

\\\`\\\`\\\`

Do not replace the question.

**\*\*## Reference-solver failure\*\***

Preserve all evidence.

If it cannot establish and verify a reference answer:

\\\`\\\`\\\`text

candidate status = REFERENCE\\\_FAILED

\\\`\\\`\\\`

Do not accept.

Do not replace.

**\*\*## W&B failure\*\***

Because W&B logging is required, do not silently continue without it.

Preserve local state and stop cleanly so the run can resume without
losing completed candidates.

\\---

**\*\*# 33. Resume behavior\*\***

The workflow must be resumable.

Before starting:

\\- scan existing deck state;

\\- never rerun a completed baseline;

\\- never regenerate a frozen candidate;

\\- never overwrite completed candidate records;

\\- resume at the earliest incomplete state.

Examples:

\\\`\\\`\\\`text

question frozen + no-tool complete + reference incomplete

→ resume reference solving

reference verified + judge missing

→ run judge only

candidate complete + W&B upload missing

→ upload/log only

\\\`\\\`\\\`

Do not spend model or simulation cost repeating completed work
unnecessarily.

\\---

**\*\*# 34. What the controller should optimize for\*\***

Optimize for:

\\\`\\\`\\\`text

scientific validity

reproducibility

hardness against prompt-only reasoning

minimal unnecessary GEOS execution

minimal unnecessary model calls

clean provenance

clear separation of no-tool and tool-enabled conditions

accurate cost accounting

adaptive learning from previous candidates

\\\`\\\`\\\`

Do not optimize for making questions look complicated.

A short question with a genuinely simulation/source-dependent answer is
preferable to a long question that is analytically trivial.

\\---

**\*\*# 35. Completion condition\*\***

The deck experiment is complete only when:

\\\`\\\`\\\`text

\[ \] baseline XML was read

\[ \] unchanged baseline was run exactly once

\[ \] every baseline output file was inventoried

\[ \] all baseline outputs were understood at high level

\[ \] reusable parsers were prepared

\[ \] no-tool runner passed technical preflight

\[ \] persistent Memory B was used for new-deck guidance when available
and a fresh Memory A was created

\[ \] N categories were created

\[ \] exactly P candidate slots per category were attempted

\[ \] every valid no-tool trace contained zero \\\`tool\\\_call\\\`
events

\[ \] every reference solution was independently solved

\[ \] every candidate with a usable reference has a frozen tool-enabled
answer and high-level tool-use summary

\[ \] every candidate received a verdict/status

\[ \] Memory A was updated after every candidate and distilled into
Memory B at deck completion

\[ \] all candidate metrics and costs were saved

\[ \] W&B logging completed

\[ \] accepted questions were written to LaTeX

\[ \] final deck-level summary was written

\\\`\\\`\\\`

Then stop.

Do not generate additional candidates unless the experimenter explicitly
changes \\\`N\\\_CATEGORIES\\\` or \\\`QUESTIONS\\\_PER\\\_CATEGORY\\\`.
