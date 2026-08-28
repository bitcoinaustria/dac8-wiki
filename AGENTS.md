# AGENTS.md

This file contains the repository-specific rules for agents. Read [README.md](README.md) for orientation and [VISION.md](VISION.md) before making scope or editorial judgments.

## Project map

- `.wiki/raw/` contains immutable source records.
- `.wiki/wiki/` contains synthesized articles, references, topics, and theses.
- `.wiki/output/` contains standalone research reports.
- `legal-docs/` contains the underlying full legal documents and its index.

## Research and writing

- Optimize current work for the Austrian proceeding. Preserve European extensibility through a repeatable method, not premature abstractions or generalized Austrian conclusions.
- Use exact statutory terms. Define an ambiguous term where it first matters; do not substitute campaign shorthand for a legal definition.
- Separate enacted law, holdings, party arguments, strategic inference, and missing facts. This prevents advocacy claims from silently becoming evidence.
- Prefer official legislation, judgments, dockets, and institutional materials. Preserve adverse authority and procedural barriers because early negative findings save time and legal cost.
- Write to the artifact's purpose, not to the conversation that produced it. Treat audience, motivation, desired outcome, and examples as guidance for scope and emphasis, not automatic copy.
- Include only decision-relevant substance. Prefer precise, evidence-led language; state uncertainty at the relevant claim, and omit prompt restatement, workflow narration, generic filler, and unnecessary reader instructions.
- A short standalone research/no-legal-advice status line may remain in exported reports because those files can circulate without repository context.

## Wiki workflow

- Use the installed LLM Wiki workflow for ingest, compilation, output changes, and linting.
- Read `.wiki/_index.md` and the relevant category index before broader searches. Indexes are derived navigation; source files and frontmatter remain authoritative.
- Do not modify `.wiki/raw/` during normal compilation. Add source-backed synthesis to `.wiki/wiki/` and generated reports to `.wiki/output/`.
- Append `.wiki/log.md` for every wiki write; never rewrite previous log entries.

## Confidentiality

- Confidential emails, mandate communications, identities, private evidence, and prompt-only context MUST NOT enter the public repository without explicit authorization for the specific material.
- Such material may guide research questions, but agents must independently source public claims and avoid distinctive copied phrasing.
- Treat publication, commits, pushes, uploads, and external messages as separate actions requiring explicit authorization.

## Quality gates

After wiki changes, run the installed plugin CLI:

```sh
llm-wiki lint --local --fix
llm-wiki lint --local
```

If `llm-wiki` is not on `PATH`, resolve `bin/llm-wiki` from the installed plugin; do not commit a machine-specific absolute path.

Before handoff:

- verify all changed links and cited local documents;
- search changed artifacts for copied confidential prompt or email language;
- search reports for duplicated audience/purpose narrative;
- report any unverified current law, deadline, fee, or procedural assumption.

## Working agreements

- Multiple agents may research bounded questions in parallel; the primary agent integrates conflicts and preserves source provenance.
- Keep changes narrow and reviewable. Preserve unrelated concurrent work.
- Do not create commits, publish the repository, or mutate external systems unless the user explicitly asks.
