# Contributing a Case Study

> **Grounding Algorapolis in real-world evidence** — How to research, write, and submit governance case studies that inform the civilization architecture.

---

## Introduction

The Algorapolis specification is a theoretical architecture — a comprehensive design for modular governance derived from civilizational failure analysis, mathematical proof, and philosophical reasoning. But theory without evidence is ideology. Case studies are the empirical anchor that prevents the architecture from drifting into abstraction: they test whether the framework's principles actually explain what happens in the real world, and they reveal dynamics that pure theory cannot anticipate.

Both positive and negative specifications are valued. A positive specification shows what works — a governance experiment that produced good outcomes, from which the architecture can learn and incorporate proven mechanisms. A negative specification shows what fails — a governance catastrophe that the architecture must structurally prevent. The Dutch Childcare Benefits Scandal and Australia's Robodebt are negative specifications that directly shaped Algorapolis's Emotional Intelligence Architecture and the principle that the SLE serves, never rules. Estonia's digital nation and Taiwan's civic tech are positive specifications that informed the Governance API architecture and democratic deliberation design.

This guide explains how to contribute a case study to the Algorapolis repository. It covers what makes a good case study, the two types of specification, the step-by-step research and writing process, the template to follow, and how case studies inform the specification update process.

---

## What Makes a Good Case Study

A good Algorapolis case study has four properties:

### 1. Empirical

It is grounded in observable, verifiable evidence — not anecdote, not speculation, not theoretical extrapolation. Primary sources (academic papers, government reports, investigative journalism, court records, audit findings) are the foundation. Secondary sources (commentary, opinion, analysis) may supplement but cannot replace primary evidence.

### 2. Analytical

It does not merely describe what happened; it analyzes *why* it happened through the lens of the Algorapolis framework. A case study that narrates a governance failure without connecting it to the architecture's principles is a news report, not a contribution. The analysis must identify which layers are relevant, which guardrails were violated (or upheld), which governance modalities were mismatched to their domains, and what the architecture would predict or prescribe.

### 3. Grounded in Evidence

Every claim is cited. Every conclusion is supported. Where evidence is ambiguous or contested, the case study acknowledges the ambiguity rather than resolving it in favor of a preferred narrative. Intellectual honesty is non-negotiable — a case study that cherry-picks evidence to confirm the framework's predictions is worse than useless; it is actively misleading.

### 4. Draws Lessons for the Architecture

The ultimate purpose of a case study is not to judge the past but to inform the future. Every case study must explicitly identify transferable lessons: what should the architecture incorporate, avoid, modify, or investigate further? A case study that ends with "this was bad" without drawing architectural implications is incomplete.

---

## Two Types of Case Study

### Positive Specification (What Works)

A positive specification documents a governance experiment, system, or approach that produced measurably good outcomes. It asks: *what did this system get right, and can the Algorapolis architecture incorporate its mechanisms?*

Characteristics of a good positive specification:

- **Documented success**: The positive outcomes are verifiable through independent evidence, not merely claimed by the system's proponents.
- **Mechanism identification**: The case study identifies *which specific mechanisms* produced the good outcomes, not just that good outcomes occurred. "Estonia's digital governance works" is an observation; "Estonia's X-Road interoperability framework eliminates bureaucratic silos by standardizing data exchange" is a mechanism.
- **Contextual awareness**: The case study acknowledges the conditions that enabled success — cultural, institutional, economic, demographic. A mechanism that works in a small, homogeneous, high-trust society (Estonia: 1.3 million people) may not transfer directly to a large, diverse, low-trust society (Tanzania: 65 million people). Context matters.
- **Limitation honesty**: Even positive specifications have limitations. Estonia's digital governance is impressive but was built on a foundation of high institutional trust and ethnic homogeneity that facilitated adoption. Taiwan's civic tech resolved specific policy disputes but operates with advisory authority only, limiting its democratic impact. Acknowledging limitations is not negativism; it is rigor.

### Negative Specification (What Fails)

A negative specification documents a governance failure, catastrophe, or structural vulnerability. It asks: *what went wrong, how does the Algorapolis framework explain it, and what must the architecture structurally prevent?*

Characteristics of a good negative specification:

- **Causal analysis, not blame assignment**: The Dutch Childcare Benefits Scandal was not caused by a single malicious actor; it was caused by an architectural failure — an algorithmic authority operating without emotional intelligence, human oversight, or constitutional constraints on automated decision-making. The case study must identify the *structural* cause, not the individual villain.
- **Guardrail relevance**: Every negative specification should connect to at least one of the Four Guardrails or Six Human-Reserved Domains. If a governance failure does not violate any Algorapolis principle, then either the failure is outside the architecture's scope or the architecture has a gap that the case study reveals. Both are valuable findings.
- **Transferability of the failure mode**: Is this a failure that could happen in other contexts, or is it unique to a specific institutional, cultural, or political environment? The most valuable negative specifications identify failure modes that are structural — they can recur anywhere the same architectural vulnerability exists.
- **Constructive implications**: A negative specification that merely documents horror is catharsis, not contribution. The case study must identify what the architecture should do differently to prevent this class of failure. The Dutch Childcare Scandal's constructive implication was the Emotional Intelligence Architecture and the Constitutional Sandbox Limits on the SLE.

---

## Step-by-Step Process

### Step 1: Select a Governance Experiment, System, or Failure

Choose a case that is:

- **Substantive**: It involves a real governance system that affected real people, not a thought experiment or hypothetical.
- **Documented**: Sufficient primary sources exist to support rigorous analysis. If the relevant documents are classified, inaccessible, or destroyed, the case cannot be adequately researched.
- **Architecturally relevant**: The case touches on at least one Algorapolis layer, guardrail, or principle. Not every governance failure is an Algorapolis case study — some are purely political, cultural, or personal. The case must have structural implications that the architecture can address.
- **Non-duplicate**: Check the [existing case studies](../../research/case-studies/) to ensure your case has not already been covered. If it has, consider whether there is a substantially different analytical angle that would justify a new study.

### Step 2: Research Primary Sources

Rigorous research is the foundation. Consult:

- **Academic papers**: Peer-reviewed studies in political science, public administration, law, economics, and technology governance. Use Google Scholar, JSTOR, SSRN, and disciplinary databases.
- **Government reports**: Official inquiries, audit reports, legislative hearings, policy evaluations. These often provide the most detailed factual record.
- **Investigative journalism**: High-quality investigative reporting (e.g., ProPublica's COMPAS investigation, the Dutch media's Childcare Scandal coverage) often reveals facts that official reports obscure.
- **Court records**: Judicial opinions, class-action filings, and regulatory enforcement actions provide legally verified facts.
- **International assessments**: Reports from the UN, World Bank, IMF, OECD, and regional bodies provide comparative context.
- **Civil society reports**: NGO analyses, whistleblower accounts, and community testimony provide perspectives that institutional sources may omit.

**Source evaluation**: Not all sources are equal. Distinguish between primary evidence (original documents, data, testimony) and secondary interpretation (commentary, analysis, opinion). Prioritize primary sources. When sources conflict, note the conflict rather than silently choosing one version.

**Minimum source count**: A case study should cite at least 10 distinct primary sources. This is a floor, not a ceiling — complex cases may require 30+.

### Step 3: Analyze Through the Algorapolis Lens

This is the step that transforms a governance narrative into an Algorapolis case study. For each case, systematically analyze:

**Which layers does it touch?**
- Layer 1 (Philosophy): Does the case involve civilizational failure analysis, foundational philosophy, or the theory of balance?
- Layer 2 (Psychology): Does it involve tribal psychology, cognitive biases, incentive structures, or empathy failures?
- Layer 3 (Governance): Does it involve governance modality, the SLE, law as code, or democratic deliberation?
- Layer 4 (Economics): Does it involve digital identity, privacy, economic design, or meritocracy?
- Layer 5 (Technology): Does it involve infrastructure, technical foundations, or the digital twin?
- Layer 6 (Security): Does it involve anti-corruption, anti-capture, constitutional locks, or defense?
- Layer 7 (Culture): Does it involve cultural legitimacy, civilizational memory, or artistic/religious freedom?
- Layer 8 (Ecology): Does it involve planetary boundaries, energy, food, or urban design?
- Layer 9 (Civilization): Does it involve family, time governance, science, disaster, or emergence?
- Layer 10 (Ark): Does it involve civilizational continuity, propagation, or transition?

**Which guardrails are relevant?**
- No omniscience: Did the system aspire to total knowledge of citizen behavior?
- No total behavioral prediction: Did the system attempt to predict individual behavior?
- No centralized social engineering: Did the system manipulate citizens toward state-defined outcomes?
- No unrestricted computational control: Did the system exercise unbounded algorithmic authority?

**Which human-reserved domains were affected?**
- Religion and Spirituality
- Culture and Identity
- Family Structure
- Moral Interpretation
- Artistic Expression
- Personal Identity

### Step 4: Apply the Matching Principle

The Matching Principle — governance modality must match domain nature — is Algorapolis's original contribution. For your case study, assess:

- **Was the governance modality appropriate for the domain?** A democracy applied to resource allocation produces inefficient outcomes. An algorithm applied to moral judgment produces inhumane outcomes. A technocracy applied to cultural expression produces cultural erasure.
- **What modality mismatch occurred, if any?** Identify the specific mismatch and its consequences.
- **What would the Algorapolis Module Map prescribe?** Which modality would the framework assign to this domain, and how would that differ from what actually happened?

The Matching Principle analysis is often the most revealing part of the case study. Many governance failures can be traced to a single modality mismatch — the right tool used for the wrong job.

### Step 5: Identify Transferable Lessons

Explicitly state what the Algorapolis architecture should learn from this case:

- **What to incorporate**: Specific mechanisms, design patterns, or institutional innovations that the case demonstrates to be effective.
- **What to avoid**: Specific failure modes, architectural vulnerabilities, or design errors that the case reveals.
- **What to investigate further**: Open questions that the case raises but cannot resolve. These become candidates for Governance Sandbox experiments or further research studies.
- **What to modify**: Existing architectural specifications that the case suggests should be revised, extended, or constrained.

### Step 6: Write the Case Study Following the Template

Use the template below. Follow it exactly — the standardized structure enables cross-case comparison, which is essential for accumulating evidence across multiple studies.

### Step 7: Submit for Peer Review

1. **Fork the repository** and create a branch: `case-study/[case-name]`
2. **Place your case study** in `research/case-studies/` following the naming convention: `[descriptive-kebab-case].md`
3. **Submit a pull request** with a clear summary of the case, the analytical lens, and the key lessons.
4. **Respond to review** — case studies receive the same adversarial scrutiny as any other contribution. Reviewers will challenge your analysis, question your source selection, and probe whether the lessons you draw are supported by the evidence.

---

## Case Study Template

```markdown
# [Case Title]

> [One-sentence description of the case]

---

## Context

- **Country/Region:**
- **Time Period:**
- **System Type:** (e.g., digital governance, algorithmic administration, democratic innovation, surveillance state)
- **Population Affected:**
- **Scale:** (individual / community / national / international)

## Governance System Description

[Describe the governance system in detail. What was it designed to do? How did it work?
What were its technical, institutional, and legal components? What was its scope and
authority? Include specifics: technologies used, institutional structures, legal
frameworks, oversight mechanisms.]

## Analysis Through Algorapolis Layers

### Layer [N]: [Layer Name]
[How does this case relate to this layer? What aspects of the governance system
fall within this layer's domain? What does the layer's specification predict
about how this system should behave?]

[Repeat for each relevant layer.]

## Constitutional Compatibility Assessment

### Guardrail Compliance
- **Guardrail 1 (No Omniscience):** [Assessment]
- **Guardrail 2 (No Total Behavioral Prediction):** [Assessment]
- **Guardrail 3 (No Centralized Social Engineering):** [Assessment]
- **Guardrail 4 (No Unrestricted Computational Control):** [Assessment]

### Human-Reserved Domain Compliance
- **Religion and Spirituality:** [Assessment]
- **Culture and Identity:** [Assessment]
- **Family Structure:** [Assessment]
- **Moral Interpretation:** [Assessment]
- **Artistic Expression:** [Assessment]
- **Personal Identity:** [Assessment]

### Matching Principle Assessment
[Was the governance modality appropriate for the domain? What modality mismatch
occurred, if any? What would the Algorapolis Module Map prescribe?]

## Lessons for the Architecture

### What to Incorporate
[Specific mechanisms, design patterns, or innovations to adopt]

### What to Avoid
[Specific failure modes, vulnerabilities, or errors to structurally prevent]

### What to Investigate Further
[Open questions requiring additional research or sandbox experimentation]

### What to Modify
[Suggested revisions to existing architectural specifications]

## Open Questions

[Questions that this case raises but cannot resolve. These may become the
starting points for new research studies, sandbox experiments, or layer proposals.]

## References

[Full citations for all primary and secondary sources, following a consistent
academic citation format (APA, Chicago, or IEEE). Minimum 10 distinct primary
sources.]

---

*Case study type: [Positive specification / Negative specification]*
*Algorapolis layers: [List relevant layer numbers]*
*Guardrails violated: [List violated guardrails, if any]*
*Human-reserved domains affected: [List affected domains, if any]*
```

---

## Existing Case Studies as Examples

The repository already contains six case studies that illustrate both positive and negative specifications. Study these as models for your own contribution:

| Case Study | Type | Key Lesson |
|-----------|------|-----------|
| [**Estonia: Digital Nation**](../../research/case-studies/estonia-digital-nation.md) | Positive | X-Road interoperability, once-only principle, and digital identity at scale. Limitation: small, homogeneous, high-trust context. |
| [**Singapore: Smart Nation**](../../research/case-studies/singapore-smart-nation.md) | Positive | Real-time urban coordination and predictive infrastructure management. Limitation: concentrated institutional authority with limited democratic deliberation. |
| [**Taiwan: Civic Tech**](../../research/case-studies/taiwan-civic-tech.md) | Positive | Participatory digital governance (vTaiwan, Join.gov.tw) resolving politically intractable questions. Limitation: advisory authority limits democratic impact. |
| [**Dutch Childcare Scandal**](../../research/case-studies/dutch-childcare-scandal.md) | Negative | Algorithmic authority without emotional intelligence, human oversight, or constitutional constraints produces morally catastrophic outcomes. Directly shaped the Emotional Intelligence Architecture. |
| [**Tanzania Election 2025**](../../research/case-studies/tanzania-election-2025.md) | Negative | Governance systems that provide no structural mechanism for preventing power perpetuation will be exploited. The crystallizing event that confirmed the framework's necessity. |
| [**China: Social Credit System**](../../research/case-studies/china-social-credit.md) | Negative | The nightmare scenario — centralized, opaque, punitive surveillance governance. The explicit negative specification that Algorapolis is architecturally designed to structurally prevent. |

---

## Priority Areas for New Case Studies

The following governance experiments, systems, and failures have been identified as high-priority candidates for new case studies. This list is not exhaustive — if you have a case that is not listed but meets the criteria above, propose it.

### High Priority

- **Rwanda post-genocide governance** — How does a nation rebuild governance infrastructure after civilizational collapse? What role does centralized authority play in reconstruction, and what are the capture risks? Relevant to Layers 3, 6, and 7, and to the Transition Architecture (Layer 10).

- **Uruguay digital government** — A small Latin American nation that achieved significant digital governance progress without the authoritarian tendencies seen in larger digital governance experiments. Relevant to Layer 3 and the question of whether digital governance requires concentrated authority.

- **Iceland constitutional reform (2010–2013)** — A nation that used participatory democratic processes to draft a new constitution, which was then rejected by political institutions. Relevant to Layer 3 (democratic deliberation), Layer 6 (anti-capture), and the question of democratic legitimacy when institutional inertia overrides popular will.

- **India Aadhaar** — The world's largest biometric identity system. Demonstrates both the power of universal digital identity and the risks of making essential services dependent on a single identity infrastructure. Relevant to Layer 4 (digital identity), Layer 6 (security), and the Four Guardrails.

- **Brazil participatory budgeting (Porto Alegre)** — The pioneering experiment in democratic resource allocation. Demonstrates that citizens can directly allocate public resources effectively, but also shows the limitations of participatory mechanisms at scale. Relevant to Layer 3 (democratic deliberation), Layer 4 (economics), and the Matching Principle.

### Medium Priority

- **South Korea digital platform government** — Rapid digitalization of government services with high citizen adoption. Relevant to Layer 3 and the question of cultural preconditions for digital governance.

- **Chile constitutional convention (2019–2022)** — Another participatory constitutional process, this one resulting in a draft that was rejected by referendum. Relevant to Layer 3 and the tensions between participatory legitimacy and institutional durability.

- **Kenya M-Pesa and financial inclusion** — Mobile money as governance infrastructure. Demonstrates that leapfrog technologies can create governance capabilities that bypass traditional institutional development. Relevant to Layer 4 (economics), Layer 5 (technology), and the African leapfrogging thesis.

- **EU GDPR enforcement** — Privacy regulation at supranational scale with real enforcement consequences. Relevant to Layer 4 (privacy), Layer 6 (security), and the question of whether legal guarantees can substitute for mathematical guarantees.

- **New Zealand Wellbeing Budget** — Government budgeting explicitly oriented around wellbeing metrics rather than GDP. Relevant to Layer 4 (economics), Layer 2 (psychology), and the question of whether governance can optimize for human flourishing rather than economic output.

### Exploratory

- **Mars simulation habitats (HI-SEAS, MDRS)** — Governance in closed-loop, resource-constrained environments. Relevant to Layer 10 (Ark) and the Mars Governance Protocol.

- **Autonomous zone governance (CHOP/CHAZ, Exarchia)** — Governance in the absence of state authority. Relevant to Layer 3 (governance), Layer 6 (security), and the Offline Resilience framework.

- **Decentralized autonomous organizations (DAOs)** — Algorithmic governance in practice, with real financial stakes and real governance failures. Relevant to Layer 3 (governance), Layer 5 (technology), and the question of whether algorithmic governance can work without human judgment.

- **Scandinavian prison systems** — Restorative justice at national scale. Relevant to Layer 2 (psychology), Layer 3 (governance), and the Emotional Intelligence Architecture.

---

## How Case Studies Inform the Specification Update Process

Case studies are not archival — they are active inputs into the architecture's evolution. When a case study reveals a gap, vulnerability, or opportunity in the specification, it triggers a structured update process:

1. **Identification**: The case study's "Lessons for the Architecture" section flags the specific specification sections that may need revision.

2. **Assessment**: Maintainers evaluate whether the case study's findings are supported by sufficient evidence to warrant specification changes, or whether further research (including sandbox experimentation) is needed first.

3. **Proposal**: If the findings are actionable, a specification amendment proposal is drafted, referencing the case study as evidence. The proposal follows the same constitutional process as any other amendment — formal specification, sandbox testing, community review, democratic authorization.

4. **Integration**: If the amendment is accepted, the specification is updated and the case study is linked from the relevant specification sections as supporting evidence.

5. **Validation**: After integration, the updated specification is tested against the case study's findings to verify that the amendment actually addresses the identified gap or vulnerability.

This creates a closed loop: case studies identify gaps → amendments address gaps → sandbox tests validate amendments → new case studies test the updated architecture against reality. The architecture improves not through top-down design but through empirical iteration grounded in evidence.

The six existing case studies have already shaped the specification in significant ways: the Dutch Childcare Scandal directly produced the Emotional Intelligence Architecture and the Constitutional Sandbox Limits; the Tanzania Election 2025 crystallized the anti-capture mechanisms; Estonia informed the Governance API design; Taiwan shaped the democratic deliberation layer; Singapore informed the real-time coordination specification; and China's Social Credit System serves as the negative specification against which every privacy and anti-surveillance measure is tested.

Your case study could be next.

---

*"Case studies are the empirical anchor that prevents the architecture from drifting into abstraction. They test whether the framework's principles actually explain what happens in the real world, and they reveal dynamics that pure theory cannot anticipate. Contribute yours."*
