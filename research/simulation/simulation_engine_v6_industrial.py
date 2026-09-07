#!/usr/bin/env python3
"""
ALGORAPOLIS CIVILIZATION SIMULATION ENGINE V6 — INDUSTRIAL SOVEREIGNTY EXTENSION
=================================================================================
Source: ALGORAPOLIS — A Civilization Architecture Framework by Goodluck Japhet Macha (2026)
Companions: simulation_engine_v4.py (validated baseline — its file is UNCHANGED) and
simulation_engine_v5_family.py (family extension — its file is also UNCHANGED; this
module extends the shared V4 metric list in memory at runtime, so the metric stack
is V4's 15 + family_integrity (16th, V5) + industrial_capacity (17th, V6)).

Extension specified by: Priority Gap Part VIII — Productive Capacity and Industrial
Sovereignty (ALG-PRI-2026-008), Case Studies 10-12 (US deindustrialization, China
overmatch + NABEP, WWII arsenal), Deeper Research 12 (education-production pipeline,
ALG-SIM-DEEP-2026-012), and the registered Study 16 DP-ESG series.

WHAT V6 ADDS TO THE V4/V5 METHODOLOGY:
  1. 17th metric: industrial_capacity (IC) — ECI-style composite (economic
     complexity, manufacturing value-added, sole-source-inverse, critical-goods
     self-sufficiency) added in place to the V4 metric list after base-rate
     computation, so ALL V4 machinery treats it as a first-class metric
  2. State variable: adversary_dependency (D in [0.05, 0.95], init 0.30) — the
     Globalist Efficiency Trap accumulator, evolving per trade regime
  3. Trade-regime axis: globalist_efficiency / autarkic_dominance /
     strategic_sufficiency — each regime is a policy environment applied
     identically to all 10 governance systems (the V4 fairness convention);
     Algorapolis's DP-PC locks block the trap components of each regime,
     exactly as DP-FS locks blocked family-hostile decay in V5
  4. Five industrial shock types (trade_embargo, sanctions_regime,
     supply_chain_weaponization, reindustrialization_response,
     tech_attrition_tail) — registered for lookup but NEVER drawn by the random
     V4 shock generator; they fire only through the trade-regime schedule
  5. Algorapolis DP-PC mechanisms: Industrial Sovereignty Locks (severity
     reduction), Industrial Capacity Dashboard (IC floor + runway-alarmed
     recovery), Protectionist Capture Guard (blocks the autarkic capture drag)
  6. Empirical interaction logic: war severity x1.25 and duration +2 when
     IC < 0.55 (the CSIS munitions-runway constraint); war-ramp conversion
     bonus for Algorapolis (WWII arsenal architecture, DP-PC-5); sanctions
     adaptation (impact halves after year 2 — Russia 2022: forecast -8.5/-10%,
     actual -2.1%); leverage decay (each weaponization event decays the next —
     the boomerang law: weaponization destroys the weapon on a 1-10yr clock)

DOCUMENT GROUNDING FOR THE INDUSTRIAL DOMAIN:
  DP-PC-1/2/3: criticality registers + adversary-graded caps + production-function
    dependency measurement (EU CRMA 10/40/25/65; API 13-17% direct vs ~47%
    effective exposure — gross imports understate ~3x)
  DP-PC-5: arsenal continuity (CSIS First Battle 2023: LRASM <1 week vs 18-24mo
    replacement, runway ratio ~= 0.01; WWII conversion ceiling ~40% of GNP)
  DP-PC-9: protectionist capture guard (sugar program $2.4-4B/yr to ~10k growers;
    WTO Art. XXI abuse; F-35 incentive fees; sunset-clause erosion)
  DP-PC-10: multi-administration continuity (ramp slippage 1.5-3x observed)
  DP-PC-12: blockade graceful degradation (Germany FSRU terminals in ~9 months;
    provenance classes — the sourced 232x, never the viral 350x)
  DP-ESG-2/3/7 (Study 16, registered by Part VIII): chokepoint diversification,
    developmental-state capabilities with Amsden reciprocity, no-dominance mirror cap

VALIDATION TARGETS (real-world episodes the calibrated dynamics must reproduce):
  1. Russia 2022 sanctions path: shallow initial GDP hit, slow attrition after
  2. Germany 2022 energy shock: persistent, large energy-intensive output loss
  3. China 2023-25 mineral controls: boomerang (adversary rerouting accelerates)
  4. US 155mm ramp: 3-4 year lag before reindustrialization response lands
  5. CSIS wargame depletion: war amplified and prolonged when IC < 0.55
  6. IMF fragmentation ordering: friend-shore (1.8%) < reshore (4.5%) < autarky
     costs — strategic_sufficiency outperforms both failure regimes
  7. Sanctions base rates: ~34% (HSE) / ~13% post-1970 unilateral (PIIE)
  8. NABEP/dominance pattern: autarkic_dominance buys dependency floors at
     growth, innovation, and capture costs that compound over the century

Usage (place alongside simulation_engine_v4.py and simulation_engine_v5_family.py
in research/simulation/):
    python simulation_engine_v6_industrial.py                 # 3 regimes, default runs
    python simulation_engine_v6_industrial.py --runs 50       # full parity with V4
    python simulation_engine_v6_industrial.py --regimes strategic_sufficiency
    python simulation_engine_v6_industrial.py --runs 2        # fast validation
"""

import json
import math
import random
import os
import sys
import argparse
from collections import defaultdict

# Import the validated baselines (same directory)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import simulation_engine_v4 as v4
import simulation_engine_v5_family as v5   # provides the 16th metric (family_integrity)

# ============================================================
# CONFIGURATION
# ============================================================
START_YEAR = 2026
END_YEAR = 2125
NUM_VILLAGES = 10
POP_PER_VILLAGE = 500
MONTE_CARLO_RUNS = 20          # default; use --runs 50 for full V4 parity
SEED_START = 262               # distinct seed base from V4 (42-91) and V5 (142)

INDUSTRIAL_METRIC = "industrial_capacity"
FAMILY_METRIC = v5.FAMILY_METRIC
GOVERNANCE_SYSTEMS = v4.GOVERNANCE_SYSTEMS

# Empirical constants (document grounding in the module docstring)
WAR_IC_CONSTRAINT = 0.55       # below this, war severity x1.25, duration +2 (CSIS)
LEVERAGE_DECAY = 0.85          # each weaponization event decays the next (boomerang)

# ============================================================
# TRADE REGIMES (the experimental axis)
# ============================================================
# Coupling semantics:
#   - Rate-level modifiers (prosperity/technology/equity/freedom/IC) are applied
#     inside compute_metric_growth_rates_v6, following the V4 fairness convention
#     (the regime is the environment; per-gov parameters encode how each system's
#     architecture responds to that environment — Algorapolis's DP-PC locks block
#     the trap components, exactly as DP-FS locks blocked hostile decay in V5).
#   - Shock-level multipliers (embargo/attrition factors) are applied inside
#     IndustrialVillageSimulation.apply_shock, scaled by the live
#     adversary_dependency state where the doctrine specifies it.

TRADE_REGIMES = {
    "globalist_efficiency": {
        "description": (
            "Post-Cold War sourcing doctrine: unit cost as the sole criterion, "
            "just-in-time logistics, resilience purchasable on demand (Part VIII "
            "Section 1.2). Cheap inputs lift prosperity while capacity atrophies "
            "and adversary dependency accumulates — the trap is invisible inside "
            "GDP until the embargo arrives amplified by the accumulated dependency. "
            "Calibrated on the US 2000-2026 experience (PNTR/WTO -> 91K plants -> "
            "runway ratio ~= 0.01)."
        ),
        # Annual adversary_dependency drift by system (the trap accumulator).
        # Algorapolis: DP-PC-1/2 criticality machinery + cap alarms slow the
        # accumulation (not zero — the regime is the polity's own doctrine).
        "d_drift": {
            "Capitalism": 0.015, "Corporatocracy": 0.017, "Democracy": 0.014,
            "Network_State": 0.015, "Technocracy": 0.012, "Socialism": 0.010,
            "Ecocracy": 0.011, "Anarcho_Syndicalism": 0.009, "Communism": 0.008,
            "Algorapolis": 0.004,   # DP-PC-2/3: registers alarm + ladder corrects
        },
        # Annual industrial_capacity growth penalty by system (capacity atrophy).
        # Market-signal systems hollow fastest; Algorapolis holds floors.
        "ic_growth_penalty": {
            "Capitalism": 0.005, "Corporatocracy": 0.006, "Network_State": 0.005,
            "Democracy": 0.003, "Technocracy": 0.002, "Socialism": 0.002,
            "Ecocracy": 0.002, "Anarcho_Syndicalism": 0.001, "Communism": 0.001,
            "Algorapolis": 0.000,   # DP-PC-1/2: strategic register floors hold IC
        },
        # Cheap-input prosperity bonus (rate add, all systems — the trap's bait)
        "prosperity_bonus": 0.004,
        # Embargo impact multiplier: 1 + 0.6 * D (the accumulated dependency
        # amplifies the embargo — Germany 2022 pattern)
        "embargo_d_amplification": 0.6,
    },
    "autarkic_dominance": {
        "description": (
            "Self-sufficiency pursued past the sufficiency threshold and converted "
            "into coercive leverage: standing industrial programs without expiry, "
            "chokepoint positions over other polities (Part VIII Section 1.3, "
            "Variant A+B combined). Dependency collapses to the floor — embargoes "
            "barely bite — but growth, innovation, and institutional capture pay "
            "compounding costs, and the polity becomes the sanctions target. "
            "Calibrated on Ujamaa/ISI (rent capture), Japan's zombie equilibrium, "
            "and China's overmatch-with-brittleness ledger (290% debt/GDP)."
        ),
        "d_target": 0.05,          # dependency driven to the floor
        "d_rate": 0.020,           # annual approach rate toward the target
        "ic_growth_bonus": 0.003,  # forced capacity buildout (real, expensive)
        "growth_penalty": 0.005,   # prosperity rate penalty (autarky's GDP cost)
        "technology_mult": 0.88,   # innovation penalty (closed-system atrophy)
        # Capture drag on equity/freedom rates by system (the rent-seeking
        # signature: support without expiry + no external examiner + no exit).
        # Algorapolis: DP-PC-9 circuitry (sunsets, reciprocity, adjudication)
        # blocks the drag.
        "capture_drag": {
            "Communism": 0.004, "Technocracy": 0.003, "Socialism": 0.003,
            "Corporatocracy": 0.002, "Capitalism": 0.002, "Democracy": 0.001,
            "Ecocracy": 0.001, "Network_State": 0.001, "Anarcho_Syndicalism": 0.001,
            "Algorapolis": 0.000,   # DP-PC-9: anti-capture circuitry holds
        },
        "embargo_mult": 0.30,      # embargoes barely bite an autarkic polity
        "attrition_mult": 1.3,     # but it pays more under sanctions/attrition
    },
    "strategic_sufficiency": {
        "description": (
            "The Part VIII doctrine: bounded domestic and allied capacity for "
            "register-class inputs — criticality machinery, adversary-graded caps "
            "(65/40/25%), stage floors (10/40/25%), 30/60/90-day buffers, the "
            "cheapest-first intervention ladder, anti-capture circuitry, and the "
            "no-dominance mirror cap. Calibrated on EU CRMA 2024, Japan ESPA 2022, "
            "the IEA reserve system, and the IMF cost ordering (friend-shoring "
            "~1.8% of GDP vs reshoring ~4.5%)."
        ),
        "d_target": 0.25,          # bounded floor — neither trap
        "d_rate": 0.010,           # annual approach rate toward the target
        "ic_growth_bonus": 0.004,  # deliberate, ladder-escalated capacity build
        "embargo_mult": 0.55,      # buffers + diversification absorb over half
        "attrition_mult": 0.70,    # redundancy shortens attrition tails
    },
}

# ============================================================
# 5 INDUSTRIAL-SPECIFIC SHOCK TYPES
# ============================================================
# Registered into the V4 shock-profile table for lookup, but NOT appended to
# v4.SHOCK_TYPES — the random V4 shock generator therefore never draws them.
# They fire only through the trade-regime schedule below.

V6_INDUSTRIAL_SHOCKS = {
    "trade_embargo": {
        "impacts": {INDUSTRIAL_METRIC: -0.15, "prosperity": -0.10, "resources": -0.08,
                    "resilience": -0.05, "monetary_system": -0.05},
        "duration_range": (2, 5),
        "note": ("Adversary cutoff of register-class inputs (Russia gas 2022; China "
                 "REE license regime Apr 2025). Severity scales with the live "
                 "adversary_dependency state under globalist_efficiency: x(1+0.6*D)"),
    },
    "sanctions_regime": {
        "impacts": {INDUSTRIAL_METRIC: -0.08, "prosperity": -0.10, "monetary_system": -0.10,
                    "technology": -0.06, "equity": -0.04},
        "duration_range": (5, 15),
        "note": ("Coalition sanctions with a 5-15yr adaptation horizon; effective "
                 "per-year impact halves after year 2 (Russia 2022: -2.1% actual "
                 "vs -8.5/-10% forecast; shadow fleet 150 -> 1,000+ tankers)"),
    },
    "supply_chain_weaponization": {
        "impacts": {INDUSTRIAL_METRIC: -0.12, "prosperity": -0.08, "technology": -0.06,
                    "security": -0.05, "resilience": -0.05},
        "duration_range": (3, 8),
        "note": ("Chokepoint escalation ladder (Ga/Ge 2023 -> Sb 2024 -> REE Apr 2025 "
                 "-> timed suspension Nov 2025). Cascade scales with dependency: "
                 "x(1+0.3*D); each prior event decays the next (boomerang law)"),
    },
    "reindustrialization_response": {
        "impacts": {INDUSTRIAL_METRIC: 0.18, "prosperity": 0.05, "technology": 0.05,
                    "resilience": 0.04, "social_classes": 0.03},
        "duration_range": (8, 15),
        "note": ("Positive spillover — the buildout program (155mm 14K -> 46K/mo in "
                 "3 yrs; TSMC AZ 4nm in ~4.5 yrs). Growth materializes after a "
                 "3-4yr lag enforced by the schedule; benefits are NOT strangulated "
                 "by shock resilience (V4 positive-spillover convention)"),
    },
    "tech_attrition_tail": {
        "impacts": {"technology": -0.08, INDUSTRIAL_METRIC: -0.08, "prosperity": -0.05,
                    "resilience": -0.04},
        "duration_range": (10, 20),
        "note": ("Slow degradation under sustained controls (EUV blockade; sanctions "
                 "decay literature). Bites hardest on the autarkic_dominance polity "
                 "(attrition x1.3) — the dominance position's deferred invoice"),
    },
}

for _stype, _profile in V6_INDUSTRIAL_SHOCKS.items():
    v4.SHOCK_PROFILES[_stype] = _profile

# ============================================================
# INDUSTRIAL-SPECIFIC METRIC WEIGHT (17th metric, V4 methodology)
# ============================================================
# Structural tendency of each system to build and maintain physical production
# capability WITHOUT a dedicated doctrine. Document-grounded: Corporatocracy and
# Network_State hollow toward services/finance; Communism builds heavy industry
# but brittly; Algorapolis highest (DP-PC lock series + skills substrate mandate).

INDUSTRIAL_METRIC_WEIGHTS = {
    "Capitalism": 0.90,          # deep industrial base, market-cycled, offshoring-prone
    "Socialism": 0.70,           # state capacity, moderate efficiency
    "Communism": 0.60,           # heavy-industry bias, soft budgets, brittle
    "Democracy": 0.75,           # mixed economy, electoral-cycle amnesia
    "Algorapolis": 1.20,         # DP-PC lock series + DP-PC-6 skills substrate
    "Corporatocracy": 0.55,      # financialization, offshoring preference
    "Ecocracy": 0.50,            # post-industrial preference
    "Technocracy": 0.85,         # planning capacity, manpower-planning risk
    "Anarcho_Syndicalism": 0.45, # thin industrial coordination
    "Network_State": 0.40,       # digital-first, thin physical base
}

# ============================================================
# ALGORAPOLIS INDUSTRIAL MECHANISMS (DP-PC document-grounded)
# ============================================================
ALGORAPOLIS_INDUSTRIAL_MECHANISMS = {
    "Industrial_Sovereignty_Locks": {
        "principle": "DP-PC-1, DP-PC-2, DP-PC-3",
        "effect": ("Criticality registers, adversary-graded caps, and production-"
                   "function dependency measurement block efficiency-trap drift and "
                   "reduce industrial-shock severity at the formal-verification layer"),
        "industrial_shock_severity_reduction": 0.60,
    },
    "Industrial_Capacity_Dashboard": {
        "principle": "DP-PC-5, DP-PC-6, DP-PC-10",
        "effect": ("NDT industrial telemetry with runway alarms: IC floor, recovery "
                   "protocols below the monitoring threshold, and multi-"
                   "administration continuity of capacity programs"),
        "ic_floor": 0.55,              # constitutional floor (below = forced recovery)
        "ic_recovery_threshold": 0.65, # monitoring threshold
        "ic_recovery_boost": 0.006,
    },
    "Protectionist_Capture_Guard": {
        "principle": "DP-PC-9 (Amsden reciprocity + sunset circuitry)",
        "effect": ("Blocks the autarkic-regime capture drag (sunsets, adjudicated "
                   "security claims, output-contingent incentives); the "
                   "reindustrialization_response benefit lands un-modulated"),
        "capture_drag_blocked": True,
    },
}

# ============================================================
# GROWTH RATES WITH THE 17TH METRIC
# ============================================================
_BASE_RATES_CACHE = None

def _get_base_rates():
    """
    Compute the V5 16-metric base rates ONCE (V4's 15 + family_integrity), then
    extend the V4 metric list in place with industrial_capacity so every
    downstream V4 computation (growth loop, stats, pairwise, phases) treats
    industrial_capacity as a first-class metric.
    """
    global _BASE_RATES_CACHE
    if _BASE_RATES_CACHE is None:
        _BASE_RATES_CACHE = v5._get_base_rates()      # V4 15 metrics + FI appended
        if INDUSTRIAL_METRIC not in v4.METRICS:
            v4.METRICS.append(INDUSTRIAL_METRIC)
    return _BASE_RATES_CACHE


def compute_metric_growth_rates_v6(trade_regime):
    """
    V5-neutral family rates for the 16 metrics (the family axis is not under
    experiment here — family_integrity follows its organic dynamics), plus
    industrial_capacity computed with the V4 formula (growth_rate x weight x
    stability x innovation modifiers) and the trade-regime modifiers:
      - globalist_efficiency: IC penalty (per-gov) + prosperity bonus
      - autarkic_dominance:   IC bonus, growth penalty, technology x0.88,
                              capture drag (per-gov, equity+freedom)
      - strategic_sufficiency: IC bonus (the ladder buildout)
    """
    family_neutral_rates = v5.compute_metric_growth_rates_v5("family_neutral")
    _get_base_rates()   # ensure IC is in v4.METRICS before any village is built

    regime = TRADE_REGIMES[trade_regime]
    rates = {}
    for gov in GOVERNANCE_SYSTEMS:
        rates[gov] = dict(family_neutral_rates[gov])
        base = v4.BASELINE_PARAMS[gov]
        weight = INDUSTRIAL_METRIC_WEIGHTS[gov]

        # V4 normalization pipeline (mirrored exactly from V5)
        raw_rate = base["growth_rate"] * weight
        stability_mod = 0.8 + 0.2 * base["stability"]
        innovation_mod = 1.0 + 0.3 * (base["innovation_rate"] - 0.05)
        ic_rate = raw_rate * stability_mod * innovation_mod

        if trade_regime == "globalist_efficiency":
            ic_rate -= regime["ic_growth_penalty"][gov]
            rates[gov]["prosperity"] += regime["prosperity_bonus"]
        elif trade_regime == "autarkic_dominance":
            ic_rate += regime["ic_growth_bonus"]
            rates[gov]["prosperity"] -= regime["growth_penalty"]
            rates[gov]["technology"] *= regime["technology_mult"]
            drag = regime["capture_drag"][gov]
            rates[gov]["equity"] -= drag
            rates[gov]["freedom"] -= drag
        elif trade_regime == "strategic_sufficiency":
            ic_rate += regime["ic_growth_bonus"]

        rates[gov][INDUSTRIAL_METRIC] = ic_rate

    return rates

# ============================================================
# VILLAGE SIMULATION (V4 subclass with the industrial layer)
# ============================================================
class IndustrialVillageSimulation(v4.VillageSimulation):
    """
    A V4 village with the industrial_capacity layer, the adversary_dependency
    state, trade-regime dynamics, sanctions adaptation, war-constraint
    interaction, leverage decay, and Algorapolis DP-PC mechanisms.

    Organic growth of industrial_capacity is handled entirely by the V4 loop
    (v4.METRICS is extended in place, and self.metric_rates carries the IC rate
    including regime modifiers). This subclass adds ONLY the industrial-domain
    specifics.
    """

    def __init__(self, governance, village_id, rng, metric_growth_rates, trade_regime):
        super().__init__(governance, village_id, rng, metric_growth_rates)
        self.trade_regime = trade_regime
        self.metrics[INDUSTRIAL_METRIC] = 0.50        # neutral start, V4 convention
        self.metric_rates[INDUSTRIAL_METRIC] = metric_growth_rates[governance][INDUSTRIAL_METRIC]
        self.adversary_dependency = 0.30              # D in [0.05, 0.95], init 0.30
        self.weaponization_events = 0                 # boomerang counter

    def apply_shock(self, shock_type, year):
        """V4 shock application + regime/D-scaled industrial dynamics."""
        if shock_type in V6_INDUSTRIAL_SHOCKS:
            original_resilience = self.params["shock_resilience"]
            regime = self.trade_regime

            if shock_type == "trade_embargo":
                if regime == "globalist_efficiency":
                    # The accumulated dependency amplifies the embargo (Germany 2022)
                    factor = 1.0 + TRADE_REGIMES["globalist_efficiency"][
                        "embargo_d_amplification"] * self.adversary_dependency
                elif regime == "autarkic_dominance":
                    factor = TRADE_REGIMES["autarkic_dominance"]["embargo_mult"]
                else:  # strategic_sufficiency
                    factor = TRADE_REGIMES["strategic_sufficiency"]["embargo_mult"]
                effective = 1.0 - factor * (1.0 - original_resilience)

            elif shock_type == "supply_chain_weaponization":
                # Cascade scales with dependency; each prior event decays the
                # weapon (boomerang law: weaponization destroys the weapon)
                factor = 1.0 + 0.3 * self.adversary_dependency
                factor *= (LEVERAGE_DECAY ** self.weaponization_events)
                effective = 1.0 - factor * (1.0 - original_resilience)
                self.weaponization_events += 1

            elif shock_type == "sanctions_regime":
                if regime == "autarkic_dominance":
                    factor = TRADE_REGIMES["autarkic_dominance"]["attrition_mult"]
                else:
                    factor = 1.0
                effective = 1.0 - factor * (1.0 - original_resilience)

            elif shock_type == "tech_attrition_tail":
                if regime == "autarkic_dominance":
                    factor = TRADE_REGIMES["autarkic_dominance"]["attrition_mult"]
                elif regime == "strategic_sufficiency":
                    factor = TRADE_REGIMES["strategic_sufficiency"]["attrition_mult"]
                else:
                    factor = 1.0
                effective = 1.0 - factor * (1.0 - original_resilience)

            else:  # reindustrialization_response (positive buildout program)
                # V4 positive-spillover convention: benefits are not strangulated
                # by shock resilience (cf. technological_disruption spillover);
                # 0.10 leaves modest buildout friction
                effective = 0.10

            # Algorapolis: Industrial Sovereignty Locks cut severity further
            if self.governance == "Algorapolis":
                reduction = ALGORAPOLIS_INDUSTRIAL_MECHANISMS[
                    "Industrial_Sovereignty_Locks"]["industrial_shock_severity_reduction"]
                if shock_type != "reindustrialization_response":
                    effective = 1.0 - (1.0 - effective) * (1.0 - reduction)

            params_backup = self.params
            patched = dict(self.params)
            patched["shock_resilience"] = max(-0.5, min(0.99, effective))
            self.params = patched
            try:
                super().apply_shock(shock_type, year)
            finally:
                self.params = params_backup

        elif shock_type == "war":
            # CSIS munitions-runway constraint: a polity with industrial_capacity
            # below 0.55 fights longer, costlier wars (severity x1.25, duration +2)
            original_resilience = self.params["shock_resilience"]
            ic_constrained = self.metrics[INDUSTRIAL_METRIC] < WAR_IC_CONSTRAINT
            if ic_constrained:
                params_backup = self.params
                patched = dict(self.params)
                patched["shock_resilience"] = 1.0 - 1.25 * (1.0 - original_resilience)
                self.params = patched
                try:
                    super().apply_shock(shock_type, year)
                    if self.active_shocks:
                        rec = self.active_shocks[-1]
                        rec["duration"] += 2     # munitions depletion prolongs the war
                        rec["remaining"] += 2
                finally:
                    self.params = params_backup
            else:
                super().apply_shock(shock_type, year)

        else:
            super().apply_shock(shock_type, year)

    def step_year(self, year):
        """V4 year step (17 metrics, incl. organic IC growth) + industrial dynamics."""
        # --- 1. Adversary-dependency dynamics (the trap accumulator) ---
        regime = self.trade_regime
        if regime == "globalist_efficiency":
            drift = TRADE_REGIMES["globalist_efficiency"]["d_drift"][self.governance]
            self.adversary_dependency = min(0.95, self.adversary_dependency + drift)
        elif regime == "autarkic_dominance":
            target = TRADE_REGIMES["autarkic_dominance"]["d_target"]
            rate = TRADE_REGIMES["autarkic_dominance"]["d_rate"]
            if self.adversary_dependency > target:
                self.adversary_dependency = max(target, self.adversary_dependency - rate)
        elif regime == "strategic_sufficiency":
            target = TRADE_REGIMES["strategic_sufficiency"]["d_target"]
            rate = TRADE_REGIMES["strategic_sufficiency"]["d_rate"]
            if self.adversary_dependency < target:
                self.adversary_dependency = min(target, self.adversary_dependency + rate)
            else:
                self.adversary_dependency = max(target, self.adversary_dependency - rate)

        # --- 2. Standard V4 year step (all 17 metrics, shocks, population) ---
        super().step_year(year)

        # --- 3. Sanctions adaptation (Russia 2022: shallow hit, slow attrition) ---
        # After year 2 of a sanctions regime, the effective per-year impact halves
        # (rerouting, shadow fleets, CIPS growth — the 5-15yr adaptation horizon).
        for shock in self.active_shocks:
            if shock["shock_type"] == "sanctions_regime":
                years_elapsed = shock["duration"] - shock["remaining"]
                if years_elapsed >= 2:
                    for metric, impact in shock["impacts"].items():
                        if metric in self.metrics and impact < 0:
                            self.metrics[metric] += (
                                0.5 * abs(impact) / shock["duration"])

        # --- 4. War-ramp conversion bonus (WWII arsenal architecture, DP-PC-5) ---
        war_active = any(s["shock_type"] == "war" for s in self.active_shocks)
        if war_active and self.governance == "Algorapolis":
            # Conversion governance doubles the organic IC ramp during wartime
            self.metrics[INDUSTRIAL_METRIC] = min(
                0.99, self.metrics[INDUSTRIAL_METRIC] + 0.006)

        # --- 5. Algorapolis industrial mechanisms ---
        if self.governance == "Algorapolis":
            dashboard = ALGORAPOLIS_INDUSTRIAL_MECHANISMS[
                "Industrial_Capacity_Dashboard"]
            if self.metrics[INDUSTRIAL_METRIC] < dashboard["ic_floor"]:
                # Constitutional floor (DP-PC-1/2) — forced recovery below floor
                self.metrics[INDUSTRIAL_METRIC] = min(
                    0.99, self.metrics[INDUSTRIAL_METRIC] + 0.010)
            elif self.metrics[INDUSTRIAL_METRIC] < dashboard["ic_recovery_threshold"]:
                # NDT runway-alarmed recovery (DP-PC-5 telemetry)
                self.metrics[INDUSTRIAL_METRIC] = min(
                    0.99, self.metrics[INDUSTRIAL_METRIC]
                    + dashboard["ic_recovery_boost"])

        # --- 6. Defensive re-clamp (super() already clamped the 17-metric loop) ---
        self.metrics[INDUSTRIAL_METRIC] = max(0.05, min(0.99, self.metrics[INDUSTRIAL_METRIC]))
        self.adversary_dependency = max(0.05, min(0.95, self.adversary_dependency))


# ============================================================
# TRADE-REGIME EVENT SCHEDULE
# ============================================================
def generate_industrial_regime_schedule(rng, trade_regime):
    """
    Regime-specific scheduled events, following the V4 shock-schedule fairness
    convention: the ADVERSARY environment (weaponization waves, the major
    embargo, the sanctions event) is generated FIRST with identical RNG
    consumption for every regime — the adversary acts regardless of the
    polity's doctrine. What differs is the doctrine's RESPONSE schedule.
    """
    schedule = defaultdict(list)

    def add_global(year, stype):
        for gov in GOVERNANCE_SYSTEMS:
            schedule[year].append({
                "type": stype, "governance": gov,
                "village_idx": -1, "scope": "global_industrial",
            })

    # --- Common adversary environment (identical across regimes, per seed) ---
    # Early chokepoint escalation ladder (China 2023-25 pattern)
    for _ in range(rng.randint(2, 4)):
        year = START_YEAR + rng.randint(8, 25)
        add_global(year, "supply_chain_weaponization")
    # The major embargo (the trap discovered — Russia gas / REE-license pattern)
    embargo_year = START_YEAR + rng.randint(30, 55)
    add_global(embargo_year, "trade_embargo")
    # A coalition sanctions event
    sanctions_year = START_YEAR + rng.randint(15, 45)
    add_global(sanctions_year, "sanctions_regime")
    # A second, late weaponization wave
    late_year = START_YEAR + rng.randint(55, 80)
    add_global(late_year, "supply_chain_weaponization")

    # --- Doctrine-specific responses ---
    if trade_regime == "strategic_sufficiency":
        # DP-PC ladder response: the buildout lands 3-4 years after the embargo
        # (155mm 14K -> 46K/mo in 3 yrs; TSMC AZ 4nm in ~4.5 yrs)
        response_year = embargo_year + rng.randint(3, 4)
        add_global(response_year, "reindustrialization_response")
    elif trade_regime == "globalist_efficiency":
        # The trap: the response only begins after the crash is absorbed, and
        # it comes a decade late (CSIS 2023 -> NDIS 2024 -> CHIPS ramp pattern)
        response_year = embargo_year + rng.randint(10, 18)
        add_global(response_year, "reindustrialization_response")
    elif trade_regime == "autarkic_dominance":
        # The self-harm: the dominance position's deferred invoice
        attrition_year = START_YEAR + rng.randint(20, 40)
        add_global(attrition_year, "tech_attrition_tail")

    return dict(schedule)


# ============================================================
# SIMULATION RUNNERS
# ============================================================
def run_single_simulation_v6(seed, trade_regime):
    """One 100-year run under one trade regime (V4 structure)."""
    rng = random.Random(seed)
    metric_growth_rates = compute_metric_growth_rates_v6(trade_regime)

    villages = {}
    for gov in GOVERNANCE_SYSTEMS:
        villages[gov] = [
            IndustrialVillageSimulation(
                gov, i, random.Random(rng.randint(0, 999999)),
                metric_growth_rates, trade_regime)
            for i in range(NUM_VILLAGES)
        ]

    v4_schedule = v4.generate_shock_schedule(rng)
    industrial_schedule = generate_industrial_regime_schedule(rng, trade_regime)
    merged = defaultdict(list)
    for y, evts in v4_schedule.items():
        merged[y].extend(evts)
    for y, evts in industrial_schedule.items():
        merged[y].extend(evts)

    for year_offset in range(END_YEAR - START_YEAR + 1):
        year = START_YEAR + year_offset
        if year in merged:
            for shock_event in merged[year]:
                gov = shock_event["governance"]
                village_idx = shock_event["village_idx"]
                if village_idx == -1:
                    for v in villages[gov]:
                        v.apply_shock(shock_event["type"], year)
                else:
                    villages[gov][village_idx].apply_shock(shock_event["type"], year)
        for gov in GOVERNANCE_SYSTEMS:
            for village in villages[gov]:
                village.step_year(year)

    results = {}
    for gov in GOVERNANCE_SYSTEMS:
        results[gov] = aggregate_governance_data_v6(villages[gov], gov)

    all_shocks = []
    for gov in GOVERNANCE_SYSTEMS:
        for village in villages[gov]:
            all_shocks.extend(village.shock_log)
    return results, all_shocks


def aggregate_governance_data_v6(villages, governance):
    """V4 aggregation (now includes IC in all metric tables) + industrial telemetry."""
    aggregated = v4.aggregate_governance_data(villages, governance)

    final_ic = sum(v.metrics[INDUSTRIAL_METRIC] for v in villages) / len(villages)
    final_d = sum(v.adversary_dependency for v in villages) / len(villages)
    weaponizations = sum(v.weaponization_events for v in villages)
    aggregated["industrial_sovereignty"] = {
        "final_industrial_capacity": round(final_ic, 4),
        "final_adversary_dependency": round(final_d, 4),
        "weaponization_events_absorbed": weaponizations,
        "note": ("IC = industrial_capacity (17th metric). D = adversary_dependency "
                 "state. Regime definitions and document grounding in "
                 "simulation_engine_v6_industrial.py header."),
    }
    return aggregated


# ============================================================
# MONTE CARLO + COMPARISON (V4 statistical methodology)
# ============================================================
def run_monte_carlo_v6(trade_regime, runs):
    print("=" * 70)
    print("ALGORAPOLIS CIVILIZATION SIMULATION V6 — INDUSTRIAL SOVEREIGNTY")
    print(f"Regime: {trade_regime} | Runs: {runs} | Seeds {SEED_START}-{SEED_START + runs - 1}")
    print("Source: ALGORAPOLIS by Goodluck J. Macha (2026); DP-PC series (Part VIII)")
    print("=" * 70)

    all_results = []
    all_shocks = []
    for run_idx in range(runs):
        seed = SEED_START + run_idx
        print(f"\n  Run {run_idx + 1}/{runs} (seed={seed})...", end=" ", flush=True)
        results, shock_log = run_single_simulation_v6(seed, trade_regime)
        all_results.append(results)
        all_shocks.extend(shock_log)
        print("DONE", flush=True)

    print("\nComputing Monte Carlo statistics...")
    mc_stats = v4.compute_monte_carlo_stats(all_results)      # includes IC (17 metrics)
    pairwise = v4.compute_pairwise_comparisons(all_results)   # includes IC
    phase_analysis = v4.compute_phase_analysis(all_results)   # includes IC
    representative = all_results[0]
    return {
        "regime": trade_regime,
        "monte_carlo_runs": runs,
        "mc_stats": mc_stats,
        "pairwise": pairwise,
        "phase_analysis": phase_analysis,
        "representative": representative,
        "shock_count": len(all_shocks),
    }


def summarize_regime(bundle):
    """Final-year metric means per governance system under this regime."""
    summary = {}
    for gov in GOVERNANCE_SYSTEMS:
        stats = bundle["mc_stats"][gov]["final_metrics_stats"]
        row = {metric: s["mean"] for metric, s in stats.items()}
        row["industrial_sovereignty"] = bundle["representative"][gov].get(
            "industrial_sovereignty", {})
        summary[gov] = row
    return summary


def print_industrial_comparison(regime_summaries):
    """Cross-regime comparison on industrial_capacity and adversary_dependency."""
    print("\n" + "=" * 92)
    print("TRADE-REGIME COMPARISON — FINAL-YEAR (2125) METRIC MEANS")
    print("=" * 92)
    header = (f"{'System':<22}{'glob:IC':>9}{'auto:IC':>9}{'suff:IC':>9}"
              f"{'glob:D':>9}{'auto:D':>9}{'suff:D':>9}"
              f"{'glob:prosp':>12}{'suff:prosp':>12}")
    print(header)
    print("-" * 92)
    for gov in GOVERNANCE_SYSTEMS:
        g = regime_summaries.get("globalist_efficiency", {}).get(gov, {})
        a = regime_summaries.get("autarkic_dominance", {}).get(gov, {})
        s = regime_summaries.get("strategic_sufficiency", {}).get(gov, {})
        gi = g.get("industrial_sovereignty", {})
        ai = a.get("industrial_sovereignty", {})
        si = s.get("industrial_sovereignty", {})
        val = lambda d, k: d.get(k, float("nan"))
        print(f"{gov:<22}"
              f"{val(gi, 'final_industrial_capacity'):>9.3f}"
              f"{val(ai, 'final_industrial_capacity'):>9.3f}"
              f"{val(si, 'final_industrial_capacity'):>9.3f}"
              f"{val(gi, 'final_adversary_dependency'):>9.3f}"
              f"{val(ai, 'final_adversary_dependency'):>9.3f}"
              f"{val(si, 'final_adversary_dependency'):>9.3f}"
              f"{val(g, 'prosperity'):>12.3f}"
              f"{val(s, 'prosperity'):>12.3f}")
    print("=" * 92)
    print("Reading: IC = industrial_capacity (17th metric, DP-PC composite).")
    print("D = adversary_dependency (the Globalist Efficiency Trap accumulator).")
    print("Under globalist_efficiency, D climbs (~0.015/yr), embargoes hit amplified")
    print("x(1+0.6*D), and capacity atrophies — discovered only at embargo-time.")
    print("Under autarkic_dominance, D collapses to the floor and embargoes barely")
    print("bite, but growth/innovation/capture costs compound all century.")
    print("Under strategic_sufficiency, D bounds at 0.25, IC builds through the")
    print("ladder, and the reindustrialization response lands 3-4 yrs post-embargo.")
    print("Validation targets (Russia 2022, Germany 2022, CSIS depletion, IMF cost")
    print("ordering) are documented in the engine header. See paper 08 Sections 4, 7.2.")


# ============================================================
# OUTPUT + MAIN
# ============================================================
def main():
    parser = argparse.ArgumentParser(description="Algorapolis Simulation V6 (industrial extension)")
    parser.add_argument("--runs", type=int, default=MONTE_CARLO_RUNS)
    parser.add_argument("--regimes", nargs="*", default=list(TRADE_REGIMES.keys()))
    args = parser.parse_args()

    out_dir = os.path.dirname(os.path.abspath(__file__))
    regime_summaries = {}
    for regime in args.regimes:
        if regime not in TRADE_REGIMES:
            print(f"Unknown regime: {regime}; skipping.")
            continue
        bundle = run_monte_carlo_v6(regime, args.runs)

        with open(os.path.join(out_dir, f"simulation_results_industrial_{regime}.json"), "w") as f:
            json.dump(bundle["representative"], f, indent=2)
        with open(os.path.join(out_dir, f"monte_carlo_stats_industrial_{regime}.json"), "w") as f:
            json.dump(bundle["mc_stats"], f, indent=2)
        with open(os.path.join(out_dir, f"phase_analysis_industrial_{regime}.json"), "w") as f:
            json.dump(bundle["phase_analysis"], f, indent=2)

        regime_summaries[regime] = summarize_regime(bundle)

    print_industrial_comparison(regime_summaries)

    comparison = {
        "description": ("Trade-regime comparison (V6). IC = industrial_capacity, "
                        "17th metric per the Part VIII DP-PC series; D = "
                        "adversary_dependency state; regime definitions and "
                        "document grounding in simulation_engine_v6_industrial.py header."),
        "regimes_run": list(regime_summaries.keys()),
        "monte_carlo_runs": args.runs,
        "final_year_metric_means": regime_summaries,
    }
    with open(os.path.join(out_dir, "industrial_regime_comparison.json"), "w") as f:
        json.dump(comparison, f, indent=2)
    print(f"\nOutputs written to {out_dir}:")
    print("  simulation_results_industrial_<regime>.json (representative runs)")
    print("  monte_carlo_stats_industrial_<regime>.json")
    print("  phase_analysis_industrial_<regime>.json")
    print("  industrial_regime_comparison.json (cross-regime summary)")


if __name__ == "__main__":
    main()
