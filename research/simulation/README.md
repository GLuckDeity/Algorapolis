# Civilization Simulation Engine (V4)

> **Civilization Architecture Comparison and Validation** — A quantitative 100-year stress test comparing 10 governance systems across 15 metrics under 17 shock types.

This directory contains the civilization simulation engine, datasets, pre-rendered charts, and the final PDF report validating the **Algorapolis** framework. The simulation model demonstrates that a modular, document-grounded algorithmic governance system outperforms traditional systems in prosperity, equity, and shock resilience.

---

## Directory Structure

```
research/simulation/
├── README.md                          ← You are here
├── simulation_engine_v4.py            ← Runs 100-year, 10-village Monte Carlo simulation
├── visualization_engine_v4.py         ← Generates 28 publication-quality charts
├── generate_report_v4.py              ← Builds the 33-page ReportLab PDF report
├── Algorapolis_Simulation_Report_V4.pdf← Completed pre-rendered PDF report
├── simulation_results.json            ← Raw time series for representative run
├── monte_carlo_stats.json             ← Consolidated stats across 50 MC runs
├── pairwise_comparisons.json          ← Win/loss matrices (Algorapolis vs others)
├── phase_analysis.json                ← Metric means split by early/mid/late phases
├── shock_log.json                     ← Log of all scheduled and randomized shocks
└── charts/                            ← 28 pre-rendered charts (01 to 28)
```

---

## Simulation Architecture

The simulation operates as a discrete-time, agent-based model with annual steps running for **100 years (2026–2125)** across **10 independent villages per system (100 villages total)** over **50 Monte Carlo runs (seeds 42–91)**.

### 1. 10 Governance Systems Compared
* **Capitalism:** High growth/innovation, but low equity, stability, and resilience.
* **Socialism:** Balanced equity, but moderate growth and lower innovation.
* **Communism:** Central planning; high theoretical equity, but poor practical outcomes.
* **Democracy:** Representative governance; balanced but vulnerable to lobbying/capture.
* **Algorapolis:** Modular algorithmic governance (SLE + NDT + Civilizational Immune System).
* **Corporatocracy:** High growth, but extreme inequality and low stability.
* **Ecocracy:** Ecology-first; high sustainability, but slow growth.
* **Technocracy:** Expert-driven; high innovation, but lacks democratic input.
* **Anarcho-Syndicalism:** Worker-managed; high equity, but coordination bottlenecks.
* **Network State:** Digital-native; high innovation, but vulnerable to external shocks.

### 2. 15 Civilization Metrics
The system tracks civilizational development across 15 dimensions:
`prosperity`, `demography`, `social_classes`, `equity`, `media_and_information`, `security`, `infrastructure`, `resources`, `agriculture`, `wildlife_and_ecology`, `monetary_system`, `technology`, `sustainability`, `freedom`, and `resilience`.

---

## Mathematical Models & Document-Grounded Multipliers

Algorapolis outperforms other systems due to seven specific mechanisms derived directly from the framework document:
1. **SLE Optimization (§158, §3653):** Continuous multi-objective optimization (+0.5% annual bonus across all metrics). Minimum Viable Architecture (MVA) eliminates initial setup costs.
2. **Grey Scale Pareto (§388-390, §2836):** Optimizes for the Pareto frontier (no metric is sacrificed for another). Enforces a metric floor (0.30) and grants a balance bonus (+0.3%) when metrics are aligned.
3. **90/10 Principle (§1209):** 90% decentralized local execution and 10% strategic coordination, yielding a 1.15x innovation multiplier and 2x faster shock recovery speed.
4. **Civilizational Immune System (§1217, §1497-1503):** 15% shock detection bonus and 1.5x recovery acceleration through multi-temporal feedback loops.
5. **Anti-Corruption Revenue (§1648-1650):** Anti-corruption releases TZS 4.9 trillion in resources, granting a +2% annual bonus to the `monetary_system` and +1% to `equity`.
6. **Dual-Track Growth (§4087):** Parallel traditional and algorithmic paths (Shenzhen model) yield a 1.25x prosperity growth multiplier and +0.8% annual infrastructure bonus.
7. **NDT Transparency (§3653):** Real-time National Digital Twin transparency eliminates information asymmetry (+1% media, +0.8% freedom, +0.5% security annual bonuses).

---

## Robustness Extensions

This repository integrates three key behavioral extensions to ensure the simulation models a complex, state-dependent political economy:

### 1. Dynamic Legitimacy & Restoration Protocols
In alignment with [Study 17 (Requirement 4)](file:///d:/GitHub/Algorapolis/research/studies/17-simulation-findings.md#L806-L840), the simulation tracks a four-dimensional legitimacy index:
* **Procedural Legitimacy** = average(`freedom`, `security`, `resilience`) [threshold: 0.70]
* **Distributive Legitimacy** = average(`equity`, `social_classes`, `prosperity`) [threshold: 0.65]
* **Ownership Legitimacy** = average(`freedom`, `monetary_system`, `infrastructure`) [threshold: 0.60]
* **Narrative Legitimacy** = average(`media_and_information`, `freedom`, `sustainability`) [threshold: 0.55]

If any of these dimensions or the composite Legitimacy Index falls below its threshold, the system initiates a **5-year Legitimacy Restoration Protocol**, redirecting computational and administrative resources to boost lagging metrics.

### 2. State-Dependent Shock Mitigation
Rather than relying on a flat resistance rating, a village's current metrics actively modulate shock severity:
* High `infrastructure` dampens `earthquake` and `flood` impacts.
* High `equity` dampens `revolution` and `corruption_scandal` impacts.
* High `monetary_system` dampens `financial_crash` and `economic_crisis` impacts.
* High `sustainability` dampens `climate_catastrophe` and `resource_depletion` impacts.

### 3. Direct Population Shock Losses
Models demographic attrition (casualties, displacement, and mortality) during catastrophic events, preventing population growth from remaining unchecked during crises:
* `war` active: `2% to 8%` annual population loss.
* `pandemic` active: `1% to 5%` annual population loss.
* `famine` active: `1% to 4%` annual population loss.
* `climate_catastrophe` / `earthquake` active: `0.5% to 2%` annual population loss.

---

## Local Setup & Run Instructions

To run the simulation suite locally, install the required python packages:
```bash
pip install numpy matplotlib reportlab
```

### Execution Pipeline

1. **Run the Simulation Engine:**
   Generates the raw Monte Carlo results and logs them as JSON files in the current folder.
   ```bash
   python simulation_engine_v4.py
   ```

2. **Generate Visualizations:**
   Reads the JSON outputs and saves 28 high-resolution charts in the `charts/` subdirectory.
   ```bash
   python visualization_engine_v4.py
   ```

3. **Generate the PDF Report:**
   Assembles the charts and logs into a publication-ready 33-page PDF report.
   ```bash
   python generate_report_v4.py
   ```
