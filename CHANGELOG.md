# Changelog

All notable changes to the Algorapolis civilization architecture framework will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html) — adapted for civilization architecture (see note below).

---

## [Unreleased]

- Priority Gap Research Part VIII: Productive Capacity and Industrial Sovereignty (`research/priority-gaps/08-productive-capacity-industrial-sovereignty-priority-gap-research.md`), establishing the two-failure-mode architecture for the physical production function — the Globalist Efficiency Trap (cost-optimized sourcing → capacity atrophy → adversary dependency) and the Autarky/Leverage Trap (rent-seeking capture and coercive leverage) — and specifying the Strategic Sufficiency without Adversarial Dominance doctrine:
  - Part XXIII (Productive Capacity and Industrial Sovereignty) specification with 12 Design Principles (`DP-PC-1` through `DP-PC-12`): Critical Goods Sovereignty Baseline (two-register criticality machinery), Strategic Sufficiency Threshold (adversary-graded 65/40/25 caps, 10/40/25 stage floors, 30/60/90-day buffers), Adversarial Dependency Prohibition (production-function measurement), Sourcing Modality-Matching (cheapest-first five-rung intervention ladder), Arsenal Continuity & Surge Capacity (runway metric, conversion architecture), Skills Substrate Mandate, Mineral & Processing Depth, Energy Sufficiency Anti-Dominance (no-dominance mirror cap, coercion-provenance voidability, audited reserves), Protectionist Capture Guard (eight-point anti-capture circuitry + Amsden reciprocity), Multi-Administration Continuity Lock (ramp-slippage-calibrated persistence), Just-in-Case Reserve Architecture, Blockade Graceful Degradation (provenance classes).
  - Registration of the orphaned Study 16 Economic Sovereignty series (`DP-ESG-1` through `DP-ESG-7` — Supply Chain Resilience, Chokepoint Diversification, Developmental State Capabilities, Mineral Geopolitics Preparedness, Monetary Multipolarity, Adaptive Trade Architecture, Geopolitical Positioning): drafted in the Civilizational Research Agenda but previously absent from the registry, architecture, schema, and simulation; registered upgraded with adversary-graded caps, anti-capture circuitry, and the no-dominance mirror cap.
  - Three new case studies (`research/case-studies/`): Case Study 10 — US Deindustrialization & China Dependency (negative specification of the efficiency trap: the munitions runway ratio ≈ 0.01 discovered at wargame-time, not on any dashboard); Case Study 11 — China Industrial Overmatch and the NABEP Energy-Dominance Mirror (adversary dual specification: overmatch-and-its-costs plus the live failure-mode-2 specimen); Case Study 12 — WWII Arsenal Mobilization (positive specification: conversion architecture as the mechanism, the ~40%-of-GNP conversion ceiling as the sufficiency calibration datum).
  - Education-to-Production Pipeline deeper research (`research/studies/deeper-research/12-education-production-pipeline-deeper-research.md`) with 6 Design Principles (`DP-EP-1` through `DP-EP-6`): Occupational Standards as Versioned Law, Funding-Follows-Verified-Placements, Pipeline Latency Planning Mandate, Retraining Guarantee Bundle, Credential Materiality Rule, Distributional Stress-Test — binding the education substrate (EDU-13/16/17) to capacity planning and closing the education-to-production gap in both directions.
  - Civilization Simulation V6 industrial extension (`research/simulation/simulation_engine_v6_industrial.py`): `industrial_capacity` as the 17th metric, the `adversary_dependency` state variable (the trap accumulator), three trade-regime comparisons (globalist_efficiency / autarkic_dominance / strategic_sufficiency), five industrial shock types (trade embargo, sanctions regime, supply-chain weaponization, reindustrialization response, tech attrition tail), Algorapolis DP-PC mechanisms, and empirically grounded interaction logic (war amplified and prolonged below the 0.55 industrial-capacity constraint per the CSIS depletion finding; sanctions adaptation halving after year two per the Russia 2022 path; leverage decay per the weaponization-boomerang law). V4 and V5 baselines unchanged.
  - Appended 25 new Design Principles to the master registry (`06-design-principles-registry.md`) bringing the total from 177 to 202; updated master cross-reference CSV (`docs/design-principles-cross-reference.csv`).
  - Updated SLE/NDT Module Specifications (`07-sle-ndt-module-specifications.md`) with the Productive Capacity Specifications section (Composite Criticality Index engine, Adversary-Dependency Ledger, Intervention Ladder Solver, Industrial Capacity Dashboard, Runway Monitor, provenance-class firewall).
  - Updated core manifesto (`manifesto/01-CORE-PRINCIPLES.md` modality table Productive Capacity row + Part XXIII pointer; `manifesto/02-SOVEREIGN-LOGIC-ENGINE.md` Industrial Sovereignty Mandate as the fifteenth binding administrative rule), technical blueprint (`framework/ARCHITECTURE.md` Layer 4 Productive Capacity module + Module Interaction Map rows), civilization-stack schema (`schema/civilization-stack.json` `industrial_capacity` domain, trade-regime lock, provenance-class constraints), and the two framework telemetry specifications (`framework/ECONOMIC-TELEMETRY.md` industrial-sovereignty stock-telemetry feeds; `framework/INFRASTRUCTURE-AWARENESS.md` strategic capacity awareness layer).
- Priority Gap Research Part VII: Family and Social Fabric (`research/priority-gaps/07-family-social-fabric-priority-gap-research.md`), extending the Six Human-Reserved Domains protection from definition/classification locks to the full four-vector functional lock series (provision monopolization, institutional default, threshold creep, ideological custody transfer) against both collectivization and weaponization failure modes:
  - Part XXII (Family and Social Fabric) specification with 12 Design Principles (`DP-FS-1` through `DP-FS-12`): Parental Primacy, Material Floor Without Custody Transfer, Formalized Intervention Threshold, Ideological Neutrality Lock, Least Coercive Means Cascade (six-tier override architecture), Provision Pluralism, Alloparental Infrastructure, Family Privacy Boundary, Values Transmission Neutrality, Family Integrity Index, Family-Policy Capture Guard, Reversibility and Pilot Dissolution.
  - Three new case studies (`research/case-studies/`): Case Study 07 — Kibbutz Communal Child-Rearing (voluntary-pathway negative specification: 59% vs 65–70% secure attachment, communal sleeping abandoned by the 1990s); Case Study 08 — Soviet De-Familization 1918–1936 (state-pathway negative specification: the family is not a state-adjustable variable, in either direction); Case Study 09 — Norway CPS Best-Interests (threshold-capture negative specification: even a best-faith state cannot administer an indeterminate intervention standard; *Strand Lobben v. Norway* line).
  - Education, Values Transmission and Ideological Curriculum Capture deeper research (`research/studies/deeper-research/11-education-values-transmission-deeper-research.md`) with 6 Design Principles (`DP-EV-1` through `DP-EV-6`): Curriculum Firewall, Curriculum Capture Monitor, Educational Provision Pluralism, Homeschooling Regulation Floor, Educator Neutrality Scope, Educational Materials Provenance.
  - Civilization Simulation V5 family extension (`research/simulation/simulation_engine_v5_family.py`): `family_integrity` as the 16th metric (DP-FS-10), three family-policy regime comparisons (family_hostile / family_neutral / family_integrative), five family-specific shock types, Algorapolis DP-FS mechanisms (Family Sovereignty Locks, FII monitoring, Capture Guard), and demand-side reversal dynamics replicating the kibbutz/Soviet evidence. V4 baseline unchanged.
  - Appended 18 new Design Principles to the master registry (`06-design-principles-registry.md`) bringing the total from 159 to 177; updated master cross-reference CSV (`docs/design-principles-cross-reference.csv`).
  - Updated SLE/NDT Module Specifications (`07-sle-ndt-module-specifications.md`) with the Family and Social Fabric and Education Values Transmission module sections (Intervention Threshold Solver, FII Dashboard, Provision Pluralism Engine, Family Privacy Boundary, Capture Guard, Curriculum Firewall).
  - Updated core manifesto (`manifesto/01-CORE-PRINCIPLES.md` modality table Family & Social Fabric row + Part XXII pointer; `manifesto/02-SOVEREIGN-LOGIC-ENGINE.md` Family Sovereignty Mandate as the fourteenth binding administrative rule), technical blueprint (`framework/ARCHITECTURE.md` Layer 9 Family and Social Fabric module + Module Interaction Map rows), and civilization-stack schema (`schema/civilization-stack.json` Layer 9 description, `family_child_welfare` civic domain, extended `family_structure` enforcement mechanisms).
- Civilization Simulation V4 suite integrated under `research/simulation/`:
  - Python engines `simulation_engine_v4.py` (extended with dynamic legitimacy feedback loops, dynamic shock mitigation, and direct population casualties), `visualization_engine_v4.py` (with Windows-portable font fallbacks), and `generate_report_v4.py`.
  - Raw time series and statistical datasets (`simulation_results.json`, `monte_carlo_stats.json`, `pairwise_comparisons.json`, `phase_analysis.json`, `shock_log.json`).
  - Pre-rendered 33-page ReportLab PDF report `Algorapolis_Simulation_Report_V4.pdf` and 28 high-resolution PNG charts in `charts/` subdirectory.
  - Comprehensive index and manual `README.md` explaining the mathematical model and code setup.
- Deeper Research integration of three academic papers:
  - Part VIII: Institutional Trust & Legitimacy (Trust decay mechanics, legitimacy lifecycles, and sortition-based restoration) with 7 Design Principles (`TD-1` through `TD-7`).
  - Part IX: Information Warfare & Narrative Defense (C2PA content credentials, asymmetric defense, and public curation) with 12 Design Principles (`IW-1` through `IW-12`).
  - Part X: Economic Architecture V2 (Chicago Plan reserve banking, federated cooperative networks, and transition gradualism) with 24 Design Principles (`EA-1` through `EA-24`).
- Appended 43 new Design Principles to the master registry (`06-design-principles-registry.md`) bringing the total to 159.
- Updated master cross-reference CSV (`docs/design-principles-cross-reference.csv`) with the 43 new principles.
- Updated SLE/NDT Module Specifications (`07-sle-ndt-module-specifications.md`) with the new specifications.
- Updated core manifesto (`manifesto/01-CORE-PRINCIPLES.md`, `manifesto/02-SOVEREIGN-LOGIC-ENGINE.md`) and technical blueprints (`framework/DIGITAL-TWIN.md`, `framework/ARCHITECTURE.md`) with integrations for the 3 new research areas.
- Updated primary document [Algorapolis.docx](file:///d:/GitHub/Algorapolis/docs/Algorapolis.docx) and expanded visual assets in [assets/](file:///d:/GitHub/Algorapolis/assets/) to incorporate recent architecture revisions and design diagrams.

- Priority Gaps Research child collection under `research/priority-gaps/` authored by Goodluck Japhet Macha:
  - Part I: Information Sovereignty (7-layer information stack, digital self-determination, cognitive security) with 12 Design Principles (`DP-IS-1` through `DP-IS-12`).
  - Part II: Monetary Systems (CBDC design, complementary currencies, Sovereign Wealth Funds, monetary discipline) with 12 Design Principles (`DP-MS-1` through `DP-MS-12`).
  - Part III: Species Preservation (Rights of Nature, insect collapse, marine governance, conservation economics) with 12 Design Principles (`DP-SP-1` through `DP-SP-12`).
  - Part IV: Intelligence & Security (Democratic oversight, mass surveillance limits, dual-use technology, autonomous weapons) with 12 Design Principles (`DP-ISec-1` through `DP-ISec-12`).
  - Part V: Wealth Transfer (Intergenerational wealth caps, Piketty's r > g, progressive wealth tax, capital stakes) with 12 Design Principles (`DP-WT-1` through `DP-WT-12`).
  - Part VI: GitHub Integration Guide (repository integration specification).
- Appended 60 new Design Principles to the master Design Principles Registry (`06-design-principles-registry.md`).
- Appended functional specifications for the 5 priority gap domains to the consolidated SLE/NDT Module Specifications (`07-sle-ndt-module-specifications.md`).
- Updated master cross-reference CSV (`docs/design-principles-cross-reference.csv`) with the 60 new priority gap principles.
- Updated core manifesto files (`manifesto/01-CORE-PRINCIPLES.md` and `manifesto/02-SOVEREIGN-LOGIC-ENGINE.md`) and technical blueprints (`framework/ARCHITECTURE.md` and `framework/DIGITAL-TWIN.md`) with priority-gap integrations.
- Study 18: Civilizational Immunity & Capture Resilience
- Study 19: Ecological Optimization: Volume I
- Study 20: Innovation Zones and Experimental Regions
- Simulation Findings Deeper Research child collection under `research/studies/deeper-research/` (including Parts I–V, a Design Principles Registry, and SLE/NDT Module Specifications).
- Design Principles Registry (`06-design-principles-registry.md` & `docs/design-principles-cross-reference.csv`) compiling and mapping 56 new design principles.
- Consolidated SLE/NDT Module Specifications (`07-sle-ndt-module-specifications.md`).
- Study 14: Enclave Formation, Human Infrastructure, and Civilizational Cohesion
- Study 15: Legal Pluralism, Food Sovereignty, and Multi-Temporal Governance
- Study 16: Civilizational Research Agenda — Comprehensive Domain Analysis
- Study 17: Simulation Findings — Institutional Trust, Governance Proximity, and the Political Economy of Computational Civilization
- New case study proposals: Konza, Niger Delta, NEOM, Shenzhen, Dubai, Singapore, Ujamaa, Tanzania legal pluralism, South Africa RCMA, Bolivia plurinational state, Brazil Zero Hunger, India e-NAM, Wales Future Generations Act, Hungary ombudsman downgrading, Japan Future Design, Netherlands Delta Programme, Porto Alegre participatory budgeting, Iceland crowdsourced constitution, Los Angeles neighborhood councils, South African ward committees
- Anti-Enclave Framework proposal with five constitutional layers
- Human Infrastructure Index (HII) and Civilizational Cohesion Index (CCI) proposals
- Computable Legal Pluralism framework with defeasible + paraconsistent logic structures
- Food Sovereignty Layer with 7 constitutional guardrails and 6-tier human override architecture
- Multi-Temporal Governance framework with 5 pace layers and temporal firewalls
- Temporal Rights Charter (6 future generations rights + 5 rights to slowness) and Future Generations Protocol
- 7-Layer Information Sovereignty Stack specification
- 17 critical domains analyzed with 82 new design principles for civilizational infrastructure
- Political Economy Encoding framework (Ownership Taxonomy, Inequality Boundaries, Algorithmic Transparency, and 4D Legitimacy System)
- 14 simulation domains analyzed with 88 new design principles for institutional trust and proximity
- Master bibliography expanded with 70+ new high-quality academic references

---

## [0.1.0] - 2026-05-30

### Added

- Complete specification document (Parts I–XIII, Sections 1–77)
- Ten-layer civilization stack architecture (6 Core + 4 Extended): Philosophy, Psychology, Governance, Economics, Technology, Security, Culture, Ecology, Civilization, Ark
- Sovereign Logic Engine (SLE) design with five distinguishing properties (Objective, Utility, Narrow, Constrained, Auditable) and constitutional constraints
- National Digital Twin specification with federated architecture and real-time data integration
- Governance Sandbox architecture for policy simulation before deployment
- Emotional Intelligence Architecture (Sections 67–77): empathetic governance framework, the Balance Principle, the Cold State diagnostic, and the Empathy Shield
- Privacy Sovereignty framework: zero-knowledge proof tier system (Groth16/PLONK/Halo 2), differential privacy, homomorphic encryption, and the Tribalism Neutralizer
- African and Tanzanian context integrated throughout — born from East African governance observation, designed for Global South leapfrog deployment
- Adversarial resilience patches (Part XI, Sections 38–51): Human Sovereignty Doctrine, Bounded Formalism, Contested Formalization Protocol, Graceful Degradation, Incentive-Compatible Transition, Democratic Legitimacy, Political Economy Realism, Comparative Governance Positioning, Explainability and Cognitive Sovereignty, Civilizational Humility
- Tanzania pilot specification (Section 46) with five-year roadmap, quantified metrics, and automatic rollback criteria
- Transition Architecture Theory (Section 37): Gradual Civilizational Migration Model, resistance modeling, legal migration frameworks, economic bootstrap models, and rollback scenarios
- Governance Meta-Architecture: Module Map with twelve civic domains and domain-specific governance modality matching
- Viable System Model (VSM) integration mapping Beer's five subsystems to Algorapolis architecture
- Law as Code: machine-readable constitutions (Akoma Ntoso), Legal Verification Pipeline (Lean 4 → Model Checking → Adversarial Testing)
- Four-Layer Operational Architecture: Foundational Infrastructure, Reasoning and Simulation, Testing and Validation, Operational Coordination
- Four Constitutional Guardrails: No omniscience, No total behavioral prediction, No centralized social engineering, No unrestricted computational control
- Six Human-Reserved Domains: Religion and Spirituality, Culture and Identity, Family Structure, Moral Interpretation, Artistic Expression, Personal Identity
- Human Experience Review Board (HERB) specification
- Open-source repository with manifesto directory (7 documents), framework directory (13 documents), and research directory (6 case studies, 13 research studies, bibliography)
- Case studies: Estonia Digital Nation, Singapore Smart Nation, Taiwan Civic Tech, China Social Credit System, Dutch Childcare Benefits Scandal, Tanzania Election 2025
- Research studies covering: civilizational collapse, sovereign logic engine design, emotional intelligence governance, privacy mathematics, African governance context, digital twin nation, governance sandbox theory, offline resilience, economic telemetry methods, predictive governance ethics, cultural preservation computation, transition architecture, and anti-capture mechanisms

---

## Versioning Note

Algorapolis uses semantic versioning adapted for civilization architecture:

- **Major version (X.0.0)**: Fundamental architectural changes — a new layer, a revised constitutional constraint, or a change to the SLE's authority model. These are civilizational-scale shifts that require democratic authorization and cannot be deployed without HERB review.
- **Minor version (0.X.0)**: Significant capability additions — a new governance module, a new privacy protocol, or an expanded pilot deployment. These are structural enhancements that require formal verification and adversarial testing but do not alter constitutional foundations.
- **Patch version (0.0.X)**: Refinements, clarifications, and corrections — documentation improvements, bug fixes in the specification, or minor adjustments to implementation details. These improve fidelity without altering architecture.

Version 0.1.0 represents the initial specification release — a complete architectural framework that has not yet undergone external formal verification or real-world deployment. The transition to version 1.0.0 will mark the completion of Phase 1 (Foundation): formal verification of constitutional constraints, SLE prototype passing adversarial testing, and Tanzania pilot MOU signed.

---

[Unreleased]: https://github.com/goodluckmacha/algorapolis/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/goodluckmacha/algorapolis/releases/tag/v0.1.0
