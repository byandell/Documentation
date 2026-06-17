# Artificial Intelligence (AI) References

This is a growing collection of references about AI concept, tools and
collaborative environments.
To learn about (generative) AI, start with the self-paced workshop on
[Generative AI & Prompt Engineering (Tyson Swetnam)](https://tyson-swetnam.github.io/intro-gpt/).

- [AI References (Quarto Slideshow)](https://byandell.github.io/Documentation/quarto/AI.html)
- [Articles about AI](#articles-about-ai)
  - [How might we think about AI?](#how-might-we-think-about-ai)
  - [What about ethics and environmental impact of AI?](#what-about-ethics-and-environmental-impact-of-ai)
- [AI Environments](#ai-environments)
  - [Cloud-Based Educational Environments](#cloud-based-educational-environments)
  - [Google Gemini and Antigravity](#google-gemini-and-antigravity)
  - [Other AI Environments](#other-ai-environments)
  - [Agentic AI](#agentic-ai)
  - [Large Language Models](#large-language-models)
- [Prompt Engineering](#prompt-engineering)
  - [AI Prompt Examples](./prompts/)
  - [Sharing Prompts instead of Code](https://byandell.github.io/Gravity-and-Antigravity/#sharing-prompts-instead-of-code)
  - [Prompts to Organize Workflows](#prompts-to-organize-workflows)
  - [Learning about prompts](#learning-about-prompts)
  - [Prompt Engineering References](#prompt-engineering-references)
- [Context Engineering](#context-engineering)
  - [Context Engineering References](#context-engineering-references)
  - [Comparison of Agent Skills and AGENTS.md](#comparison-of-agent-skills-and-agentsmd)
  - [AGENTS.md (Repository Context)](#agentsmd-repository-context)
  - [Agent Skills / SKILL.md (Actionable Capabilities)](#agent-skills--skillmd-actionable-capabilities)

_[byandell.github.io/Documentation](https://byandell.github.io/Documentation)_  

## Articles about AI

Interestingly, when I started populating this list, AI hallucinated several entries, which I had to go back and properly curate.

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
- The Atlantic on AI (2026)
  - [The AI-Panic Cycle—And What’s Actually Different Now (Charlie Warzel)](https://www.theatlantic.com/podcasts/2026/02/the-ai-panic-cycle-and-whats-actually-different-now/686077/)
  - [What Do the People Building AI Believe? (Charlie Warzel)](https://www.theatlantic.com/podcasts/2026/02/what-do-the-people-building-ai-believe/686173/)
  - [America Isn’t Ready for What AI Will Do to Jobs (Josh Tyrangiel)](https://www.theatlantic.com/magazine/2026/03/ai-economy-labor-market-transformation/685731/)
  - [Don’t Call It ‘Intelligence’ (Charles Yu)](https://www.theatlantic.com/ideas/2026/03/intelligence-concept/686121/)
- New York Times on AI (2026)
  - [I Saw Something New in San Francisco (Ezra Klein)](https://www.nytimes.com/2026/03/29/opinion/ai-claude-chatgpt-gemini-mcluhan.html)
  - [Coding After Coders: The End of Computer Programming as We Know It (Clive Thompson)](https://www.nytimes.com/2026/03/12/magazine/ai-coding-programming-jobs-claude-chatgpt.html)
  - [The Workers Letting AI Do Their Jobs (The Daily)](https://www.nytimes.com/2026/04/14/podcasts/the-daily/ai-coders.html)
  - [The Small-Business Owners Managing Whole Armies of A.I. Employees (Clive Thompson)](https://www.nytimes.com/2026/06/04/magazine/ai-agents-openclaw-small-business.html)
  - [The World’s Leading Deepfake Expert No Longer Trusts His Own Eyes (Hany Farid)](https://www.nytimes.com/2026/06/14/us/ai-deepfake-hany-farid.html)
- [What is the Future of AI? (Forbes)](https://www.forbes.com/sites/gilpress/2026/02/16/what-is-the-future-of-ai-heres-what-one-successful-investor-says/?ctpv=searchpage)

### What about ethics and environmental impact of AI?

AI companies are trying to improve their efficiency, and their image.
The power and water demands for rapid growth of data centers,
including those for commercial AI companies,
is a serious challenge
even as machines and algorithms are becoming more efficient
in their use of those scarce resources.
Also, there is an emerging effort to support the communities that are protecting and nourishing the water that weaves through their lands.
Below is an eclectic collection of resources about AI and its implications.

- [The Pope and AI](https://byandell.github.io/The-Pope-and_AI/)
- [What does AI cost? (CU ESIIL)](https://cu-esiil.github.io/Project_group_OASIS/ai-for-sustainability/what-does-it-cost/)
- [The uncritical adoption of AI in science is alarming — we urgently need guard rails (Nature)](https://www.nature.com/articles/d41586-026-01557-x)
- [On AI, Sustainability, and the Tensions Worth Keeping (Juan Maestre)](https://setx-uifl.org/esiil-2026/)
- [Ethics of AI (Tyson Swetnam Blog)](https://tysonswetnam.com/blog/posts/2025-01-14-gpt101/#ethics-of-ai)
- [No Data Centers on Native Land Campaign (Honor Earth)](https://Honorearth.org/stopdatacolonialism)

#### Energy and Water Reports

- [The Environmental Cost of Artificial Intelligence: Carbon, Water, and Land Footprints (UN University)](https://unu.edu/inweh/collection/environmental-cost-of-AIs-Enrgy-Use-Carbon-water-and-land-footprints)
  - [Rising Emissions, Depleting Water and Vanishing Land—UN Scientists: AI Is Threatening Natural Resources for Billions (UN University)](https://unu.edu/inweh/news/environmental-cost-of-AIs-Enrgy-use-carbon-water-and-land-footprints)
  - [New Form of Imperialism": Renowned U.N. Scientist on AI Boom's Huge Water, Carbon & Land Footprint (DemocracyNow!)](https://www.democracynow.org/2026/6/12/ai_data_centers_water_waste)
- [Data centers are growing in Texas, but big questions remain about water use (UT News)](https://news.utexas.edu/2026/05/06/data-centers-are-growing-in-texas-but-big-questions-remain-about-water-use/)
  - [Water Requirements for Data Centers (UT Bureau of Economic Geology)](https://compass.beg.utexas.edu/assets/publications/Water_Requirements_for_DC_White_Paper.pdf) (missing)
  - [Thirsty Data: Water Use and the Projected Data Center Boom in Texas (HARC)](https://harcresearch.org/wp-content/uploads/2026/01/Thirsty-Data-Water-Use-and-The-Projected-Data-Center-Boom-in-Texas.pdf)
- [United States Data Center Energy Usage Report (LBNL)](https://eta-publications.lbl.gov/sites/default/files/2024-12/lbnl-2024-united-states-data-center-energy-usage-report.pdf)
- [Data Center Infrastructure in the United States, March 2026 (Nat Lib Rockies)](https://docs.nlr.gov/docs/gen/fy26/99908.jpg)
- [Data Center Map](https://www.datacentermap.com/)

#### Company Statements

- [Sustainable by Design (Microsoft)](https://www.microsoft.com/en-us/microsoft-cloud/blog/2024/12/09/sustainable-by-design-next-generation-datacenters-consume-zero-water-for-cooling/)
- [Commitment to Climate Conscious Data Center Cooling (Google)](https://blog.google/company-news/outreach-and-initiatives/sustainability/our-commitment-to-climate-conscious-data-center-cooling/)
- [AI Energy Innovation Climate Research (NVIDIA)](https://blogs.nvidia.com/blog/ai-energy-innovation-climate-research/)

#### Carbon-neutral and micro data center forecasts and best practices

- [Carbon Neutral Data Centers Market Forecasts (GII Research)](https://www.giiresearch.com/report/smrc2007748-carbon-neutral-data-centers-market-forecasts.html)
- [Carbon Neutral Data Center 2030 (Computer Forecast)](https://www.computeforecast.com/blogs/carbon-neutral-data-center-2030/)
- [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2589004225019662)
- [Zero Edge Cloud Data Sovereignty (Salish Tribal Alliance)](https://salishtribalalliancegroup.com/data-centers)
- [Modern data center sustainability best practices to consider (TechTarget)](https://www.techtarget.com/searchDataCenter/tip/Modern-data-center-sustainability-best-practices-to-consider)
- [Micro Data Centers: The Future of Edge Computing (GBC Engineers)](https://gbc-engineers.com/news/micro-data-centers)
- [Micro Data Centers: A Practical Guide for Small IT Teams (Data Center Knowledge)](https://www.datacenterknowledge.com/modular-data-centers/micro-data-centers-a-practical-guide-for-small-it-teams)

## AI Environments

We typically work with AI within an environment.
Most "traditional" tools are now flavored with AI suggestions,
including messaging and email apps
(which can be optionally turned off).
There are now innumerable AI tools for coding and analysis,
and this will not be a compendium.
Instead, I am trying to keep abreast of the landscape
that seems relevant to me,
and will add notes here as I learn more.

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

### Cloud-Based Educational Environments

Cloud-based educational environments enable students and instructors
to learn code, optionally with AI agent interactions,
without having to try to set up systems on their
own, idiosyncratic devices.

For those working directly in GitHub,
code generation within repos is improving with the nuanced integration of
[GitHub Copilot](https://github.com/features/copilot),
both for repo editing and for use in
[GitHub Codespaces](https://github.com/features/codespaces),
which is a cloud-based IDE optionally
integrated with each GitHub repo.

[Google Colab](https://colab.research.google.com/)
 provides a free and simple way to code in R and Python,
with optional AI support via
[Google Gemini](https://gemini.google/about/).

[CyVerse Discovery Environment](https://de.cyverse.org/)
is a cloud-based enviroment for data science and bioinformatics.
I have used this in conjunction with
[Environmental Science and Innovation & Impact Laboratory (ESIIL)](https://esiil.org/)
to catalyze instruction, research and tool development.
Recently, CyVerse DE added AI engines
[Roo and Cline](https://www.openxcell.com/blog/roo-code-vs-cline/)
to their VScode IDE environment.
(**NB: Roo and Cline seem to work best in a Chrome browser**.)
We can use LLM APIs from
[AI Verde](https://chat.cyverse.ai/)
to tunnel a variety of LLMs
into either CyVerse DE or other IDEs of our choice.
See
[AI-VERDE Manual & Resource Site](https://aiverde-docs.cyverse.ai/)
and
[AI Verde API](https://aiverde-docs.cyverse.ai/api/).

CyVerse and AI Verde use
[Jetstream2](https://jetstream-2.iu.edu)
to host computing tools at scale.
Jetstream2 is part of the NSF-funded
[ACCESS](https://access-ci.org),
which provides free access to compute and AI resources at scale.
These resources also include
[HTCondor](https://htcondor.org)
and
[PATh](https://path-cc.io).
ACCESS resources typically require an educational account
and benefit from technical guidance.

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
as a suite of 4 tools:

- `Antigravity 2.0`: full multi-agentic AI code development environment
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
  - [Prompt design strategies (Google AI for Developers)](https://ai.google.dev/gemini-api/docs/prompt-design)
  - [File input methods (Google AI for Developers)](https://ai.google.dev/gemini-api/docs/file-inputs)
  - [Import a GitHub repository & ask about it in the Gemini web app (UW-Madison)](https://kb.wisc.edu/ai/135575)
  - [Connect Box (Google Cloud)](https://cloud.google.com/gemini-enterprise/docs/connect-box)
- [Antigravity](https://antigravity.google/)
  - [Google Antigravity Documentation](https://antigravity.google/docs/get-started)
  - [Getting Started with Google Antigravity (CodeLabs)](https://codelabs.developers.google.com/getting-started-google-antigravity)
  - [Recovering Antigravity 1.x Conversations](recover_conversations.md)

### Other AI Environments

`Antigravity` and many other IDEs began as forks of the
[VS Code](https://code.visualstudio.com/)
that integrate LLMs with collaboration on a user's local files and tools.
Some have evolved away from these roots toward standalone apps.

- [Anthropic's Claude Code](https://www.anthropic.com/product/code)
- [Open AI's Codex](https://openai.com/index/openai-codex/)
- [Posit's Positron](https://posit.co/products/open-source/positron/)
- [Cursor MCP Docs](https://docs.cursor.sh/mcp)
- [Windsurf Review 2026: The AI IDE Redefining Coding Workflows (Second Talent)](https://secondtalent.com/insights/windsurf-review-2026-the-ai-ide-redefining-coding-workflows/)

See caution in [Using R in VS Code with Radian](radian.md)
about `radian` and AI environments.

### Agentic AI

There are concepts of "AI-native" and "agent-native" IDEs, but I am not sure I fully grasp the distinction.
It seems that "AI-native" concerns conversations with LLMs, while "agent-native" concerns the use of AI agents to do work.
Further, the straightforward use of conversations via prompt
and context engineering is often described (as below) in the
setting of using one AI agent at a time.

Nowadays (Spring 2026), sophisticated users of AI orchestrate multiple AI agents
to accomplish complex tasks.
[Claude](https://claude.com/solutions/agents),
[OpenAI ChatGPT][https://openai.com/index/introducing-workspace-agents-in-chatgpt/)
and
[Google Antigravity](https://antigravity.google/)
have been evolving such capabilities quickly
in the commercial world,
while new open source platforms have emerged,
notably
[OpenClaw](https://www.openclaw.ai/) and
[Hermes](https://hermes-agent.org/).

A science version of OpenClaw
[OASIS ScienceClaw](https://github.com/CU-ESIIL/openclaw_container)
is under development for scientific teams by ESIIL.
(See also
[ScienceClaw](https://github.com/beita6969/ScienceClaw).)
ESIIL is imagining OASIS ScienceClaw as a
[digital twin](https://www.ibm.com/think/topics/digital-twin)
of an
[ESIIL Working Group](https://esiil.org/working_groups).

There is an emerging concept of
[SOUL.md](https://soul.md/)
that defines each agent by the content
of a markdown file in a project folder.

- [SOUL Overview (Richard Weiss, Anthropic)](https://gist.github.com/Richard-Weiss/)
- [SOUL Template (OpenClaw)](https://docs.openclaw.ai/reference/templates/SOUL/)
- [SOUL Personality Guide (OpenClaw)](https://docs.openclaw.ai/concepts/soul)

This all takes time and practice
to build up both our ability
to understand and use multiple agents.
Selection and organization of appropriate agents for a task.
Further, multiple agents will likely require a larger monthly
fee, if using commercial agents.
See for instance

- [Agentic AI](https://tyson-swetnam.github.io/intro-gpt/agentic/)
- [Multi-Agent Orchestration Guide](https://www.agensi.io/learn/multi-agent-orchestration-guide)

### Large Language Models

Large language models (LLMs) are basically big transformer networks,
with nodes joined by edges that have weights based on the
strength of connection.
The nodes and edges (connections) for a particular LLM
are fixed, but the weights on the edges can be adjusted
based on data.
The nodes are representations (tokens) of (parts of) words,
or images or audio or other snippets of data.
Often this is described as learning patterns to predict
the next token in a sequence.
At scale, with billions or trillions of nodes,
these LLMs are able to quickly string together useful
responses to prompts to address a surprising range
of tasks.
I am a novice on this, so appeal to others
through links below to find good explanations.

#### What are large language models (LLMs)?

- [IBM](https://www.ibm.com/think/topics/large-language-models)
- [GeeksforGeeks](https://www.geeksforgeeks.org/artificial-intelligence/large-language-model-llm/)
- [AWS](https://aws.amazon.com/what-is/large-language-model/)

#### How do encoders and decoders work?

LLMs work by encoding text into numerical representations and then decoding them back into text. For instance, see
[Understanding Encoder-Only and Decoder-Only Transformer Models (Sebastian Raschka)](https://magazine.sebastianraschka.com/p/understanding-encoder-and-decoder)

- **Input Tokenization:** Text input is split into smaller units called tokens, which can be words or subwords.
- **Encoding:** Tokens are converted into numerical representations (embeddings) that capture their meanings.
- **Contextualization:** The model processes these embeddings through multiple layers to understand context and relationships between tokens.
- **Decoding:** The model generates output tokens based on the processed information, predicting the next token in the sequence.
- **Detokenization:** The generated tokens are converted back into human-readable text.
- **Fine-tuning:** The model can be further trained on specific tasks to improve its performance in generating relevant responses.

#### What is a Mixture of Experts (MoE)?

- [Maarten Grootendorst](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-mixture-of-experts)
- [GeeksforGeeks](https://www.geeksforgeeks.org/nlp/what-is-mixture-of-experts-moe/)
- [Hugging Face](https://huggingface.co/blog/moe)
- [Siyuan Mu and Sen Lin (2026)](https://arxiv.org/abs/2503.07137)

#### Open Source LLMs

The file
[verde_models.csv](https://github.com/byandell/Documentation/blob/main/verde_models.csv)
has open-source LLMs
 currently available (10 June 2026) via
[AI Verde](https://chat.cyverse.ai/),
which are cataloged on
[HuggingFace](https://huggingface.co/models).
Information includes:

- Technical Specifications
  - **Developer/Organization:** creator of model (e.g., Zhipu AI, Moonshot AI, Google, Meta). Tracking the lineage and ecosystem of the models.
  - **Context Window:** maximum number of tokens model can process in a single prompt (e.g., 32k, 128k, 1M). Critical factor for use cases involving long documents.
  - **Training Tokens:** number of tokens model was trained on, correlates with overall knowledge and reasoning capabilities.
- Operational & Licensing Details
 **Release Date:** how "state-of-the-art" it is relative to newer releases.
  - **License Type:** open-source (e.g., Apache 2.0, Llama 3 License) or proprietary. Determines how the model can be used commercially.
  - **Quantization Level:** bit-depth (e.g., FP16, INT8, 4-bit). Clarifies the memory requirements.
- Performance & Capabilities
  - **Benchmark Scores (e.g., MMLU, GSM8K):** standardized tests  compare the "intelligence" or reasoning ability of different models.
  - **Primary Modalities:** text-only or multimodal (e.g., can process images, audio, or video).
  - **Supported Languages:** English-centric, bilingual (e.g., English/Chinese), or multilingual.

Sources researched by Gemini include:

- [glm-4.7-flash (Ollama)](https://ollama.com/library/glm-4.7-flash)
- [Gemma 3 12B (OpenRouter)](https://openrouter.ai/models/google/gemma-3-12b)
- [Phi-4 (NVIDIA)](https://catalog.ngc.nvidia.com/models/nvidia/phi-4/overview)
- [[2505.09388] Qwen3 Technical Report (arXiv)](https://arxiv.org/abs/2505.09388)
- [MiniMax M2 (OpenRouter)](https://openrouter.ai/models/minimax/minimax-m2)
- [gpt-oss-120b (OpenRouter)](https://openrouter.ai/models/gpt-oss-120b)

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
[AI Prompt Examples](./prompts/).

### Prompts to Organize Workflows

Workflows can get rather complicated.
Often, it is helpful to organize them into human-size chunks to make them easier to manage and understand.

I experimented with developing a series of prompts to transform a workflow into its components. The functions do the work but need not be viewed in the workflow. The workflow should be a concise document that shows the steps and the results together. The following steps should begin with a workflow file, e.g. ​`workflow.R`.
The workflow prompt is included in
[AI Prompt Examples](./prompts/#organize-a-workflow).

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
- [AI Prompt Examples](./prompts/)

## Context Engineering

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

### Context Engineering References

- [Agent Skills for Context Engineering (Murat Cankoylan)](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering)
- [Antigravity Agent Skills](https://antigravity.google/docs/skills)
- [Antigravity Skills (CodeLabs)](https://codelabs.developers.google.com/getting-started-google-antigravity#8)
- [Claude Skills](https://claude.com/skills)
- [Anthropic Skills](https://github.com/anthropics/skills)
& [Anthropic Context Engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents).
- [AgentSkills.io](https://agentskills.io/home)
- [GitHub Topics: agent-skills](https://github.com/topics/agent-skills)

### Comparison of Agent Skills and AGENTS.md

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
