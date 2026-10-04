# Research Proposal Toolkit

English | [简体中文](README-zh.md)

> **From research questions to a complete proposal workflow.**

Built on [Research Question Forge](https://github.com/q1feng/research-question-forge), Research Proposal Toolkit develops early ideas into evidence-grounded literature reviews and complete proposal drafts. It connects question formation, literature synthesis, evidence tracking, research design, and iterative revision.

Use it as-is, or as a reference architecture for composing your own research workflow.

[Start without installation](en/proposal-guide.md) · [Install the Skill](en/usage.md) · [中文使用](zh/usage.md)

## What this toolkit is

A guided workflow for graduate research proposals, with a master's scope by default and adaptation to other degrees and disciplines. You can start with a rough observation, an existing framework, or drafts that need revision. Institutional requirements take precedence.

Its deliverable is readable prose with traceable evidence, not just forms or a collection of paper summaries. You can request the full workflow or a single stage.

## Built on Research Question Forge

Forge provides question formation, literature feedback, expansion and decomposition, and a structured research framework. The Toolkit continues into synthesis, citation auditing, research design, and coordinated review/proposal writing.

This repository is one complete workflow built on Forge, not the only way Forge can be used. It includes a tracked core snapshot so a separate installation is unnecessary.

## End-to-end workflow

```text
Observation / ideas → Forge → Research framework
                                      ↕
                       Search / reading ↔ Evidence audit
                                      ↕
                    Literature synthesis ↔ Research design
                                      ↓
                       Literature review ↔ Research proposal

New evidence / feedback ──→ Question abstraction (Forge)
                        ├─→ Expansion / decomposition (Forge)
                        └─→ Framework → Revise both drafts
                        ╌╌→ Rethink observation, ideas,
                            and how questions are formed
```

Solid arrows show direct progress and revision: new evidence and feedback can reshape question abstraction, expansion or decomposition, and the research framework together. Dashed arrows show deeper epistemological reflection: why certain phenomena draw our attention, how we observe and interpret them, which assumptions shape our ideas, and how observations become questions. Both forms of feedback can recur throughout the work, before a framework or draft is complete.

The loop can return to the question when literature, resources, or supervisor feedback changes its basis. It is not a one-shot title-to-report generator.

## Core outputs

| File | Purpose |
|---|---|
| research-framework.md | Question, scope, prior work, directions, design, decisions, open issues |
| citation-ledger.md | Source identity, reading depth, claim support, locations, limits, substantive analysis |
| literature-review.md | Thematic synthesis of knowledge, differences, disputes, and unresolved questions |
| research-proposal.md | Rationale, objectives, content, methods, evidence plan, feasibility, schedule, expected contributions |

Reuse equivalent existing files. Detailed task briefs are optional. The default review target is about ten A4 pages of body text, excluding front matter, bibliography, and audit; pagination is verified only after layout.

## How the two drafts stay aligned

Both drafts share questions, definitions, closest work, evidence, unresolved issues, and methodological assumptions. The review develops understanding of the field; the proposal develops the intended study. Background and comparisons can be reused with their sources and qualifications.

A substantive change prompts a check of the framework, evidence record, and other draft. Stable source IDs survive changes in citation numbering. Proposed work never becomes a completed result merely through rewriting.

## Iterative research and writing

New sources test the question and comparison baselines. Synthesis precedes prose; structure and evidence precede polishing. A review explains differences and forms bounded judgments rather than stacking abstracts. A proposal connects questions to methods and evidence rather than listing implementation steps.

Respect the user's sequence, including review first, further reading, then proposal. The researcher chooses substantial redirection after seeing options and rework costs.

## Use it as-is or compose your own workflow

This toolkit incorporates selected core mechanisms from literature-review and research-proposal Skills, while treating composition as a central principle. Users are encouraged to discover and choose literature-search, research-framework revision, academic editing, and paper-writing Skills suited to their discipline, research stage, and deliverables, building a workflow of their own. Figure-creation and presentation Skills are also possible extensions, but these integrations have not yet been tested with this toolkit. Additional Skills are optional; the toolkit and portable guide remain usable on their own.

Replace search, paper reading, citation management, study design, coding, analysis, writing, or layout with your own tools or Skills. Each handoff carries the question, confirmed context, source requirements, uncertainty, and allowed scope. No specific model, API key, or community suite is required.

The portable guide also serves as a reference for designing a workflow without installing this package. Actual retrieval, computation, and document export depend on host capabilities.

## Quick start

Attach the [portable guide](en/proposal-guide.md), or install the complete [English Skill folder](en/research-proposal-toolkit-en/SKILL.md) in a supported client. Retain its references and metadata.

> Use $research-proposal-toolkit-en. My field and degree are …; my idea, sources, and resources are …. Help me frame the question, compare the literature, and draft a standalone review before the proposal. Discuss substantive changes with me.

Provide your institution's requirements and optional style samples. See [usage](en/usage.md) and the optional [citation-audit template](en/citation-audit-template.md).

## Research principles

- Never invent sources, reading, results, resources, achievements, or novelty.
- Separate direct evidence, indirect support, inference, and proposed work.
- Preserve counterevidence, disciplinary differences, and researcher choice.
- Keep internal process notes outside formal prose without hiding scholarly uncertainty.
- A complete draft is not a completed study; human review remains necessary.

## Project structure and participation

Each language has usage documentation, a portable guide, a citation template, and an independently installable Skill. The bundled Forge rules have recorded hashes; scripts check snapshot consistency, links, structure, and generated guides without claiming semantic or scholarly validation.

[Contributing](CONTRIBUTING.md) · [Changes](CHANGELOG.md) · [Maintenance](maintenance-guide-en.md) · [Citation](CITATION.cff) · [MIT license](LICENSE)

## Acknowledgments

We thank [nature-skills](https://github.com/Yuan1z0825/nature-skills) and [Research-Starter-Kit](https://github.com/LAMDA-NeSy/Research-Starter-Kit) for openly sharing academic tools and research practices. These projects offer valuable reference points and inspiration for exploring AI-assisted research workflows.

We hope that the ideas and methods explored here—for forming research questions, critically engaging with literature, and developing research proposals—can contribute to the growth of open-source academic tools and research skills, and continue to improve through community discussion, reuse, and collaboration.
