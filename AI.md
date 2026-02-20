# Artificial Intelligence (AI) References

This is a (growing?) collection of references about AI concept, tools and
collaborative environments.

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
  - [invoke R or radian from terminal in panel below editor](https://antigravity.google/docs/get-started)

### Other AI Environments

`Antigravity` and other IDEs are essentially next-generation versions of
[VS Code](https://code.visualstudio.com/).
While you can use the enhanced R tool
[radian](https://github.com/randian-r/radian)
within these environments, they are not as seamless as
[Posit's RStudio](https://posit.co/download/rstudio-desktop/).
In fact, `radian` can interfere with the "memory" and operation of these tools.

- [Anthropic'sClaude Code](https://www.anthropic.com/product/code)
- [Posit's Positron](https://posit.co/products/open-source/positron/)
- [Cursor MCP Docs](https://docs.cursor.sh/mcp)
- [Windsurf Review 2026: The AI IDE Redefining Coding Workflows | Second Talent](https://secondtalent.com/insights/windsurf-review-2026-the-ai-ide-redefining-coding-workflows/)

As I understand it, Cursor and Windsurf are less comprehensive IDEs.
There are concepts of "AI-native" and "agent-native" IDEs, but I am not sure I fully grasp the distinction.

## Prompt Engineering

Prompt engineering is the process of designing prompts that elicit the desired output from an AI model. It is a general approach to using AI tools, and can be applied to a wide range of tasks. So far, my focus has been on prompt engineering of code, or at least GitHub repositories.
Below is a schema I am developing.

Prompt engineering is about laying a digital trail of prompts that guide the AI toward what one wants to investigate, gradually refining. These are embedded in conversations one develops. It is possible, and now done regularly by experts, to develop a set of AI agents that respond to their own prompts and do part of their work. I don’t yet know how to manage such agents.

### Prompt to separate functions from workflow

The goal of this prompt is to separate the functions from the workflow, so the workflow is more human-readable. The functions do the work but need not be viewed in the workflow. The workflow should be a concise document that shows the steps and the results together. The following steps should begin with a file ​`xxx.R`.

- Place the functions in their own R file (functions.R). This file should retain the comments that organize them into the workflow steps.
- Organize the workflow into a Quarto document (workflow.qmd). This file should invoke (source) the functions.R and have its R code in chunks, with the comments turned into section delimiters and text blocks.
- Modify the workflow to display results, with options to save images and tables as PDF and CSV files, respectively.
- Present the workflow in source and rendered form to be readable by a human.

Later prompts would modify the workflow to have options to examine different datasets.
Initial efforts with the
[sysgenAnalysis](https://github.com/AttieLab-Systems-Genetics/sysgenAnalysis)
repository are shown in the
[Script Transformation Prompt](https://github.com/AttieLab-Systems-Genetics/sysgenAnalysis/blob/main/inst/doc/prompt.md)
based on step-by-step instructions in the
[Project Walkthroughs](https://github.com/AttieLab-Systems-Genetics/sysgenAnalysis/blob/main/inst/doc/walkthrough.md)

Another example of prompt engineering was in the
[Three Rivers ESIIL working group](https://cu-esiil.github.io/resilience-rare-hydrologic-events-management-innovation-summit-2025__15/)
where we developed
[AI Prompt Engineering](https://github.com/CU-ESIIL/resilience-rare-hydrologic-events-management-innovation-summit-2025__15/blob/main/docs/index.md#ai-prompt-engineering)
and
[Draft AI Task using Claude and MCP](https://github.com/CU-ESIIL/resilience-rare-hydrologic-events-management-innovation-summit-2025__15/blob/main/documentation/group-notes.md#draft-ai-task-using-claude-and-mcp)

Below are some references on prompt engineering quickly culled from the web:

- [Prompt design strategies | Gemini API | Google AI for Developers](https://ai.google.dev/gemini-api/docs/prompt-design)
- [What is prompt engineering? | Google Cloud](https://cloud.google.com/discover/what-is-prompt-engineering)
- [IBMPrompt engineering](https://www.ibm.com/think/prompt-engineering)
- [Prompt engineering](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/prompt-engineering)
- [Prompt engineering Guide](https://www.promptingguide.ai/)
- [Coursera What Is Prompt Engineering?](https://cloud.google.com/discover/what-is-prompt-engineering)
- [GitHubWhat is prompt engineering?](https://github.com/resources/articles/what-is-prompt-engineering)
