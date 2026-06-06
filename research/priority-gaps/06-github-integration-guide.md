# GITHUB INTEGRATION GUIDE: ALGORAPOLIS PRIORITY GAP RESEARCH

**Author:** Goodluck Japhet Macha
**Affiliation:** Independent Researcher, Tanzania
**Date:** June 2026
**Status:** Integration Specification — For Repository Maintainer
**License:** CC-BY-SA 4.0 (content) / MIT (code)
**Related Documents:**
- Algorapolis Core Framework (primary)
- Design Principles Registry (deeper-research/06)
- SLE/NDT Module Specifications (deeper-research/07)
- Priority Gap Research (Parts I–V)

**Document ID:** ALG-PRI-2026-006

---

## 1. Overview

### 1.1 What This Research Covers

The Algorapolis Priority Gap Research identifies five domains that the core Algorapolis.docx (currently at Part XVI) covers with either **zero substantive treatment** or only brief outlines insufficient for engineering specification. Across 33,585 words of publication-grade research, these five domains establish 60 new Design Principles (DPs) — up from the originally estimated 58 upon closer enumeration; Intelligence & Security contains 12 DPs, not the initially projected ~10 — for integration into the Sovereign Logic Engine (SLE) and National Digital Twin (NDT) specification.

The five domains are:

| # | Domain | Words | DPs | Core Gap Severity |
|---|--------|-------|-----|-------------------|
| I | Information Sovereignty | 8,498 | 12 (IS-1 to IS-12) | **Zero coverage** in core docx; Civilizational Agenda had brief 7-layer outline only |
| II | Monetary Systems | 6,189 | 12 (MS-1 to MS-12) | Section 51.1 exists but at outline depth; CBDC/complementary currency/species-ecology gap unfilled |
| III | Species Preservation | 8,154 | 12 (SP-1 to SP-12) | Section 22 + existing species ecology research (12,620 words) provide foundation; Rights of Nature, insect collapse, marine governance, conservation economics are gaps |
| IV | Intelligence & Security | 6,603 | 12 (ISec-1 to ISec-12) | Sections 14–15 cover operational layer; democratic oversight gap is untreated |
| V | Wealth Transfer | 4,141 | 12 (WT-1 to WT-12) | Simulation Findings Part IX identifies r>g; zero countermeasures encoded |

### 1.2 Why These Gaps Are Critical

These are not "nice to have" additions. Each represents a **structural absence** in the civilizational architecture:

- **Information Sovereignty** is the precondition for every other domain's integrity. If the information environment is compromised, monetary policy, democratic deliberation, and civilizational immunity are all compromised with it. The core framework has zero coverage.
- **Monetary Systems** are the metabolic substrate of civilization. The SLE cannot govern resource allocation without monetary architecture, and the existing Section 51.1 outline lacks the specification depth for CBDC design, complementary currency tiers, or systemic risk prevention.
- **Species Preservation** addresses the biospheric foundation upon which all civilization depends. The existing ecology research covers extinction metrics and conservation biology but omits the legal personhood revolution, insect collapse, marine governance, and conservation financing architecture.
- **Intelligence & Security** contains the democratic gap — the absence of which makes the SLE a surveillance apparatus waiting for a captor. Operational capabilities without democratic accountability constitute an existential risk.
- **Wealth Transfer** determines whether computational governance serves all citizens or becomes the instrument of a hereditary capital class. Piketty's r > g dynamic is a structural engine, not a market failure, and requires structural countermeasures.

---

## 2. File Structure

### 2.1 Recommended GitHub Paths

The priority gap research files should be placed alongside existing research directories in the Algorapolis repository. The recommended structure creates a new `priority-gaps/` directory under `/research/` to distinguish these gap-fill documents from the existing deeper-research and simulation-findings materials.

```
/research/
├── simulation-findings/                          # EXISTING
│   └── deeper-research/                          # EXISTING (4 domains)
├── immunity/                                     # EXISTING
├── civilizational-agenda/                        # EXISTING (had brief outlines of these 5 domains)
├── species-ecology/                              # EXISTING (12,620 words)
├── priority-gaps/                                # NEW DIRECTORY
│   ├── 01-information-sovereignty-priority-gap-research.md
│   ├── 02-monetary-systems-priority-gap-research.md
│   ├── 03-species-preservation-priority-gap-research.md
│   ├── 04-intelligence-security-democratic-gap-research.md
│   ├── 05-wealth-transfer-generational-wealth-priority-gap-research.md
│   ├── 06-github-integration-guide.md            # THIS FILE
│   └── README.md                                 # Index file for the directory
```

### 2.2 Naming Convention

All files follow the pattern: `NN-domain-keywords-priority-gap-research.md`

- `NN` = Two-digit sequence number (01–06)
- `domain-keywords` = Kebab-case domain descriptor
- `priority-gap-research` = Consistent suffix identifying these as gap-fill documents

### 2.3 Integration with Existing Directories

| Existing Path | Relationship to Priority Gap Research |
|---|---|
| `/research/civilizational-agenda/` | The agenda document contained brief outlines of all 5 domains. The priority gap research **supersedes** those outlines with specification-grade content. The agenda's outlines should be annotated with cross-references to the corresponding priority gap files. |
| `/research/species-ecology/` | The existing 12,620-word species ecology research is **foundational** to Part III (Species Preservation). Part III explicitly builds on and extends that research, filling the gaps it identified. The two documents are complementary, not redundant. |
| `/research/simulation-findings/` | Simulation Findings Part IX identified the r>g structural inequality engine. Part V (Wealth Transfer) encodes the countermeasures that the simulation identified as necessary. Cross-reference bidirectional. |
| `/research/simulation-findings/deeper-research/` | The 4-domain deeper research (Cyber-Civilization Resilience, etc.) is parallel to but distinct from the 5-domain priority gap research. Both fill gaps, but the priority gap research addresses domains with zero coverage, while the deeper research extends domains with partial coverage. |
| `/research/immunity/` | The Civilizational Immunity Protocol (Part XVI of the docx) is cross-referenced by multiple priority gap DPs. The immunity research's Ideological Entropy Index and capture detection algorithms should be integrated with IS-12 (Institutional Health Monitoring) and ISec-1 (Architectural Privacy Enforcement). |

---

## 3. Cross-Reference Mapping

### 3.1 Part I: Information Sovereignty

| Dimension | Mapping |
|---|---|
| **Core sections filled** | Section 13 (Information Sovereignty) — currently zero coverage; this research **creates** the section's substantive content |
| **Existing research built on** | Civilizational Agenda brief 7-layer outline (functional labels); Civilizational Immunity Protocol (capture detection) |
| **Design principles to integrate** | IS-1 through IS-12 (see Section 5) |
| **SLE modules affected** | Data Sovereignty Protocol; Algorithmic Glass Box audit interfaces; Cross-Border Data Flow routing logic; Constitutional Drift Detector; Contestation Register |
| **NDT modules affected** | Physical Infrastructure Sovereignty Index; Data Infrastructure Health Monitor; Algorithmic Sovereignty Audit; Narrative Environment Monitor; Cultural Vitality Index; Sovereignty Equity Index; Layer Integrity Index |
| **Cross-references to other parts** | IS-12 (Institutional Health Monitoring) integrates with Civilizational Immune System; IS-2 (Data as Sovereign Territory) cross-references MS-2 (Privacy-by-Architecture); IS-4 (Cross-Border Data Flow) cross-references the Schrems analysis in ISec-11 (Cross-Jurisdictional Accountability); IS-3 (Algorithmic Glass Box) is the transparency complement to ISec-4 (Classification as Exception) |

### 3.2 Part II: Monetary Systems

| Dimension | Mapping |
|---|---|
| **Core sections filled** | Section 51.1 (Monetary Architecture) — currently outline depth; this research **expands** to specification grade with CBDC, complementary currencies, SWF, inflation governance, capital stakes, and systemic risk |
| **Existing research built on** | Section 51.1 four-layer architecture (Reserve, Settlement, Transaction, Constitutional); Simulation Findings macroeconomic models |
| **Design principles to integrate** | MS-1 through MS-12 (see Section 5) |
| **SLE modules affected** | Constitutional inflation band enforcement; Zero-knowledge proof monetary transaction layer; Complementary currency authorization and pegging logic; CSWF algorithmic withdrawal enforcement; Bail-in trigger logic; Fiscal-monetary coordination engine |
| **NDT modules affected** | Financial system interconnectedness models; Asset-liability mismatch detection; Shadow banking growth monitoring; Monetary infrastructure resilience monitoring; Complementary currency issuance tracking |
| **Cross-references to other parts** | MS-2 (Privacy-by-Architecture) operationalizes IS-2 (Data as Sovereign Territory) in the monetary domain; MS-4/MS-5 (CSWF) are the funding mechanism for WT-3/WT-4 (Constitutional Capital Stake); MS-7 (Constitutional Capital Stake) is shared with WT-3; MS-8 (Systemic Risk) complements the civilizational immunity framework; MS-10 (Fiscal-Monetary Coordination) is the NDT module that prevents the r>g dynamics addressed in WT-1 through WT-12 |

### 3.3 Part III: Species Preservation

| Dimension | Mapping |
|---|---|
| **Core sections filled** | Section 22 (Ecology) — existing coverage of extinction metrics and conservation biology; this research **extends** with Rights of Nature, insect collapse, 3-tier hierarchy, conservation economics, marine governance, and rewilding specification |
| **Existing research built on** | `/research/species-ecology/` (12,620 words): extinction metrics, seed banking, rewilding overview, international frameworks, philosophical obligations. Part III explicitly references and builds on this foundation. |
| **Design principles to integrate** | SP-1 through SP-12 (see Section 5) |
| **SLE modules affected** | Biodiversity Fiscal Engine; Ecological guardian agent framework; Constitutional Biodiversity Emergency Protocol; Marine Governance Layer; Insect Collapse Emergency triggers; Rewilding simulation authorization; Constitutional Biodiversity Floor enforcement |
| **NDT modules affected** | Ecological network models (trophic cascades, pollination networks); Genomic Preservation Dashboard; Connectivity modeling and corridor monitoring; Marine monitoring extension; Coral reef climate refugia identification; eDNA/bioacoustic sensor integration; Biodiversity Integrity Term computation |
| **Cross-references to other parts** | SP-2 (Biodiversity Fiscal Engine) is funded by the monetary architecture in MS-4 (CSWF); SP-9 (Constitutional Inheritance Doctrine) parallels the intergenerational logic of WT-1 (Transfer Cap); SP-1 (Legal Personhood) is a rights-framework analog to IS-2 (Data as Sovereign Territory); SP-12 (Ecological Monitoring as Constitutional Obligation) is a monitoring mandate paralleling IS-7 (Physical Infrastructure Sovereignty Index) |

### 3.4 Part IV: Intelligence & Security

| Dimension | Mapping |
|---|---|
| **Core sections filled** | Sections 14–15 (Intelligence and Security) — currently cover operational layer (how intelligence is conducted, how systems are defended); this research **fills the democratic gap** (how intelligence is held accountable) |
| **Existing research built on** | Existing DP-IS-1 through DP-IS-8; Zero-Knowledge Oversight principle; Dual-Key Authorization system; `/research/simulation-findings/deeper-research/` cyber-civilization resilience research |
| **Design principles to integrate** | ISec-1 through ISec-12 (see Section 5) |
| **SLE modules affected** | Architectural privacy enforcement (core logic constraints); Intelligence Oversight Tribunal certification interface; Dual-key cryptographic authorization; Classification management system; Whistleblower protection protocols; Dual-use technology classification protocol; Autonomous lethal force prohibition (hardcoded); Computational Civil Defense architecture; Emergency power sunset enforcement |
| **NDT modules affected** | Surveillance compliance monitoring; Classification gradient tracking; Digital continuity bunker inventory; Societal immune drill scheduling and results; Analog fallback readiness assessment |
| **Cross-references to other parts** | ISec-1 (Architectural Privacy Enforcement) is the enforcement layer for IS-2 (Data as Sovereign Territory) and MS-2 (Privacy-by-Architecture); ISec-4 (Classification as Exception) complements IS-3 (Algorithmic Glass Box); ISec-6 (Dual-Use Technology Assessment) parallels IS-3/IS-6 (Open-Source by Default) in governing technology deployment; ISec-8 (Computational Civil Defense) is the security dimension of civilizational immunity; ISec-11 (Cross-Jurisdictional Accountability) operationalizes IS-4 (Cross-Border Data Flow Sovereignty) |

### 3.5 Part V: Wealth Transfer

| Dimension | Mapping |
|---|---|
| **Core sections filled** | Simulation Findings Part IX (Structural Equality vs Algorithmic Equality) — identifies r>g as a structural inequality engine but encodes zero countermeasures; this research **encodes the countermeasures** |
| **Existing research built on** | Simulation Findings Part IX; Civilizational Research Agenda Part IV (brief outline); MS-4/MS-5/MS-7 (CSWF and Constitutional Capital Stake from Part II) |
| **Design principles to integrate** | WT-1 through WT-12 (see Section 5) |
| **SLE modules affected** | Intergenerational transfer cap enforcement; Progressive wealth tax assessment engine; Constitutional Capital Stake account management; Beneficial ownership verification; Exit tax collection; Great Compression encoding (progressive income tax, estate tax, labor protections); Wealth concentration limit enforcement; Secrecy jurisdiction sanctions; Automation rent capture; Pay ratio enforcement |
| **NDT modules affected** | Comprehensive wealth register; Real-time Wealth Inequality Dashboard (Gini, top shares, mobility elasticity, capital-labor shares); Asset valuation engine; Intergenerational mobility modeling; CSWF dividend distribution |
| **Cross-references to other parts** | WT-3/WT-4 (Constitutional Capital Stake / CSWF) are shared with MS-4/MS-5/MS-7 — the same institutional architecture; WT-5 (Beneficial Ownership) operationalizes IS-4 (Cross-Border Data Flow) for financial assets; WT-7 (Great Compression Encoding) provides the fiscal architecture that MS-10 (Fiscal-Monetary Coordination) models; WT-8 (Wealth Concentration Limit) is the structural countermeasure to r>g that the SLE's monetary governance (MS-1, MS-6) supports |

---

## 4. Integration Strategy

### 4.1 The Three Options

Three integration strategies are available for incorporating the priority gap research into Algorapolis.docx:

| Option | Description | Pros | Cons |
|---|---|---|---|
| **A: Append as New Parts** | Add Parts XVII–XXI to the docx, one per domain, after the current Part XVI | Clean separation; no disruption to existing structure; each domain gets full treatment; easy to reference | May feel disconnected from related existing sections; requires explicit cross-references to avoid siloing |
| **B: Integrate into Existing Sections** | Expand existing sections (13, 22, 51.1, 14–15) with gap-fill content | Organic integration; content lives where it's referenced; avoids document bloat at the end | These are GAPS (zero coverage), not extensions — cramming new major domains into existing sections misrepresents their scope; would unbalance existing sections; core docx sections become unwieldy |
| **C: Hybrid — Append with Bidirectional Links** | Add Parts XVII–XXI as in Option A, but also insert "gap-fill pointers" in existing sections that reference the new parts | Preserves clean structure of Option A; ensures discoverability from existing sections; existing sections gain awareness of related new content | Slightly more complex document management; requires maintaining bidirectional cross-references |

### 4.2 Recommendation: Option C (Hybrid)

**Justification:**

1. **These are gaps, not extensions.** Information Sovereignty has zero coverage in the core docx. Wealth Transfer has zero countermeasures. These require NEW sections, not additions to existing ones. Option B would create the false impression that these domains are sub-topics of existing sections, when they are co-equal architectural domains.

2. **Cross-referencing prevents siloing.** The primary risk of Option A is that the new parts become isolated from the existing framework. Option C mitigates this by inserting gap-fill pointers — brief paragraphs in existing sections that direct readers to the corresponding new Part. For example, Section 13 would gain a paragraph: "For the full specification of Information Sovereignty architecture, including the 7-Layer Stack, Data Governance, and Algorithmic Accountability, see Part XVII."

3. **SLE/NDT module coherence.** Many DPs span multiple domains (e.g., MS-2 Privacy-by-Architecture operationalizes IS-2 Data as Sovereign Territory). Option C's bidirectional links make these cross-domain dependencies visible without merging the domains.

4. **Incremental integration.** Option C allows the five new Parts to be added sequentially — one at a time, with testing and review — rather than requiring a single massive document restructuring.

### 4.3 Gap-Fill Pointer Template

For each existing section that gains a pointer to a new Part, use this template:

```markdown
### [Existing Section Title] — Priority Gap Extension

The foundational treatment of [topic] in this section is extended by specification-grade
research in Part [XVII–XXI]: [Domain Name]. That Part addresses the following gaps
identified in the core framework:

- [Gap 1 description]
- [Gap 2 description]
- [Gap 3 description]

[Count] new Design Principles ([DP-ID range]) are specified for SLE/NDT integration.
See Part [XVII–XXI] for full treatment.
```

### 4.4 Specific Gap-Fill Pointer Locations

| Existing Section | Pointer Target | Pointer Location |
|---|---|---|
| Section 13 (Information Sovereignty) | Part XVII (Information Sovereignty) | End of current Section 13 content |
| Section 51.1 (Monetary Architecture) | Part XVIII (Monetary Systems) | End of current Section 51.1 content |
| Section 22 (Ecology) | Part XIX (Species Preservation) | End of current Section 22 content |
| Sections 14–15 (Intelligence/Security) | Part XX (Intelligence & Security) | End of current Section 15 content |
| Simulation Findings Part IX | Part XXI (Wealth Transfer) | End of current Part IX content |

---

## 5. Design Principles Extraction

### 5.1 Complete Table of All 60 New Design Principles

> **Note:** The original scope estimated 58 DPs (~10 for Intelligence & Security). Actual enumeration reveals 12 DPs for that domain, yielding 60 total.

| Global ID | Original ID | Domain | Title | Recommended Integration Target |
|---|---|---|---|---|
| **IS-1** | DP-IS-1 | Information Sovereignty | Full-Stack Sovereignty Mandate | Part XVII §1 (7-Layer Stack) |
| **IS-2** | DP-IS-2 | Information Sovereignty | Data as Sovereign Territory | Part XVII §2 (Data Governance) |
| **IS-3** | DP-IS-3 | Information Sovereignty | Algorithmic Glass Box Standard | Part XVII §4 (Algorithmic Accountability) |
| **IS-4** | DP-IS-4 | Information Sovereignty | Cross-Border Data Flow Sovereignty | Part XVII §3 (Cross-Border Data Flows) |
| **IS-5** | DP-IS-5 | Information Sovereignty | Algorithmic Contestability Right | Part XVII §4 (Algorithmic Accountability) |
| **IS-6** | DP-IS-6 | Information Sovereignty | Open-Source by Default | Part XVII §5 (Open-Source Mandate) |
| **IS-7** | DP-IS-7 | Information Sovereignty | Physical Infrastructure Sovereignty Index | Part XVII §1 (7-Layer Stack, Layer 1) |
| **IS-8** | DP-IS-8 | Information Sovereignty | Narrative Environment Monitoring | Part XVII §1 (7-Layer Stack, Layer 4) |
| **IS-9** | DP-IS-9 | Information Sovereignty | Cultural Vitality Index | Part XVII §1 (7-Layer Stack, Layer 5) |
| **IS-10** | DP-IS-10 | Information Sovereignty | Sovereignty Equity Mandate | Part XVII §6 (Global South Dimensions) |
| **IS-11** | DP-IS-11 | Information Sovereignty | Constitutional Drift Detection | Part XVII §1 (7-Layer Stack, Layer 7) |
| **IS-12** | DP-IS-12 | Information Sovereignty | Institutional Health Monitoring | Part XVII §1 (7-Layer Stack, Layer 6) |
| **MS-1** | DP-M1 | Monetary Systems | Constitutional Currency Sovereignty | Part XVIII §1 (CBDC Design) |
| **MS-2** | DP-M2 | Monetary Systems | Privacy-by-Architecture for Monetary Transactions | Part XVIII §1 (CBDC Design) |
| **MS-3** | DP-M3 | Monetary Systems | Multi-Layer Currency Architecture | Part XVIII §2 (Complementary Currencies) |
| **MS-4** | DP-M4 | Monetary Systems | Civilizational Sovereign Wealth Fund (CSWF) | Part XVIII §3 (Sovereign Wealth Funds) |
| **MS-5** | DP-M5 | Monetary Systems | Anti-Capture Protection for Sovereign Wealth | Part XVIII §3 (Sovereign Wealth Funds) |
| **MS-6** | DP-M6 | Monetary Systems | Algorithmic Monetary Discipline | Part XVIII §4 (Inflation/Deflation Governance) |
| **MS-7** | DP-M7 | Monetary Systems | Constitutional Capital Stake (CCS) | Part XVIII §5 (Universal Basic Capital) |
| **MS-8** | DP-M8 | Monetary Systems | Systemic Risk Surveillance and Constitutional Limits | Part XVIII §6 (Financial Stability) |
| **MS-9** | DP-M9 | Monetary Systems | Bail-In by Design | Part XVIII §6 (Financial Stability) |
| **MS-10** | DP-M10 | Monetary Systems | Fiscal-Monetary Coordination via the NDT | Part XVIII §4 (Inflation/Deflation Governance) |
| **MS-11** | DP-M11 | Monetary Systems | Interoperable Complementary Currency Pegging | Part XVIII §2 (Complementary Currencies) |
| **MS-12** | DP-M12 | Monetary Systems | Monetary Infrastructure Resilience | Part XVIII §6 (Financial Stability) |
| **SP-1** | DP-SP1 | Species Preservation | Constitutional Legal Personhood for Ecosystems | Part XIX §1 (Rights of Nature) |
| **SP-2** | DP-SP2 | Species Preservation | Biodiversity Fiscal Engine | Part XIX §4 (Conservation Economics) |
| **SP-3** | DP-SP3 | Species Preservation | Three-Tier Preservation Hierarchy with Allocation Priority | Part XIX §3 (3-Tier Hierarchy) |
| **SP-4** | DP-SP4 | Species Preservation | Mandatory Connectivity Mandate | Part XIX §5 (Habitat Corridors/Rewilding) |
| **SP-5** | DP-SP5 | Species Preservation | Cascading Effects Modeling | Part XIX §2 (Sixth Mass Extinction) |
| **SP-6** | DP-SP6 | Species Preservation | Marine Governance Layer | Part XIX §6 (Marine Biodiversity) |
| **SP-7** | DP-SP7 | Species Preservation | Insect Collapse Emergency Protocol | Part XIX §2 (Sixth Mass Extinction) |
| **SP-8** | DP-SP8 | Species Preservation | Rewilding-by-Default with NDT Simulation | Part XIX §5 (Habitat Corridors/Rewilding) |
| **SP-9** | DP-SP9 | Species Preservation | Constitutional Inheritance Doctrine | Part XIX §3 (3-Tier Hierarchy) |
| **SP-10** | DP-SP10 | Species Preservation | Genomic Preservation Completeness Mandate | Part XIX §3 (3-Tier Hierarchy, Tier 3) |
| **SP-11** | DP-SP11 | Species Preservation | Coral Reef Climate Refugia Protection | Part XIX §6 (Marine Biodiversity) |
| **SP-12** | DP-SP12 | Species Preservation | Ecological Monitoring as Constitutional Obligation | Part XIX §2 (Sixth Mass Extinction, Monitoring) |
| **ISec-1** | DP-DG-1 | Intelligence & Security | Architectural Privacy Enforcement | Part XX §2 (Surveillance Limits) |
| **ISec-2** | DP-DG-2 | Intelligence & Security | Independent Intelligence Oversight Tribunal | Part XX §1 (Democratic Oversight) |
| **ISec-3** | DP-DG-3 | Intelligence & Security | Dual-Key Surveillance Authorization | Part XX §4 (Intelligence Accountability) |
| **ISec-4** | DP-DG-4 | Intelligence & Security | Classification as Exception | Part XX §4 (Intelligence Accountability) |
| **ISec-5** | DP-DG-5 | Intelligence & Security | Whistleblower Constitutional Protection | Part XX §4 (Intelligence Accountability) |
| **ISec-6** | DP-DG-6 | Intelligence & Security | Dual-Use Technology Assessment Mandate | Part XX §3 (Dual-Use Governance) |
| **ISec-7** | DP-DG-7 | Intelligence & Security | Autonomous Lethal Force Prohibition | Part XX §5 (AI/Autonomous Weapons) |
| **ISec-8** | DP-DG-8 | Intelligence & Security | Computational Civil Defense | Part XX §6 (Civil Defense) |
| **ISec-9** | DP-DG-9 | Intelligence & Security | Intelligence Budget Transparency | Part XX §1 (Democratic Oversight) |
| **ISec-10** | DP-DG-10 | Intelligence & Security | Periodic Intelligence Review | Part XX §1 (Democratic Oversight) |
| **ISec-11** | DP-DG-11 | Intelligence & Security | Cross-Jurisdictional Accountability | Part XX §1 (Democratic Oversight) |
| **ISec-12** | DP-DG-12 | Intelligence & Security | Democratic Override of Emergency Powers | Part XX §6 (Civil Defense) |
| **WT-1** | DP-WT-1 | Wealth Transfer | Intergenerational Transfer Cap Principle | Part XXI §3 (Intergenerational Wealth Transfer) |
| **WT-2** | DP-WT-2 | Wealth Transfer | Progressive Wealth Tax Principle | Part XXI §4 (Wealth Taxes) |
| **WT-3** | DP-WT-3 | Wealth Transfer | Constitutional Capital Stake Principle | Part XXI §5 (Universal Capital Stakes) |
| **WT-4** | DP-WT-4 | Wealth Transfer | Civilizational Sovereign Wealth Fund Principle | Part XXI §5 (Universal Capital Stakes) |
| **WT-5** | DP-WT-5 | Wealth Transfer | Beneficial Ownership Mandate Principle | Part XXI §6 (Tax Havens) |
| **WT-6** | DP-WT-6 | Wealth Transfer | Exit Tax Principle | Part XXI §6 (Tax Havens) |
| **WT-7** | DP-WT-7 | Wealth Transfer | Great Compression Encoding Principle | Part XXI §2 (Great Compression) |
| **WT-8** | DP-WT-8 | Wealth Transfer | Wealth Concentration Limit Principle | Part XXI §3 (Intergenerational Wealth Transfer) |
| **WT-9** | DP-WT-9 | Wealth Transfer | Secrecy Jurisdiction Sanctions Principle | Part XXI §6 (Tax Havens) |
| **WT-10** | DP-WT-10 | Wealth Transfer | Automation Rent Redistribution Principle | Part XXI §1 (Piketty r>g) |
| **WT-11** | DP-WT-11 | Wealth Transfer | Pay Ratio Principle | Part XXI §2 (Great Compression) |
| **WT-12** | DP-WT-12 | Wealth Transfer | Wealth Inequality Dashboard Principle | Part XXI §1 (Piketty r>g, SLE Design) |

### 5.2 Cross-Domain DP Dependencies

The following DPs have direct dependencies across domains and must be integrated with awareness of their cross-domain implications:

| Dependency Chain | DPs Involved | Nature of Dependency |
|---|---|---|
| **Privacy architecture** | IS-2 → MS-2 → ISec-1 | IS-2 establishes data sovereignty as principle; MS-2 operationalizes it for monetary transactions; ISec-1 makes it architecturally unalterable for surveillance prevention |
| **CSWF funding chain** | MS-4/MS-5 → WT-4 → WT-3 → MS-7 | The CSWF (MS-4/MS-5) is the financial engine; WT-4 establishes its capitalization sources; WT-3/MS-7 distribute its returns as capital stakes |
| **Democratic accountability** | ISec-2 → ISec-3 → ISec-4 → ISec-5 → IS-3 | Oversight Tribunal (ISec-2) requires dual-key (ISec-3), classification reform (ISec-4), whistleblower protection (ISec-5), and algorithmic transparency (IS-3) to function |
| **Biodiversity financing** | SP-2 → MS-4 → WT-2 | The Biodiversity Fiscal Engine (SP-2) requires funding from the CSWF (MS-4) and wealth tax receipts (WT-2) |
| **Constitutional drift** | IS-11 → ISec-12 → IS-12 | Drift detection (IS-11) must be connected to emergency power constraints (ISec-12) and institutional health monitoring (IS-12) to prevent gradual constitutional erosion |
| **Wealth monitoring** | WT-12 → WT-8 → MS-8 | The Wealth Inequality Dashboard (WT-12) triggers concentration limits (WT-8), which parallel systemic risk limits (MS-8) in the financial domain |

---

## 6. Implementation Priority for Docx Upgrade

### 6.1 Recommended Order: Parts XVII–XXI

The five new Parts should be added to Algorapolis.docx in the following order, with rationale:

| Priority | Part | Domain | Rationale |
|---|---|---|---|
| **1st** | **Part XVII** | Information Sovereignty | **Precondition for all others.** Every other domain depends on information integrity. The SLE and NDT are information-processing architectures; without information sovereignty, no other domain's specifications can be trusted. IS-1 (Full-Stack Sovereignty Mandate) establishes the monitoring infrastructure that subsequent parts will rely on. IS-2 (Data as Sovereign Territory) is the principle that MS-2 and ISec-1 operationalize. Must come first. |
| **2nd** | **Part XVIII** | Monetary Systems | **Metabolic substrate.** The civilizational monetary architecture funds everything else — the CSWF (MS-4/MS-5) is the financial engine for capital stakes (WT-3/WT-4) and biodiversity financing (SP-2). The privacy architecture for monetary transactions (MS-2) must be consistent with the information sovereignty principles (IS-2) established in Part XVII. Must come second because it depends on IS principles and enables WT/SP financing. |
| **3rd** | **Part XX** | Intelligence & Security | **Existential risk mitigation.** The democratic gap in intelligence and security is the most dangerous absence: an SLE with intelligence capabilities but without democratic accountability is a surveillance apparatus. ISec-1 (Architectural Privacy Enforcement) must be specified after IS-2 (Data as Sovereign Territory) to ensure consistency. ISec-8 (Computational Civil Defense) is the security dimension of civilizational immunity and should be integrated while the immunity protocol (Part XVI) is fresh. Comes third because it operationalizes the privacy principles from Parts XVII–XVIII. |
| **4th** | **Part XIX** | Species Preservation | **Biospheric foundation.** While ecologically foundational, the species preservation architecture is less of a direct dependency for the SLE's core governance logic. SP-2 (Biodiversity Fiscal Engine) requires the CSWF (MS-4) to be established first. SP-1 (Legal Personhood) is a rights framework that follows logically after the information sovereignty and monetary rights frameworks. SP-12 (Ecological Monitoring) parallels the monitoring infrastructure in IS-1/IS-7 and can reuse established NDT patterns. |
| **5th** | **Part XXI** | Wealth Transfer | **Political economy capstone.** The wealth transfer DPs are the most cross-referential: WT-3/WT-4 depend on MS-4/MS-5/MS-7 (CSWF and Capital Stakes); WT-7 (Great Compression Encoding) depends on MS-10 (Fiscal-Monetary Coordination); WT-5 (Beneficial Ownership) depends on IS-4 (Cross-Border Data Flow). Wealth transfer is the domain that ties the others together — it requires the monetary infrastructure (Part XVIII), the information sovereignty (Part XVII), and the democratic accountability (Part XX) to be in place before its countermeasures can be fully specified. It is the capstone, not the foundation. |

### 6.2 Integration Timeline

| Phase | Duration | Activities |
|---|---|---|
| **Phase 1: Foundation** | Weeks 1–3 | Add Part XVII (Information Sovereignty). Insert gap-fill pointer in Section 13. Update repository README with new directory structure. Verify IS-1 through IS-12 cross-references. |
| **Phase 2: Monetary Architecture** | Weeks 4–6 | Add Part XVIII (Monetary Systems). Insert gap-fill pointer in Section 51.1. Verify MS-2 consistency with IS-2. Verify MS-4/MS-5 CSWF architecture is compatible with WT-3/WT-4 requirements (pre-positioning). |
| **Phase 3: Democratic Accountability** | Weeks 7–9 | Add Part XX (Intelligence & Security). Insert gap-fill pointer in Sections 14–15. Verify ISec-1 consistency with IS-2 and MS-2. Verify ISec-8 integration with Civilizational Immunity Protocol (Part XVI). |
| **Phase 4: Biospheric Architecture** | Weeks 10–12 | Add Part XIX (Species Preservation). Insert gap-fill pointer in Section 22. Verify SP-2 funding chain through MS-4. Verify SP-1 legal personhood framework is compatible with IS-2 data sovereignty framework. Add cross-references to `/research/species-ecology/`. |
| **Phase 5: Political Economy Capstone** | Weeks 13–15 | Add Part XXI (Wealth Transfer). Insert gap-fill pointer in Simulation Findings Part IX. Verify WT-3/WT-4 consistency with MS-4/MS-5/MS-7. Verify WT-5 consistency with IS-4. Verify WT-12 dashboard integration with NDT monitoring infrastructure. |
| **Phase 6: Cross-Reference Audit** | Weeks 16–18 | Complete audit of all bidirectional cross-references. Verify DP dependency chains (Section 5.2). Ensure no circular or broken references. Generate updated DP master index. |

### 6.3 Risk Mitigation

| Risk | Mitigation |
|---|---|
| **Cross-domain DP inconsistency** | Before each Part integration, verify that all DPs referencing previously integrated Parts are consistent with the established specifications. Use the dependency chains in Section 5.2 as a checklist. |
| **Document bloat** | Each new Part should follow the existing Algorapolis docx format: introduction → domain analysis → SLE/NDT implications → Design Principles. Avoid duplicating material that exists in the research files; reference by file path and section number. |
| **DP numbering conflicts** | The global IDs (IS-1, MS-1, SP-1, ISec-1, WT-1) are domain-prefixed and do not conflict with existing DP numbering. Maintain a master DP index that maps global IDs to docx locations. |
| **License compatibility** | All priority gap research is CC-BY-SA 4.0 (content) compatible with the existing framework's content license. Code-level specifications should be MIT-licensed consistent with the existing code license. |

---

## 7. Author & License

### 7.1 Author

**Goodluck Japhet Macha**  
Independent Researcher, Tanzania  

The Priority Gap Research (Parts I–V) and this Integration Guide (Part VI) were authored as a unified research program to fill the foundational gaps identified in the Algorapolis Civilization Architecture Framework. All five domain research chapters and this integration guide constitute original work building on the Algorapolis framework's existing structure, cross-referencing its existing sections, and specifying new architecture for the SLE and NDT.

### 7.2 License

This work is dual-licensed, consistent with the Algorapolis Civilization Architecture Framework:

- **Code and technical specifications** (SLE/NDT module definitions, algorithmic specifications, data structures, computational protocols): **MIT License**
- **Content, research, analysis, and prose** (all narrative text, case studies, empirical evidence, design principle descriptions, policy analysis): **Creative Commons Attribution-ShareAlike 4.0 International (CC-BY-SA 4.0)**

### 7.3 Citation

```
Macha, G. J. (2026). Algorapolis Priority Gap Research: Information Sovereignty,
Monetary Systems, Species Preservation, Intelligence & Security, and Wealth Transfer.
Integration Guide (ALG-GUIDE-2026-001). Algorapolis Civilization Architecture Framework.
Licensed under CC-BY-SA 4.0 (content) and MIT (code).
```

### 7.4 Related Documents in Repository

| Document | Path | Relationship |
|---|---|---|
| Information Sovereignty Gap Research | `/research/priority-gaps/01-information-sovereignty-priority-gap-research.md` | Part I of this research program |
| Monetary Systems Gap Research | `/research/priority-gaps/02-monetary-systems-priority-gap-research.md` | Part II of this research program |
| Species Preservation Gap Research | `/research/priority-gaps/03-species-preservation-priority-gap-research.md` | Part III of this research program |
| Intelligence & Security Gap Research | `/research/priority-gaps/04-intelligence-security-democratic-gap-research.md` | Part IV of this research program |
| Wealth Transfer Gap Research | `/research/priority-gaps/05-wealth-transfer-generational-wealth-priority-gap-research.md` | Part V of this research program |
| Species Ecology Research | `/research/species-ecology/` | Foundation for Part III (Species Preservation) |
| Civilizational Immunity Protocol | `/research/immunity/` | Cross-referenced by IS-12, ISec-1, ISec-8 |
| Civilizational Research Agenda | `/research/civilizational-agenda/` | Original brief outlines superseded by Parts I–V |
| Simulation Findings | `/research/simulation-findings/` | Part IX identifies r>g; Part V encodes countermeasures |
| Deeper Research | `/research/simulation-findings/deeper-research/` | Parallel gap-fill for partially-covered domains |

---

*End of Integration Guide. For questions regarding DP integration priority, cross-reference verification, or SLE/NDT module dependencies, refer to the dependency chains in Section 5.2 and the implementation timeline in Section 6.2.*
