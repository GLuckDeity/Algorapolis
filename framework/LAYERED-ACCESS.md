# LAYERED ACCESS

## Layered Access & Governance Permissions — Who Sees What

---

## The Core Principle

In Algorapolis, information visibility is not binary — it is layered. Not every citizen needs to see every piece of governance data, and not every official needs access to every system. But the default is transparency: access restrictions must be justified, not access grants. The architecture implements the principle that **the government's business is the people's business**, with specific, constitutionally defined exceptions for security, privacy, and operational necessity.

---

## The Six Visibility Layers

### Layer 1: Citizen View (Default)
**Access scope:** Aggregated, anonymized data about governance operations, resource flows, and system health.

Every citizen has the right to see: where money comes from and where it goes, which infrastructure systems are functioning and which are failing, what the SLE is deciding and why, how their representatives are voting, and what the overall well-being indicators show. The Citizen View is the cognitive interface between the governance system and the population it serves. It uses visual, spatial, and color-coded representations — citizens should see resource flows rather than read spreadsheets.

**Technical implementation:** Public dashboards, USSD/IVR interfaces, open data APIs, narrative explanations of all consequential decisions.

### Layer 2: Civic Participation View
**Access scope:** Domain-specific data relevant to a citizen's active participation in governance.

Citizens serving on sortition-based assemblies, participating in deliberative processes, or exercising liquid democracy delegation receive enhanced access to the specific data relevant to their civic function. This includes: detailed policy analysis documents, simulation results from governance sandboxes, comparative governance data from other jurisdictions, and expert testimony summaries.

**Technical implementation:** Role-based access grants with automatic expiration tied to civic service terms.

### Layer 3: Professional Operational View
**Access scope:** Data necessary for professional functions within the governance system.

Civil servants, infrastructure operators, healthcare professionals, and other operational roles receive access to the data necessary for their professional function. This includes: real-time infrastructure telemetry, service delivery metrics, case-level data for their domain, and operational coordination information. Access is strictly limited to the professional domain: a healthcare operator cannot access transportation data, and a land registry official cannot access tax data.

**Technical implementation:** Attribute-Based Access Control (ABAC) with role, domain, and need-to-know constraints.

### Layer 4: Analytical Intelligence View
**Access scope:** Cross-domain data for analysis, prediction, and policy development.

Analysts, researchers, and SLE operators receive access to cross-domain data for the purposes of governance intelligence: pattern detection, anomaly identification, predictive modeling, and policy simulation. This layer includes: cross-domain data fusion, statistical analysis tools, simulation environments, and historical trend data. All access is logged and auditable. Individual-level data remains inaccessible — only aggregated and differentially private data.

**Technical implementation:** Secure analytical environments with differential privacy, query auditing, and output monitoring.

### Layer 5: Institutional Leadership View
**Access scope:** Strategic overview data for institutional decision-making.

Elected officials, constitutional council members, and HERB members receive access to strategic overview data: system health dashboards, exception alerts, well-being trajectories, and cross-domain coordination status. This layer does not provide access to individual-level data but provides the most comprehensive aggregate view of governance operations.

**Technical implementation:** Executive dashboards with real-time data feeds, decision support systems, and crisis coordination interfaces.

### Layer 6: Constitutional Oversight View
**Access scope:** Full access for constitutional compliance verification.

Distributed Constitutional Councils, the Supreme Constitutional Court, and authorized auditors receive the most comprehensive access for the purpose of verifying constitutional compliance. This includes: complete SLE audit trails, all module interaction logs, constitutional compliance verification results, and any data relevant to constitutional review proceedings. This is the only layer with access to case-level data across domains — and even this access is limited to constitutional review proceedings, with all access logged and publicly disclosed.

**Technical implementation:** Multi-signature access requiring authorization from multiple independent constitutional actors, with full access logging and public disclosure.

---

## Technical Implementation: RBAC-ABAC Hybrid with Zero Trust

### Role-Based Access Control (RBAC)
Base roles are defined by civic function: Citizen, Civic Participant, Operational Staff, Analyst, Leadership, Constitutional Oversight. Each role maps to a set of permitted visibility layers and data domains.

### Attribute-Based Access Control (ABAC)
Dynamic attributes supplement base roles: domain expertise, current assignment, security clearance, geographic jurisdiction, temporal access window. A citizen serving on a land policy assembly temporarily gains access to Layer 2 data in the land domain — access that automatically expires when the assembly concludes.

### Zero Trust Architecture
No user, system, or module is trusted by default. Every access request is authenticated, authorized, and encrypted. The network perimeter is not the security boundary — every interaction is verified regardless of origin. Implementation uses mutual TLS, policy engines (Open Policy Agent / AWS Cedar), and continuous authentication.

### Policy Engine
Open Policy Agent (OPA) provides the unified policy decision point. All access control policies are expressed in Rego (OPA's policy language), stored in version-controlled repositories, and subject to the same formal verification pipeline as governance rules. Changing access control policies requires the same constitutional compliance verification as any governance rule.

---

## Constitutional Constraints on Access

### The Transparency Default
Access restrictions must be justified, not access grants. Any data that is not explicitly restricted by constitutional provision is, by default, publicly accessible at Layer 1. The burden of proof lies with those who wish to restrict access, not with those who seek it.

### The Anti-Surveillance Principle
No access layer grants access to individual citizen data. The system observes patterns and aggregates; it does not observe individuals. Even at Layer 6 (Constitutional Oversight), case-level data access is limited to constitutional review proceedings and requires multi-signature authorization.

### The Temporal Limitation
All enhanced access grants (Layers 2–6) have mandatory expiration dates. Civic participation access expires when civic service ends. Professional access expires when employment ends. Analytical access expires when the analysis is complete. No permanent enhanced access exists — all access is temporary, auditable, and revocable.

### The Audit Trail
Every access event — every query, every data retrieval, every dashboard view — is logged permanently. Access logs are themselves subject to access control: citizens can see aggregate access patterns, while detailed access logs are visible only to Constitutional Oversight.

---

## Cross-Domain Access Matrix

| Data Domain | Layer 1 | Layer 2 | Layer 3 | Layer 4 | Layer 5 | Layer 6 |
|-------------|---------|---------|---------|---------|---------|---------|
| **Budget execution** | Aggregated flows | Domain detail | Operational | Cross-domain | Strategic | Full |
| **Infrastructure status** | System health | Domain detail | Real-time | Predictive | Exception | Full |
| **Economic telemetry** | Indicators | Sector detail | Domain ops | Cross-domain | Strategic | Full |
| **Well-being indices** | Aggregated | Domain detail | — | Statistical | Trend | Full |
| **Civic emotional signals** | Aggregated only | Domain detail | — | Statistical | Trend | Full |
| **SLE decisions** | 3 representations | Policy detail | Operational | Analytical | Strategic | Full audit |
| **Individual citizen data** | — | — | Domain-limited | Differentially private | — | Constitutional only |
| **Security/defense** | — | — | Operational | Threat analysis | Strategic | Full |

---

## African and Tanzanian Context

Tanzania's e-Government Agency (eGA) has been building digital government infrastructure, but current access control is largely role-based and manually administered. The RBAC-ABAC hybrid with zero trust represents a significant capability upgrade. Key considerations include: USSD-based access for Layer 1 (citizen view on basic phones), multilingual access interfaces (Swahili, English, local languages), low-bandwidth optimization for all layers, and integration with NIDA identity systems for authentication.

---

*The government's business is the people's business. Access restrictions must be justified, not access grants.*
