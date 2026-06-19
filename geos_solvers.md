# GEOS Available Solvers and Simulators

A complete list of physics solvers available in GEOS, organized by category. These are specified as XML elements inside the `<Solvers>` block of a GEOS input file.

---

## Wave Propagation

| Solver | Description |
|--------|-------------|
| `AcousticSEM` | Acoustic wave propagation using the spectral element method. |
| `AcousticFirstOrderSEM` | First-order acoustic wave equation solver using SEM. |
| `AcousticDG` | Acoustic wave propagation using the discontinuous Galerkin method. |
| `AcousticVTISEM` | Acoustic wave propagation in vertically transverse isotropic (VTI) media. |
| `AcousticElasticSEM` | Coupled acoustic-elastic wave propagation using SEM. |
| `ElasticSEM` | Elastic wave propagation using the spectral element method. |
| `ElasticFirstOrderSEM` | First-order elastic wave equation solver using SEM. |

---

## Single-Phase Flow

| Solver | Description |
|--------|-------------|
| `SinglePhaseFVM` | Single-phase fluid flow using the finite volume method. |
| `SinglePhaseHybridFVM` | Single-phase flow using a hybrid finite volume discretization. |
| `SinglePhaseProppantFVM` | Single-phase flow with proppant transport coupling. |
| `SinglePhaseStatistics` | Computes and outputs statistics for single-phase flow simulations. |
| `SinglePhaseWell` | Models wellbore flow for single-phase fluid systems. |
| `SinglePhaseReservoir` | Couples single-phase flow with well models for reservoir simulation. |

---

## Compositional / Multiphase Flow

| Solver | Description |
|--------|-------------|
| `CompositionalMultiphaseFVM` | Compositional multiphase flow using the finite volume method. |
| `CompositionalMultiphaseHybridFVM` | Compositional multiphase flow using hybrid FVM discretization. |
| `CompositionalMultiphaseStatistics` | Computes statistics for compositional multiphase flow simulations. |
| `CompositionalMultiphaseWell` | Models wellbore flow for compositional multiphase systems. |
| `CompositionalMultiphaseReservoir` | Couples compositional multiphase flow with well models. |
| `ImmiscibleMultiphaseFlow` | Multiphase flow for immiscible fluid systems (e.g., oil-water). |

---

## Reactive Transport

| Solver | Description |
|--------|-------------|
| `SinglePhaseReactiveTransport` | Single-phase flow coupled with reactive chemical transport. |
| `ReactiveCompositionalMultiphaseOBL` | Reactive compositional multiphase flow using operator-based linearization. |

---

## Proppant Transport

| Solver | Description |
|--------|-------------|
| `ProppantTransport` | Simulates proppant particle transport in fracture fluid flow. |
| `FlowProppantTransport` | Coupled flow and proppant transport solver. |

---

## Solid Mechanics

| Solver | Description |
|--------|-------------|
| `SolidMechanicsLagrangianFEM` | Solid mechanics using Lagrangian finite element method. |
| `SolidMechanicsLagrangianFEMInitialization` | Initialization step for the Lagrangian FEM solid mechanics solver. |
| `SolidMechanics_MPM` | Solid mechanics using the Material Point Method for large deformations. |
| `SolidMechanicsStateReset` | Resets the mechanical state (e.g., between loading stages). |
| `SolidMechanicsStatistics` | Computes and outputs statistics for solid mechanics simulations. |

---

## Contact Mechanics

| Solver | Description |
|--------|-------------|
| `SolidMechanicsLagrangeContact` | Fracture contact mechanics using Lagrange multiplier method. |
| `SolidMechanicsLagrangeContactBubbleStab` | Lagrange contact mechanics with bubble function stabilization. |
| `SolidMechanicsLagrangeContactInitialization` | Initialization for the Lagrange contact solver. |
| `SolidMechanicsAugmentedLagrangianContact` | Fracture contact mechanics using augmented Lagrangian method. |
| `SolidMechanicsAugmentedLagrangianContactInitialization` | Initialization for the augmented Lagrangian contact solver. |
| `FrictionlessContact` | Contact mechanics without friction on fracture surfaces. |
| `OneWayCoupledFractureFlowContactMechanics` | One-way coupled fracture flow with contact mechanics. |

---

## Embedded Fractures

| Solver | Description |
|--------|-------------|
| `SolidMechanicsEmbeddedFractures` | Solid mechanics with embedded discrete fracture representations (EDFM). |
| `SolidMechanicsEmbeddedFracturesInitialization` | Initialization for the embedded fractures solver. |

---

## Hydraulic Fracturing

| Solver | Description |
|--------|-------------|
| `Hydrofracture` | Fully coupled hydraulic fracture propagation solver. |
| `HydrofractureInitialization` | Initialization step for the hydraulic fracture solver. |

---

## Phase Field Fracture

| Solver | Description |
|--------|-------------|
| `PhaseFieldDamageFEM` | Phase field damage model using finite element method. |
| `PhaseFieldFracture` | Coupled phase field fracture propagation solver. |

---

## Single-Phase Poromechanics

| Solver | Description |
|--------|-------------|
| `SinglePhasePoromechanics` | Coupled single-phase flow and solid mechanics (Biot poromechanics). |
| `SinglePhasePoromechanicsInitialization` | Initialization for single-phase poromechanics. |
| `SinglePhasePoromechanicsConformingFractures` | Single-phase poromechanics with conforming fracture representations. |
| `SinglePhasePoromechanicsConformingFracturesInitialization` | Initialization for conforming fracture poromechanics. |
| `SinglePhasePoromechanicsConformingFracturesALM` | Single-phase poromechanics with conforming fractures using augmented Lagrangian. |
| `SinglePhasePoromechanicsConformingFracturesALMInitialization` | Initialization for ALM conforming fracture poromechanics. |
| `SinglePhasePoromechanicsEmbeddedFractures` | Single-phase poromechanics with embedded discrete fractures. |
| `SinglePhasePoromechanicsEmbeddedFracturesInitialization` | Initialization for embedded fracture poromechanics. |
| `SinglePhasePoromechanicsReservoir` | Single-phase poromechanics coupled with well models. |
| `SinglePhaseReservoirPoromechanics` | Reservoir simulation with single-phase poromechanics. |
| `SinglePhaseReservoirPoromechanicsConformingFractures` | Reservoir poromechanics with conforming fractures. |
| `SinglePhaseReservoirPoromechanicsConformingFracturesALM` | Reservoir poromechanics with conforming fractures and ALM contact. |
| `SinglePhaseReservoirPoromechanicsConformingFracturesALMInitialization` | Initialization for reservoir ALM conforming fracture poromechanics. |
| `SinglePhaseReservoirPoromechanicsConformingFracturesInitialization` | Initialization for reservoir conforming fracture poromechanics. |
| `SinglePhaseReservoirPoromechanicsInitialization` | Initialization for reservoir poromechanics. |
| `SinglePhasePoromechanicsConformingFracturesReservoir` | Conforming fracture poromechanics coupled with reservoir wells. |

---

## Multiphase Poromechanics

| Solver | Description |
|--------|-------------|
| `MultiphasePoromechanics` | Coupled multiphase flow and solid mechanics. |
| `MultiphasePoromechanicsInitialization` | Initialization for multiphase poromechanics. |
| `MultiphasePoromechanicsConformingFractures` | Multiphase poromechanics with conforming fracture surfaces. |
| `MultiphasePoromechanicsConformingFracturesInitialization` | Initialization for conforming fracture multiphase poromechanics. |
| `MultiphasePoromechanicsConformingFracturesALM` | Multiphase poromechanics with conforming fractures and ALM contact. |
| `MultiphasePoromechanicsConformingFracturesALMInitialization` | Initialization for ALM conforming fracture multiphase poromechanics. |
| `MultiphasePoromechanicsReservoir` | Multiphase poromechanics coupled with well models. |
| `PhaseFieldPoromechanics` | Phase field fracture coupled with poromechanics. |

---

## Compositional Multiphase Poromechanics (Reservoir)

| Solver | Description |
|--------|-------------|
| `CompositionalMultiphaseReservoirPoromechanics` | Compositional multiphase reservoir simulation with poromechanics coupling. |
| `CompositionalMultiphaseReservoirPoromechanicsInitialization` | Initialization for compositional reservoir poromechanics. |
| `CompositionalMultiphaseReservoirPoromechanicsConformingFractures` | Compositional reservoir poromechanics with conforming fractures. |
| `CompositionalMultiphaseReservoirPoromechanicsConformingFracturesInitialization` | Initialization for compositional reservoir conforming fracture poromechanics. |
| `CompositionalMultiphaseReservoirPoromechanicsConformingFracturesALM` | Compositional reservoir poromechanics with conforming fractures and ALM contact. |
| `CompositionalMultiphaseReservoirPoromechanicsConformingFracturesALMInitialization` | Initialization for compositional reservoir ALM conforming fracture poromechanics. |

---

## Induced Seismicity

| Solver | Description |
|--------|-------------|
| `SeismicityRate` | Computes seismicity rate based on rate-and-state friction and stress changes. |

---

## Multiscale Methods

| Solver | Description |
|--------|-------------|
| `Multiscale` | Multiscale preconditioner/solver for improved performance on large problems. |

---

## Well Models

| Solver | Description |
|--------|-------------|
| `InternalWell` | Internal well model for coupling wellbore flow with reservoir. |
| `InternalWellbore` | Wellbore flow model including thermal and mechanical effects. |
| `VTKWell` | Well model loaded from VTK file format. |
| `WellControls` | Specifies operating constraints (rate, pressure) for well models. |

---

## General / Coupling

| Solver | Description |
|--------|-------------|
| `Coupled` | Generic coupling solver that combines multiple physics solvers. |
| `HydrostaticEquilibrium` | Computes initial hydrostatic pressure equilibrium. |
| `LinearSolverParameters` | Configuration for the linear solver (direct, iterative, AMG, etc.). |
| `NonlinearSolverParameters` | Configuration for the nonlinear solver (Newton iterations, tolerances). |

---

## Summary

| Category | Count |
|----------|-------|
| Wave Propagation | 7 |
| Single-Phase Flow | 6 |
| Compositional / Multiphase Flow | 6 |
| Reactive Transport | 2 |
| Proppant Transport | 2 |
| Solid Mechanics | 5 |
| Contact Mechanics | 7 |
| Embedded Fractures | 2 |
| Hydraulic Fracturing | 2 |
| Phase Field Fracture | 2 |
| Single-Phase Poromechanics | 16 |
| Multiphase Poromechanics | 8 |
| Compositional Reservoir Poromechanics | 6 |
| Induced Seismicity | 1 |
| Multiscale | 1 |
| Well Models | 4 |
| General / Coupling | 4 |
| **Total** | **~81** |
