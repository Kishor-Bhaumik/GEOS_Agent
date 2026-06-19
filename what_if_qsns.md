# GEOS: Counterfactual and What-If Analysis

GEOS is an open-source, HPC-oriented multiphysics simulator for subsurface and geomechanical problems (https://geosx-geosx.readthedocs-hosted.com). It couples solvers for single- and multi-phase fluid flow (with wells), solid mechanics, fracture mechanics (discrete and hydraulic fracturing), poromechanics, and thermal transport, on top of a constitutive-model library (elastic, poro-elastic, Drucker-Prager family, Modified Cam-Clay, thermo-poro-elastic, etc.) and large-scale unstructured/VTK meshing. Where a geometry engine like GEOS-the-library answers "what's inside, outside, or overlapping," GEOS-the-simulator answers a different kind of counterfactual: "If we change this operational parameter, material property, well design, or loading condition, how does the coupled physical system respond — and does it cross a failure, leakage, or performance threshold compared to the base case?"

## Types of Counterfactual / What-If Analysis

**1. Parameter and property sensitivity:** Vary a material, fluid, or rock property (permeability, Young's modulus, cohesion, relative permeability curve, thermal conductivity) and recompute the field response to determine which parameters control the outcome and by how much.

**2. Operational scenario comparison:** Change an operational decision (injection rate, well placement, completion design, production schedule, drilling mud weight) and compare resulting pressure, stress, or flow fields against the baseline plan.

**3. Failure / threshold and risk analysis:** Push a loading or injection scenario until a geomechanical or hydraulic threshold is crossed (yield, slip, fracture propagation, wellbore breakout) and identify the conditions under which the system transitions from stable to unstable.

**4. Coupled-process interaction analysis:** Toggle or strengthen the coupling between physics (flow–mechanics, thermal–poromechanics, fracture–flow) to determine whether a single-physics approximation is adequate or whether cross-physics feedback changes the answer.

**5. Design and geometry alternatives:** Compare alternative well trajectories, fracture stage spacing, casing/cement designs, or mesh/discretization choices to see which configuration best satisfies an engineering objective (recovery, containment, structural integrity).

**6. Constitutive-model and calibration counterfactuals:** Swap one constitutive law for another (e.g., Drucker-Prager vs. Modified Cam-Clay, isothermal vs. non-isothermal) or recalibrate against new lab/field data, and assess how much the predicted response changes.

**7. Long-term / multi-decade forecasting under altered boundary conditions:** Change far-field boundary conditions, in-situ stress state, or injection/production history and project how the reservoir, caprock, or wellbore evolves over years to decades.

**8. Verification and benchmark deviation analysis:** Perturb a validated analytical or semi-analytical case (Sneddon's problem, Kirsch wellbore, KGD/PKN fracture) to quantify how far a numerical configuration can be pushed before it deviates from the known solution.

## Real Questions Users Answer with GEOS

### CO2 Storage and Carbon Sequestration

- If we increase the CO2 injection rate by 50%, does the plume reach the spill point of the storage structure before the project's monitoring period ends?
- What fraction of injected CO2 is trapped by residual and dissolution trapping versus remaining mobile, and how does that ratio change with injection rate or relative permeability hysteresis?
- If an abandoned well intersects the storage formation, how much CO2 or brine leaks through it over the project lifetime, and how sensitive is that leakage to the well's effective permeability?
- How does caprock integrity (computed via induced stress and pore pressure at the caprock) change if the injection pressure is increased to meet a higher throughput target?
- If we switch from an isothermal to a non-isothermal (thermal) model of CO2 injection, how much does the predicted plume shape and pressure buildup change?
- What is the minimum injection well spacing that avoids unacceptable pressure interference between adjacent storage wells?

### Oil & Gas Reservoir Engineering and Multiphase Flow

- If we add an additional injection well at location X, how much does cumulative oil recovery increase compared to the current well pattern?
- How does production decline change if we alter the bottom-hole pressure constraint on existing wells versus the base operating plan?
- If reservoir permeability is actually half of the calibrated estimate, how much does breakthrough time at the producer change?
- What is the impact of coupling the flow solver with wells (rather than using fixed boundary fluxes) on near-wellbore pressure and rate predictions?
- If we change the relative permeability curves used in history matching, which alternative best reproduces observed field pressure and rate data?
- How sensitive is ultimate recovery to the assumed compressibility of the reservoir fluid and rock?

### Hydraulic Fracturing and Stimulation Design

- If we increase the fluid injection rate during a hydraulic fracturing treatment, does the fracture become more toughness-dominated or viscosity-dominated, and how does that change its final length and width?
- How does proppant transport and placement change if the fracturing fluid viscosity is altered, based on slot-test-calibrated proppant transport behavior?
- If two fracture stages are spaced closer together, do the resulting fractures interact or interfere with each other (computed via the fracture-intersection problem)?
- What is the predicted fracture geometry under a KGD versus a penny-shaped (radial) fracture model, and which better matches the field's confinement conditions?
- If in-situ stress anisotropy is higher than assumed, how much does the predicted fracture propagation direction or width deviate from the base case?
- How does total injected fluid volume change the toughness-dominated fracture length compared to the viscosity-dominated regime?

### Wellbore Integrity and Drilling

- If we increase the mud weight (wellbore pressure) during drilling, does the predicted stress concentration around the wellbore (per the Kirsch solution) exceed the rock's failure criterion?
- How does a deviated or horizontal wellbore's stress state differ from a vertical wellbore under the same in-situ stress field?
- If we change the casing and cement design of a cased wellbore, how much does the predicted radial stress transfer to the surrounding rock change?
- What happens to predicted wellbore stability if imperfect (non-bonded) casing-cement-rock interfaces are modeled instead of perfectly bonded ones?
- If a wellbore is subjected to thermal cycling (injection of cold or hot fluid), how does the resulting thermo-elastic or thermo-poro-elastic stress compare to the purely mechanical case?
- How sensitive is predicted near-wellbore plastic yielding to the choice of constitutive model (elastic, Drucker-Prager with hardening, Modified Cam-Clay)?

### Faults, Fractures, and Induced Seismicity

- If pore pressure near a fault increases due to injection, at what pressure does the fault reach its slip (Coulomb failure) threshold?
- How does the stress field along a fault change if two intersecting fractures are present versus a single isolated fracture?
- If a fracture is subjected to shear under compression, how does its frictional sliding behavior change with normal stress, based on the single-fracture-under-shear benchmark?
- What is the induced stress redistribution along a fault following a nearby injection or extraction operation, and how does it compare to the pre-operation stress state?
- If contact stiffness or friction coefficient at a fracture interface is varied, how much does the predicted slip distance or reactivation pressure change?

### Poromechanics, Subsidence, and Compaction

- If reservoir pressure is drawn down by production, how much surface subsidence is predicted, and how does that compare to a scenario with pressure maintenance via injection?
- How does the coupled poromechanical response (pressure and displacement) differ from a flow-only simulation that ignores mechanical compaction?
- If the reservoir transitions from elastic to elasto-plastic behavior under increased effective stress, at what point does the deformation become irreversible?
- What discretization method for the coupled multiphysics solver (e.g., sequential versus fully implicit) changes the predicted pressure-displacement coupling the most?
- If pore pressure and in-situ stress are both elevated simultaneously near a wellbore, how does the combined poro-elasto-plastic response compare to applying each loading independently?

### Thermal and Thermo-Hydro-Mechanical (THM) Coupling

- If injected fluid is significantly colder or hotter than the formation, how far does the thermal front propagate compared to the pressure front over the same time period?
- How does volumetric heat capacity that depends on temperature (rather than being constant) change the predicted thermal diffusion profile around a wellbore?
- If single-phase thermal conductivity is temperature-dependent rather than constant, how much does the predicted temperature distribution deviate from the linear-diffusion base case?
- What is the combined effect of thermal and poroelastic stresses on a cased wellbore subjected to a temperature change, compared to thermal or poroelastic loading alone?
- If imperfect thermal contact is modeled at a cased wellbore's casing-cement-rock interfaces, how does that change predicted temperature and stress profiles compared to assuming perfect thermal bonding?

### Constitutive Model and Calibration Choices

- If we replace a standard Drucker-Prager model with its extended (cap) or viscous variant, how much does predicted plastic strain accumulation change under the same loading path?
- How well does a Modified Cam-Clay model versus a viscoplastic model reproduce triaxial test data for a given rock or soil sample?
- If we add rate dependence (viscoplasticity) to an otherwise rate-independent plasticity model, how does the predicted stress relaxation behavior change over time?
- What is the impact of using a hardening law versus a non-hardening Drucker-Prager model on predicted wellbore breakout angle?

## Who Asks These Questions

- **Reservoir engineers** evaluating well placement, injection/production schedules, and recovery strategies under multiphase flow with wells.
- **CO2 storage and carbon management project teams** assessing plume containment, caprock integrity, and leakage risk through abandoned wells or faults.
- **Hydraulic fracturing and completions engineers** designing stage spacing, fluid systems, and proppant schedules to achieve target fracture geometry.
- **Drilling and wellbore integrity engineers** selecting mud weights, casing/cement designs, and trajectories to avoid wellbore failure.
- **Geomechanics and induced-seismicity specialists** assessing fault reactivation risk and ground deformation from injection or extraction operations.
- **Geothermal developers** evaluating thermal front propagation, THM coupling, and long-term reservoir thermal drawdown.
- **Subsidence and compaction analysts** quantifying surface deformation risk from pressure depletion or injection.
- **Model verification and V&V engineers** comparing GEOS predictions against analytical or semi-analytical benchmarks to qualify the simulator for a given application.
- **R&D and constitutive-modeling researchers** selecting and calibrating material models against laboratory triaxial or relaxation test data.
- **HPC and numerical-methods engineers** evaluating discretization schemes, solver coupling strategies, and mesh choices for computational efficiency and accuracy trade-offs.

The common thread: "If we change this operational, material, or boundary condition, how does the coupled flow, mechanical, thermal, or fracture response evolve — and does it cross a performance, containment, or failure threshold compared to the status quo?" GEOS provides the multiphysics solvers, constitutive-model library, and benchmarked verification cases that let reservoir engineers, drilling teams, geomechanics specialists, and storage-project developers run these physics-based counterfactuals before committing to costly field decisions.
