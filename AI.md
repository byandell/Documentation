# Artificial Intelligence (AI) References

This is a (growing?) collection of references about AI concept, tools and
collaborative environments.

- [Articles about AI](#articles-about-ai)
- [AI Tools and Agents](#ai-tools-and-agents)
  - [Google Gemini and Antigravity](#google-gemini-and-antigravity)
  - [Other AI Environments](#other-ai-environments)
- [Prompt Engineering](#prompt-engineering)
  - [Prompts to Organize Workflows](#prompts-to-organize-workflows)
  - [Prompt Engineering References](#prompt-engineering-references)

## Articles about AI

- [There is no AI](https://byandell.github.io/Jaron-Lanier-There-is-no-AI/)
- [The A.I. Disruption We’ve Been Waiting for Has Arrived](https://www.theatlantic.com/technology/archive/2026/02/ai-disruption-future-of-work/708317/)
- [Something Big Is Happening](https://www.theatlantic.com/technology/archive/2026/02/ai-disruption-future-of-work/708317/)
- [The Atlantic: Josh Tyrangiel on AI and the Future of Work](https://www.theatlantic.com/technology/archive/2026/02/ai-disruption-future-of-work/708317/)
- [AI Agents Are Taking America by Storm](https://www.theatlantic.com/technology/archive/2026/02/ai-disruption-future-of-work/708317/)
- [The Great Software Quality Collapse: How We Normalized Catastrophe](https://www.theatlantic.com/technology/archive/2026/02/ai-disruption-future-of-work/708317/)

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
`Claude Code`). The revolutionary idea is that a large language model (LLM) is not just a text generator, but can interact with your other tools and data to get information and take actions. However, this has quickly been integrated into code environments so that one need not be concerned about the MCP mechanics of LLM communication with local (or cloud-based) tools and data to (with explicit permission) change local code or documents and create reports.

### Google Gemini and Antigravity

Google Gemini has an enterprise contract with UW-Madison; hence I concentrate a bit on it here.
[Antigravity](https://antigravity.google/) is the google-native integrated development environment (IDE) for Gemini.

- [Google Gemini](https://gemini.google.com/)
  - [Generative AI Services at UW–Madison: Tools, Policies & Resources](https://kb.wisc.edu/ai/)
  - [Prompt design strategies | Gemini API | Google AI for Developers](https://ai.google.dev/gemini-api/docs/prompt-design)
  - [File input methods | Gemini API | Google AI for Developers](https://ai.google.dev/gemini-api/docs/file-inputs)
  - [Import a GitHub repository & ask about it in the Gemini web app](https://kb.wisc.edu/ai/135575)
  - [Connect Box | Gemini Enterprise | Google Cloud Documentation](https://cloud.google.com/gemini-enterprise/docs/connect-box)
- [Antigravity](https://antigravity.google/)
  - [Antigravity Documentation](https://antigravity.google/docs/get-started)
  - [Full guide from install to Custom rules, workflows and MCP integration](https://antigravity.google/docs/get-started)
  - [Getting Started with Google Antigravity](https://codelabs.developers.google.com/getting-started-google-antigravity).

### Other AI Environments

`Antigravity` and other IDEs are essentially next-generation versions of
[VS Code](https://code.visualstudio.com/)
that integrate LLMs with collaboration on a user's local files and tools.

- [Anthropic's Claude Code](https://www.anthropic.com/product/code)
- [Open AI's Codex](https://openai.com/index/openai-codex/)
- [Posit's Positron](https://posit.co/products/open-source/positron/)
- [Cursor MCP Docs](https://docs.cursor.sh/mcp)
- [Windsurf Review 2026: The AI IDE Redefining Coding Workflows | Second Talent](https://secondtalent.com/insights/windsurf-review-2026-the-ai-ide-redefining-coding-workflows/)

As I understand it, Cursor and Windsurf are less comprehensive IDEs.
There are concepts of "AI-native" and "agent-native" IDEs, but I am not sure I fully grasp the distinction.

See caution in [Using R in VS Code with Radian](radian.md)
about `radian` and AI environments.

## Prompt Engineering

Prompt engineering is the process of designing prompts that elicit the desired output from an AI model. It is a general approach to using AI tools, and can be applied to a wide range of tasks. So far, my focus has been on prompt engineering of code, or at least GitHub repositories.
Below is a schema I am developing.

Prompt engineering is about laying a digital trail of prompts that guide the AI toward what one wants to investigate, gradually refining. These are embedded in conversations one develops. It is possible, and now done regularly by experts, to develop a set of AI agents that respond to their own prompts and do part of their work. I don’t yet know how to manage such agents.

### Prompts to Organize Workflows

Workflows can get rather complicated.
Often, it is helpful to organize them into human-size chunks to make them easier to manage and understand.

I experimented with developing a series of prompts to transform a workflow into its compontents. The functions do the work but need not be viewed in the workflow. The workflow should be a concise document that shows the steps and the results together. The following steps should begin with a workflow file, e.g. ​`workflow.R`.

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

I began learning about this from
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
- [What Is Prompt Engineering? (Coursera)](https://cloud.google.com/discover/what-is-prompt-engineering)
- [What is prompt engineering? (GitHub)](https://github.com/resources/articles/what-is-prompt-engineering)
