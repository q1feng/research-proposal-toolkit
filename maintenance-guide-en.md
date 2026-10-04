# Maintenance guide

[简体中文](maintenance-guide-zh.md) · [Home](README.md)

## Responsibilities and changes

The language-specific `research-proposal-toolkit-en` and `research-proposal-toolkit-zh` folders are installable Skills. SKILL.md handles discovery, routing, and boundaries; references hold detailed rules; agents/openai.yaml holds UI text. Ordinary files rely on language directories rather than repeated suffixes. Root-level bilingual documents retain suffixes. Generated portable guides must not be edited separately.

Describe the concrete failure and intended decision change before editing a module. Avoid accumulating warnings or unnecessary files. Maintain structural, capability, and exception parity manually across languages using natural wording; the builder does not translate. Users may replace disciplinary, institutional, or tool-specific components while preserving question–evidence–decision traceability.

## Build and check

Use Python 3.10 or newer; scripts require only the standard library:

```sh
python scripts/build_guides.py
python scripts/build_guides.py --check
python scripts/validate_structure.py
```

Use `--language en` or `--language zh` for one edition. Checks cover names, the simple YAML/JSON fields used here, UI text, language modules, reference routing, links, generated-file consistency, and selected sensitive patterns. CITATION.cff uses JSON-compatible YAML without invented DOI, release date, or version metadata.

These checks do not validate full YAML/CFF schemas, semantic translation equivalence, citation truth, or research quality. Run an official Skill validator when available. Report actual inputs, outputs, and limitations of behavioral tests; a rule walkthrough is not an execution trial.

## Research regression and release

Review broad wishes, existing answers, counterevidence, theoretical/qualitative work, excessive scope, explicitly authorized revision, and offline use. Workflow checks also include summary stacking, inconsistent drafts, template conflicts, missing full text, and unverified metrics. Repair research judgments and structure before wording.

Public files must contain generic methods or authorized material, not cases extracted from private research, conversations, or sample reports. Isolate suspicious material and flag it rather than propagating it. Scripts do not rewrite Git history. Manually review privacy and rights before release and inspect README, usage, Skill, and portable-guide entry points.

CHANGELOG records capabilities and academic reasons; usage guides omit development history. Preserve the MIT license and attribution. Maintainers manage version tags and GitHub About text; the package does not publish, change account settings, or update installed copies automatically.

## Forge core synchronization

The five same-language modules under references/forge/ are embedded from upstream. forge-core-sync.json records the source repository, content snapshot ID, and per-file SHA-256 hashes. The content version is not presented as a nonexistent release tag. MIT attribution remains in the license.

With a local Forge checkout, explicitly run:

```sh
python scripts/sync_forge_core.py --source ../research-question-forge --check
python scripts/sync_forge_core.py --source ../research-question-forge
python scripts/build_guides.py
python scripts/validate_structure.py
```

After synchronization, review integration, writing, and citation rules rather than independently evolving embedded copies. Standalone distribution does not require an adjacent Forge checkout; only explicit synchronization or cross-repository checking needs that path.
