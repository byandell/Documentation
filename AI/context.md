## AI Context Engineering

- [What is Context Engineering?](#what-is-context-engineering)
- [Context Engineering References](#context-engineering-references)
- [Comparison of Agent Skills and AGENTS.md](#comparison-of-agent-skills-and-agentsmd)
  - [AGENTS.md (Repository Context)](#agentsmd-repository-context)
  - [Agent Skills / SKILL.md (Actionable Capabilities)](#agent-skills--skillmd-actionable-capabilities)
  - [Summary of Differences](#summary-of-differences)

## What is Context Engineering?

A conversation with an AI agent involves a chain of prompts and their responses,
which over time fill up an agent's limited attention budget,
otherwise known as the `context window`.
At some point the AI agent runs out of gas and
either cannot proceed or starts hallucinating,
and we might consider moving to a new conversation.
Curating the material passed to an AI agent, including prompts
and shared documents, is known as `context engineering`.

Simply put, we should design our conversations
so that they are sufficiently focused to achieve our goal.
For instance, limit unnecessary background information, and limit the size of documents we
ask the AI agent to ingest.
It is better to ask an AI agent to summarize a document
than to have it read and retained,
and then perhaps save that summary
for use in subsequent conversations.

Project-level systems instructions and agent skills,
project context, etc.
can be built into a project's
"README for agents" called
[AGENTS.md](https://agents.md/).
The challenge with `AGENTS.md` is that it is automatically loaded into the
context window by AI agents working in the project.
Hence, it already fills up part of the context window,
limiting space for your conversation prompts and results.
One solution is to have a concise `AGENTS.md`
(with perhaps a more detailed `AGENTS-LONG.md` loaded when needed)
This works well as long as the concise version is sufficient.

Another trick is to use `agent skills` located
in one or more `skills` folders, each containing a `SKILL.md` file.
These are reusable packages of knowledge that extend what an agent
can do to handle different aspects of a project.

## Context Engineering References

- [Agent Skills for Context Engineering (Murat Cankoylan)](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering)
- [Antigravity Agent Skills](https://antigravity.google/docs/skills)
- [Antigravity Skills (CodeLabs)](https://codelabs.developers.google.com/getting-started-google-antigravity#8)
- [Claude Skills](https://claude.com/skills)
- [Anthropic Skills](https://github.com/anthropics/skills)
& [Anthropic Context Engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents).
- [AgentSkills.io](https://agentskills.io/home)
- [GitHub Topics: agent-skills](https://github.com/topics/agent-skills)

## Comparison of Agent Skills and AGENTS.md

Based on the technical paradigms for AI coding assistants (such as Claude Code, GitHub Copilot, Cursor, and Codex), **Agent Skills** (or `SKILL.md`) and **`AGENTS.md`** are two complementary standards used to provide context and capabilities to AI agents.

A comparative breakdown highlights their distinct roles, structures, and intended use cases:

| Feature | `AGENTS.md` | Agent Skills (`SKILL.md`) |
| --- | --- | --- |
| **Primary Purpose** | Defines **repository-specific context** (tech stack, coding standards, project layout, architecture rules). | Packages **procedural knowledge** or actionable automation capabilities (how to deploy, audit, generate code, or test). |
| **Scope** | Bound to a specific codebase/repository (Static local context). | Portable across different repositories and platforms (Reusable "recipes"). |
| **Core Components** | A single Markdown file matching the [agents.md specification](https://agents.md). | A folder structure containing `SKILL.md` (frontmatter + rules) and optional automation scripts (Bash, Python, Node). |
| **Trigger Mechanism** | Loaded automatically when an agent begins working inside that repository. | Activated dynamically on-demand when the agent recognizes a relevant trigger phrase or task. |

---

### `AGENTS.md` (Repository Context)

Think of `AGENTS.md` as the **onboarding handbook** for an AI agent entering a specific project. It tells the agent _what_ the project is and _how_ it should behave to blend in seamlessly with human contributors.

- **Target Audience:** The AI agent working _inside_ that specific codebase.
- **Content Focus:**
  - Tech stack definitions (e.g., React 18, TypeScript, Tailwind).
  - Directory layout (where to find hooks, components, or API services).
  - Design tokens and rigid rules (e.g., _"Do not introduce new dependencies," "Prefer existing `Button` component"_).
- **Layering & Scope:** Can be nested. A root `AGENTS.md` might define company-wide standards, while a nested `services/api/AGENTS.md` layers on rules specific only to the backend service.

#### AGENTS.md Examples

See for instance these example AGENTS.md files with listed sections:

- [Working Group OASIS AGENTS.md](https://github.com/CU-ESIIL/Working_group_OASIS/blob/main/AGENTS.md) (CU ESIIL)
  - Guidelines for agents
  - Working Group OASIS and Project Group OASIS
- [LLM lesson exemplar AGENTS.md](https://github.com/CU-ESIIL/LLM_lesson_exemplar/blob/main/AGENTS.md) (Cassie Buhler)
  - [Repository Purpose](https://github.com/CU-ESIIL/LLM_lesson_exemplar/blob/main/AGENTS.md#repository-purpose)
  - [Step 1: Read the Example](https://github.com/CU-ESIIL/LLM_lesson_exemplar/blob/main/AGENTS.md#step-1-read-the-example)
  - [Core Steps](https://github.com/CU-ESIIL/LLM_lesson_exemplar/blob/main/AGENTS.md#core-steps)
  - [After It Runs](https://github.com/CU-ESIIL/LLM_lesson_exemplar/blob/main/AGENTS.md#after-it-runs)
  - [Directory Structure](https://github.com/CU-ESIIL/LLM_lesson_exemplar/blob/main/AGENTS.md#directory-structure)
  - [Region Boundaries](https://github.com/CU-ESIIL/LLM_lesson_exemplar/blob/main/AGENTS.md#region-boundaries)
  - [Required Script Header](https://github.com/CU-ESIIL/LLM_lesson_exemplar/blob/main/AGENTS.md#required-script-header)
  - [Output Requirements](https://github.com/CU-ESIIL/LLM_lesson_exemplar/blob/main/AGENTS.md#output-requirements)
  - [Failure Handling](https://github.com/CU-ESIIL/LLM_lesson_exemplar/blob/main/AGENTS.md#failure-handling)
  - [Resampling Rules](https://github.com/CU-ESIIL/LLM_lesson_exemplar/blob/main/AGENTS.md#resampling-rules)
  - [Ad-Hoc Preprocessing](https://github.com/CU-ESIIL/LLM_lesson_exemplar/blob/main/AGENTS.md#ad-hoc-preprocessing)
- [openclaw_container AGENTS.md](https://github.com/CU-ESIIL/openclaw_container/blob/main/AGENTS.md) (CU ESIIL OASIS ScienceClaw)
  - [Core Operating Contract](https://github.com/CU-ESIIL/openclaw_container/blob/main/AGENTS.md#core-operating-contract)
  - [Default Workflow](https://github.com/CU-ESIIL/openclaw_container/blob/main/AGENTS.md#default-workflow)
  - [Documentation and Website Policy](https://github.com/CU-ESIIL/openclaw_container/blob/main/AGENTS.md#documentation-and-website-policy)
  - [Testing Policy](https://github.com/CU-ESIIL/openclaw_container/blob/main/AGENTS.md#testing-policy)
  - [Package and Structure Separation Policy](https://github.com/CU-ESIIL/openclaw_container/blob/main/AGENTS.md#package-and-structure-separation-policy)
  - [Data Discovery and Data Use Policy](https://github.com/CU-ESIIL/openclaw_container/blob/main/AGENTS.md#data-discovery-and-data-use-policy)
  - [Data Sovereignty and Intellectual Property Policy](https://github.com/CU-ESIIL/openclaw_container/blob/main/AGENTS.md#data-sovereignty-and-intellectual-property-policy)
  - [Design and Usability Policy](https://github.com/CU-ESIIL/openclaw_container/blob/main/AGENTS.md#design-and-usability-policy)
  - [Decision Logging](https://github.com/CU-ESIIL/openclaw_container/blob/main/AGENTS.md#decision-logging)
  - [OpenClaw Slack/Gateway Operations](https://github.com/CU-ESIIL/openclaw_container/blob/main/AGENTS.md#openclaw-slackgateway-operations)
  - [Model Routing Policy](https://github.com/CU-ESIIL/openclaw_container/blob/main/AGENTS.md#model-routing-policy)

### Agent Skills / `SKILL.md` (Actionable Capabilities)

Think of Agent Skills as a **toolbox or an app store** for the AI agent. Instead of general project guidelines, a skill teaches the agent how to execute a complex, multi-step workflow.

- **Target Audience:** The AI agent across _any_ project that requires this specific ability.
- **Content Focus:**
  - Strict step-by-step procedural workflows (e.g., `/spec`, `/plan`, `/review`).
  - Structural anti-rationalization tables (rules preventing the agent from cutting corners, like skipping unit tests).
  - Executable automation helpers (scripts located in a nested `scripts/` directory).
- **Structure Requirements:** Requires structured YAML frontmatter at the top:

```markdown
---
name: vercel-deploy
description: Deploy my web app to Vercel production.
---
# Deploy Skill
...

```

Comments gleaned from Gemini browser summary:

- Agent skills typically refer to the capabilities or functions an AI can perform.
- The context window includes the information the AI can reference during a conversation.
- Skills may influence the AI's responses but are not directly counted in the context window.
- The context window primarily consists of user inputs and previous exchanges.
- Skills can enhance the AI's ability to interpret and respond to context effectively.
- Understanding the distinction helps clarify how AI processes information during interactions.

### Summary of Differences

While **`AGENTS.md`** sets the **boundaries and context** of _where_ the agent is working, **Agent Skills** extend the **functional capability** of _what_ the agent can actually execute. For example, your `AGENTS.md` might dictate that you use Vitest for unit testing, but you would activate an `agent-skill` to execute a structured test-driven development workflow using those tools.
