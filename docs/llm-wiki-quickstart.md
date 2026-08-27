# LLM Wiki quickstart

This repository uses [NVK's LLM Wiki](https://github.com/nvk/llm-wiki), an MIT-licensed, Markdown-native research and knowledge-base workflow for AI agents. Sources, compiled articles, and reports live in the project-local [`.wiki/`](../.wiki/) directory.

## 1. Clone this repository

Access to the private GitHub repository is currently required.

```sh
git clone https://github.com/bitcoinaustria/dac8-wiki.git
cd dac8-wiki
```

Install the plugin for either Codex or Claude Code. Both agents automatically select this repository's `.wiki/` when started from the repository root.

## 2A. Install for OpenAI Codex

```sh
codex plugin marketplace add nvk/llm-wiki
codex plugin add wiki@llm-wiki
```

Start a new Codex thread in this directory after installation. Enter wiki requests in the Codex chat, not in the shell:

```text
@wiki show the status of the local wiki
$wiki-query "What does the wiki say about G 178/2024?"
@wiki research "Austrian DAC8 procedural developments"
@wiki ingest https://example.com/source
```

- `$wiki-query` is the small, read-only lookup path.
- `@wiki` is the full research and maintenance workflow.
- Automated session capture is optional. Review the bundled hooks in `/hooks` before trusting them.

Update later with:

```sh
codex plugin marketplace upgrade llm-wiki
codex plugin add wiki@llm-wiki
```

Restart Codex if an existing thread does not detect the changed plugin state.

## 2B. Install for Claude Code

Add the marketplace, install the plugin, and reload plugins:

```sh
claude plugin marketplace add nvk/llm-wiki
claude plugin install wiki@llm-wiki
```

Inside Claude Code, run:

```text
/reload-plugins
/wiki
/wiki:query "What does the wiki say about G 178/2024?"
/wiki:research "Austrian DAC8 procedural developments"
/wiki:ingest https://example.com/source
```

Update later with:

```sh
claude plugin update wiki@llm-wiki
```

Then run `/reload-plugins` or restart Claude Code.

## 3. Work safely in this repository

Read [`AGENTS.md`](../AGENTS.md) before changing the wiki. In particular:

- query before launching new research;
- preserve official sources, adverse authority, and provenance;
- do not edit `.wiki/raw/` during normal compilation;
- keep confidential mandate material and prompt-only context out of Git;
- do not commit or publish without explicit authorization.

After wiki changes, ask the installed LLM Wiki plugin to lint the local wiki and fix mechanical issues. Review the resulting diff before committing.

## Upstream documentation

- [NVK/llm-wiki repository and complete command reference](https://github.com/nvk/llm-wiki)
- [LLM Wiki website](https://llm-wiki.net/)
- [Claude Code plugin marketplace documentation](https://code.claude.com/docs/en/discover-plugins)
