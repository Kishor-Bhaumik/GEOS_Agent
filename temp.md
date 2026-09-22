# No-Tool Answers Summary


---

## Q01

### Question

Consider isothermal two-phase gravity segregation of water and gas in a 10 m cube. The cube is meshed with hexahedra of Δx = Δy = 1 m and Δz = 2.5/3 m (cell centres at 0.5, 1.5, …, 9.5 m in x and y; 0.417, 1.25, 2.083, 3.75, …, 9.583 m in z). Flow is confined to a 3-D staircase of permeable rock; the complementary blocks are impermeable (empty of pore fluid). Permeable occupancy is:
– z ∈ [0, 2.5] m: y ∈ [0, 5] m, x ∈ [0, 10] m;
– z ∈ [2.5, 5] m: x ∈ [0, 5] m, y ∈ [0, 10] m;
– z ∈ [5, 7.5] m: y ∈ [5, 10] m, x ∈ [0, 10] m;
– z ∈ [7.5, 10] m: x ∈ [5, 10] m, y ∈ [0, 10] m.
Gravity acts downward along −z (9.81 m s⁻²). There are no wells and no open boundaries. The initial pressure is 5 MPa, uniform (not hydrostatic). The temperature is isothermal at 300 K.

The two horizontal permeabilities are k_x = k_y = 1×10^{-15} m² and the vertical permeability is k_z = 1×10^{-16} m². The reference porosity is 0.20 at 5 MPa, with pore-volume compressibility 1×10^-9 Pa^{-1}.

The two components are immiscible. Surface densities are 1022 kg m⁻³ (water) and 0.9907 kg m⁻³ (gas); molar masses are 0.018 kg mol⁻¹ (water) and 0.016 kg mol⁻¹ (gas). Phase behaviour is given by tabulated dead-oil / black-oil formation-volume-factor and viscosity versus pressure.
Water, single reference point: P_ref = 3.06000001×10^7 Pa, B_w = 1.03, C_p = 4.1×10^{-10} Pa^{-1}, μ_w = 3.0×10^{-4} Pa·s.
Gas formation-volume factor B_g (m³/sm³) and viscosity μ_g (Pa·s) versus pressure P (Pa):
P = (3000000, 6000000, 9000000, 12000000, 15000000, 18000000, 21000000, 24000000, 27000000, 29500000, 31000000, 33000000, 53000000)
B_g = (0.04234, 0.02046, 0.01328, 0.00977, 0.00773, 0.006426, 0.005541, 0.004919, 0.004471, 0.004194, 0.004031, 0.00391, 0.003868)
μ_g = (0.00005344, 0.0000542, 0.00005526, 0.0000566, 0.00005818, 0.00005994, 0.00006181, 0.0000637, 0.00006559, 0.00006714, 0.00006806, 0.00006832, 0.00006935).

Drainage relative permeabilities are tabulated as follows.
Water, k_rw(S_w):
S_w = (0.22000, 0.25000, 0.30000, 0.35000, 0.40000, 0.45000, 0.50000, 0.55000, 0.60000, 0.65000, 0.66000, 0.68000, 0.72000, 0.82000, 0.91000, 1.00000)
k_rw = (0.00000, 0.00100, 0.00300, 0.01000, 0.01800, 0.03500, 0.04000, 0.05700, 0.08800, 0.14500, 0.16000, 0.19000, 0.26300, 0.45500, 0.69200, 1.)
Gas, k_rg(S_g):
S_g = (0.000, 0.010, 0.030, 0.050, 0.100, 0.150, 0.200, 0.250, 0.300, 0.350, 0.400, 0.450, 0.500, 0.550, 0.600, 0.650, 0.700, 0.750, 0.780)
k_rg = (0.00000, 0.00200, 0.00700, 0.01000, 0.02000, 0.04000, 0.07500, 0.12700, 0.18000, 0.24000, 0.31000, 0.37300, 0.46000, 0.55000, 0.64000, 0.73000, 0.82500, 0.92000, 1.00000).

Imbibition relative permeabilities, used together with the drainage tables under history-dependent hysteresis (scanning between the two curves), are:
Water, k_rw(S_w):
S_w = (0.22000, 0.25000, 0.30000, 0.35000, 0.40000, 0.45000, 0.50000, 0.55000, 0.60000, 0.65000, 0.66000, 0.70000)
k_rw = (0, 0.0156, 0.0680, 0.1409, 0.2296, 0.3317, 0.4455, 0.5700, 0.7044, 0.8479, 0.8776, 0.9382)
Gas, k_rg(S_g):
S_g = (0.300, 0.350, 0.400, 0.450, 0.500, 0.550, 0.600, 0.650, 0.700, 0.750, 0.780)
k_rg = (0.0000, 0.03361965, 0.09509072, 0.17469281, 0.26895718, 0.37587908, 0.49410588, 0.62264458, 0.76072577, 0.90773047, 1.).

Both drainage and imbibition relative-permeability tables are used, with history-dependent hysteresis (scanning between the two curves).

Initial overall mole fractions are specified in two overlapping boxes: a bottom layer z ∈ [0, 1.01] m and the remainder z ∈ [0.80, 10] m, with the bottom-layer specification overwriting the overlap z ∈ [0.80, 1.01] m. The stack is inverted: the bottom layer is the gas-rich side (water mole fraction 0.10, gas 0.90); the remainder is water 0.99, gas 0.01.

Time is advanced with a maximum step of 4×10^6 s after a short increasing start-up, to an end time of 4×10^8 s.

Determine the gas saturation (gas phase volume fraction) at the cell centred at (2.5, 2.5, 0.417) m at t = 8×10^7 s, while the bottom-layer gas cushion is still collapsing. Report the value as a saturation in [0, 1], non-negative. Answers within 1.0% relative are accepted.


### Ground Truth

0.5448722276315476


### No-Tool Answer

The predicted gas saturation is

\[
\boxed{S_g(2.5,2.5,0.417;\ 8\times10^7\ \mathrm{s}) \approx 0.56}
\]

This is an estimate based on gravity-driven counter-current flux with hysteretic imbibition in the collapsing gas-rich bottom cell.


### Judge


- Verdict: INCORRECT

- No-tool estimate: 0.56

- No-tool conclusion: None

- Relative error percent: 2.776388958969311

- Reasoning sound: False

- Decisive comparison: The answer commits to Sg ≈ 0.56 at the west-bottom cell, about 2.8% above the true 0.54487 and outside the 1.0% relative window (about 0.5394–0.5503).

- Key discrepancy: It ballparks a still-collapsing hysteretic cushion near 0.56 instead of the simulated anisotropic gravity-segregation value 0.545.


---

## Q02

### Question

Consider isothermal two-phase gravity segregation of water and gas in a 10 m cube. The cube is meshed with hexahedra of Δx = Δy = 1 m and Δz = 2.5/3 m (cell centres at 0.5, 1.5, …, 9.5 m in x and y; 0.417, 1.25, 2.083, 3.75, …, 9.583 m in z). Flow is confined to a 3-D staircase of permeable rock; the complementary blocks are impermeable (empty of pore fluid). Permeable occupancy is:
– z ∈ [0, 2.5] m: y ∈ [0, 5] m, x ∈ [0, 10] m;
– z ∈ [2.5, 5] m: x ∈ [0, 5] m, y ∈ [0, 10] m;
– z ∈ [5, 7.5] m: y ∈ [5, 10] m, x ∈ [0, 10] m;
– z ∈ [7.5, 10] m: x ∈ [5, 10] m, y ∈ [0, 10] m.
Gravity acts downward along −z (9.81 m s⁻²). There are no wells and no open boundaries. The initial pressure is 5 MPa, uniform (not hydrostatic). The temperature is isothermal at 300 K.

The permeable rock is isotropic with permeability 1×10^{-15} m². The reference porosity is 0.20 at 5 MPa, with pore-volume compressibility 1×10^-9 Pa^{-1}.

The two components are immiscible. Surface densities are 1022 kg m⁻³ (water) and 0.9907 kg m⁻³ (gas); molar masses are 0.018 kg mol⁻¹ (water) and 0.016 kg mol⁻¹ (gas). Phase behaviour is given by tabulated dead-oil / black-oil formation-volume-factor and viscosity versus pressure.
Water, single reference point: P_ref = 3.06000001×10^7 Pa, B_w = 1.03, C_p = 4.1×10^{-10} Pa^{-1}, μ_w = 3.0×10^{-4} Pa·s.
Gas formation-volume factor B_g (m³/sm³) and viscosity μ_g (Pa·s) versus pressure P (Pa):
P = (3000000, 6000000, 9000000, 12000000, 15000000, 18000000, 21000000, 24000000, 27000000, 29500000, 31000000, 33000000, 53000000)
B_g = (0.04234, 0.02046, 0.01328, 0.00977, 0.00773, 0.006426, 0.005541, 0.004919, 0.004471, 0.004194, 0.004031, 0.00391, 0.003868)
μ_g = (0.00005344, 0.0000542, 0.00005526, 0.0000566, 0.00005818, 0.00005994, 0.00006181, 0.0000637, 0.00006559, 0.00006714, 0.00006806, 0.00006832, 0.00006935).

Drainage relative permeabilities are tabulated as follows.
Water, k_rw(S_w):
S_w = (0.22000, 0.25000, 0.30000, 0.35000, 0.40000, 0.45000, 0.50000, 0.55000, 0.60000, 0.65000, 0.66000, 0.68000, 0.72000, 0.82000, 0.91000, 1.00000)
k_rw = (0.00000, 0.00100, 0.00300, 0.01000, 0.01800, 0.03500, 0.04000, 0.05700, 0.08800, 0.14500, 0.16000, 0.19000, 0.26300, 0.45500, 0.69200, 1.)
Gas, k_rg(S_g):
S_g = (0.000, 0.010, 0.030, 0.050, 0.100, 0.150, 0.200, 0.250, 0.300, 0.350, 0.400, 0.450, 0.500, 0.550, 0.600, 0.650, 0.700, 0.750, 0.780)
k_rg = (0.00000, 0.00200, 0.00700, 0.01000, 0.02000, 0.04000, 0.07500, 0.12700, 0.18000, 0.24000, 0.31000, 0.37300, 0.46000, 0.55000, 0.64000, 0.73000, 0.82500, 0.92000, 1.00000).

Imbibition relative permeabilities, used together with the drainage tables under history-dependent hysteresis (scanning between the two curves), are:
Water, k_rw(S_w):
S_w = (0.22000, 0.25000, 0.30000, 0.35000, 0.40000, 0.45000, 0.50000, 0.55000, 0.60000, 0.65000, 0.66000, 0.70000)
k_rw = (0, 0.0156, 0.0680, 0.1409, 0.2296, 0.3317, 0.4455, 0.5700, 0.7044, 0.8479, 0.8776, 0.9382)
Gas, k_rg(S_g):
S_g = (0.300, 0.350, 0.400, 0.450, 0.500, 0.550, 0.600, 0.650, 0.700, 0.750, 0.780)
k_rg = (0.0000, 0.03361965, 0.09509072, 0.17469281, 0.26895718, 0.37587908, 0.49410588, 0.62264458, 0.76072577, 0.90773047, 1.).

Both drainage and imbibition relative-permeability tables are used, with history-dependent hysteresis (scanning between the two curves).

Initial overall mole fractions are specified in two overlapping boxes: a bottom layer z ∈ [0, 1.01] m and the remainder z ∈ [0.80, 10] m, with the bottom-layer specification overwriting the overlap z ∈ [0.80, 1.01] m. The stack is inverted: the bottom layer is the gas-rich side (water mole fraction 0.10, gas 0.90); the remainder is water 0.99, gas 0.01.

Time is advanced with a maximum step of 4×10^6 s after a short increasing start-up, to an end time of 4×10^8 s.

Determine the mean gas saturation (gas phase volume fraction) in the permeable 5 m × 5 m × 2.5 m block occupying x ∈ [0, 5] m, y ∈ [0, 5] m, z ∈ [2.5, 5] m at t = 3.96×10^8 s, after gas has ponded under that stair ceiling. Report the value as a saturation in [0, 1], non-negative. Answers within 1.0% relative are accepted.


### Ground Truth

0.3381601245373953


### No-Tool Answer

The predicted mean gas saturation is

\[
\boxed{\overline{S_g}\approx 0.46}
\]

At late time, the upper cell layer is gas-ponded near \(S_g=0.78\), while the two lower layers are imbibed to the hysteretic residual \(S_g\approx0.30\). Since the three layers have equal volume,

\[
\overline{S_g}\approx\frac{0.78+0.30+0.30}{3}=0.46.
\]


### Judge


- Verdict: INCORRECT

- No-tool estimate: 0.46

- No-tool conclusion: None

- Relative error percent: 36.03023142639371

- Reasoning sound: False

- Decisive comparison: The answer commits to a block-mean gas saturation of 0.46, while the simulation truth is 0.33816; the relative error is about 36%, far beyond the 1% relative tolerance.

- Key discrepancy: It treats the 2.5 m stair as one fully ponded cell at Sg=0.78 over two residual layers at Sg=0.30, but the ceiling pond does not fill a whole layer to residual-gas-free saturation, so the true block mean is 0.338 rather than 0.46.


---

## Q03

### Question

Consider isothermal two-phase gravity segregation of water and gas in a 10 m cube. The cube is meshed with hexahedra of Δx = Δy = 1 m and Δz = 2.5/3 m (cell centres at 0.5, 1.5, …, 9.5 m in x and y; 0.417, 1.25, 2.083, 3.75, …, 9.583 m in z). Flow is confined to a 3-D staircase of permeable rock; the complementary blocks are impermeable (empty of pore fluid). Permeable occupancy is:
– z ∈ [0, 2.5] m: y ∈ [0, 5] m, x ∈ [0, 10] m;
– z ∈ [2.5, 5] m: x ∈ [0, 5] m, y ∈ [0, 10] m;
– z ∈ [5, 7.5] m: y ∈ [5, 10] m, x ∈ [0, 10] m;
– z ∈ [7.5, 10] m: x ∈ [5, 10] m, y ∈ [0, 10] m.
Gravity acts downward along −z (9.81 m s⁻²). There are no wells and no open boundaries. The initial pressure is 5 MPa, uniform (not hydrostatic). The temperature is isothermal at 300 K.

The two horizontal permeabilities are k_x = k_y = 1×10^{-15} m² and the vertical permeability is k_z = 1×10^{-16} m². The reference porosity is 0.20 at 5 MPa, with pore-volume compressibility 1×10^-9 Pa^{-1}.

The two components are immiscible. Surface densities are 1022 kg m⁻³ (water) and 0.9907 kg m⁻³ (gas); molar masses are 0.018 kg mol⁻¹ (water) and 0.016 kg mol⁻¹ (gas). Phase behaviour is given by tabulated dead-oil / black-oil formation-volume-factor and viscosity versus pressure.
Water, single reference point: P_ref = 3.06000001×10^7 Pa, B_w = 1.03, C_p = 4.1×10^{-10} Pa^{-1}, μ_w = 3.0×10^{-4} Pa·s.
Gas formation-volume factor B_g (m³/sm³) and viscosity μ_g (Pa·s) versus pressure P (Pa):
P = (3000000, 6000000, 9000000, 12000000, 15000000, 18000000, 21000000, 24000000, 27000000, 29500000, 31000000, 33000000, 53000000)
B_g = (0.04234, 0.02046, 0.01328, 0.00977, 0.00773, 0.006426, 0.005541, 0.004919, 0.004471, 0.004194, 0.004031, 0.00391, 0.003868)
μ_g = (0.00005344, 0.0000542, 0.00005526, 0.0000566, 0.00005818, 0.00005994, 0.00006181, 0.0000637, 0.00006559, 0.00006714, 0.00006806, 0.00006832, 0.00006935).

Drainage relative permeabilities are tabulated as follows.
Water, k_rw(S_w):
S_w = (0.22000, 0.25000, 0.30000, 0.35000, 0.40000, 0.45000, 0.50000, 0.55000, 0.60000, 0.65000, 0.66000, 0.68000, 0.72000, 0.82000, 0.91000, 1.00000)
k_rw = (0.00000, 0.00100, 0.00300, 0.01000, 0.01800, 0.03500, 0.04000, 0.05700, 0.08800, 0.14500, 0.16000, 0.19000, 0.26300, 0.45500, 0.69200, 1.)
Gas, k_rg(S_g):
S_g = (0.000, 0.010, 0.030, 0.050, 0.100, 0.150, 0.200, 0.250, 0.300, 0.350, 0.400, 0.450, 0.500, 0.550, 0.600, 0.650, 0.700, 0.750, 0.780)
k_rg = (0.00000, 0.00200, 0.00700, 0.01000, 0.02000, 0.04000, 0.07500, 0.12700, 0.18000, 0.24000, 0.31000, 0.37300, 0.46000, 0.55000, 0.64000, 0.73000, 0.82500, 0.92000, 1.00000).

Imbibition relative permeabilities, used together with the drainage tables under history-dependent hysteresis (scanning between the two curves), are:
Water, k_rw(S_w):
S_w = (0.22000, 0.25000, 0.30000, 0.35000, 0.40000, 0.45000, 0.50000, 0.55000, 0.60000, 0.65000, 0.66000, 0.70000)
k_rw = (0, 0.0156, 0.0680, 0.1409, 0.2296, 0.3317, 0.4455, 0.5700, 0.7044, 0.8479, 0.8776, 0.9382)
Gas, k_rg(S_g):
S_g = (0.300, 0.350, 0.400, 0.450, 0.500, 0.550, 0.600, 0.650, 0.700, 0.750, 0.780)
k_rg = (0.0000, 0.03361965, 0.09509072, 0.17469281, 0.26895718, 0.37587908, 0.49410588, 0.62264458, 0.76072577, 0.90773047, 1.).

Both drainage and imbibition relative-permeability tables are used, with history-dependent hysteresis (scanning between the two curves).

Initial overall mole fractions are specified in two overlapping boxes: a bottom layer z ∈ [0, 1.01] m and the remainder z ∈ [0.80, 10] m, with the bottom-layer specification overwriting the overlap z ∈ [0.80, 1.01] m. The stack is inverted: the bottom layer is the gas-rich side (water mole fraction 0.10, gas 0.90); the remainder is water 0.99, gas 0.01.

Time is advanced with a maximum step of 4×10^6 s after a short increasing start-up, to an end time of 4×10^8 s.

Determine the gas saturation (gas phase volume fraction) at the cell centred at (7.5, 7.5, 8.75) m at t = 3.96×10^8 s, where gas ponds in the upper-north stair. Report the value as a saturation in [0, 1], non-negative. Answers within 1.0% relative are accepted.


### Ground Truth

0.3926790512864315


### No-Tool Answer

Estimated gas saturation:

\[
\boxed{S_g(7.5,7.5,8.75;\,3.96\times10^8\ \mathrm{s}) \approx 0.78}
\]

The ponded cell follows drainage toward the endpoint \(S_g=0.78\), corresponding to irreducible water saturation \(S_w=0.22\).


### Judge


- Verdict: INCORRECT

- No-tool estimate: 0.78

- No-tool conclusion: None

- Relative error percent: 98.63550078484973

- Reasoning sound: False

- Decisive comparison: The answer commits to Sg ≈ 0.78 at (7.5, 7.5, 8.75) m, while the simulation truth is 0.3927; the relative error is about 99%, far beyond the 1% relative tolerance.

- Key discrepancy: It assumes the upper-north pond drains fully to the drainage endpoint 1−Swc = 0.78; late-time anisotropic ponding leaves Sg ≈ 0.393, not residual-water-free fill.


---

## Q04

### Question

Consider isothermal two-phase gravity segregation of water and gas in a 10 m cube. The cube is meshed with hexahedra of Δx = Δy = 1 m and Δz = 2.5/3 m (cell centres at 0.5, 1.5, …, 9.5 m in x and y; 0.417, 1.25, 2.083, 3.75, …, 9.583 m in z). Flow is confined to a 3-D staircase of permeable rock; the complementary blocks are impermeable (empty of pore fluid). Permeable occupancy is:
– z ∈ [0, 2.5] m: y ∈ [0, 5] m, x ∈ [0, 10] m;
– z ∈ [2.5, 5] m: x ∈ [0, 5] m, y ∈ [0, 10] m;
– z ∈ [5, 7.5] m: y ∈ [5, 10] m, x ∈ [0, 10] m;
– z ∈ [7.5, 10] m: x ∈ [5, 10] m, y ∈ [0, 10] m.
Gravity acts downward along −z (9.81 m s⁻²). There are no wells and no open boundaries. The initial pressure is 5 MPa, uniform (not hydrostatic). The temperature is isothermal at 300 K.

The permeable rock is isotropic with permeability 1×10^{-15} m². The reference porosity is 0.20 at 5 MPa, with pore-volume compressibility 1×10^-9 Pa^{-1}.

The two components are immiscible. Surface densities are 1022 kg m⁻³ (water) and 0.9907 kg m⁻³ (gas); molar masses are 0.018 kg mol⁻¹ (water) and 0.016 kg mol⁻¹ (gas). Phase behaviour is given by tabulated dead-oil / black-oil formation-volume-factor and viscosity versus pressure.
Water, single reference point: P_ref = 3.06000001×10^7 Pa, B_w = 1.03, C_p = 4.1×10^{-10} Pa^{-1}, μ_w = 3.0×10^{-4} Pa·s.
Gas formation-volume factor B_g (m³/sm³) and viscosity μ_g (Pa·s) versus pressure P (Pa):
P = (3000000, 6000000, 9000000, 12000000, 15000000, 18000000, 21000000, 24000000, 27000000, 29500000, 31000000, 33000000, 53000000)
B_g = (0.04234, 0.02046, 0.01328, 0.00977, 0.00773, 0.006426, 0.005541, 0.004919, 0.004471, 0.004194, 0.004031, 0.00391, 0.003868)
μ_g = (0.00005344, 0.0000542, 0.00005526, 0.0000566, 0.00005818, 0.00005994, 0.00006181, 0.0000637, 0.00006559, 0.00006714, 0.00006806, 0.00006832, 0.00006935).

Drainage relative permeabilities are tabulated as follows.
Water, k_rw(S_w):
S_w = (0.22000, 0.25000, 0.30000, 0.35000, 0.40000, 0.45000, 0.50000, 0.55000, 0.60000, 0.65000, 0.66000, 0.68000, 0.72000, 0.82000, 0.91000, 1.00000)
k_rw = (0.00000, 0.00100, 0.00300, 0.01000, 0.01800, 0.03500, 0.04000, 0.05700, 0.08800, 0.14500, 0.16000, 0.19000, 0.26300, 0.45500, 0.69200, 1.)
Gas, k_rg(S_g):
S_g = (0.000, 0.010, 0.030, 0.050, 0.100, 0.150, 0.200, 0.250, 0.300, 0.350, 0.400, 0.450, 0.500, 0.550, 0.600, 0.650, 0.700, 0.750, 0.780)
k_rg = (0.00000, 0.00200, 0.00700, 0.01000, 0.02000, 0.04000, 0.07500, 0.12700, 0.18000, 0.24000, 0.31000, 0.37300, 0.46000, 0.55000, 0.64000, 0.73000, 0.82500, 0.92000, 1.00000).

Imbibition relative permeabilities, used together with the drainage tables under history-dependent hysteresis (scanning between the two curves), are:
Water, k_rw(S_w):
S_w = (0.22000, 0.25000, 0.30000, 0.35000, 0.40000, 0.45000, 0.50000, 0.55000, 0.60000, 0.65000, 0.66000, 0.70000)
k_rw = (0, 0.0156, 0.0680, 0.1409, 0.2296, 0.3317, 0.4455, 0.5700, 0.7044, 0.8479, 0.8776, 0.9382)
Gas, k_rg(S_g):
S_g = (0.300, 0.350, 0.400, 0.450, 0.500, 0.550, 0.600, 0.650, 0.700, 0.750, 0.780)
k_rg = (0.0000, 0.03361965, 0.09509072, 0.17469281, 0.26895718, 0.37587908, 0.49410588, 0.62264458, 0.76072577, 0.90773047, 1.).

Both drainage and imbibition relative-permeability tables are used, with history-dependent hysteresis (scanning between the two curves).

Initial overall mole fractions are specified in two overlapping boxes: a bottom layer z ∈ [0, 1.01] m and the remainder z ∈ [0.80, 10] m, with the bottom-layer specification overwriting the overlap z ∈ [0.80, 1.01] m. The stack is inverted: the bottom layer is the gas-rich side (water mole fraction 0.10, gas 0.90); the remainder is water 0.99, gas 0.01.

Time is advanced with a maximum step of 4×10^6 s after a short increasing start-up, to an end time of 4×10^8 s.

Determine the gas saturation (gas phase volume fraction) at the cell centred at (2.5, 7.5, 3.75) m at t = 3.96×10^8 s, in the northward connecting corridor after the gas cushion has risen. Report the value as a saturation in [0, 1], non-negative. Answers within 1.0% relative are accepted.


### Ground Truth

0.1351198169000638


### No-Tool Answer

The predicted gas saturation is

\[
\boxed{S_g(2.5,7.5,3.75;\,3.96\times10^8\ \mathrm{s}) \approx 0.300}
\]

The gas cushion sweeps this connecting corridor and then rises onward. During subsequent imbibition, gas becomes trapped near the imbibition endpoint \(S_g=0.30\), where \(k_{rg}=0\). Minor finite-time/numerical deviations from 0.30 are possible.


### Judge


- Verdict: INCORRECT

- No-tool estimate: 0.3

- No-tool conclusion: None

- Relative error percent: 122.02516764945254

- Reasoning sound: False

- Decisive comparison: The answer commits to Sg ≈ 0.30, the imbibition kr,g = 0 endpoint, whereas the simulation value at (2.5, 7.5, 3.75) m and t = 3.96e8 s is 0.135, far outside the 1% relative tolerance.

- Key discrepancy: It treats the northward corridor as fully drained then imbibed to the table residual Sg = 0.30; history-dependent hysteresis leaves a lower leftover because that cell never reached a high enough Sg.


---

## Q05

### Question

Consider isothermal two-phase gravity segregation of water and gas in a 10 m cube. The cube is meshed with hexahedra of Δx = Δy = 1 m and Δz = 2.5/3 m (cell centres at 0.5, 1.5, …, 9.5 m in x and y; 0.417, 1.25, 2.083, 3.75, …, 9.583 m in z). Flow is confined to a 3-D staircase of permeable rock; the complementary blocks are impermeable (empty of pore fluid). Permeable occupancy is:
– z ∈ [0, 2.5] m: y ∈ [0, 5] m, x ∈ [0, 10] m;
– z ∈ [2.5, 5] m: x ∈ [0, 5] m, y ∈ [0, 10] m;
– z ∈ [5, 7.5] m: y ∈ [5, 10] m, x ∈ [0, 10] m;
– z ∈ [7.5, 10] m: x ∈ [5, 10] m, y ∈ [0, 10] m.
Gravity acts downward along −z (9.81 m s⁻²). There are no wells and no open boundaries. The initial pressure is 5 MPa, uniform (not hydrostatic). The temperature is isothermal at 300 K.

The two horizontal permeabilities are k_x = k_y = 7×10^{-16} m² and the vertical permeability is k_z = 7×10^{-17} m². The reference porosity is 0.20 at 5 MPa, with pore-volume compressibility 1×10^-9 Pa^{-1}.

The two components are immiscible. Surface densities are 1022 kg m⁻³ (water) and 0.9907 kg m⁻³ (gas); molar masses are 0.018 kg mol⁻¹ (water) and 0.016 kg mol⁻¹ (gas). Phase behaviour is given by tabulated dead-oil / black-oil formation-volume-factor and viscosity versus pressure.
Water, single reference point: P_ref = 3.06000001×10^7 Pa, B_w = 1.03, C_p = 4.1×10^{-10} Pa^{-1}, μ_w = 3.0×10^{-4} Pa·s.
Gas formation-volume factor B_g (m³/sm³) and viscosity μ_g (Pa·s) versus pressure P (Pa):
P = (3000000, 6000000, 9000000, 12000000, 15000000, 18000000, 21000000, 24000000, 27000000, 29500000, 31000000, 33000000, 53000000)
B_g = (0.04234, 0.02046, 0.01328, 0.00977, 0.00773, 0.006426, 0.005541, 0.004919, 0.004471, 0.004194, 0.004031, 0.00391, 0.003868)
μ_g = (0.00005344, 0.0000542, 0.00005526, 0.0000566, 0.00005818, 0.00005994, 0.00006181, 0.0000637, 0.00006559, 0.00006714, 0.00006806, 0.00006832, 0.00006935).

Drainage relative permeabilities are tabulated as follows.
Water, k_rw(S_w):
S_w = (0.22000, 0.25000, 0.30000, 0.35000, 0.40000, 0.45000, 0.50000, 0.55000, 0.60000, 0.65000, 0.66000, 0.68000, 0.72000, 0.82000, 0.91000, 1.00000)
k_rw = (0.00000, 0.00100, 0.00300, 0.01000, 0.01800, 0.03500, 0.04000, 0.05700, 0.08800, 0.14500, 0.16000, 0.19000, 0.26300, 0.45500, 0.69200, 1.)
Gas, k_rg(S_g):
S_g = (0.000, 0.010, 0.030, 0.050, 0.100, 0.150, 0.200, 0.250, 0.300, 0.350, 0.400, 0.450, 0.500, 0.550, 0.600, 0.650, 0.700, 0.750, 0.780)
k_rg = (0.00000, 0.00200, 0.00700, 0.01000, 0.02000, 0.04000, 0.07500, 0.12700, 0.18000, 0.24000, 0.31000, 0.37300, 0.46000, 0.55000, 0.64000, 0.73000, 0.82500, 0.92000, 1.00000).

Only the drainage relative-permeability curves are used; there is no hysteresis and the imbibition tables are not present.

Initial overall mole fractions are specified in two overlapping boxes: a bottom layer z ∈ [0, 1.01] m and the remainder z ∈ [0.80, 10] m, with the bottom-layer specification overwriting the overlap z ∈ [0.80, 1.01] m. The stack is inverted: the bottom layer is the gas-rich side (water mole fraction 0.10, gas 0.90); the remainder is water 0.99, gas 0.01.

Time is advanced with a maximum step of 4×10^6 s after a short increasing start-up, to an end time of 4×10^8 s.

Determine the gas saturation (gas phase volume fraction) at the cell centred at (2.5, 2.5, 0.417) m at t = 3.96×10^8 s, after the inverted cushion has been allowed to drain without hysteresis. Report the value as a saturation in [0, 1], non-negative. Answers within 0.01 absolute are accepted.


### Ground Truth

0.0253137363446471


### No-Tool Answer

The predicted gas saturation is:

\[
\boxed{S_g(2.5,2.5,0.417\ \mathrm{m}) \approx 0.00}
\]

After \(3.96\times10^8\) s (12.6 years), buoyant gas has drained upward from the bottom cell and been replaced by water. With no hysteresis or residual-gas constraint, gas saturation can fall to zero.


### Judge


- Verdict: INCORRECT

- No-tool estimate: 0.0

- No-tool conclusion: None

- Relative error percent: -100.0

- Reasoning sound: False

- Decisive comparison: The answer commits to Sg ≈ 0.00 at the west-bottom cell, while the simulation truth is 0.02531; the absolute error is 0.0253, outside the accepted 0.01 window.

- Key discrepancy: It treats drainage-only (no hysteresis) as implying residual gas can fall identically to zero, but at this still-slow anisotropic permeability the cell retains a small leftover Sg ≈ 0.0253 rather than emptying.


---

## Q06

### Question

Consider isothermal two-phase gravity segregation of water and gas in a 10 m cube. The cube is meshed with hexahedra of Δx = Δy = 1 m and Δz = 2.5/3 m (cell centres at 0.5, 1.5, …, 9.5 m in x and y; 0.417, 1.25, 2.083, 3.75, …, 9.583 m in z). Flow is confined to a 3-D staircase of permeable rock; the complementary blocks are impermeable (empty of pore fluid). Permeable occupancy is:
– z ∈ [0, 2.5] m: y ∈ [0, 5] m, x ∈ [0, 10] m;
– z ∈ [2.5, 5] m: x ∈ [0, 5] m, y ∈ [0, 10] m;
– z ∈ [5, 7.5] m: y ∈ [5, 10] m, x ∈ [0, 10] m;
– z ∈ [7.5, 10] m: x ∈ [5, 10] m, y ∈ [0, 10] m.
Gravity acts downward along −z (9.81 m s⁻²). There are no wells and no open boundaries. The initial pressure is 5 MPa, uniform (not hydrostatic). The temperature is isothermal at 300 K.

The two horizontal permeabilities equal an unknown value k_h, and the vertical permeability is 0.10 k_h. k_h lies in the closed interval [3×10^{-16}, 1×10^{-14}] m². The reference porosity is 0.20 at 5 MPa, with pore-volume compressibility 1×10^{-9} Pa^{-1}.

The two components are immiscible. Surface densities are 1022 kg m⁻³ (water) and 0.9907 kg m⁻³ (gas); molar masses are 0.018 kg mol⁻¹ (water) and 0.016 kg mol⁻¹ (gas). Phase behaviour is given by tabulated dead-oil / black-oil formation-volume-factor and viscosity versus pressure.
Water, single reference point: P_ref = 3.06000001×10^7 Pa, B_w = 1.03, C_p = 4.1×10^{-10} Pa^{-1}, μ_w = 3.0×10^{-4} Pa·s.
Gas formation-volume factor B_g (m³/sm³) and viscosity μ_g (Pa·s) versus pressure P (Pa):
P = (3000000, 6000000, 9000000, 12000000, 15000000, 18000000, 21000000, 24000000, 27000000, 29500000, 31000000, 33000000, 53000000)
B_g = (0.04234, 0.02046, 0.01328, 0.00977, 0.00773, 0.006426, 0.005541, 0.004919, 0.004471, 0.004194, 0.004031, 0.00391, 0.003868)
μ_g = (0.00005344, 0.0000542, 0.00005526, 0.0000566, 0.00005818, 0.00005994, 0.00006181, 0.0000637, 0.00006559, 0.00006714, 0.00006806, 0.00006832, 0.00006935).

Drainage relative permeabilities are tabulated as follows.
Water, k_rw(S_w):
S_w = (0.22000, 0.25000, 0.30000, 0.35000, 0.40000, 0.45000, 0.50000, 0.55000, 0.60000, 0.65000, 0.66000, 0.68000, 0.72000, 0.82000, 0.91000, 1.00000)
k_rw = (0.00000, 0.00100, 0.00300, 0.01000, 0.01800, 0.03500, 0.04000, 0.05700, 0.08800, 0.14500, 0.16000, 0.19000, 0.26300, 0.45500, 0.69200, 1.)
Gas, k_rg(S_g):
S_g = (0.000, 0.010, 0.030, 0.050, 0.100, 0.150, 0.200, 0.250, 0.300, 0.350, 0.400, 0.450, 0.500, 0.550, 0.600, 0.650, 0.700, 0.750, 0.780)
k_rg = (0.00000, 0.00200, 0.00700, 0.01000, 0.02000, 0.04000, 0.07500, 0.12700, 0.18000, 0.24000, 0.31000, 0.37300, 0.46000, 0.55000, 0.64000, 0.73000, 0.82500, 0.92000, 1.00000).

Imbibition relative permeabilities, used together with the drainage tables under history-dependent hysteresis (scanning between the two curves), are:
Water, k_rw(S_w):
S_w = (0.22000, 0.25000, 0.30000, 0.35000, 0.40000, 0.45000, 0.50000, 0.55000, 0.60000, 0.65000, 0.66000, 0.70000)
k_rw = (0, 0.0156, 0.0680, 0.1409, 0.2296, 0.3317, 0.4455, 0.5700, 0.7044, 0.8479, 0.8776, 0.9382)
Gas, k_rg(S_g):
S_g = (0.300, 0.350, 0.400, 0.450, 0.500, 0.550, 0.600, 0.650, 0.700, 0.750, 0.780)
k_rg = (0.0000, 0.03361965, 0.09509072, 0.17469281, 0.26895718, 0.37587908, 0.49410588, 0.62264458, 0.76072577, 0.90773047, 1.).

Both drainage and imbibition relative-permeability tables are used, with history-dependent hysteresis (scanning between the two curves).

Initial overall mole fractions are specified in two overlapping boxes: a bottom layer z ∈ [0, 1.01] m and the remainder z ∈ [0.80, 10] m, with the bottom-layer specification overwriting the overlap z ∈ [0.80, 1.01] m. The stack is inverted: the bottom layer is the gas-rich side (water mole fraction 0.10, gas 0.90); the remainder is water 0.99, gas 0.01.

Time is advanced with a maximum step of 4×10^6 s after a short increasing start-up, to an end time of 4×10^8 s.

Find the smallest k_h in that interval such that the gas saturation at the cell centred at (2.5, 2.5, 0.417) m at t = 8×10^7 s is strictly less than 0.4000. Report k_h in m² (non-negative). The interval contains a single crossing. Answers within 1.0% relative are accepted.


### Ground Truth

1.4355468750000002e-15 m^2


### No-Tool Answer

Interpreting “smallest” as the crossing value (infimum), my estimate is

\[
\boxed{k_h \approx 1.45\times10^{-15}\ {\rm m^2}}
\]

The estimate accounts for \(k_v=0.1k_h\), counter-current gravity flux, and the imbibition hysteresis branch encountered as gas saturation decreases in the bottom cell. The strict inequality is satisfied for values just above this threshold.


### Judge


- Verdict: INCORRECT

- No-tool estimate: 1.45e-15

- No-tool conclusion: None

- Relative error percent: 1.0068027210884283

- Reasoning sound: False

- Decisive comparison: The answer commits to k_h ≈ 1.45e-15 m^2, while the simulation infimum is 1.435546875e-15 m^2; the relative error is about 1.007%, just outside the 1.0% window (about 1.421e-15–1.450e-15 m^2).

- Key discrepancy: It names kv=0.1 kh, counter-current gravity, and imbibition hysteresis but does not derive the crossing; the boxed 1.45e-15 m^2 slightly overshoots the refined Sg=0.4000 infimum.


---

## Q07

### Question

Consider isothermal two-phase gravity segregation of water and gas in a 10 m cube. The cube is meshed with hexahedra of Δx = Δy = 1 m and Δz = 2.5/3 m (cell centres at 0.5, 1.5, …, 9.5 m in x and y; 0.417, 1.25, 2.083, 3.75, …, 9.583 m in z). Flow is confined to a 3-D staircase of permeable rock; the complementary blocks are impermeable (empty of pore fluid). Permeable occupancy is:
– z ∈ [0, 2.5] m: y ∈ [0, 5] m, x ∈ [0, 10] m;
– z ∈ [2.5, 5] m: x ∈ [0, 5] m, y ∈ [0, 10] m;
– z ∈ [5, 7.5] m: y ∈ [5, 10] m, x ∈ [0, 10] m;
– z ∈ [7.5, 10] m: x ∈ [5, 10] m, y ∈ [0, 10] m.
Gravity acts downward along −z (9.81 m s⁻²). There are no wells and no open boundaries. The initial pressure is 5 MPa, uniform (not hydrostatic). The temperature is isothermal at 300 K.

The two horizontal permeabilities equal an unknown value k_h, and the vertical permeability is 0.10 k_h. k_h lies in the closed interval [3×10^{-16}, 1×10^{-14}] m². The reference porosity is 0.20 at 5 MPa, with pore-volume compressibility 1×10^{-9} Pa^{-1}.

The two components are immiscible. Surface densities are 1022 kg m⁻³ (water) and 0.9907 kg m⁻³ (gas); molar masses are 0.018 kg mol⁻¹ (water) and 0.016 kg mol⁻¹ (gas). Phase behaviour is given by tabulated dead-oil / black-oil formation-volume-factor and viscosity versus pressure.
Water, single reference point: P_ref = 3.06000001×10^7 Pa, B_w = 1.03, C_p = 4.1×10^{-10} Pa^{-1}, μ_w = 3.0×10^{-4} Pa·s.
Gas formation-volume factor B_g (m³/sm³) and viscosity μ_g (Pa·s) versus pressure P (Pa):
P = (3000000, 6000000, 9000000, 12000000, 15000000, 18000000, 21000000, 24000000, 27000000, 29500000, 31000000, 33000000, 53000000)
B_g = (0.04234, 0.02046, 0.01328, 0.00977, 0.00773, 0.006426, 0.005541, 0.004919, 0.004471, 0.004194, 0.004031, 0.00391, 0.003868)
μ_g = (0.00005344, 0.0000542, 0.00005526, 0.0000566, 0.00005818, 0.00005994, 0.00006181, 0.0000637, 0.00006559, 0.00006714, 0.00006806, 0.00006832, 0.00006935).

Drainage relative permeabilities are tabulated as follows.
Water, k_rw(S_w):
S_w = (0.22000, 0.25000, 0.30000, 0.35000, 0.40000, 0.45000, 0.50000, 0.55000, 0.60000, 0.65000, 0.66000, 0.68000, 0.72000, 0.82000, 0.91000, 1.00000)
k_rw = (0.00000, 0.00100, 0.00300, 0.01000, 0.01800, 0.03500, 0.04000, 0.05700, 0.08800, 0.14500, 0.16000, 0.19000, 0.26300, 0.45500, 0.69200, 1.)
Gas, k_rg(S_g):
S_g = (0.000, 0.010, 0.030, 0.050, 0.100, 0.150, 0.200, 0.250, 0.300, 0.350, 0.400, 0.450, 0.500, 0.550, 0.600, 0.650, 0.700, 0.750, 0.780)
k_rg = (0.00000, 0.00200, 0.00700, 0.01000, 0.02000, 0.04000, 0.07500, 0.12700, 0.18000, 0.24000, 0.31000, 0.37300, 0.46000, 0.55000, 0.64000, 0.73000, 0.82500, 0.92000, 1.00000).

Only the drainage relative-permeability curves are used; there is no hysteresis and the imbibition tables are not present.

Initial overall mole fractions are specified in two overlapping boxes: a bottom layer z ∈ [0, 1.01] m and the remainder z ∈ [0.80, 10] m, with the bottom-layer specification overwriting the overlap z ∈ [0.80, 1.01] m. The stack is inverted: the bottom layer is the gas-rich side (water mole fraction 0.10, gas 0.90); the remainder is water 0.99, gas 0.01.

Time is advanced with a maximum step of 4×10^6 s after a short increasing start-up, to an end time of 4×10^8 s.

Find the smallest k_h in that interval such that the gas saturation at the cell centred at (7.5, 7.5, 8.75) m at t = 3.96×10^8 s exceeds 0.7300. Report k_h in m² (non-negative). The interval contains a single crossing. Answers within 1.0% relative are accepted.


### Ground Truth

7.962890625000001e-15 m^2


### No-Tool Answer

\[
\boxed{k_h \approx 8.9\times10^{-15}\ {\rm m^2}}
\]

This is an estimated crossing based on the gravity-segregation timescale, including \(k_v=0.1k_h\), counter-current phase mobility, and the staircase’s effective vertical/lateral migration path. A precise value requires numerical simulation.


### Judge


- Verdict: INCORRECT

- No-tool estimate: 8.9e-15

- No-tool conclusion: None

- Relative error percent: 11.768457198920764

- Reasoning sound: False

- Decisive comparison: The answer commits to kh ≈ 8.9e-15 m^2, while the simulation crossing is 7.962890625e-15 m^2; the relative error is about 11.8%, well outside the 1.0% relative tolerance.

- Key discrepancy: A gravity-segregation timescale heuristic with kv=0.1 kh and a staircase path overestimates the smallest kh at which attic Sg exceeds 0.7300 at 3.96e8 s; the true threshold sits near 7.96e-15 m^2, not 8.9e-15 m^2.


---

## Q08

### Question

Consider isothermal two-phase gravity segregation of water and gas in a 10 m cube. The cube is meshed with hexahedra of Δx = Δy = 1 m and Δz = 2.5/3 m (cell centres at 0.5, 1.5, …, 9.5 m in x and y; 0.417, 1.25, 2.083, 3.75, …, 9.583 m in z). Flow is confined to a 3-D staircase of permeable rock; the complementary blocks are impermeable (empty of pore fluid). Permeable occupancy is:
– z ∈ [0, 2.5] m: y ∈ [0, 5] m, x ∈ [0, 10] m;
– z ∈ [2.5, 5] m: x ∈ [0, 5] m, y ∈ [0, 10] m;
– z ∈ [5, 7.5] m: y ∈ [5, 10] m, x ∈ [0, 10] m;
– z ∈ [7.5, 10] m: x ∈ [5, 10] m, y ∈ [0, 10] m.
Gravity acts downward along −z (9.81 m s⁻²). There are no wells and no open boundaries. The initial pressure is 5 MPa, uniform (not hydrostatic). The temperature is isothermal at 300 K.

The two horizontal permeabilities are k_x = k_y = 1×10^{-15} m² and the vertical permeability is k_z = 1×10^{-16} m². The reference porosity φ at 5 MPa is unknown, with pore-volume compressibility 1×10^{-9} Pa^{-1}. φ lies in the closed interval [0.15, 0.28].

The two components are immiscible. Surface densities are 1022 kg m⁻³ (water) and 0.9907 kg m⁻³ (gas); molar masses are 0.018 kg mol⁻¹ (water) and 0.016 kg mol⁻¹ (gas). Phase behaviour is given by tabulated dead-oil / black-oil formation-volume-factor and viscosity versus pressure.
Water, single reference point: P_ref = 3.06000001×10^7 Pa, B_w = 1.03, C_p = 4.1×10^{-10} Pa^{-1}, μ_w = 3.0×10^{-4} Pa·s.
Gas formation-volume factor B_g (m³/sm³) and viscosity μ_g (Pa·s) versus pressure P (Pa):
P = (3000000, 6000000, 9000000, 12000000, 15000000, 18000000, 21000000, 24000000, 27000000, 29500000, 31000000, 33000000, 53000000)
B_g = (0.04234, 0.02046, 0.01328, 0.00977, 0.00773, 0.006426, 0.005541, 0.004919, 0.004471, 0.004194, 0.004031, 0.00391, 0.003868)
μ_g = (0.00005344, 0.0000542, 0.00005526, 0.0000566, 0.00005818, 0.00005994, 0.00006181, 0.0000637, 0.00006559, 0.00006714, 0.00006806, 0.00006832, 0.00006935).

Drainage relative permeabilities are tabulated as follows.
Water, k_rw(S_w):
S_w = (0.22000, 0.25000, 0.30000, 0.35000, 0.40000, 0.45000, 0.50000, 0.55000, 0.60000, 0.65000, 0.66000, 0.68000, 0.72000, 0.82000, 0.91000, 1.00000)
k_rw = (0.00000, 0.00100, 0.00300, 0.01000, 0.01800, 0.03500, 0.04000, 0.05700, 0.08800, 0.14500, 0.16000, 0.19000, 0.26300, 0.45500, 0.69200, 1.)
Gas, k_rg(S_g):
S_g = (0.000, 0.010, 0.030, 0.050, 0.100, 0.150, 0.200, 0.250, 0.300, 0.350, 0.400, 0.450, 0.500, 0.550, 0.600, 0.650, 0.700, 0.750, 0.780)
k_rg = (0.00000, 0.00200, 0.00700, 0.01000, 0.02000, 0.04000, 0.07500, 0.12700, 0.18000, 0.24000, 0.31000, 0.37300, 0.46000, 0.55000, 0.64000, 0.73000, 0.82500, 0.92000, 1.00000).

Imbibition relative permeabilities, used together with the drainage tables under history-dependent hysteresis (scanning between the two curves), are:
Water, k_rw(S_w):
S_w = (0.22000, 0.25000, 0.30000, 0.35000, 0.40000, 0.45000, 0.50000, 0.55000, 0.60000, 0.65000, 0.66000, 0.70000)
k_rw = (0, 0.0156, 0.0680, 0.1409, 0.2296, 0.3317, 0.4455, 0.5700, 0.7044, 0.8479, 0.8776, 0.9382)
Gas, k_rg(S_g):
S_g = (0.300, 0.350, 0.400, 0.450, 0.500, 0.550, 0.600, 0.650, 0.700, 0.750, 0.780)
k_rg = (0.0000, 0.03361965, 0.09509072, 0.17469281, 0.26895718, 0.37587908, 0.49410588, 0.62264458, 0.76072577, 0.90773047, 1.).

Both drainage and imbibition relative-permeability tables are used, with history-dependent hysteresis (scanning between the two curves).

Initial overall mole fractions are specified in two overlapping boxes: a bottom layer z ∈ [0, 1.01] m and the remainder z ∈ [0.80, 10] m, with the bottom-layer specification overwriting the overlap z ∈ [0.80, 1.01] m. The stack is inverted: the bottom layer is the gas-rich side (water mole fraction 0.10, gas 0.90); the remainder is water 0.99, gas 0.01.

Time is advanced with a maximum step of 4×10^6 s after a short increasing start-up, to an end time of 4×10^8 s.

At t = 8×10^7 s the gas saturation at the cell centred at (2.5, 2.5, 0.417) m is 0.5000. Determine φ. The interval contains a single value consistent with that observation. Answers within 1.0% relative are accepted.


### Ground Truth

0.17851562499999998


### No-Tool Answer

\[
\boxed{\phi \approx 0.200}
\]

Thus the reference porosity is approximately **20%**.

This is consistent with the gravity-segregation timescale \(t\propto\phi/k_z\). Converting the initial mole fractions gives approximately \(S_g=0.996\) in the bottom layer and \(S_g=0.20\) above it. With \(k_z=10^{-16}\,\mathrm{m^2}\), the tabulated hysteretic mobilities, and the roughly \(956\,\mathrm{kg\,m^{-3}}\) density contrast, reaching \(S_g=0.5000\) after \(8\times10^7\) s corresponds to \(\phi\simeq0.20\).


### Judge


- Verdict: INCORRECT

- No-tool estimate: 0.2

- No-tool conclusion: None

- Relative error percent: 12.035010940919053

- Reasoning sound: False

- Decisive comparison: The answer commits to φ ≈ 0.200, while the simulation value is 0.1785; the relative error is about 12%, well outside the 1.0% relative tolerance.

- Key discrepancy: It maps Sg=0.5000 onto the baseline porosity 0.20 with a t∝φ/kz gravity-segregation timescale, instead of inverting the still-transient anisotropic staircase, which matches at φ≈0.1785.


---

## Q09

### Question

Consider isothermal two-phase gravity segregation of water and gas in a 10 m cube. The cube is meshed with hexahedra of Δx = Δy = 1 m and Δz = 2.5/3 m (cell centres at 0.5, 1.5, …, 9.5 m in x and y; 0.417, 1.25, 2.083, 3.75, …, 9.583 m in z). Flow is confined to a 3-D staircase of permeable rock; the complementary blocks are impermeable (empty of pore fluid). Permeable occupancy is:
– z ∈ [0, 2.5] m: y ∈ [0, 5] m, x ∈ [0, 10] m;
– z ∈ [2.5, 5] m: x ∈ [0, 5] m, y ∈ [0, 10] m;
– z ∈ [5, 7.5] m: y ∈ [5, 10] m, x ∈ [0, 10] m;
– z ∈ [7.5, 10] m: x ∈ [5, 10] m, y ∈ [0, 10] m.
Gravity acts downward along −z (9.81 m s⁻²). There are no wells and no open boundaries. The initial pressure is 5 MPa, uniform (not hydrostatic). The temperature is isothermal at 300 K.

The two horizontal permeabilities equal an unknown value k_h, and the vertical permeability is 0.10 k_h. k_h lies in the closed interval [3×10^{-16}, 9×10^{-15}] m². The reference porosity is 0.20 at 5 MPa, with pore-volume compressibility 1×10^{-9} Pa^{-1}.

The two components are immiscible. Surface densities are 1022 kg m⁻³ (water) and 0.9907 kg m⁻³ (gas); molar masses are 0.018 kg mol⁻¹ (water) and 0.016 kg mol⁻¹ (gas). Phase behaviour is given by tabulated dead-oil / black-oil formation-volume-factor and viscosity versus pressure.
Water, single reference point: P_ref = 3.06000001×10^7 Pa, B_w = 1.03, C_p = 4.1×10^{-10} Pa^{-1}, μ_w = 3.0×10^{-4} Pa·s.
Gas formation-volume factor B_g (m³/sm³) and viscosity μ_g (Pa·s) versus pressure P (Pa):
P = (3000000, 6000000, 9000000, 12000000, 15000000, 18000000, 21000000, 24000000, 27000000, 29500000, 31000000, 33000000, 53000000)
B_g = (0.04234, 0.02046, 0.01328, 0.00977, 0.00773, 0.006426, 0.005541, 0.004919, 0.004471, 0.004194, 0.004031, 0.00391, 0.003868)
μ_g = (0.00005344, 0.0000542, 0.00005526, 0.0000566, 0.00005818, 0.00005994, 0.00006181, 0.0000637, 0.00006559, 0.00006714, 0.00006806, 0.00006832, 0.00006935).

Drainage relative permeabilities are tabulated as follows.
Water, k_rw(S_w):
S_w = (0.22000, 0.25000, 0.30000, 0.35000, 0.40000, 0.45000, 0.50000, 0.55000, 0.60000, 0.65000, 0.66000, 0.68000, 0.72000, 0.82000, 0.91000, 1.00000)
k_rw = (0.00000, 0.00100, 0.00300, 0.01000, 0.01800, 0.03500, 0.04000, 0.05700, 0.08800, 0.14500, 0.16000, 0.19000, 0.26300, 0.45500, 0.69200, 1.)
Gas, k_rg(S_g):
S_g = (0.000, 0.010, 0.030, 0.050, 0.100, 0.150, 0.200, 0.250, 0.300, 0.350, 0.400, 0.450, 0.500, 0.550, 0.600, 0.650, 0.700, 0.750, 0.780)
k_rg = (0.00000, 0.00200, 0.00700, 0.01000, 0.02000, 0.04000, 0.07500, 0.12700, 0.18000, 0.24000, 0.31000, 0.37300, 0.46000, 0.55000, 0.64000, 0.73000, 0.82500, 0.92000, 1.00000).

Only the drainage relative-permeability curves are used; there is no hysteresis and the imbibition tables are not present.

Initial overall mole fractions are specified in two overlapping boxes: a bottom layer z ∈ [0, 1.01] m and the remainder z ∈ [0.80, 10] m, with the bottom-layer specification overwriting the overlap z ∈ [0.80, 1.01] m. The stack is inverted: the bottom layer is the gas-rich side (water mole fraction 0.10, gas 0.90); the remainder is water 0.99, gas 0.01.

Time is advanced with a maximum step of 4×10^6 s after a short increasing start-up, to an end time of 4×10^8 s.

At t = 3.96×10^8 s the gas saturation at the cell centred at (7.5, 7.5, 8.75) m is 0.7200. Determine k_h in m². The interval contains a single value consistent with that observation. Answers within 1.0% relative are accepted.


### Ground Truth

6.787109375e-15 m^2


### No-Tool Answer

\[
\boxed{k_h \approx 3.00\times10^{-15}\ {\rm m^2}}
\]

Thus the vertical permeability is \(k_v=0.10k_h\approx3.00\times10^{-16}\ {\rm m^2}\).


### Judge


- Verdict: INCORRECT

- No-tool estimate: 3e-15

- No-tool conclusion: None

- Relative error percent: -55.79856115107914

- Reasoning sound: False

- Decisive comparison: The answer commits to 3.00e-15 m^2, while the simulation truth is 6.787109375e-15 m^2; the relative error is about 56%, far outside the 1% window.

- Key discrepancy: It reports 3.00e-15 m^2, a round lower-end value in the allowed interval, rather than the refined inversion of Sg=0.7200 at the top-north cell.


---

## Q10

### Question

Consider isothermal two-phase gravity segregation of water and gas in a 10 m cube. The cube is meshed with hexahedra of Δx = Δy = 1 m and Δz = 2.5/3 m (cell centres at 0.5, 1.5, …, 9.5 m in x and y; 0.417, 1.25, 2.083, 3.75, …, 9.583 m in z). Flow is confined to a 3-D staircase of permeable rock; the complementary blocks are impermeable (empty of pore fluid). Permeable occupancy is:
– z ∈ [0, 2.5] m: y ∈ [0, 5] m, x ∈ [0, 10] m;
– z ∈ [2.5, 5] m: x ∈ [0, 5] m, y ∈ [0, 10] m;
– z ∈ [5, 7.5] m: y ∈ [5, 10] m, x ∈ [0, 10] m;
– z ∈ [7.5, 10] m: x ∈ [5, 10] m, y ∈ [0, 10] m.
Gravity acts downward along −z (9.81 m s⁻²). There are no wells and no open boundaries. The initial pressure is 5 MPa, uniform (not hydrostatic). The temperature is isothermal at 300 K.

The two horizontal permeabilities equal an unknown value k_h, and the vertical permeability is 0.10 k_h. k_h lies in the closed interval [3×10^{-16}, 1×10^{-14}] m². The reference porosity is 0.20 at 5 MPa, with pore-volume compressibility 1×10^{-9} Pa^{-1}.

The two components are immiscible. Surface densities are 1022 kg m⁻³ (water) and 0.9907 kg m⁻³ (gas); molar masses are 0.018 kg mol⁻¹ (water) and 0.016 kg mol⁻¹ (gas). Phase behaviour is given by tabulated dead-oil / black-oil formation-volume-factor and viscosity versus pressure.
Water, single reference point: P_ref = 3.06000001×10^7 Pa, B_w = 1.03, C_p = 4.1×10^{-10} Pa^{-1}, μ_w = 3.0×10^{-4} Pa·s.
Gas formation-volume factor B_g (m³/sm³) and viscosity μ_g (Pa·s) versus pressure P (Pa):
P = (3000000, 6000000, 9000000, 12000000, 15000000, 18000000, 21000000, 24000000, 27000000, 29500000, 31000000, 33000000, 53000000)
B_g = (0.04234, 0.02046, 0.01328, 0.00977, 0.00773, 0.006426, 0.005541, 0.004919, 0.004471, 0.004194, 0.004031, 0.00391, 0.003868)
μ_g = (0.00005344, 0.0000542, 0.00005526, 0.0000566, 0.00005818, 0.00005994, 0.00006181, 0.0000637, 0.00006559, 0.00006714, 0.00006806, 0.00006832, 0.00006935).

Drainage relative permeabilities are tabulated as follows.
Water, k_rw(S_w):
S_w = (0.22000, 0.25000, 0.30000, 0.35000, 0.40000, 0.45000, 0.50000, 0.55000, 0.60000, 0.65000, 0.66000, 0.68000, 0.72000, 0.82000, 0.91000, 1.00000)
k_rw = (0.00000, 0.00100, 0.00300, 0.01000, 0.01800, 0.03500, 0.04000, 0.05700, 0.08800, 0.14500, 0.16000, 0.19000, 0.26300, 0.45500, 0.69200, 1.)
Gas, k_rg(S_g):
S_g = (0.000, 0.010, 0.030, 0.050, 0.100, 0.150, 0.200, 0.250, 0.300, 0.350, 0.400, 0.450, 0.500, 0.550, 0.600, 0.650, 0.700, 0.750, 0.780)
k_rg = (0.00000, 0.00200, 0.00700, 0.01000, 0.02000, 0.04000, 0.07500, 0.12700, 0.18000, 0.24000, 0.31000, 0.37300, 0.46000, 0.55000, 0.64000, 0.73000, 0.82500, 0.92000, 1.00000).

Only the drainage relative-permeability curves are used; there is no hysteresis and the imbibition tables are not present.

Initial overall mole fractions are specified in two overlapping boxes: a bottom layer z ∈ [0, 1.01] m and the remainder z ∈ [0.80, 10] m, with the bottom-layer specification overwriting the overlap z ∈ [0.80, 1.01] m. The stack is inverted: the bottom layer is the gas-rich side (water mole fraction 0.10, gas 0.90); the remainder is water 0.99, gas 0.01.

Time is advanced with a maximum step of 4×10^6 s after a short increasing start-up, to an end time of 4×10^8 s.

Find the k_h in that interval that maximises the gas saturation at the cell centred at (7.5, 7.5, 8.75) m at t = 3.96×10^8 s, subject to the constraint that the gas saturation at the cell centred at (2.5, 2.5, 0.417) m at t = 8×10^7 s is at least 0.4000. If the maximiser is an interval, report the infimum. Report k_h in m² (non-negative). Answers within 1.0% relative are accepted.


### Ground Truth

1.3574218750000001e-15 m^2


### No-Tool Answer

\[
\boxed{k_h \approx 1.8\times10^{-15}\ {\rm m^2}}
\]

Gravity-segregation rates scale approximately with \(k_h t\). A fractional-flow shock estimate places the \(S_g=0.4000\) threshold in the bottom cell at \(8\times10^7\) s when \(k_h\approx1.8\times10^{-15}\,\mathrm{m^2}\). The upper-cell saturation increases with this segregation rate, so the constraint is active at the maximizer.


### Judge


- Verdict: INCORRECT

- No-tool estimate: 1.8e-15

- No-tool conclusion: None

- Relative error percent: 32.60431654676258

- Reasoning sound: True

- Decisive comparison: The committed estimate 1.8e-15 m^2 lies about 33% above the simulation maximiser 1.357e-15 m^2, far outside the 1.0% relative tolerance. The qualitative argument that the leftover-Sg constraint is active and that attic Sg increases with kh is right, but the shock estimate of the binding kh is not.

- Key discrepancy: Fractional-flow shock timing placed the Sg=0.4000 crossing at kh≈1.8e-15 m^2 instead of the simulated infimum 1.357e-15 m^2.


---

## Q11

### Question

Consider isothermal two-phase gravity segregation of water and gas in a 10 m cube. The cube is meshed with hexahedra of Δx = Δy = 1 m and Δz = 2.5/3 m (cell centres at 0.5, 1.5, …, 9.5 m in x and y; 0.417, 1.25, 2.083, 3.75, …, 9.583 m in z). Flow is confined to a 3-D staircase of permeable rock; the complementary blocks are impermeable (empty of pore fluid). Permeable occupancy is:
– z ∈ [0, 2.5] m: y ∈ [0, 5] m, x ∈ [0, 10] m;
– z ∈ [2.5, 5] m: x ∈ [0, 5] m, y ∈ [0, 10] m;
– z ∈ [5, 7.5] m: y ∈ [5, 10] m, x ∈ [0, 10] m;
– z ∈ [7.5, 10] m: x ∈ [5, 10] m, y ∈ [0, 10] m.
Gravity acts downward along −z (9.81 m s⁻²). There are no wells and no open boundaries. The initial pressure is 5 MPa, uniform (not hydrostatic). The temperature is isothermal at 300 K.

The two horizontal permeabilities equal an unknown value k_h, and the vertical permeability is 0.10 k_h. k_h lies in the closed interval [3×10^{-16}, 1×10^{-14}] m². The reference porosity is 0.20 at 5 MPa, with pore-volume compressibility 1×10^{-9} Pa^{-1}.

The two components are immiscible. Surface densities are 1022 kg m⁻³ (water) and 0.9907 kg m⁻³ (gas); molar masses are 0.018 kg mol⁻¹ (water) and 0.016 kg mol⁻¹ (gas). Phase behaviour is given by tabulated dead-oil / black-oil formation-volume-factor and viscosity versus pressure.
Water, single reference point: P_ref = 3.06000001×10^7 Pa, B_w = 1.03, C_p = 4.1×10^{-10} Pa^{-1}, μ_w = 3.0×10^{-4} Pa·s.
Gas formation-volume factor B_g (m³/sm³) and viscosity μ_g (Pa·s) versus pressure P (Pa):
P = (3000000, 6000000, 9000000, 12000000, 15000000, 18000000, 21000000, 24000000, 27000000, 29500000, 31000000, 33000000, 53000000)
B_g = (0.04234, 0.02046, 0.01328, 0.00977, 0.00773, 0.006426, 0.005541, 0.004919, 0.004471, 0.004194, 0.004031, 0.00391, 0.003868)
μ_g = (0.00005344, 0.0000542, 0.00005526, 0.0000566, 0.00005818, 0.00005994, 0.00006181, 0.0000637, 0.00006559, 0.00006714, 0.00006806, 0.00006832, 0.00006935).

Drainage relative permeabilities are tabulated as follows.
Water, k_rw(S_w):
S_w = (0.22000, 0.25000, 0.30000, 0.35000, 0.40000, 0.45000, 0.50000, 0.55000, 0.60000, 0.65000, 0.66000, 0.68000, 0.72000, 0.82000, 0.91000, 1.00000)
k_rw = (0.00000, 0.00100, 0.00300, 0.01000, 0.01800, 0.03500, 0.04000, 0.05700, 0.08800, 0.14500, 0.16000, 0.19000, 0.26300, 0.45500, 0.69200, 1.)
Gas, k_rg(S_g):
S_g = (0.000, 0.010, 0.030, 0.050, 0.100, 0.150, 0.200, 0.250, 0.300, 0.350, 0.400, 0.450, 0.500, 0.550, 0.600, 0.650, 0.700, 0.750, 0.780)
k_rg = (0.00000, 0.00200, 0.00700, 0.01000, 0.02000, 0.04000, 0.07500, 0.12700, 0.18000, 0.24000, 0.31000, 0.37300, 0.46000, 0.55000, 0.64000, 0.73000, 0.82500, 0.92000, 1.00000).

Only the drainage relative-permeability curves are used; there is no hysteresis and the imbibition tables are not present.

Initial overall mole fractions are specified in two overlapping boxes: a bottom layer z ∈ [0, 1.01] m and the remainder z ∈ [0.80, 10] m, with the bottom-layer specification overwriting the overlap z ∈ [0.80, 1.01] m. The stack is inverted: the bottom layer is the gas-rich side (water mole fraction 0.10, gas 0.90); the remainder is water 0.99, gas 0.01.

Time is advanced with a maximum step of 4×10^6 s after a short increasing start-up, to an end time of 4×10^8 s.

Find the k_h in that interval that maximises the mean gas saturation in the permeable 5 m × 5 m × 2.5 m block occupying x ∈ [5, 10] m, y ∈ [5, 10] m, z ∈ [7.5, 10] m at t = 3.96×10^8 s, subject to the constraint that the pressure span ΔP = P_max − P_min over the permeable staircase at t = 8×10^7 s does not exceed 5.200×10^4 Pa. If the maximiser is an interval, report the infimum. Report k_h in m² (non-negative). Answers within 1.0% relative are accepted.


### Ground Truth

8.892578125e-15 m^2


### No-Tool Answer

\[
\boxed{k_h \approx 5.0\times10^{-15}\ {\rm m^2}}
\]

The objective increases with permeability, while the \(8\times10^7\) s pressure-span constraint supplies the active upper bound. Thus the maximizing feasible permeability is approximately \(5.0\times10^{-15}\,\mathrm{m^2}\). This is a physics-based estimate without running the simulation.


### Judge


- Verdict: INCORRECT

- No-tool estimate: 5e-15

- No-tool conclusion: None

- Relative error percent: -43.7733362618054

- Reasoning sound: False

- Decisive comparison: The answer commits to k_h ≈ 5.0×10^{-15} m², while the constrained maximiser is 8.892578125×10^{-15} m²; the relative error is about 44%, far beyond the 1% relative tolerance.

- Key discrepancy: It correctly treats attic mean S_g as increasing in k_h with the ΔP ≤ 5.200×10^4 Pa bound as the active cap, but guesses ~5×10^{-15} (near the arithmetic midpoint of the search interval) instead of the simulated ΔP crossing at ~8.89×10^{-15} m².


---

## Q12

### Question

Consider isothermal two-phase gravity segregation of water and gas in a 10 m cube. The cube is meshed with hexahedra of Δx = Δy = 1 m and Δz = 2.5/3 m (cell centres at 0.5, 1.5, …, 9.5 m in x and y; 0.417, 1.25, 2.083, 3.75, …, 9.583 m in z). Flow is confined to a 3-D staircase of permeable rock; the complementary blocks are impermeable (empty of pore fluid). Permeable occupancy is:
– z ∈ [0, 2.5] m: y ∈ [0, 5] m, x ∈ [0, 10] m;
– z ∈ [2.5, 5] m: x ∈ [0, 5] m, y ∈ [0, 10] m;
– z ∈ [5, 7.5] m: y ∈ [5, 10] m, x ∈ [0, 10] m;
– z ∈ [7.5, 10] m: x ∈ [5, 10] m, y ∈ [0, 10] m.
Gravity acts downward along −z (9.81 m s⁻²). There are no wells and no open boundaries. The initial pressure is 5 MPa, uniform (not hydrostatic). The temperature is isothermal at 300 K.

The permeable rock is isotropic with permeability 1×10^{-15} m². The reference porosity is 0.20 at 5 MPa, with pore-volume compressibility 1×10^-9 Pa^{-1}.

The two components are immiscible. Surface densities are 1022 kg m⁻³ (water) and 0.9907 kg m⁻³ (gas); molar masses are 0.018 kg mol⁻¹ (water) and 0.016 kg mol⁻¹ (gas). Phase behaviour is given by tabulated dead-oil / black-oil formation-volume-factor and viscosity versus pressure.
Water, single reference point: P_ref = 3.06000001×10^7 Pa, B_w = 1.03, C_p = 4.1×10^{-10} Pa^{-1}, μ_w = 3.0×10^{-4} Pa·s.
Gas formation-volume factor B_g (m³/sm³) and viscosity μ_g (Pa·s) versus pressure P (Pa):
P = (3000000, 6000000, 9000000, 12000000, 15000000, 18000000, 21000000, 24000000, 27000000, 29500000, 31000000, 33000000, 53000000)
B_g = (0.04234, 0.02046, 0.01328, 0.00977, 0.00773, 0.006426, 0.005541, 0.004919, 0.004471, 0.004194, 0.004031, 0.00391, 0.003868)
μ_g = (0.00005344, 0.0000542, 0.00005526, 0.0000566, 0.00005818, 0.00005994, 0.00006181, 0.0000637, 0.00006559, 0.00006714, 0.00006806, 0.00006832, 0.00006935).

Drainage relative permeabilities are tabulated as follows.
Water, k_rw(S_w):
S_w = (0.22000, 0.25000, 0.30000, 0.35000, 0.40000, 0.45000, 0.50000, 0.55000, 0.60000, 0.65000, 0.66000, 0.68000, 0.72000, 0.82000, 0.91000, 1.00000)
k_rw = (0.00000, 0.00100, 0.00300, 0.01000, 0.01800, 0.03500, 0.04000, 0.05700, 0.08800, 0.14500, 0.16000, 0.19000, 0.26300, 0.45500, 0.69200, 1.)
Gas, k_rg(S_g):
S_g = (0.000, 0.010, 0.030, 0.050, 0.100, 0.150, 0.200, 0.250, 0.300, 0.350, 0.400, 0.450, 0.500, 0.550, 0.600, 0.650, 0.700, 0.750, 0.780)
k_rg = (0.00000, 0.00200, 0.00700, 0.01000, 0.02000, 0.04000, 0.07500, 0.12700, 0.18000, 0.24000, 0.31000, 0.37300, 0.46000, 0.55000, 0.64000, 0.73000, 0.82500, 0.92000, 1.00000).

Imbibition relative permeabilities, used together with the drainage tables under history-dependent hysteresis (scanning between the two curves), are:
Water, k_rw(S_w):
S_w = (0.22000, 0.25000, 0.30000, 0.35000, 0.40000, 0.45000, 0.50000, 0.55000, 0.60000, 0.65000, 0.66000, 0.70000)
k_rw = (0, 0.0156, 0.0680, 0.1409, 0.2296, 0.3317, 0.4455, 0.5700, 0.7044, 0.8479, 0.8776, 0.9382)
Gas, k_rg(S_g):
S_g = (0.300, 0.350, 0.400, 0.450, 0.500, 0.550, 0.600, 0.650, 0.700, 0.750, 0.780)
k_rg = (0.0000, 0.03361965, 0.09509072, 0.17469281, 0.26895718, 0.37587908, 0.49410588, 0.62264458, 0.76072577, 0.90773047, 1.).

Initial overall mole fractions are specified in two overlapping boxes: a bottom layer z ∈ [0, 1.01] m and the remainder z ∈ [0.80, 10] m, with the bottom-layer specification overwriting the overlap z ∈ [0.80, 1.01] m. The stack is inverted: the bottom layer is the gas-rich side (water mole fraction 0.10, gas 0.90); the remainder is water 0.99, gas 0.01.

Time is advanced with a maximum step of 4×10^6 s after a short increasing start-up, to an end time of 4×10^8 s.

Two otherwise identical cases are compared. Case H uses both the drainage and imbibition relative-permeability tables with history-dependent hysteresis. Case D uses only the drainage curves, with no hysteresis.

Is the gas saturation at the cell centred at (7.5, 7.5, 8.75) m at t = 3.96×10^8 s in Case H greater than 0.20 times the corresponding saturation in Case D? Answer yes or no.


### Ground Truth

No; the hysteretic attic gas saturation is 0.193 times the drainage-only value, which is not greater than 0.20.


### No-Tool Answer

Yes.

Buoyant gas accumulates in the upper staircase. Moreover, hysteretic imbibition reduces gas mobility and traps gas near \(S_g\approx0.30\), so Case H should retain well over 20% of the Case D gas saturation at that location.


### Judge


- Verdict: INCORRECT

- No-tool estimate: None

- No-tool conclusion: Yes; Case H attic gas saturation is greater than 0.20 times Case D.

- Relative error percent: None

- Reasoning sound: False

- Decisive comparison: The true result is No: hysteretic Sg at the top-north cell is 0.193 times the drainage-only value, which is not greater than 0.20. The no-tool answer concludes Yes and treats the attic as a gas accumulation in both cases.

- Key discrepancy: It assumes buoyant gas fills the upper staircase in Case H and is only modestly reduced by trapping near Sg≈0.30, so the ratio would exceed 0.20; hysteresis actually traps gas along the rise, leaving a drained corridor (Sg≈0.143 vs 0.744) with ratio 0.193 < 0.20.


---

## Q13

### Question

Consider isothermal two-phase gravity segregation of water and gas in a 10 m cube. The cube is meshed with hexahedra of Δx = Δy = 1 m and Δz = 2.5/3 m (cell centres at 0.5, 1.5, …, 9.5 m in x and y; 0.417, 1.25, 2.083, 3.75, …, 9.583 m in z). Flow is confined to a 3-D staircase of permeable rock; the complementary blocks are impermeable (empty of pore fluid). Permeable occupancy is:
– z ∈ [0, 2.5] m: y ∈ [0, 5] m, x ∈ [0, 10] m;
– z ∈ [2.5, 5] m: x ∈ [0, 5] m, y ∈ [0, 10] m;
– z ∈ [5, 7.5] m: y ∈ [5, 10] m, x ∈ [0, 10] m;
– z ∈ [7.5, 10] m: x ∈ [5, 10] m, y ∈ [0, 10] m.
Gravity acts downward along −z (9.81 m s⁻²). There are no wells and no open boundaries. The initial pressure is 5 MPa, uniform (not hydrostatic). The temperature is isothermal at 300 K.

The permeable rock is isotropic with permeability 1×10^{-15} m². The reference porosity is 0.20 at 5 MPa, with pore-volume compressibility 1×10^-9 Pa^{-1}.

The two components are immiscible. Surface densities are 1022 kg m⁻³ (water) and 0.9907 kg m⁻³ (gas); molar masses are 0.018 kg mol⁻¹ (water) and 0.016 kg mol⁻¹ (gas). Phase behaviour is given by tabulated dead-oil / black-oil formation-volume-factor and viscosity versus pressure.
Water, single reference point: P_ref = 3.06000001×10^7 Pa, B_w = 1.03, C_p = 4.1×10^{-10} Pa^{-1}, μ_w = 3.0×10^{-4} Pa·s.
Gas formation-volume factor B_g (m³/sm³) and viscosity μ_g (Pa·s) versus pressure P (Pa):
P = (3000000, 6000000, 9000000, 12000000, 15000000, 18000000, 21000000, 24000000, 27000000, 29500000, 31000000, 33000000, 53000000)
B_g = (0.04234, 0.02046, 0.01328, 0.00977, 0.00773, 0.006426, 0.005541, 0.004919, 0.004471, 0.004194, 0.004031, 0.00391, 0.003868)
μ_g = (0.00005344, 0.0000542, 0.00005526, 0.0000566, 0.00005818, 0.00005994, 0.00006181, 0.0000637, 0.00006559, 0.00006714, 0.00006806, 0.00006832, 0.00006935).

Drainage relative permeabilities are tabulated as follows.
Water, k_rw(S_w):
S_w = (0.22000, 0.25000, 0.30000, 0.35000, 0.40000, 0.45000, 0.50000, 0.55000, 0.60000, 0.65000, 0.66000, 0.68000, 0.72000, 0.82000, 0.91000, 1.00000)
k_rw = (0.00000, 0.00100, 0.00300, 0.01000, 0.01800, 0.03500, 0.04000, 0.05700, 0.08800, 0.14500, 0.16000, 0.19000, 0.26300, 0.45500, 0.69200, 1.)
Gas, k_rg(S_g):
S_g = (0.000, 0.010, 0.030, 0.050, 0.100, 0.150, 0.200, 0.250, 0.300, 0.350, 0.400, 0.450, 0.500, 0.550, 0.600, 0.650, 0.700, 0.750, 0.780)
k_rg = (0.00000, 0.00200, 0.00700, 0.01000, 0.02000, 0.04000, 0.07500, 0.12700, 0.18000, 0.24000, 0.31000, 0.37300, 0.46000, 0.55000, 0.64000, 0.73000, 0.82500, 0.92000, 1.00000).

Imbibition relative permeabilities, used together with the drainage tables under history-dependent hysteresis (scanning between the two curves), are:
Water, k_rw(S_w):
S_w = (0.22000, 0.25000, 0.30000, 0.35000, 0.40000, 0.45000, 0.50000, 0.55000, 0.60000, 0.65000, 0.66000, 0.70000)
k_rw = (0, 0.0156, 0.0680, 0.1409, 0.2296, 0.3317, 0.4455, 0.5700, 0.7044, 0.8479, 0.8776, 0.9382)
Gas, k_rg(S_g):
S_g = (0.300, 0.350, 0.400, 0.450, 0.500, 0.550, 0.600, 0.650, 0.700, 0.750, 0.780)
k_rg = (0.0000, 0.03361965, 0.09509072, 0.17469281, 0.26895718, 0.37587908, 0.49410588, 0.62264458, 0.76072577, 0.90773047, 1.).

Both drainage and imbibition relative-permeability tables are used, with history-dependent hysteresis (scanning between the two curves).

Time is advanced with a maximum step of 4×10^6 s after a short increasing start-up, to an end time of 4×10^8 s.

Two otherwise identical hysteretic cases are compared. Case I uses the inverted stack: the bottom layer z ∈ [0, 1.01] m is water 0.10, gas 0.90, and the remainder is water 0.99, gas 0.01 (bottom overwriting z ∈ [0.80, 1.01] m). Case S uses the stable stack: the remainder is water 0.10, gas 0.90, and the bottom layer is water 0.99, gas 0.01.

Is the permeable-staircase pressure span ΔP = P_max − P_min at t = 3.96×10^8 s in Case I more than 25 times the corresponding span in Case S? Answer yes or no.


### Ground Truth

Yes; the inverted-stack span is 27.5 times the stable-stack span, which exceeds 25.


### No-Tool Answer

No.

A late-time hydrostatic estimate gives:

- Case I: mostly water column, \(\Delta P_I \sim 90\!-\!100\) kPa.
- Case S: about 1 m water plus 9 m gas, \(\Delta P_S \sim 13\) kPa.

Thus \(\Delta P_I/\Delta P_S\) is roughly \(7\), well below \(25\). Hysteresis affects segregation rate and trapping but is unlikely to raise the late-time ratio above 25.


### Judge


- Verdict: INCORRECT

- No-tool estimate: None

- No-tool conclusion: No

- Relative error percent: None

- Reasoning sound: False

- Decisive comparison: The true result is Yes: the inverted-stack span is 27.5 times the stable-stack span (88295 Pa vs 3210 Pa), which exceeds 25. The no-tool answer concludes No from a hydrostatic ratio of about 7.

- Key discrepancy: It treats Case S as a late-time hydrostatic 1 m water + 9 m gas column (~13 kPa), but the stable hysteretic stack barely rearranges, so ΔP remains 3210 Pa and the ratio is 27.5 rather than ~7.


---

## Q14

### Question

Consider isothermal two-phase gravity segregation of water and gas in a 10 m cube. The cube is meshed with hexahedra of Δx = Δy = 1 m and Δz = 2.5/3 m (cell centres at 0.5, 1.5, …, 9.5 m in x and y; 0.417, 1.25, 2.083, 3.75, …, 9.583 m in z). Flow is confined to a 3-D staircase of permeable rock; the complementary blocks are impermeable (empty of pore fluid). Permeable occupancy is:
– z ∈ [0, 2.5] m: y ∈ [0, 5] m, x ∈ [0, 10] m;
– z ∈ [2.5, 5] m: x ∈ [0, 5] m, y ∈ [0, 10] m;
– z ∈ [5, 7.5] m: y ∈ [5, 10] m, x ∈ [0, 10] m;
– z ∈ [7.5, 10] m: x ∈ [5, 10] m, y ∈ [0, 10] m.
Gravity acts downward along −z (9.81 m s⁻²). There are no wells and no open boundaries. The initial pressure is 5 MPa, uniform (not hydrostatic). The temperature is isothermal at 300 K.

The reference porosity is 0.20 at 5 MPa, with pore-volume compressibility 1×10^{-9} Pa^{-1}. Two otherwise identical hysteretic inverted stacks are compared. In both, the two horizontal permeabilities are 1×10^{-15} m². Case I is isotropic (vertical permeability 1×10^{-15} m²). Case A has vertical permeability 1×10^{-16} m² (one-tenth of the horizontal value).

The two components are immiscible. Surface densities are 1022 kg m⁻³ (water) and 0.9907 kg m⁻³ (gas); molar masses are 0.018 kg mol⁻¹ (water) and 0.016 kg mol⁻¹ (gas). Phase behaviour is given by tabulated dead-oil / black-oil formation-volume-factor and viscosity versus pressure.
Water, single reference point: P_ref = 3.06000001×10^7 Pa, B_w = 1.03, C_p = 4.1×10^{-10} Pa^{-1}, μ_w = 3.0×10^{-4} Pa·s.
Gas formation-volume factor B_g (m³/sm³) and viscosity μ_g (Pa·s) versus pressure P (Pa):
P = (3000000, 6000000, 9000000, 12000000, 15000000, 18000000, 21000000, 24000000, 27000000, 29500000, 31000000, 33000000, 53000000)
B_g = (0.04234, 0.02046, 0.01328, 0.00977, 0.00773, 0.006426, 0.005541, 0.004919, 0.004471, 0.004194, 0.004031, 0.00391, 0.003868)
μ_g = (0.00005344, 0.0000542, 0.00005526, 0.0000566, 0.00005818, 0.00005994, 0.00006181, 0.0000637, 0.00006559, 0.00006714, 0.00006806, 0.00006832, 0.00006935).

Drainage relative permeabilities are tabulated as follows.
Water, k_rw(S_w):
S_w = (0.22000, 0.25000, 0.30000, 0.35000, 0.40000, 0.45000, 0.50000, 0.55000, 0.60000, 0.65000, 0.66000, 0.68000, 0.72000, 0.82000, 0.91000, 1.00000)
k_rw = (0.00000, 0.00100, 0.00300, 0.01000, 0.01800, 0.03500, 0.04000, 0.05700, 0.08800, 0.14500, 0.16000, 0.19000, 0.26300, 0.45500, 0.69200, 1.)
Gas, k_rg(S_g):
S_g = (0.000, 0.010, 0.030, 0.050, 0.100, 0.150, 0.200, 0.250, 0.300, 0.350, 0.400, 0.450, 0.500, 0.550, 0.600, 0.650, 0.700, 0.750, 0.780)
k_rg = (0.00000, 0.00200, 0.00700, 0.01000, 0.02000, 0.04000, 0.07500, 0.12700, 0.18000, 0.24000, 0.31000, 0.37300, 0.46000, 0.55000, 0.64000, 0.73000, 0.82500, 0.92000, 1.00000).

Imbibition relative permeabilities, used together with the drainage tables under history-dependent hysteresis (scanning between the two curves), are:
Water, k_rw(S_w):
S_w = (0.22000, 0.25000, 0.30000, 0.35000, 0.40000, 0.45000, 0.50000, 0.55000, 0.60000, 0.65000, 0.66000, 0.70000)
k_rw = (0, 0.0156, 0.0680, 0.1409, 0.2296, 0.3317, 0.4455, 0.5700, 0.7044, 0.8479, 0.8776, 0.9382)
Gas, k_rg(S_g):
S_g = (0.300, 0.350, 0.400, 0.450, 0.500, 0.550, 0.600, 0.650, 0.700, 0.750, 0.780)
k_rg = (0.0000, 0.03361965, 0.09509072, 0.17469281, 0.26895718, 0.37587908, 0.49410588, 0.62264458, 0.76072577, 0.90773047, 1.).

Both drainage and imbibition relative-permeability tables are used, with history-dependent hysteresis (scanning between the two curves).

Initial overall mole fractions are specified in two overlapping boxes: a bottom layer z ∈ [0, 1.01] m and the remainder z ∈ [0.80, 10] m, with the bottom-layer specification overwriting the overlap z ∈ [0.80, 1.01] m. The stack is inverted: the bottom layer is the gas-rich side (water mole fraction 0.10, gas 0.90); the remainder is water 0.99, gas 0.01.

Time is advanced with a maximum step of 4×10^6 s after a short increasing start-up, to an end time of 4×10^8 s.

Is the gas saturation at the cell centred at (2.5, 2.5, 0.417) m at t = 8×10^7 s in Case A more than 2.0 times the corresponding saturation in Case I? Answer yes or no.


### Ground Truth

No; the anisotropic saturation is 1.82 times the isotropic value, which is not greater than 2.0.


### No-Tool Answer

No. The tenfold lower vertical permeability delays gas removal, but by \(8\times10^7\) s the expected Case A saturation is not more than twice Case I’s saturation.


### Judge


- Verdict: CORRECT

- No-tool estimate: None

- No-tool conclusion: No; Case A saturation is not more than twice Case I.

- Relative error percent: None

- Reasoning sound: True

- Decisive comparison: The answer's no matches the true statement: the anisotropic bottom-cell gas saturation is 1.82 times the isotropic value, which is not greater than 2.0. It correctly treats the tenfold drop in vertical permeability as delaying gas rise from the inverted stack rather than scaling leftover saturation by ten.

- Key discrepancy: None


---

## Q15

### Question

Consider isothermal two-phase gravity segregation of water and gas in a 10 m cube. The cube is meshed with hexahedra of Δx = Δy = 1 m and Δz = 2.5/3 m (cell centres at 0.5, 1.5, …, 9.5 m in x and y; 0.417, 1.25, 2.083, 3.75, …, 9.583 m in z). Flow is confined to a 3-D staircase of permeable rock; the complementary blocks are impermeable (empty of pore fluid). Permeable occupancy is:
– z ∈ [0, 2.5] m: y ∈ [0, 5] m, x ∈ [0, 10] m;
– z ∈ [2.5, 5] m: x ∈ [0, 5] m, y ∈ [0, 10] m;
– z ∈ [5, 7.5] m: y ∈ [5, 10] m, x ∈ [0, 10] m;
– z ∈ [7.5, 10] m: x ∈ [5, 10] m, y ∈ [0, 10] m.
Gravity acts downward along −z (9.81 m s⁻²). There are no wells and no open boundaries. The initial pressure is 5 MPa, uniform (not hydrostatic). The temperature is isothermal at 300 K.

The permeable rock is isotropic with permeability 1×10^{-15} m². The reference porosity is 0.20 at 5 MPa, with pore-volume compressibility 1×10^-9 Pa^{-1}.

The two components are immiscible. Surface densities are 1022 kg m⁻³ (water) and 0.9907 kg m⁻³ (gas); molar masses are 0.018 kg mol⁻¹ (water) and 0.016 kg mol⁻¹ (gas). Phase behaviour is given by tabulated dead-oil / black-oil formation-volume-factor and viscosity versus pressure.
Water, single reference point: P_ref = 3.06000001×10^7 Pa, B_w = 1.03, C_p = 4.1×10^{-10} Pa^{-1}, μ_w = 3.0×10^{-4} Pa·s.
Gas formation-volume factor B_g (m³/sm³) and viscosity μ_g (Pa·s) versus pressure P (Pa):
P = (3000000, 6000000, 9000000, 12000000, 15000000, 18000000, 21000000, 24000000, 27000000, 29500000, 31000000, 33000000, 53000000)
B_g = (0.04234, 0.02046, 0.01328, 0.00977, 0.00773, 0.006426, 0.005541, 0.004919, 0.004471, 0.004194, 0.004031, 0.00391, 0.003868)
μ_g = (0.00005344, 0.0000542, 0.00005526, 0.0000566, 0.00005818, 0.00005994, 0.00006181, 0.0000637, 0.00006559, 0.00006714, 0.00006806, 0.00006832, 0.00006935).

Drainage relative permeabilities are tabulated as follows.
Water, k_rw(S_w):
S_w = (0.22000, 0.25000, 0.30000, 0.35000, 0.40000, 0.45000, 0.50000, 0.55000, 0.60000, 0.65000, 0.66000, 0.68000, 0.72000, 0.82000, 0.91000, 1.00000)
k_rw = (0.00000, 0.00100, 0.00300, 0.01000, 0.01800, 0.03500, 0.04000, 0.05700, 0.08800, 0.14500, 0.16000, 0.19000, 0.26300, 0.45500, 0.69200, 1.)
Gas, k_rg(S_g):
S_g = (0.000, 0.010, 0.030, 0.050, 0.100, 0.150, 0.200, 0.250, 0.300, 0.350, 0.400, 0.450, 0.500, 0.550, 0.600, 0.650, 0.700, 0.750, 0.780)
k_rg = (0.00000, 0.00200, 0.00700, 0.01000, 0.02000, 0.04000, 0.07500, 0.12700, 0.18000, 0.24000, 0.31000, 0.37300, 0.46000, 0.55000, 0.64000, 0.73000, 0.82500, 0.92000, 1.00000).

Imbibition relative permeabilities, used together with the drainage tables under history-dependent hysteresis (scanning between the two curves), are:
Water, k_rw(S_w):
S_w = (0.22000, 0.25000, 0.30000, 0.35000, 0.40000, 0.45000, 0.50000, 0.55000, 0.60000, 0.65000, 0.66000, 0.70000)
k_rw = (0, 0.0156, 0.0680, 0.1409, 0.2296, 0.3317, 0.4455, 0.5700, 0.7044, 0.8479, 0.8776, 0.9382)
Gas, k_rg(S_g):
S_g = (0.300, 0.350, 0.400, 0.450, 0.500, 0.550, 0.600, 0.650, 0.700, 0.750, 0.780)
k_rg = (0.0000, 0.03361965, 0.09509072, 0.17469281, 0.26895718, 0.37587908, 0.49410588, 0.62264458, 0.76072577, 0.90773047, 1.).

Both drainage and imbibition relative-permeability tables are used, with history-dependent hysteresis (scanning between the two curves).

Initial overall mole fractions are specified in two overlapping boxes: a bottom layer z ∈ [0, 1.01] m and the remainder z ∈ [0.80, 10] m, with the bottom-layer specification overwriting the overlap z ∈ [0.80, 1.01] m. The stack is gravitationally stable: the top of the domain (the remainder) is the gas-rich side (water mole fraction 0.10, gas 0.90); the bottom layer is water 0.99, gas 0.01.

Time is advanced with a maximum step of 4×10^6 s after a short increasing start-up, to an end time of 4×10^8 s.

Does the gas saturation at the cell centred at (2.5, 2.5, 0.417) m at t = 3.96×10^8 s exceed 0.18? Answer yes or no.


### Ground Truth

Yes; the west-bottom gas saturation remains 0.198, which exceeds 0.18.


### No-Tool Answer

No. The bottom cell undergoes water imbibition as gas segregates upward; over \(3.96\times10^8\) s, its gas saturation is expected to fall below 0.18.


### Judge


- Verdict: INCORRECT

- No-tool estimate: None

- No-tool conclusion: No

- Relative error percent: None

- Reasoning sound: False

- Decisive comparison: The true result is yes: west-bottom gas saturation remains 0.198, which exceeds 0.18. The no-tool answer concludes no and expects Sg to fall below 0.18.

- Key discrepancy: It treats the bottom cell as draining by upward gas segregation and water imbibition, missing that a 1% gas mole fraction flashes to Sg ≈ 0.198 and the gravitationally stable stack does not drain that cell.
