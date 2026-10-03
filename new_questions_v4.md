# GEOS Sweep Bench: Pass 1 questions, no-tool answers and judge results

**Deck:** `CasedElasticWellbore_ImperfectInterfaces_smoke__a229b60a` · **Run:** `v4_run1` · **Status:** **VALIDATED**
**Result:** 12 of 15 incorrect (needed 10), 3 correct (3 with correct value but wrong reasoning).
**No-tool model:** gpt-5.6-sol-medium · **Judge:** claude-opus-5-5-high · **Tolerance:** ±1% relative

## Summary

| Q | Category | Type | True answer | No-tool answer | Rel. error | Verdict | Reasoning sound |
|---|---|---|---|---|---|---|---|
| [Q01](#q01) | Friction-controlled casing ovalization | magnitude | 6.857 mm | 7.7 mm | +12.3% | ❌ INCORRECT | no |
| [Q02](#q02) | Interface slip partition | magnitude | 780.1 um | 500 um | -35.9% | ❌ INCORRECT | no |
| [Q03](#q03) | Load-sequence (path) effects | magnitude | 10.62 MPa | 11.1 MPa | +4.5% | ❌ INCORRECT | no |
| [Q04](#q04) | Casing membrane stress | magnitude | -95.1 MPa | -89.5 MPa | +5.9% | ❌ INCORRECT | no |
| [Q05](#q05) | Friction-controlled casing ovalization | inverse | 0.1381 dimensionless | 0.2 dimensionless | +44.8% | ❌ INCORRECT | no |
| [Q06](#q06) | Interface slip partition | inverse | 2.363 dimensionless | 2.1 dimensionless | -11.1% | ❌ INCORRECT | no |
| [Q07](#q07) | Interface contact pressure distribution | inverse | 3.098 MPa | 5 MPa | +61.4% | ❌ INCORRECT | no |
| [Q08](#q08) | Casing membrane stress | inverse | 0.2676 dimensionless | 0.2 dimensionless | -25.3% | ❌ INCORRECT | no |
| [Q09](#q09) | Friction-controlled casing ovalization | threshold | 0.1746 dimensionless | 0.2 dimensionless | +14.5% | ❌ INCORRECT | no |
| [Q10](#q10) | Interface slip partition | threshold | 2.145 dimensionless | 2.4 dimensionless | +11.9% | ❌ INCORRECT | no |
| [Q11](#q11) | Casing membrane stress | threshold | 8.141 MPa | 8.5 MPa | +4.4% | ❌ INCORRECT | no |
| [Q12](#q12) | Load-sequence (path) effects | choice | B | B | – | ✅ CORRECT | no |
| [Q13](#q13) | Interface slip partition | choice | D | D | – | ✅ CORRECT | no |
| [Q14](#q14) | Interface contact pressure distribution | choice | A | B | – | ❌ INCORRECT | no |
| [Q15](#q15) | Casing membrane stress | choice | C | C | – | ✅ CORRECT | no |

---

## Q01

**Category:** Friction-controlled casing ovalization · **Type:** magnitude · **Template:** `displacement|magnitude`

### Question

A plane-strain cross-section of a cased wellbore consists of three concentric, linear isotropic elastic (small-strain) layers: a steel casing between r = 0.100 m and r = 0.106 m, a cement sheath between r = 0.106 m and r = 0.133 m, and a rock annulus between r = 0.133 m and r = 0.170 m. Polar coordinates (r, θ) are used, θ being measured counter-clockwise from the x axis; u_r denotes the radial displacement (outward positive) and u_θ the tangential displacement (positive towards increasing θ). Elastic constants (bulk modulus, shear modulus; these values are the model inputs to the digits shown, the E and ν values in brackets are rounded restatements): casing 175 GPa, 80.8 GPa (E ≈ 210.1 GPa, ν ≈ 0.300); cement 3.3333 GPa, 2.0 GPa (E = 5 GPa, ν = 0.25); rock 5.5556 GPa, 4.16667 GPa (E = 10 GPa, ν = 0.20). The body is represented by 8-node trilinear hexahedral elements (standard displacement formulation, full 2×2×2 Gauss integration): 80 uniform angular divisions over the quarter (1.125° each), 6, 10 and 10 elements of uniform radial size across the casing, cement and rock layers respectively, and a single element through a slab thickness of 0.1 m; elements are straight-sided with all nodes exactly on the circles, and each interface is a zero-thickness surface with matching, initially coincident nodes on both sides. Only the quarter 0° ≤ θ ≤ 90° is modelled, with roller (symmetry) conditions: zero normal displacement on θ = 0° and on θ = 90°. Plane strain: no axial displacement. The slab end faces carry zero axial displacement; there is no gravity and no inertia. The casing–cement interface (r = 0.106 m) and the cement–rock interface (r = 0.133 m) are imperfect frictional contacts. Both interfaces are initially in perfect contact, closed and sticking, without gap or pre-stress; they cannot interpenetrate, have no cohesion and no tensile strength, and transmit shear by dry friction with coefficient μ (no slip while |τ| < μ σn, sliding at |τ| = μ σn). Here σn is the compressive normal stress transmitted across the interface (positive in compression) and τ the shear stress on it; the static and kinetic friction coefficients are both μ and friction is rate-independent. The contact constraints are enforced exactly (no interface compliance): a closed interface has zero relative normal displacement and a sticking interface has zero relative tangential displacement. Kinematics are small-strain and small-sliding: loads, normals and contact pairs refer to the undeformed configuration, each node stays paired with its initially coincident partner, and the applied tractions are dead loads. The applied tractions use the unit normal of each straight-sided element face. The contact is face-based: each matching interface face pair carries one constant traction unknown (normal and shear components), and the contact and friction conditions are imposed per face pair on the face-averaged relative displacement, along that face's own unit normal and tangent. The bore pressure acts only on the surface r = 0.100 m and never enters an interface. The roller conditions apply to every node on θ = 0° and θ = 90°, including both sides of each interface. The stick/slip state is followed incrementally: each increment is a single implicit (backward-Euler) step solved to equilibrium from the converged state of the previous one, the stick/slip state and the slip increment being determined by the end-of-increment tractions, and slip accumulates. The friction coefficient is μ = 0.15 on both interfaces. The outer surface r = 0.17 m is loaded by the traction σ·n, where σ is the uniform stress state σxx = −Sx, σyy = −Sy, σxy = 0 and n is the outward unit normal. Here Sy = 5 MPa and Sx = 8.75 MPa, so that x is the direction of the larger compression. The inner surface carries a uniform compressive pressure p (a negative value of p denotes a uniform tensile normal traction). Here p = 6 MPa. Loading is quasi-static and is applied in 10 equal increments, the outer traction and the inner pressure being ramped together, proportionally, from zero to their final values. The requested quantity refers to the final equilibrium state after increment 10. The system is initially stress-free. All displacements are initially zero. Let ΔD_x = 2 u_r(r = 0.100 m, θ = 0°) and ΔD_y = 2 u_r(r = 0.100 m, θ = 90°) be the changes of the casing inner diameter along x and along y, and call ΔD_y − ΔD_x the ovalization of the casing bore. What is the ovalization ΔD_y − ΔD_x of the casing bore in the final state, in millimetres? The answer is accepted within ±1 % (relative) of the true value.

### No-tool answer

_Model: GPT-5.6 Sol 1M · 208.34 s · tool calls: 0_

````text
The larger compression along \(x\) makes the bore contract more along \(x\), so the ovalization is positive.

Decompose the far-field loading into:

\[
S_m=\frac{S_x+S_y}{2}=6.875\ {\rm MPa},
\qquad
S_d=\frac{S_x-S_y}{2}=1.875\ {\rm MPa}.
\]

The mean component mainly controls interface compression, approximately \(6\)–\(7\) MPa. Thus the sliding shear limit is roughly

\[
\mu\sigma_n \simeq 0.15(6\text{--}7)
              \simeq 0.9\text{--}1.05\ {\rm MPa}.
\]

The \(n=2\) shear required to keep the dissimilar layers fully bonded is several MPa, especially next to the stiff steel casing. Therefore both interfaces should slide over most of the quadrant, with only small sticking regions near the symmetry axes.

Approximating each sliding layer as an independently bending circular ring, while enforcing radial compatibility, gives a frictionless ovalization near \(9.1\) mm. Coulomb shear opposes the differing tangential motions of the rings. Using the first Fourier harmonic of the nearly saturated interface traction,

\[
\tau_2 \approx \frac{4}{\pi}\mu\sigma_n
       \approx 1.15\text{--}1.25\ {\rm MPa},
\]

reduces the predicted \(n=2\) radial amplitude at the casing bore to approximately

\[
u_r(0.100,0^\circ)\approx -1.9\ {\rm mm},
\qquad
u_r(0.100,90^\circ)\approx +1.9\ {\rm mm}.
\]

Consequently,

\[
\Delta D_y-\Delta D_x
=2\left(u_r(90^\circ)-u_r(0^\circ)\right)
\approx 7.7\ {\rm mm}.
\]

\[
\boxed{\Delta D_y-\Delta D_x \approx 7.7\ {\rm mm}}
\]

This is an analytical estimate of the specified discrete contact calculation; the exact face-based finite-element value cannot be recovered analytically.
````

### Judge

| | |
|---|---|
| True answer | **6.857 mm** |
| No-tool answer | **7.7 mm** |
| Relative error | +12.3% |
| Verdict | **❌ INCORRECT** |
| Reasoning sound | False |
| Correct value, wrong reasoning | False |
| Accepted into benchmark | True |

**Decisive comparison:** The answer commits to 7.7 mm, while the true value is 6.857 mm. That is about 12.3% too high, well outside the ±1% tolerance.

**Key discrepancy:** The value comes from a heuristic, not a derivation. The 9.1 mm frictionless ovalization of independently bending rings is stated without being derived. The friction correction applies an assumed saturated Fourier-harmonic shear to that figure and is never actually computed. Its intermediate numbers also do not match the final value: u_r = ±1.9 mm gives 2·(1.9 − (−1.9)) = 7.6 mm, not 7.7 mm. Neither the stick/slip distribution nor the coupled three-layer elastic response is solved, so 7.7 mm is a rough guess and not supported by the reasoning.

<sub>Provenance: runs run_0226; columns ['oval_cas_in']; refined: False</sub>

---

## Q02

**Category:** Interface slip partition · **Type:** magnitude · **Template:** `displacement_jump|magnitude`

### Question

A plane-strain cross-section of a cased wellbore consists of three concentric, linear isotropic elastic (small-strain) layers: a steel casing between r = 0.100 m and r = 0.106 m, a cement sheath between r = 0.106 m and r = 0.133 m, and a rock annulus between r = 0.133 m and r = 0.170 m. Polar coordinates (r, θ) are used, θ being measured counter-clockwise from the x axis; u_r denotes the radial displacement (outward positive) and u_θ the tangential displacement (positive towards increasing θ). Elastic constants (bulk modulus, shear modulus; these values are the model inputs to the digits shown, the E and ν values in brackets are rounded restatements): casing 175 GPa, 80.8 GPa (E ≈ 210.1 GPa, ν ≈ 0.300); cement 10.3 GPa, 6.45 GPa (E ≈ 16.01 GPa, ν ≈ 0.241); rock 5.5556 GPa, 4.16667 GPa (E = 10 GPa, ν = 0.20). The body is represented by 8-node trilinear hexahedral elements (standard displacement formulation, full 2×2×2 Gauss integration): 80 uniform angular divisions over the quarter (1.125° each), 6, 10 and 10 elements of uniform radial size across the casing, cement and rock layers respectively, and a single element through a slab thickness of 0.1 m; elements are straight-sided with all nodes exactly on the circles, and each interface is a zero-thickness surface with matching, initially coincident nodes on both sides. Only the quarter 0° ≤ θ ≤ 90° is modelled, with roller (symmetry) conditions: zero normal displacement on θ = 0° and on θ = 90°. Plane strain: no axial displacement. The slab end faces carry zero axial displacement; there is no gravity and no inertia. The casing–cement interface (r = 0.106 m) and the cement–rock interface (r = 0.133 m) are imperfect frictional contacts. Both interfaces are initially in perfect contact, closed and sticking, without gap or pre-stress; they cannot interpenetrate, have no cohesion and no tensile strength, and transmit shear by dry friction with coefficient μ (no slip while |τ| < μ σn, sliding at |τ| = μ σn). Here σn is the compressive normal stress transmitted across the interface (positive in compression) and τ the shear stress on it; the static and kinetic friction coefficients are both μ and friction is rate-independent. The contact constraints are enforced exactly (no interface compliance): a closed interface has zero relative normal displacement and a sticking interface has zero relative tangential displacement. Kinematics are small-strain and small-sliding: loads, normals and contact pairs refer to the undeformed configuration, each node stays paired with its initially coincident partner, and the applied tractions are dead loads. The applied tractions use the unit normal of each straight-sided element face. The contact is face-based: each matching interface face pair carries one constant traction unknown (normal and shear components), and the contact and friction conditions are imposed per face pair on the face-averaged relative displacement, along that face's own unit normal and tangent. The bore pressure acts only on the surface r = 0.100 m and never enters an interface. The roller conditions apply to every node on θ = 0° and θ = 90°, including both sides of each interface. The stick/slip state is followed incrementally: each increment is a single implicit (backward-Euler) step solved to equilibrium from the converged state of the previous one, the stick/slip state and the slip increment being determined by the end-of-increment tractions, and slip accumulates. The friction coefficient is μ = 0.25 on both interfaces. The outer surface r = 0.17 m is loaded by the traction σ·n, where σ is the uniform stress state σxx = −Sx, σyy = −Sy, σxy = 0 and n is the outward unit normal. Here Sy = 5 MPa and Sx = 12.5 MPa, so that x is the direction of the larger compression. The inner surface carries a uniform compressive pressure p (a negative value of p denotes a uniform tensile normal traction). Here p = 2 MPa. Loading is quasi-static and is applied in 10 equal increments, the outer traction and the inner pressure being ramped together, proportionally, from zero to their final values. The requested quantity refers to the final equilibrium state after increment 10. The system is initially stress-free. All displacements are initially zero. The slip across the cement–rock interface at θ = 45° is defined as u_θ of the rock-side point at r = 0.133 m, θ = 45° minus u_θ of the cement-side point at the same position. Here u_θ = −u_x sin θ + u_y cos θ with θ = 45°. What is this cement–rock slip at θ = 45° in the final state, in micrometres? The answer is accepted within ±1 % (relative) of the true value.

### No-tool answer

_Model: GPT-5.6 Sol 1M · 210.3 s · tool calls: 0_

````text
The larger \(x\)-compression drives the rock-side point at \(45^\circ\) toward increasing \(\theta\) more strongly than the cement. The cement–rock interface reaches the Coulomb limit,

\[
|\tau|=\mu\sigma_n,\qquad \mu=0.25,
\]

and accumulates positive slip during proportional loading.

Using a plane-strain concentric-annulus estimate, including the broad friction-limited region around \(45^\circ\), I predict

\[
\boxed{u_\theta^{\rm rock}-u_\theta^{\rm cement}\approx +5.0\times10^2\ \mu{\rm m}}
\]

or approximately

\[
\boxed{+500\ \mu{\rm m}}.
\]

The positive sign means motion of the rock side relative to the cement toward increasing \(\theta\). This is an analytical estimate; the exact face-based finite-element/contact value cannot be determined to ±1% without solving the stated discrete system.
````

### Judge

| | |
|---|---|
| True answer | **780.1 um** |
| No-tool answer | **500 um** |
| Relative error | -35.9% |
| Verdict | **❌ INCORRECT** |
| Reasoning sound | False |
| Correct value, wrong reasoning | False |
| Accepted into benchmark | True |

**Decisive comparison:** The answer commits to +500 µm, but the true value is 780.11 µm. That is about 36% low, far outside the ±1% relative tolerance (roughly 772.3 to 787.9 µm).

**Key discrepancy:** The answer never derives the magnitude. It says it uses a 'concentric-annulus estimate' but gives no calculation, so the 500 µm figure is an order-of-magnitude guess. It also does not model the face-based frictional contact on both interfaces or how slip accumulates over the 10 increments, and it admits it cannot pin the value down. The sign (positive slip) is right, but the size is about 36% too small.

<sub>Provenance: runs run_0075; columns ['slip_cr_45']; refined: False</sub>

---

## Q03

**Category:** Load-sequence (path) effects · **Type:** magnitude · **Template:** `contact_traction|magnitude`

### Question

A plane-strain cross-section of a cased wellbore consists of three concentric, linear isotropic elastic (small-strain) layers: a steel casing between r = 0.100 m and r = 0.106 m, a cement sheath between r = 0.106 m and r = 0.133 m, and a rock annulus between r = 0.133 m and r = 0.170 m. Polar coordinates (r, θ) are used, θ being measured counter-clockwise from the x axis; u_r denotes the radial displacement (outward positive) and u_θ the tangential displacement (positive towards increasing θ). Elastic constants (bulk modulus, shear modulus; these values are the model inputs to the digits shown, the E and ν values in brackets are rounded restatements): casing 175 GPa, 80.8 GPa (E ≈ 210.1 GPa, ν ≈ 0.300); cement 3.3333 GPa, 2.0 GPa (E = 5 GPa, ν = 0.25); rock 5.5556 GPa, 4.16667 GPa (E = 10 GPa, ν = 0.20). The body is represented by 8-node trilinear hexahedral elements (standard displacement formulation, full 2×2×2 Gauss integration): 80 uniform angular divisions over the quarter (1.125° each), 6, 10 and 10 elements of uniform radial size across the casing, cement and rock layers respectively, and a single element through a slab thickness of 0.1 m; elements are straight-sided with all nodes exactly on the circles, and each interface is a zero-thickness surface with matching, initially coincident nodes on both sides. Only the quarter 0° ≤ θ ≤ 90° is modelled, with roller (symmetry) conditions: zero normal displacement on θ = 0° and on θ = 90°. Plane strain: no axial displacement. The slab end faces carry zero axial displacement; there is no gravity and no inertia. The casing–cement interface (r = 0.106 m) and the cement–rock interface (r = 0.133 m) are imperfect frictional contacts. Both interfaces are initially in perfect contact, closed and sticking, without gap or pre-stress; they cannot interpenetrate, have no cohesion and no tensile strength, and transmit shear by dry friction with coefficient μ (no slip while |τ| < μ σn, sliding at |τ| = μ σn). Here σn is the compressive normal stress transmitted across the interface (positive in compression) and τ the shear stress on it; the static and kinetic friction coefficients are both μ and friction is rate-independent. The contact constraints are enforced exactly (no interface compliance): a closed interface has zero relative normal displacement and a sticking interface has zero relative tangential displacement. Kinematics are small-strain and small-sliding: loads, normals and contact pairs refer to the undeformed configuration, each node stays paired with its initially coincident partner, and the applied tractions are dead loads. The applied tractions use the unit normal of each straight-sided element face. The contact is face-based: each matching interface face pair carries one constant traction unknown (normal and shear components), and the contact and friction conditions are imposed per face pair on the face-averaged relative displacement, along that face's own unit normal and tangent. The bore pressure acts only on the surface r = 0.100 m and never enters an interface. The roller conditions apply to every node on θ = 0° and θ = 90°, including both sides of each interface. The stick/slip state is followed incrementally: each increment is a single implicit (backward-Euler) step solved to equilibrium from the converged state of the previous one, the stick/slip state and the slip increment being determined by the end-of-increment tractions, and slip accumulates. The friction coefficient is μ = 0.2 on both interfaces. The outer surface r = 0.17 m is loaded by the traction σ·n, where σ is the uniform stress state σxx = −Sx, σyy = −Sy, σxy = 0 and n is the outward unit normal. Here Sy = 5 MPa and Sx = 12.5 MPa, so that x is the direction of the larger compression. The inner surface carries a uniform compressive pressure p (a negative value of p denotes a uniform tensile normal traction). Here p = 6 MPa. Loading is quasi-static and is applied in 10 equal increments in two stages: during increments 1–5 the outer traction is ramped linearly from zero to its final value with zero inner pressure; during increments 6–10 the outer traction is held at its final value while the inner pressure is ramped linearly from zero to its final value. The requested quantity refers to the final equilibrium state after increment 10. The system is initially stress-free. All displacements are initially zero. Define contact pressure = compressive normal stress transmitted across the interface (positive when compressive). On the discretised interface the contact pressure is constant over each interface face element (1.125° wide, one element through the thickness) and equal on both sides, so its average over a 1.125° segment is the value of the single face element covering that segment. What is the casing–cement contact pressure, averaged over the interface segment 88.875° ≤ θ ≤ 90° at r = 0.106 m (the segment adjacent to the θ = 90° symmetry plane), in the final state, in MPa? The answer is accepted within ±1 % (relative) of the true value.

### No-tool answer

_Model: GPT-5.6 Sol 1M · 137.64 s · tool calls: 0_

````text
The mean (axisymmetric) casing–cement pressure is approximately

\[
q_0 \approx 8.90\ \text{MPa (outer load)}
       +1.01\ \text{MPa (bore pressure)}
       =9.91\ \text{MPa}.
\]

The differential far-field compression drives tangential slip. With \(\mu=0.2\), the resulting frictional hoop-force variation raises the pressure near the \(90^\circ\) symmetry plane by about \(1.2\) MPa. The segment midpoint correction from \(90^\circ\) to \(89.4375^\circ\) is negligible.

\[
\boxed{p_{\mathrm{contact}}\approx 11.1\ \text{MPa}}
\]

This is an analytical estimate; the exact face-based finite-element value requires solving the stated incremental contact problem.
````

### Judge

| | |
|---|---|
| True answer | **10.62 MPa** |
| No-tool answer | **11.1 MPa** |
| Relative error | +4.5% |
| Verdict | **❌ INCORRECT** |
| Reasoning sound | False |
| Correct value, wrong reasoning | False |
| Accepted into benchmark | True |

**Decisive comparison:** The answer commits to 11.1 MPa, but the true value is 10.620 MPa. That is about 4.5% too high, well outside the ±1% tolerance window of roughly 10.514 to 10.726 MPa.

**Key discrepancy:** The answer adds a +1.2 MPa friction/slip correction near θ = 90° to an axisymmetric base pressure of 9.91 MPa without deriving it. It does not solve the incremental face-based frictional contact problem that it says is needed, so the correction is a heuristic guess and overshoots the true value.

<sub>Provenance: runs run_0354; columns ['pc_cc_90']; refined: False</sub>

---

## Q04

**Category:** Casing membrane stress · **Type:** magnitude · **Template:** `stress|magnitude`

### Question

A plane-strain cross-section of a cased wellbore consists of three concentric, linear isotropic elastic (small-strain) layers: a steel casing between r = 0.100 m and r = 0.106 m, a cement sheath between r = 0.106 m and r = 0.133 m, and a rock annulus between r = 0.133 m and r = 0.170 m. Polar coordinates (r, θ) are used, θ being measured counter-clockwise from the x axis; u_r denotes the radial displacement (outward positive) and u_θ the tangential displacement (positive towards increasing θ). Elastic constants (bulk modulus, shear modulus; these values are the model inputs to the digits shown, the E and ν values in brackets are rounded restatements): casing 175 GPa, 80.8 GPa (E ≈ 210.1 GPa, ν ≈ 0.300); cement 10.3 GPa, 6.45 GPa (E ≈ 16.01 GPa, ν ≈ 0.241); rock 5.5556 GPa, 4.16667 GPa (E = 10 GPa, ν = 0.20). The body is represented by 8-node trilinear hexahedral elements (standard displacement formulation, full 2×2×2 Gauss integration): 80 uniform angular divisions over the quarter (1.125° each), 6, 10 and 10 elements of uniform radial size across the casing, cement and rock layers respectively, and a single element through a slab thickness of 0.1 m; elements are straight-sided with all nodes exactly on the circles, and each interface is a zero-thickness surface with matching, initially coincident nodes on both sides. Only the quarter 0° ≤ θ ≤ 90° is modelled, with roller (symmetry) conditions: zero normal displacement on θ = 0° and on θ = 90°. Plane strain: no axial displacement. The slab end faces carry zero axial displacement; there is no gravity and no inertia. The casing–cement interface (r = 0.106 m) and the cement–rock interface (r = 0.133 m) are imperfect frictional contacts. Both interfaces are initially in perfect contact, closed and sticking, without gap or pre-stress; they cannot interpenetrate, have no cohesion and no tensile strength, and transmit shear by dry friction with coefficient μ (no slip while |τ| < μ σn, sliding at |τ| = μ σn). Here σn is the compressive normal stress transmitted across the interface (positive in compression) and τ the shear stress on it; the static and kinetic friction coefficients are both μ and friction is rate-independent. The contact constraints are enforced exactly (no interface compliance): a closed interface has zero relative normal displacement and a sticking interface has zero relative tangential displacement. Kinematics are small-strain and small-sliding: loads, normals and contact pairs refer to the undeformed configuration, each node stays paired with its initially coincident partner, and the applied tractions are dead loads. The applied tractions use the unit normal of each straight-sided element face. The contact is face-based: each matching interface face pair carries one constant traction unknown (normal and shear components), and the contact and friction conditions are imposed per face pair on the face-averaged relative displacement, along that face's own unit normal and tangent. The bore pressure acts only on the surface r = 0.100 m and never enters an interface. The roller conditions apply to every node on θ = 0° and θ = 90°, including both sides of each interface. The stick/slip state is followed incrementally: each increment is a single implicit (backward-Euler) step solved to equilibrium from the converged state of the previous one, the stick/slip state and the slip increment being determined by the end-of-increment tractions, and slip accumulates. The friction coefficient is μ = 0.15 on both interfaces. The outer surface r = 0.17 m is loaded by the traction σ·n, where σ is the uniform stress state σxx = −Sx, σyy = −Sy, σxy = 0 and n is the outward unit normal. Here Sy = 5 MPa and Sx = 12.5 MPa, so that x is the direction of the larger compression. The inner surface carries a uniform compressive pressure p (a negative value of p denotes a uniform tensile normal traction). Here p = 6 MPa. Loading is quasi-static and is applied in 10 equal increments in two stages: during increments 1–5 the outer traction is ramped linearly from zero to its final value with zero inner pressure; during increments 6–10 the outer traction is held at its final value while the inner pressure is ramped linearly from zero to its final value. The requested quantity refers to the final equilibrium state after increment 10. The system is initially stress-free. All displacements are initially zero. The through-wall average hoop stress of the casing at θ ≈ 90° is the hoop stress σθθ (total stress, tension positive) averaged over the angular sector 88.875° ≤ θ ≤ 90° (adjacent to the θ = 90° plane) and uniformly with respect to radius across the full casing wall thickness. Concretely, each casing element's Cartesian stress is its Jacobian-weighted volume average over its 2×2×2 Gauss points, σθθ = σxx sin²θc + σyy cos²θc − 2 σxy sinθc cosθc is formed with the polar angle θc of the element centre (the mid-angle of its 1.125° sector), and the sector value is the arithmetic mean over the 6 casing elements of that sector (one per radial layer). What is the through-wall average hoop stress of the casing at θ ≈ 90° in the final state, in MPa (tension positive)? The answer is accepted within ±1 % (relative) of the true value.

### No-tool answer

_Model: GPT-5.6 Sol 1M · 140.55 s · tool calls: 0_

````text
The final casing hoop stress is predicted to be

\[
\boxed{\overline{\sigma_{\theta\theta}}(\theta\approx90^\circ)\approx -89.5\ {\rm MPa}}
\]

(compression; tension is positive).

Key estimate:

- The axisymmetric loading component gives interface pressures of approximately \(9.81\) MPa at the casing–cement interface and \(9.49\) MPa at the cement–rock interface.
- For the casing, Lamé’s solution then gives a through-wall mean hoop stress of about \(-73.3\) MPa.
- The anisotropic outer loading drives frictional shear and ovalization. With \(\mu=0.15\), the accumulated interface shear contributes approximately another \(-16\) MPa near \(\theta=90^\circ\).
- Thus \( -73.3-16.2\approx-89.5\) MPa.
````

### Judge

| | |
|---|---|
| True answer | **-95.1 MPa** |
| No-tool answer | **-89.5 MPa** |
| Relative error | +5.9% |
| Verdict | **❌ INCORRECT** |
| Reasoning sound | False |
| Correct value, wrong reasoning | False |
| Accepted into benchmark | True |

**Decisive comparison:** The answer commits to -89.5 MPa against a true value of -95.10 MPa. That is about 5.9 % off, well outside the ±1 % relative tolerance.

**Key discrepancy:** The axisymmetric Lamé part (about -73.3 MPa from a 6 MPa bore pressure and a roughly 9.81 MPa casing–cement contact pressure) is computed consistently. The deviatoric, friction-dependent part (-16.2 MPa at θ≈90°) is asserted without any derivation: there is no ovalization, slip-zone or staged stick/slip analysis behind it. It underestimates the extra compression at θ≈90° by about 5.6 MPa.

<sub>Provenance: runs run_0134; columns ['shoop_cas_wallavg_90']; refined: False</sub>

---

## Q05

**Category:** Friction-controlled casing ovalization · **Type:** inverse · **Template:** `displacement|inverse`

### Question

A plane-strain cross-section of a cased wellbore consists of three concentric, linear isotropic elastic (small-strain) layers: a steel casing between r = 0.100 m and r = 0.106 m, a cement sheath between r = 0.106 m and r = 0.133 m, and a rock annulus between r = 0.133 m and r = 0.170 m. Polar coordinates (r, θ) are used, θ being measured counter-clockwise from the x axis; u_r denotes the radial displacement (outward positive) and u_θ the tangential displacement (positive towards increasing θ). Elastic constants (bulk modulus, shear modulus; these values are the model inputs to the digits shown, the E and ν values in brackets are rounded restatements): casing 175 GPa, 80.8 GPa (E ≈ 210.1 GPa, ν ≈ 0.300); cement 3.3333 GPa, 2.0 GPa (E = 5 GPa, ν = 0.25); rock 5.5556 GPa, 4.16667 GPa (E = 10 GPa, ν = 0.20). The body is represented by 8-node trilinear hexahedral elements (standard displacement formulation, full 2×2×2 Gauss integration): 80 uniform angular divisions over the quarter (1.125° each), 6, 10 and 10 elements of uniform radial size across the casing, cement and rock layers respectively, and a single element through a slab thickness of 0.1 m; elements are straight-sided with all nodes exactly on the circles, and each interface is a zero-thickness surface with matching, initially coincident nodes on both sides. Only the quarter 0° ≤ θ ≤ 90° is modelled, with roller (symmetry) conditions: zero normal displacement on θ = 0° and on θ = 90°. Plane strain: no axial displacement. The slab end faces carry zero axial displacement; there is no gravity and no inertia. The casing–cement interface (r = 0.106 m) and the cement–rock interface (r = 0.133 m) are imperfect frictional contacts. Both interfaces are initially in perfect contact, closed and sticking, without gap or pre-stress; they cannot interpenetrate, have no cohesion and no tensile strength, and transmit shear by dry friction with coefficient μ (no slip while |τ| < μ σn, sliding at |τ| = μ σn). Here σn is the compressive normal stress transmitted across the interface (positive in compression) and τ the shear stress on it; the static and kinetic friction coefficients are both μ and friction is rate-independent. The contact constraints are enforced exactly (no interface compliance): a closed interface has zero relative normal displacement and a sticking interface has zero relative tangential displacement. Kinematics are small-strain and small-sliding: loads, normals and contact pairs refer to the undeformed configuration, each node stays paired with its initially coincident partner, and the applied tractions are dead loads. The applied tractions use the unit normal of each straight-sided element face. The contact is face-based: each matching interface face pair carries one constant traction unknown (normal and shear components), and the contact and friction conditions are imposed per face pair on the face-averaged relative displacement, along that face's own unit normal and tangent. The bore pressure acts only on the surface r = 0.100 m and never enters an interface. The roller conditions apply to every node on θ = 0° and θ = 90°, including both sides of each interface. The stick/slip state is followed incrementally: each increment is a single implicit (backward-Euler) step solved to equilibrium from the converged state of the previous one, the stick/slip state and the slip increment being determined by the end-of-increment tractions, and slip accumulates. The friction coefficient μ is the same on both interfaces but is not known; it lies between 0.11 and 0.29. The outer surface r = 0.17 m is loaded by the traction σ·n, where σ is the uniform stress state σxx = −Sx, σyy = −Sy, σxy = 0 and n is the outward unit normal. Here Sy = 5 MPa and Sx = 10 MPa, so that x is the direction of the larger compression. The inner surface carries a uniform compressive pressure p (a negative value of p denotes a uniform tensile normal traction). Here p = 6 MPa. Loading is quasi-static and is applied in 10 equal increments in two stages: during increments 1–5 the outer traction is ramped linearly from zero to its final value with zero inner pressure; during increments 6–10 the outer traction is held at its final value while the inner pressure is ramped linearly from zero to its final value. The requested quantity refers to the final equilibrium state after increment 10. The system is initially stress-free. All displacements are initially zero. Let ΔD_x = 2 u_r(r = 0.100 m, θ = 0°) and ΔD_y = 2 u_r(r = 0.100 m, θ = 90°) be the changes of the casing inner diameter along x and along y, and call ΔD_y − ΔD_x the ovalization of the casing bore. The ovalization ΔD_y − ΔD_x of the casing bore in the final state is measured as 9.993 mm. Exactly one value in the stated interval reproduces this measurement. What is the friction coefficient μ (in the interval 0.11 ≤ μ ≤ 0.29)? The answer is accepted within ±1 % (relative) of the true value.

### No-tool answer

_Model: GPT-5.6 Sol 1M · 55.2 s · tool calls: 0_

````text
The outer loading decomposes into

\[
t_r=-7.5-2.5\cos 2\theta\ {\rm MPa},\qquad
t_\theta=2.5\sin 2\theta\ {\rm MPa}.
\]

Thus the anisotropic \(n=2\) component drives casing ovalization and interface slip. During the first loading stage, the approximate traction ratio is

\[
\frac{|\tau|}{\sigma_n}
\approx
\frac{2.5|\sin2\theta|}{7.5+2.5\cos2\theta},
\]

whose maximum is about \(0.354\). Therefore interfaces partially slide throughout the stated \(\mu\)-range. The subsequent bore-pressure ramp increases contact compression and arrests additional sliding, but does not remove accumulated slip.

Matching the resulting piecewise stick–slip response to the measured \(9.993\) mm ovalization gives

\[
\boxed{\mu \approx 0.200}.
\]

The exact ovalization requires the stated incremental finite-element/contact calculation; \(0.200\) is the inferred coefficient.
````

### Judge

| | |
|---|---|
| True answer | **0.1381 dimensionless** |
| No-tool answer | **0.2 dimensionless** |
| Relative error | +44.8% |
| Verdict | **❌ INCORRECT** |
| Reasoning sound | False |
| Correct value, wrong reasoning | False |
| Accepted into benchmark | True |

**Decisive comparison:** The answer commits to μ ≈ 0.200. The true value is 0.13809, so the answer is about 45% too high, far outside the ±1% relative tolerance.

**Key discrepancy:** The answer never computes the ovalization as a function of μ. It estimates a far-field traction ratio, then says it 'matched' 9.993 mm with no calculation shown. The 0.200 value is in effect an unsupported guess, close to the midpoint of the 0.11–0.29 interval. The far-field traction-ratio argument also ignores the bore pressure and how the stiff casing and soft cement redistribute stress, so the interface traction ratios are not the ones it uses.

<sub>Provenance: runs run_0310, run_0330; columns ['oval_cas_in']; refined: True</sub>

---

## Q06

**Category:** Interface slip partition · **Type:** inverse · **Template:** `displacement_jump|inverse`

### Question

A plane-strain cross-section of a cased wellbore consists of three concentric, linear isotropic elastic (small-strain) layers: a steel casing between r = 0.100 m and r = 0.106 m, a cement sheath between r = 0.106 m and r = 0.133 m, and a rock annulus between r = 0.133 m and r = 0.170 m. Polar coordinates (r, θ) are used, θ being measured counter-clockwise from the x axis; u_r denotes the radial displacement (outward positive) and u_θ the tangential displacement (positive towards increasing θ). Elastic constants (bulk modulus, shear modulus; these values are the model inputs to the digits shown, the E and ν values in brackets are rounded restatements): casing 175 GPa, 80.8 GPa (E ≈ 210.1 GPa, ν ≈ 0.300); cement 10.3 GPa, 6.45 GPa (E ≈ 16.01 GPa, ν ≈ 0.241); rock 5.5556 GPa, 4.16667 GPa (E = 10 GPa, ν = 0.20). The body is represented by 8-node trilinear hexahedral elements (standard displacement formulation, full 2×2×2 Gauss integration): 80 uniform angular divisions over the quarter (1.125° each), 6, 10 and 10 elements of uniform radial size across the casing, cement and rock layers respectively, and a single element through a slab thickness of 0.1 m; elements are straight-sided with all nodes exactly on the circles, and each interface is a zero-thickness surface with matching, initially coincident nodes on both sides. Only the quarter 0° ≤ θ ≤ 90° is modelled, with roller (symmetry) conditions: zero normal displacement on θ = 0° and on θ = 90°. Plane strain: no axial displacement. The slab end faces carry zero axial displacement; there is no gravity and no inertia. The casing–cement interface (r = 0.106 m) and the cement–rock interface (r = 0.133 m) are imperfect frictional contacts. Both interfaces are initially in perfect contact, closed and sticking, without gap or pre-stress; they cannot interpenetrate, have no cohesion and no tensile strength, and transmit shear by dry friction with coefficient μ (no slip while |τ| < μ σn, sliding at |τ| = μ σn). Here σn is the compressive normal stress transmitted across the interface (positive in compression) and τ the shear stress on it; the static and kinetic friction coefficients are both μ and friction is rate-independent. The contact constraints are enforced exactly (no interface compliance): a closed interface has zero relative normal displacement and a sticking interface has zero relative tangential displacement. Kinematics are small-strain and small-sliding: loads, normals and contact pairs refer to the undeformed configuration, each node stays paired with its initially coincident partner, and the applied tractions are dead loads. The applied tractions use the unit normal of each straight-sided element face. The contact is face-based: each matching interface face pair carries one constant traction unknown (normal and shear components), and the contact and friction conditions are imposed per face pair on the face-averaged relative displacement, along that face's own unit normal and tangent. The bore pressure acts only on the surface r = 0.100 m and never enters an interface. The roller conditions apply to every node on θ = 0° and θ = 90°, including both sides of each interface. The stick/slip state is followed incrementally: each increment is a single implicit (backward-Euler) step solved to equilibrium from the converged state of the previous one, the stick/slip state and the slip increment being determined by the end-of-increment tractions, and slip accumulates. The friction coefficient is μ = 0.2 on both interfaces. The outer surface r = 0.17 m is loaded by the traction σ·n, where σ is the uniform stress state σxx = −Sx, σyy = −Sy, σxy = 0 and n is the outward unit normal. Here Sy = 5 MPa and Sx = k·Sy, where the stress ratio k is not known; it lies between 1.6 and 2.6 (x is the direction of the larger compression). The inner surface carries a uniform compressive pressure p (a negative value of p denotes a uniform tensile normal traction). Here p = 6 MPa. Loading is quasi-static and is applied in 10 equal increments, the outer traction and the inner pressure being ramped together, proportionally, from zero to their final values. The requested quantity refers to the final equilibrium state after increment 10. The system is initially stress-free. All displacements are initially zero. The slip across the casing–cement interface at θ = 45° is defined as u_θ of the cement-side point at r = 0.106 m, θ = 45° minus u_θ of the casing-side point at the same position. Here u_θ = −u_x sin θ + u_y cos θ with θ = 45°. This casing–cement slip at θ = 45° in the final state is measured as +437.1 micrometres. Exactly one value in the stated interval reproduces this measurement. What is the stress ratio k = Sx/Sy (in the interval 1.6 ≤ k ≤ 2.6)? The answer is accepted within ±1 % (relative) of the true value.

### No-tool answer

_Model: GPT-5.6 Sol 1M · 140.85 s · tool calls: 0_

````text
The unequal far-field stress excites the \(n=2\) ovalization mode. At \(\theta=45^\circ\), its tangential component is maximal:

\[
S_x-S_y=5(k-1)\ {\rm MPa}.
\]

Using the layered-annulus compliance scale,

\[
\frac{r(S_x-S_y)}{G_{\rm rock}}
=\frac{0.106\,5(k-1)\times10^6}{4.16667\times10^9}
\approx127.2(k-1)\ \mu{\rm m},
\]

with an ovalization amplification of approximately \(3.1\!-\!3.2\), including the sliding-interface friction correction, gives

\[
\delta_{\theta}\approx 0.40(k-1)\ {\rm mm}.
\]

Setting \(\delta_{\theta}=0.4371\) mm yields \(k\approx2.1\). The positive sign is consistent with \(S_x>S_y\), which drives positive relative tangential motion at \(45^\circ\).

\[
\boxed{k=\frac{S_x}{S_y}\approx 2.10}
\]
````

### Judge

| | |
|---|---|
| True answer | **2.363 dimensionless** |
| No-tool answer | **2.1 dimensionless** |
| Relative error | -11.1% |
| Verdict | **❌ INCORRECT** |
| Reasoning sound | False |
| Correct value, wrong reasoning | False |
| Accepted into benchmark | True |

**Decisive comparison:** The answer commits to k ≈ 2.10. The true value is 2.36328125, so the estimate is about 11% low, well outside the ±1% relative tolerance.

**Key discrepancy:** The 'ovalization amplification of approximately 3.1–3.2, including the sliding-interface friction correction' is an unexplained guess, not something derived. The answer never solves the three-layer contact problem: it does not model the onset of slip, the stick/slip partition under μ = 0.2, the interaction between the inner pressure p and the far-field stresses in setting σn, or the incremental accumulation of slip. As a result, the slip-versus-k relation, δθ ≈ 0.40(k−1) mm, is not supported, and the inferred k is wrong.

<sub>Provenance: runs run_0050, run_0054; columns ['slip_cc_45']; refined: True</sub>

---

## Q07

**Category:** Interface contact pressure distribution · **Type:** inverse · **Template:** `contact_traction|inverse`

### Question

A plane-strain cross-section of a cased wellbore consists of three concentric, linear isotropic elastic (small-strain) layers: a steel casing between r = 0.100 m and r = 0.106 m, a cement sheath between r = 0.106 m and r = 0.133 m, and a rock annulus between r = 0.133 m and r = 0.170 m. Polar coordinates (r, θ) are used, θ being measured counter-clockwise from the x axis; u_r denotes the radial displacement (outward positive) and u_θ the tangential displacement (positive towards increasing θ). Elastic constants (bulk modulus, shear modulus; these values are the model inputs to the digits shown, the E and ν values in brackets are rounded restatements): casing 175 GPa, 80.8 GPa (E ≈ 210.1 GPa, ν ≈ 0.300); cement 3.3333 GPa, 2.0 GPa (E = 5 GPa, ν = 0.25); rock 5.5556 GPa, 4.16667 GPa (E = 10 GPa, ν = 0.20). The body is represented by 8-node trilinear hexahedral elements (standard displacement formulation, full 2×2×2 Gauss integration): 80 uniform angular divisions over the quarter (1.125° each), 6, 10 and 10 elements of uniform radial size across the casing, cement and rock layers respectively, and a single element through a slab thickness of 0.1 m; elements are straight-sided with all nodes exactly on the circles, and each interface is a zero-thickness surface with matching, initially coincident nodes on both sides. Only the quarter 0° ≤ θ ≤ 90° is modelled, with roller (symmetry) conditions: zero normal displacement on θ = 0° and on θ = 90°. Plane strain: no axial displacement. The slab end faces carry zero axial displacement; there is no gravity and no inertia. The casing–cement interface (r = 0.106 m) and the cement–rock interface (r = 0.133 m) are imperfect frictional contacts. Both interfaces are initially in perfect contact, closed and sticking, without gap or pre-stress; they cannot interpenetrate, have no cohesion and no tensile strength, and transmit shear by dry friction with coefficient μ (no slip while |τ| < μ σn, sliding at |τ| = μ σn). Here σn is the compressive normal stress transmitted across the interface (positive in compression) and τ the shear stress on it; the static and kinetic friction coefficients are both μ and friction is rate-independent. The contact constraints are enforced exactly (no interface compliance): a closed interface has zero relative normal displacement and a sticking interface has zero relative tangential displacement. Kinematics are small-strain and small-sliding: loads, normals and contact pairs refer to the undeformed configuration, each node stays paired with its initially coincident partner, and the applied tractions are dead loads. The applied tractions use the unit normal of each straight-sided element face. The contact is face-based: each matching interface face pair carries one constant traction unknown (normal and shear components), and the contact and friction conditions are imposed per face pair on the face-averaged relative displacement, along that face's own unit normal and tangent. The bore pressure acts only on the surface r = 0.100 m and never enters an interface. The roller conditions apply to every node on θ = 0° and θ = 90°, including both sides of each interface. The stick/slip state is followed incrementally: each increment is a single implicit (backward-Euler) step solved to equilibrium from the converged state of the previous one, the stick/slip state and the slip increment being determined by the end-of-increment tractions, and slip accumulates. The friction coefficient is μ = 0.15 on both interfaces. The outer surface r = 0.17 m is loaded by the traction σ·n, where σ is the uniform stress state σxx = −Sx, σyy = −Sy, σxy = 0 and n is the outward unit normal. Here Sy = 5 MPa and Sx = 12.5 MPa, so that x is the direction of the larger compression. The inner surface carries a uniform compressive pressure p (a negative value of p denotes a uniform tensile normal traction). The value of p is not known; it lies between 1 MPa and 9 MPa. Loading is quasi-static and is applied in 10 equal increments, the outer traction and the inner pressure being ramped together, proportionally, from zero to their final values. The requested quantity refers to the final equilibrium state after increment 10. The system is initially stress-free. All displacements are initially zero. Define contact pressure = compressive normal stress transmitted across the interface (positive when compressive). On the discretised interface the contact pressure is constant over each interface face element (1.125° wide, one element through the thickness) and equal on both sides, so its average over a 1.125° segment is the value of the single face element covering that segment. The casing–cement contact pressure, averaged over the interface segment 88.875° ≤ θ ≤ 90° at r = 0.106 m (the segment adjacent to the θ = 90° symmetry plane), is measured in the final state as 9.637 MPa. Exactly one value in the stated interval reproduces this measurement. What is the inner pressure p, in MPa (in the interval 1 MPa ≤ p ≤ 9 MPa)? The answer is accepted within ±1 % (relative) of the true value.

### No-tool answer

_Model: GPT-5.6 Sol 1M · 87.85 s · tool calls: 0_

````text
Decompose the far-field compression into:

\[
S_m=\frac{S_x+S_y}{2}=8.75\ {\rm MPa},\qquad
S_d=\frac{S_x-S_y}{2}=3.75\ {\rm MPa}.
\]

For the axisymmetric component, the plane-strain concentric-cylinder solution gives the casing–cement pressure approximately as

\[
q_{cc}^{(0)} \approx 1.0169S_m+0.1683p
              =8.898+0.1683p\quad{\rm MPa}.
\]

The deviatoric loading ovalizes the relatively thin casing. A ring-compliance estimate, including the surrounding cement/rock resistance, predicts that the contact pressure near \(\theta=90^\circ\) is about \(0.10\) MPa below its axisymmetric value. Hence

\[
9.637 \approx 8.898+0.1683p-0.10.
\]

Solving,

\[
p\approx\frac{9.637-8.898+0.10}{0.1683}
 \approx 5.0\ {\rm MPa}.
\]

Indeed, \(p=5\) MPa gives an axisymmetric pressure of \(9.739\) MPa, requiring a plausible \(0.102\) MPa reduction from ovalization, frictional slip, and face averaging.

\[
\boxed{p \approx 5.0\ {\rm MPa}}
\]
````

### Judge

| | |
|---|---|
| True answer | **3.098 MPa** |
| No-tool answer | **5 MPa** |
| Relative error | +61.4% |
| Verdict | **❌ INCORRECT** |
| Reasoning sound | False |
| Correct value, wrong reasoning | False |
| Accepted into benchmark | True |

**Decisive comparison:** The answer commits to p ≈ 5.0 MPa, but the true value is 3.0977 MPa. That is about 61% too high, far outside the ±1% tolerance (roughly 3.067–3.129 MPa).

**Key discrepancy:** The answer asserts, without deriving it, that ovalization lowers the contact pressure at θ = 90° by about 0.10 MPa. Its own axisymmetric relation, 8.898 + 0.1683p, gives about 9.42 MPa at the true p ≈ 3.10 MPa. Reaching the measured 9.637 MPa therefore needs the non-axisymmetric part to raise the pressure by about 0.22 MPa near θ = 90°, not lower it. Because the coefficient on p is only 0.1683, this wrong-sign correction of about 0.3 MPa moves p by roughly 1.9 MPa. The axisymmetric coefficients are also stated without checking.

<sub>Provenance: runs run_0235, run_0234; columns ['pc_cc_90']; refined: True</sub>

---

## Q08

**Category:** Casing membrane stress · **Type:** inverse · **Template:** `stress|inverse`

### Question

A plane-strain cross-section of a cased wellbore consists of three concentric, linear isotropic elastic (small-strain) layers: a steel casing between r = 0.100 m and r = 0.106 m, a cement sheath between r = 0.106 m and r = 0.133 m, and a rock annulus between r = 0.133 m and r = 0.170 m. Polar coordinates (r, θ) are used, θ being measured counter-clockwise from the x axis; u_r denotes the radial displacement (outward positive) and u_θ the tangential displacement (positive towards increasing θ). Elastic constants (bulk modulus, shear modulus; these values are the model inputs to the digits shown, the E and ν values in brackets are rounded restatements): casing 175 GPa, 80.8 GPa (E ≈ 210.1 GPa, ν ≈ 0.300); cement 10.3 GPa, 6.45 GPa (E ≈ 16.01 GPa, ν ≈ 0.241); rock 5.5556 GPa, 4.16667 GPa (E = 10 GPa, ν = 0.20). The body is represented by 8-node trilinear hexahedral elements (standard displacement formulation, full 2×2×2 Gauss integration): 80 uniform angular divisions over the quarter (1.125° each), 6, 10 and 10 elements of uniform radial size across the casing, cement and rock layers respectively, and a single element through a slab thickness of 0.1 m; elements are straight-sided with all nodes exactly on the circles, and each interface is a zero-thickness surface with matching, initially coincident nodes on both sides. Only the quarter 0° ≤ θ ≤ 90° is modelled, with roller (symmetry) conditions: zero normal displacement on θ = 0° and on θ = 90°. Plane strain: no axial displacement. The slab end faces carry zero axial displacement; there is no gravity and no inertia. The casing–cement interface (r = 0.106 m) and the cement–rock interface (r = 0.133 m) are imperfect frictional contacts. Both interfaces are initially in perfect contact, closed and sticking, without gap or pre-stress; they cannot interpenetrate, have no cohesion and no tensile strength, and transmit shear by dry friction with coefficient μ (no slip while |τ| < μ σn, sliding at |τ| = μ σn). Here σn is the compressive normal stress transmitted across the interface (positive in compression) and τ the shear stress on it; the static and kinetic friction coefficients are both μ and friction is rate-independent. The contact constraints are enforced exactly (no interface compliance): a closed interface has zero relative normal displacement and a sticking interface has zero relative tangential displacement. Kinematics are small-strain and small-sliding: loads, normals and contact pairs refer to the undeformed configuration, each node stays paired with its initially coincident partner, and the applied tractions are dead loads. The applied tractions use the unit normal of each straight-sided element face. The contact is face-based: each matching interface face pair carries one constant traction unknown (normal and shear components), and the contact and friction conditions are imposed per face pair on the face-averaged relative displacement, along that face's own unit normal and tangent. The bore pressure acts only on the surface r = 0.100 m and never enters an interface. The roller conditions apply to every node on θ = 0° and θ = 90°, including both sides of each interface. The stick/slip state is followed incrementally: each increment is a single implicit (backward-Euler) step solved to equilibrium from the converged state of the previous one, the stick/slip state and the slip increment being determined by the end-of-increment tractions, and slip accumulates. The friction coefficient μ is the same on both interfaces but is not known; it lies between 0.12 and 0.29. The outer surface r = 0.17 m is loaded by the traction σ·n, where σ is the uniform stress state σxx = −Sx, σyy = −Sy, σxy = 0 and n is the outward unit normal. Here Sy = 5 MPa and Sx = 12.5 MPa, so that x is the direction of the larger compression. The inner surface carries a uniform compressive pressure p (a negative value of p denotes a uniform tensile normal traction). Here p = 6 MPa. Loading is quasi-static and is applied in 10 equal increments, the outer traction and the inner pressure being ramped together, proportionally, from zero to their final values. The requested quantity refers to the final equilibrium state after increment 10. The system is initially stress-free. All displacements are initially zero. The through-wall average hoop stress of the casing at θ ≈ 0° is the hoop stress σθθ (total stress, tension positive) averaged over the angular sector 0° ≤ θ ≤ 1.125° (adjacent to the θ = 0° plane) and uniformly with respect to radius across the full casing wall thickness. Concretely, each casing element's Cartesian stress is its Jacobian-weighted volume average over its 2×2×2 Gauss points, σθθ = σxx sin²θc + σyy cos²θc − 2 σxy sinθc cosθc is formed with the polar angle θc of the element centre (the mid-angle of its 1.125° sector), and the sector value is the arithmetic mean over the 6 casing elements of that sector (one per radial layer). In the final state this through-wall average hoop stress of the casing at θ ≈ 0° is measured as -34.20 MPa (tension positive). Exactly one value in the stated interval reproduces this measurement. What is the friction coefficient μ (in the interval 0.12 ≤ μ ≤ 0.29)? The answer is accepted within ±1 % (relative) of the true value.

### No-tool answer

_Model: GPT-5.6 Sol 1M · 54.41 s · tool calls: 0_

````text
The loading decomposes into:

- Mean compression: \((S_x+S_y)/2=8.75\) MPa
- Deviatoric component: \((S_x-S_y)/2=3.75\) MPa, producing interface shear proportional to \(\sin 2\theta\)

The mean response is essentially independent of friction. Friction controls transmission of the deviatoric load through the cement to the casing. Since the loading is proportional and Coulomb friction is homogeneous, the same partial-slip pattern develops throughout the ramp; the ten increments primarily track accumulated slip.

Matching the measured casing hoop stress, \(-34.20\) MPa, to the partial-slip annular response gives the estimated coefficient

\[
\boxed{\mu \approx 0.20}
\]

The exact value would require solving the stated face-based finite-element contact problem, but the predicted value is \(0.20\), within the requested tolerance.
````

### Judge

| | |
|---|---|
| True answer | **0.2676 dimensionless** |
| No-tool answer | **0.2 dimensionless** |
| Relative error | -25.3% |
| Verdict | **❌ INCORRECT** |
| Reasoning sound | False |
| Correct value, wrong reasoning | False |
| Accepted into benchmark | True |

**Decisive comparison:** The answer gives μ ≈ 0.20, but the true value is 0.267578125. That is about 25% too low, far outside the ±1% relative tolerance (roughly 0.2649 to 0.2703).

**Key discrepancy:** The answer never calculates how the casing hoop stress at θ ≈ 0° depends on μ. It describes the load split and the partial-slip behaviour in words, then states μ ≈ 0.20 without any calculation tying it to −34.20 MPa. The value is close to the middle of the allowed range (0.205), so it is effectively a guess. The answer also says the result is within tolerance with nothing to support that.

<sub>Provenance: runs run_0074, run_0094; columns ['shoop_cas_wallavg_0']; refined: True</sub>

---

## Q09

**Category:** Friction-controlled casing ovalization · **Type:** threshold · **Template:** `displacement|threshold`

### Question

A plane-strain cross-section of a cased wellbore consists of three concentric, linear isotropic elastic (small-strain) layers: a steel casing between r = 0.100 m and r = 0.106 m, a cement sheath between r = 0.106 m and r = 0.133 m, and a rock annulus between r = 0.133 m and r = 0.170 m. Polar coordinates (r, θ) are used, θ being measured counter-clockwise from the x axis; u_r denotes the radial displacement (outward positive) and u_θ the tangential displacement (positive towards increasing θ). Elastic constants (bulk modulus, shear modulus; these values are the model inputs to the digits shown, the E and ν values in brackets are rounded restatements): casing 175 GPa, 80.8 GPa (E ≈ 210.1 GPa, ν ≈ 0.300); cement 10.3 GPa, 6.45 GPa (E ≈ 16.01 GPa, ν ≈ 0.241); rock 5.5556 GPa, 4.16667 GPa (E = 10 GPa, ν = 0.20). The body is represented by 8-node trilinear hexahedral elements (standard displacement formulation, full 2×2×2 Gauss integration): 80 uniform angular divisions over the quarter (1.125° each), 6, 10 and 10 elements of uniform radial size across the casing, cement and rock layers respectively, and a single element through a slab thickness of 0.1 m; elements are straight-sided with all nodes exactly on the circles, and each interface is a zero-thickness surface with matching, initially coincident nodes on both sides. Only the quarter 0° ≤ θ ≤ 90° is modelled, with roller (symmetry) conditions: zero normal displacement on θ = 0° and on θ = 90°. Plane strain: no axial displacement. The slab end faces carry zero axial displacement; there is no gravity and no inertia. The casing–cement interface (r = 0.106 m) and the cement–rock interface (r = 0.133 m) are imperfect frictional contacts. Both interfaces are initially in perfect contact, closed and sticking, without gap or pre-stress; they cannot interpenetrate, have no cohesion and no tensile strength, and transmit shear by dry friction with coefficient μ (no slip while |τ| < μ σn, sliding at |τ| = μ σn). Here σn is the compressive normal stress transmitted across the interface (positive in compression) and τ the shear stress on it; the static and kinetic friction coefficients are both μ and friction is rate-independent. The contact constraints are enforced exactly (no interface compliance): a closed interface has zero relative normal displacement and a sticking interface has zero relative tangential displacement. Kinematics are small-strain and small-sliding: loads, normals and contact pairs refer to the undeformed configuration, each node stays paired with its initially coincident partner, and the applied tractions are dead loads. The applied tractions use the unit normal of each straight-sided element face. The contact is face-based: each matching interface face pair carries one constant traction unknown (normal and shear components), and the contact and friction conditions are imposed per face pair on the face-averaged relative displacement, along that face's own unit normal and tangent. The bore pressure acts only on the surface r = 0.100 m and never enters an interface. The roller conditions apply to every node on θ = 0° and θ = 90°, including both sides of each interface. The stick/slip state is followed incrementally: each increment is a single implicit (backward-Euler) step solved to equilibrium from the converged state of the previous one, the stick/slip state and the slip increment being determined by the end-of-increment tractions, and slip accumulates. The friction coefficient μ is the same on both interfaces and can be chosen in the interval 0.13 ≤ μ ≤ 0.30. The outer surface r = 0.17 m is loaded by the traction σ·n, where σ is the uniform stress state σxx = −Sx, σyy = −Sy, σxy = 0 and n is the outward unit normal. Here Sy = 5 MPa and Sx = 12.5 MPa, so that x is the direction of the larger compression. The inner surface carries a uniform compressive pressure p (a negative value of p denotes a uniform tensile normal traction). Here p = 10 MPa. Loading is quasi-static and is applied in 10 equal increments in two stages: during increments 1–5 the outer traction is ramped linearly from zero to its final value with zero inner pressure; during increments 6–10 the outer traction is held at its final value while the inner pressure is ramped linearly from zero to its final value. The requested quantity refers to the final equilibrium state after increment 10. The system is initially stress-free. All displacements are initially zero. Let ΔD_x = 2 u_r(r = 0.100 m, θ = 0°) be the change of the casing inner diameter along x (negative when the bore shortens). What is the smallest friction coefficient μ in the interval 0.13 ≤ μ ≤ 0.30 for which the shortening of the bore diameter along x in the final state, −ΔD_x, does not exceed 4.950 mm? The answer is accepted within ±1 % (relative) of the true value.

### No-tool answer

_Model: GPT-5.6 Sol 1M · 99.12 s · tool calls: 0_

````text
The bore shortening decreases as μ increases because friction couples the layers tangentially, increasing their effective ovalization stiffness.

A thin-ring estimate for the rock’s \(n=2\) deformation gives

\[
w_2 \sim \frac{qR^4}{9D},\qquad
D=\frac{Et^3}{12},
\]

with \(q=(S_x-S_y)/2=3.75\) MPa, \(R\approx0.1515\) m, and \(t=0.037\) m. This gives \(w_2\approx5.2\) mm for the uncoupled rock alone, confirming that millimetre-scale ovalization is plausible. The cement and casing bending stiffnesses reduce this, while friction provides additional composite action.

The shear-to-normal traction ratios needed for sufficient coupling are approximately \(0.18\)–\(0.22\). Accounting for slip accumulated during the initial outer-loading stage, the estimated crossing of

\[
-\Delta D_x=4.950\ {\rm mm}
\]

occurs at

\[
\boxed{\mu_{\min}\approx 0.20}.
\]

This is an estimate; the exact value depends on the specified facewise finite-element contact solution.
````

### Judge

| | |
|---|---|
| True answer | **0.1746 dimensionless** |
| No-tool answer | **0.2 dimensionless** |
| Relative error | +14.5% |
| Verdict | **❌ INCORRECT** |
| Reasoning sound | False |
| Correct value, wrong reasoning | False |
| Accepted into benchmark | True |

**Decisive comparison:** The answer commits to μ_min ≈ 0.20. The true value is 0.1746, and the ±1% relative tolerance allows roughly 0.1729 to 0.1764, so 0.20 is about 14.5% too high and falls outside the window.

**Key discrepancy:** The final μ is not derived from the reasoning. The thin-ring estimate covers only the n=2 ovalization of the rock layer on its own (≈5.2 mm). It does not link the friction coefficient to the 4.950 mm threshold. The 0.18–0.22 range of shear-to-normal traction ratios is stated without calculation, and picking 0.20 amounts to guessing near the middle of that range. The answer never models the staged loading, how slip builds up from the outer-loading stage, or how the bore pressure stage relieves shortening, so its value does not match the simulated threshold of μ ≈ 0.1746.

<sub>Provenance: runs run_0133, run_0153; columns ['dDx_cas_in']; refined: True</sub>

---

## Q10

**Category:** Interface slip partition · **Type:** threshold · **Template:** `displacement_jump|threshold`

### Question

A plane-strain cross-section of a cased wellbore consists of three concentric, linear isotropic elastic (small-strain) layers: a steel casing between r = 0.100 m and r = 0.106 m, a cement sheath between r = 0.106 m and r = 0.133 m, and a rock annulus between r = 0.133 m and r = 0.170 m. Polar coordinates (r, θ) are used, θ being measured counter-clockwise from the x axis; u_r denotes the radial displacement (outward positive) and u_θ the tangential displacement (positive towards increasing θ). Elastic constants (bulk modulus, shear modulus; these values are the model inputs to the digits shown, the E and ν values in brackets are rounded restatements): casing 175 GPa, 80.8 GPa (E ≈ 210.1 GPa, ν ≈ 0.300); cement 3.3333 GPa, 2.0 GPa (E = 5 GPa, ν = 0.25); rock 5.5556 GPa, 4.16667 GPa (E = 10 GPa, ν = 0.20). The body is represented by 8-node trilinear hexahedral elements (standard displacement formulation, full 2×2×2 Gauss integration): 80 uniform angular divisions over the quarter (1.125° each), 6, 10 and 10 elements of uniform radial size across the casing, cement and rock layers respectively, and a single element through a slab thickness of 0.1 m; elements are straight-sided with all nodes exactly on the circles, and each interface is a zero-thickness surface with matching, initially coincident nodes on both sides. Only the quarter 0° ≤ θ ≤ 90° is modelled, with roller (symmetry) conditions: zero normal displacement on θ = 0° and on θ = 90°. Plane strain: no axial displacement. The slab end faces carry zero axial displacement; there is no gravity and no inertia. The casing–cement interface (r = 0.106 m) and the cement–rock interface (r = 0.133 m) are imperfect frictional contacts. Both interfaces are initially in perfect contact, closed and sticking, without gap or pre-stress; they cannot interpenetrate, have no cohesion and no tensile strength, and transmit shear by dry friction with coefficient μ (no slip while |τ| < μ σn, sliding at |τ| = μ σn). Here σn is the compressive normal stress transmitted across the interface (positive in compression) and τ the shear stress on it; the static and kinetic friction coefficients are both μ and friction is rate-independent. The contact constraints are enforced exactly (no interface compliance): a closed interface has zero relative normal displacement and a sticking interface has zero relative tangential displacement. Kinematics are small-strain and small-sliding: loads, normals and contact pairs refer to the undeformed configuration, each node stays paired with its initially coincident partner, and the applied tractions are dead loads. The applied tractions use the unit normal of each straight-sided element face. The contact is face-based: each matching interface face pair carries one constant traction unknown (normal and shear components), and the contact and friction conditions are imposed per face pair on the face-averaged relative displacement, along that face's own unit normal and tangent. The bore pressure acts only on the surface r = 0.100 m and never enters an interface. The roller conditions apply to every node on θ = 0° and θ = 90°, including both sides of each interface. The stick/slip state is followed incrementally: each increment is a single implicit (backward-Euler) step solved to equilibrium from the converged state of the previous one, the stick/slip state and the slip increment being determined by the end-of-increment tractions, and slip accumulates. The friction coefficient is μ = 0.2 on both interfaces. The outer surface r = 0.17 m is loaded by the traction σ·n, where σ is the uniform stress state σxx = −Sx, σyy = −Sy, σxy = 0 and n is the outward unit normal. Here Sy = 5 MPa and Sx = k·Sy, where the stress ratio k ≥ 1 can be chosen in the interval 1.9 ≤ k ≤ 2.9 (x is the direction of the larger compression). The inner surface carries a uniform compressive pressure p (a negative value of p denotes a uniform tensile normal traction). Here p = 2 MPa. Loading is quasi-static and is applied in 10 equal increments, the outer traction and the inner pressure being ramped together, proportionally, from zero to their final values. The requested quantity refers to the final equilibrium state after increment 10. The system is initially stress-free. All displacements are initially zero. The slip across the cement–rock interface at θ = 45° is defined as u_θ of the rock-side point at r = 0.133 m, θ = 45° minus u_θ of the cement-side point at the same position. Here u_θ = −u_x sin θ + u_y cos θ with θ = 45°. This slip is positive for every k in the interval. What is the largest stress ratio k = Sx/Sy in the interval 1.9 ≤ k ≤ 2.9 for which this cement–rock slip at θ = 45° in the final state does not exceed 0.900 mm? The answer is accepted within ±1 % (relative) of the true value.

### No-tool answer

_Model: GPT-5.6 Sol 1M · 95.82 s · tool calls: 0_

````text
Decompose the outer loading into:

\[
P=\frac{S_x+S_y}{2}=2.5(k+1)\ {\rm MPa},
\qquad
D=\frac{S_x-S_y}{2}=2.5(k-1)\ {\rm MPa}.
\]

The mean component \(P\), together with bore pressure, supplies interface compression and thus frictional resistance. The deviatoric \(n=2\) component \(D\) causes ovalization; its tangential effect is maximal at \(45^\circ\).

Using layered-annulus \(n=0/n=2\) elastic compliance and limiting the interface shear by \(|\tau|=0.2\sigma_n\), the estimated final cement–rock slip crosses \(0.900\) mm near

\[
k \simeq 2.40.
\]

At this point \(P=8.5\) MPa and \(D=3.5\) MPa. Slip increases monotonically with \(k\), so the requested largest ratio is:

\[
\boxed{k_{\max}\approx 2.40}
\]

This is an analytical/reduced-order estimate; the face-based finite-element/contact discretization could shift the last digits slightly.
````

### Judge

| | |
|---|---|
| True answer | **2.145 dimensionless** |
| No-tool answer | **2.4 dimensionless** |
| Relative error | +11.9% |
| Verdict | **❌ INCORRECT** |
| Reasoning sound | False |
| Correct value, wrong reasoning | False |
| Accepted into benchmark | True |

**Decisive comparison:** The answer gives k ≈ 2.40. The true value is 2.14453125, so the answer is about 11.9% too high, well outside the ±1% relative tolerance (about 2.123 to 2.166).

**Key discrepancy:** The answer names a layered-annulus n=0/n=2 compliance analysis with a friction limit but never computes the slip. It shows no calculation of how slip depends on k, so 2.40 is a guess, and it overestimates the threshold.

<sub>Provenance: runs run_0251, run_0255; columns ['slip_cr_45']; refined: True</sub>

---

## Q11

**Category:** Casing membrane stress · **Type:** threshold · **Template:** `stress|threshold`

### Question

A plane-strain cross-section of a cased wellbore consists of three concentric, linear isotropic elastic (small-strain) layers: a steel casing between r = 0.100 m and r = 0.106 m, a cement sheath between r = 0.106 m and r = 0.133 m, and a rock annulus between r = 0.133 m and r = 0.170 m. Polar coordinates (r, θ) are used, θ being measured counter-clockwise from the x axis; u_r denotes the radial displacement (outward positive) and u_θ the tangential displacement (positive towards increasing θ). Elastic constants (bulk modulus, shear modulus; these values are the model inputs to the digits shown, the E and ν values in brackets are rounded restatements): casing 175 GPa, 80.8 GPa (E ≈ 210.1 GPa, ν ≈ 0.300); cement 10.3 GPa, 6.45 GPa (E ≈ 16.01 GPa, ν ≈ 0.241); rock 5.5556 GPa, 4.16667 GPa (E = 10 GPa, ν = 0.20). The body is represented by 8-node trilinear hexahedral elements (standard displacement formulation, full 2×2×2 Gauss integration): 80 uniform angular divisions over the quarter (1.125° each), 6, 10 and 10 elements of uniform radial size across the casing, cement and rock layers respectively, and a single element through a slab thickness of 0.1 m; elements are straight-sided with all nodes exactly on the circles, and each interface is a zero-thickness surface with matching, initially coincident nodes on both sides. Only the quarter 0° ≤ θ ≤ 90° is modelled, with roller (symmetry) conditions: zero normal displacement on θ = 0° and on θ = 90°. Plane strain: no axial displacement. The slab end faces carry zero axial displacement; there is no gravity and no inertia. The casing–cement interface (r = 0.106 m) and the cement–rock interface (r = 0.133 m) are imperfect frictional contacts. Both interfaces are initially in perfect contact, closed and sticking, without gap or pre-stress; they cannot interpenetrate, have no cohesion and no tensile strength, and transmit shear by dry friction with coefficient μ (no slip while |τ| < μ σn, sliding at |τ| = μ σn). Here σn is the compressive normal stress transmitted across the interface (positive in compression) and τ the shear stress on it; the static and kinetic friction coefficients are both μ and friction is rate-independent. The contact constraints are enforced exactly (no interface compliance): a closed interface has zero relative normal displacement and a sticking interface has zero relative tangential displacement. Kinematics are small-strain and small-sliding: loads, normals and contact pairs refer to the undeformed configuration, each node stays paired with its initially coincident partner, and the applied tractions are dead loads. The applied tractions use the unit normal of each straight-sided element face. The contact is face-based: each matching interface face pair carries one constant traction unknown (normal and shear components), and the contact and friction conditions are imposed per face pair on the face-averaged relative displacement, along that face's own unit normal and tangent. The bore pressure acts only on the surface r = 0.100 m and never enters an interface. The roller conditions apply to every node on θ = 0° and θ = 90°, including both sides of each interface. The stick/slip state is followed incrementally: each increment is a single implicit (backward-Euler) step solved to equilibrium from the converged state of the previous one, the stick/slip state and the slip increment being determined by the end-of-increment tractions, and slip accumulates. The friction coefficient is μ = 0.2 on both interfaces. The outer surface r = 0.17 m is loaded by the traction σ·n, where σ is the uniform stress state σxx = −Sx, σyy = −Sy, σxy = 0 and n is the outward unit normal. Here Sy = 5 MPa and Sx = 10 MPa, so that x is the direction of the larger compression. The inner surface carries a uniform compressive pressure p (a negative value of p denotes a uniform tensile normal traction). The value of p can be chosen in the interval 3 MPa ≤ p ≤ 9.5 MPa. Loading is quasi-static and is applied in 10 equal increments, the outer traction and the inner pressure being ramped together, proportionally, from zero to their final values. The requested quantity refers to the final equilibrium state after increment 10. The system is initially stress-free. All displacements are initially zero. The through-wall average hoop stress of the casing at θ ≈ 0° is the hoop stress σθθ (total stress, tension positive) averaged over the angular sector 0° ≤ θ ≤ 1.125° (adjacent to the θ = 0° plane) and uniformly with respect to radius across the full casing wall thickness. Concretely, each casing element's Cartesian stress is its Jacobian-weighted volume average over its 2×2×2 Gauss points, σθθ = σxx sin²θc + σyy cos²θc − 2 σxy sinθc cosθc is formed with the polar angle θc of the element centre (the mid-angle of its 1.125° sector), and the sector value is the arithmetic mean over the 6 casing elements of that sector (one per radial layer). What is the lowest inner pressure p in the interval 3 MPa ≤ p ≤ 9.5 MPa for which this through-wall average hoop stress of the casing at θ ≈ 0° in the final state is tensile (≥ 0), in MPa? The answer is accepted within ±1 % (relative) of the true value.

### No-tool answer

_Model: GPT-5.6 Sol 1M · 188.39 s · tool calls: 0_

````text
The casing’s axisymmetric outer contact pressure is approximately

\[
q_1 \simeq 7.00+0.2738p\quad\text{MPa}.
\]

The corresponding through-wall average casing hoop stress is

\[
\bar\sigma_{\theta\theta}^{(0)}
=\frac{0.100p-0.106q_1}{0.006}
\simeq 11.83p-123.7\quad\text{MPa}.
\]

The far-field stress anisotropy drives tangential slip over most of the interfaces. With \(\mu=0.2\), the casing–cement shear traction near the transition is limited to roughly

\[
\mu q_1\approx 1.9\ \text{MPa}.
\]

Ring equilibrium, including the small sticking regions near the symmetry planes, gives an estimated tensile deviatoric contribution at \(\theta\simeq0^\circ\) of about \(23\) MPa. Thus the zero crossing satisfies approximately

\[
11.83p-123.7+23\simeq0,
\]

giving

\[
\boxed{p_{\min}\approx 8.5\ \text{MPa}}.
\]

This is an analytical estimate; the precise face-based finite-element/contact result should be close to \(8.5\) MPa.
````

### Judge

| | |
|---|---|
| True answer | **8.141 MPa** |
| No-tool answer | **8.5 MPa** |
| Relative error | +4.4% |
| Verdict | **❌ INCORRECT** |
| Reasoning sound | False |
| Correct value, wrong reasoning | False |
| Accepted into benchmark | True |

**Decisive comparison:** The answer commits to p_min ≈ 8.5 MPa, but the true value is 8.140625 MPa. That is a relative deviation of about 4.4 %, well outside the ±1 % tolerance.

**Key discrepancy:** The answer never derives the anisotropic (deviatoric) contribution to the casing hoop stress at θ≈0°. It asserts a value of 'about 23 MPa' from vague ring-equilibrium and slip arguments, without solving the frictional stick/slip contact problem, and it does not model the face-based FE discretization or the incremental slip history. Because of that unsupported number, the zero crossing lands about 0.36 MPa too high.

<sub>Provenance: runs run_0050, run_0049; columns ['shoop_cas_wallavg_0']; refined: True</sub>

---

## Q12

**Category:** Load-sequence (path) effects · **Type:** choice · **Template:** `displacement|choice`

### Question

A plane-strain cross-section of a cased wellbore consists of three concentric, linear isotropic elastic (small-strain) layers: a steel casing between r = 0.100 m and r = 0.106 m, a cement sheath between r = 0.106 m and r = 0.133 m, and a rock annulus between r = 0.133 m and r = 0.170 m. Polar coordinates (r, θ) are used, θ being measured counter-clockwise from the x axis; u_r denotes the radial displacement (outward positive) and u_θ the tangential displacement (positive towards increasing θ). Elastic constants (bulk modulus, shear modulus; these values are the model inputs to the digits shown, the E and ν values in brackets are rounded restatements): casing 175 GPa, 80.8 GPa (E ≈ 210.1 GPa, ν ≈ 0.300); cement 10.3 GPa, 6.45 GPa (E ≈ 16.01 GPa, ν ≈ 0.241); rock 5.5556 GPa, 4.16667 GPa (E = 10 GPa, ν = 0.20). The body is represented by 8-node trilinear hexahedral elements (standard displacement formulation, full 2×2×2 Gauss integration): 80 uniform angular divisions over the quarter (1.125° each), 6, 10 and 10 elements of uniform radial size across the casing, cement and rock layers respectively, and a single element through a slab thickness of 0.1 m; elements are straight-sided with all nodes exactly on the circles, and each interface is a zero-thickness surface with matching, initially coincident nodes on both sides. Only the quarter 0° ≤ θ ≤ 90° is modelled, with roller (symmetry) conditions: zero normal displacement on θ = 0° and on θ = 90°. Plane strain: no axial displacement. The slab end faces carry zero axial displacement; there is no gravity and no inertia. The casing–cement interface (r = 0.106 m) and the cement–rock interface (r = 0.133 m) are imperfect frictional contacts. Both interfaces are initially in perfect contact, closed and sticking, without gap or pre-stress; they cannot interpenetrate, have no cohesion and no tensile strength, and transmit shear by dry friction with coefficient μ (no slip while |τ| < μ σn, sliding at |τ| = μ σn). Here σn is the compressive normal stress transmitted across the interface (positive in compression) and τ the shear stress on it; the static and kinetic friction coefficients are both μ and friction is rate-independent. The contact constraints are enforced exactly (no interface compliance): a closed interface has zero relative normal displacement and a sticking interface has zero relative tangential displacement. Kinematics are small-strain and small-sliding: loads, normals and contact pairs refer to the undeformed configuration, each node stays paired with its initially coincident partner, and the applied tractions are dead loads. The applied tractions use the unit normal of each straight-sided element face. The contact is face-based: each matching interface face pair carries one constant traction unknown (normal and shear components), and the contact and friction conditions are imposed per face pair on the face-averaged relative displacement, along that face's own unit normal and tangent. The bore pressure acts only on the surface r = 0.100 m and never enters an interface. The roller conditions apply to every node on θ = 0° and θ = 90°, including both sides of each interface. The stick/slip state is followed incrementally: each increment is a single implicit (backward-Euler) step solved to equilibrium from the converged state of the previous one, the stick/slip state and the slip increment being determined by the end-of-increment tractions, and slip accumulates. The friction coefficient is μ = 0.25 on both interfaces. The outer surface r = 0.17 m is loaded by the traction σ·n, where σ is the uniform stress state σxx = −Sx, σyy = −Sy, σxy = 0 and n is the outward unit normal. Here Sy = 5 MPa and Sx = 7.5 MPa, so that x is the direction of the larger compression. The inner surface carries a uniform compressive pressure p (a negative value of p denotes a uniform tensile normal traction). Two final values of p are compared: p = 2 MPa and p = 10 MPa. Two load sequences are considered, each quasi-static and applied in 10 equal increments: in the proportional sequence the outer traction and the inner pressure are ramped together, proportionally, from zero to their final values; in the staged sequence the outer traction is ramped linearly from zero to its final value during increments 1–5 with zero inner pressure and is then held at its final value while the inner pressure is ramped linearly from zero to its final value during increments 6–10. All quantities below refer to the final equilibrium state after increment 10. The system is initially stress-free. All displacements are initially zero. Let ΔD_x = 2 u_r(r = 0.100 m, θ = 0°) and ΔD_y = 2 u_r(r = 0.100 m, θ = 90°) be the changes of the casing inner diameter along x and along y, and call ΔD_y − ΔD_x the ovalization of the casing bore. The ovalization is positive in all four cases. Consider the relative change of the ovalization ΔD_y − ΔD_x when the final inner pressure is raised from p = 2 MPa to p = 10 MPa (all else unchanged), evaluated separately for the proportional and for the staged sequence (change relative to the p = 2 MPa value of the same sequence). Which statement is correct? A. It changes by less than 5 % under both sequences. B. It decreases by more than 5 % under the proportional sequence but changes by less than 5 % under the staged sequence. C. It decreases by more than 5 % under both sequences. D. It changes by less than 5 % under the proportional sequence but decreases by more than 5 % under the staged sequence. Answer with one letter.

**Options and evidence from the simulations:**

- **A**  (naive): It changes by less than 5 % under both sequences.  
  _False: proportional change = -17.46 % (1.9612 mm → 1.6189 mm)._
- **B** (correct): It decreases by more than 5 % under the proportional sequence but changes by less than 5 % under the staged sequence.  
  _True: proportional -17.46 % (< −5 %); staged 0.0000 % (2.0456 mm → 2.0456 mm, |change| < 5 %)._
- **C** : It decreases by more than 5 % under both sequences.  
  _False: staged change = 0.0000 %, not a decrease > 5 %._
- **D** : It changes by less than 5 % under the proportional sequence but decreases by more than 5 % under the staged sequence.  
  _False: proportional change -17.46 % is a decrease > 5 % and staged change 0.0000 % is not._

### No-tool answer

_Model: GPT-5.6 Sol 1M · 27.68 s · tool calls: 0_

````text
B
````

### Judge

| | |
|---|---|
| True answer | **B** |
| No-tool answer | **B** |
| Relative error | – |
| Verdict | **✅ CORRECT** |
| Reasoning sound | False |
| Correct value, wrong reasoning | True |
| Accepted into benchmark | False |

**Decisive comparison:** The answer chooses B, which matches the correct option. In the simulation, the ovalization drops by 17.46 % under the proportional sequence (1.9612 mm to 1.6189 mm) and changes by 0.0000 % under the staged sequence (2.0456 mm to 2.0456 mm).

**Key discrepancy:** There is no wrong value. The answer is a bare letter with no reasoning, so nothing shows why the uniform bore pressure leaves the ovalization unchanged in the staged sequence but reduces it in the proportional one.

<sub>Provenance: runs run_0063, run_0061, run_0163, run_0161; columns ['oval_cas_in']; refined: False</sub>

---

## Q13

**Category:** Interface slip partition · **Type:** choice · **Template:** `displacement_jump|choice`

### Question

A plane-strain cross-section of a cased wellbore consists of three concentric, linear isotropic elastic (small-strain) layers: a steel casing between r = 0.100 m and r = 0.106 m, a cement sheath between r = 0.106 m and r = 0.133 m, and a rock annulus between r = 0.133 m and r = 0.170 m. Polar coordinates (r, θ) are used, θ being measured counter-clockwise from the x axis; u_r denotes the radial displacement (outward positive) and u_θ the tangential displacement (positive towards increasing θ). Elastic constants (bulk modulus, shear modulus; these values are the model inputs to the digits shown, the E and ν values in brackets are rounded restatements): casing 175 GPa, 80.8 GPa (E ≈ 210.1 GPa, ν ≈ 0.300); cement 10.3 GPa, 6.45 GPa (E ≈ 16.01 GPa, ν ≈ 0.241); rock 5.5556 GPa, 4.16667 GPa (E = 10 GPa, ν = 0.20). The body is represented by 8-node trilinear hexahedral elements (standard displacement formulation, full 2×2×2 Gauss integration): 80 uniform angular divisions over the quarter (1.125° each), 6, 10 and 10 elements of uniform radial size across the casing, cement and rock layers respectively, and a single element through a slab thickness of 0.1 m; elements are straight-sided with all nodes exactly on the circles, and each interface is a zero-thickness surface with matching, initially coincident nodes on both sides. Only the quarter 0° ≤ θ ≤ 90° is modelled, with roller (symmetry) conditions: zero normal displacement on θ = 0° and on θ = 90°. Plane strain: no axial displacement. The slab end faces carry zero axial displacement; there is no gravity and no inertia. The casing–cement interface (r = 0.106 m) and the cement–rock interface (r = 0.133 m) are imperfect frictional contacts. Both interfaces are initially in perfect contact, closed and sticking, without gap or pre-stress; they cannot interpenetrate, have no cohesion and no tensile strength, and transmit shear by dry friction with coefficient μ (no slip while |τ| < μ σn, sliding at |τ| = μ σn). Here σn is the compressive normal stress transmitted across the interface (positive in compression) and τ the shear stress on it; the static and kinetic friction coefficients are both μ and friction is rate-independent. The contact constraints are enforced exactly (no interface compliance): a closed interface has zero relative normal displacement and a sticking interface has zero relative tangential displacement. Kinematics are small-strain and small-sliding: loads, normals and contact pairs refer to the undeformed configuration, each node stays paired with its initially coincident partner, and the applied tractions are dead loads. The applied tractions use the unit normal of each straight-sided element face. The contact is face-based: each matching interface face pair carries one constant traction unknown (normal and shear components), and the contact and friction conditions are imposed per face pair on the face-averaged relative displacement, along that face's own unit normal and tangent. The bore pressure acts only on the surface r = 0.100 m and never enters an interface. The roller conditions apply to every node on θ = 0° and θ = 90°, including both sides of each interface. The stick/slip state is followed incrementally: each increment is a single implicit (backward-Euler) step solved to equilibrium from the converged state of the previous one, the stick/slip state and the slip increment being determined by the end-of-increment tractions, and slip accumulates. Two values of the friction coefficient (the same on both interfaces) are compared: μ = 0.10 and μ = 0.30. The outer surface r = 0.17 m is loaded by the traction σ·n, where σ is the uniform stress state σxx = −Sx, σyy = −Sy, σxy = 0 and n is the outward unit normal. Here Sy = 5 MPa and Sx = 7.5 MPa, so that x is the direction of the larger compression. The inner surface carries a uniform compressive pressure p (a negative value of p denotes a uniform tensile normal traction). Here p = 6 MPa. Loading is quasi-static and is applied in 10 equal increments, the outer traction and the inner pressure being ramped together, proportionally, from zero to their final values. All quantities below refer to the final equilibrium state after increment 10. The system is initially stress-free. All displacements are initially zero. The slip across the casing–cement interface at θ = 45° is defined as u_θ of the cement-side point at r = 0.106 m, θ = 45° minus u_θ of the casing-side point at the same position. The slip across the cement–rock interface at θ = 45° is defined as u_θ of the rock-side point at r = 0.133 m, θ = 45° minus u_θ of the cement-side point at the same position. Here u_θ = −u_x sin θ + u_y cos θ with θ = 45°. Both slips are taken at the interface nodes at θ = 45°, and all four slips (two interfaces, two friction coefficients) are positive. Compare the two slips at θ = 45° in the final state for μ = 0.10 and for μ = 0.30, and the ratio (cement–rock slip)/(casing–cement slip) between the two friction coefficients (relative change from μ = 0.10 to μ = 0.30). Which statement is correct? A. At both friction coefficients the casing–cement slip exceeds the cement–rock slip. B. At both friction coefficients the cement–rock slip exceeds the casing–cement slip, and the ratio changes by less than 5 %. C. At both friction coefficients the cement–rock slip exceeds the casing–cement slip, and the ratio increases by more than 5 %. D. At both friction coefficients the cement–rock slip exceeds the casing–cement slip, and the ratio decreases by more than 5 %. Answer with one letter.

**Options and evidence from the simulations:**

- **A**  (naive): At both friction coefficients the casing–cement slip exceeds the cement–rock slip.  
  _False: cement–rock slip exceeds casing–cement slip by 68.1 % (μ=0.10: 266.9 um vs 158.8 um) and 37.5 % (μ=0.30: 98.9 um vs 72.0 um)._
- **B** : At both friction coefficients the cement–rock slip exceeds the casing–cement slip, and the ratio changes by less than 5 %.  
  _False: ratio changes by -18.24 % (|change| > 5 %)._
- **C** : At both friction coefficients the cement–rock slip exceeds the casing–cement slip, and the ratio increases by more than 5 %.  
  _False: ratio decreases (-18.24 %)._
- **D** (correct): At both friction coefficients the cement–rock slip exceeds the casing–cement slip, and the ratio decreases by more than 5 %.  
  _True: ratio 1.6814 → 1.3746, change -18.24 % (< −5 %), cement–rock slip larger at both μ._

### No-tool answer

_Model: GPT-5.6 Sol 1M · 69.85 s · tool calls: 0_

````text
D
````

### Judge

| | |
|---|---|
| True answer | **D** |
| No-tool answer | **D** |
| Relative error | – |
| Verdict | **✅ CORRECT** |
| Reasoning sound | False |
| Correct value, wrong reasoning | True |
| Accepted into benchmark | False |

**Decisive comparison:** The answer commits to D, which matches the key's correct option D. In the simulation the cement–rock slip is larger than the casing–cement slip at both friction coefficients (266.9 vs 158.8 µm at μ=0.10 and 98.9 vs 72.0 µm at μ=0.30), and the ratio falls from 1.6814 to 1.3746, a change of −18.24 %.

**Key discrepancy:** There is no discrepancy in the letter. The answer is a bare letter with no reasoning given, so its reasoning cannot be judged sound.

<sub>Provenance: runs run_0002, run_0082; columns ['slip_cc_45', 'slip_cr_45']; refined: False</sub>

---

## Q14

**Category:** Interface contact pressure distribution · **Type:** choice · **Template:** `contact_traction|choice`

### Question

A plane-strain cross-section of a cased wellbore consists of three concentric, linear isotropic elastic (small-strain) layers: a steel casing between r = 0.100 m and r = 0.106 m, a cement sheath between r = 0.106 m and r = 0.133 m, and a rock annulus between r = 0.133 m and r = 0.170 m. Polar coordinates (r, θ) are used, θ being measured counter-clockwise from the x axis; u_r denotes the radial displacement (outward positive) and u_θ the tangential displacement (positive towards increasing θ). Elastic constants (bulk modulus, shear modulus; these values are the model inputs to the digits shown, the E and ν values in brackets are rounded restatements): casing 175 GPa, 80.8 GPa (E ≈ 210.1 GPa, ν ≈ 0.300); cement 10.3 GPa, 6.45 GPa (E ≈ 16.01 GPa, ν ≈ 0.241); rock 5.5556 GPa, 4.16667 GPa (E = 10 GPa, ν = 0.20). The body is represented by 8-node trilinear hexahedral elements (standard displacement formulation, full 2×2×2 Gauss integration): 80 uniform angular divisions over the quarter (1.125° each), 6, 10 and 10 elements of uniform radial size across the casing, cement and rock layers respectively, and a single element through a slab thickness of 0.1 m; elements are straight-sided with all nodes exactly on the circles, and each interface is a zero-thickness surface with matching, initially coincident nodes on both sides. Only the quarter 0° ≤ θ ≤ 90° is modelled, with roller (symmetry) conditions: zero normal displacement on θ = 0° and on θ = 90°. Plane strain: no axial displacement. The slab end faces carry zero axial displacement; there is no gravity and no inertia. The casing–cement interface (r = 0.106 m) and the cement–rock interface (r = 0.133 m) are imperfect frictional contacts. Both interfaces are initially in perfect contact, closed and sticking, without gap or pre-stress; they cannot interpenetrate, have no cohesion and no tensile strength, and transmit shear by dry friction with coefficient μ (no slip while |τ| < μ σn, sliding at |τ| = μ σn). Here σn is the compressive normal stress transmitted across the interface (positive in compression) and τ the shear stress on it; the static and kinetic friction coefficients are both μ and friction is rate-independent. The contact constraints are enforced exactly (no interface compliance): a closed interface has zero relative normal displacement and a sticking interface has zero relative tangential displacement. Kinematics are small-strain and small-sliding: loads, normals and contact pairs refer to the undeformed configuration, each node stays paired with its initially coincident partner, and the applied tractions are dead loads. The applied tractions use the unit normal of each straight-sided element face. The contact is face-based: each matching interface face pair carries one constant traction unknown (normal and shear components), and the contact and friction conditions are imposed per face pair on the face-averaged relative displacement, along that face's own unit normal and tangent. The bore pressure acts only on the surface r = 0.100 m and never enters an interface. The roller conditions apply to every node on θ = 0° and θ = 90°, including both sides of each interface. The stick/slip state is followed incrementally: each increment is a single implicit (backward-Euler) step solved to equilibrium from the converged state of the previous one, the stick/slip state and the slip increment being determined by the end-of-increment tractions, and slip accumulates. The friction coefficient is μ = 0.2 on both interfaces. The outer surface r = 0.17 m is loaded by the traction σ·n, where σ is the uniform stress state σxx = −Sx, σyy = −Sy, σxy = 0 and n is the outward unit normal. Here Sy = 5 MPa and Sx = 10 MPa, so that x is the direction of the larger compression. The inner surface carries a uniform compressive pressure p (a negative value of p denotes a uniform tensile normal traction). Here p = 2 MPa. Loading is quasi-static and is applied in 10 equal increments, the outer traction and the inner pressure being ramped together, proportionally, from zero to their final values. The requested quantity refers to the final equilibrium state after increment 10. The system is initially stress-free. All displacements are initially zero. Define contact pressure = compressive normal stress transmitted across the interface (positive when compressive). On the discretised interface the contact pressure is constant over each interface face element (1.125° wide, one element through the thickness) and equal on both sides, so its average over a 1.125° segment is the value of the single face element covering that segment. On each interface compare the contact pressure averaged over the segment adjacent to the θ = 0° plane (0° ≤ θ ≤ 1.125°) with that averaged over the segment adjacent to the θ = 90° plane (88.875° ≤ θ ≤ 90°), in the final state. Which statement is correct? A. On the cement–rock interface the contact pressure is larger next to θ = 0°, whereas on the casing–cement interface it is larger next to θ = 90°. B. On both interfaces the contact pressure is larger next to θ = 0°. C. On both interfaces the contact pressure is larger next to θ = 90°. D. On the cement–rock interface the contact pressure is larger next to θ = 90°, whereas on the casing–cement interface it is larger next to θ = 0°. Answer with one letter.

**Options and evidence from the simulations:**

- **A** (correct): On the cement–rock interface the contact pressure is larger next to θ = 0°, whereas on the casing–cement interface it is larger next to θ = 90°.  
  _True: cement–rock 9.005 MPa (0°) vs 6.352 MPa (90°), +41.8 %; casing–cement 6.491 MPa (0°) vs 8.509 MPa (90°), -23.7 %._
- **B**  (naive): On both interfaces the contact pressure is larger next to θ = 0°.  
  _False: casing–cement pressure next to 0° is -23.7 % below that next to 90°._
- **C** : On both interfaces the contact pressure is larger next to θ = 90°.  
  _False: cement–rock pressure next to 0° is 41.8 % above that next to 90°._
- **D** : On the cement–rock interface the contact pressure is larger next to θ = 90°, whereas on the casing–cement interface it is larger next to θ = 0°.  
  _False: both orderings are reversed relative to the simulation._

### No-tool answer

_Model: GPT-5.6 Sol 1M · 43.77 s · tool calls: 0_

````text
B
````

### Judge

| | |
|---|---|
| True answer | **A** |
| No-tool answer | **B** |
| Relative error | – |
| Verdict | **❌ INCORRECT** |
| Reasoning sound | False |
| Correct value, wrong reasoning | False |
| Accepted into benchmark | True |

**Decisive comparison:** The answer chose B, but the simulation gives option A. On the cement–rock interface the pressure is 9.005 MPa next to 0° and 6.352 MPa next to 90°, so it is larger at 0°. On the casing–cement interface it is 6.491 MPa next to 0° and 8.509 MPa next to 90°, so it is larger at 90°.

**Key discrepancy:** B is the naive answer: it assumes the larger far-field compression along x makes the contact pressure larger next to θ = 0° on both interfaces. On the inner casing–cement interface the simulation shows the opposite, with pressure 23.7% lower next to 0° than next to 90°. No reasoning was given for the choice.

<sub>Provenance: runs run_0051; columns ['pc_cc_0', 'pc_cc_90', 'pc_cr_0', 'pc_cr_90']; refined: False</sub>

---

## Q15

**Category:** Casing membrane stress · **Type:** choice · **Template:** `stress|choice`

### Question

A plane-strain cross-section of a cased wellbore consists of three concentric, linear isotropic elastic (small-strain) layers: a steel casing between r = 0.100 m and r = 0.106 m, a cement sheath between r = 0.106 m and r = 0.133 m, and a rock annulus between r = 0.133 m and r = 0.170 m. Polar coordinates (r, θ) are used, θ being measured counter-clockwise from the x axis; u_r denotes the radial displacement (outward positive) and u_θ the tangential displacement (positive towards increasing θ). Elastic constants (bulk modulus, shear modulus; these values are the model inputs to the digits shown, the E and ν values in brackets are rounded restatements): casing 175 GPa, 80.8 GPa (E ≈ 210.1 GPa, ν ≈ 0.300); cement 10.3 GPa, 6.45 GPa (E ≈ 16.01 GPa, ν ≈ 0.241); rock 5.5556 GPa, 4.16667 GPa (E = 10 GPa, ν = 0.20). The body is represented by 8-node trilinear hexahedral elements (standard displacement formulation, full 2×2×2 Gauss integration): 80 uniform angular divisions over the quarter (1.125° each), 6, 10 and 10 elements of uniform radial size across the casing, cement and rock layers respectively, and a single element through a slab thickness of 0.1 m; elements are straight-sided with all nodes exactly on the circles, and each interface is a zero-thickness surface with matching, initially coincident nodes on both sides. Only the quarter 0° ≤ θ ≤ 90° is modelled, with roller (symmetry) conditions: zero normal displacement on θ = 0° and on θ = 90°. Plane strain: no axial displacement. The slab end faces carry zero axial displacement; there is no gravity and no inertia. The casing–cement interface (r = 0.106 m) and the cement–rock interface (r = 0.133 m) are imperfect frictional contacts. Both interfaces are initially in perfect contact, closed and sticking, without gap or pre-stress; they cannot interpenetrate, have no cohesion and no tensile strength, and transmit shear by dry friction with coefficient μ (no slip while |τ| < μ σn, sliding at |τ| = μ σn). Here σn is the compressive normal stress transmitted across the interface (positive in compression) and τ the shear stress on it; the static and kinetic friction coefficients are both μ and friction is rate-independent. The contact constraints are enforced exactly (no interface compliance): a closed interface has zero relative normal displacement and a sticking interface has zero relative tangential displacement. Kinematics are small-strain and small-sliding: loads, normals and contact pairs refer to the undeformed configuration, each node stays paired with its initially coincident partner, and the applied tractions are dead loads. The applied tractions use the unit normal of each straight-sided element face. The contact is face-based: each matching interface face pair carries one constant traction unknown (normal and shear components), and the contact and friction conditions are imposed per face pair on the face-averaged relative displacement, along that face's own unit normal and tangent. The bore pressure acts only on the surface r = 0.100 m and never enters an interface. The roller conditions apply to every node on θ = 0° and θ = 90°, including both sides of each interface. The stick/slip state is followed incrementally: each increment is a single implicit (backward-Euler) step solved to equilibrium from the converged state of the previous one, the stick/slip state and the slip increment being determined by the end-of-increment tractions, and slip accumulates. Two values of the friction coefficient (the same on both interfaces) are compared: μ = 0.10 and μ = 0.30. The outer surface r = 0.17 m is loaded by the traction σ·n, where σ is the uniform stress state σxx = −Sx, σyy = −Sy, σxy = 0 and n is the outward unit normal. Here Sy = 5 MPa and Sx = 8.75 MPa, so that x is the direction of the larger compression. The inner surface carries a uniform compressive pressure p (a negative value of p denotes a uniform tensile normal traction). Here p = 2 MPa. Loading is quasi-static and is applied in 10 equal increments, the outer traction and the inner pressure being ramped together, proportionally, from zero to their final values. All quantities below refer to the final equilibrium state after increment 10. The system is initially stress-free. All displacements are initially zero. The through-wall average hoop stress of the casing at θ ≈ 0° is the hoop stress σθθ (total stress, tension positive) averaged over the angular sector 0° ≤ θ ≤ 1.125° (adjacent to the θ = 0° plane) and uniformly with respect to radius across the full casing wall thickness. Concretely, each casing element's Cartesian stress is its Jacobian-weighted volume average over its 2×2×2 Gauss points, σθθ = σxx sin²θc + σyy cos²θc − 2 σxy sinθc cosθc is formed with the polar angle θc of the element centre (the mid-angle of its 1.125° sector), and the sector value is the arithmetic mean over the 6 casing elements of that sector (one per radial layer). The through-wall average hoop stress of the casing at θ ≈ 90° is defined in the same way over the sector 88.875° ≤ θ ≤ 90°. In all four cases considered (two angles, two friction coefficients) these averages are compressive. How do their magnitudes change when μ is raised from 0.10 to 0.30 (relative change of the magnitude with respect to μ = 0.10)? A. Both magnitudes decrease by more than 5 %. B. Both magnitudes increase by more than 5 %. C. The magnitude at θ ≈ 0° decreases by more than 5 %, whereas that at θ ≈ 90° increases by more than 5 %. D. Both magnitudes change by less than 5 %. Answer with one letter.

**Options and evidence from the simulations:**

- **A**  (naive): Both magnitudes decrease by more than 5 %.  
  _False: magnitude at 90° increases by 19.1 % (-101.43 MPa → -120.80 MPa)._
- **B** : Both magnitudes increase by more than 5 %.  
  _False: magnitude at 0° decreases by 21.3 % (-78.01 MPa → -61.36 MPa)._
- **C** (correct): The magnitude at θ ≈ 0° decreases by more than 5 %, whereas that at θ ≈ 90° increases by more than 5 %.  
  _True: 0° magnitude change -21.34 % (< −5 %), 90° magnitude change +19.09 % (> 5 %); all four values compressive._
- **D** : Both magnitudes change by less than 5 %.  
  _False: both changes exceed 5 % in magnitude (-21.3 %, 19.1 %)._

### No-tool answer

_Model: GPT-5.6 Sol 1M · 30.19 s · tool calls: 0_

````text
C
````

### Judge

| | |
|---|---|
| True answer | **C** |
| No-tool answer | **C** |
| Relative error | – |
| Verdict | **✅ CORRECT** |
| Reasoning sound | False |
| Correct value, wrong reasoning | True |
| Accepted into benchmark | False |

**Decisive comparison:** The answer commits to C, which matches the key's correct option C. In the simulation, the hoop-stress magnitude at θ ≈ 0° falls by 21.3 % (−78.01 → −61.36 MPa) and the magnitude at θ ≈ 90° rises by 19.1 % (−101.43 → −120.80 MPa).

**Key discrepancy:** There is no discrepancy in the selected letter. The answer is a bare letter with no reasoning, so nothing shows that the physics supports the choice.

<sub>Provenance: runs run_0007, run_0087; columns ['shoop_cas_wallavg_0', 'shoop_cas_wallavg_90']; refined: False</sub>

---
