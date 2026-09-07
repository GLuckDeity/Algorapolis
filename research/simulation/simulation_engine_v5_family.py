#!/usr/bin/env python3
"""
ALGORAPOLIS CIVILIZATION SIMULATION ENGINE V5 — FAMILY & SOCIAL FABRIC EXTENSION
=================================================================================
Source: ALGORAPOLIS — A Civilization Architecture Framework by Goodluck Japhet Macha (2026)
Companion to: simulation_engine_v4.py (validated baseline — its file is UNCHANGED;
this module extends the V4 module in memory at runtime)

Extension specified by: Priority Gap Part VII — Family and Social Fabric
(ALG-PRI-2026-007), Case Studies 07-09 (kibbutz, Soviet de-familization, Norway CPS),
and the Family Integrity Index specification (DP-FS-10).

WHAT V5 ADDS TO THE V4 METHODOLOGY:
  1. 16th metric: family_integrity — added in place to the V4 metric list after
     base-rate computation, so ALL V4 machinery (organic growth loop, Grey Scale
     floor, Immune System recovery, Legitimacy Restoration, Monte Carlo stats,
     pairwise comparisons, phase analysis) treats it as a first-class metric
  2. Family-policy regime axis: family_hostile / family_neutral / family_integrative
     — each regime is a policy overlay applied identically to all 10 governance
     systems (the V4 fairness convention for global shocks)
  3. Five family-specific shock types (collectivization_program, threshold_creep,
     kinship_surveillance, demographic_crisis, family_policy_reversal) — scheduled
     only through the family-regime schedule, never drawn by the random V4 shock
     generator, so the neutral regime is not contaminated
  4. Algorapolis DP-FS mechanisms: Family_Sovereignty_Locks (constitutional floor +
     shock-severity reduction at the formal-verification layer), Family_Integrity_
     Index monitoring (FII-triggered recovery), Family_Policy_Capture_Guard
  5. Demand-side reversal dynamics (kibbutz/Soviet evidence, DP-FS-12): hostile
     regimes face internal reversal pressure when family_integrity collapses —
     IF the system's freedom permits expression of parental demand, or when
     demographic costs force even an authoritarian state to reverse

DOCUMENT GROUNDING FOR THE FAMILY DOMAIN:
  DP-FS-1/2: Parental primacy + material floor without custody transfer
    (Meyer/Pierce/Troxel line; CRC Art. 5/18; ECHR Art. 8; Shaefer et al. 2018/2024)
  DP-FS-3:  Formalized intervention threshold (Strand Lobben v. Norway 2019;
    US substantiation variance <6% to >50%, Font et al. 2019)
  DP-FS-6:  Provision pluralism (Quebec JPE 2019; East/West German cohorts)
  DP-FS-10: Family Integrity Index (kibbutz attachment 59% vs 65-70% baseline;
    van IJzendoorn; Sidi et al. 2020)
  DP-FS-11: Family-policy capture guard (Carnegie 2025; Study 18 antibodies)
  DP-FS-12: Reversibility (kibbutz communal sleeping abandoned by the 1990s;
    Soviet 1918 -> 1936 reversal in ~19 years)

Usage (place alongside simulation_engine_v4.py in research/simulation/):
    python simulation_engine_v5_family.py                      # 3 regimes, default runs
    python simulation_engine_v5_family.py --runs 50            # full parity with V4
    python simulation_engine_v5_family.py --regimes family_hostile
    python simulation_engine_v5_family.py --runs 2             # fast validation
"""

import json
import math
import random
import os
import sys
import argparse
from collections import defaultdict

# Import the validated V4 baseline (same directory)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import simulation_engine_v4 as v4

# ============================================================
# CONFIGURATION
# ============================================================
START_YEAR = 2026
END_YEAR = 2125
NUM_VILLAGES = 10
POP_PER_VILLAGE = 500
MONTE_CARLO_RUNS = 20          # default; use --runs 50 for full V4 parity
SEED_START = 142               # distinct seed base from V4 (42-91) for independence

FAMILY_METRIC = "family_integrity"
GOVERNANCE_SYSTEMS = v4.GOVERNANCE_SYSTEMS

# ============================================================
# FAMILY-POLICY REGIMES (the experimental axis)
# ============================================================
# Coupling semantics: drift_k = coupling[metric] * (family_integrity - 0.50).
# Positive coupling means family erosion (FI < 0.50) drags the coupled metric
# down, and family health lifts it — the Soviet demographic cost ledger.

FAMILY_REGIMES = {
    "family_hostile": {
        "description": (
            "Four-vector hostile program: provision monopolization, institutional "
            "default for care settings, intervention-threshold creep, and "
            "family-linked values scrutiny (Part VII Section 1 vectors). Calibrated "
            "on Soviet de-familization 1918-1936, kibbutz communal sleeping, "
            "Romanian institutional overflow, China SCS family-linked consequences."
        ),
        # Annual family_integrity decay rate by system vulnerability.
        # Constitutional-lock systems resist; Algorapolis blocks via DP-FS locks.
        "hostile_decay": {
            "Communism": 0.010, "Technocracy": 0.008, "Corporatocracy": 0.008,
            "Socialism": 0.006, "Network_State": 0.006, "Capitalism": 0.004,
            "Democracy": 0.003, "Ecocracy": 0.003, "Anarcho_Syndicalism": 0.002,
            "Algorapolis": 0.000,   # DP-FS-1..4, 8: constitutional locks block decay
        },
        "coupling": {"demography": 0.005, "social_classes": 0.002, "resilience": 0.001},
    },
    "family_neutral": {
        "description": (
            "Status-quo family policy environment: no coordinated program touching "
            "family functions. family_integrity follows each system's organic "
            "dynamics (market time-pressure, welfare floors, cultural factors). "
            "Occasional background threshold-creep incidents (the Norway pattern "
            "occurs without any hostile program)."
        ),
        "hostile_decay": {g: 0.0 for g in GOVERNANCE_SYSTEMS},
        "coupling": {"demography": 0.002, "social_classes": 0.001},
    },
    "family_integrative": {
        "description": (
            "Material-floor-without-custody-transfer policy stack (DP-FS-2/6/7): "
            "unconditional child floors as cash/provision rights to the family, "
            "plural and choice-preserving care provision, alloparental "
            "infrastructure. Algorapolis additionally runs the full DP-FS lock "
            "series with FII monitoring. Calibrated on Shaefer et al. 2018/2024, "
            "Canada Child Benefit, the reformed-kibbutz hybrid configuration."
        ),
        # Annual family_integrity growth bonus by system (floors help everywhere;
        # Algorapolis runs the full specification)
        "integrative_bonus": {
            "Capitalism": 0.004, "Socialism": 0.005, "Communism": 0.004,
            "Democracy": 0.006, "Algorapolis": 0.010,
            "Corporatocracy": 0.003, "Ecocracy": 0.006, "Technocracy": 0.004,
            "Anarcho_Syndicalism": 0.005, "Network_State": 0.004,
        },
        "coupling": {"demography": 0.003, "social_classes": 0.002, "resilience": 0.001},
    },
}

# ============================================================
# 5 FAMILY-SPECIFIC SHOCK TYPES
# ============================================================
# Registered into the V4 shock-profile table for lookup, but NOT appended to
# v4.SHOCK_TYPES — the random V4 shock generator therefore never draws them.
# They fire only through the family-regime schedule below.

V5_FAMILY_SHOCKS = {
    "collectivization_program": {
        "impacts": {FAMILY_METRIC: -0.20, "demography": -0.08, "freedom": -0.10,
                    "social_classes": -0.06, "equity": -0.04},
        "duration_range": (5, 15),   # long policy programs, not events
        "note": "Provision monopolization wave (Vector 1+2): Soviet 1918-1936 pattern",
    },
    "threshold_creep": {
        "impacts": {FAMILY_METRIC: -0.10, "freedom": -0.06, "equity": -0.05},
        "duration_range": (3, 8),
        "note": "Intervention-standard drift (Vector 3): Norway/variance pattern",
    },
    "kinship_surveillance": {
        "impacts": {FAMILY_METRIC: -0.12, "freedom": -0.12, "media_and_information": -0.04},
        "duration_range": (4, 10),
        "note": "Family-linked scoring/joint liability (Vector 4/Mode B): China SCS pattern",
    },
    "demographic_crisis": {
        "impacts": {"demography": -0.15, "prosperity": -0.08, "social_classes": -0.06,
                    FAMILY_METRIC: -0.05},
        "duration_range": (5, 12),
        "note": "Soviet cost-ledger endpoint: besprizornye + labor-force decline",
    },
    "family_policy_reversal": {
        "impacts": {FAMILY_METRIC: 0.15, "freedom": 0.05, "demography": 0.04},
        "duration_range": (4, 10),
        "note": ("Positive spillover — the reform wave after demand-side reversal "
                 "(kibbutz by the 1990s; Soviet 1936; Norway 2024-25): recovery "
                 "is real but slow and partial"),
    },
}

for _stype, _profile in V5_FAMILY_SHOCKS.items():
    v4.SHOCK_PROFILES[_stype] = _profile

# ============================================================
# FAMILY-SPECIFIC METRIC WEIGHT (16th metric, V4 methodology)
# ============================================================
# Structural tendency of each system to protect family functions WITHOUT a
# dedicated lock architecture. Document-grounded: Communism (de-familization +
# pronatalist oscillation) lowest; Democracy/Ecocracy moderate-high; Algorapolis
# highest (DP-FS lock series + alloparental infrastructure).

FAMILY_METRIC_WEIGHTS = {
    "Capitalism": 0.70,          # family autonomy high, market time-pressure high
    "Socialism": 0.60,           # provision strong, family autonomy moderate
    "Communism": 0.40,           # historical de-familization + pronatalist oscillation
    "Democracy": 0.80,           # strong autonomy norms, moderate floors
    "Algorapolis": 1.20,         # DP-FS lock series + alloparental infrastructure
    "Corporatocracy": 0.45,      # family as labor-supply unit
    "Ecocracy": 0.85,            # community + household embeddedness
    "Technocracy": 0.50,         # family as optimization object
    "Anarcho_Syndicalism": 0.75, # community autonomy, thin floors
    "Network_State": 0.60,       # atomization risk, exit rights moderate
}

# ============================================================
# ALGORAPOLIS FAMILY MECHANISMS (DP-FS document-grounded)
# ============================================================
ALGORAPOLIS_FAMILY_MECHANISMS = {
    "Family_Sovereignty_Locks": {
        "principle": "DP-FS-1, DP-FS-2, DP-FS-3, DP-FS-8",
        "effect": ("Constitutional locks block hostile-regime decay and reduce "
                   "family-shock severity at the formal-verification layer"),
        "hostile_regime_blocked": True,
        "family_shock_severity_reduction": 0.70,
        "family_integrity_floor": 0.55,
    },
    "Family_Integrity_Index": {
        "principle": "DP-FS-10",
        "effect": ("NDT FII telemetry triggers automatic recovery protocols when "
                   "family_integrity drops below the monitoring threshold"),
        "fii_recovery_threshold": 0.60,
        "fii_recovery_boost": 0.006,
    },
    "Family_Policy_Capture_Guard": {
        "principle": "DP-FS-11",
        "effect": ("Study-18 antibody machinery on family-law/child-welfare surfaces: "
                   "threshold-creep and kinship-surveillance shocks detected early"),
        "early_detection_reduction": 0.50,   # extra severity cut for creep/surveillance
    },
    "Alloparental_Infrastructure": {
        "principle": "DP-FS-7",
        "effect": ("Distributed care support around the attachment unit lifts "
                   "organic family_integrity growth (reformed-kibbutz configuration)"),
        "family_metric_weight": FAMILY_METRIC_WEIGHTS["Algorapolis"],
    },
}


# ============================================================
# GROWTH RATES WITH THE 16TH METRIC
# ============================================================
_BASE_RATES_CACHE = None

def _get_base_rates():
    """
    Compute V4 base rates ONCE (15 metrics), then extend the V4 metric list
    in place so every downstream V4 computation (growth loop, stats, pairwise,
    phases) treats family_integrity as a first-class metric.
    """
    global _BASE_RATES_CACHE
    if _BASE_RATES_CACHE is None:
        _BASE_RATES_CACHE = v4.compute_metric_growth_rates()  # validated V4 computation
        if FAMILY_METRIC not in v4.METRICS:
            v4.METRICS.append(FAMILY_METRIC)
    return _BASE_RATES_CACHE


def compute_metric_growth_rates_v5(regime):
    """
    V4 growth rates for the 15 base metrics (identical to V4), plus
    family_integrity computed with the V4 formula (growth_rate x weight x
    stability x innovation modifiers) and the regime modifier:
      - family_hostile:     rate -= hostile_decay (Algorapolis: locks block decay)
      - family_integrative: rate += integrative_bonus
      - family_neutral:     organic rate only
    """
    base_rates = _get_base_rates()

    rates = {}
    for gov in GOVERNANCE_SYSTEMS:
        rates[gov] = dict(base_rates[gov])
        base = v4.BASELINE_PARAMS[gov]
        weight = FAMILY_METRIC_WEIGHTS[gov]

        # V4 normalization pipeline (mirrored exactly)
        raw_rate = base["growth_rate"] * weight
        stability_mod = 0.8 + 0.2 * base["stability"]
        innovation_mod = 1.0 + 0.3 * (base["innovation_rate"] - 0.05)
        fi_rate = raw_rate * stability_mod * innovation_mod

        if regime == "family_hostile":
            decay = FAMILY_REGIMES["family_hostile"]["hostile_decay"][gov]
            fi_rate = fi_rate - decay          # Algorapolis decay = 0.0 (locks)
        elif regime == "family_integrative":
            fi_rate += FAMILY_REGIMES["family_integrative"]["integrative_bonus"][gov]

        rates[gov][FAMILY_METRIC] = fi_rate

    return rates


# ============================================================
# VILLAGE SIMULATION (V4 subclass with family layer)
# ============================================================
class FamilyVillageSimulation(v4.VillageSimulation):
    """
    A V4 village with the family_integrity layer, regime dynamics, demand-side
    reversal pressure, and Algorapolis DP-FS mechanisms.

    Organic growth of family_integrity is handled entirely by the V4 loop
    (v4.METRICS is extended in place, and self.metric_rates carries the FI rate
    including regime modifiers). This subclass adds ONLY the family-domain
    specifics: coupling drift, DP-FS floors and FII recovery, and reversal.
    """

    def __init__(self, governance, village_id, rng, metric_growth_rates, regime):
        super().__init__(governance, village_id, rng, metric_growth_rates)
        self.regime = regime
        self.metrics[FAMILY_METRIC] = 0.50          # neutral start, V4 convention
        self.metric_rates[FAMILY_METRIC] = metric_growth_rates[governance][FAMILY_METRIC]
        self.reversal_active = False
        self.reversal_years_remaining = 0
        self.ever_reversed = False

    def apply_shock(self, shock_type, year):
        """V4 shock application + Algoropoulos family-lock severity reduction."""
        if shock_type in V5_FAMILY_SHOCKS and self.governance == "Algorapolis":
            locks = ALGORAPOLIS_FAMILY_MECHANISMS["Family_Sovereignty_Locks"]
            guard = ALGORAPOLIS_FAMILY_MECHANISMS["Family_Policy_Capture_Guard"]
            reduction = locks["family_shock_severity_reduction"]
            if shock_type in ("threshold_creep", "kinship_surveillance"):
                reduction = max(reduction, guard["early_detection_reduction"] + 0.20)
            original_resilience = self.params["shock_resilience"]
            # Effective resilience -> family-shock impacts scaled by (1 - resilience)
            # are blocked at the formal-verification layer before impacts compute
            effective = 1.0 - (1.0 - original_resilience) * (1.0 - reduction)
            params_backup = self.params
            patched = dict(self.params)
            patched["shock_resilience"] = effective
            self.params = patched
            try:
                super().apply_shock(shock_type, year)
            finally:
                self.params = params_backup
        else:
            super().apply_shock(shock_type, year)

    def step_year(self, year):
        """V4 year step (16 metrics, incl. organic FI growth) + family dynamics."""
        # --- 1. Coupling drift, applied before the V4 step ---
        # drift = k * (FI - 0.50): family erosion drags demography/cohesion down
        fi_current = self.metrics[FAMILY_METRIC]
        coupling = FAMILY_REGIMES[self.regime].get("coupling", {})
        for target_metric, k in coupling.items():
            if target_metric in self.metrics:
                self.metrics[target_metric] += k * (fi_current - 0.50)

        # --- 2. Standard V4 year step (all 16 metrics, shocks, population) ---
        super().step_year(year)

        # --- 3. Hostile-regime demand-side reversal pressure (DP-FS-12 evidence) ---
        if self.regime == "family_hostile" and self.governance != "Algorapolis":
            fi = self.metrics[FAMILY_METRIC]
            freedom = self.metrics["freedom"]
            demography = self.metrics["demography"]
            # Reversal preconditions (kibbutz: expressed parental demand via freedom;
            # Soviet: state cost feedback via demographic collapse or orphan-scale
            # family dissolution — besprizornye at the millions)
            can_express_demand = freedom > 0.60
            state_cost_pressure = demography < 0.45 or fi < 0.15
            if (not self.reversal_active) and year > START_YEAR + 30 and \
               (fi < 0.35) and (can_express_demand or state_cost_pressure):
                self.reversal_active = True
                self.ever_reversed = True
                self.reversal_years_remaining = 10
                self.shock_log.append({
                    "year": year, "village_id": self.village_id,
                    "governance": self.governance,
                    "shock_type": "family_policy_reversal_trigger",
                    "severity": round(fi, 4), "duration": 10, "remaining": 10,
                    "impacts": {},
                })
            if self.reversal_active and self.reversal_years_remaining > 0:
                # Recovery is real but slow and partial (kibbutz/Soviet/Norway pattern)
                self.metrics[FAMILY_METRIC] = min(0.99, self.metrics[FAMILY_METRIC] + 0.012)
                self.metrics["freedom"] = min(0.99, self.metrics["freedom"] + 0.002)
                self.metrics["demography"] = min(0.99, self.metrics["demography"] + 0.001)
                self.reversal_years_remaining -= 1
                if self.reversal_years_remaining == 0:
                    self.reversal_active = False

        # --- 4. Algorapolis family mechanisms ---
        if self.governance == "Algorapolis":
            locks = ALGORAPOLIS_FAMILY_MECHANISMS["Family_Sovereignty_Locks"]
            fii = ALGORAPOLIS_FAMILY_MECHANISMS["Family_Integrity_Index"]
            # Constitutional floor (DP-FS locks) — stronger than the Grey Scale floor
            if self.metrics[FAMILY_METRIC] < locks["family_integrity_floor"]:
                self.metrics[FAMILY_METRIC] = min(
                    0.99, self.metrics[FAMILY_METRIC] + 0.010)
            # FII monitoring recovery (DP-FS-10)
            elif self.metrics[FAMILY_METRIC] < fii["fii_recovery_threshold"]:
                self.metrics[FAMILY_METRIC] = min(
                    0.99, self.metrics[FAMILY_METRIC] + fii["fii_recovery_boost"])

        # --- 5. Clamp family_integrity (V4 convention; super() already clamped
        #        it in the 16-metric loop, this is a defensive re-clamp) ---
        self.metrics[FAMILY_METRIC] = max(0.05, min(0.99, self.metrics[FAMILY_METRIC]))


# ============================================================
# FAMILY-REGIME EVENT SCHEDULE
# ============================================================
def generate_family_regime_schedule(rng, regime):
    """
    Regime-specific scheduled events, following the V4 shock-schedule fairness
    convention: regime events hit governance systems identically (the regime is
    the environment); the system-level response differs by architecture.
    """
    schedule = defaultdict(list)
    num_years = END_YEAR - START_YEAR + 1

    if regime == "family_hostile":
        # Early program wave (years 3-12): provision monopolization rollout
        wave_year = START_YEAR + rng.randint(3, 12)
        for gov in GOVERNANCE_SYSTEMS:
            schedule[wave_year].append({
                "type": "collectivization_program", "governance": gov,
                "village_idx": -1, "scope": "global_family",
            })
        # Mid-century threshold-creep and surveillance waves (local, recurring)
        for _ in range(rng.randint(4, 7)):
            year = START_YEAR + rng.randint(10, num_years - 30)
            stype = rng.choice(["threshold_creep", "kinship_surveillance"])
            for gov in GOVERNANCE_SYSTEMS:
                schedule[year].append({
                    "type": stype, "governance": gov,
                    "village_idx": rng.randint(0, NUM_VILLAGES - 1),
                    "scope": "local_family",
                })
        # Late-century demographic reckoning (Soviet cost ledger, decades delayed)
        reckoning_year = START_YEAR + rng.randint(40, 70)
        for gov in GOVERNANCE_SYSTEMS:
            schedule[reckoning_year].append({
                "type": "demographic_crisis", "governance": gov,
                "village_idx": -1, "scope": "global_family",
            })

    elif regime == "family_neutral":
        # Background drift: occasional threshold-creep incidents (the Norway
        # pattern occurs without any hostile program)
        for _ in range(rng.randint(1, 3)):
            year = START_YEAR + rng.randint(15, num_years - 15)
            gov = rng.choice(GOVERNANCE_SYSTEMS)
            schedule[year].append({
                "type": "threshold_creep", "governance": gov,
                "village_idx": rng.randint(0, NUM_VILLAGES - 1),
                "scope": "local_family",
            })

    elif regime == "family_integrative":
        # One mid-century reform wave (the positive reversal shock) for systems
        # that had drifted; Algorapolis receives it as a mild confirmation event
        year = START_YEAR + rng.randint(20, 40)
        for gov in GOVERNANCE_SYSTEMS:
            schedule[year].append({
                "type": "family_policy_reversal", "governance": gov,
                "village_idx": -1, "scope": "global_family",
            })

    return dict(schedule)


# ============================================================
# SIMULATION RUNNERS
# ============================================================
def run_single_simulation_v5(seed, regime):
    """One 100-year run under one family-policy regime (V4 structure)."""
    rng = random.Random(seed)
    metric_growth_rates = compute_metric_growth_rates_v5(regime)

    villages = {}
    for gov in GOVERNANCE_SYSTEMS:
        villages[gov] = [
            FamilyVillageSimulation(
                gov, i, random.Random(rng.randint(0, 999999)),
                metric_growth_rates, regime)
            for i in range(NUM_VILLAGES)
        ]

    v4_schedule = v4.generate_shock_schedule(rng)
    family_schedule = generate_family_regime_schedule(rng, regime)
    merged = defaultdict(list)
    for y, evts in v4_schedule.items():
        merged[y].extend(evts)
    for y, evts in family_schedule.items():
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
        results[gov] = aggregate_governance_data_v5(villages[gov], gov)

    all_shocks = []
    for gov in GOVERNANCE_SYSTEMS:
        for village in villages[gov]:
            all_shocks.extend(village.shock_log)
    return results, all_shocks


def aggregate_governance_data_v5(villages, governance):
    """V4 aggregation (now includes FI in all metric tables) + reversal telemetry."""
    aggregated = v4.aggregate_governance_data(villages, governance)

    reversal_years = [s["year"] for v in villages for s in v.shock_log
                      if s["shock_type"] == "family_policy_reversal_trigger"]
    aggregated["family_reversal"] = {
        "villages_ever_reversed": sum(1 for v in villages if v.ever_reversed),
        "median_reversal_year": (sorted(reversal_years)[len(reversal_years) // 2]
                                 if reversal_years else None),
        "reversal_event_count": len(reversal_years),
    }
    return aggregated


# ============================================================
# MONTE CARLO + COMPARISON (V4 statistical methodology)
# ============================================================
def run_monte_carlo_v5(regime, runs):
    print("=" * 70)
    print("ALGORAPOLIS CIVILIZATION SIMULATION V5 — FAMILY & SOCIAL FABRIC")
    print(f"Regime: {regime} | Runs: {runs} | Seeds {SEED_START}-{SEED_START + runs - 1}")
    print("Source: ALGORAPOLIS by Goodluck Japhet Macha (2026); DP-FS series (Part VII)")
    print("=" * 70)

    all_results = []
    all_shocks = []
    for run_idx in range(runs):
        seed = SEED_START + run_idx
        print(f"\n  Run {run_idx + 1}/{runs} (seed={seed})...", end=" ", flush=True)
        results, shock_log = run_single_simulation_v5(seed, regime)
        all_results.append(results)
        all_shocks.extend(shock_log)
        print("DONE", flush=True)

    print("\nComputing Monte Carlo statistics...")
    mc_stats = v4.compute_monte_carlo_stats(all_results)      # includes FI (16 metrics)
    pairwise = v4.compute_pairwise_comparisons(all_results)   # includes FI
    phase_analysis = v4.compute_phase_analysis(all_results)   # includes FI
    representative = all_results[0]
    return {
        "regime": regime,
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
        row["family_reversal"] = bundle["representative"][gov].get("family_reversal", {})
        summary[gov] = row
    return summary


def print_family_comparison(regime_summaries):
    """Cross-regime comparison on family_integrity and coupled metrics."""
    print("\n" + "=" * 84)
    print("FAMILY-POLICY REGIME COMPARISON — FINAL-YEAR (2125) METRIC MEANS")
    print("=" * 84)
    header = (f"{'System':<22}{'hostile:FI':>11}{'neutral:FI':>12}{'integr:FI':>11}"
              f"{'hostile:demo':>14}{'neutral:demo':>14}")
    print(header)
    print("-" * 84)
    for gov in GOVERNANCE_SYSTEMS:
        h = regime_summaries.get("family_hostile", {}).get(gov, {})
        n = regime_summaries.get("family_neutral", {}).get(gov, {})
        i = regime_summaries.get("family_integrative", {}).get(gov, {})
        fi = lambda d, k: d.get(k, float("nan"))
        print(f"{gov:<22}"
              f"{fi(h, FAMILY_METRIC):>11.3f}"
              f"{fi(n, FAMILY_METRIC):>12.3f}"
              f"{fi(i, FAMILY_METRIC):>11.3f}"
              f"{fi(h, 'demography'):>14.3f}"
              f"{fi(n, 'demography'):>14.3f}")
    print("=" * 84)
    print("Reading: FI = family_integrity (DP-FS-10 suite). demo = demography.")
    print("Under family_hostile, weak-lock systems collapse and face demand-side")
    print("reversal (kibbutz/Soviet pattern); Algorapolis holds the constitutional")
    print("floor (DP-FS-1..4) and recovers. Under family_integrative, floors lift FI")
    print("everywhere; Algorapolis leads (full DP-FS stack). See paper 07 Section 3.")


# ============================================================
# OUTPUT + MAIN
# ============================================================
def main():
    parser = argparse.ArgumentParser(description="Algorapolis Simulation V5 (family extension)")
    parser.add_argument("--runs", type=int, default=MONTE_CARLO_RUNS)
    parser.add_argument("--regimes", nargs="*", default=list(FAMILY_REGIMES.keys()))
    args = parser.parse_args()

    out_dir = os.path.dirname(os.path.abspath(__file__))
    regime_summaries = {}
    for regime in args.regimes:
        if regime not in FAMILY_REGIMES:
            print(f"Unknown regime: {regime}; skipping.")
            continue
        bundle = run_monte_carlo_v5(regime, args.runs)

        with open(os.path.join(out_dir, f"simulation_results_family_{regime}.json"), "w") as f:
            json.dump(bundle["representative"], f, indent=2)
        with open(os.path.join(out_dir, f"monte_carlo_stats_family_{regime}.json"), "w") as f:
            json.dump(bundle["mc_stats"], f, indent=2)
        with open(os.path.join(out_dir, f"phase_analysis_family_{regime}.json"), "w") as f:
            json.dump(bundle["phase_analysis"], f, indent=2)

        regime_summaries[regime] = summarize_regime(bundle)

    print_family_comparison(regime_summaries)

    comparison = {
        "description": ("Family-policy regime comparison (V5). FI = family_integrity, "
                        "16th metric per DP-FS-10; regime definitions and document "
                        "grounding in simulation_engine_v5_family.py header."),
        "regimes_run": list(regime_summaries.keys()),
        "monte_carlo_runs": args.runs,
        "final_year_metric_means": regime_summaries,
    }
    with open(os.path.join(out_dir, "family_regime_comparison.json"), "w") as f:
        json.dump(comparison, f, indent=2)
    print(f"\nOutputs written to {out_dir}:")
    print("  simulation_results_family_<regime>.json (representative runs)")
    print("  monte_carlo_stats_family_<regime>.json")
    print("  phase_analysis_family_<regime>.json")
    print("  family_regime_comparison.json (cross-regime summary)")


if __name__ == "__main__":
    main()
