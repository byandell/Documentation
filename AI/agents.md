---
title: "Agents and Workspace Rules"
parent: "AI (Artificial Intelligence)"
nav_order: 6
---

# Agents and Workspace Rules

- [What is an `AGENTS.md` file?](#what-is-an-agentsmd-file)
- [Comparison of `AGENTS.md`, `README.md`, and `DEVELOPER.md`](#comparison-of-agentsmd-readme-and-developer)
- [Example `AGENTS.md` files](#example-agentsmd-files)
- Additional Pages
  - [Context Engineering](context.md)

## What is an `AGENTS.md` file?

Project-level systems instructions and agent skills,
project context, etc.
can be built into a project's
"README for agents" called
[AGENTS.md](https://agents.md/).
Think of `AGENTS.md` as the **onboarding handbook** for an AI agent entering a specific project. It tells the agent _what_ the project is and _how_ it should behave to blend in seamlessly with human contributors.

The challenge with `AGENTS.md` is that it is automatically loaded into the
context window by AI agents working in the project.
Hence, it already fills up part of the context window,
limiting space for your conversation prompts and results.
One solution is to have a concise `AGENTS-mini.md`
(with perhaps a more detailed `AGENTS-LONG.md` loaded when needed)
This works well as long as the concise version is sufficient
---

## Comparing README.md, DEVELOPER.md, and AGENTS.md

In a collaborative repository, documentation is stratified by target audience, technical depth, and operational purpose.
A **human developer** uses the `README.md` to get started, reads `DEVELOPER.md` to understand _why_ the code is designed the way it is, and defines rules in `AGENTS.md` so that their **AI partner** knows exactly _how_ it must behave when editing files.
The table below outlines how these three entrypoint documents complement one another:

| Metric | `README.md` | `DEVELOPER.md` | `AGENTS.md` |
| :--- | :--- | :--- | :--- |
| **Primary Audience** | Users, evaluators, and prospective contributors. | Human developers, maintainers, and onboardees. | AI coding assistants (e.g., Antigravity, Copilot). |
| **Core Goal** | Welcoming introduction; get the project running and explain what it does. | Explain the codebase design, module boundaries, and architecture. | Dictate strict operational rules, workflows, and programming constraints. |
| **Typical Scope & Content** | Quick start, installation, dependencies, and licensing. | System/reactivity diagrams, module indices, and extension guides. | Code formatting rules, file-versioning workflows, and strict constraints. |
| **Tone & Style** | Descriptive, promotional, and high-level. | Explanatory, conceptual, and diagram-heavy. | Concise, strict, imperative, and rule-focused. |
| **Location & Integration** | Repository Root (`/README.md`) | Root, `docs/` folder, or package articles (`vignettes/`). | Workspace config folders (e.g., `.agents/AGENTS.md`). Can be nested to layer subdirectory-specific rules. |

#### AGENTS.md Examples

Ask an AI agent to "create `AGENTS.md` for this project".
I just did this for multiple projects, including this one.
See for instance these example `AGENTS.md` files with listed sections:

- [Document Digital Tools `AGENTS.md`](../AGENTS.md)
  - Purpose
  - Repository Structure
  - Key Files
  - Conventions
  - Related Organizations & Repositories
  - Code Preferences
- [Working Group OASIS `AGENTS.md`](https://github.com/CU-ESIIL/Working_group_OASIS/blob/main/AGENTS.md) (CU ESIIL)
  - Guidelines for agents
  - Working Group OASIS and Project Group OASIS
- [LLM lesson exemplar `AGENTS.md`](https://github.com/CU-ESIIL/LLM_lesson_exemplar/blob/main/AGENTS.md) (Cassie Buhler)
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
- [openclaw_container `AGENTS.md`](https://github.com/CU-ESIIL/openclaw_container/blob/main/AGENTS.md) (CU ESIIL OASIS ScienceClaw)
  - [Core Operating Contract](https://github.com/CU-ESIIL/openclaw_container/blob/main/AGENTS.md#core-operating-contract)
  - [Default Workflow](https://github.com/CU-ESIIL/openclaw_container/blob/main/AGENTS.md#default-workflow) ⚠️
  - [Documentation and Website Policy](https://github.com/CU-ESIIL/openclaw_container/blob/main/AGENTS.md#documentation-and-website-policy)
  - [Testing Policy](https://github.com/CU-ESIIL/openclaw_container/blob/main/AGENTS.md#testing-policy)
  - [Package and Structure Separation Policy](https://github.com/CU-ESIIL/openclaw_container/blob/main/AGENTS.md#package-and-structure-separation-policy)
  - [Data Discovery and Data Use Policy](https://github.com/CU-ESIIL/openclaw_container/blob/main/AGENTS.md#data-discovery-and-data-use-policy)
  - [Data Sovereignty and Intellectual Property Policy](https://github.com/CU-ESIIL/openclaw_container/blob/main/AGENTS.md#data-sovereignty-and-intellectual-property-policy)
  - [Design and Usability Policy](https://github.com/CU-ESIIL/openclaw_container/blob/main/AGENTS.md#design-and-usability-policy)
  - [Decision Logging](https://github.com/CU-ESIIL/openclaw_container/blob/main/AGENTS.md#decision-logging)
  - [OpenClaw Slack/Gateway Operations](https://github.com/CU-ESIIL/openclaw_container/blob/main/AGENTS.md#openclaw-slackgateway-operations)
  - [Model Routing Policy](https://github.com/CU-ESIIL/openclaw_container/blob/main/AGENTS.md#model-routing-policy)
