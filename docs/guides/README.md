# Guides

> **Practical handbooks for interacting with the Algorapolis framework** — Step-by-step instructions for proposing layers, running sandboxes, contributing case studies, and more.

---

## Introduction

The Algorapolis specification is a comprehensive architecture — ten layers of civilization, a Sovereign Logic Engine, constitutional constraints, governance modalities, and adversarial resilience patches. But architecture without practice is theory without consequence. These guides exist to bridge the gap between the specification and the people who must work with it: the researchers who extend it, the developers who implement it, the policy architects who test it, and the citizens who must ultimately live within it.

Each guide in this directory is a practical, actionable document. It does not repeat the specification — it operationalizes it. Where the specification says "Governance Sandboxes test policies on synthetic populations," the guide says "Here is how you run a Governance Sandbox, step by step, with tool recommendations, ethical considerations, and real-world constraints." Where the specification says "the ten layers are not arbitrary," the guide says "Here is the constitutional process for proposing an eleventh — and here is why you should think very carefully before doing so."

These guides are living documents. As the Algorapolis framework evolves through research, adversarial testing, and real-world deployment, so too will these guides. They are versioned alongside the specification and should always be read in conjunction with the relevant framework and manifesto sections they reference.

---

## Available Guides

| Guide | Description |
|-------|-------------|
| [**Proposing a New Civilization Layer**](./proposing-a-layer.md) | How to propose, specify, and defend a new layer for the ten-layer civilization stack. Covers constitutional compatibility, formal verification, sandbox testing, and democratic authorization. |
| [**Running a Governance Sandbox**](./running-a-sandbox.md) | How to configure, execute, and interpret a Governance Sandbox experiment. Covers synthetic population generation, simulation parameters, adversarial stress testing, and publishing results. |
| [**Contributing a Case Study**](./contributing-a-case-study.md) | How to research, write, and submit a governance case study that grounds the Algorapolis architecture in real-world evidence. Covers both positive and negative specifications. |

---

## Who These Guides Are For

These guides are written for anyone who engages with the Algorapolis framework as more than a reader:

- **Researchers** — Academics and independent scholars who want to extend the framework with new layers, test its assumptions through sandbox experimentation, or contribute empirical evidence through case studies. If you are writing a paper that engages with Algorapolis, these guides explain how to do so in a way that is consistent with the architecture's constitutional constraints.

- **Developers** — Engineers and technologists who want to implement components of the architecture — the Sovereign Logic Engine, Governance APIs, privacy infrastructure, or simulation tooling. The sandbox guide in particular provides concrete tool recommendations and technical workflows.

- **Policy Architects** — Governance practitioners, civil servants, and institutional designers who want to apply Algorapolis principles to real-world governance challenges. The sandbox guide is your primary resource: it explains how to test a policy before it affects real humans.

- **Governance Practitioners** — Activists, civil society organizations, and democratic innovators who want to understand how the framework's principles — the Matching Principle, the Four Guardrails, the Six Human-Reserved Domains — translate into actionable governance design.

- **Citizens** — Anyone who will live within governance systems shaped by this architecture. The guides are written in plain language with technical terms defined on first use. You do not need a degree in political science or computer science to follow them. If a guide is not accessible to an engaged citizen, it is a bug in the guide, not a feature.

---

## How to Propose a New Guide

The guide directory is not closed. If you identify a practical need that the existing guides do not address, you can propose a new one:

1. **Open an issue** using the [Research Proposal template](../../.github/ISSUE_TEMPLATE/research-proposal.md) in the repository's issue tracker.
2. **Title your issue** with the prefix `[Guide Proposal]` — for example: `[Guide Proposal] Implementing Privacy Infrastructure with ZKPs`.
3. **Describe the gap** — What practical task does this guide address? Who is it for? Which sections of the specification does it operationalize?
4. **Demonstrate demand** — Reference discussions, issues, or community questions that show the guide would be used.
5. **Outline the structure** — Provide a preliminary table of contents showing the guide's major sections.

Guide proposals are reviewed by maintainers and the community. A proposal is accepted when it addresses a genuine practical need, does not duplicate existing content, and is consistent with the framework's principles and tone.

---

## Relationship to Other Directories

```
algorapolis/
├── manifesto/          ← The philosophical argument (why)
├── framework/          ← The technical architecture (what)
├── research/           ← The scholarly foundation (evidence)
└── docs/
    └── guides/         ← The practical handbooks (how) ← YOU ARE HERE
```

- **[manifesto/](../../manifesto/)** — The manifesto articulates *why* Algorapolis exists: the Logic Heartbreak, the core principles, the African context, and the future declaration. Guides reference the manifesto for foundational justification but do not repeat its arguments.
- **[framework/](../../framework/)** — The framework specifies *what* Algorapolis is: the ten-layer stack, the SLE, the Module Map, the Governance Sandbox Architecture. Guides operationalize the framework's specifications into step-by-step instructions.
- **[research/](../../research/)** — The research directory provides the *evidence*: studies, case studies, and bibliography. Guides reference research for empirical grounding; the case study contribution guide explains how to add to this evidence base.

The relationship is circular: the manifesto provides the motivation, the framework provides the architecture, the research provides the evidence, and the guides provide the practice. Practice reveals gaps, which motivate new research, which refines the framework, which updates the guides.

---

## Language Accessibility

Algorapolis originates from Tanzania, and its author writes in English as a global lingua franca — not as a native language. The framework's concepts are deeply informed by Swahili-speaking, East African governance experience. This creates a linguistic asymmetry: the people whose experience most shaped the architecture may have the most difficulty accessing it.

**Swahili translations of these guides are planned.** If you can contribute to translation efforts — whether for Swahili or any other language — please open an issue or contact the maintainers. The framework's commitment to civilizational pluralism and linguistic diversity (see Layer 7 — Culture, Section on Language and Communication) begins at home: the documentation itself must be accessible.

In the interim, all guides are written with the following commitments:

- **Plain language first** — Technical terms are defined on first use. Jargon is avoided unless it is the precise term of art.
- **Examples over abstractions** — Where possible, concepts are illustrated with concrete examples rather than left at the theoretical level.
- **Progressive depth** — Each guide begins with what you need to know to get started and introduces complexity only when it becomes necessary for the task at hand.

---

*"Algorapolis is offered as a foundation, not a conclusion. These guides are offered as pathways, not walls. Walk them, improve them, and build new ones where the terrain demands it."*
