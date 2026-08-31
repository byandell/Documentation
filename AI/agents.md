---
title: "Agents and Workspace Rules"
parent: "AI (Artificial Intelligence)"
nav_order: 6
---

# Agents and Workspace Rules

- [What is an `AGENTS.md` File?](#what-is-an-agentsmd-file)
- [Comparing `README.md`, `DEVELOPER.md`, and `AGENTS.md`](#comparing-readmemd-developermd-and-agentsmd)
- [Cascading Hierarchy: User, Project, and Subfolder](#cascading-hierarchy-user-project-and-subfolder)
  - [User-Level Rules (`~/.agents/AGENTS.md`)](#user-level-rules-agentsagentsmd)
  - [Project-Level Rules (`./AGENTS.md` & `.agents/`)](#project-level-rules-agentsmd--agents)
  - [Subdirectory / Monorepo Rules](#subdirectory--monorepo-rules)
- [What to Include at Each Level](#what-to-include-at-each-level)
- [Real-World `AGENTS.md` Examples](#real-world-agentsmd-examples)
- Additional Pages
  - [Context Engineering](context.md)
  - [Prompt Engineering](prompt.md)

## What is an `AGENTS.md` File?

An [`AGENTS.md`](https://agents.md/) file serves as the **onboarding handbook** for an AI coding assistant entering a repository. It provides the agent with project context, architectural boundaries, coding preferences, and operational rules so that it behaves like an experienced human collaborator. See
[What Is AGENTS.md? How to Write One in 2026 (Tembo)](https://www.tembo.io/blog/agents-md).

> [!NOTE]
> **Context Budget Caution**: `AGENTS.md` is automatically loaded into the AI agent's context window on every turn. Keep it concise, imperative, and focused on essential constraints to avoid filling up the token budget.

## Comparing `README.md`, `DEVELOPER.md`, and `AGENTS.md`

Documentation is stratified by audience and purpose:

| Document | Primary Audience | Core Focus | Style & Scope |
| --- | --- | --- | --- |
| **`README.md`** | Users & contributors | Project overview, installation, and quick start | High-level, welcoming |
| **`DEVELOPER.md`** | Human developers | Architecture, system design, and module boundaries | Conceptual, diagram-heavy |
| **`AGENTS.md`** | AI coding agents | Mandatory constraints, conventions, and test commands | Strict, concise, imperative |

## Cascading Hierarchy: User, Project, and Subfolder

AI instructions operate under a cascading hierarchy where more specific rules override broader baselines:

### User-Level Rules (`~/.agents/AGENTS.md`)

Sets universal developer habits, safety boundaries, and global preferences across all projects on your machine.

- **Single Source of Truth**: Use `~/.agents/AGENTS.md` (or `~/.gemini/config/AGENTS.md` for Gemini / Antigravity).
- **Tool Bridging**: Symlink vendor-specific config files back to your canonical standard file if needed:

  ```bash
  mkdir -p ~/.gemini/config ~/.claude
  ln -s ~/.agents/AGENTS.md ~/.gemini/config/AGENTS.md
  ln -s ~/.agents/AGENTS.md ~/.claude/CLAUDE.md
  ```

### Project-Level Rules (`./AGENTS.md` & `.agents/`)

- **Root `AGENTS.md` (Standard)**: Visible to GitHub browsers and recognized by tools like Antigravity, Claude Code, Cursor, and Copilot.
- **`.agents/` Folder (Workspace Root)**: A hidden configuration directory used by agent harnesses (like Antigravity) for skills (`.agents/skills/`) and rules. If using both, make `.agents/AGENTS.md` a simple pointer:

  ```markdown
  # Project AI Guidelines
  See [AGENTS.md](../AGENTS.md) at the repository root.
  ```

### Subdirectory Rules

Nested `AGENTS.md` files (e.g., in `packages/core/AGENTS.md` or `quarto/AGENTS.md`)
apply targeted constraints to specific subdirectories without cluttering the
top-level project rules.

## What to Include at Each Level

### User-Level (`~/.agents/AGENTS.md`)

- **Safety Boundaries**: No committing secrets/`.env`, ask before destructive edits.
- **Git Conventions**: Commit message format, branch naming, no automated push.
- **Communication Tone**: Concise responses, complete drop-in diffs.
- **Coding Style Defaults**: Type hinting, docstring conventions.

### Project-Level (`./AGENTS.md`)

- **Project Structure**: Key directory layouts and component paths.
- **Verification Commands**: Build and test suites (`quarto render`, `pytest`, `R CMD check`).
- **Domain Conventions**: Package namespacing, specific data schemas.
- **Version Rules**: Handling legacy files or migration patterns.

## Real-World `AGENTS.md` Examples

- [Documentation `AGENTS.md`](../AGENTS.md): Site structure, Quarto rendering conventions, and multi-version commit workflows.
- [Working Group OASIS](https://github.com/CU-ESIIL/Working_group_OASIS/blob/main/AGENTS.md) (CU ESIIL): Guidelines for collaborative research agents.
- [LLM Lesson Exemplar](https://github.com/CU-ESIIL/LLM_lesson_exemplar/blob/main/AGENTS.md) (Cassie Buhler): Script headers, regional boundary rules, and failure handling.
- [OASIS ScienceClaw `openclaw_container`](https://github.com/CU-ESIIL/openclaw_container/blob/main/AGENTS.md): Core operating contract, data sovereignty policy, and testing protocols.
