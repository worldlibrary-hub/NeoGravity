# NeoGravity Verification Suite

Companion computational materials for **The Theory of NeoGravity & Ether Dynamics**

**John Salvatore Guagliardo**, Independent Researcher\
ORCID: [0000-0003-0756-6886](https://orcid.org/0000-0003-0756-6886)\
Archived DOI: [10.5281/zenodo.22087714](https://doi.org/10.5281/zenodo.22087714)

**Version 4.0 · 6 September 2026.** Supersedes version 3.1 (3 September 2026), which
superseded version 2.0. What changed at each step, and why, is set out at the end of
this file; a reviewer who ran an earlier release should read that section first.

---

## Purpose

Every central mathematical claim in the series is reduced here to executable
code. A reviewer can verify the derivation chain rather than checking algebra by
hand.

The suite is deliberately adversarial toward its own theory. It marks `[WRONG]`
on phrasings that overclaim, states which quantity is fitted rather than derived,
and identifies the results that are *not* independent confirmation. It exits
non-zero if any check fails.

## Running

```bash
pip install sympy numpy
python3 verify_neogravity.py
```

Output is reproduced verbatim in `sample_output.txt`. One file is all that ships:
the four per-paper scripts written in September 2026 have been folded in as
Claims 6, 13 and 14 rather than deposited separately.

---

## Conventions

| Term | Definition |
|---|---|
| **Ether Plenum** (The Modern Ether) | The continuous, Lorentz-invariant medium proposed to fill space: quantum-vacuum zero-point energy, the Higgs field vacuum expectation value, and the universal electromagnetic background. |
| **Radiative Undertow** | The **inward**-directed reaction load returned by the Ether Plenum on matter, under Newton's Third Law, in response to the outward transport of mass-energy. Identified with gravitational attraction. |
| **Ether Density** (ρ_ether) | Local mass-energy density of the Plenum. **Increases** toward a gravitating mass. |
| **Ambient density** | ρ₀ = 4.645 × 10⁻³¹ kg m⁻³, from the CMB temperature by Stefan–Boltzmann and E = mc². |
| **Equation of state** | w = 1/3, **derived** from the traceless stress tensor of any massless field. Not fitted. |
| **Equilibrium profile** | ρ(r) = ρ₀ exp[3GM/(c²r)], from hydrostatic balance with w = 1/3. |
| **Refractive index** | n = (ρ/ρ₀)^k with k = 2/3, exactly. Equivalently n(r) = exp(2GM/rc²). A denser medium slows light, as glass does. The linear form n ≈ 1 + 2GM/rc² is its first-order expansion, not the framework's index; no prediction may rest on the expansion. |

**The kinematic–dynamic boundary.** A medium account reproduces the *kinematics*
of general relativity — how signals propagate through a given background —
without thereby reproducing its *dynamics*, what determines that background.
Every result below is a statement about propagation. Every open problem is a
statement about sourcing. Passing every kinematic test is necessary and not
sufficient.

---

## What is checked

| # | Claim | Method |
|---|---|---|
| 1 | Hydrostatic equilibrium of the Plenum | SymPy `dsolve` on a first-order ODE |
| 2 | The exponential is not a 1/r power law | Series expansion at large r |
| 3 | **w = 1/3, forced by the traceless stress tensor** | Trace of the stress tensor of a massless field |
| 4 | Ambient density ρ₀ from the CMB | Stefan–Boltzmann and E = mc² |
| 5 | **Calibration of the optical exponent k = 2/3** | First-order coefficient solved against the measured deflection |
| 6 | Second-order solar-limb deflection, 0.73 μas | Taylor expansion of both indices; closed form π·Δa₂·x² |
| 7 | Mercury perihelion advance | Secular advance formula |
| 8 | Gravitational redshift and Shapiro delay | Closed-form evaluation |
| 9 | Photon-capture diameter b_c = 2e·GM/c² | Stationary point of b(r) = n(r)·r |
| 10 | Frame dragging: topology, and R_eff as definitional | Explicit statement of what is matched |
| 11 | Two constraints on the Undertow mechanism | Luminosity-to-mass ratios against MICROSCOPE; radiation pressure against gravity |
| 12 | Hellings–Downs from the transverse-traceless family | Correlation evaluated across separation |
| 13 | The compression residue κ_L, bounded | Kramer et al. (2021) double-pulsar precision |
| 14 | The withdrawn vorticity account of galactic rotation | Recorded as withdrawn |
| 15 | A potential body force sources the compression branch only | curl grad Φ = 0, symbolically |
| 16 | The relaxational source rule κ_L = κ₀/(ωτ_s)², a MODEL | Settling time bounded by the double pulsar |
| 17 | The wave-sector energy is coupling-set field energy, not the medium's inertia | Ratio to the medium's inertial energy computed; recorded as a postulate |
| 18 | The relaxation window's top is the Hubble time; a galaxy lies below it | 1/H₀ against the window; the galactic Deborah crossing |
| 19 | The transverse source at the double pulsar, and what P4 viscous coupling gives | Required solenoidal force against Stokes entrainment across the window |
| — | Dimensional consistency | The density-gradient law reduced to Newton |

---

## Epistemic status

**DERIVED** — follows from the postulates with no free parameters:

- Ambient density ρ₀ = 4.645 × 10⁻³¹ kg m⁻³, from the CMB
- Inverse-square form of the Undertow (spherical shell geometry in ℝ³)
- **The equation of state w = 1/3**, forced by the traceless stress tensor of any
  massless field, not fitted
- Equilibrium density profile and refractive index form
- The temporal response coefficient, from energy conservation alone
- The density-gradient law a = −(c²/3)∇ln ρ, which contains no mass, no
  separation and no gravitational constant, and recovers Newton exactly
- Mercury's perihelion advance, 42.98″/century against 42.98 ± 0.04
- Gravitational redshift
- Shapiro time delay
- The transverse-traceless wave sector, and with it the Hellings–Downs
  inter-pulsar correlation
- Rotational frame dragging

**FITTED** — one quantity:

- `k = 2/3`, the optical exponent, equivalently the parametrized post-Newtonian
  parameter **γ**, which every metric theory of gravitation carries and none
  derives from first principles. Calibrated on the measured solar light
  deflection.

A second constant governing the frame-dragging amplitude was fitted in Paper 12
and has since been retired as definitional: R_eff is defined by Ω R_eff³ = 2GJ/c²
and carries no independent content, so the ratio it is checked against returns 1
by construction.

**PREDICTED, AND NOT YET MEASURABLE:**

- A photon-capture diameter b_c = 2e·GM/c² ≈ 5.437 GM/c² against the
  Schwarzschild 3√3 ≈ 5.196 — a **4.63 %** excess, mass-independent, at zeroth
  order in spin
- A second-order solar-limb deflection differing from general relativity by
  **0.73 μas** (0.7298 = π·Δa₂·x²), roughly thirty times below current
  astrometric precision

**BOUNDED, NOT DERIVED:**

- The compression residue κ_L < 1.3 × 10⁻⁴, from the double pulsar's own
  published precision. Order-counting puts it near 4 × 10⁻⁶, some thirty times
  inside that bound. **What the series has not derived is the coefficient itself.** No
  computation of this coefficient from the continuum equations exists; producing
  one is the outstanding task, and the elastic reading is withdrawn if the
  computed value exceeds the bound
- The scalar-longitudinal amplitude of the nanohertz background, below
  4.2 × 10⁻¹⁷ (Wu et al. 2022) — a second and independent handle, four decades
  lower in frequency


**TOPOLOGY ONLY** — shared functional form, physically distinct mechanism:

- The frame-dragging dipole sin(θ)/r²

**CONSTRAINT** — required by observation, not supplied by the theory:

- The coupling tracks total mass-energy, not thermal luminosity. Comparing the
  Sun's luminosity-to-mass ratio with the Earth's total infrared emission — the
  conservative of the two defensible readings, and the one the series' FAQ
  quotes — leaves a disparity near 9,400, against MICROSCOPE's 10⁻¹⁵ bound on
  composition-dependent free fall. Taking the Earth's own internal heat instead
  gives 2.4 × 10⁷; the suite prints both and argues from the smaller

---

## Corrections enforced here

1. **exp(A/r) is not a 1/r power law.** The 1/r dependence sits in the exponent;
   a 1/r perturbation appears only at first order. Manuscripts claiming the
   integration "produces a 1/r profile" are wrong as phrased.

2. **The exponential index is exact, and the linear form is only its expansion.**
   A prediction resting on n ≈ 1 + 2GM/rc² is void: a linear index has no
   stationary point in b(r) = n(r)·r and therefore yields no photon capture and
   no shadow at all.

3. **Frame dragging is not "algebraically identical" to Stokes flow.** Stokes
   creeping flow requires viscosity and a no-slip boundary; Kerr is a vacuum
   solution. They share dipole topology only.

4. **Earth's moment of inertia is I = 0.3307 M R², not (2/5)M R².** Earth is
   centrally condensed; the uniform-sphere value overstates J by 21 % and yields
   an incorrect R_eff near 5.24 km. Any effective radius must be quoted with the
   convention that fixes it, or it is not a number.

5. **Light deflection is not independent confirmation.** The optical exponent was
   calibrated on that measurement. The Shapiro delay is a same-parameter
   consistency check rather than an independent success, and the redshift is a
   temporal input to the calibration. The genuinely independent success is
   Mercury's perihelion advance.

6. **Radiation pressure is not the Undertow.** Measured solar radiation pressure
   is 6.1 × 10¹³ times too weak, and points outward rather than inward.

---

## Constants

CODATA 2022 and IAU 2015 nominal solar values, declared at the top of the script.
Every constant used is either exactly defined or unchanged from CODATA 2018.

## Citation

> Guagliardo, J. S. (2026). *NeoGravity verification suite: Computational checks
> for the Theory of NeoGravity & Ether Dynamics* (Version 4.0) [Computer
> software]. Zenodo. https://doi.org/10.5281/zenodo.22087714

## License

Released for verification and reuse. Attribution appreciated.

