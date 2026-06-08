# Artificial Intelligence (AI) References

This is a (growing?) collection of references about AI concept, tools and
collaborative environments.
To learn about (generative) AI, start with the self-paced workshop on
[Generative AI & Prompt Engineering (Tyson Swetnam)](https://tyson-swetnam.github.io/intro-gpt/).

- [Articles about AI](#articles-about-ai)
  - [How might we think about AI?](#how-might-we-think-about-ai)
  - [What about ethics and environmental impact of AI?](#what-about-ethics-and-environmental-impact-of-ai)
- [AI Tools and Agents](#ai-tools-and-agents)
  - [Google Gemini and Antigravity](#google-gemini-and-antigravity)
  - [Other AI Environments](#other-ai-environments)
- [Prompt Engineering](#prompt-engineering)
  - [AI Prompt Examples](AI_prompts.md)
  - [Sharing Prompts instead of Code](https://byandell.github.io/Gravity-and-Antigravity/#sharing-prompts-instead-of-code)
  - [Prompts to Organize Workflows](#prompts-to-organize-workflows)
  - [Learning about prompts](#learning-about-prompts)
  - [Prompt Engineering References](#prompt-engineering-references)
- [Agent Skills](#agent-skills)

## Articles about AI

Interestingly, when I started populating this list, AI halucinated several entries, which I had to go back and properly curate.

### How might we think about AI?

As Ezra Klein noted
[recently](https://www.nytimes.com/2026/03/29/opinion/ai-claude-chatgpt-gemini-mcluhan.html), John Culkin (1967) provided a helpful summary of Marshall McLuhan's ideas:

- “We shape our tools and thereafter they shape us.”
- “The environments set up by different media are not just containers for people; they are processes which shape people.”

Klein went on 'to steal one more McLuhanism, “the numb stance of the technological idiot” [is] to treat A.I. as merely a tool waiting passively for our use. To use A.I. deeply is to engage in a process, not just to push a button. It will reshape us; it already is. We have to be attentive to how.'

Jaron Lanier has written and spoken extensively about AI.
His provocative
[There is no AI](https://byandell.github.io/Jaron-Lanier-There-is-no-AI/)
reframed AI as a tool for human social collaboration,
particularly when credit for sources encourages data dignity.

A couple articles point out that new startups have found
early success in building new tools with AI agents
while legacy companies (think Google)
see only marginal replacement of human force by AI agents.
AI's disruption of the workforce is real, and it may be radically changing
what we do.
However, rather than eliminating the need for people,
many (most?) realms of society and industry have an opportunity to rethink
how we work and collaborate.
As multiple authors writing in early 2026 point out,
this is not a future event, but something we are now experincing.

- [There is no AI](https://byandell.github.io/Jaron-Lanier-There-is-no-AI/)
- [I Saw Something New in San Francisco (Ezra Klein, NYTimes)](https://www.nytimes.com/2026/03/29/opinion/ai-claude-chatgpt-gemini-mcluhan.html)
- The Atlantic on AI (2026)
  - [The AI-Panic Cycle—And What’s Actually Different Now](https://www.theatlantic.com/podcasts/2026/02/the-ai-panic-cycle-and-whats-actually-different-now/686077/)
  - [What Do the People Building AI Believe? (The Atlantic)](https://www.theatlantic.com/podcasts/2026/02/what-do-the-people-building-ai-believe/686173/)
  - [America Isn’t Ready for What AI Will Do to Jobs](https://www.theatlantic.com/magazine/2026/03/ai-economy-labor-market-transformation/685731/)
  - [Don’t Call It ‘Intelligence’](https://www.theatlantic.com/ideas/2026/03/intelligence-concept/686121/)
- [What is the Future of AI? (Forbes)](https://www.forbes.com/sites/gilpress/2026/02/16/what-is-the-future-of-ai-heres-what-one-successful-investor-says/?ctpv=searchpage)
- [Coding After Coders: The End of Computer Programming as We Know It (NYTimes)](https://www.nytimes.com/2026/03/12/magazine/ai-coding-programming-jobs-claude-chatgpt.html)

### What about ethics and environmental impact of AI?

AI companies are trying to improve their efficiency, and their image.
This includes making machines and algorithms that use less water and power.
Also, there is an emerging effort to support the communities that are protecting and nourishing the water that weaves through their lands.

Here are some approaches to this challenge,
which range from zero-water data centers to rethinking how we train people to use data.

- [Ethics of AI (Tyson Swetnam Blog)](https://tysonswetnam.com/blog/posts/2025-01-14-gpt101/#ethics-of-ai)
- [Sustainable by Design (Microsoft)](https://www.microsoft.com/en-us/microsoft-cloud/blog/2024/12/09/sustainable-by-design-next-generation-datacenters-consume-zero-water-for-cooling/)
- [Commitment to Climate Conscious Data Center Cooling (Google)](https://blog.google/company-news/outreach-and-initiatives/sustainability/our-commitment-to-climate-conscious-data-center-cooling/)
- [AI Energy Innovation Climate Research (NVIDIA)](https://blogs.nvidia.com/blog/ai-energy-innovation-climate-research/)
- [No Data Centers on Native Land Campaign (Honor Earth)](https://Honorearth.org/stopdatacolonialism)

References on carbon-neutral and micro data center forecasts and best practices:

- [Carbon Neutral Data Centers Market Forecasts (GII Research)](https://www.giiresearch.com/report/smrc2007748-carbon-neutral-data-centers-market-forecasts.html)
- [Carbon Neutral Data Center 2030 (Computer Forecast)](https://www.computeforecast.com/blogs/carbon-neutral-data-center-2030/)
- [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2589004225019662)
- [Zero Edge Cloud Data Sovereignty (Salish Tribal Alliance)](https://salishtribalalliancegroup.com/data-centers)
- [Modern data center sustainability best practices to consider (TechTarget)](https://www.techtarget.com/searchDataCenter/tip/Modern-data-center-sustainability-best-practices-to-consider)
- [Micro Data Centers: The Future of Edge Computing (GBC Engineers)](https://gbc-engineers.com/news/micro-data-centers)
- [Micro Data Centers: A Practical Guide for Small IT Teams (Data Center Knowledge)](https://www.datacenterknowledge.com/modular-data-centers/micro-data-centers-a-practical-guide-for-small-it-teams)

Here are maps and reports of data centers in the US:

- [United States Data Center Energy Usage Report (LBNL)](https://eta-publications.lbl.gov/sites/default/files/2024-12/lbnl-2024-united-states-data-center-energy-usage-report.pdf)
- [Data Center Infrastructure in the United States, March 2026 (Nat Lib Rockies)](https://docs.nlr.gov/docs/gen/fy26/99908.jpg)
- [Data Center Map](https://www.datacentermap.com/)

## AI Tools and Agents

There are now innumerable AI tools for coding and analysis,
and this will not be a compendium.
Instead, I am trying to keep abreast of the landscape
and will add notes here as I learn more.
When using most "traditional" tools, there are now flavors of AI that
have infiltrated, including messaging and email apps.
Code generation using GitHub repos is improving with the nuanced integration of
[GitHub Copilot](https://github.com/features/copilot).

Initially, it seemed important to understand
[Model context protocol (MCP)](https://modelcontextprotocol.io/),
the concept and protocol developed by Anthropic (and first available in
`Claude Code`). The revolutionary idea is that a large language model (LLM) is not just a text generator, but can interact with your other tools and data to get information and take actions.
However, this was quickly integrated into an
[integrated development environment (IDE)](https://www.geeksforgeeks.org/blogs/what-is-ide/)
building on
[Visual Studio Code (VScode or code)](https://code.visualstudio.com/)
so that one can edit code manually and/or interact with an LLM via
an AI agent in a side panel.
This AI agent uses MCP to connect with your data and code
under your guidance.
We need not be concerned about the MCP mechanics of LLM
communication with local (or cloud-based) tools and data.
Instead, we carry on conversations with an AI agent who,
with explicit permission from us,
changes local code or documents and creates reports.

More sophisticated AI environments redesign such tools to offer
a fully natural language experience in which we may guide a team
of AI agents, each with its own role and expertise, to accomplish
a larger set of tasks.

### Google Gemini and Antigravity

Google Gemini has an enterprise contract with UW-Madison; hence I concentrate a bit on it here.
Much of this applies more broadly to other AI environments.
While Gemini is available via the browser, it is also being embedded
into a variety of tools.
These tools are evolving fast, due to competition as well as
tool advances through use of AI on the tool development process.

Google initially offered `Antigravity 1.0` as an extension of
[`VScode`](https://code.visualstudio.com/)
with a Gemini AI agent in the right panel.
On 19 May 2026, Google released
[`Antigravity 2.0`](https://antigravity.google/)
as a suite of 4 tools

- `Antigravity 2.0`: full agentic development platform
- `Antigravity CLI`: command line interface (CLI), used in the terminal
- `Antigravity SDK`: software development kit (SDK), used by developers to build apps
- `Antigravity IDE`: integrated development environment (IDE), an updated version of the previous (`1.x`) IDE

Unfortunately, this release confused previous users.
The new tool, with the same name as the previous tool, presents
as a chat window without IDE-like features, and without clear indication
about how it differs from the prior tool, or how to get back
to the prior tool.
This will be a useful tool for
[vibe coding](https://vibe-coding.run/)
but not directly relevant to those of us developing code-based tools.
`Antigravity IDE` seems better suited for that task.
Again, unfortunately, the IDE did not carry any previous chat history
(known as `conversations`) over to 2.0.
See
[Recovering Antigravity Conversations](recover_conversations.md)
for a guide I wrote to recover them based on community response.

- [Google Gemini](https://gemini.google.com/)
  - [Generative AI Services at UW–Madison: Tools, Policies & Resources](https://kb.wisc.edu/ai/)
  - [Prompt design strategies | Gemini API | Google AI for Developers](https://ai.google.dev/gemini-api/docs/prompt-design)
  - [File input methods | Gemini API | Google AI for Developers](https://ai.google.dev/gemini-api/docs/file-inputs)
  - [Import a GitHub repository & ask about it in the Gemini web app](https://kb.wisc.edu/ai/135575)
  - [Connect Box | Gemini Enterprise | Google Cloud Documentation](https://cloud.google.com/gemini-enterprise/docs/connect-box)
- [Antigravity](https://antigravity.google/)
  - [Google Antigravity Documentation](https://antigravity.google/docs/get-started)
  - [Getting Started with Google Antigravity (CodeLabs)](https://codelabs.developers.google.com/getting-started-google-antigravity)
  - [Recovering Antigravity 1.x Conversations](recover_conversations.md)

### Other AI Environments

`Antigravity` and other IDEs began as forks of the
[VS Code](https://code.visualstudio.com/)
that integrate LLMs with collaboration on a user's local files and tools.
Some have evolved away from these roots toward standalone apps.

- [Anthropic's Claude Code](https://www.anthropic.com/product/code)
- [Open AI's Codex](https://openai.com/index/openai-codex/)
- [Posit's Positron](https://posit.co/products/open-source/positron/)
- [Cursor MCP Docs](https://docs.cursor.sh/mcp)
- [Windsurf Review 2026: The AI IDE Redefining Coding Workflows | Second Talent](https://secondtalent.com/insights/windsurf-review-2026-the-ai-ide-redefining-coding-workflows/)

As I understand it, Cursor and Windsurf are less comprehensive IDEs.
There are concepts of "AI-native" and "agent-native" IDEs, but I am not sure I fully grasp the distinction.
It seems that "AI-native" concerns conversations with LLMs, while "agent-native" concerns the use of AI agents to do work.
See for instance [Agentic AI](https://tyson-swetnam.github.io/intro-gpt/agentic/).

See caution in [Using R in VS Code with Radian](radian.md)
about `radian` and AI environments.

## Prompt Engineering

Prompt engineering is the process of designing prompts that elicit the desired output from an AI model. It is a general approach to using AI tools, and can be applied to a wide range of tasks. So far, my focus has been on prompt engineering of code, or at least GitHub repositories.
Below is a schema I am developing.

Prompt engineering is about laying a digital trail of prompts that guide the AI toward what one wants to investigate, gradually refining. These are embedded in conversations one develops. It is possible, and now done regularly by experts, to develop a set of AI agents that respond to their own prompts and do part of their work. I don’t yet know how to manage such agents.

Prompts, and
[prompt engineering](https://www.promptingguide.ai/introduction/what-is-prompt-engineering),
is a useful way to develop tools without having to directly write code.
A great guide is Tyson Swetnam's
[Getting Started with Prompts](https://tyson-swetnam.github.io/intro-gpt/prompts/#getting-started-basic-prompt-structure).
However, if you just use prompts and don't keep track of them, you are missing an opportunity to easily document your work flow.
That is, how will you later remember what you did and how? And how will you share your learning with others?

A simple way to begin is to ask your AI agent to save your prompts in a file, e.g. `prompts.md`.
If you do more work within the same conversation, ask the AI agent to update the file.
The next section shows how I used this approach to organize a somewhat complicated workflow.
For some of my examples, see
[Sharing Prompts instead of Code](https://byandell.github.io/Gravity-and-Antigravity/#sharing-prompts-instead-of-code)
and
[AI Prompt Examples](AI_prompts.md).

### Prompts to Organize Workflows

Workflows can get rather complicated.
Often, it is helpful to organize them into human-size chunks to make them easier to manage and understand.

I experimented with developing a series of prompts to transform a workflow into its components. The functions do the work but need not be viewed in the workflow. The workflow should be a concise document that shows the steps and the results together. The following steps should begin with a workflow file, e.g. ​`workflow.R`.
The workflow prompt is included in
[AI Prompt Examples](AI_prompts.md#organize-a-workflow).

- Place the functions in their own R file (`functions.R`). This file should retain the comments that organize them into the workflow steps.
- Organize the workflow into a Quarto document (`workflow.qmd`). This file should invoke (source) the `functions.R` and have its R code in chunks, with the comments turned into section delimiters and text blocks.
- Modify the workflow to display results, with options to save images and tables as PDF and CSV files, respectively.
- Present the workflow in source and rendered form to be readable by a human.

Later prompts would modify the workflow to have options to examine different datasets.
Once I had understood these steps, I saw how I could have one comprehensive prompt that would orchestrate the process. I asked the AI agent to create this.
These initial efforts are in the
[sysgenAnalysis](https://github.com/AttieLab-Systems-Genetics/sysgenAnalysis)
repository, with the
[Workflow Prompt](https://github.com/AttieLab-Systems-Genetics/sysgenAnalysis/blob/main/inst/doc/walkthrough.md#workflow-prompt)
based on step-by-step instructions in the
[Workflow Walkthroughs](https://github.com/AttieLab-Systems-Genetics/sysgenAnalysis/blob/main/inst/doc/walkthrough.md#workflow-walkthroughs)

### Learning about Prompts

I began learning about prompts from
[Tyson Swetnam](https://www.tysonswetnam.com/),
who demonstrated at the
[ESIIL Innovation Summit 2025](https://cu-esiil.github.io/Innovation-Summit-2025/)
how a natural language paragraph could become an AI prompt.
I adapted this with the
[Draft AI Task using Claude and MCP](https://github.com/CU-ESIIL/resilience-rare-hydrologic-events-management-innovation-summit-2025__15/blob/main/documentation/group-notes.md#draft-ai-task-using-claude-and-mcp)
for the
[Three Rivers ESIIL working group](https://cu-esiil.github.io/resilience-rare-hydrologic-events-management-innovation-summit-2025__15/),
which became the section on
[AI Prompt Engineering](https://github.com/CU-ESIIL/resilience-rare-hydrologic-events-management-innovation-summit-2025__15/blob/main/docs/index.md#ai-prompt-engineering).
This exciting project is on hold but has great potential.

### Prompt Engineering References

Below are some references on prompt engineering quickly culled from the web:

- [Generative AI & Prompt Engineering (Tyson Swetnam)](https://tyson-swetnam.github.io/intro-gpt/)
- [Prompt design strategies (Google Gemini API)](https://ai.google.dev/gemini-api/docs/prompt-design)
- [What is prompt engineering? (Google Cloud)](https://cloud.google.com/discover/what-is-prompt-engineering)
- [Prompt engineering (IBM)](https://www.ibm.com/think/prompt-engineering)
- [Prompt engineering (Microsoft)](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/prompt-engineering)
- [Prompt engineering Guide (Prompting Guide)](https://www.promptingguide.ai/)
  - [What is prompt engineering?](https://www.promptingguide.ai/introduction/what-is-prompt-engineering)
- [What Is Prompt Engineering? (Coursera)](https://cloud.google.com/discover/what-is-prompt-engineering)
- [What is prompt engineering? (GitHub)](https://github.com/resources/articles/what-is-prompt-engineering)
- [AI Prompt Examples](AI_prompts.md)

## Agent Skills

Further, there are things called `skills` that guide how agents work.

- [Antigravity Agent Skills](https://antigravity.google/docs/skills)
- [Antigravity Skills (CodeLabs)](https://codelabs.developers.google.com/getting-started-google-antigravity#8)
- [Claude Skills](https://claude.com/skills)
- [Anthropic Skills](https://github.com/anthropics/skills)
- [Agent Skills.io](https://agentskills.io/home)
- [GitHub Topics: agent-skills](https://github.com/topics/agent-skills)

Systems instructions can be entered as prompts, or can be built into a
`README for agents` as a project file
[AGENTS.md](https://agents.md/).
See for instance Cassie Buhler's
[LLM lesson exemplar](https://github.com/CU-ESIIL/LLM_lesson_exemplar/blob/main/AGENTS.md).

Based on the technical paradigms for AI coding assistants (such as Claude Code, GitHub Copilot, Cursor, and Codex), **Agent Skills** (or `SKILL.md`) and **`AGENTS.md`** are two complementary standards used to provide context and capabilities to AI agents.

A comparative breakdown highlights their distinct roles, structures, and intended use cases:

| Feature | `AGENTS.md` | Agent Skills (`SKILL.md`) |
| --- | --- | --- |
| **Primary Purpose** | Defines **repository-specific context** (tech stack, coding standards, project layout, architecture rules). | Packages **procedural knowledge** or actionable automation capabilities (how to deploy, audit, generate code, or test). |
| **Scope** | Bound to a specific codebase/repository (Static local context). | Portable across different repositories and platforms (Reusable "recipes"). |
| **Core Components** | A single Markdown file matching the [agents.md specification](https://agents.md). | A folder structure containing `SKILL.md` (frontmatter + rules) and optional automation scripts (Bash, Python, Node). |
| **Trigger Mechanism** | Loaded automatically when an agent begins working inside that repository. | Activated dynamically on-demand when the agent recognizes a relevant trigger phrase or task. |

---

### 1. `AGENTS.md` (Repository Context)

Think of `AGENTS.md` as the **onboarding handbook** for an AI agent entering a specific project. It tells the agent *what* the project is and *how* it should behave to blend in seamlessly with human contributors.

- **Target Audience:** The AI agent working *inside* that specific codebase.
- **Content Focus:** * Tech stack definitions (e.g., React 18, TypeScript, Tailwind).
- Directory layout (where to find hooks, components, or API services).
- Design tokens and rigid rules (e.g., *"Do not introduce new dependencies," "Prefer existing `Button` component"*).

- **Layering & Scope:** Can be nested. A root `AGENTS.md` might define company-wide standards, while a nested `services/api/AGENTS.md` layers on rules specific only to the backend service.

### 2. Agent Skills / `SKILL.md` (Actionable Capabilities)

Think of Agent Skills as a **toolbox or an app store** for the AI agent. Instead of general project guidelines, a skill teaches the agent how to execute a complex, multi-step workflow.

- **Target Audience:** The AI agent across *any* project that requires this specific ability.
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

### Summary of Differences

While **`AGENTS.md`** sets the **boundaries and context** of *where* the agent is working, **Agent Skills** extend the **functional capability** of *what* the agent can actually execute. For example, your `AGENTS.md` might dictate that you use Vitest for unit testing, but you would activate an `agent-skill` to execute a structured test-driven development workflow using those tools.

## Create a README.md for a Folder

**Prompts:**

- "create a `README.md` document that concisely summarizes contents of this folder at a high level"
- "update `README.md` with any additional files, obeying restrictions in `.gitignore`"

**Example:**

- [mkeller3Projects2](https://github.com/AttieLab-Systems-Genetics/mkeller3Projects2/blob/master/README.md)
- [sysgenDO1200](https://github.com/AttieLab-Systems-Genetics/sysgenDO1200/blob/main/README.md) has various examples
