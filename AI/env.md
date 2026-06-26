# AI Environments

We typically work with AI within an environment.
Most "traditional" tools are now flavored with AI suggestions,
including messaging and email apps
(which can be optionally turned off).
There are now innumerable AI tools for coding and analysis,
and this will not be a compendium.
Instead, I am trying to keep abreast of the landscape
that seems relevant to me,
and will add notes here as I learn more.

- [What is an AI Environment?](#what-is-an-ai-environment)
- [Integrated Development Environments (IDEs)](#integrated-development-environments-ides)
  - [Cloud-Based Research Environments](#cloud-based-research-environments)
  - [Google Gemini and Antigravity](#google-gemini-and-antigravity)
  - [Other AI Environments](#other-ai-environments)
- [Agentic AI](#agentic-ai)
- [Large Language Models](#large-language-models)
  - [What are large language models (LLMs)?](#what-are-large-language-models-llms)
  - [What are AI tokens?](#what-are-ai-tokens)
  - [What is a Mixture of Experts (MoE)?](#what-is-a-mixture-of-experts-moe)
  - [Open Source LLMs](#open-source-llms)
- [What is an AI Harness?](#what-is-an-ai-harness)

## What is an AI Environment?

An AI environment is a setting where artificial intelligence systems operate and interact with data and users.
It includes hardware, software, data, and algorithms that facilitate AI functions.
Environments can be physical (like robots) or virtual (like simulations or cloud platforms).
AI environments allow for real-time interaction and feedback between AI systems and their surroundings.
They often incorporate machine learning capabilities, enabling AI to adapt and improve over time.
Common applications include autonomous vehicles, smart homes, and virtual assistants.
([Google Gemini](https://gemini.google.com))

- [Types of Environments in AI (Geeks4Geeks)](https://www.geeksforgeeks.org/artificial-intelligence/types-of-environments-in-ai/)
- [What is an Environment in AI (Analytics Vidhya)](https://www.analyticsvidhya.com/blog/2026/01/types-of-environments-in-ai/)
- [Environment in AI (ScholarHat)](https://www.scholarhat.com/tutorial/artificialintelligence/environment-in-ai)
- [What is Environment in AI: A Complete Guide (KeyGroup)](https://key-g.com/blog/what-is-environment-in-ai-types-of-environments-in-ai-a-complete-guide)

## Integrated Development Environments (IDEs)

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

### Cloud-Based Research Environments

Cloud-based research environments enable researchers,
including students and instructors,
to develop code, optionally with AI agent interactions,
without having to try to set up systems on their
own, idiosyncratic devices.

For those working directly in
[GitHub](../github/),
code generation within repos is improving with the nuanced integration of
[GitHub Copilot](https://github.com/features/copilot),
both for repo editing and for use in
[GitHub Codespaces](https://github.com/features/codespaces),
which is a cloud-based IDE optionally
integrated with each GitHub repo.
GitHub also has capabilities to publish
[GitHub Pages](../github/#github-pages),
such a personal or organization portfolios.

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
[Recovering Antigravity Conversations](../recover_conversations.md)
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
  - [Recovering Antigravity 1.x Conversations](../recover_conversations.md)

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

See caution in [Using R in VS Code with Radian](../radian.md)
about `radian` and AI environments.

## Agentic AI

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
- [Agent-Environment Interface in AI](https://www.geeksforgeeks.org/artificial-intelligence/agent-environment-interface-in-ai/)
- [Multi-Agent Orchestration Guide](https://www.agensi.io/learn/multi-agent-orchestration-guide)
- [Agentic Engineering (Jaymin West)](https://www.jayminwest.com/agentic-engineering-book/)

## Large Language Models

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

### What are large language models (LLMs)?

- [IBM](https://www.ibm.com/think/topics/large-language-models)
- [GeeksforGeeks](https://www.geeksforgeeks.org/artificial-intelligence/large-language-model-llm/)
- [AWS](https://aws.amazon.com/what-is/large-language-model/)

### What are AI tokens?

LLMs work by encoding text into numerical representations (tokens), then decoding them back into text.
According to
[Google Gemini](https://gemini.google.com)
AI tokens are units of data used in natural language processing models to represent words or phrases.
Tokenization is the method of breaking down text into smaller components (tokens) for easier analysis and understanding.
Encoding converts text into tokens that the AI model can understand.
Tokens can be words or subwords (or images or audio snippets, etc.),
which are converted into numerical representations (embeddings) that capture their meanings.
Token embeddings can carry contextual meanings, allowing models to understand nuances in language.
The model processes (contextualizes) embeddings through multiple layers to understand context and relationships among tokens.

The model generates output tokens based on the processed information, predicting the next token in the sequence.
Decoding reverses the process, transforming tokens back into human-readable form.
AI tokens are used in various applications, including chatbots, translation services, and content generation.
Each model has a maximum token limit, which can affect the amount of text processed at once.
The choice of tokenization method can significantly impact the performance and accuracy of AI models.
The model can be further trained on specific tasks to improve its performance in generating relevant responses.

- [Understanding Encoder-Only and Decoder-Only Transformer Models (Sebastian Raschka)](https://magazine.sebastianraschka.com/p/understanding-encoder-and-decoder)
- [What Are AI Tokens? (NVIDIA)](https://blogs.nvidia.com/blog/ai-tokens-explained/)
- [What Are AI Tokens? How Models Read Text, Images & Code (Aiinsights)](https://aiinsightsnews.net/what-are-tokens-in-ai/)
- [Tokens Explained: The New Currency of Generative AI (Sentisight)](https://www.sentisight.ai/tokens-explained-new-currency-of-generative-ai/)
- [The Invisible Building Blocks of AI: What You Need to Know About Tokenization (Medium: Data Science Collective)](https://medium.com/data-science-collective/the-invisible-building-blocks-of-ai-what-you-need-to-know-about-tokenization-acadd86a63ba)
- [gpt-tokenizer playground](https://gpt-tokenizer.dev/)

### What is a Mixture of Experts (MoE)?

- [Maarten Grootendorst](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-mixture-of-experts)
- [GeeksforGeeks](https://www.geeksforgeeks.org/nlp/what-is-mixture-of-experts-moe/)
- [Hugging Face](https://huggingface.co/blog/moe)
- [Siyuan Mu and Sen Lin (2026)](https://arxiv.org/abs/2503.07137)

### Open Source LLMs

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

## What is an AI Harness?

According to
[Andrew Maynard](https://andrewmaynard.net/),
"the crystallizing moment came in early February 2026, when Mitchell Hashimoto — cofounder of HashiCorp and creator of
[Terraform](https://developer.hashicorp.com/terraform)
— published a blog post that gave the ... name ... “harness engineering”....
“It is the idea that anytime
you find an agent makes a mistake, you take the time to engineer a solution such that the agent
never makes that mistake again”
[(Hashimoto, 2026)]((https://mitchellh.com/writing/my-ai-adoption-journey)). ...
And on February 18, Ethan Mollick’s widely read guide to AI both popularized and started
the process of normalizing the term as it organized its entire framework around three concepts:
“Models, Apps, and Harnesses”
[(Mollick, 2026)](https://www.oneusefulthing.org/p/a-guide-to-which-ai-to-use-in-the)."

As stated by Jaymin West,
"Ethan Mollick introduced the horse harness metaphor to explain why the term is well-chosen (Mollick, ~2026-Q1). A horse has raw physical capability — strength, speed, endurance. But raw capability cannot pull a plow, draw a carriage, or haul freight without a harness. The harness converts raw power into directed, controlled, useful work."
Sarah Chen stated,
"The Large Language Model (LLM) is a powerful horse, enormous raw capability, but no sense of direction, no understanding of boundaries, and no concept of “stop.” The harness is the bridle, reins, and saddle. It channels that power into controlled, useful work. Without it, the horse runs wherever it wants."

[Google Gemini](https://gemini.google.com)
attributed the horse metaphor for AI harness
to the late
[John McCarthy](http://jmc.stanford.edu/),
founder of the field of AI,
although I have not been able to find the term connected
with his name.
Interestingly, there is a horse photographer named
[Jon McCarthy](https://www.jonmccarthyphoto.com/),
and a (deceased) noted breeder of Irish Draft Horses named
[John McCarthy](https://chronofhorse.com/en/article/john-mccarthy/)
Perhaps Gemini conflated these?

- [My AI Adoption Journey (Mitchell Hashimoto)](https://mitchellh.com/writing/my-ai-adoption-journey)
- [A Guide to Which AI to Use in the Agentic Era (One Useful Thing, Ethan Mollick)](https://www.oneusefulthing.org/p/a-guide-to-which-ai-to-use-in-the)

Here are some other analogies:

- "The model is commodity. The harness is moat.” (Sarah Chen)
- "The model is the engine. The harness is the car." (Grant Harvey)

According to [Google Gemini](https://gemini.google.com),
An AI harness is a framework designed to integrate AI capabilities into applications.
It provides tools and resources for developers to build and deploy AI models efficiently.
The harness often includes pre-built algorithms and data processing pipelines.
It facilitates the management of AI workflows, from training to deployment.
AI harnesses can enhance collaboration among data scientists and engineers.
They help streamline the process of scaling AI solutions across different environments.

- [Complete Guide to Agent Harness: What It Is and Why It Matters (Sarah Chen, Harness Engineering)](https://harness-engineering.ai/blog/agent-harness-complete-guide/)
- [What is Harness Engineering? (Emily Winks, atlan)](https://atlan.com/know/what-is-harness-engineering/)
- [AI Harnesses and CLIs, Explained (Grant Harvey, eero)](https://www.theneuron.ai/explainer-articles/ai-harnesses-and-clis-explained-the-real-reason-everyones-talking-about-infrastructure/)
- [What is a Harness? (Agentic Engineering, Jaymin West)](https://www.jayminwest.com/agentic-engineering-book/6-harnesses/1-what-is-a-harness)
- [What the Rapid Adoption of the “Harness” Metaphor in Artificial Intelligence Reveals About How We Conceptualize Human–AI Relations (Andrew Maynard)](https://andrewmaynard.net/what-the-rapid-adoption-of-the-harness-metaphor-in-artificial-intelligence-reveals-about-how-we-conceptualize-human-ai-relations/)
