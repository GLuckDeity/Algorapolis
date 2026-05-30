# Assets

Visual and design assets for the **Algorapolis** project — a modular governance architecture that aligns the Rule of Logic (Algo) with the Public Assembly (Agora) to secure the Common Good (Polis).

---

## Purpose

This directory contains visual and design assets that support the understanding, communication, and branding of the Algorapolis framework. Assets range from technical architecture diagrams to brand identity materials, all serving the goal of making Algorapolis's complex multi-layer architecture accessible to diverse audiences — from governance researchers and software engineers to policymakers and citizens.

---

## Directory Structure

```
assets/
├── diagrams/            # Technical architecture and system diagrams
│   ├── civilization-stack/    # Ten-layer stack visualizations
│   ├── operational-arch/      # Four-layer operational architecture
│   ├── module-map/            # Civic domain governance modality mappings
│   ├── privacy-architecture/  # ZKP tiers, differential privacy flows
│   └── vsm-integration/       # Viable System Model mappings
├── logos/               # Project logos and wordmarks
├── presentations/       # Slide decks and presentation materials
└── badges/              # Status badges, shields, and contribution markers
```

---

## Asset Naming Conventions

All assets must follow these naming conventions:

| Pattern | Example | Notes |
|---------|---------|-------|
| `{category}-{descriptor}-{variant}.{ext}` | `diagram-civilization-stack-light.svg` | Use lowercase with hyphens |
| `{category}-{descriptor}-{size}.{ext}` | `logo-algorapolis-512px.png` | Specify dimensions for raster assets |
| `{category}-{descriptor}-{lang}.{ext}` | `diagram-module-map-sw.svg` | Append ISO 639-1 code for translations |
| `{category}-{descriptor}-{version}.{ext}` | `diagram-operational-arch-v2.svg` | Version major structural changes |

**Rules:**
- Use only lowercase letters, digits, and hyphens in filenames
- Prefer SVG for all diagrams and logos (scalable, accessible, version-controllable)
- Provide PNG exports at 1x and 2x resolution for raster-only contexts
- Include source files (e.g., Figma, Draw.io, Excalidraw) alongside exports where applicable
- Never include spaces, special characters, or camelCase in filenames

---

## License

All assets in this directory are released under **Creative Commons Attribution-ShareAlike 4.0 International (CC-BY-SA 4.0)** unless otherwise noted in the file header.

- You are free to share, adapt, and build upon these assets
- You must give appropriate credit to the Algorapolis project
- Derivatives must be distributed under the same license
- Full license text: https://creativecommons.org/licenses/by-sa/4.0/

Code-related diagrams (e.g., architecture specifications encoded in code) may additionally be available under the MIT license where they appear in the codebase. When in doubt, check the file header.

---

## Contribution Guidelines

We welcome contributions of visual assets that help communicate the Algorapolis architecture. Please follow these guidelines:

### Submission Process

1. **Open an issue** describing the asset you intend to create before starting work
2. **Follow the naming conventions** defined above
3. **Provide source files** alongside any exported/rendered assets
4. **Include a text description** (see Accessibility below)
5. **Submit via pull request** with the asset in the appropriate subdirectory
6. **Certify compatibility** with CC-BY-SA 4.0 licensing

### Quality Standards

- Diagrams must be technically accurate and consistent with the current specification
- Use the project color palette (see below) for brand consistency
- Text in diagrams must be legible at both thumbnail and full resolution
- All exported SVGs must pass W3C validation
- Avoid proprietary font dependencies; prefer system fonts or open-source typefaces

### Color Palette (Recommended)

| Role | Hex | Usage |
|------|-----|-------|
| Primary | `#1B4332` | Core Algorapolis brand (deep green — growth, stability) |
| Secondary | `#2D6A4F` | Supporting elements |
| Accent | `#40916C` | Highlights, interactive elements |
| Warm | `#D4A373` | Extended layers, cultural warmth |
| Alert | `#E63946` | Warnings, guardrails |
| Background | `#FEFAE0` | Light backgrounds |
| Neutral Dark | `#2B2D42` | Text, borders |
| Neutral Light | `#8D99AE` | Secondary text, dividers |

All color combinations must pass WCAG 2.1 AA contrast requirements (minimum 4.5:1 for normal text, 3:1 for large text).

---

## Current Status

**This directory is currently empty.** Visual assets will be added as the project develops its brand identity and diagram library.

---

## Requested Contributions

We are actively seeking contributions for the following asset categories:

### Architecture Diagrams

- **Ten-layer civilization stack** — A clear, hierarchical visualization showing the six core layers (Philosophy → Psychology → Governance → Economics → Technology → Security) and four extended layers (Culture → Ecology → Civilization → Ark), with inter-layer dependencies and governance modality indicators
- **Four-layer operational architecture** — Foundational Infrastructure → Reasoning & Simulation → Testing & Validation → Operational Coordination, with component mappings
- **Module Map visualization** — The twelve civic domains with their governance modality assignments, showing the Matching Principle in action
- **SLE architecture** — Internal structure of the Sovereign Logic Engine showing the five properties, formal verification pipeline, and constitutional constraint enforcement
- **Privacy architecture** — The tiered ZKP system (Groth16 → PLONK → Halo 2), differential privacy flows, and homomorphic encryption boundaries

### Layer Visualization

- Individual layer diagrams showing subdomains, dependencies, and constitutional constraints
- Cross-layer dependency graphs
- Governance modality distribution heat map across layers

### Civilization Stack Infographic

- A comprehensive, publication-ready infographic suitable for academic papers, presentations, and public communication
- Should clearly convey: the ten layers, the core/extended distinction, the Matching Principle, the constitutional guardrails, and the human-reserved domains

### Logo Concepts

- **Algorapolis wordmark** — Incorporating the three morphemes (Algo + Agora + Polis)
- **SLE icon** — A symbol for the Sovereign Logic Engine that conveys constrained, auditable computation
- **Civic domain icons** — Twelve icons representing each domain in the Module Map
- **Guardrail icons** — Four icons representing the constitutional guardrails

### African-Inspired Governance Iconography

Algorapolis originates from Tanzania and is designed with African governance contexts as a primary use case. We seek visual elements that:

- Draw inspiration from African geometric patterns, textiles (kanga, kitenge), and architectural forms (e.g., Swahili coral stone, Great Zimbabwe)
- Incorporate pan-African color symbolism where appropriate (without reducing to stereotype)
- Reflect the Swahili model of multilingual, pluralistic coexistence that the architecture references
- Avoid exoticization or appropriation — contributors from African design traditions are especially encouraged
- Maintain technical precision and clarity (these are specification diagrams, not decorative art)

---

## Accessibility Requirements

All visual assets must meet the following accessibility standards:

### Diagrams

- **Text descriptions**: Every diagram must include a comprehensive text alternative that conveys the same information as the visual. Place descriptions in an adjacent `.alt.txt` file or within the SVG `<desc>` element.
- **Color-blind friendly palettes**: Never rely solely on color to convey information. Use patterns, shapes, labels, and textures as redundant encoding. Test all diagrams with Coblis or similar color blindness simulators.
- **Scalable text**: All text in SVGs must remain legible when zoomed to 200%. Use relative units (em, %) where possible.
- **High contrast**: All diagram elements must meet WCAG 2.1 AA contrast requirements.

### Presentations

- Include speaker notes for all slides
- Provide text transcripts for any embedded audio/video
- Ensure slide content is readable without visual context

### General

- Provide alt text for all raster images
- Use semantic structure in SVGs (title, desc, group labels)
- Avoid flashing or rapidly animating elements (WCAG 2.3)
- Test assets with screen readers where applicable

---

## Cultural Sensitivity

Algorapolis is a governance framework that explicitly protects cultural identity, religion, artistic expression, and personal identity as human-reserved domains. Visual assets must reflect these commitments:

- **No stereotypical or reductive depictions** of any culture, religion, or ethnic group
- **No iconography that implies surveillance or control** over individuals — Algorapolis is structurally opposed to both
- **Respect for religious and spiritual symbolism** — avoid co-opting sacred symbols for branding purposes
- **Inclusive representation** — imagery should reflect the global and pluralistic aspirations of the architecture
- **African authorship visibility** — Algorapolis originates from an independent Tanzanian researcher; visual assets should not erase or obscure this context
- **Avoid techno-utopian aesthetics** that contradict the Civilizational Humility principle (the framework is permanently incomplete, not a perfect civilization)

When in doubt about whether an asset is culturally appropriate, err on the side of caution and seek review from community members with relevant cultural knowledge.

---

*"Algorapolis is offered not as a perfect civilization but as an adversarially hardened, permanently incomplete, and self-correcting architecture."*