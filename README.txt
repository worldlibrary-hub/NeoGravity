# NeoGravity Verification Suite

Companion computational materials for **The Theory of NeoGravity & Ether Dynamics**

**John Salvatore Guagliardo**, Researcher, World Library Foundation\
ORCID: [0000-0003-0756-6886](https://orcid.org/0000-0003-0756-6886)\
Archive: [https://github.com/worldlibrary-hub/NeoGravity](https://github.com/worldlibrary-hub/NeoGravity) · DOI [10.5281/zenodo.22080221](https://doi.org/10.5281/zenodo.22080221)

**Version 4.2 · 17 September 2026.** Supersedes version 4.1 (14 September 2026), which
superseded 4.0 (6 September 2026), 3.1 and 2.0. **Twenty-seven claims**; version 4.0
carried nineteen. The suite prints its own version history when it runs, so a reviewer
who ran an earlier release should start the program and read the header.

---

## Where every claim comes from

Each of the twenty-seven prints the Part of the series it belongs to, the paper that
deposits it, the numbered section and, where there is one, the subsection, together
with what it recomputes, which of the five instruments it belongs to, and its
epistemic standing. A reader who wants to check a claim against the paper behind it
can go straight there.

```
==========================================================================
CLAIM 1 -- Hydrostatic equilibrium of the Ether Plenum
--------------------------------------------------------------------------
  Part III. The Law
  Gravity as Hydrodynamics, Paper 11
  Section 3. Deriving the Index  |  3.2 Hydrostatic Equilibrium
  Recomputes: rho(r) = rho_0 exp(3GM/rc^2) from the inward load under
              hydrostatic equilibrium
  The Plenum, and its constants  |  DERIVED
==========================================================================
```

The register those lines come from was **generated from the corpus rather than
typed**: paper titles from the series concordance, section titles read out of the
papers themselves, the Parts read out of the Series in Eleven Parts block. It is
frozen into the one deposited file, and a companion instrument, `check_sources.py`,
reads the papers back and verifies all twenty-seven rows character for character, so
a renamed section is caught rather than left citing a place that is no longer there.
The full register is reproduced in `claim_register.txt`.

### The five instruments

They partition the twenty-seven exactly, and the program refuses to finish if they
stop doing so.

| Instrument | Claims |
|---|---|
| The Plenum, and its constants | 1, 2, 3, 4, 5, 20, 21 |
| The solar system | 6, 7, 8, 10, 11 |
| The strong field | 9, 24, 25, 26 |
| Waves, and the bounds they set | 12, 13, 15, 16, 17, 19, 22, 23 |
| Galaxies and the expansion | 14, 18, 27 |

### The epistemic summary is generated

The closing SUMMARY OF EPISTEMIC STATUS is built from the same register the claims
are, so it cannot drift from them, and every line of it carries its claim number. The
four results the framework establishes that are not separately numbered claims are
carried in it and labelled as such, so nothing the summary used to say was lost.

### Reporting one instrument, one claim, or the register alone

```bash
python3 verify_neogravity.py                  the verification
python3 verify_neogravity.py --register       the claim register, then stop
python3 verify_neogravity.py --family strong  report one instrument
python3 verify_neogravity.py --claim 9        report one claim
python3 verify_neogravity.py --json           register and results, machine-readable
```

These select what is **reported**. The program always **computes** all twenty-seven,
because the later claims use the earlier ones' values, and a filtered run prints a
banner saying it is not the verification. `--json` is what the verification page on
NeoGravity.org is generated from, so that page cannot disagree with the program.

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
| **Ether Plenum** (The Modern Ether) | The continuous, Lorentz-invariant fluid proposed to fill space: quantum-vacuum zero-point energy, the Higgs field vacuum expectation value, and the universal electromagnetic background. |
| **Radiative Undertow** | The **inward**-directed reaction load returned by the Ether Plenum on matter, under Newton's Third Law, in response to the outward transport of mass-energy. Identified with gravitational attraction. |
| **Ether Density** (ρ_ether) | Local mass-energy density of the Plenum. **Increases** toward a gravitating mass. |
| **Ambient density** | ρ₀ = 4.645 × 10⁻³¹ kg m⁻³, from the CMB temperature by Stefan–Boltzmann and E = mc². |
| **Equation of state** | w = 1/3, **derived** from the traceless stress tensor of any massless field. Not fitted. |
| **Equilibrium profile** | ρ(r) = ρ₀ exp[3GM/(c²r)], from hydrostatic balance with w = 1/3. |
| **Refractive index** | n = (ρ/ρ₀)^k with k = 2/3, exactly. Equivalently n(r) = exp(2GM/rc²). A denser medium slows light, as glass does. The linear form n ≈ 1 + 2GM/rc² is its first-order expansion, not the framework's index; no prediction may rest on the expansion. |

**The kinematic–dynamic boundary.** A plenum account reproduces the *kinematics*
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
| 8 | Gravitational redshift and Shapiro delay | Pound–Rebka tower, z = gh/c²; Shapiro Δt = (4GM/c³)·ln(4r₁r₂/b²) |
| 9 | Photon-capture diameter b_c = 2e·GM/c² | Stationary point of b(r) = n(r)·r |
| 10 | Frame dragging: topology, and R_eff as definitional | Explicit statement of what is matched |
| 11 | Two constraints on the Undertow | Luminosity-to-mass ratios against MICROSCOPE; radiation pressure against gravity |
| 12 | Hellings–Downs from the transverse-traceless family | Correlation evaluated across separation |
| 13 | The compression residue κ_L, bounded | Kramer et al. (2021) double-pulsar precision |
| 14 | The withdrawn vorticity account of galactic rotation | Recorded as withdrawn |
| 15 | A potential body force sources the compression branch only | curl grad Φ = 0, symbolically |
| 16 | The relaxational source rule κ_L = κ₀/(ωτ_s)², a MODEL | Settling time bounded by the double pulsar |
| 17 | The wave-sector energy is coupling-set field energy, not the Plenum's inertia | Ratio to the Plenum's inertial energy computed; recorded as a postulate |
| 18 | The relaxation window's top is the Hubble time; a galaxy lies below it | 1/H₀ against the window; the galactic Deborah crossing |
| 19 | The transverse source at the double pulsar, and what P4 viscous coupling gives | Required solenoidal force against Stokes entrainment across the window |
| 20 | **β = 1, the nonlinearity parameter** | Read off the PPN perihelion coefficient with γ = 1 |
| 21 | Shear modulus μ(ρ₀) = ρ₀c², **at the ambient density only** | c_T = √(μ/ρ₀) = c, solved |
| 22 | Finding A6.1: steady amplitudes are viscosity-independent | The steady Stokes field of a rotating sphere carries no η |
| 23 | Finding A6.2: the barotropic law annihilates the baroclinic source | ∇ρ × ∇p ≡ 0 for p = p(ρ), symbolically |
| 24 | **Finding A8.1: the inflow is strictly subluminal, so there is no acoustic horizon** | v/c = √(1 − e^(−2x)); 0.795 at the capture surface; the limit at r → 0 |
| 25 | The areal radius and the wormhole rival. **Recorded, not settled** | Stationary point of R(r) = r·e^(m/r) |
| 26 | Finding A12.1: the constitutive arrow, so no time-reversed threshold | The Maxwell element under t → −t, for any τ > 0 |
| 27 | Finding A13.1: the conformal mapping and the three inherited tests | Null rays independent of a(η); the (1+z) scalings |
| — | The claim count itself | The program counts its own claims and refuses to finish if the number has drifted |
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


**TOPOLOGY ONLY** — shared functional form, physically distinct cause:

- The frame-dragging dipole sin(θ)/r²

**CONSTRAINT** — required by observation, not supplied by the theory:

- The coupling tracks total mass-energy, not thermal luminosity. Comparing the
  Sun's luminosity-to-mass ratio with the Earth's total infrared emission — the
  conservative of the two defensible readings, and the one the series' FAQ
  quotes — leaves a disparity near 9,400, against MICROSCOPE's 10⁻¹⁵ bound on
  composition-dependent free fall. Taking the Earth's own internal heat instead
  gives 2.4 × 10⁷; the suite prints both and argues from the smaller

---

## What changed from version 4.1

Taken from the program’s own header, so that the two cannot drift apart.

The compression residue is no longer bounded-and-not-derived. Claim 13 now derives it
from P1 to P5 with nothing added -- the orbit's loss to the compression branch is the
work of that branch's own reaction field on the bodies, which the reading law fixes --
and the answer, (c/c_L)^7/18 = 9.3e-3 of Peters-Mathews for the Newtonian body force and
0.23 for the drive that holds the full profile, lies ABOVE the double pulsar's bound.
That meets the retroactive-falsification clause the series set itself, so the formulation
as first written fails on that branch, and the successor formulation narrows the reading
law: matter reads the settled profile and not the compression wave. The order-counting
estimate near four parts per million is withdrawn and printed as withdrawn.

Claim 16, the relaxational source rule, is WITHDRAWN for the same run of work: the
settling time it needs is supplied neither by the postulates (the Plenum settles a
compression across the orbit in 2.27 s, four orders short) nor by the sourcing without a
lunar lag that laser ranging excludes by ten orders.

Open problems 4, 5 and 6 and the suite-task list are brought level with both.

---

## What changed from version 4.0

A reading of the corpus on 14 September found the claim list short in a way that
mattered. Every numbered **Finding** in the strong-field and cosmological papers was
outside it, and two rows of the Status Register (*The Central Roadmap*, Paper 20,
Table 3) marked **Derived** had no check behind them. Eight claims were added, 20 to
27. Each recomputes something the papers already deposit; none is new physics.

The one that matters most is **Claim 24, Finding A8.1**. Paper 28 calls it "the
sharpest internal discipline here" and marks it *Derived and verified*, and the suite
did not verify it. The framework's inflow speed √(1 − e^(−2x)) passes 0.795c at the
capture surface and approaches c only as r → 0: strictly subluminal everywhere, so
there is no sonic surface and no acoustic horizon. The standard river reaches c at
r_s; this profile never does.

**Claim 25 records a rival rather than settling it.** The areal radius of the
exponential metric has a stationary point at r = GM/c², inside the capture surface.
That is the Boonserm–Ngampitipan–Simpson–Visser wormhole reading. Whether it is a
traversable throat is a question about stress-energy, which this program cannot
adjudicate; it computes the mathematics and says so plainly. Paper 28 records the
rival as standing, and Paper 29 is the argument against it.

**Two corrections to claims version 4.0 already had**, both found by re-reading the
gate against the corpus rather than against itself:

- **Claim 8** was titled "Gravitational redshift and Shapiro delay" and computed no
  Shapiro delay at all. It also checked the *solar surface* redshift against a
  "measured 2.12 × 10⁻⁶" that no paper in the corpus states. Both repaired: the
  redshift is now computed over Pound and Rebka's own tower and reproduces the
  corpus's 2.459 × 10⁻¹⁵, the Shapiro delay reproduces the corpus's 232.6 μs, and
  the solar figure is kept as context with its false label withdrawn.
- **Claim 18** used 220 km/s for a galaxy's speed, which is the *Sun's* figure from
  Paper 39's Table 1, and printed 4.21 × 10¹⁵ s beside a citation of that paper's
  4.6 × 10¹⁵. Corrected to the galaxy's own 200 km/s, which reproduces 4.6 × 10¹⁵ s.

**The count is now asserted by the program.** The forty papers quote the number of
claims in their Data and Code Availability sections, so the number is a fact about
this program that the corpus repeats. `verify_neogravity.py` counts its own claims,
checks that they run 1 to N without a gap, and fails if either has drifted.

Nothing version 4.0 checked was dropped; the claim list is a superset.

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
> for the Theory of NeoGravity & Ether Dynamics* (Version 4.2) [Computer
> software]. https://github.com/worldlibrary-hub/NeoGravity

## License

GPL-3.0-or-later. See the LICENSE file in this repository, which governs.
In short: the suite may be used, studied, changed and redistributed, and a
redistributed version, changed or not, must carry the same terms and its source.
Attribution is appreciated beyond what the licence requires.

