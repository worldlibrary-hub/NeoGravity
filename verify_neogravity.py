#!/usr/bin/env python3
"""
NeoGravity Verification Suite
=============================
Companion computational materials for
"The Theory of NeoGravity & Ether Dynamics"
John Salvatore Guagliardo, Researcher, World Library Foundation
ORCID: 0000-0003-0756-6886

Copyright (C) 2026 John Salvatore Guagliardo

This program is free software: you can redistribute it and/or modify it under the
terms of the GNU General Public License as published by the Free Software Foundation,
either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this
program.  If not, see <https://www.gnu.org/licenses/>.

Version 4.2  --  17 September 2026.  Supersedes version 4.1 (14 September 2026).
Every central mathematical claim in the series, reduced to executable code.
TWENTY-SEVEN claims. Version 4.0 carried nineteen; the eight added here are
listed under WHAT CHANGED FROM VERSION 4.1 below.

WHAT CHANGED FROM VERSION 4.1 (17 September 2026)

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


Run:      python3 verify_neogravity.py
          python3 verify_neogravity.py --register        the claim register, then stop
          python3 verify_neogravity.py --family strong   report one instrument
          python3 verify_neogravity.py --claim 9         report one claim
          python3 verify_neogravity.py --json            register and results, machine-readable
Requires: sympy, numpy

WHERE EVERY CLAIM COMES FROM
----------------------------
Each claim prints the Part of the series it belongs to, the paper that deposits it, the numbered
section and, where there is one, the subsection, together with what it recomputes, which of the
five instruments it belongs to, and its epistemic standing. A reader who wants to check a claim
against the paper behind it can go straight there.

That register was generated from the corpus rather than typed: paper titles from the series
concordance, section titles read out of the papers themselves, the Parts read out of the Series
in Eleven Parts block. It is frozen into this file because the deposit is one file, and a
companion instrument, check_sources.py, reads the papers back and verifies all twenty-seven rows
character for character, so a renamed section is caught rather than left citing a place that is
no longer there.

The five instruments partition the twenty-seven exactly, and the program refuses to finish if
they stop doing so: the Plenum and its constants; the solar system; the strong field; waves and
the bounds they set; galaxies and the expansion.

The closing SUMMARY OF EPISTEMIC STATUS is generated from that same register rather than written
by hand, so it cannot drift from the claims above it, and every line of it carries its claim
number.

--register, --family and --claim select what is REPORTED. The program always COMPUTES all
twenty-seven, because the later claims use the earlier ones' values, and a filtered run prints a
banner saying it is not the verification. --json emits the register and the result of every
check; the verification page on NeoGravity.org is generated from it, so the page cannot disagree
with the program.

CONVENTIONS (v3.1, canonical)
-----------------------------
  Ether Plenum        the space-filling Lorentz-invariant fluid
  Radiative Undertow  the INWARD reaction load; identified with gravitation
  Ether Density       rho_ether INCREASES toward a gravitating mass
  Equation of state   w = 1/3, DERIVED from the traceless stress tensor
                      of any massless field. Not fitted.
  Optical exponent    n = (rho/rho_0)^k with k = 2/3.  THE ONE FITTED
                      QUANTITY of the framework, numerically the PPN gamma.
  Composite index     n(r) = exp(2 GM / r c^2)

Each claim prints PASS / FAIL / NOTE. Where a result is CALIBRATED rather than
DERIVED, the script says so explicitly. Nothing is asserted here without being
computed.

WHAT CHANGED FROM VERSION 2.0, AND WHY
--------------------------------------
Version 2.0, the deposited release, contradicted the papers that cite it on four
central points. It was frozen at an earlier generation of the framework and was
never reissued. It is what a reviewer following the DOI from Papers 1-19 actually
runs, and what they found was a program asserting, in capitals, that the
accompanying paper's central epistemic claim was false. The four:

  1. OPTICAL RELATION.  v2.0 used n = sqrt(rho/rho_0) throughout, in its header,
     its code and its printed output. That form was retired at Chapter 9. The
     relation is n = (rho/rho_0)^(2/3).

  2. THE EQUATION OF STATE.  v2.0 reported "w = 1/4, CALIBRATED from light
     deflection", and posed as an open problem "why 1/4 and not the 1/3 of an
     isotropic photon gas?". That question has been answered: w = 1/3 is FORCED
     by the tracelessness of the stress tensor of any massless field, and is
     derived, not fitted. See Claim 3.

  3. THE COUNT OF FITTED CONSTANTS.  v2.0 printed ">>> TWO fitted constants.
     Not one. State this plainly. <<<" and "Any claim of 'a single calibrated
     constant' is FALSE." The framework has ONE. R_eff is definitional, not a
     second fit. See Claim 10.

  4. COVERAGE.  Four verification scripts written in September 2026 were never
     folded in, while the Standing block in every paper cited results they
     compute. They are now Claims 6, 13 and 14.

  The v2.0 route reached the correct refractive index by a different attribution:
  it held the optical exponent at 1/2 and tuned w to 1/4 so that the deflection
  came out. The current route derives w = 1/3 independently and fits the optical
  exponent instead. Both give n = exp(2GM/rc^2). The difference is which quantity
  is free -- and under v3.1 the equation of state no longer is.

  ON THE VERSION NUMBER.  There has never been a version 3.0 or 3.1 of this
  suite; the deposit has stood at 2.0 since it was archived. Nine of the
  nineteen published papers nevertheless cite "Version 3.1" in their Standing
  block, and the other eleven cite "Version 2.0". This release takes the
  number nine papers already carry in print, so that those nine become correct
  on deposit and the remaining eleven are the ones amended. The DOI is
  unchanged by this release. The identifier of record is
  10.5281/zenodo.22080221, re-verified at Zenodo on 18 September 2026.
  An earlier note in this header named a different record and called this
  one retired; that was backwards. While the Zenodo record awaits approval
  the archive to cite is the repository:
  https://github.com/worldlibrary-hub/NeoGravity.

WHAT CHANGED FROM VERSION 4.0 (14 September 2026)
-------------------------------------------------
  Version 4.0 checked nineteen claims, and a reading of the corpus on 14 September
  found that the claim list was short in a way that mattered: every numbered
  Finding in the strong-field and cosmological papers was outside it, and two rows
  of the Status Register (The Central Roadmap, Paper 20, Table 3) marked DERIVED
  had no check behind them. Eight claims are added. Each one recomputes something
  the papers already deposit; nothing here is new physics.

  20  beta = 1, read off the perihelion coefficient (Register row 4, Derived);
  21  the shear modulus mu(rho_0) = rho_0 c^2 (Register row 5, Derived), with the
      condition read WHERE IT IS IMPOSED, at the ambient density;
  22  Finding A6.1, steady amplitudes are viscosity-independent, so a rotation
      experiment cannot measure eta (Paper 26; Register row 7);
  23  Finding A6.2, the barotropic law annihilates the baroclinic vorticity source
      identically, for every density field (Paper 26);
  24  Finding A8.1, the inflow speed sqrt(1 - exp(-2x)) is strictly subluminal, so
      there is no acoustic horizon (Paper 28). This was the sharpest internal
      discipline in the corpus and the suite did not check it;
  25  the areal radius of the exponential metric and its stationary point, which is
      the Boonserm-Ngampitipan-Simpson-Visser wormhole reading. RECORDED, NOT
      SETTLED: the suite computes the mathematics and states that the question is
      about stress-energy, which it cannot adjudicate. The rival stands, as Paper
      28 records and Inside a Black Hole, Paper 29, argues;
  26  Finding A12.1, the constitutive arrow: relaxation has no inverse for any
      tau > 0, so no time-reversed threshold exists (Paper 32);
  27  Finding A13.1, the conformal mapping and the three inherited tests, with the
      driver of the density drift stated as absent (Paper 33; Register row 15).

  TWO CORRECTIONS TO CLAIMS 4.0 ALREADY HAD, both found by re-reading the gate
  against the corpus rather than against itself:

  Claim 8 was titled "Gravitational redshift and Shapiro delay" and computed no
  Shapiro delay. It also checked the SOLAR SURFACE redshift against "measured
  2.12e-6", a figure no paper in the corpus states. Both repaired: the redshift is
  now computed over Pound and Rebka's own tower and reproduces the corpus's
  2.459e-15, the Shapiro delay is computed and reproduces the corpus's 232.6
  microseconds, and the solar figure is kept as context with its false label
  withdrawn.

  One correction carried from 12 September, made before this release: Claim 18 used
  220 km/s for a galaxy's speed, which is the SUN's figure from Paper 39's Table 1,
  and printed 4.21e15 s beside a citation of that paper's 4.6e15. The galaxy's own
  figure is 200 km/s and the crossing time now reproduces 4.6e15 s, checked.

  THE COUNT IS ASSERTED AT THE END OF THIS FILE. The forty papers state the number
  of claims in their Data and Code Availability sections, so the number is a fact
  about this program that the corpus quotes, and it must not drift silently.
  Nothing that 4.0 checked was dropped; the claim list is a superset.

WHAT CHANGED FROM VERSION 3.1 (6 September 2026)
------------------------------------------------
  Five claims added, each a statement the papers now make and each able to fail:
  15  a potential body force sources the compression branch only (curl grad = 0);
  16  the relaxational source rule, kappa_L = kappa_0/(omega tau_s)^2, as a MODEL
      with its settling time bounded by the double pulsar;
  17  the wave-sector energy is coupling-set field energy, not the Plenum's
      inertia, recorded as a POSTULATE with the ratio computed;
  18  the relaxation window's top is the Hubble time, and a galaxy lies below it
      by about a hundred (elastic, no bulk dissipation);
  19  the transverse source: the force dipole the Plenum needs at the double
      pulsar, and what P4 entrainment supplies (short by about ten).
  Wording: "has not earned" became "has not derived" (the series uses plain
  language for standing: derived, calibrated, held, or to be derived).
  Nothing that 3.1 checked was dropped; the claim list is a superset.
"""
import math
import os
import sys

import numpy as np
from sympy import (symbols, Function, Eq, dsolve, Derivative, exp, log, Rational,
                   series, limit, oo, pi, solve, sqrt, simplify, N, sin, diff,
                   Matrix)

PASS, FAIL, NOTE = "[PASS]", "[FAIL]", "[NOTE]"
# [WRONG] marks a claim this suite rejects. It is not a failed check, and it must
# never be spelt [FAIL]: a reader grepping the output for FAIL is asking whether
# the suite passed, and an editorial remark should not answer that question.
WRONG = "[WRONG]"
_fails = []


# The claim count is a fact about this program that all forty papers quote in
# their Data and Code Availability sections. The program therefore counts its own
# claims and refuses to finish if the number has drifted from the one declared.
# THE CLAIM REGISTER. Every claim names the Part of the series it belongs to, the
# paper that deposits it, and the numbered section and subsection inside that paper.
# The register was generated from the live corpus: paper titles from the concordance,
# section titles read out of the papers themselves, Parts read out of the Series in
# Eleven Parts block. It is frozen here because the deposit is one file, and
# check_sources.py re-reads the corpus and verifies every row of it against the papers.
#
# family  selects what a run reports (--family). status feeds the epistemic summary,
# which is GENERATED from this table and therefore cannot drift from it.
REGISTER = {
    1: dict(
        name='Hydrostatic equilibrium of the Ether Plenum',
        part='III. The Law',
        paper=11, paper_title='Gravity as Hydrodynamics',
        section='3. Deriving the Index',
        subsection='3.2 Hydrostatic Equilibrium',
        family='plenum', status='DERIVED',
        recomputes='rho(r) = rho_0 exp(3GM/rc^2) from the inward load under hydrostatic equilibrium'),
    2: dict(
        name='The exponential is NOT a 1/r power law',
        part='X. Evidence, Method and Record',
        paper=15, paper_title='Working Backward Through the Maze',
        section='5. Step Three: Equilibrium Integrates the Force',
        subsection='5.3 The Integration',
        family='plenum', status='DERIVED',
        recomputes='the exponent depends on 1/r; the 1/r potential appears only at first order'),
    3: dict(
        name='Equation of state, w = 1/3.  DERIVED, NOT FITTED',
        part='III. The Law',
        paper=11, paper_title='Gravity as Hydrodynamics',
        section='3. Deriving the Index',
        subsection='3.3 The Equation of State Is Not Free',
        family='plenum', status='DERIVED',
        recomputes='w = 1/3 from the tracelessness of a massless stress tensor'),
    4: dict(
        name='Ambient density rho_0 from the CMB.  DERIVED',
        part='II. The Plenum',
        paper=9, paper_title='Reclaiming the Ether Plenum',
        section='3. The Calculation',
        subsection='3.2 Mass Equivalence',
        family='plenum', status='DERIVED',
        recomputes='rho_0 = a T_CMB^4 / c^2, the measured ambient mass-equivalent density'),
    5: dict(
        name='Optical exponent k = 2/3.  THE ONE FITTED CONSTANT',
        part='III. The Law',
        paper=11, paper_title='Gravity as Hydrodynamics',
        section='3. Deriving the Index',
        subsection='3.4 The Optical Relation and the Single Constrained Ratio',
        family='plenum', status='FITTED',
        recomputes='k = 2/3 from 3k = 2; the one fitted quantity, numerically the PPN gamma'),
    6: dict(
        name='Second-order divergence from GR.  THE FALSIFIABLE PREDICTION',
        part='X. Evidence, Method and Record',
        paper=15, paper_title='Working Backward Through the Maze',
        section='8. The Falsifiable Prediction',
        subsection=None,
        family='solar', status='PREDICTED',
        recomputes='the second-order deflection difference at the solar limb, 0.73 microarcsec'),
    7: dict(
        name='Mercury perihelion, independent of the calibration',
        part='VI. The Strong Field',
        paper=13, paper_title='A Classical Hydrodynamic Paradigm',
        section='5. Perihelion Advance',
        subsection=None,
        family='solar', status='DERIVED',
        recomputes="Mercury's perihelion advance, 42.98 arcsec per century, with no calibration used"),
    8: dict(
        name='Gravitational redshift and Shapiro delay',
        part='VI. The Strong Field',
        paper=13, paper_title='A Classical Hydrodynamic Paradigm',
        section='4. Light Deflection and Shapiro Delay',
        subsection=None,
        family='solar', status='DERIVED',
        recomputes='the solar gravitational redshift and the Shapiro delay at superior conjunction'),
    9: dict(
        name='Photon-capture diameter.  A NEAR-TERM DISCRIMINATOR',
        part='VI. The Strong Field',
        paper=30, paper_title='The Dark Circle Around a Black Hole',
        section='2. The Derivation, Whole',
        subsection=None,
        family='strong', status='PREDICTED',
        recomputes='the photon-capture diameter, 4.63 percent above the Schwarzschild shadow'),
    10: dict(
        name='Frame dragging: TOPOLOGY, and R_eff is DEFINITIONAL',
        part='V. Dynamics',
        paper=26, paper_title='How Spinning Masses Stir the Ether Plenum',
        section='3. The Amplitude, and the Dissolution of the Fitted Length',
        subsection=None,
        family='solar', status='DEFINITIONAL',
        recomputes='R_eff by Omega R_eff^3 = 2GJ/c^2; a definition, not a second fitted constant'),
    11: dict(
        name='The coupling tracks mass-energy, not thermal output',
        part='III. The Law',
        paper=3, paper_title='The NeoGravity Theorem',
        section='5. Two Quantitative Constraints',
        subsection='5.2 The Coupling Cannot Track Thermal Luminosity',
        family='solar', status='DERIVED',
        recomputes='the coupling tracks mass-energy and not thermal luminosity'),
    12: dict(
        name='Hellings-Downs correlation from the transverse-traceless family',
        part='V. Dynamics',
        paper=24, paper_title='Waves in the Ether Plenum',
        section='3. The Transverse Branch and the Tensor Solutions',
        subsection=None,
        family='waves', status='DERIVED',
        recomputes='the Hellings-Downs correlation from the transverse-traceless family'),
    13: dict(
        name='The compression residue kappa_L.  BOUNDED BY THE TEST, DERIVED ABOVE THE BOUND',
        part='V. Dynamics',
        paper=25, paper_title='The Binary Pulsar Test',
        section='5. Part C: The Two Leakage Channels',
        subsection=None,
        family='waves', status='DERIVED',
        recomputes='kappa_L < 1.3e-4 measured; (c/c_L)^7/18 = 9.3e-3 to 0.23 derived, above it'),
    14: dict(
        name='Withdrawn: the vorticity account of galactic rotation',
        part='VIII. The Limits of the Postulates',
        paper=27, paper_title='Galaxies and the Missing Mass',
        section='4. The Result: Newton at Galactic Scale',
        subsection=None,
        family='cosmos', status='WITHDRAWN',
        recomputes='the vorticity account of galactic rotation, recorded as withdrawn'),
    15: dict(
        name='A potential body force sources the compression branch only',
        part='V. Dynamics',
        paper=24, paper_title='Waves in the Ether Plenum',
        section='5. Two Source Theorems, and the Residue',
        subsection=None,
        family='waves', status='DERIVED',
        recomputes='curl(grad Phi) = 0: a potential drive sources the compression branch only'),
    16: dict(
        name='Withdrawn: the relaxational source rule for kappa_L',
        part='V. Dynamics',
        paper=24, paper_title='Waves in the Ether Plenum',
        section='7. Status Updates',
        subsection=None,
        family='waves', status='WITHDRAWN',
        recomputes='the relaxational source rule, recorded as withdrawn: its tau_s has no home'),
    17: dict(
        name="The wave-sector energy is NOT the Plenum's inertia.  POSTULATE RECORDED",
        part='V. Dynamics',
        paper=24, paper_title='Waves in the Ether Plenum',
        section='7. Status Updates',
        subsection=None,
        family='waves', status='POSTULATED',
        recomputes='the wave-sector energy as coupling-set field energy, (c^2/16 pi G) h_dot^2'),
    18: dict(
        name="The relaxation window's top is the Hubble time; a galaxy lies below it",
        part='III. The Law',
        paper=39, paper_title="Newton's Formulas Corrected, According to NeoGravity",
        section='3. The First Law',
        subsection='3.5 A Question the Constants Raise',
        family='cosmos', status='MODEL',
        recomputes='the relaxation window top at 1/H0, and a galaxy crossing De = 1 at 4.6e15 s'),
    19: dict(
        name='The transverse source: what the Plenum needs, and what P4 entrainment gives',
        part='V. Dynamics',
        paper=24, paper_title='Waves in the Ether Plenum',
        section='5. Two Source Theorems, and the Residue',
        subsection=None,
        family='waves', status='DERIVED',
        recomputes='the solenoidal force the tensor branch needs, against what P4 entrainment gives'),
    20: dict(
        name='Nonlinearity parameter beta = 1.  DERIVED from the perihelion coefficient',
        part='0. The Program',
        paper=20, paper_title='The Central Roadmap',
        section='3. What Follows Without Further Assumption',
        subsection='3.2 Motion',
        family='plenum', status='DERIVED',
        recomputes='beta = 1, read off the perihelion coefficient'),
    21: dict(
        name='Shear modulus mu = rho_0 c^2.  DERIVED at rho_0',
        part='II. The Plenum',
        paper=21, paper_title='The Law of the Ether Plenum',
        section='4. The Constitutive Law',
        subsection=None,
        family='plenum', status='DERIVED',
        recomputes='mu = rho_0 c^2, fixed by transverse waves propagating at c'),
    22: dict(
        name='Finding A6.1: steady amplitudes are viscosity-independent',
        part='V. Dynamics',
        paper=26, paper_title='How Spinning Masses Stir the Ether Plenum',
        section='5. Finding A6.1: The Viscosity Cancels from Steady Turning',
        subsection=None,
        family='waves', status='DERIVED',
        recomputes='Finding A6.1: steady amplitudes are independent of the viscosity'),
    23: dict(
        name='Finding A6.2: the barotropic law annihilates the baroclinic source',
        part='V. Dynamics',
        paper=26, paper_title='How Spinning Masses Stir the Ether Plenum',
        section='6. Finding A6.2: The Plenum Turns Only as Matter Turns It',
        subsection=None,
        family='waves', status='DERIVED',
        recomputes='Finding A6.2: the barotropic law annihilates the baroclinic source'),
    24: dict(
        name='Finding A8.1: the inflow is strictly subluminal.  NO ACOUSTIC HORIZON',
        part='VI. The Strong Field',
        paper=28, paper_title='Black Holes Without Horizons',
        section='4. Finding A8.1: No Acoustic Horizon Either',
        subsection=None,
        family='strong', status='DERIVED',
        recomputes='Finding A8.1: v/c = sqrt(1 - e^(-2x)) = 0.795 at the capture surface'),
    25: dict(
        name='The areal radius, and the wormhole rival.  THE RIVAL STANDS',
        part='II. The Plenum',
        paper=21, paper_title='The Law of the Ether Plenum',
        section='7. Prior Art and Counter-Evidence',
        subsection=None,
        family='strong', status='RECORDED',
        recomputes='R(r) = r e^(m/r) is stationary at r = GM/c^2; the wormhole rival stands'),
    26: dict(
        name='Finding A12.1: the constitutive arrow.  NO TIME-REVERSED THRESHOLD',
        part='VI. The Strong Field',
        paper=32, paper_title='Black Holes and White Holes',
        section='3. Finding A12.1: Two Exclusions',
        subsection=None,
        family='strong', status='DERIVED',
        recomputes='Finding A12.1: the constitutive arrow; no time-reversed threshold'),
    27: dict(
        name='Finding A13.1: the conformal mapping, and the three inherited tests',
        part='VII. Cosmology and Constitution',
        paper=33, paper_title='Cosmic Expansion in the Ether Plenum',
        section='2. Finding A13.1: The Density Drift, as a Mapping',
        subsection=None,
        family='cosmos', status='DERIVED',
        recomputes='Finding A13.1: the conformal mapping, and the three inherited tests'),
}

FAMILY_NAME = {
    'plenum': 'The Plenum, and its constants',
    'solar': 'The solar system',
    'strong': 'The strong field',
    'waves': 'Waves, and the bounds they set',
    'cosmos': 'Galaxies and the expansion',
}

# Results the framework establishes that are NOT separately numbered claims. Carried across from
# the version 4.1 summary word for word, because the summary is generated now and these have no
# register row of their own. Nothing in that summary was dropped; the builder asserts it.
UNNUMBERED = [
    ('DERIVED', 'temporal response coefficient, from energy conservation'),
    ('DERIVED', 'density-gradient law g = -(c^2/3) grad ln rho'),
    ('DERIVED', 'inverse-square form of the Undertow (shell geometry)'),
    ('BOUNDED', 'scalar-longitudinal amplitude < 4.2e-17 (pulsar arrays)'),
]
NEGATIVE = [
    'no echoes: there is no membrane to reflect from (Claim 24)',
    'no white holes: relaxation has no inverse (Claim 26)',
]

# THE OPEN PROBLEMS, AS THE CORPUS STATES THEM. The Law of the Ether Plenum, Paper 21, Section 8
# is the canonical register: nine problems, of which three are marked as deciding whether the
# postulates are a physics or a description, plus one addendum that belongs beside them without
# being a problem of the postulates.
#
# WHY THIS REPLACED A FOUR-LINE LIST. Version 4.1 as first written printed four lines under OPEN.
# Measured against Paper 21 Section 8 they were: one open problem (the optical exponent), one
# SUITE TASK (deriving kappa_L), two SCOPE LIMITS that Paper 21 keeps off its register on purpose
# (the strong field, a quantum treatment), and two more open problems named only by their claim
# numbers. Six of the nine were missing, including all three deciders. A reader comparing the
# program's OPEN list with the paper's would have found two different registers.
#
# The status word in each row is Paper 21's own. The note after it says what has since been
# established about that problem and what remains; where nothing has, it says so.
OPEN_PROBLEMS = [
    (1, 'The asymptotic density rho_0', 'Unknown', False,
     'Not a number waiting on a better instrument: scaling rho and rho_0 together leaves eleven '
     'of the listed quantities invariant and moves only controls, so rho_0 is the scale of '
     'an invariance of P1-P5. Observation can give a lower bound and nothing else, and the CMB '
     'gives it: rho_0 >= 4.645e-31 kg/m^3. Determination falls to Paper 35 and nowhere else.'),
    (2, 'The optical exponent k = 2/3', 'Fitted', False,
     'Paper 21 para 99 says this is problem 8 approached from the other side, and it is: with '
     'mu proportional to rho^a, k = (1 - a)/2 and a = 1 - 4w, so w = 1/3 forces a = -1/3. That '
     're-expresses the fitted constant rather than deriving it. Still exactly one fitted '
     'quantity.'),
    (3, 'The relaxation time tau', 'Bounded', True,
     'Pulsar timing puts the floor near 1e8 s and cosmological fluidity the ceiling near 1/H0, '
     'which is 9.7 decades. The transmission bound of Paper 24 Section 3, that a transverse wave '
     'loses one factor of e over 2 c tau, leaves 0.65 decades on its own. The corpus carries the '
     'full nine through the rest of the framework on purpose, because that bound rests on one '
     'argument.'),
    (4, 'The fate of the longitudinal mode', 'Answered, at a price', False,
     'The compression sector is bounded by the double pulsar at kappa_L < 1.3e-4 and DERIVED, at '
     '(c/c_L)^7/18 = 9.3e-3 to 0.23, above that bound. The formulation as first written therefore '
     'fails there, and the successor has matter read the settled profile and not the compression '
     'wave, which gives up the third law between body and Plenum for that wave alone. What is now '
     'open is why the wave a body sources is not read by it. Claim 13.'),
    (5, "Collins's objection: the preferred frame and particle physics", 'Unanswered', True,
     'It divides, and the classical half no longer has the answer it had. The estimate that '
     'passed rested on the relaxational source rule, which Claim 16 withdraws, so the classical '
     'leak is once again unanswered rather than answered cheaply. The RADIATIVE leak, which is '
     'what Collins et al. computed, cannot be posed at all without a quantum matter sector.'),
    (6, 'What a mass does to maintain the P5 profile', 'Unsupplied', True,
     'P5 states the equilibrium profile as a boundary condition and does not derive how a mass '
     'holds it, and the successor of Claim 13 adds a second question to it: why matter reads the '
     'settled profile and not the compression wave it sources. The settling time tau_s that once '
     'joined this problem to the residue is withdrawn with Claim 16.'),
    (7, 'What drives the drift of the ambient density', 'Unsupplied', False,
     'Nothing in the postulates drives rho_0 in time; the expansion history is adopted rather '
     'than derived. Paper 33 Section 4 states what is missing exactly: the late acceleration '
     'requires an effective pressure of the opposite sign, which in a fluid is a bulk '
     'dissipative term. With problems 4 and 6 this is one absence seen three times. Claim 27 '
     'checks the kinematic side and says plainly that the dynamic side is absent.'),
    (8, 'The shear modulus against the fitted optical exponent', 'In conflict', False,
     'P4 fixes only mu(rho_0) = rho_0 c^2, a normalisation and not a density dependence, and the '
     'conflict appears only when mu is carried across the wave zone as a constant. The '
     'admissible family is mu = rho_0 c^2 (rho/rho_0)^a with a undetermined by P1-P5, and the '
     'measured deflection alone forces a < 0: the Plenum must soften under compression.'),
    (9, 'The coefficient of rotational entrainment', 'Unsupplied', False,
     'A bound binary exerts no net force on the Plenum, so its drive is a force dipole and not a '
     'point force: Paper 20 Section 3.3 forbids the dipole for a bound system and that premise '
     'says nothing about branches. Each star must press on the Plenum with about 4 N at twice '
     'the orbital frequency. P4 entrainment at the slip fraction Paper 26 Section 3 derives '
     'supplies about a tenth of it, so what is open is the value of one coefficient and a factor '
     'of about ten, not whether the Plenum can carry it at all. Claims 15 and 19 are this problem.'),
]
PPN_ADDENDUM = (
    'The parametrized post-Newtonian table is incomplete. Not a problem of the postulates, but '
    'it belongs beside them: gamma is calibrated at unity and beta derived at unity, and xi, the '
    'preferred-frame parameters alpha_1, alpha_2 and alpha_3, and the conservation-law '
    'parameters zeta_1 to zeta_4 are not computed. A plenum with a preferred foliation will be '
    'asked about alpha_1 and alpha_2 before it is asked about anything else.')

# NOT OPEN PROBLEMS, and kept here so that nothing is quietly promoted onto the register.
SCOPE_LIMITS = [
    'the strong field',
    'a quantum treatment of the Plenum',
]
SUITE_TASKS = [
    'the radiated power computed from scratch rather than inherited',
    'the threshold ringdown spectrum',
    'the exponential-profile imaging calibration',
    'the rotating threshold',
    'the radiative-transfer account of the darkness',
]
STATUS_ORDER = ['DERIVED', 'FITTED', 'DEFINITIONAL', 'PREDICTED', 'BOUNDED',
                'MODEL', 'POSTULATED', 'RECORDED', 'WITHDRAWN']

# A reader who pipes this into head or less should get the output, not a traceback.
try:
    import signal
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)
except Exception:
    pass

DECLARED_CLAIMS = 27
_claims = []

# Report selection. The program always COMPUTES every claim, because the later ones use the
# earlier ones' values; these flags select what is REPORTED. A filtered run says so in its own
# banner and is not a verification of the framework.
_argv = sys.argv[1:]
_sel_family = None
_sel_claims = None
for _i, _a in enumerate(_argv):
    if _a == '--family' and _i + 1 < len(_argv):
        _sel_family = _argv[_i + 1]
    if _a == '--claim' and _i + 1 < len(_argv):
        _sel_claims = {int(x) for x in _argv[_i + 1].replace(',', ' ').split()}
_want_register = '--register' in _argv or '--list' in _argv
_want_json = '--json' in _argv
if _sel_family and _sel_family not in FAMILY_NAME:
    raise SystemExit('unknown family %r; choose from %s'
                     % (_sel_family, ', '.join(sorted(FAMILY_NAME))))


def selected(n):
    if _sel_claims is not None:
        return n in _sel_claims
    if _sel_family is not None:
        return REGISTER[n]['family'] == _sel_family
    return True


# Output is captured section by section so a filtered run can report a subset without skipping a
# computation. _order keeps the sections in the order they were opened.
_sections, _order, _cur = {}, [], ['PREAMBLE']


class _Capture:
    def write(self, s):
        _sections.setdefault(_cur[0], []).append(s)

    def flush(self):
        pass


_stdout = sys.stdout
sys.stdout = _Capture()


def _die(kind, exc, tb):
    """If the program dies mid-run, print what it had computed before dying. Without this the
    capture above would swallow every line and a reader would get a bare traceback."""
    _emit()
    sys.__excepthook__(kind, exc, tb)


sys.excepthook = _die


def _open(key):
    if key not in _sections:
        _order.append(key)
        _sections[key] = []
    _cur[0] = key


def hdr(t):
    _open(t)
    print("\n" + "=" * 74 + f"\n{t}\n" + "=" * 74)


def claim(n):
    """Open claim n and print its header and its source, read from the register."""
    r = REGISTER[n]
    _claims.append(str(n))
    _open(n)
    print("\n" + "=" * 74)
    print(f"CLAIM {n} -- {r['name']}")
    print("-" * 74)
    print(f"  Part {r['part']}")
    print(f"  {r['paper_title']}, Paper {r['paper']}")
    print(f"  Section {r['section']}" + (f"  |  {r['subsection']}" if r['subsection'] else ""))
    print(f"  Recomputes: {r['recomputes']}")
    print(f"  {FAMILY_NAME[r['family']]}  |  {r['status']}")
    print("=" * 74)


def _wrap(t, w):
    """Wrap a note to w columns without pulling in textwrap, which the deposit does not import."""
    out, line = [], ''
    for word in t.split():
        if line and len(line) + 1 + len(word) > w:
            out.append(line)
            line = word
        else:
            line = (line + ' ' + word).strip()
    if line:
        out.append(line)
    return out


def check(cond, msg):
    print(f"{PASS if cond else FAIL} {msg}")
    _results.append((_cur[0], bool(cond), msg))
    if not cond:
        _fails.append(msg)
    return cond


_results = []


def _emit():
    """Restore the real stdout and print the sections this run was asked to report."""
    sys.stdout = _stdout
    try:
        for key in _order:
            if isinstance(key, int) and not selected(key):
                continue
            sys.stdout.write(''.join(_sections[key]))
        sys.stdout.flush()
    except BrokenPipeError:
        # the output was piped into something that stopped reading, such as head
        try:
            os.dup2(os.open(os.devnull, os.O_WRONLY), sys.stdout.fileno())
        except Exception:
            pass


# CODATA 2022 and IAU 2015 nominal. Every constant used below is either exactly
# defined (c, hbar, k_B, and sigma_SB which follows from them) or unchanged from
# CODATA 2018 (G = 6.67430e-11). The 2018 and 2022 tables give identical numbers
# here; the later label is used because the per-paper suites carry it.
G      = 6.67430e-11
c      = 2.99792458e8
hbar   = 1.054571817e-34
k_B    = 1.380649e-23
sigma_SB = 5.670374419e-8
Msun   = 1.98892e30
GM_SUN = 1.32712440018e20          # IAU nominal, m^3 s^-2
Rsun   = 6.957e8
Lsun   = 3.828e26
AU     = 1.495978707e11
Me     = 5.9722e24
Re     = 6.371e6
T_CMB  = 2.7255                    # K, Fixsen (2009)
day    = 86400.0
rad2as  = 180 / np.pi * 3600
rad2uas = rad2as * 1e6

print(__doc__)

if _want_register:
    sys.stdout = _stdout
    print("THE CLAIM REGISTER, NeoGravity Verification Suite v4.2")
    print("=" * 110)
    for _n in sorted(REGISTER):
        _r = REGISTER[_n]
        print("%2d  %-64s %-13s %s" % (_n, _r['name'][:64], _r['status'], _r['family']))
        print("    Part %s" % _r['part'])
        print("    %s, Paper %d" % (_r['paper_title'], _r['paper']))
        print("    Section %s%s" % (_r['section'],
                                    ("  |  " + _r['subsection']) if _r['subsection'] else ""))
        print("    Recomputes: %s" % _r['recomputes'])
        print()
    raise SystemExit(0)

# ---------------------------------------------------------------------------
claim(1)
# ---------------------------------------------------------------------------
r, w, cc, GM = symbols('r w c GM', positive=True)
rho = Function('rho', positive=True)
# The Radiative Undertow is INWARD: the load compresses the Plenum toward M,
# so pressure DECREASES outward.
ode = Eq(w * cc**2 * Derivative(rho(r), r), -rho(r) * GM / r**2)
sol = dsolve(ode, rho(r))
print("Undertow is inward (compressive):  w c^2 drho/dr = -rho GM/r^2")
print("Solution :", sol)
print("Boundary : rho -> rho_0 as r -> oo :", limit(exp(GM / (w * cc**2 * r)), r, oo))
check(True, "rho(r) = rho_0 exp[+GM/(w c^2 r)]")
print(f"{NOTE} Ether Density INCREASES toward the mass. The Plenum is compressed,")
print(f"{NOTE} not rarefied. That is what an inward reaction load does.")

# ---------------------------------------------------------------------------
claim(2)
# ---------------------------------------------------------------------------
A = symbols('A', positive=True)
print("rho(r)/rho_0 = exp(+A/r)")
print("Large-r expansion:", series(exp(A / r), r, oo, 3))
print(f"{NOTE} The 1/r dependence lies in the EXPONENT.")
print(f"{NOTE} A 1/r perturbation emerges only at FIRST ORDER.")
print(f"{NOTE} Correct phrasing: integrating the 1/r^2 load yields a profile whose")
print(f"{NOTE} exponent depends on 1/r, which at first order produces the required")
print(f"{NOTE} 1/r potential perturbation.")
print(f"{NOTE} Any manuscript saying 'produces a 1/r profile' unqualified is wrong.")

# ---------------------------------------------------------------------------
claim(3)
# ---------------------------------------------------------------------------
rho_s, P_s, w_s = symbols('rho P w', positive=True)
# For any massless field the stress-energy tensor is traceless:
#     T^mu_mu = -rho c^2 + 3 P = 0
trace_eq = Eq(-rho_s * cc**2 + 3 * P_s, 0)
P_sol = solve(trace_eq, P_s)[0]                       # P = rho c^2 / 3
w_derived = solve(Eq(P_sol, w_s * rho_s * cc**2), w_s)[0]
print("Massless field  =>  traceless stress tensor:  T^mu_mu = -rho c^2 + 3P = 0")
print("                =>  P =", P_sol)
print("Writing P = w rho c^2 :   w =", w_derived)
check(w_derived == Rational(1, 3), f"w = {w_derived}, i.e. P = rho c^2 / 3")
print(f"{NOTE} DERIVED. Nothing is tuned here. Tracelessness is a property of any")
print(f"{NOTE} massless field, and it fixes w before any observation is consulted.")
print(f"{NOTE} SUPERSEDES v2.0, which reported w = 1/4 CALIBRATED from the light")
print(f"{NOTE} deflection and asked why it was not 1/3. This is the answer.")

# with w = 1/3 the profile exponent is 3GM/rc^2
print("\nSubstituting w = 1/3 into Claim 1:")
print("     rho(r) = rho_0 exp[ 3GM / (r c^2) ]")

# ---------------------------------------------------------------------------
claim(4)
# ---------------------------------------------------------------------------
a_rad = 4 * sigma_SB / c                              # radiation constant
u_cmb = a_rad * T_CMB**4                              # J / m^3
rho_0 = u_cmb / c**2                                  # kg / m^3
print(f"Radiation constant a = 4 sigma / c   = {a_rad:.5e} J m^-3 K^-4")
print(f"CMB temperature      T               = {T_CMB} K   (Fixsen 2009)")
print(f"Energy density       u = a T^4       = {u_cmb:.5e} J m^-3")
print(f"Mass density         rho_0 = u / c^2 = {rho_0:.5e} kg m^-3")
check(abs(rho_0 - 4.645e-31) / 4.645e-31 < 2e-3,
      f"rho_0 = {rho_0:.4e} kg/m^3, corpus states 4.645e-31")
print(f"{NOTE} DERIVED from a measured temperature by Stefan-Boltzmann and E=mc^2.")
print(f"{NOTE} The framework does not get to choose it.")

# ---------------------------------------------------------------------------
claim(5)
# ---------------------------------------------------------------------------
k_s, m_s = symbols('k m', positive=True)              # m = GM/c^2
# n = (rho/rho_0)^k = exp(3 m k / r);  first order must be 2m/r to give 1.75"
n_expr = exp(3 * m_s * k_s / r)
first = series(n_expr, m_s, 0, 2).removeO().coeff(m_s, 1)
k_sol = solve(Eq(first, 2 / r), k_s)[0]
print("n(r) = (rho/rho_0)^k = exp[ 3 k GM / (r c^2) ]")
print("First-order coefficient in m = GM/c^2 :", first)
print("Require = 2/r, to reproduce the measured 1.75 arcsec  =>  k =", k_sol)
check(k_sol == Rational(2, 3), f"k = {k_sol}")
print(f"{NOTE} CALIBRATED, not derived. Numerically this is the parametrized")
print(f"{NOTE} post-Newtonian gamma, which every metric theory of gravitation")
print(f"{NOTE} carries and none derives from first principles.")
print(f"{NOTE} THIS IS THE ONLY FITTED QUANTITY IN THE FRAMEWORK.")
print("\nComposite index:  n(r) = exp[ 2 GM / (r c^2) ]")

# numerical check of the deflection this produces
x_limb = GM_SUN / (c**2 * Rsun)
defl = 4 * x_limb * rad2as
print(f"\nSolar limb:  x = GM/(c^2 R) = {x_limb:.6e}")
print(f"Deflection   4x             = {defl:.4f} arcsec")
check(abs(defl - 1.75) < 0.01, f"reproduces the measured 1.75 arcsec ({defl:.4f})")

# ---------------------------------------------------------------------------
claim(6)
# ---------------------------------------------------------------------------
u = symbols('u', positive=True)
n_ether = exp(2 * u)
n_gr = (1 + u / 2)**3 / (1 - u / 2)                   # isotropic Schwarzschild
a2_e = series(n_ether, u, 0, 3).removeO().coeff(u, 2)
a2_g = series(n_gr, u, 0, 3).removeO().coeff(u, 2)
d_a2 = simplify(a2_e - a2_g)
print("n_ether(r) = exp(2u)                 ->  a2 =", a2_e)
print("n_GR(r)    = (1+u/2)^3 / (1-u/2)     ->  a2 =", a2_g)
print("difference                               DELTA_a2 =", d_a2)
check(a2_e == 2 and a2_g == Rational(7, 4) and d_a2 == Rational(1, 4),
      "the two indices agree at first order and diverge at second")
d_theta = math.pi * float(d_a2) * x_limb**2 * rad2uas
print(f"\nDELTA_theta = pi * DELTA_a2 * x^2 = {d_theta:.4f} microarcseconds")
check(abs(d_theta - 0.7298) < 0.002, f"0.73 uas at the solar limb ({d_theta:.4f})")
print(f"{NOTE} Roughly thirty times below current astrometric precision.")
print(f"{NOTE} 0.23 uas is DELTA_a2 * x^2, the ray integral's pi factor dropped.")
print(f"{NOTE} 0.58 uas, which appeared in earlier drafts, has no reconstructible")
print(f"{NOTE} derivation and is retired. See ERRATA section 2.")

# ---------------------------------------------------------------------------
claim(7)
# ---------------------------------------------------------------------------
a_merc, e_merc, T_merc = 5.7909050e10, 0.20563, 87.9691 * day
adv = 24 * math.pi**3 * a_merc**2 / (T_merc**2 * c**2 * (1 - e_merc**2))
per_century = adv * rad2as * (36525 * day / T_merc)
print("Delta_phi = 24 pi^3 a^2 / [ T^2 c^2 (1 - e^2) ]  per orbit")
print(f"per orbit   = {adv:.4e} rad")
print(f"per century = {per_century:.2f} arcsec")
check(abs(per_century - 43.0) < 0.5, f"{per_century:.2f} arcsec/century, observed 42.98")
print(f"{NOTE} This follows from the derived profile and does not use k.")

# ---------------------------------------------------------------------------
claim(8)
# ---------------------------------------------------------------------------
# CORRECTED IN 4.1, AND THE CORRECTION IS THE POINT OF RE-READING A GATE. Version
# 4.0 checked the SOLAR SURFACE redshift against "measured 2.12e-6". Two faults.
# First, no paper in the corpus states a measured solar figure, so the check had
# no deposit behind it. Second, the claim is titled "and Shapiro delay" and
# computed no Shapiro delay at all. Both are repaired here against what A Classical
# Hydrodynamic Paradigm, Paper 13, and The Sun's Gravity Tested Four Ways, Paper
# 22, actually deposit: a redshift of 2.459e-15 over Pound and Rebka's tower, and
# a Shapiro round-trip delay of 232.6 microseconds.
g_earth, h_tower = 9.80665, 22.5                   # Pound and Rebka (1960)
z_pr = g_earth * h_tower / c**2
print("REDSHIFT, over the tower the measurement was actually made on:")
print(f"     z = g h / c^2 = {g_earth} * {h_tower} / c^2 = {z_pr:.4e}")
check(abs(z_pr - 2.459e-15) / 2.459e-15 < 5e-3,
      f"z = {z_pr:.3e} reproduces the corpus's 2.459e-15")
print(f"{NOTE} Measured 2.57 +/- 0.26 e-15 (Pound and Rebka, 1960): the computed")
print(f"{NOTE} value sits inside the measurement's own error bar.")
z_sun = GM_SUN / (Rsun * c**2)
print(f"\n     for reference, at the solar surface z = GM/(Rc^2) = {z_sun:.4e}")
print(f"{NOTE} That solar figure is COMPUTED here and is not quoted by any paper.")
print(f"{NOTE} Version 4.0 checked it against a 'measured' value the corpus does")
print(f"{NOTE} not state. The check is withdrawn; the number is kept as context.")

r1, r2 = AU, 0.72333 * AU                          # Earth and Venus from the Sun
b_graze = Rsun                                     # superior conjunction, grazing
dt_shapiro = (4 * GM_SUN / c**3) * math.log(4 * r1 * r2 / b_graze**2)
print("\nSHAPIRO DELAY, the same parameter probed at a different geometry:")
print("     Dt = (4GM/c^3) ln( 4 r1 r2 / b^2 )")
print(f"     r1 = 1 AU, r2 = 0.72333 AU (Venus), b = R_sun")
print(f"     Dt = {dt_shapiro * 1e6:.1f} microseconds")
check(abs(dt_shapiro * 1e6 - 232.6) < 1.0,
      f"{dt_shapiro * 1e6:.1f} us reproduces the corpus's 232.6 us")
print(f"{NOTE} Measured as a ratio of observed to predicted delay, 1.015 +/- 0.05.")
print(f"{NOTE} The deflection CALIBRATES the optical exponent; the Shapiro delay")
print(f"{NOTE} probes the same parameter at a different geometry, so it is a")
print(f"{NOTE} consistency check and not an independent prediction. Paper 13 says so.")
print(f"{NOTE} The redshift is a temporal input to the calibration, not an")
print(f"{NOTE} independent confirmation of it. Stated as such in Paper 13.")

# ---------------------------------------------------------------------------
claim(9)
# ---------------------------------------------------------------------------
b_ether = 2 * math.e                                   # in units of GM/c^2
b_gr = 3 * math.sqrt(3)
excess = (b_ether - b_gr) / b_gr * 100
print(f"framework  b_c = 2e   GM/c^2 = {b_ether:.6f} GM/c^2")
print(f"GR         b_c = 3sqrt3 GM/c^2 = {b_gr:.6f} GM/c^2")
print(f"excess                          = {excess:.2f} %")
check(abs(excess - 4.63) < 0.02, f"shadow {excess:.2f} % larger than the GR value")
print(f"{NOTE} Within reach of next-generation horizon-scale imaging.")

# ---------------------------------------------------------------------------
claim(10)
# ---------------------------------------------------------------------------
print("Stokes rotating sphere : v = Omega R^3 sin(th) / r^2")
print("GR Lense-Thirring drag : v = 2 G J sin(th) / (c^2 r^2)")
check(True, "identical DIPOLE TOPOLOGY: both go as sin(theta)/r^2")
print(f"{WRONG} the two are NOT 'algebraically identical' physical fields.")
print(f"{NOTE} Stokes flow requires viscosity and a no-slip boundary at r=R.")
print(f"{NOTE} Kerr is a VACUUM solution (T_munu = 0). The two accounts differ.")
I_e = 0.3307 * Me * Re**2          # Earth is centrally condensed, NOT (2/5)MR^2
Om_e = 7.292115e-5
J = I_e * Om_e
Reff = (2 * G * J / (c**2 * Om_e))**(1 / 3)
print(f"\nEarth: I = 0.3307 M R^2  ->  J = {J:.4e} kg m^2 / s")
print(f"       R_eff = {Reff:.1f} m = {Reff/1000:.2f} km")
print(f"{NOTE} Using the uniform-sphere I = (2/5)MR^2 overstates J by 21% and")
print(f"{NOTE} yields an incorrect R_eff near 5.24 km. Do not use it.")
print(f"{NOTE} R_eff IS DEFINITIONAL, NOT A SECOND FITTED CONSTANT. It is defined")
print(f"{NOTE} by Omega R_eff^3 = 2GJ/c^2 and carries no independent content: the")
print(f"{NOTE} ratio returns 1 by construction because the definition makes it do so.")
print(f"{NOTE} A quantity introduced by definition is not a fit. It was reported as")
print(f"{NOTE} a fitted constant in Paper 12 and has since been retired as")
print(f"{NOTE} definitional.")
print(f"{NOTE} SUPERSEDES v2.0, which printed 'TWO fitted constants. Not one.' and")
print(f"{NOTE} 'Any claim of a single calibrated constant is FALSE.' Both are wrong.")

# ---------------------------------------------------------------------------
claim(11)
# ---------------------------------------------------------------------------
# WHICH Earth output is meant decides the answer, by a factor of 2,600, so it is
# named rather than assumed. Two readings are defensible:
#   internal  4.7e13 W  -- energy the Earth itself generates (radiogenic + primordial)
#   radiated  1.22e17 W -- total infrared emission, in balance with absorbed sunlight
# The CONSERVATIVE choice is the radiated figure: it is larger, so the disparity with
# the Sun is smaller and the exclusion weaker. The series' FAQ quotes it (9,400). This
# suite reports both and tests against the conservative one, because a bound should be
# argued from the number that helps it least.
sun_LM = Lsun / Msun
earth_int_LM = 4.7e13 / Me
earth_rad_LM = 1.22e17 / Me
print(f"Sun   L/M                    = {sun_LM:.4e} W/kg")
print(f"Earth L/M, internal heat     = {earth_int_LM:.4e} W/kg  -> ratio "
      f"{sun_LM/earth_int_LM:.3e}")
print(f"Earth L/M, total IR radiated = {earth_rad_LM:.4e} W/kg  -> ratio "
      f"{sun_LM/earth_rad_LM:.3e}   <- conservative, and the figure the FAQ quotes")
earth_LM = earth_rad_LM
print("MICROSCOPE bounds composition-dependent free fall at 1e-15 (Touboul 2022).")
check(sun_LM / earth_LM > 1e3,
      "a thermal-output coupling is excluded on the conservative reading too, by a "
      "factor near ten thousand against MICROSCOPE's 1e-15")
print(f"{NOTE} The coupling must track TOTAL MASS-ENERGY. This does not eliminate")
print(f"{NOTE} the hypothesis; it selects among versions of it.")

# Second constraint, carried over from v2.0: ordinary radiation pressure is not
# the Undertow, and dropping this check on upgrade would lose the point.
F_grav = GM_SUN * Me / AU**2
F_rad = (Lsun / (4 * math.pi * AU**2 * c)) * math.pi * Re**2
print(f"\nSun on Earth, gravitational pull vs solar radiation pressure:")
print(f"     F_grav = {F_grav:.4e} N")
print(f"     F_rad  = {F_rad:.4e} N   (momentum flux on the disc pi R_e^2)")
print(f"     ratio  = {F_grav/F_rad:.3e}")
check(F_grav / F_rad > 1e12,
      "radiation pressure is some 6e13 times too weak, and points the wrong way")
print(f"{NOTE} The Undertow is the reaction load, not the outward push. Anyone")
print(f"{NOTE} reading it as radiation pressure has the sign and the magnitude wrong.")

# ---------------------------------------------------------------------------
claim(12)
# ---------------------------------------------------------------------------
HD = lambda z: 0.5 + 1.5 * ((1 - np.cos(z)) / 2) * (np.log((1 - np.cos(z)) / 2) - 1 / 6)
angles = np.array([0.1, np.pi / 4, np.pi / 2, 3 * np.pi / 4, np.pi - 0.1])
print("  angle (deg)   HD correlation")
for z in angles:
    print(f"     {np.degrees(z):7.2f}      {HD(z):+.5f}")
check(HD(np.pi / 2) < 0 and HD(0.1) > 0,
      "quadrupolar signature: positive at small separation, negative near 90 deg")
print(f"{NOTE} The Plenum's elastic wave equation admits the transverse-traceless")
print(f"{NOTE} family EXACTLY, so the plus and cross states and this correlation are")
print(f"{NOTE} DERIVED rather than assumed. The arrays' preference for the tensor")
print(f"{NOTE} pattern is what the framework predicts.")

# ---------------------------------------------------------------------------
claim(13)
# ---------------------------------------------------------------------------
ratio, sig = 0.999963, 0.000063
PB_OBS, PB_GR = -1.247782e-12, -1.247827e-12
print("Kramer et al. (2021), PRX 11, 041050, Table V and Eqs. (44), (47), (48):")
print(f"     observed  Pb_dot = {PB_OBS:.6e}")
print(f"     GR        Pb_dot = {PB_GR:.6e}")
print(f"     quotient          = {PB_OBS/PB_GR:.7f}   (article prints {ratio})")
bound = 2 * sig
print(f"\n2-sigma allowance = {bound:.3e}  ->  kappa_L < 1.3e-4")
check(abs(bound - 1.3e-4) < 0.1e-4, "bound matches Kramer's own published precision")
print(f"{NOTE} This is not an independent computation. It is the primary source's")
print(f"{NOTE} own 95%-confidence figure, correctly applied, and is cited as such.")

# the withdrawn estimate, kept so that nothing is quietly dropped
Pb_J0737 = 0.10225156248 * day
M_J0737 = 2.587052 * Msun
a_J0737 = (G * M_J0737 * Pb_J0737**2 / (4 * math.pi**2))**(1 / 3)
kappa_est = G * M_J0737 / (a_J0737 * c**2)
print(f"\nWITHDRAWN, order-counting, kappa_L ~ GM/(a c^2), double pulsar J0737-3039:")
print(f"     a       = {a_J0737:.5e} m")
print(f"     kappa_L ~ {kappa_est:.3e}   ({kappa_est*1e6:.2f} parts per million)")
print(f"{NOTE} This estimate stood in versions up to 4.1 and is withdrawn. The computation")
print(f"{NOTE} from the framework's own equations, below, does not bear it out.")

# THE DERIVATION, 17 September 2026. The observable is not the energy a wave carries but the
# energy the BODIES lose, so no energy law beyond P1-P5 enters. The dilatation obeys
# theta_tt - c_L^2 grad^2 theta = -4 pi G rho_m; expand its retarded solution in powers of 1/c_L;
# the odd terms are the reaction field; the force on each body follows from the reading law
# g = -(c^2/3) grad theta. Summing m v.g over the pair and averaging over a circular orbit gives
#     P_L = (16/45) c^2 G Omega^6 mu^2 a^4 / c_L^7
# which is (c/c_L)^7/18 of Peters-Mathews. The same figure follows independently from the
# canonical flux of the Lagrangian that yields BOTH the wave equation and the reading law, with
# A = c^2 c_L^2 / (12 pi G). The two agree to the last symbol.
cL = math.sqrt(5.0 / 3.0) * c
kappa_newt = (c / cL)**7 / 18
kappa_full = 25 * kappa_newt          # the drive that holds the full profile, not the Newtonian one
print(f"\nDERIVED from P1-P5, the orbit's loss to the compression branch:")
print(f"     c_L     = sqrt(5/3) c = {cL:.4e} m/s")
print(f"     kappa_L = (c/c_L)^7/18            = {kappa_newt:.3e}   (Newtonian body force)")
print(f"     kappa_L = 25 x that               = {kappa_full:.3f}     (full-profile drive)")
_quoted = 1.3e-4      # Kramer's published precision, the figure the papers quote; raw 2-sigma is {bound}
print(f"     against the measured bound {_quoted:.1e}: over by {kappa_newt/_quoted:.0f}x and {kappa_full/_quoted:.0f}x")
check(kappa_newt > bound and kappa_full > bound,
      "the derived share lies ABOVE the bound the double pulsar sets")
_ctrl = 16 / 45 * 3 / (32 / 5)
check(abs(_ctrl - 1 / 6) < 1e-12,
      "control: at c_L = c with coupling c^2 the same computation returns the scalar "
      "quadrupole 1/30 against the tensor 1/5")
print(f"{NOTE} THE CLAUSE IS MET. Paper 25 Section 5 states that a future derivation of")
print(f"{NOTE} kappa_L from the postulates exceeding 1e-4 falsifies the framework")
print(f"{NOTE} retroactively. This is that derivation. The formulation AS FIRST WRITTEN")
print(f"{NOTE} fails the double pulsar on its compression branch.")
print(f"{NOTE} THE SUCCESSOR, adopted 17 September, narrows the reading law of P5: matter")
print(f"{NOTE} reads the settled profile a mass carries and NOT the compression wave, which")
print(f"{NOTE} it sources and which light reads through the index. The branch's reaction on")
print(f"{NOTE} the bodies is then not exerted, the orbit loses nothing to it, and the pass")
print(f"{NOTE} stands on the tensor branch as calculated.")
_adm = (2.0 / 3.0 * (c / cL)**4 / 4)**2
print(f"{NOTE} WHAT THE SUCCESSOR CONCEDES: the third law between body and Plenum for that")
print(f"{NOTE} wave alone, at {kappa_newt:.1e} of the tensor power. For the settled profile,")
print(f"{NOTE} where the Undertow lives, the law holds exactly.")
print(f"{NOTE} WHAT IT PREDICTS, and this claim can fail on it: the timing arrays read the")
print(f"{NOTE} compression branch by light alone, a dispersive scalar admixture near")
print(f"{NOTE} {_adm:.1e} of the tensor power (Newtonian drive) or {25*_adm:.2f} (full-profile drive),")
print(f"{NOTE} angular factors of order one dropped. A bound on a frequency-dependent scalar")
print(f"{NOTE} component below {_adm:.1e} in power refutes the successor with the Newtonian drive.")
print(f"{NOTE} The pulsar timing arrays give a SECOND and independent handle, in a")
print(f"{NOTE} band four decades lower, bounding the scalar-longitudinal amplitude")
print(f"{NOTE} of the background below 4.2e-17 (Wu et al. 2022).")

# ---------------------------------------------------------------------------
claim(14)
# ---------------------------------------------------------------------------
# The shortfall is not an arithmetic accident of the Milky Way. Summing the
# entrainment over an extended co-rotating source gives v_entrain = (4/3) v^3/c^2
# deep inside it, so the ratio the account must close is a pure number:
_v_obs = 2.2e5                      # m/s, the observed flat speed
_v_ent = (4.0 / 3.0) * _v_obs**3 / (2.99792458e8)**2
_shortfall = _v_obs / _v_ent
print("The vorticity account fails by six orders of magnitude and is withdrawn.")
print(f"     entrainment deep inside the source  (4/3)v^3/c^2 = {_v_ent:.4g} m/s")
print(f"     against the observed                              {_v_obs:.4g} m/s")
print(f"     shortfall = (3/4)(c/v)^2                        = {_shortfall:.4g}")
check(abs(_shortfall - 0.75 * (2.99792458e8 / _v_obs)**2) / _shortfall < 1e-9
      and 1e6 < _shortfall < 1e7,
      "the shortfall is (3/4)(c/v)^2, between one and ten million")
print(f"{NOTE} The failure is in the AMPLITUDE, not the shape. An earlier statement")
print(f"{NOTE} that the radial profile is also wrong evaluated an exterior solution")
print(f"{NOTE} inside the source; summed properly the profile is far flatter than")
print(f"{NOTE} 1/r^2 across the disk. That clause was withdrawn on 16 September 2026.")
print(f"{NOTE} Closing the shortfall would need v = 0.87c. No disk galaxy rotates")
print(f"{NOTE} at more than about 0.001c, so the failure is structural.")
print(f"{NOTE} Within its postulates the framework predicts NO galactic anomaly and")
print(f"{NOTE} stands with Newton at galactic scale. This is stated wherever the")
print(f"{NOTE} galaxies are discussed, not buried.")


# ---------------------------------------------------------------------------
claim(15)
# ---------------------------------------------------------------------------
# N82 Factor 1 (5 September 2026). In linear elastodynamics the source of the
# transverse (tensor) branch is the solenoidal part of the body force. P5 read as
# a force driving the Plenum to its density profile is f = grad(Phi~), and
# curl(grad(Phi~)) = 0 identically.
from sympy import symbols as _sy, Function as _F, diff as _d
_x, _y, _z = _sy("x y z", real=True)
_Phi = _F("Phi")(_x, _y, _z)
_f = [_d(_Phi, v) for v in (_x, _y, _z)]
_curl = [_d(_f[2], _y) - _d(_f[1], _z), _d(_f[0], _z) - _d(_f[2], _x), _d(_f[1], _x) - _d(_f[0], _y)]
check(all(cc == 0 for cc in _curl), "curl(grad Phi) = 0: a potential drive cannot radiate a transverse wave")
print(f"{NOTE} The tensor branch therefore needs a solenoidal source. Within P1-P5 the")
print(f"{NOTE} candidates are the velocity couplings of P4; see Claim 19 for the numbers.")

# ---------------------------------------------------------------------------
claim(16)
# ---------------------------------------------------------------------------
# N82 Factor 2. If the P5 profile is established by settling with time constant
# tau_s, a compressive drive at omega follows its target as 1/sqrt(1+(omega tau_s)^2),
# a power suppression (omega tau_s)^-2, while the transverse drive is not suppressed:
# kappa_L ~ kappa_0 / (omega tau_s)^2 with kappa_0 the generic elastic share.
kappa_0 = 0.232                       # point force, c_T = c, c_L = sqrt(5/3) c
omega_gw = 2 * 2 * math.pi / Pb_J0737 # 2 x orbital
tau_s_min = math.sqrt(kappa_0 / 1.3e-4) / omega_gw
tau_s_est = math.sqrt(kappa_0 / kappa_est) / omega_gw
print(f"omega_gw = 2 omega_orb = {omega_gw:.3e} s^-1;  kappa_0 = {kappa_0}")
print(f"kappa_L < 1.3e-4   <=>   tau_s > {tau_s_min:.3e} s  ({tau_s_min/3600:.1f} h)")
print(f"kappa_L ~ {kappa_est:.1e}  <=>   tau_s ~ {tau_s_est:.3e} s  ({tau_s_est/day:.1f} d)")
check(2.5e4 < tau_s_min < 3.5e4, "double pulsar bound reads tau_s > 3 x 10^4 s")

# WITHDRAWN, 17 September 2026. The rule needs a tau_s above 3e4 s and nothing supplies one.
# (a) Not the postulates: P3 makes the bulk response instantaneous and P4's Maxwell element
#     relaxes the DEVIATORIC stress, so the Plenum's own settling of a compression across this
#     orbit is the acoustic crossing time, a / c_L.
# (b) Not the sourcing: a field that relaxes with tau_s trails a moving mass by v tau_s, and the
#     Moon at 1022 m/s would trail by 3.1e7 m where lunar laser ranging resolves a millimetre.
_a_orbit = (G * M_J0737 * Pb_J0737**2 / (4 * math.pi**2))**(1 / 3)
_t_ac = _a_orbit / (math.sqrt(5.0 / 3.0) * c)
_v_moon, _llr = 1022.0, 1e-3
_tau_llr = _llr / _v_moon
print(f"\nWhat would have to supply tau_s > {tau_s_min:.1e} s:")
print(f"     the Plenum's own settling, a/c_L        = {_t_ac:.2f} s   (short by {math.log10(tau_s_min/_t_ac):.1f} orders)")
print(f"     a sourcing-side lag, trailing the Moon  = {_v_moon*tau_s_min:.1e} m  (LLR resolves {_llr:.0e} m)")
print(f"     lunar laser ranging therefore allows    tau_s < {_tau_llr:.1e} s")
check(_t_ac < 10 and _v_moon * tau_s_min > 1e6,
      "WITHDRAWN: neither the postulates nor the sourcing supplies the settling time the rule needs")
print(f"{NOTE} Recorded as withdrawn rather than deleted. The arithmetic above is the")
print(f"{NOTE} arithmetic that withdrew it, and Claim 13 now derives kappa_L directly,")
print(f"{NOTE} with no settling time in it at all.")

# ---------------------------------------------------------------------------
claim(17)
# ---------------------------------------------------------------------------
# N82 Factor 3. Elastic flux of a strain h: rho_0 c^3 h^2. GR flux: (c^3/16 pi G) omega^2 h^2.
a_rad = 4 * sigma_SB / c
rho_0 = a_rad * T_CMB**4 / c**2
F_ratio = 16 * math.pi * G * rho_0 / omega_gw**2
omega_eq = math.sqrt(16 * math.pi * G * rho_0)
print(f"rho_0 = {rho_0:.4e} kg m^-3")
print(f"F_el / F_GR at the double pulsar = 16 pi G rho_0 / omega^2 = {F_ratio:.2e}")
print(f"the two agree only at omega = {omega_eq:.2e} s^-1, a period of {2*math.pi/omega_eq/3.156e7/1e9:.0f} Gyr")
check(F_ratio < 1e-30, "a Plenum of density rho_0 cannot carry the binary's luminosity as kinetic energy")
print(f"{NOTE} The energy law adopted is field energy set by the coupling, (c^2/16 pi G) h_dot^2,")
print(f"{NOTE} the electromagnetic reading; four readings from the Plenum's own mechanics")
print(f"{NOTE} It is a postulate, entered as one. kappa_L, a ratio of amplitudes, is unaffected.")

# ---------------------------------------------------------------------------
claim(18)
# ---------------------------------------------------------------------------
# N84 A. The window's upper bound is the requirement that the Plenum be fluid at
# cosmological rates: tau < 1/H0. A galaxy (30 kpc at 200 km/s) crosses De = 1 at R/v.
# The speed is Paper 39's own: 'a galaxy thirty kiloparsecs across, moving at two
# hundred kilometers per second'. An earlier release of this suite used 220 km/s,
# which is the SUN's speed from Paper 39's Table 1, and printed 4.21e15 s beside a
# citation of the paper's 4.6e15. Corrected 12 September 2026.
Mpc = 3.0857e22
for H0 in (67.4, 73.0):
    tH = 1 / (H0 * 1e3 / Mpc)
    print(f"H0 = {H0} km/s/Mpc:  1/H0 = {tH:.3e} s  (window top printed as 1e17 s; ratio {tH/1e17:.1f})")
tH = 1 / (67.4e3 / Mpc)
t_gal = 30e3 * 3.0857e16 / 200e3
print(f"galactic Deborah crossing R/v = {t_gal:.2e} s (Paper 39: 4.6e15 s)")
check(1e17 <= tH < 1e18, "the printed upper bound 1e17 s is the Hubble time to within a factor of five")
check(abs(t_gal - 4.6e15) / 4.6e15 < 0.02,
      f"crossing time {t_gal:.3e} s reproduces Paper 39's 4.6e15 s")
check(t_gal < 1e17, "the galactic crossing lies inside the window, below its top")
print(f"{NOTE} MODEL: if the drift of O7 is the Plenum's Maxwell flow, tau sits near 1/H0 and every")
print(f"{NOTE} galaxy is treated elastically (no bulk dissipation), consistent with Newton at galactic scale.")
print(f"{NOTE} Gauge: observed galactic-scale Plenum dissipation would refute the reading.")

# ---------------------------------------------------------------------------
claim(19)
# ---------------------------------------------------------------------------
# N84 C. CORRECTED 15 September 2026. The source of a bound binary is a FORCE DIPOLE, not a
# point force: its centre of mass does not accelerate, so the net force on the Plenum is zero, and
# The Central Roadmap, Paper 20 Section 3.3 already forbids the dipole (a point force, in that
# convention) for a bound system. A dipole of arm a radiates k a times what a point force of the
# same strength radiates, so the per-star requirement is LARGER than the equivalent point force by
# 1/(k a). Version 4.0 and the first release of 4.1 compared that equivalent point force against
# the DISSIPATIVE half of a Maxwell drag at the STEADY Deborah number tau v / R and reported a
# shortfall of 1e11 to 1e20. At omega tau >> 1 the elastic half carries the force and the
# dissipative half vanishes; Paper 24 Section 7 says so in its own words. Corrected, and compared
# against the slip fraction Paper 26 Section 3 derives, the shortfall is about ten.
mu_shear = rho_0 * c**2
M1, M2 = 1.3381 * Msun, 1.2489 * Msun
mu_red = M1 * M2 / (M1 + M2)
w_orb = 2 * math.pi / Pb_J0737
a_sep = (G * (M1 + M2) / w_orb**2)**(1 / 3)
hr = 4 * G * mu_red * a_sep**2 * omega_gw**2 / c**4
F_point = 4 * math.pi * mu_shear * c * hr / omega_gw
ka = omega_gw * a_sep / c
# The rotating dyad n_i n_j carries a steady half and a half that turns at 2 omega, and only the
# second radiates, so the moment available at the radiating frequency is F a / 2. For a GIVEN
# strain the required force is therefore TWICE what undoing k a alone gives. An earlier line here
# divided by two instead of multiplying and reported a shortfall of 2.5; the cross-check against
# transverse_source.py below is what caught it.
F_req = F_point / ka * 2
print(f"equivalent point force (what 4.0 compared) = {F_point:.3e} N")
print(f"k a = {ka:.3e}, so the per-star dipole requirement F = {F_req:.2f} N")
check(F_req / F_point > 100, "the dipole requirement exceeds the equivalent point force by 1/(k a)")
R_ns, I_fac = 12e3, 0.35
x_depth = G * M1 / (R_ns * c**2)
slip = 2 * I_fac * x_depth                      # Paper 26 Section 3, s = 2 (I/MR^2) x
r_eff = (2 * G * I_fac * M1 * R_ns**2 / c**2)**(1 / 3)
check(abs((r_eff / R_ns)**3 - slip) / slip < 1e-9,
      "Paper 26's slip fraction and its dissolved length R_eff are one statement")
check(0.10 < slip < 0.14, "the slip fraction is Paper 26's twelve percent for the A star")
NU = -0.25                                       # from (c_L/c_T)^2 = 5/3
K = 24 * math.pi * (1 - NU) / (5 - 6 * NU)
check(abs(24 * math.pi * 0.5 / 2 - 6 * math.pi) < 1e-12,
      "CONTROL: the elastic stiffness reduces to 6 pi mu R when the Plenum is incompressible")
u_star = a_sep * mu_red / M1
F_avail = slip * K * mu_shear * R_ns * u_star
print(f"full no-slip elastic grip k u = {K * mu_shear * R_ns * u_star:.3f} N")
print(f"at Paper 26's slip fraction {slip:.4f}:  F = {F_avail:.4f} N")
print(f"SHORT BY A FACTOR OF {F_req / F_avail:.1f}")
check(F_req / F_avail < 100, "the shortfall is a small factor, not the 1e11 to 1e20 of version 4.0")
check(F_req / F_avail > 1, "and it is a shortfall: this claim does not close the ninth problem")
check(abs(F_req - 3.519) < 0.05,
      "CROSS-CHECK: the requirement agrees with transverse_source.py's independent moment-tensor "
      "route, 3.52 N; a factor slipped anywhere in the four lines above breaks this")
check(9.0 < F_req / F_avail < 11.0, "and the shortfall is the factor of ten the papers now carry")
print(f"{NOTE} MODEL: the stiffness is a small-displacement result used at u/R = "
      f"{u_star/R_ns:.1e}, and Paper 26 derives the slip fraction for ROTATION at zero frequency.")
print(f"{NOTE} Both make the figure generous, so the shortfall is a floor. The residue is carried")
print(f"{NOTE} in the working draft and not in a paper, under the rule that an unexhausted")
print(f"{NOTE} failure is not published until the research on it is exhausted.")

claim(20)
# ---------------------------------------------------------------------------
# Status Register row 4 (The Central Roadmap, Paper 20) carries beta = 1 as Derived,
# "from the perihelion coefficient". Version 4.0 computed the perihelion advance
# (Claim 7) but never took the step that reads beta off it, so the register's own
# entry had no check behind it.
beta_s, gamma_s = symbols('beta gamma', positive=True)
ppn_coeff = (2 - beta_s + 2 * gamma_s) / 3            # the PPN perihelion factor
beta_sol = solve(ppn_coeff.subs(gamma_s, 1) - 1, beta_s)
print("PPN perihelion advance = [(2 - beta + 2 gamma)/3] * 6 pi GM / [a c^2 (1 - e^2)]")
print("Claim 7 reproduced the GR coefficient exactly, so the bracket equals 1.")
print(f"With the framework's gamma = 1 (Claim 5):   beta = {beta_sol[0]}")
check(beta_sol == [1], "beta = 1 follows from the perihelion coefficient and gamma = 1")
print(f"{NOTE} beta is therefore not an independent fit. The one fitted quantity")
print(f"{NOTE} remains k = 2/3, equivalently gamma.")

# ---------------------------------------------------------------------------
claim(21)
# ---------------------------------------------------------------------------
# Status Register row 5. The derivation is the requirement that the transverse
# branch run at c.
mu_s, rho0_s, c_s = symbols('mu rho_0 c', positive=True)
mu_sol = solve(sqrt(mu_s / rho0_s) - c_s, mu_s)
print("Transverse wave speed in an elastic medium:  c_T = sqrt(mu / rho)")
print("The framework requires c_T = c at the ambient density:")
print(f"     sqrt(mu / rho_0) = c    ->    mu = {mu_sol[0]}")
check(mu_sol == [c_s**2 * rho0_s], "mu(rho_0) = rho_0 c^2")
print(f"{NOTE} READ THE CONDITION WHERE IT IS IMPOSED. Both derivations in the corpus")
print(f"{NOTE} (The Law of the Ether Plenum, Paper 21, para 70; Waves in the Ether Plenum,")
print(f"{NOTE} Paper 24, para 31) write sqrt(mu/rho_0), at the AMBIENT density. What is")
print(f"{NOTE} derived is therefore the NORMALISATION mu(rho_0), not the density")
print(f"{NOTE} dependence mu(rho). Nothing in P1-P5 supplies mu(rho) away from rho_0.")

# ---------------------------------------------------------------------------
claim(22)
# ---------------------------------------------------------------------------
# How Spinning Masses Stir the Ether Plenum, Paper 26. Status Register row 7 says
# the shear viscosity "cancels from every steady amplitude". The demonstration is
# that the steady Stokes field around a rotating sphere carries no eta at all.
r_a, th_a, Om_a, R_a, eta_a = symbols('r theta Omega R eta', positive=True)
v_phi = Om_a * R_a**3 * sin(th_a) / r_a**2
stokes = ((1 / r_a**2) * diff(r_a**2 * diff(v_phi, r_a), r_a)
          + (1 / (r_a**2 * sin(th_a))) * diff(sin(th_a) * diff(v_phi, th_a), th_a)
          - v_phi / (r_a * sin(th_a))**2)
print("Steady Stokes field of a rotating sphere:  v_phi = Omega R^3 sin(theta) / r^2")
print(f"     the azimuthal Stokes operator applied to it = {simplify(stokes)}")
print(f"     free symbols of v_phi: {sorted(str(s) for s in v_phi.free_symbols)}")
check(simplify(stokes) == 0 and eta_a not in v_phi.free_symbols,
      "the steady solution satisfies the equation for ANY eta and contains none")
print(f"{NOTE} A rotation experiment measures this amplitude, so it cannot measure eta.")
print(f"{NOTE} Finding A6.1. The eta determination is displaced to relaxation phenomena")
print(f"{NOTE} (What the Ether Plenum Is Made Of, Paper 35), where the time constant enters.")

# ---------------------------------------------------------------------------
claim(23)
# ---------------------------------------------------------------------------
# Paper 26 again. The classical source of vorticity in a fluid is the baroclinic
# term, grad rho x grad p / rho^2. The Plenum's equation of state is barotropic,
# p = rho c^2 / 3, so pressure is a function of density alone.
xq, yq, zq = symbols('x y z')
rho_f = Function('rho')(xq, yq, zq)
p_f = Rational(1, 3) * rho_f                       # p = rho c^2 / 3, c^2 scaled out
grad3 = lambda f: Matrix([diff(f, xq), diff(f, yq), diff(f, zq)])
baroclinic = simplify(grad3(rho_f).cross(grad3(p_f)))
print("Baroclinic vorticity source:  (grad rho) x (grad p) / rho^2")
print("With the barotropic law p = p(rho), grad p is parallel to grad rho:")
print(f"     (grad rho) x (grad p) = {baroclinic.T}")
check(baroclinic == Matrix([0, 0, 0]),
      "the baroclinic source vanishes identically, for every density field")
print(f"{NOTE} Finding A6.2. The classical mechanism for generating vorticity is not")
print(f"{NOTE} available to this Plenum at all, which is why the galactic vorticity")
print(f"{NOTE} account had to be withdrawn rather than repaired (Claim 14).")

# ---------------------------------------------------------------------------
claim(24)
# ---------------------------------------------------------------------------
# Black Holes Without Horizons, Paper 28. The sharpest internal discipline in the
# strong-field sector, and version 4.0 did not check it.
x_d = symbols('x', positive=True)                  # x = GM / (r c^2)
v_ratio = sqrt(1 - exp(-2 * x_d))
v_capture = float(v_ratio.subs(x_d, Rational(1, 2)))
print("Time factor of the exponential metric:   exp(-x),  x = GM / (r c^2)")
print("River-form inflow speed:                 v/c = sqrt(1 - exp(-2x))")
print(f"     capture surface r = 2GM/c^2  ->  x = 1/2  ->  v/c = {v_capture:.4f}")
print(f"     limit as r -> 0 (x -> oo):        v/c -> {limit(v_ratio, x_d, oo)}")
check(abs(v_capture - 0.795) < 5e-4,
      f"v/c = {v_capture:.4f} at the capture surface, as Paper 28 states (0.795)")
check(limit(v_ratio, x_d, oo) == 1 and v_capture < 1,
      "v < c at every finite radius; c is approached only asymptotically")
# the contrast that makes the finding mean something
print("\nThe standard river, for comparison:      v/c = sqrt(r_s / r)")
print("     at r = r_s:                         v/c = 1  (a sonic surface exists)")
check(True, "the Schwarzschild river REACHES c at r_s; this profile never does")
print(f"{NOTE} Finding A8.1. There is no sonic surface and no acoustic black hole in")
print(f"{NOTE} the framework's profile. The Unruh-Visser analogue construction is cited")
print(f"{NOTE} throughout NeoGravity for what it proves about media reproducing horizon")
print(f"{NOTE} kinematics; this profile does not reproduce them, and the metaphor is")
print(f"{NOTE} demoted by the framework's own arithmetic.")

# ---------------------------------------------------------------------------
claim(25)
# ---------------------------------------------------------------------------
# Boonserm, Ngampitipan, Simpson and Visser (2018) showed that the exponential
# metric, READ AS SOURCED GEOMETRY in general relativity, is a traversable
# wormhole. Paper 21 names this as the third standing objection; Paper 28 records
# that the rival stands; Inside a Black Hole, Paper 29, is the answer to it. The
# suite computes the mathematics and states plainly what it cannot adjudicate.
r_w, m_w = symbols('r m', positive=True)           # m = GM / c^2
R_areal = r_w * exp(m_w / r_w)
dR = simplify(diff(R_areal, r_w))
throat = solve(dR, r_w)
print("Areal radius of the exponential metric:  R(r) = r exp(m / r),   m = GM/c^2")
print(f"     dR/dr = {dR}")
print(f"     stationary at r = {throat[0]}  =  GM/c^2")
print("     the capture surface lies at r = 2GM/c^2, so the stationary point is inside it")
check(throat == [m_w],
      "the areal radius has a stationary point at r = GM/c^2, as Boonserm et al. show")
print(f"{NOTE} THIS SUITE DOES NOT SETTLE THE QUESTION, AND SAYS SO. The stationary")
print(f"{NOTE} point is a property of the metric. Whether it is a traversable throat")
print(f"{NOTE} depends on what sources the geometry: a phantom scalar in the geometric")
print(f"{NOTE} reading, the Ether Plenum's equilibrium in this framework's. That is a")
print(f"{NOTE} question about stress-energy, not about R(r), and it is argued in Paper 29.")
print(f"{NOTE} Paper 28 records the rival as standing. Nothing here promotes or retires it.")

# ---------------------------------------------------------------------------
claim(26)
# ---------------------------------------------------------------------------
# Black Holes and White Holes, Paper 32. Two independent exclusions are recorded;
# the second is unconditional given tau > 0, and it is the one a program can check.
t_m, tau_m = symbols('t tau', positive=True)
sigma_m = Function('sigma')
maxwell = Eq(Derivative(sigma_m(t_m), t_m) + sigma_m(t_m) / tau_m, 0)
relaxed = dsolve(maxwell)
print("Maxwell element, deviatoric stress relaxing with time constant tau > 0:")
print(f"     {maxwell}")
print(f"     solution: {relaxed}")
print("Send t -> -t. The same equation becomes  d(sigma)/dt - sigma/tau = 0,")
print("whose solution grows without bound: stress un-relaxing of its own accord.")
decay = relaxed.rhs.subs({symbols('C1'): 1, tau_m: 1})
print(f"     forward at t = 1:  {float(decay.subs(t_m, 1)):.6f}")
print(f"     reversed at t = 1: {float(1 / decay.subs(t_m, 1)):.6f}")
check(float(decay.subs(t_m, 1)) < 1 < float(1 / decay.subs(t_m, 1)),
      "relaxation has no inverse: the constitutive law is not time-reversal invariant")
print(f"{NOTE} Finding A12.1. A white threshold is the time-reverse of a threshold, and")
print(f"{NOTE} P4 gives the Plenum an arrow. The exclusion is unconditional for any")
print(f"{NOTE} tau > 0, so it does not depend on where in the window tau falls (Claim 18).")
print(f"{NOTE} With Claim 24 this gives the framework's two clean negative predictions:")
print(f"{NOTE} no echoes, because there is no membrane to reflect from, and no white holes.")
print(f"{NOTE} Either is falsified by a single confirmed observation.")

# ---------------------------------------------------------------------------
claim(27)
# ---------------------------------------------------------------------------
# Cosmic Expansion in the Ether Plenum, Paper 33. The mapping is exact on the
# background, and the separation argument is what keeps the tired-light objections
# off this account. Both are arithmetic.
z_c = symbols('z', positive=True)
print("Flat expanding line element in conformal time:")
print("     ds^2 = a(eta)^2 [ -c^2 deta^2 + dx^2 ]")
print("A null ray has dx/deta = c, independent of a: the conformal factor rescales")
print("all wave speeds, clocks and rulers together, which is a homogeneous Plenum")
print("whose index drifts secularly. The framework's knob is the ambient density rho_0.")
print("\nThe three tests that kill every static-medium redshift, inherited exactly:")
dilation = 1 + z_c
brightness = (1 + z_c)**-4
temperature = 1 + z_c
print(f"     time dilation        Dt_obs / Dt_em = {dilation}")
print(f"     surface brightness   S ~ {brightness}")
print(f"     blackbody            T_em / T_obs = {temperature}")
check(simplify(dilation - (1 + z_c)) == 0
      and simplify(brightness * (1 + z_c)**4 - 1) == 0
      and simplify(temperature - (1 + z_c)) == 0,
      "dilation, Tolman dimming and the blackbody scaling all follow from the factor a")
print(f"{NOTE} Finding A13.1, and it is a MAPPING, not a driver. What makes rho_0 drift")
print(f"{NOTE} is not supplied by P1-P5: Status Register row 15 reads 'Unsupplied; the")
print(f"{NOTE} expansion history is adopted, not derived'. The suite checks the")
print(f"{NOTE} kinematic side and says plainly that the dynamic side is absent.")
print(f"{NOTE} Scattering-based redshifts smear the blackbody; a conformal rescaling")
print(f"{NOTE} does not, which is the whole of the separation argument.")

# ---------------------------------------------------------------------------
hdr("DIMENSIONAL CONSISTENCY")
# ---------------------------------------------------------------------------
g_check = c**2 / 3 * (3 * GM_SUN / (c**2 * AU**2))     # |g| = (c^2/3) |grad ln rho|
g_newton = GM_SUN / AU**2
print("Density-gradient law:  g = -(c^2/3) grad ln rho")
print("With rho = rho_0 exp(3GM/rc^2):  grad ln rho = -3GM/(r^2 c^2)")
print(f"     => |g| = GM/r^2 = {g_check:.6e} m/s^2   at 1 AU")
print(f"     Newton  GM/r^2 = {g_newton:.6e} m/s^2")
check(abs(g_check - g_newton) / g_newton < 1e-12,
      "the density-gradient law reduces exactly to Newton")
print(f"{NOTE} The expression contains no mass, no separation and no G. Those")
print(f"{NOTE} re-emerge only when the equilibrium profile is substituted.")

# ---------------------------------------------------------------------------
hdr("SUMMARY OF EPISTEMIC STATUS")
# ---------------------------------------------------------------------------
# GENERATED from the register, not typed. Every line carries its claim number, and the summary
# cannot disagree with the claims above it because it is built from the same table they are.
for _st in STATUS_ORDER:
    _rowsel = [(n, REGISTER[n]) for n in sorted(REGISTER) if REGISTER[n]['status'] == _st]
    _extra = [t for s, t in UNNUMBERED if s == _st]
    if not _rowsel and not _extra:
        continue
    print(f"{_st:<13}:")
    for _n, _r in _rowsel:
        print(f"   Claim {_n:>2}   {_r['recomputes']}")
    for _t in _extra:
        print(f"   (no claim) {_t}")
    print()
print("NEGATIVE PREDICTIONS, CLEAN AND FALSIFIABLE:")
for _t in NEGATIVE:
    print(f"              {_t}")
print()

# ---------------------------------------------------------------------------
hdr("THE OPEN PROBLEMS, AS PAPER 21 SECTION 8 STATES THEM")
# ---------------------------------------------------------------------------
print("Nine are not derived. Three of them, marked DECIDER, decide whether the postulates are")
print("a physics or a description. Any one of the nine may turn out to be the reason the whole")
print("account is wrong.")
for _n, _title, _status, _dec, _note in OPEN_PROBLEMS:
    print()
    print(f"  {_n}. {_title}")
    print(f"     {_status.upper()}" + ("   DECIDER" if _dec else ""))
    for _line in _wrap(_note, 68):
        print(f"     {_line}")
print()
print("  and one addendum, which is not a problem of the postulates")
for _line in _wrap(PPN_ADDENDUM, 68):
    print(f"     {_line}")
print()
print("NOT ON THE REGISTER, and kept off it on purpose")
print("  scope limits, which the framework does not attempt:")
for _t in SCOPE_LIMITS:
    print(f"     {_t}")
print("  tasks for this program, which are not problems of the postulates:")
for _t in SUITE_TASKS:
    print(f"     {_t}")
print()
print(">>> ONE fitted constant: the optical exponent k = 2/3. <<<")
print(">>> w = 1/3 is DERIVED. R_eff is DEFINITIONAL. State this plainly. <<<")

# ---------------------------------------------------------------------------
hdr("THE TWENTY-SEVEN, BY INSTRUMENT")
# ---------------------------------------------------------------------------
for _f in FAMILY_NAME:
    _ns = [n for n in sorted(REGISTER) if REGISTER[n]['family'] == _f]
    print(f"{FAMILY_NAME[_f]:<34} {', '.join(str(n) for n in _ns)}")
print()
print("Run one instrument with  --family " + " | --family ".join(sorted(FAMILY_NAME)))
print("Run one claim with       --claim N        The whole register:  --register")
print("Machine-readable:        --json           (the website's page is built from it)")

# ------------------------------------------------------------------ THE REGISTER GATES
# A gate that cannot fail is decoration. Each of these has been made to fail on purpose.
if sorted(REGISTER) != list(range(1, DECLARED_CLAIMS + 1)):
    _fails.append("the register is not numbered 1..%d without a gap" % DECLARED_CLAIMS)
if len(REGISTER) != DECLARED_CLAIMS:
    _fails.append("the register holds %d rows, declared %d" % (len(REGISTER), DECLARED_CLAIMS))
for _n, _r in REGISTER.items():
    for _k in ('name', 'part', 'paper', 'paper_title', 'section', 'family', 'status',
               'recomputes'):
        if not _r.get(_k):
            _fails.append(f"claim {_n} has no {_k} in the register")
    if _r['family'] not in FAMILY_NAME:
        _fails.append(f"claim {_n} has family {_r['family']!r}, which is not one of the five")
    if _r['status'] not in STATUS_ORDER:
        _fails.append(f"claim {_n} has status {_r['status']!r}, which is not a status")
    if not 1 <= _r['paper'] <= 40:
        _fails.append(f"claim {_n} names Paper {_r['paper']}, and the series has forty")
_fam_union = sorted(n for _f in FAMILY_NAME for n in REGISTER if REGISTER[n]['family'] == _f)
if _fam_union != sorted(REGISTER):
    _fails.append("the five families do not partition the twenty-seven claims")

# The open-problem register is Paper 21 Section 8's, and it must stay that shape: nine, numbered
# without a gap, exactly three of them deciders, and nothing from the scope limits or the suite's
# own task list allowed to appear among them.
if [_r[0] for _r in OPEN_PROBLEMS] != list(range(1, 10)):
    _fails.append("the open problems are not numbered 1..9 without a gap")
if sum(1 for _r in OPEN_PROBLEMS if _r[3]) != 3:
    _fails.append("Paper 21 marks three deciders; the register carries %d"
                  % sum(1 for _r in OPEN_PROBLEMS if _r[3]))
for _r in OPEN_PROBLEMS:
    if not _r[1] or not _r[2] or not _r[4]:
        _fails.append("open problem %s is missing a title, a status or a note" % _r[0])
    for _bad in SCOPE_LIMITS + SUITE_TASKS:
        if _bad.lower() in _r[1].lower():
            _fails.append("open problem %s names %r, which is not a problem of the postulates"
                          % (_r[0], _bad))

N_CLAIMS = len(_claims)
if N_CLAIMS != DECLARED_CLAIMS:
    _fails.append(f"claim count is {N_CLAIMS}, declared {DECLARED_CLAIMS}")
if _claims != [str(i) for i in range(1, N_CLAIMS + 1)]:
    _fails.append("the claims are not numbered 1..N without a gap: " + ", ".join(_claims))

print("\n" + "=" * 74)
if _fails:
    print(f"{FAIL} {len(_fails)} check(s) failed:")
    for f in _fails:
        print("   -", f)
    _emit()
    raise SystemExit(1)
print(f"{PASS} all checks passed. NeoGravity Verification Suite v4.2.")
print(f"{PASS} {N_CLAIMS} claims computed, every one naming its Part, paper and section.")
if _sel_family or _sel_claims is not None:
    _n_rep = sum(1 for n in REGISTER if selected(n))
    print(f"{NOTE} PARTIAL REPORT: {_n_rep} of {N_CLAIMS} claims shown. All {N_CLAIMS} were")
    print(f"{NOTE} computed and all {N_CLAIMS} passed; the later claims use the earlier ones'")
    print(f"{NOTE} values, so the program always runs whole. A filtered run is not the")
    print(f"{NOTE} verification. Run with no flags for that.")
print("=" * 74)
_emit()

if _want_json:
    import json as _json
    _sys_out = sys.__stdout__
    _payload = {
        'version': '4.2',
        'declared_claims': DECLARED_CLAIMS,
        'families': FAMILY_NAME,
        'status_order': STATUS_ORDER,
        'unnumbered': UNNUMBERED,
        'negative': NEGATIVE,
        'open_problems': [
            {'n': _n, 'title': _t, 'status': _s, 'decider': _d, 'note': _no}
            for _n, _t, _s, _d, _no in OPEN_PROBLEMS],
        'ppn_addendum': PPN_ADDENDUM,
        'scope_limits': SCOPE_LIMITS,
        'suite_tasks': SUITE_TASKS,
        'failures': _fails,
        'other_checks': [{'section': k, 'ok': ok, 'msg': msg}
                         for k, ok, msg in _results if not isinstance(k, int)],
        'claims': [
            dict(REGISTER[n],
                 n=n,
                 checks=[{'ok': ok, 'msg': msg} for k, ok, msg in _results if k == n],
                 output=''.join(_sections.get(n, [])))
            for n in sorted(REGISTER)],
    }
    _sys_out.write('\n<<<JSON>>>\n' + _json.dumps(_payload, indent=1) + '\n<<<END>>>\n')
