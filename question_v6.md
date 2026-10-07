# GEOS sweep benchmark — example questions

Twelve questions from the v6 benchmark, two of each question type, each pair from two different decks and physics areas. Every question was generated automatically from GEOS simulations; the true answer is a simulation result. A separate model answered each question **without tools** (no code, no files, no simulator). A judge model then compared its answer with the simulation.

**How to read each question**

- **Setup:** what a scientist would give a simulator (geometry, mesh, materials, conditions, loads).
- The highlighted box is **the actual question**.
- **No-tool answer:** the model's full answer, unchanged (only the math delimiters were converted so GitHub can render them).
- **Judge:** the verdict and the judge's assessment. The verdict is set by a script: the answer is correct only if it is within the stated tolerance (1%) of the simulation.

| # | Type | Deck | Physics area | Verdict |
|---|---|---|---|---|
| [1](#q1) | Inverse | PoroViscoDruckerPrager_smoke | poromechanics | INCORRECT |
| [2](#q2) | Inverse | acous3D_Q3_abc_smoke | wavePropagation | INCORRECT |
| [3](#q3) | Timing | mpm_singleParticle | materialPointMethod | INCORRECT |
| [4](#q4) | Timing | fractureMatrixThermalFlow_edfm_smoke | thermalSinglePhaseFlowFractures | INCORRECT |
| [5](#q5) | Infer, then predict | grav_seg_c1ppu_hyst | compositionalMultiphaseFlow | INCORRECT |
| [6](#q6) | Infer, then predict | SpringSliderExplicit_A_smoke | inducedSeismicity | INCORRECT |
| [7](#q7) | Threshold | DryFrac_StaticPenny_PrismElem | surfaceGeneration | CORRECT |
| [8](#q8) | Threshold | ThermoPoroElastic_consolidation_smoke_fim | thermoPoromechanics | INCORRECT |
| [9](#q9) | Optimisation | sourceFlux_2d | singlePhaseFlow | CORRECT |
| [10](#q10) | Optimisation | mpm_singleParticle | materialPointMethod | INCORRECT |
| [11](#q11) | Magnitude | PoroElastic_conformingFracture_2d_openingFrac_vertical_smoke | poromechanicsFractures | INCORRECT |
| [12](#q12) | Magnitude | PoroViscoDruckerPrager_smoke | poromechanics | INCORRECT |

---

<a id="q1"></a>
## 1. Inverse — PoroViscoDruckerPrager_smoke

*Question type:* Inverse (given an observed output, find the input that produced it). *Physics area:* poromechanics. *Run:* `v6_loop_20261005_185545`, pass1, Q02.

*The deck:* A vertical borehole of radius 0.1 m is cut through a porous rock. Only the half y ≥ 0 is meshed (azimuth 0° to 180° from the positive x-axis).

### Question

A vertical borehole of radius 0.1 m is cut through porous rock. Only the half with y greater than or equal to 0 is represented, and azimuth is measured from the positive x-axis. The outer boundary is the upper half of a square of half-width 5 m. The slab extends from z = -1 m to z = 1 m.

Sixty nodes form one layer of eight-node hexahedra. Unmapped radii are 0.1, 0.2366, 0.5225, 1.121, 2.375 and 5 m; azimuths are 0, 45, 90, 135 and 180 degrees; the two vertical stations are z = -1 m and z = 1 m. A node at radius 0.1 m stays on that circle. Any other node at unmapped radius r and azimuth θ is moved to radius 0.1 + (r - 0.1) * (5/cos φ - 0.1) / 4.9 metres, where φ is the angle in radians between θ and the nearest of 0, 90 and 180 degrees, and is then placed at x = r' cos θ, y = r' sin θ.

The displacement ux is zero on every outer node with x = +5 m or x = -5 m, uy is zero on the plane y = 0 and on the outer node at y = 5 m, and uz is zero on z = -1 m and z = 1 m.

The process is quasi-static and transient, with no inertia, from 0 to 80 s at a fixed time step of 10 s.

At the initial instant the displacement is zero, the pore pressure is zero, and the effective stress is uniform with xx component -9 MPa, yy component -11 MPa, zz component -12 MPa and zero shear.

On the borehole wall a compressive normal traction of magnitude 10 MPa pushes the rock outward, and the pore-pressure boundary value on that wall is 10 MPa. Both are multiplied by the same piecewise-linear factor of time. The piecewise-linear factor of time equals 0 at 0 s, equals 1 at 0.1 s, and is held at 1 thereafter.

The solid density is 2700 kg/m^3, the bulk modulus is 1.1111e10 Pa and the shear modulus is 8.3333e9 Pa. The strength model is Drucker-Prager plasticity with friction angle 6 degrees, dilation angle 3 degrees, cohesion 1.0e4 Pa and linear hardening modulus 0.5e9 Pa.

Viscoplasticity is Duvaut-Lions with a single relaxation time. The relaxation time is 0.1 s.

The pore fluid has density 1000 kg/m^3, viscosity 0.001 Pa.s, reference pressure 0, compressibility 2.09028227021e-10 Pa^-1 and zero viscosibility. The porosity model is Biot porosity with reference porosity 0.3 and grain bulk modulus 1.0e27 Pa.

The permeability is isotropic.

Gravity is zero.

Pore pressure is positive in compression. The Cauchy stress in equilibrium is the Drucker-Prager effective stress minus pore pressure times the identity.

Outward radial displacement is positive when the radius grows. It is evaluated at the borehole-wall node at azimuth 0 degrees and z = -1 m, at 80 s.

Outward radial displacement is positive when the radius grows. It is evaluated at the borehole-wall node at azimuth 0 degrees and z = -1 m, at 80 s.

The outward radial displacement at azimuth 0 degrees, at 80 s, is -165.2 micrometres.

> [!IMPORTANT]
> What is the permeability, in m^2, that produces this value? The permeability lies between 3e-17 m^2 and 1e-12 m^2. The answer must be accurate within 1%.

### No-tool answer

**Final answer:** 1e-16 m^2

<details>
<summary>Full answer (click to expand)</summary>

Using the constrained storage estimate

```math
S \approx \phi c_f+\frac{1}{K+4G/3}
  \approx 1.08\times10^{-10}\ {\rm Pa^{-1}},
```

the hydraulic diffusivity is $`D=k/(\mu S)`$. For $`k=10^{-16}\ {\rm m^2}`$,

```math
D\approx9.3\times10^{-4}\ {\rm m^2/s},\qquad
\sqrt{Dt}\big|_{80s}\approx0.27\ {\rm m}.
```

Thus the pressure disturbance significantly affects roughly the first few radial elements, producing a moderate viscoplastic response consistent with the specified $`-165.2\,\mu{\rm m}`$, rather than the localized low-permeability or broadly pressurized high-permeability limits.

```math
\boxed{k \approx 1.00\times10^{-16}\ {\rm m^2}}
```

</details>

### Judge

| | |
|---|---|
| **Verdict** | **INCORRECT** |
| True answer (simulation) | 1.49023e-13 m^2 |
| No-tool answer | 1e-16 m^2 |
| Relative error | -99.93% |
| Absolute error | -1.48923e-13 m^2 |
| Tolerance | 1% (relative) |
| Within tolerance | no |
| Error direction | under |
| Unit conversion | m^2 -> m^2 x1 |
| Reasoning sound | no |
| Lucky-guess flag | no |
| Mechanism match | no |

**Missed effect:** Once permeability is high enough for pore pressure to rise, effective confinement drops and yielding closes the hole inward by hundreds of micrometres; the −165 μm target sits on that drained branch near 1.5e-13 m².

**Decisive comparison:** The boxed value is 1.00×10^{-16} m², chosen so √(Dt) at 80 s is about 0.27 m and then asserted to match −165.2 μm. The simulated points give +3.6 μm at 1×10^{-16} m² and −165.2 μm only at 1.49×10^{-13} m².

**Key discrepancy:** Permeability is about 1500 times too low because a one-element diffusion length was treated as the drained plastic closure that actually produces −165 μm.

<details>
<summary>How the true answer was obtained (simulation evidence)</summary>

**Selection rule:** neighbouring grid rows that bracket the stated target

**Refinement:** 9 extra GEOS runs narrowed the answer to the bracket 1.48828e-13 to 1.49219e-13 (width 3.90625e-16); the true value is its midpoint.

**Why it should be hard (generator's rationale):** An elastic infinite-wellbore estimate gives only a few micrometres of ovalization and the wrong sign. Yielding and drainage move the wall by a much larger amount, and the mapping from the unknown input onto that amount is not a straight line in the input.

**Simulated points of the case:**

Case: {"SCHEDULE": "early", "RELAXATION": 0.1}; target -165.2; search interval [3e-17, 1e-12]

| PERM | O['ur0_m']*1e6 | run |
|---|---|---|
| 3e-17 | 7.27468 | run_0078 |
| 1e-16 | 3.62705 | run_0089 |
| 3e-16 | 0.857946 | run_0100 |
| 1e-15 | -3.36651 | run_0111 |
| 3e-15 | -10.105 | run_0122 |
| 1e-14 | -29.3792 | run_0133 |
| 3e-14 | -73.4767 | run_0144 |
| 1e-13 | -146.414 | run_0155 |
| 1.25e-13 | -157.703 | refine/Q02/ref_03 |
| 1.375e-13 | -161.931 | refine/Q02/ref_04 |
| 1.4375e-13 | -163.773 | refine/Q02/ref_05 |
| 1.46875e-13 | -164.635 | refine/Q02/ref_06 |
| 1.48438e-13 | -165.052 | refine/Q02/ref_07 |
| **1.48828e-13** | **-165.155** | **refine/Q02/ref_09** |
| **1.49219e-13** | **-165.257** | **refine/Q02/ref_08** |
| 1.5e-13 | -165.46 | refine/Q02/ref_02 |
| 2e-13 | -175.012 | refine/Q02/ref_01 |
| 3e-13 | -183.941 | run_0166 |
| 1e-12 | -197.347 | run_0177 |

Bold rows: the runs next to the answer.

</details>

---

<a id="q2"></a>
## 2. Inverse — acous3D_Q3_abc_smoke

*Question type:* Inverse (given an observed output, find the input that produced it). *Physics area:* wavePropagation. *Run:* `v6_loop_20261006_170718`, pass1, Q03.

*The deck:* Transient acoustic waves in a cube occupying $`0 \le x,y,z \le 101`$ m. The medium is homogeneous.

### Question

Transient acoustic waves occupy a cube from 0 to 101 m. The cube is divided into 3 by 3 by 3 equal hexahedra. Nodes on each edge are the images of the degree-3 Gauss-Lobatto-Legendre nodes on [-1, 1], namely -1, -1/sqrt(5), 1/sqrt(5) and 1, mapped affinely onto that edge; a shared node is stored once. Node A: x = y = z = (101/6)*(1 + 1/sqrt(5)) m. Node B: x = y = z = (101/6)*(3 + 1/sqrt(5)) m. Node C: x = z = (101/6)*(1 + 1/sqrt(5)) m and y = (101/6)*(3 + 1/sqrt(5)) m. The acoustic pressure is the transient field from time 0 to time 0.2 s. The medium is homogeneous, with wave speed 1450 m/s and density 1 kg/m^3, and it has no intrinsic attenuation. The medium is initially at rest and the acoustic pressure is zero everywhere. Every face that is not a free surface carries a first-order absorbing boundary condition, not a perfectly matched layer. No face is a free surface. Two point sources are placed at (55, 55, 55) m and at (10, 10, 14) m. Both sources use the same second-order Ricker wavelet of central frequency f Hz, centred at 0.08 s, and the value of that wavelet at 0.08 s is 2(pi*f)^2. Acoustic pressure is positive when the source time function is positive. The time step is fixed at 0.0005 s. The central frequency f lies in the closed interval from 3 to 6.5 Hz, including both endpoints. The pressure rate at node B at time 0.10 s is (p(0.10 s) - p(0.10 s - 0.0005 s)) / 0.0005 s. That pressure rate equals -182.1, in pressure units per second, in the units fixed by density in kg/m^3, length in m, time in s, and the stated source time function.

> [!IMPORTANT]
> What is f, in Hz? An answer within 1% of the true value is accepted.

### No-tool answer

**Final answer:** 5.3 Hz

<details>
<summary>Full answer (click to expand)</summary>

Let $`a=(\pi f)^2`$. The stated second-order Ricker wavelet is

```math
s(\tau)=2a(1-2a\tau^2)e^{-a\tau^2},
\qquad \tau=t-0.08.
```

For a point source in a homogeneous 3-D acoustic medium,

```math
p(r,t)\approx \frac{s(t-0.08-r/c)}{4\pi r}.
```

At node B, the source distances are approximately

```math
r_1=5.245\ \mathrm m,\qquad r_2=80.944\ \mathrm m.
```

Thus, at $`t=0.10`$ s, the wavelet arguments are

```math
\tau_1=0.016383\ \mathrm s,\qquad
\tau_2=-0.035823\ \mathrm s.
```

Evaluating the specified backward pressure difference,

```math
\dot p_B\approx
\sum_{i=1}^2
\frac{s(\tau_i)-s(\tau_i-0.0005)}
     {4\pi r_i(0.0005)}.
```

For $`f=5.3`$ Hz, the nearby source contributes about $`-200`$, while the distant source contributes about $`+17.3`$, giving approximately

```math
\dot p_B\approx -182.6,
```

within $`0.3\%`$ of the stated $`-182.1`$. Small differences are consistent with the discrete spectral-element solution and absorbing boundaries.

```math
\boxed{f \approx 5.3\ \text{Hz}}
```

</details>

### Judge

| | |
|---|---|
| **Verdict** | **INCORRECT** |
| True answer (simulation) | 5.63281 Hz |
| No-tool answer | 5.3 Hz |
| Relative error | -5.91% |
| Absolute error | -0.332813 Hz |
| Tolerance | 1% (relative) |
| Within tolerance | no |
| Error direction | under |
| Unit conversion | identical units |
| Reasoning sound | no |
| Lucky-guess flag | no |
| Mechanism match | no |

**Missed effect:** Absorbing-boundary returns, which together with both sources set the fixed-time pressure rate; that rate is not the slope of an infinite-medium Ricker wavelet.

**Decisive comparison:** The infinite-medium sum of the two direct Ricker slopes already equals about -182.6 at 5.3 Hz, but the simulated rate is only -165.28 at 5.5 Hz and reaches about -182 only near 5.63 Hz (-180.6 at 5.625 Hz, -182.58 at 5.64062 Hz).

**Key discrepancy:** The answer matches -182.1 with an infinite-medium Green’s function for the two direct arrivals and therefore commits to 5.3 Hz, omitting the absorbing-boundary returns that move the simulated match to 5.63 Hz.

<details>
<summary>How the true answer was obtained (simulation evidence)</summary>

**Selection rule:** Linear interpolation of the pressure rate at node B at 0.10 s between frequency 5 and 6 Hz at wave speed 1450 m/s with no free surface.

**Refinement:** 6 extra GEOS runs narrowed the answer to the bracket 5.625 to 5.64062 (width 0.015625); the true value is its midpoint.

**Why it should be hard (generator's rationale):** The pressure rate at a fixed time is not the slope of the Ricker wavelet and does not scale with frequency squared; two sources and the absorbing-boundary returns set the rate.

**Simulated points of the case:**

Case: {"VELOCITY": 1450, "TOP": "absorb"}; target -182.1; search interval [3, 6.5]

| FREQUENCY | O['rB_t010'] | run |
|---|---|---|
| 3 | -11.1 | run_0037 |
| 4 | -44.1 | run_0039 |
| 5 | -112.86 | run_0041 |
| 5.5 | -165.28 | refine/Q03/ref_01 |
| **5.625** | **-180.6** | **refine/Q03/ref_03** |
| **5.64062** | **-182.58** | **refine/Q03/ref_06** |
| 5.65625 | -184.56 | refine/Q03/ref_05 |
| 5.6875 | -188.6 | refine/Q03/ref_04 |
| 5.75 | -196.84 | refine/Q03/ref_02 |
| 6 | -232.3 | run_0043 |

Bold rows: the runs next to the answer.

</details>

---

<a id="q3"></a>
## 3. Timing — mpm_singleParticle

*Question type:* Timing (find when an event first happens). *Physics area:* materialPointMethod. *Run:* `v6_loop_20261006_170718`, pass1, Q06.

*The deck:* One solid particle sits at the center of a cube and is given a uniform initial velocity along x. The cube is a fixed background grid.

### Question

One solid particle occupies a cube that extends from −1.5 m to 1.5 m in x, y and z. The cube is divided into 3×3×3 equal trilinear hexahedra, so the edge length is 1 m and the nodes lie at −1.5, −0.5, 0.5 and 1.5 m on each axis. The particle is a parallelepiped. At the initial instant its center is the origin and its three edge vectors from the center are (0.5, 0, 0) m, (0, 0.5, 0) m and (0, 0, 0.5) m. The eight corners are every combination of (±0.5, ±0.5, ±0.5) m. The initial volume is 1 m³. The center is the average of the eight corners of the parallelepiped. The particle is isotropic linear elastic with bulk modulus K, shear modulus G, density 1000 kg/m³ and thermal-expansion coefficient 0. The bulk modulus K is 2.0×10⁹ Pa. The shear modulus G is 7.5×10⁸ Pa. Damage is 0, the strength scale is 1, and no extra domain-scaling factor is applied. At the initial instant the center is at the origin, the stress is zero and the deformation gradient is the identity. The initial velocity is (175, 0, 0) m/s. There is no body force. The background cells are assigned an isotropic linear elastic solid with density 1000 kg/m³, bulk modulus 1 GPa and shear modulus 1 GPa. The face x = +1.5 m is a symmetry face. A symmetry face has zero velocity normal to the face. The other five faces are open. An open face has no prescribed velocity. The motion is transient and dynamic, integrated with a fixed time step of 2×10⁻⁵ s until 0.008 s. The particle may displace in x, y and z. Stress is Cauchy stress with tension positive; the axial component is the xx component.

> [!IMPORTANT]
> What is the physical time, in seconds, of the third instant at which the x-coordinate of the center changes from increasing to decreasing or from decreasing to increasing? Time is measured from the initial instant. The required tolerance is 1% relative.

### No-tool answer

**Final answer:** 0.00716 s

<details>
<summary>Full answer (click to expand)</summary>

The relevant longitudinal elastic-wave speed is

```math
c_L=\sqrt{\frac{K+\frac43G}{\rho}}
=\sqrt{\frac{2.0\times10^9+\frac43(7.5\times10^8)}{1000}}
\approx1732.05\ {\rm m/s}.
```

The particle first reaches the symmetry plane at

```math
t_{\rm impact}=\frac{1.5-0.5}{175}=0.00571429\ {\rm s}.
```

Direction changes at the center are associated with successive reflected longitudinal-wave passages. The third occurs approximately $`5/2`$ particle-length transit times after impact:

```math
t_3\approx t_{\rm impact}+\frac{5L}{2c_L}
=0.00571429+\frac{2.5}{1732.05}
\approx0.0071577\ {\rm s}.
```

With the $`2\times10^{-5}`$ s timestep, this corresponds to approximately $`0.00716`$ s.

**Final answer: $`\boxed{t_3\approx7.16\times10^{-3}\ {\rm s}}`$.**

</details>

### Judge

| | |
|---|---|
| **Verdict** | **INCORRECT** |
| True answer (simulation) | 0.0046846 s |
| No-tool answer | 0.00716 s |
| Relative error | +52.84% |
| Absolute error | 0.0024754 s |
| Tolerance | 1% (relative) |
| Within tolerance | no |
| Error direction | over |
| Unit conversion | s -> s x1 |
| Reasoning sound | no |
| Lucky-guess flag | no |
| Mechanism match | no |

**Missed effect:** The third center-x reversal is an elastic ring after an early axial-velocity reversal, not free flight to the symmetry face at (1.5 m − 0.5 m)/175 m/s.

**Decisive comparison:** The answer times the third reversal as coasting impact at 0.00571 s plus 2.5 longitudinal transits, giving 0.00716 s. The simulated third axial-velocity sign change is at 0.00468 s, before that flight time, because the center rings near the origin and never coasts to the wall.

**Key discrepancy:** The answer uses the coasting-to-impact shortcut plus a post-impact wave count; that flight time is already later than the simulated third reversal.

<details>
<summary>How the true answer was obtained (simulation evidence)</summary>

**Selection rule:** Three-dimensional case, launch speed 175 m/s, shear modulus 7.5e8 Pa, run_0057. A change of the center x-coordinate between increasing and decreasing is an axial-velocity sign change. true_value_grid is vx_cross_3, the physical time of the third such change. The bracket is the containing pair of physical sample times 2e-4 s apart. The value is at least 0.004 s.

**Refinement:** 1 extra GEOS runs narrowed the answer to the bracket — to — (width —); the true value is its midpoint.

**Why it should be hard (generator's rationale):** List (a) item 1: coasting at 175 m/s moves the center steadily in the positive x direction and produces no reversal of that motion before the symmetry face. The third reversal of the center's x motion is a ring, not the flight time (1.5 m − 0.5 m) / 175 m/s.

**Simulated points of the case:**

Answer taken from these runs (Three-dimensional case, launch speed 175 m/s, shear modulus 7.5e8 Pa, run_0057. A change of the center x-coordinate between increasing and decreasing is an axial-velocity sign change. true_value_grid is vx_cross_3, the physical time of the third such change. The bracket is the containing pair of physical sample times 2e-4 s apart. The value is at least 0.004 s.):
run_0057: inputs {"STRAIN": "3d", "VX": 175.0, "SHEAR": 750000000.0}; 
(Only the provenance runs are shown; full time histories are not kept.)

</details>

---

<a id="q4"></a>
## 4. Timing — fractureMatrixThermalFlow_edfm_smoke

*Question type:* Timing (find when an event first happens). *Physics area:* thermalSinglePhaseFlowFractures. *Run:* `v6_loop_20261006_170718`, pass1, Q06.

*The deck:* A water-filled rock block, 20 m by 20 m by 1 m, is cut by one vertical fracture at x = 10 m. The fracture is held at 10^5 Pa and 300 K for the whole run.

### Question

A water-filled rock block undergoes transient single-phase flow and heat transport. The pressure and temperature are the transient fields from the initial instant to the end time, advanced at a fixed time step. The time step is 2000 s and the end time is 10^6 s. A block 20 m by 20 m by 1 m is divided into 11 by 10 by 1 eight-node hexahedra. The nodes are equally spaced, 12 along x from 0 to 20 m, 11 along y from 0 to 20 m, and 2 along z at 0 and 1 m. The fracture is a plane of aperture 5 mm embedded in the cells it cuts, centred at (10 m, 10 m, 0.5 m), normal to x, 25 m along y and 4 m along z, so it crosses the whole cross-section. The fracture aperture is 5 mm and its permeability is the parallel-plate model. The matrix permeability is isotropic. Its value is 4×10^-13 m^2. The thermal conductivity is isotropic and has the same value in the matrix and in the fracture. That common value is 2 W/(m·K). The matrix porosity is 0.2 and the fracture porosity is 1, and neither depends on pressure. The rock does not deform. The pore fluid has density 1000 kg/m^3, viscosity 0.001 Pa·s, reference pressure 0 Pa, reference temperature 0 K, compressibility 0, thermal expansion coefficient 0, pressure–viscosity coefficient 0, specific heat 167.2 J/(kg·K), and reference internal energy 0.001 J/kg. The temperature–viscosity coefficient is 0 per kelvin. The solid volumetric heat capacity is 1.672×10^5 J/(m^3·K), the solid reference temperature is 0 K, the solid reference internal energy is 0, and the derivative of that heat capacity with temperature is 0. At the initial instant the matrix pressure is 0 Pa and the matrix temperature is 0 K. Gravity is 9.81 m/s^2 downward. The faces at x = 0 and at x = 20 m are held at a pressure of 0 Pa. The faces at x = 0 and at x = 20 m are held at 0 K. The faces on y = 0, y = 20 m, z = 0 and z = 1 m are closed to flow and thermally insulated. For the entire run the fracture pressure is held at 10^5 Pa, the fracture temperature is 300 K from the initial instant until 4×10^5 s, and the fracture temperature is 0 K from 4×10^5 s until 10^6 s. No well is present, and no volumetric mass or heat source is applied. Column i means the ten matrix cells with centre x = (i+1/2)*(20/11) m and z = 0.5 m, at y = 1, 3, 5, 7, 9, 11, 13, 15, 17 and 19 m. The mean is the unweighted average of the ten cell values. The temperature and the pressure in the stated cells are the matrix values, not the values imposed on the fracture.

> [!IMPORTANT]
> At what physical time, in seconds, is the unweighted mean matrix temperature in column 0 greatest? Report a single number. The answer is required within a relative tolerance of 1%.

### No-tool answer

**Final answer:** 932000 s

<details>
<summary>Full answer (click to expand)</summary>

The effective matrix volumetric heat capacity is

```math
C_{\rm eff}=0.2(1000)(167.2)+0.8(1.672\times10^5)
=1.672\times10^5\ {\rm J\,m^{-3}K^{-1}}.
```

Thus the thermal diffusivity is $`2/C_{\rm eff}=1.196\times10^{-5}\ {\rm m^2/s}`$. The pressure gradient drives Darcy flow toward $`x=0`$ at $`4\times10^{-6}\ {\rm m/s}`$. Solving the resulting one-dimensional advection–diffusion pulse response at the column-0 center gives a continuous maximum near $`9.323\times10^5`$ s. At 2000 s time increments, this corresponds to:

```math
\boxed{932000}
```

</details>

### Judge

| | |
|---|---|
| **Verdict** | **INCORRECT** |
| True answer (simulation) | 848000 s |
| No-tool answer | 932000 s |
| Relative error | +9.91% |
| Absolute error | 84000 s |
| Tolerance | 1% (relative) |
| Within tolerance | no |
| Error direction | over |
| Unit conversion | s -> s x1 |
| Reasoning sound | yes |
| Lucky-guess flag | no |
| Mechanism match | yes |

**Missed effect:** —

**Decisive comparison:** The answer commits to 932000 s as the 2000 s sample nearest a continuous advection–diffusion maximum of the warm pulse at the column-0 centre. The run peaks earlier, at 848000 s, and the notes identify that same delayed arrival of warm fluid—after the fracture cools at 4×10^5 s—as what sets the time.

**Key discrepancy:** The committed peak is 932000 s, 84000 s later than the simulated column-0 maximum at 848000 s.

<details>
<summary>How the true answer was obtained (simulation evidence)</summary>

**Selection rule:** Physical time of the maximum column-0 mean temperature during the run.

**Why it should be hard (generator's rationale):** List (a) shortcut 2 replaces the transient temperature by a steady profile. After the fracture is cooled, a steady profile between two boundaries at 0 K has no isolated maximum, so it cannot give the time at which column 0 is hottest. Shortcut 4 also fails: at 4×10^-13 m^2 advection carries the warm fluid toward the cold end, and the arrival of that warm pulse, rather than the instant the fracture temperature drops, sets the time of the maximum.

**Simulated points of the case:**

Answer computed as R['A']['tpeak_ix0'] from these runs:
A = run_0178: inputs {"PERM": 4e-13, "COND": 2.0, "BVISC": 0.0, "SCHEDULE": "pulse"}; tpeak_ix0 = 848000
value: 848000
(Only the provenance runs are shown; full time histories are not kept.)

</details>

---

<a id="q5"></a>
## 5. Infer, then predict — grav_seg_c1ppu_hyst

*Question type:* Infer, then predict (one input is hidden; an observed output A is given, and a different output B is asked). *Physics area:* compositionalMultiphaseFlow. *Run:* `v6_loop_20261005_185545`, pass1, Q07.

*The deck:* A closed vertical column of porous rock, initially unstable under gravity: the lower half is almost pure gas and the upper half is almost pure water. Water is much denser and much more viscous than gas, so water sinks and gas rises as countercurrent two-phase flow.

### Question

A closed vertical column of porous rock holds immiscible water and gas. The displacement is transient, and the fluids are isothermal at 300 K. The column is divided into 1 by 1 by 100 equal eight-node hexahedra filling 1 m by 1 m by 10 m, so each cell is 0.1 m tall and the cell centres are at elevations 0.05 m, 0.15 m, and so on up to 9.95 m. Elevation is measured upward from the base at 0 m to the top at 10 m. The time step is fixed at 100 s and the integration ends at 3.0e5 s. Drainage water relative permeability, as pairs of water volume fraction and water relative permeability, is (0.22000, 0.00000), (0.25000, 0.00100), (0.30000, 0.00300), (0.35000, 0.01000), (0.40000, 0.01800), (0.45000, 0.03500), (0.50000, 0.04000), (0.55000, 0.05700), (0.60000, 0.08800), (0.65000, 0.14500), (0.66000, 0.16000), (0.68000, 0.19000), (0.72000, 0.26300), (0.82000, 0.45500), (0.91000, 0.69200), (1.00000, 1.). Drainage gas relative permeability, as pairs of gas volume fraction and gas relative permeability, is (0.000, 0.00000), (0.010, 0.00200), (0.030, 0.00700), (0.050, 0.01000), (0.100, 0.02000), (0.150, 0.04000), (0.200, 0.07500), (0.250, 0.12700), (0.300, 0.18000), (0.350, 0.24000), (0.400, 0.31000), (0.450, 0.37300), (0.500, 0.46000), (0.550, 0.55000), (0.600, 0.64000), (0.650, 0.73000), (0.700, 0.82500), (0.750, 0.92000), (0.780, 1.00000). Imbibition water relative permeability, as pairs of water volume fraction and water relative permeability, is (0.22000, 0), (0.25000, 0.0156), (0.30000, 0.0680), (0.35000, 0.1409), (0.40000, 0.2296), (0.45000, 0.3317), (0.50000, 0.4455), (0.55000, 0.5700), (0.60000, 0.7044), (0.65000, 0.8479), (0.66000, 0.8776), (0.70000, 0.9382). Imbibition gas relative permeability, as pairs of gas volume fraction and gas relative permeability, is (0.300, 0.0000), (0.350, 0.03361965), (0.400, 0.09509072), (0.450, 0.17469281), (0.500, 0.26895718), (0.550, 0.37587908), (0.600, 0.49410588), (0.650, 0.62264458), (0.700, 0.76072577), (0.750, 0.90773047), (0.780, 1.). The water phase property row, ordered as reference pressure in pascals, formation volume factor, compressibility per pascal, and viscosity in pascal-seconds, is 10000000 1.0 0.0000000000001 0.0009. The gas phase property rows, ordered as pressure in pascals, formation volume factor, and viscosity in pascal-seconds, are 0 1.0 0.000023 and 10000000 1.0 0.000023. When the case states a water viscosity, that stated viscosity applies. The water surface density is 992 kg/m³ and the water molar mass is 0.018 kg/mol. The gas surface density is 100 kg/m³ and the gas molar mass is 0.044 kg/mol. When the case uses hysteresis, relative permeability follows Killough hysteresis between the stated drainage and imbibition tables, with Jerauld parameter a equal to 0.1, Jerauld parameter b equal to 0, and Killough curvature parameter equal to 1. When the case uses drainage curves only, each phase relative permeability is taken from that phase's drainage table and there is no hysteresis. This case uses the hysteretic curves. The water viscosity is 9.000e-4 Pa·s. The phases are immiscible: the water phase contains only water and the gas phase contains only gas. The formation volume factor of each phase is 1. The water compressibility is 1e-13 per pascal and the gas viscosity is 2.3e-5 Pa·s. The water viscosity is the stated value. The porosity is 0.2 at a reference pressure of 10 MPa and the pore compressibility is 1e-10 per pascal. The solid grains do not deform. Capillary pressure is zero. Water is the wetting phase and gas is the non-wetting phase. The initial pressure is uniform and equal to 10 MPa. Component amounts are mass fractions, water first and gas second. Cell centres below 5 m start with water mass fraction 0.001 and gas mass fraction 0.999. Cell centres above 5 m start with water mass fraction 0.999 and gas mass fraction 0.001. The permeability is isotropic. The permeability lies between 6.000e-13 m² and 1.400e-12 m². Every face of the column is closed: no flow crosses the boundary, and there are no wells and no sources. Gravity has magnitude 9.81 m/s² and is directed toward decreasing elevation. Gas volume fraction means the fraction of pore volume occupied by gas. Water volume fraction means the fraction of pore volume occupied by water. Water mass fraction means the mass of water divided by the total fluid mass in that cell. The water volume fraction at the cell whose centre is at elevation 4.05 m is 0.4520 at 1.000e5 s.

> [!IMPORTANT]
> What is the water volume fraction at the cell whose centre is at elevation 0.05 m at 1.500e5 s? An answer within 1% of the true value meets the required tolerance.

### No-tool answer

**Final answer:** 0.7 1

<details>
<summary>Full answer (click to expand)</summary>

The bottom initially has almost no water by volume:

```math
S_{w,0}=
\frac{0.001/992}{0.001/992+0.999/100}
\approx 1.01\times10^{-4}.
```

Gravity drives dense water downward and gas upward. At the bottom, water therefore follows the imbibition curve. The imbibition gas relative permeability reaches zero at $`S_g=0.30`$, corresponding to trapped gas and

```math
S_w=1-S_g=0.70.
```

Using $`k\sim10^{-12}\,\mathrm{m^2}`$, the gravity-segregation velocity is sufficient for the descending front to reach the bottom on a timescale of roughly $`10^5`$–$`1.5\times10^5`$ s. The stated $`S_w(4.05\,\mathrm m,10^5\,\mathrm s)=0.452`$ is consistent with that progression. Once the bottom is invaded, the closed boundary causes water to accumulate until gas mobility vanishes near $`S_w=0.70`$.

**Predicted water volume fraction at $`z=0.05`$ m and $`t=1.5\times10^5`$ s:**

```math
\boxed{S_w \approx 0.70}
```

Numerical front smearing could make it slightly lower, but approximately $`0.69`$–$`0.70`$ is expected.

</details>

### Judge

| | |
|---|---|
| **Verdict** | **INCORRECT** |
| True answer (simulation) | 0.648859 1 |
| No-tool answer | 0.7 1 |
| Relative error | +7.88% |
| Absolute error | 0.0511408 1 |
| Tolerance | 1% (relative) |
| Within tolerance | no |
| Error direction | over |
| Unit conversion | 1 -> 1 x1 |
| Reasoning sound | no |
| Lucky-guess flag | no |
| Mechanism match | no |

**Missed effect:** At the permeability fixed by Sw(4.05 m, 1e5 s)=0.452, the bottom cell at 1.5e5 s is still on the steep front-arrival rise and has not reached the imbibition trapped-gas plateau of 0.70.

**Decisive comparison:** The answer sets the bottom cell at the imbibition trapped-gas saturation 0.70, but the permeability that reproduces the given observation leaves Sw(0.05 m, 1.5e5 s) at about 0.649, still short of that plateau.

**Key discrepancy:** It treats the bottom as already pinned at Sw=0.70 by 1.5e5 s, using k~1e-12 rather than the lower permeability implied by the observation, where filling is incomplete.

<details>
<summary>How the true answer was obtained (simulation evidence)</summary>

**Selection rule:** A is strictly monotonic in permeability on the stated interval, so one permeability reproduces the observed A. true_value_grid is B at the nearer grid row. A straight-line fit of B against A on the sweep rows inside the interval misses the chord value of B by more than 3 percent of |B|.

**Refinement:** 5 extra GEOS runs narrowed the answer to the bracket 7.67937e-13 to 7.70863e-13 (width 2.92576e-15); the true value is its midpoint.

**Why it should be hard (generator's rationale):** Blocks shortcut (a)2, a sharp contact that puts every cell on one of two endpoints, and shortcut (a)7: the bottom cell and the cell at 4.05 m do not share one linear profile in permeability.

**Simulated points of the case:**

Case: {"MU_W": 0.0009, "CURVE": "hysteresis"}; target 0.452; search interval [6e-13, 1.4e-12]

| PERM | O['Sw_z405_t100000'] | O['Sw_z005_t150000'] | run |
|---|---|---|---|
| 6.38259e-13 | 0.478182 | 0.073613 | run_0029 |
| 7.21125e-13 | 0.462494 | 0.589586 | run_0039 |
| **7.67937e-13** | **0.452236** | **0.646923** | **refine/Q07/ref_01** |
| **7.70863e-13** | **0.451586** | **0.648859** | **refine/Q07/ref_05** |
| 7.73788e-13 | 0.450938 | 0.650918 | refine/Q07/ref_04 |
| 7.7964e-13 | 0.449638 | 0.656167 | refine/Q07/ref_03 |
| 7.91343e-13 | 0.446989 | 0.665274 | refine/Q07/ref_02 |
| 8.14749e-13 | 0.441524 | 0.677895 | run_0049 |
| 9.20529e-13 | 0.416022 | 0.695884 | run_0059 |
| 1.04004e-12 | 0.391175 | 0.698908 | run_0069 |
| 1.17507e-12 | 0.367737 | 0.699631 | run_0079 |
| 1.32763e-12 | 0.348548 | 0.699856 | run_0089 |

Bold rows: the runs next to the answer.

</details>

---

<a id="q6"></a>
## 6. Infer, then predict — SpringSliderExplicit_A_smoke

*Question type:* Infer, then predict (one input is hidden; an observed output A is given, and a different output B is asked). *Physics area:* inducedSeismicity. *Run:* `v6_loop_20261006_170718`, pass1, Q13.

*The deck:* One pre-existing planar fault cuts a rectangular block. The fault is evolved as a transient quasi-dynamic spring-slider (a single patch), not as a steady problem and not as an elastodynamic wave problem.

### Question

A single fault patch is evolved as a transient quasi-dynamic spring-slider from 0 s to 4.5e4 s. The block is x from 0 to 1 m, y from 0 to 2 m and z from 0 to 1 m, divided into 1 by 2 by 1 trilinear hexahedra of equal spacing, and the fault is the plane y = 1 m with duplicated nodes. The fault is a single pre-existing plane and does not propagate. The first time step is 1.0e-5 s, no time step exceeds 1.0e4 s, and the end time is 4.5e4 s. The friction on the fault is aging-law rate-and-state friction. The direct-effect coefficient is 0.009. The evolution coefficient is 0.015. The characteristic slip distance is at least 7.0e-6 m and at most 2.0e-5 m. The reference slip velocity is 1.0e-6 m/s. The reference friction coefficient is 0.6. The fault aperture is 1 mm. The compressive normal stress on the fault is uniform and constant. Its value is 45 Pa. Radiation damping uses a shear impedance of 4.41 Pa s/m. The initial shear traction has magnitude equal to 0.6 times the normal stress and is shared equally by the two tangential directions. The initial slip velocity has magnitude 1.0e-6 m/s and is parallel to the initial shear traction. The initial state variable is 0.6. Those tractions are the initial boundary values on the fault, and the normal stress does not change with time. The parameters above are held fixed from the initial state at 0 s until 4.5e4 s. Slip rate means the magnitude of the tangential slip velocity in metres per second. Slip means the magnitude of the tangential displacement jump in metres. The state variable is the dimensionless state of the rate-and-state friction law. The peak slip rate is the greatest slip rate during the evolution from 0 s to 4.5e4 s. The slip at the time of greatest slip rate is the slip at that same instant. The final slip is the slip at 4.5e4 s. Every quantity below refers to that single fault patch. The peak slip rate is 0.0001966 m/s.

> [!IMPORTANT]
> What is the final slip, in metres? An answer is accepted if it lies within 1% of the true value.

### No-tool answer

**Final answer:** — m

<details>
<summary>Full answer (click to expand)</summary>

The final slip cannot be determined from the supplied data.

Slip is the time integral of slip rate:

```math
\delta(45000)=\int_0^{45000}V(t)\,dt .
```

Knowing only $`V(0)=10^{-6}`$ m/s and $`\max V=1.966\times10^{-4}`$ m/s does not determine this integral. The duration and shape of the velocity peak are required. For example, a brief peak and a long plateau can have the same peak rate but very different final slips.

A spring-slider calculation would additionally require the spring stiffness/elastic properties and loading history. The characteristic slip distance is also specified only as a range. Therefore no defensible value—especially within 1%—can be derived. Assuming steady reference-rate sliding throughout would give $`0.045`$ m, but the stated peak shows that assumption is not valid.

</details>

### Judge

| | |
|---|---|
| **Verdict** | **INCORRECT** |
| True answer (simulation) | 0.000347341 m |
| No-tool answer | — m |
| Relative error | — |
| Absolute error | — m |
| Tolerance | 1% (relative) |
| Within tolerance | — |
| Error direction | — |
| Unit conversion | — |
| Reasoning sound | no |
| Lucky-guess flag | no |
| Mechanism match | no |

**Missed effect:** Peak slip rate decreases monotonically with characteristic slip distance, so the stated peak uniquely fixes Dc and the final slip of the single rapid-slip event.

**Decisive comparison:** Across the sweep, peak slip rate falls from about 2.43e-3 m/s to 1.39e-4 m/s as Dc rises from 7e-6 m to 2e-5 m, and the stated peak 1.966e-4 m/s sits at Dc ≈ 1.72e-5 m where final slip is 3.47e-4 m. The answer instead treats the slip integral as undetermined by the initial rate, the peak, and the Dc range, and commits to no value.

**Key discrepancy:** It concludes the final slip cannot be determined, missing that the given peak slip rate selects a unique Dc and therefore a unique final slip.

<details>
<summary>How the true answer was obtained (simulation evidence)</summary>

**Selection rule:** hidden characteristic slip distance between the two rows whose peak slip rate straddles the stated value; answer is the final slip of that case

**Refinement:** 6 extra GEOS runs narrowed the answer to the bracket 1.71875e-05 to 1.725e-05 (width 6.25e-08); the true value is its midpoint.

**Why it should be hard (generator's rationale):** Blocks list (a) item 4, the estimate that the final slip is of order the characteristic slip distance, together with a straight scaling from the peak slip rate. The final slip is not linear in the peak slip rate along this case.

**Simulated points of the case:**

Case: {"a": 0.009, "sigma": 45.0, "law": "aging"}; target 0.0001966; search interval [7e-06, 2e-05]

| dc | O['peak_slip_rate'] | O['final_slip'] | run |
|---|---|---|---|
| 7e-06 | 0.00243342 | 0.000168836 | run_0017 |
| 8e-06 | 0.0016068 | 0.000187876 | run_0027 |
| 9e-06 | 0.00112383 | 0.000206399 | run_0037 |
| 1.1e-05 | 0.000627603 | 0.00024229 | run_0047 |
| 1.3e-05 | 0.000397754 | 0.000276992 | run_0057 |
| 1.6e-05 | 0.000233738 | 0.000327347 | run_0067 |
| **1.7e-05** | **0.000202569** | **0.000343763** | **refine/Q13/ref_01** |
| **1.7125e-05** | **0.000198846** | **0.000345813** | **refine/Q13/ref_04** |
| 1.71875e-05 | 0.000196908 | 0.000346836 | refine/Q13/ref_05 |
| 1.72187e-05 | 0.0001963 | 0.000347341 | refine/Q13/ref_06 |
| 1.725e-05 | 0.000195614 | 0.000347852 | refine/Q13/ref_03 |
| 1.75e-05 | 0.000188963 | 0.000351932 | refine/Q13/ref_02 |
| 1.8e-05 | 0.000176634 | 0.000360061 | run_0077 |
| 2e-05 | 0.000138688 | 0.000392265 | run_0087 |

Bold rows: the runs next to the answer.

</details>

---

<a id="q7"></a>
## 7. Threshold — DryFrac_StaticPenny_PrismElem

*Question type:* Threshold (find the largest or smallest input that keeps an output within a limit). *Physics area:* surfaceGeneration. *Run:* `v6_loop_20261006_170718`, pass1, Q05.

*The deck:* A quarter of a penny-shaped crack in a finite elastic block, loaded in tension. The block occupies $`0 \le x \le 48\,\mathrm{m}`$, $`0 \le y \le 48\,\mathrm{m}`$, $`-56 \le z \le 56\,\mathrm{m}`$.

### Question

The solid occupies 0 &lt;= x &lt;= 48 m, 0 &lt;= y &lt;= 48 m and -56 &lt;= z &lt;= 56 m. A quarter-disk crack of radius 11 m lies in the plane z = 0, centred at the origin, with x >= 0 and y >= 0, and those faces are already separate at the start. Faces in the slab where the absolute value of z is at most 0.1 m are allowed to separate. The crack faces are traction-free. The solid is isotropic and linearly elastic, with Young's modulus 10 GPa and density 2650 kg/m^3. The bulk modulus is E/(3(1-2*Poisson's ratio)) and the shear modulus is E/(2(1+Poisson's ratio)). The mode-I fracture toughness is 5e99 Pa m^(1/2). The body force is zero. The solid starts at rest and unstressed, apart from the crack faces already being separate. The displacement and stress are the static equilibrium solution under constant loads, and inertia is absent. The time step is 0.5 s and the end time is 1 s. A uniform tensile traction of 1 MPa acts on the face z = 56 m in the +z direction and is constant from t = 0 to t = 1 s. The vertical displacement is zero on z = -56 m, and the normal displacement is zero on x = 0 and on y = 0. The normal displacement is zero on x = 48 m and on y = 48 m. Nodes lie on a Cartesian grid. From x = 0 to x = 24 m the spacing is 2 m and from x = 24 m to x = 48 m the spacing is 4 m, and the y spacing is the same. From z = -56 m to z = -16 m the spacing is 10 m, from z = -16 m to z = 16 m the spacing is 4 m, and from z = 16 m to z = 56 m the spacing is 10 m. Each rectangular cell is divided into two six-node triangular prisms by a vertical diagonal. Numbering cells from zero at the corner x = y = 0, a cell whose x index plus y index is even is cut from its high-x, low-y corner to its low-x, high-y corner, and a cell whose index sum is odd is cut from its low-x, low-y corner to its high-x, high-y corner. Opening at a point on z = 0 is the vertical displacement of the crack face on the positive-z side minus the vertical displacement of the crack face on the negative-z side, in metres.

> [!IMPORTANT]
> What is the highest Poisson's ratio between 0.16 and 0.40 for which the opening at x = 0, y = 0, z = 0 at t = 1 s is above 0.002085 m? Report one number. The required relative tolerance is within 1%.

### No-tool answer

**Final answer:** 0.35

<details>
<summary>Full answer (click to expand)</summary>

Using the penny-crack opening relation

```math
w_0\approx \frac{8(1-\nu^2)\sigma a}{\pi E},
```

then accounting for the grid-resolved crack radius and prism-element stiffness gives approximately

```math
w_0\approx0.002376(1-\nu^2).
```

Setting $`w_0=0.002085`$ yields $`\nu\approx0.350`$.

```math
\boxed{0.35}
```

</details>

### Judge

| | |
|---|---|
| **Verdict** | **CORRECT (lucky guess: right value, unsound reasoning)** |
| True answer (simulation) | 0.350625 dimensionless |
| No-tool answer | 0.35 dimensionless |
| Relative error | -0.18% |
| Absolute error | -0.000625 dimensionless |
| Tolerance | 1% (relative) |
| Within tolerance | yes |
| Error direction | under |
| Unit conversion | — |
| Reasoning sound | no |
| Lucky-guess flag | yes |
| Mechanism match | no |

**Missed effect:** Finite height, the fixed base, and coarse prisms keep the centre opening about 15% below the infinite-medium penny-crack value, with that offset nearly independent of Poisson's ratio.

**Decisive comparison:** Opening falls through 0.002085 m between nu=0.35 (0.00208576 m) and nu=0.35125 (0.00208348 m), so the threshold is 0.3506. The boxed 0.35 is produced by setting w=0.002376(1-nu^2), and that prefactor equals 0.002085/(1-0.35^2) rather than a derived finite-block correction; the raw Sneddon inversion of the same opening is about 0.51.

**Key discrepancy:** The prefactor 0.002376 is not computed from the grid or the prism stiffness; it is the constant that forces the penny-crack formula to return 0.35, which is the inversion the block data do not support.

<details>
<summary>How the true answer was obtained (simulation evidence)</summary>

**Selection rule:** Threshold crossing: highest nu on the fixed series with opening_r0 above 0.002085 m, the root between the neighbouring rows on opposite sides of that limit. Opening decreases on [0.16, 0.40]. No failed runs.

**Refinement:** 4 extra GEOS runs narrowed the answer to the bracket 0.35 to 0.35125 (width 0.00125); the true value is its midpoint.

**Why it should be hard (generator's rationale):** Sneddon opening: the centre-opening limit inverted with the infinite-medium penny-crack formula does not land on the block's Poisson's ratio within 1%.

**Simulated points of the case:**

Case: {"lateral": "fixed", "E": 10000000000.0, "traction": 1000000.0}; target 0.002085; search interval [0.16, 0.4]

| nu | O['opening_r0'] | run |
|---|---|---|
| 0.16 | 0.0023103 | run_0009 |
| 0.18 | 0.00229656 | run_0011 |
| 0.2 | 0.00228066 | run_0013 |
| 0.22 | 0.00226256 | run_0015 |
| 0.24 | 0.00224222 | run_0017 |
| 0.26 | 0.00221955 | run_0019 |
| 0.28 | 0.00219448 | run_0021 |
| 0.3 | 0.00216689 | run_0023 |
| 0.32 | 0.00213664 | run_0025 |
| 0.34 | 0.0021035 | run_0027 |
| **0.35** | **0.00208576** | **refine/Q05/ref_01** |
| **0.35125** | **0.00208348** | **refine/Q05/ref_04** |
| 0.3525 | 0.00208119 | refine/Q05/ref_03 |
| 0.355 | 0.00207657 | refine/Q05/ref_02 |
| 0.36 | 0.00206717 | run_0029 |
| 0.38 | 0.00202716 | run_0031 |
| 0.4 | 0.0019827 | run_0033 |

Bold rows: the runs next to the answer.

</details>

---

<a id="q8"></a>
## 8. Threshold — ThermoPoroElastic_consolidation_smoke_fim

*Question type:* Threshold (find the largest or smallest input that keeps an output within a limit). *Physics area:* thermoPoromechanics. *Run:* `v6_loop_20261005_185545`, pass2, Q12.

*The deck:* A vertical column of fluid-saturated porous rock, 1 m × 7 m × 1 m, is compressed on its top face and heated there, while the fluid pressure on that face is held at the initial pressure. The base and the vertical faces are fixed against normal displacement, and they are closed to fluid and to heat.

### Question

The requested value is taken from the transient solution, not from a steady state. The domain is a column 1 m by 7 m by 1 m. It is divided into 1 by 14 by 1 eight-node hexahedra with equally spaced nodes, so each element is 1 m by 0.5 m by 1 m. Nodes lie at x = 0 and x = 1 m, at z = 0 and z = 1 m, and at y = 0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5 and 7 m. Cell centres lie at x = 0.5 m, z = 0.5 m and at y = 0.25, 0.75, 1.25, 1.75, 2.25, 2.75, 3.25, 3.75, 4.25, 4.75, 5.25, 5.75, 6.25 and 6.75 m. The time step is fixed at 10 s from the initial instant through 2e4 s.

The skeleton is isotropic linear thermoelastic, with density 2400 kg/m^3, drained bulk modulus 1e4 Pa and shear modulus 2143 Pa. The skeleton is initially stress-free, and its drained linear thermal expansion is measured from the initial temperature of 273 K. The drained linear thermal-expansion coefficient of the skeleton and the porosity thermal-expansion coefficient are separate inputs, and each equals 3e-7 per kelvin. Porosity follows a Biot porosity model with grain bulk modulus 1e27 Pa and reference porosity 0.2. The pore fluid is a single liquid. The fluid density is 1000 kg/m^3 at 0 Pa and 0 K and follows the full exponential of compressibility times the pressure change minus thermal expansivity times the temperature change from that reference; the linear approximation of the exponential is not used, and the isothermal compressibility is 0. The skeleton volumetric heat capacity is 1.672e5 J/(m^3 K) with energy datum 0 at 0 K, and the fluid specific heat is 167.2 J/(kg K) with reference internal energy 0.001 J/kg. The fluid viscosity is 0.001 Pa s and does not depend on pressure or temperature. The fluid thermal expansivity is 0.008 per kelvin. The permeability is isotropic and is not known; it lies in the continuous interval from 1.2e-10 to 3.25e-10 m^2. The thermal conductivity is isotropic and equal to 440 W/(m K).

The initial pressure is 0 Pa and the initial temperature is 273 K, and the column is initially at rest. Horizontal displacement is held at zero on both faces x = 0 and x = 1 m, vertical displacement is held at zero on y = 0, and the out-of-plane displacement is held at zero on both faces z = 0 and z = 1 m. The base and the four vertical faces are closed to fluid flow and to heat flow. The fluid pressure on the top face is held at 0 Pa. Gravity is absent. The top face carries a uniform normal traction that rises linearly from 0 at t = 0 to a compressive value of 1 Pa at t = 1e-10 s and remains 1 Pa thereafter; the force on the solid points opposite the outward normal of the top face. The temperature of the top face is held at 323 K from the initial instant onward.

Vertical displacement is positive upward, from the fixed base toward the loaded top. Pressure is the fluid pressure in the cell, on the same datum as the initial pressure of 0 Pa. Temperature is the absolute temperature in the cell, in kelvin.

> [!IMPORTANT]
> What is the highest permeability, in m^2, at which the vertical displacement of the top face y = 7 m at t = 6000 s is at least 0.1743 m? Accept an answer within 1% of the true value.

### No-tool answer

**Final answer:** 3.04e-10 m^2

<details>
<summary>Full answer (click to expand)</summary>

The controlling mechanism is thermally generated pore pressure. Heating expands the nearly incompressible fluid; lower permeability retains more pressure, producing upward poroelastic expansion. Increasing permeability drains this pressure and reduces top displacement.

Using the constrained one-dimensional modulus

```math
M=K+\frac{4G}{3}
  =10^4+\frac{4(2143)}3
  \approx1.286\times10^4\ {\rm Pa},
```

the vertical strain is approximately

```math
\epsilon_y=\frac{-1+p+3K\alpha_s(T-273)}{M}.
```

Thus $`u_y=0.1743`$ m requires an integrated pore pressure of about

```math
\int_0^7p\,dy \approx
M(0.1743)+7-3K\alpha_s\int_0^7(T-273)\,dy
\approx2.24\times10^3\ {\rm Pa\,m}.
```

The full exponential fluid-density law is important:

```math
\frac{\rho(T)}{\rho(273)}
 =e^{-\beta_f(T-273)},\qquad \beta_f=0.008\ {\rm K^{-1}},
```

so undrained heating produces approximately

```math
p_{\rm th}\approx M\phi_0
\left[e^{\beta_f(T-273)}-1\right],
```

rather than the linearized $`M\phi_0\beta_f(T-273)`$.

Combining this source with one-dimensional thermal diffusion and pressure diffusion,

```math
D_p=\frac{kM}{\mu},
```

and applying the drained top and sealed base conditions gives the displacement threshold at approximately

```math
\boxed{k_{\max}\approx3.0\times10^{-10}\ {\rm m^2}}
```

with my best numerical estimate being

```math
\boxed{k_{\max}\simeq3.04\times10^{-10}\ {\rm m^2}}.
```

This is an analytical/modal estimate of the stated transient problem, not a directly evaluated simulation result.

</details>

### Judge

| | |
|---|---|
| **Verdict** | **INCORRECT** |
| True answer (simulation) | 2.93945e-10 m^2 |
| No-tool answer | 3.04e-10 m^2 |
| Relative error | +3.42% |
| Absolute error | 1.00547e-11 m^2 |
| Tolerance | 1% (relative) |
| Within tolerance | no |
| Error direction | over |
| Unit conversion | m^2 -> m^2 x1 |
| Reasoning sound | no |
| Lucky-guess flag | no |
| Mechanism match | yes |

**Missed effect:** —

**Decisive comparison:** The simulated top displacement at 6000 s falls through 0.1743 m inside the bracket from 2.9336e-10 to 2.9453e-10 m^2, so the threshold permeability is 2.939e-10 m^2, and it drops steadily as permeability rises because thermal pore pressure drains. The answer uses that same thermal-pressure-and-drainage mechanism, but the boxed 3.04e-10 m^2 is not produced by any shown solution of the strain integral or the coupled diffusion problem.

**Key discrepancy:** The strain, undrained thermal-pressure, and diffusivity relations are never solved; 3.04e-10 m^2 is only asserted as a modal estimate.

<details>
<summary>How the true answer was obtained (simulation evidence)</summary>

**Selection rule:** Linear interpolation of KPERM between the two neighbouring rows whose uy7_t6000 brackets the stated value 0.1743.

**Refinement:** 8 extra GEOS runs narrowed the answer to the bracket 2.93359e-10 to 2.94531e-10 (width 1.17187e-12); the true value is its midpoint.

**Why it should be hard (generator's rationale):** Top displacement does not identify a one-digit hydraulic diffusivity. The thermal pressure and its drainage both change across the permeability interval.

**Simulated points of the case:**

Case: {"COND": 440.0, "ALPHA": 0.008, "SCHEDULE": "step"}; target 0.1743; search interval [1.2e-10, 3.25e-10]

| KPERM | O['uy7_t6000'] | run |
|---|---|---|
| 2.5e-10 | 0.197384 | refine/Q12/ref_01 |
| 2.875e-10 | 0.177233 | refine/Q12/ref_03 |
| 2.92187e-10 | 0.174957 | refine/Q12/ref_06 |
| **2.93359e-10** | **0.174395** | **refine/Q12/ref_08** |
| **2.94531e-10** | **0.173837** | **refine/Q12/ref_07** |
| 2.96875e-10 | 0.172729 | refine/Q12/ref_05 |
| 3.0625e-10 | 0.168413 | refine/Q12/ref_04 |
| 3.25e-10 | 0.160305 | refine/Q12/ref_02 |

Bold rows: the runs next to the answer.

</details>

---

<a id="q9"></a>
## 9. Optimisation — sourceFlux_2d

*Question type:* Optimisation (find the input value that maximises or minimises an output). *Physics area:* singlePhaseFlow. *Run:* `v6_loop_20261005_185545`, pass1, Q15.

*The deck:* A closed 11 m × 11 m × 1 m box of porous rock holds a single isothermal fluid. Fluid is injected into one interior cell.

### Question

The pressure evolves as a transient process from the initial state until 2.0e4 s. The time step is fixed at 10 s. The domain is a box 11 m by 11 m by 1 m, divided into a uniform grid of 11 by 11 by 1 eight-node hexahedra with nodes on a 1 m lattice, so every cell is a 1 m cube and every cell centre lies at half-metre coordinates with elevation 0.5 m. All outer faces of the box are closed to flow. Gravity is 9.81 m/s^2 in the negative vertical direction; because every cell centre has the same elevation, the gravitational head difference between any pair of cells is zero. The fluid is water-like and isothermal, with an exponential pressure-density relation, reference density 1000 kg/m^3 at reference pressure 0 Pa, compressibility 5.0e-10 Pa^-1, and a constant viscosity of 0.001 Pa·s (the viscosity does not depend on pressure). The rock porosity follows an exponential pressure-porosity relation with reference porosity 0.05 at reference pressure 0 Pa and compressibility 1.0e-9 Pa^-1. Outside the barrier cells the permeability is isotropic and constant in time, with each diagonal component equal to the stated matrix value. The barrier cells, each with isotropic permeability 2.0e-22 m^2, are the five cells with x from 3 m to 4 m and y from 3 m to 8 m, and the five cells with x from 7 m to 8 m and y from 3 m to 8 m. The entire injected mass enters the single cell that occupies x from 5 m to 6 m and y from 5 m to 6 m. The pressure is held at 5.0e6 Pa for the whole transient in the four cells occupying x,y ranges [1 m, 2 m] by [1 m, 2 m], [9 m, 10 m] by [1 m, 2 m], [1 m, 2 m] by [9 m, 10 m], and [9 m, 10 m] by [9 m, 10 m]. The initial pressure is 5.0e6 Pa in every cell. Injection rates below are positive mass rates in kg/s into that cell. The fluid mass in a cell is the product of its porosity, its fluid density and its volume of 1 m^3, and a regional fluid mass is the sum of that quantity over the named cells. The bulk volume of each cell does not change. Outside the barrier cells the matrix permeability is 2.2e-16 m^2. The equivalent rate Q is 1.55e-3 kg/s. The total mass Q times 2.0e4 kg is injected at a constant rate from the start until time τ and none after. The schedule time τ lies between 5.5e3 s and 1.15e4 s.

> [!IMPORTANT]
> What value of τ, in seconds, maximises the increase of the fluid mass summed over all 121 cells above the fluid mass present in those cells at the initial pressure, at 1.0e4 s? Give τ within 1%.

### No-tool answer

**Final answer:** 10000 s

<details>
<summary>Full answer (click to expand)</summary>

Let $`T=10{,}000`$ s and total injected mass

```math
M=Q(2.0\times10^4)=1.55\times10^{-3}\times2.0\times10^4=31\ {\rm kg}.
```

For a schedule ending at $`\tau`$, the rate is $`M/\tau`$.

Let $`h(a)`$ be the fraction of an injected mass increment remaining after age $`a`$. Because fluid progressively escapes into the four pressure-controlled cells, $`h(a)`$ decreases with age.

For $`\tau\le T`$,

```math
\Delta m(T)=\frac{M}{\tau}\int_0^\tau h(T-s)\,ds.
```

Increasing $`\tau`$ shifts injection toward later times, giving it less time to escape, so stored mass increases.

For $`\tau>T`$, only the fraction $`T/\tau`$ of the prescribed 31 kg has entered by $`T`$:

```math
\Delta m(T)=\frac{M}{\tau}\int_0^T h(T-s)\,ds,
```

which decreases as $`\tau`$ increases.

Thus the maximum occurs where the injection finishes exactly at the observation time:

```math
\boxed{\tau=1.00\times10^4\ {\rm s}}
```

The corresponding injection rate is $`31/10{,}000=3.10\times10^{-3}\ {\rm kg/s}`$. Pressure-dependent density and porosity are weak enough here that they should not shift this optimum materially.

</details>

### Judge

| | |
|---|---|
| **Verdict** | **CORRECT** |
| True answer (simulation) | 9988.28 s |
| No-tool answer | 10000 s |
| Relative error | +0.12% |
| Absolute error | 11.7188 s |
| Tolerance | 1% (relative) |
| Within tolerance | yes |
| Error direction | over |
| Unit conversion | identical units |
| Reasoning sound | yes |
| Lucky-guess flag | no |
| Mechanism match | yes |

**Missed effect:** —

**Decisive comparison:** The answer commits to τ = 10000 s: with a fixed injected mass, later shut-in leaves less time for expulsion through the pressure-controlled cells, while any shut-in after the observation time has not yet delivered the full 31 kg, so the stored-mass maximum sits where injection ends at 1.0e4 s. The simulated domain-mass increase follows that same rise-then-fall and peaks at 9988 s.

**Key discrepancy:** The optimum is taken to be exactly the observation time; the quadratic vertex of the simulated mass increase is 9988 s.

<details>
<summary>How the true answer was obtained (simulation evidence)</summary>

**Selection rule:** Quadratic vertex of O['m_dom_t10000']-6095.469641625134 versus TAU through run_0127, run_0128 and run_0129, the middle of which is strictly best.

**Refinement:** 11 extra GEOS runs narrowed the answer to the bracket 9968.75 to 10007.8 (width 39.0625); the true value is its midpoint.

**Why it should be hard (generator's rationale):** List (a) shortcut 4 fails: stored mass is not the injected mass, and the expelled fraction depends on the schedule, so the shut-in time that maximises the domain mass increase is not fixed by the injected mass, which is the same at every shut-in time.

**Simulated points of the case:**

Case: {"MODE": "shut_in", "K": 2.2e-16, "Q": 0.00155, "DT": 10.0, "T_END": 20000.0}; search interval [5500.0, 11500.0]

| TAU | O['m_dom_t10000']-6095.469641625134 | run |
|---|---|---|
| 5500 | 12.9574 | run_0126 |
| 7500 | 15.768 | run_0127 |
| 8500 | 17.2596 | refine/Q15/ref_02 |
| 9500 | 18.6584 | run_0128 |
| 9656.25 | 18.8698 | refine/Q15/ref_05 |
| 9812.5 | 19.0431 | refine/Q15/ref_04 |
| 9890.62 | 19.1434 | refine/Q15/ref_07 |
| 9929.69 | 19.1929 | refine/Q15/ref_09 |
| **9968.75** | **19.2421** | **refine/Q15/ref_06** |
| **9988.28** | **19.2665** | **refine/Q15/ref_11** |
| 10007.8 | 19.2599 | refine/Q15/ref_10 |
| 10046.9 | 19.185 | refine/Q15/ref_08 |
| 10125 | 19.0369 | refine/Q15/ref_03 |
| 10750 | 17.9299 | refine/Q15/ref_01 |

Bold rows: the runs next to the answer.

</details>

---

<a id="q10"></a>
## 10. Optimisation — mpm_singleParticle

*Question type:* Optimisation (find the input value that maximises or minimises an output). *Physics area:* materialPointMethod. *Run:* `v6_loop_20261006_170718`, pass1, Q13.

*The deck:* One solid particle sits at the center of a cube and is given a uniform initial velocity along x. The cube is a fixed background grid.

### Question

One solid particle occupies a cube that extends from −1.5 m to 1.5 m in x, y and z. The cube is divided into 3×3×3 equal trilinear hexahedra, so the edge length is 1 m and the nodes lie at −1.5, −0.5, 0.5 and 1.5 m on each axis. The particle is a parallelepiped. At the initial instant its center is the origin and its three edge vectors from the center are (0.5, 0, 0) m, (0, 0.5, 0) m and (0, 0, 0.5) m. The eight corners are every combination of (±0.5, ±0.5, ±0.5) m. The initial volume is 1 m³. The center is the average of the eight corners of the parallelepiped. The particle is isotropic linear elastic with bulk modulus K, shear modulus G, density 1000 kg/m³ and thermal-expansion coefficient 0. The bulk modulus K is 2.0×10⁹ Pa. The shear modulus G lies in the continuous interval from 5.0×10⁸ Pa to 1.9×10⁹ Pa, endpoints included. Damage is 0, the strength scale is 1, and no extra domain-scaling factor is applied. At the initial instant the center is at the origin, the stress is zero and the deformation gradient is the identity. The initial velocity is (200, 0, 0) m/s. There is no body force. The background cells are assigned an isotropic linear elastic solid with density 1000 kg/m³, bulk modulus 1 GPa and shear modulus 1 GPa. The face x = +1.5 m is a symmetry face. A symmetry face has zero velocity normal to the face. The other five faces are open. An open face has no prescribed velocity. The motion is transient and dynamic, integrated with a fixed time step of 2×10⁻⁵ s until 0.008 s. The particle may displace in x, y and z. Stress is Cauchy stress with tension positive; the axial component is the xx component.

> [!IMPORTANT]
> What shear modulus G, in pascals, makes the x-component of velocity at 0.008 s as small as possible in the algebraic sense? The required tolerance is 1% relative.

### No-tool answer

**Final answer:** 1.9e+09 Pa

<details>
<summary>Full answer (click to expand)</summary>

The relevant longitudinal modulus is

```math
M=K+\frac{4G}{3},
\qquad
c_L=\sqrt{\frac{M}{\rho}}.
```

Increasing $`G`$ raises $`c_L`$, so the rigid symmetry boundary reverses the particle’s momentum sooner. In this coarse one-particle discretization, that also reduces the time over which boundary coupling dissipates momentum, producing a more negative $`v_x`$ at $`0.008`$ s.

Therefore, the predicted algebraic minimum occurs at the upper endpoint:

```math
\boxed{G \approx 1.90\times10^9\ {\rm Pa}}
```

An ideal, lossless continuum bar would rebound at approximately $`-200`$ m/s for every listed $`G`$ by this time; the endpoint selection is therefore a prediction based on the stated coarse transient discretization.

</details>

### Judge

| | |
|---|---|
| **Verdict** | **INCORRECT** |
| True answer (simulation) | 1.59375e+09 Pa |
| No-tool answer | 1.9e+09 Pa |
| Relative error | +19.22% |
| Absolute error | 3.0625e+08 Pa |
| Tolerance | 1% (relative) |
| Within tolerance | no |
| Error direction | over |
| Unit conversion | Pa -> Pa x1 |
| Reasoning sound | no |
| Lucky-guess flag | no |
| Mechanism match | no |

**Missed effect:** On this interval vx at 0.008 s is non-monotonic in G: it reaches an algebraic minimum near 1.59 GPa and then becomes less negative, so a stiffer particle does not have a monotonically smaller late velocity.

**Decisive comparison:** The answer treats a higher dilatational speed as always leaving a more negative vx at 0.008 s and therefore picks the upper endpoint 1.9e9 Pa. The simulated points fall from about +84 m/s at 0.5 GPa to about -126 m/s near 1.594e9 Pa, then rise to about -114 m/s at 1.75e9 Pa.

**Key discrepancy:** The committed value is the upper endpoint, but the algebraic minimum of vx_end is an interior turning point near 1.594e9 Pa.

<details>
<summary>How the true answer was obtained (simulation evidence)</summary>

**Selection rule:** Three-dimensional case, launch speed 200 m/s. On the stated interval the discrete minimum of vx_end is at SHEAR 1.5e9 Pa (run_0071, -121.81087265 m/s), with neighbours run_0070 at 1.25e9 Pa (-74.49685636 m/s) and run_0072 at 1.75e9 Pa (-114.40598552 m/s). true_value_grid is the vertex of the quadratic through those three points. The vertex lies between 1.25e9 Pa and 1.75e9 Pa. No other grid shear in [5.0e8, 1.9e9] Pa has a smaller vx_end.

**Refinement:** 11 extra GEOS runs narrowed the answer to the bracket 1.58984e+09 to 1.59766e+09 (width 7.8125e+06); the true value is its midpoint.

**Why it should be hard (generator's rationale):** List (a) item 3: an undamped spring has a frequency that rises smoothly with shear modulus, and it does not put the most negative late velocity at an interior modulus near 1.6 GPa. Stiffer does not mean a monotonically smaller late velocity on this interval. List (a) item 1 fails because coasting keeps the velocity equal to 200 m/s for every modulus.

**Simulated points of the case:**

Case: {"STRAIN": "3d", "VX": 200.0}; search interval [500000000.0, 1900000000.0]

| SHEAR | O['vx_end'] | run |
|---|---|---|
| 5e+08 | 83.5791 | run_0067 |
| 7.5e+08 | 67.8539 | run_0068 |
| 1e+09 | 2.69164 | run_0069 |
| 1.25e+09 | -74.4969 | run_0070 |
| 1.375e+09 | -104.049 | refine/Q13/ref_01 |
| 1.5e+09 | -121.811 | run_0071 |
| 1.53125e+09 | -124.079 | refine/Q13/ref_04 |
| 1.5625e+09 | -125.426 | refine/Q13/ref_03 |
| 1.57812e+09 | -125.75 | refine/Q13/ref_06 |
| 1.58594e+09 | -125.824 | refine/Q13/ref_08 |
| **1.58984e+09** | **-125.84** | **refine/Q13/ref_10** |
| **1.59375e+09** | **-125.84** | **refine/Q13/ref_05** |
| 1.59766e+09 | -125.826 | refine/Q13/ref_11 |
| 1.60156e+09 | -125.798 | refine/Q13/ref_09 |
| 1.60938e+09 | -125.698 | refine/Q13/ref_07 |
| 1.625e+09 | -125.325 | refine/Q13/ref_02 |
| 1.75e+09 | -114.406 | run_0072 |

Bold rows: the runs next to the answer.

</details>

---

<a id="q11"></a>
## 11. Magnitude — PoroElastic_conformingFracture_2d_openingFrac_vertical_smoke

*Question type:* Magnitude (find how large a quantity is at a stated place and time). *Physics area:* poromechanicsFractures. *Run:* `v6_loop_20261005_185545`, pass1, Q13.

*The deck:* A square rock slab, 2 m by 2 m in the horizontal plane and 1 m thick, contains one pre-existing vertical fracture on the plane x = 0. The fracture is filled with water and can open or stay closed under Coulomb contact.

### Question

A square rock slab extends from x = −1 m to x = 1 m, from y = −1 m to y = 1 m, and from z = 0 m to z = 1 m. The mesh is 8 by 10 by 1 eight-node hexahedra with equal spacing, 0.25 m in x, 0.20 m in y, and 1 m in z. A single pre-existing vertical fracture lies on x = 0 and spans y = −0.8 m to y = 0.8 m through the full thickness; it does not propagate. The response is the transient evolution from the initial state under the load schedule below. The time step is 0.04 s and the end time is 20 s. The solid skeleton is isotropic and linear elastic, with bulk modulus 5555555555.5556 Pa and shear modulus 4166666666.6667 Pa. The solid density is 1 kg/m³ and the gravity vector is zero. The pore space follows a Biot porosity model with reference porosity 0.2 and grain bulk modulus 1e27 Pa. The rock permeability is constant and isotropic with value 1e-14 m². The water density is 1000 kg/m³ and the viscosity is 1e-3 Pa·s and does not depend on pressure. The water compressibility is 0, so the density stays 1000 kg/m³; the reference pressure used by that model is 1e6 Pa. The fracture pore volume fraction is fixed at 1, with pore compressibility 0 and reference pressure 0. Fracture permeability is the parallel-plate cubic law applied to the hydraulic aperture. The reference mechanical aperture of the fracture is 1e-3 m. The hydraulic aperture is 1e-6 m at a mechanical aperture of −1e-3 m and 1e-3 m at a mechanical aperture of 0, and is extended linearly. The fracture faces obey Coulomb friction with coefficient 0.577350269 and cohesion 0. The pore pressure is zero everywhere at the initial instant. Effective stress is the Biot effective stress and is positive in tension. The initial effective stress is σ_xx = -1 Pa with every other component equal to 0. The pore pressure on the faces y = −1 m and y = 1 m is held at 0. The normal displacement is zero on y = ±1 m, the vertical displacement is zero on z = 0, and the face z = 1 m is free of traction. The wall at x = −1 m moves in the +x direction and the wall at x = +1 m moves in the −x direction, each by 5e-5 m, with that distance increasing linearly from 0 at the initial instant to 5e-5 m at the end of the ramp and then held. No pore pressure is prescribed on the fracture. The ramp duration is 8 s.

> [!IMPORTANT]
> What is the pore pressure, in pascals, at 15 s in the matrix cell centered at (0.375 m, 0.1 m, 0.5 m)? Give a single number. The required tolerance is relative: the answer must be within 1%.

### No-tool answer

**Final answer:** 15000 Pa

<details>
<summary>Full answer (click to expand)</summary>

15000

</details>

### Judge

| | |
|---|---|
| **Verdict** | **INCORRECT** |
| True answer (simulation) | 25499.3 Pa |
| No-tool answer | 15000 Pa |
| Relative error | -41.17% |
| Absolute error | -10499.3 Pa |
| Tolerance | 1% (relative) |
| Within tolerance | no |
| Error direction | under |
| Unit conversion | Pa -> Pa x1 |
| Reasoning sound | no |
| Lucky-guess flag | no |
| Mechanism match | no |

**Missed effect:** At 1e-14 m² the 15 s matrix pressure is set by the transient race between the inward-wall compression ramp and leakoff to the drained ends, not by an undrained peak or a steady drained value.

**Decisive comparison:** The simulation for this 8 s compression ramp at 1e-14 m² gives 25499 Pa at 15 s, while the ramp is still inside the drainage transient. The reply commits to 15000 Pa with no derivation, so it neither uses that ramp–leakoff balance nor supports the number.

**Key discrepancy:** A bare 15000 Pa guess omits the partial leakoff that fixes the mid-cell pressure after the ramp.

<details>
<summary>How the true answer was obtained (simulation evidence)</summary>

**Selection rule:** Taken directly from the sweep table. Optimisation on ramp duration was replaced because the only interior peaks sit at the observation time and did not converge within 12 refinement runs.

**Refinement:** 12 extra GEOS runs narrowed the answer to the bracket 9.96875 to 10.0625 (width 0.09375); the true value is its midpoint.

**Why it should be hard (generator's rationale):** List (a) item 5: the ramp duration that maximises the mid-cell pressure at the fixed time 10 s is not 10 s. Drainage during the ramp moves the maximiser away from the observation time.

**Simulated points of the case:**

Answer computed as R['A']['p_mid_t15'] from these runs:
A = run_0038: inputs {"DT": 0.04, "TMAX": 20.0, "amp": 5e-05, "k": 1e-14, "scenario": "compress", "tau": 8.0}; p_mid_t15 = 25499.3
value: 25499.3
(Only the provenance runs are shown; full time histories are not kept.)

</details>

---

<a id="q12"></a>
## 12. Magnitude — PoroViscoDruckerPrager_smoke

*Question type:* Magnitude (find how large a quantity is at a stated place and time). *Physics area:* poromechanics. *Run:* `v6_loop_20261005_185545`, pass1, Q15.

*The deck:* A vertical borehole of radius 0.1 m is cut through a porous rock. Only the half y ≥ 0 is meshed (azimuth 0° to 180° from the positive x-axis).

### Question

A vertical borehole of radius 0.1 m is cut through porous rock. Only the half with y greater than or equal to 0 is represented, and azimuth is measured from the positive x-axis. The outer boundary is the upper half of a square of half-width 5 m. The slab extends from z = -1 m to z = 1 m.

Sixty nodes form one layer of eight-node hexahedra. Unmapped radii are 0.1, 0.2366, 0.5225, 1.121, 2.375 and 5 m; azimuths are 0, 45, 90, 135 and 180 degrees; the two vertical stations are z = -1 m and z = 1 m. A node at radius 0.1 m stays on that circle. Any other node at unmapped radius r and azimuth θ is moved to radius 0.1 + (r - 0.1) * (5/cos φ - 0.1) / 4.9 metres, where φ is the angle in radians between θ and the nearest of 0, 90 and 180 degrees, and is then placed at x = r' cos θ, y = r' sin θ.

The displacement ux is zero on every outer node with x = +5 m or x = -5 m, uy is zero on the plane y = 0 and on the outer node at y = 5 m, and uz is zero on z = -1 m and z = 1 m.

The process is quasi-static and transient, with no inertia, from 0 to 80 s at a fixed time step of 10 s.

At the initial instant the displacement is zero, the pore pressure is zero, and the effective stress is uniform with xx component -9 MPa, yy component -11 MPa, zz component -12 MPa and zero shear.

On the borehole wall a compressive normal traction of magnitude 10 MPa pushes the rock outward, and the pore-pressure boundary value on that wall is 10 MPa. Both are multiplied by the same piecewise-linear factor of time. The piecewise-linear factor of time equals 0 at 0 s, equals 1 at 0.1 s, and is held at 1 thereafter.

The solid density is 2700 kg/m^3, the bulk modulus is 1.1111e10 Pa and the shear modulus is 8.3333e9 Pa. The strength model is Drucker-Prager plasticity with friction angle 6 degrees, dilation angle 3 degrees, cohesion 1.0e4 Pa and linear hardening modulus 0.5e9 Pa.

Viscoplasticity is Duvaut-Lions with a single relaxation time. The relaxation time is 0.1 s.

The pore fluid has density 1000 kg/m^3, viscosity 0.001 Pa.s, reference pressure 0, compressibility 2.09028227021e-10 Pa^-1 and zero viscosibility. The porosity model is Biot porosity with reference porosity 0.3 and grain bulk modulus 1.0e27 Pa.

The permeability is isotropic. Its value is 1e-14 m^2.

Gravity is zero.

Pore pressure is positive in compression. The Cauchy stress in equilibrium is the Drucker-Prager effective stress minus pore pressure times the identity.

The requested pore pressure is the element-volume-weighted average over the rock at 80 s.

The requested pore pressure is the element-volume-weighted average over the rock at 80 s.

> [!IMPORTANT]
> What is that average pore pressure, in MPa? The answer must be accurate within 1%.

### No-tool answer

**Final answer:** 1.42 MPa

<details>
<summary>Full answer (click to expand)</summary>

The pressure evolution is primarily hydraulic diffusion from the 10 MPa borehole boundary.

Using Biot storage for a plane-strain porous solid,

```math
S \approx \phi c_f+\frac{1}{K+\frac43G}
=0.3(2.0903\times10^{-10})
+\frac{1}{1.1111\times10^{10}+\frac43(8.3333\times10^9)}
\approx1.08\times10^{-10}\ {\rm Pa^{-1}}.
```

Thus,

```math
D=\frac{k}{\mu S}
\approx\frac{10^{-14}}{10^{-3}(1.08\times10^{-10})}
\approx0.093\ {\rm m^2/s}.
```

At 80 s, $`Dt/a^2\approx740`$. Approximating diffusion from the cylindrical wall and accounting for the 10 s implicit time steps and finite square domain gives a normalized volume-average pressure of approximately $`0.142`$.

Therefore, my best estimate is

```math
\boxed{\overline p(80\,{\rm s})\approx 1.42\ {\rm MPa}}.
```

The plastic and viscoplastic corrections should be small for the domain-averaged pressure because the relaxation time (0.1 s) is much shorter than each time step.

</details>

### Judge

| | |
|---|---|
| **Verdict** | **INCORRECT** |
| True answer (simulation) | 2.03152 MPa |
| No-tool answer | 1.42 MPa |
| Relative error | -30.10% |
| Absolute error | -0.61152 MPa |
| Tolerance | 1% (relative) |
| Within tolerance | no |
| Error direction | under |
| Unit conversion | MPa -> MPa x1 |
| Reasoning sound | no |
| Lucky-guess flag | no |
| Mechanism match | yes |

**Missed effect:** —

**Decisive comparison:** The answer treats this 1e-14 m² case as partial hydraulic diffusion, which is the effect that leaves the volume-averaged pressure only partly built, but the factor 0.142 is asserted after Dt/a²≈740 and is not obtained from that diffusion solution.

**Key discrepancy:** The committed 1.42 MPa rests on an unsupported normalized average of 0.142 rather than a closed diffusion estimate.

<details>
<summary>How the true answer was obtained (simulation evidence)</summary>

**Selection rule:** Single successful row: early schedule, permeability 1e-14 m^2, relaxation time 0.1 s, volume-averaged pore pressure.

**Refinement:** 12 extra GEOS runs narrowed the answer to the bracket 2.71875e-15 to 2.8125e-15 (width 9.375e-17); the true value is its midpoint.

**Why it should be hard (generator's rationale):** Treating the rock as either fully undrained (pressure stays near zero) or fully drained (pressure equals 10 MPa) misses this intermediate permeability, where the average pore pressure is only partly built.

**Simulated points of the case:**

Answer computed as R['A']['p_avg_Pa']/1e6 from these runs:
A = run_0133: inputs {"SCHEDULE": "early", "PERM": 1e-14, "RELAXATION": 0.1}; SCHEDULE = early, PERM = 1e-14, RELAXATION = 0.1, p_avg_Pa = 2.03152e+06
value: 2.03152
(Only the provenance runs are shown; full time histories are not kept.)

</details>

