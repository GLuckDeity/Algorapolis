# Proposing a New Civilization Layer

> **A constitutional process for extending the ten-layer civilization stack** — Adding a layer is not a feature request; it is a constitutional act that affects the entire architecture.

---

## Introduction

The Algorapolis civilization stack is organized into ten layers — six core (Philosophy, Psychology, Governance, Economics, Technology, Security) and four extended (Culture, Ecology, Civilization, Ark). These layers are not arbitrary. Each represents a fundamental domain of civilization: a material reality that governance must address, a set of constraints that no other layer covers, and a set of interactions with every other layer that produces emergent effects too complex to collapse into any single existing layer.

Adding an eleventh layer — or splitting, merging, or reordering the existing ten — is therefore not a casual act. It is a constitutional amendment to the architecture itself. It changes what the system governs, how it governs, and what it protects. It creates new dependencies, new failure modes, and new opportunities for both flourishing and capture.

This does not mean the stack is frozen. The Civilizational Humility Doctrine (Principle 10) explicitly acknowledges that the framework is permanently incomplete. The Non-Linear Continuity principle — drawn from the same philosophical wellspring as the Ark Protocol — recognizes that civilization does not evolve by smooth increment but by punctuated change. New layers may become necessary as material reality changes: space colonization, post-singularity coordination, or domains we cannot yet name.

But the barrier to adding a layer must be high. The "layer proliferation" risk is real: a stack with twenty layers is not twice as comprehensive as a stack with ten — it is a system where no one understands the interactions, where constitutional constraints become incoherent, and where every new layer becomes a potential vector for capture. The ten layers were chosen because each is necessary, none is sufficient alone, and the dependencies between them form a coherent whole. A new layer must meet the same standard.

This guide specifies the process for proposing a new civilization layer. It is designed to be rigorous without being prohibitive, and democratic without being anarchic. Follow every step. Skip none.

---

## Prerequisites

Before proposing a new layer, you must demonstrate three things:

1. **Deep understanding of the existing stack.** You should have read and engaged with the full architecture specification ([framework/ARCHITECTURE.md](../../framework/ARCHITECTURE.md)) and the core principles ([manifesto/01-CORE-PRINCIPLES.md](../../manifesto/01-CORE-PRINCIPLES.md)). A proposal that reinvents an existing layer, or proposes a layer that is already covered by the interaction of two existing layers, indicates insufficient preparation.

2. **Literature review.** What does existing scholarship say about the domain you want to elevate? Is there academic consensus that this domain is fundamental? Are there competing frameworks that treat it differently? A layer proposal without a literature review is an opinion, not a contribution.

3. **Demonstrated gap.** You must show that the existing ten layers, individually and in their interactions, cannot adequately address the material reality you are concerned with. This is the hardest prerequisite and the most important: the burden of proof is on the proposer to demonstrate necessity, not on the architecture to demonstrate sufficiency.

---

## Step-by-Step Process

### Step 1: Identify the Gap

**Question: What material reality is not covered by the existing stack?**

The ten layers cover philosophy, psychology, governance, economics, technology, security, culture, ecology, civilization-scale coordination, and civilizational continuity. If you believe there is a domain that falls outside all of these — or that is so fundamentally different in nature that subsuming it under an existing layer produces category errors — identify it precisely.

- What is the domain? Define its boundaries.
- What material reality does it address? A layer must correspond to something real — not an abstraction, not a metaphor, not a political preference.
- Why cannot existing layers handle it? Be specific. "The Governance layer doesn't address X" is a claim; demonstrate it with examples where the Governance layer's modality mismatch produces bad outcomes.
- What happens if this gap remains unfilled? What civilizational risk does it create?

**Output**: A gap statement — one paragraph that precisely identifies the uncovered material reality.

### Step 2: Literature Review

**Question: What does existing scholarship say about this domain?**

A civilization layer must be grounded in more than one person's observation. Survey the academic literature:

- Is this domain recognized as fundamental in political science, sociology, economics, philosophy, or any relevant discipline?
- Are there existing frameworks that treat this domain as a distinct governance concern?
- What are the major debates within the field? Where do scholars disagree?
- What empirical evidence supports the claim that this domain is fundamental?

The literature review must cite primary sources — peer-reviewed papers, established theoretical frameworks, and empirical studies. Blog posts, opinion pieces, and personal observations may supplement but cannot replace scholarly engagement.

**Output**: A literature review document (minimum 2,000 words) with full citations.

### Step 3: Constitutional Compatibility Check

**Question: Does the proposed layer violate any guardrail or human-reserved domain?**

Before investing further effort, verify that your proposed layer is constitutionally permissible. Check it against:

**The Four Guardrails:**
1. **No omniscience** — Does the layer require total knowledge of citizen behavior? If so, it violates Guardrail 1 and is constitutionally prohibited.
2. **No total behavioral prediction** — Does the layer require predicting individual behavior? If so, it violates Guardrail 2 and is constitutionally prohibited.
3. **No centralized social engineering** — Does the layer require manipulating citizen behavior toward state-defined outcomes? If so, it violates Guardrail 3 and is constitutionally prohibited.
4. **No unrestricted computational control** — Does the layer require unbounded SLE authority? If so, it violates Guardrail 4 and is constitutionally prohibited.

**The Six Human-Reserved Domains:**
1. Religion and Spirituality
2. Culture and Identity
3. Family Structure
4. Moral Interpretation
5. Artistic Expression
6. Personal Identity

If your proposed layer's primary function involves governing any of these domains, it is constitutionally prohibited unless it operates exclusively as a *protective boundary* (preventing others from violating the domain) rather than as a *governing authority* (defining what happens within the domain).

**Output**: A constitutional compatibility statement — for each guardrail and each human-reserved domain, a brief argument for why the proposed layer is compatible or how conflicts are resolved.

### Step 4: Module Map Integration

**Question: Which governance modalities apply to the proposed layer?**

The Matching Principle (Core Principle 1) requires that governance modality match domain nature. For your proposed layer, specify:

- Which civic domains fall within this layer?
- For each domain, which primary governance modality applies — algorithmic administration, democratic deliberation, constitutional locks, meritocratic selection, or human-reserved?
- Why is each modality the appropriate match? Reference the Module Map in the architecture specification.
- Are hybrid modalities required? Many domains require combinations (e.g., Healthcare uses hybrid algorithmic + democratic).

If your proposed layer requires a *new* governance modality not currently in the framework, you must also justify and specify that modality — a substantially larger undertaking.

**Output**: A Module Map extension table specifying domain-modality mappings with rationale.

### Step 5: Dependency Analysis

**Question: Which existing layers does the proposed layer depend on, and which depend on it?**

No layer exists in isolation. Map the dependencies:

- **Upstream dependencies**: Which existing layers must function for this layer to operate? (e.g., Technology depends on Economics for resource allocation; Security depends on Governance for constitutional authority.)
- **Downstream dependencies**: Which existing layers would depend on this new layer? What breaks if this layer fails?
- **Lateral interactions**: How does this layer interact with peer layers? Are there feedback loops, conflicts, or synergies?
- **Circular dependencies**: Does this layer create any circular dependency chains? If Layer A depends on Layer B which depends on Layer A, the architecture has a coherence problem.

The dependency analysis must be comprehensive. A layer that silently depends on an unstated assumption is a layer that will fail when that assumption is violated.

**Output**: A dependency graph (visual or textual) with all upstream, downstream, and lateral relationships specified.

### Step 6: Formal Specification

**Question: Can you prove constitutional compliance?**

This is where the proposal becomes engineering rather than advocacy. Using the Lean 4 theorem prover (the same tool used in the Algorapolis Legal Verification Pipeline), you must formally specify:

1. The layer's constitutional constraints — what it may and may not do.
2. The layer's invariants — properties that must hold at all times.
3. Proof that the layer's constraints are compatible with the existing constitutional framework.
4. Proof that the layer cannot expand its own authority without democratic authorization.

If you are not familiar with formal verification, this step may require collaboration with someone who is. The Algorapolis framework does not accept "trust me" as a constitutional argument. Mathematics is the armor; formal proofs are the armor's quality tests.

**Output**: A Lean 4 specification file with proven theorems, submitted alongside the proposal.

### Step 7: Governance Sandbox Testing

**Question: What happens when this layer is simulated?**

Before any layer is added to the architecture, it must be tested in the Governance Sandbox. Follow the [Running a Governance Sandbox](./running-a-sandbox.md) guide to:

1. Generate a synthetic population that includes the domain your layer addresses.
2. Run a baseline simulation (current architecture, without the new layer).
3. Run an intervention simulation (with the new layer).
4. Compare outcomes across metrics: economic efficiency, well-being, trust, social cohesion, constitutional compliance.
5. Stress test with adversarial scenarios: elite capture attempts, system shocks, constitutional subversion attempts.
6. Generate a Fidelity Gap Assessment.

The sandbox does not prove the layer works — it reveals how it behaves under controlled conditions. Sandbox results are advisory, not authoritative (the Critical Principle, Section 58.3). But a layer that produces catastrophic outcomes in sandbox testing is a layer that should not proceed.

**Output**: A sandbox experiment report following the format in the sandbox guide.

### Step 8: Community Review and Adversarial Testing

**Question: Can the proposal survive scrutiny?**

Submit the complete proposal (gap statement, literature review, constitutional compatibility statement, Module Map extension, dependency analysis, formal specification, and sandbox results) for community review:

1. **Open comment period** (minimum 30 days) — Anyone may review, critique, and challenge the proposal.
2. **Adversarial review** — Designated reviewers attempt to break the proposal: find constitutional violations the proposer missed, identify dependency failures, challenge the literature review's completeness, and probe the formal specification for errors.
3. **Red team exercise** — The Corruption Red Team tests whether the new layer introduces new vectors for capture, corruption, or constitutional erosion.
4. **Revision** — The proposer addresses all substantive concerns. Proposals that cannot survive adversarial review are withdrawn or fundamentally reworked.

The review process is intentionally stressful. A layer that cannot survive scrutiny in a controlled academic environment will not survive deployment in a real governance system. The adversity is the point.

**Output**: A final proposal incorporating all revisions, with a transparent record of objections raised and how they were addressed.

### Step 9: Democratic Authorization

**Question: Does the Agora approve?**

No layer is added to the architecture without democratic authorization. The proposal must be presented to the community through the Agora — the democratic deliberation layer — and must receive affirmative authorization through whatever deliberation mechanism the community has established.

This is not a rubber stamp. The democratic authorization process exists because the architecture serves the polis, not the other way around. A technically perfect layer that the community does not want is a layer that should not be deployed. Democratic legitimacy is not an inconvenience to be managed; it is the source of constitutional authority.

**Output**: A record of the democratic authorization vote, including the deliberation record, the vote tally, and any conditions or amendments attached to authorization.

### Step 10: Graduated Deployment

**Question: How does the new layer enter reality?**

Even after authorization, the new layer is not deployed universally. It follows a graduated deployment protocol:

1. **Shadow mode** — The layer runs in parallel with existing systems, processing real inputs but producing no real outputs. Its behavior is monitored for unexpected effects.
2. **Pilot deployment** — The layer is deployed in a limited jurisdiction (a single municipality, for example) with full monitoring and instant rollback capability.
3. **Expanded deployment** — If the pilot produces acceptable outcomes, deployment is gradually expanded with continued monitoring.
4. **Full deployment** — Only after successful expanded deployment is the layer considered fully operational.

At every stage, the rollback criterion is clear: if the layer produces constitutional violations, capture vulnerabilities, or outcomes worse than the status quo, it is rolled back. No layer has a right to exist; it earns its place through demonstrated performance.

**Output**: A deployment record with monitoring data, rollback assessments, and final deployment confirmation.

---

## Layer Proposal Template

When submitting a formal layer proposal, use the following structure:

```markdown
# Layer Proposal: [Layer Name]

## Proposer
- Name:
- Affiliation:
- Date:

## 1. Gap Statement
[One paragraph identifying the uncovered material reality]

## 2. Literature Review
[Minimum 2,000 words with full citations]

## 3. Constitutional Compatibility
### 3.1 Guardrail Compliance
- Guardrail 1 (No Omniscience): [Compliance argument]
- Guardrail 2 (No Total Behavioral Prediction): [Compliance argument]
- Guardrail 3 (No Centralized Social Engineering): [Compliance argument]
- Guardrail 4 (No Unrestricted Computational Control): [Compliance argument]

### 3.2 Human-Reserved Domain Compliance
- Religion and Spirituality: [Compliance argument]
- Culture and Identity: [Compliance argument]
- Family Structure: [Compliance argument]
- Moral Interpretation: [Compliance argument]
- Artistic Expression: [Compliance argument]
- Personal Identity: [Compliance argument]

## 4. Module Map Extension
| Civic Domain | Primary Modality | Rationale |
|-------------|-----------------|-----------|
| [Domain] | [Modality] | [Why this modality matches] |

## 5. Dependency Analysis
### 5.1 Upstream Dependencies
[Layers this layer depends on]

### 5.2 Downstream Dependencies
[Layers that depend on this layer]

### 5.3 Lateral Interactions
[Interactions with peer layers]

### 5.4 Dependency Graph
[Visual or textual representation]

## 6. Formal Specification
[Lean 4 specification file, attached separately]

## 7. Sandbox Results
[Experiment report following the sandbox guide format]

## 8. Community Review Record
[Summary of objections, challenges, and resolutions]

## 9. Democratic Authorization
[Vote record and deliberation summary]

## 10. Deployment Plan
[Graduated deployment protocol with rollback criteria]
```

---

## Potential Future Layers

The following domains have been identified as candidates that may eventually warrant their own layers, should material reality and scholarly consensus converge:

- **Meta-Governance** — The governance of governance itself: how the architecture modifies its own rules, updates its constitutional constraints, and adjudicates conflicts between layers. Currently distributed across the Governance layer (Layer 3) and the Ark layer (Layer 10), meta-governance may eventually require its own layer as the architecture matures and self-modification becomes more frequent.

- **Space Infrastructure** — Currently a subdomain of the Ark layer (Layer 10), space governance may become a full layer as humanity's off-world presence grows. The Mars Governance Protocol already exists in the specification; a dedicated layer would address the unique challenges of governing environments where the physics is different, the distances are vast, and the latency between Earth and colony makes real-time coordination impossible.

- **Consciousness and Cognition** — As brain-computer interfaces, neural augmentation, and artificial consciousness advance, the boundary between human cognition and computational systems will blur. This may require a layer that addresses the governance of cognitive augmentation, the rights of augmented persons, and the constitutional constraints on cognitive surveillance.

- **Inter-Civilization Coordination** — If multiple Algorapolis-compatible civilizations emerge (on Earth, Mars, or elsewhere), a layer may be needed to govern the relationships between them — a meta-layer for civilizational pluralism and propagation.

These are speculative. None should be proposed until the prerequisites — deep understanding, literature review, demonstrated gap — are met. They are listed here to illustrate the kinds of domains that might, in the fullness of time, justify constitutional extension.

---

## Warning: The Layer Proliferation Risk

The temptation to add layers is understandable. Each layer represents a domain someone cares deeply about. Education advocates will argue that Education deserves its own layer. Health advocates will argue the same for Health. Environmental justice advocates will make the case for Climate. And each argument will have merit — these domains *are* fundamental.

But the ten-layer stack is not a ranking of importance. It is a mapping of *governance modality dependencies*. Education is governed by democratic deliberation (curriculum) and meritocratic selection (teacher competence) — modalities already present in the Governance and Economics layers. Health is governed by hybrid algorithmic-democratic modalities — also present. A separate Education layer would not add a new modality; it would duplicate existing ones, creating jurisdictional conflicts, coordination overhead, and new capture vectors.

The layer proliferation risk is not hypothetical. The European Union's institutional architecture — with its proliferating directorates, agencies, and committees — demonstrates what happens when organizational boundaries expand without discipline: nobody understands who is responsible for what, democratic accountability dissipates across diffuse institutions, and lobbying capture becomes easier because there are more entry points.

**The test for a new layer is not "Is this domain important?" but "Does this domain require a governance modality that the existing layers cannot provide?"** If the answer is no, the domain should be governed within an existing layer, not elevated to a new one.

---

## The Non-Linear Continuity Principle Applied to Layer Evolution

The Non-Linear Continuity principle — drawn from the Ark Protocol and the broader philosophy of civilizational propagation — states that civilization does not evolve through smooth, continuous change but through punctuated equilibria: long periods of stability interrupted by rapid, discontinuous shifts.

Applied to layer evolution, this principle has two implications:

1. **Layers should not be added incrementally.** A new layer should emerge when material reality changes discontinuously — when a new domain becomes governable, when a new technology creates a new category of civilization, or when a civilizational shock reveals a gap that the existing stack cannot fill. Adding a layer because it would be "nice to have" violates the principle; adding one because material reality has changed is consistent with it.

2. **Layers may become obsolete.** If material reality changes such that a domain no longer requires dedicated governance — because it has been subsumed by other domains, because the problem it addressed has been solved, or because the domain itself has transformed — the layer should be retired. The stack is not a monument; it is a living architecture. But layer retirement follows the same constitutional process as layer addition: formal specification, sandbox testing, democratic authorization, and graduated phase-out.

The ten-layer stack is designed for the material reality of the early twenty-first century. It will not be the right stack for the twenty-second. The process described in this guide is how the architecture adapts — not through casual revision, but through constitutional amendment that preserves the framework's integrity while acknowledging its incompleteness.

---

*"The ten layers are not arbitrary — each represents a fundamental domain of civilization. Adding a layer is a constitutional act. Treat it with the gravity it deserves."*
