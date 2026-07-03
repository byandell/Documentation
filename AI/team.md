---
title: "Team Science Platforms"
parent: "AI (Artificial Intelligence)"
nav_order: 3
---

# Team Science Platforms

Team Science Platforms have begun emerging
that promise to empower scientists to collaborate with each other
and with AI agents to accomplish complex tasks.
These include open source and commercial platforms,
as well as repositories focused on collaboration environments.
The [ESIIL team](https://esiil.org/our-team)
imagines using such platforms as
[digital twins](https://www.ibm.com/think/topics/digital-twin)
for some
[ESIIL Working Groups](https://esiil.org/working_groups).

One open challenge is whether it makes sense to
"go big" or "go small" ("go local")
in the design and implementation of these systems.
Going big may involve more sophisticated AI environments
with either larger and more powerful commercial LLMs and/or
open-source platforms.
Such a platform would have a natural language experience that orchestrates a team of AI agents,
each with its own role and expertise,
to accomplish a larger set of tasks.

These tend to be more expensive to implement, requiring more
resources (funding, expertise, energy and water) and more time.
Going small involves using smaller, open-source LLMs,
local platforms (say behind firewalls to respect data sovereignty)
and implementing smaller and simpler agentic systems.
Small systems may be easier to tailor and design an interface
but may be more stochastic (variable or even hallucinatory in response to prompts).

- [Agentic Repository](#agentic-repository)
- [Open Source Platforms](#open-source-platforms)
- [Commercial Platforms](#commercial-platforms)
- [Digital twins as a tool for ecosystem research (Trends in Ecol & Evol)](https://doi.org/10.1016/j.tree.2026.04.016)

## Agentic Repository

The
[Geospatial Harmonization with LLMs (CU-ESIIL)](https://cu-esiil.github.io/LLM_lesson_exemplar/)
project is an
[agentic repository](https://jfrog.com/learn/devops/agentic-repository/)
that contains:

- code
- data access patterns
- workflows
- and, critically, the rules that govern how an AI agent interacts with them.

At the core of this structure is a simple idea: if you want to use AI in science,
you must constrain it in the same way you constrain any computational system.
[Large language models (LLMs)](LLM.md)
enable teams to express intent in natural language and generate working code but they need guidance.
That means defining interfaces, expectations, and boundaries.

- [Geospatial Harmonization with LLMs (CU-ESIIL)](https://cu-esiil.github.io/LLM_lesson_exemplar/)

## Open Source Platforms

New open source platforms have emerged, notably
[OpenClaw](https://www.openclaw.ai/) and
[Hermes](https://hermes-agent.org/).
A science version of OpenClaw
[OASIS ScienceClaw](https://github.com/CU-ESIIL/openclaw_container)
is under development for scientific teams by ESIIL.
(See also
[ScienceClaw](https://github.com/beita6969/ScienceClaw).)
[PegasusAI](https://pegasus-ai.org/)
is a workflow system that uses
[Specification.md](https://specification.md/)
in a collaboration with
[HTCondor](https://htcondor.org/)
and
[PATh](https://path-cc.io/)
reported upon at
[High Throughput Computing Week 2026 (HTCondor)](https://agenda.hep.wisc.edu/event/2432/).

- [OpenClaw](https://www.openclaw.ai/)
- [Hermes](https://hermes-agent.org/)
- [ESIIL OASIS ScienceClaw](https://github.com/CU-ESIIL/openclaw_container)
- [ScienceClaw](https://github.com/beita6969/ScienceClaw)
- [PegasusAI](https://pegasus-ai.org/)
  - [Specification.md](https://specification.md/)
  - See slides at [HTCondor](https://htcondor.org/)
  for `High Throughput Computing Week 2026` (not posted yet)

## Commercial Platforms

Commercial platforms aimed at scientists are rapidly developing,
including
[Co-Scientist (DeepMind)](https://deepmind.google/blog/co-scientist-a-multi-agent-ai-partner-to-accelerate-research/),
[Claude Science (Anthropic)](https://claude.com/product/claude-science)
and
[Prism (OpenAI)](https://openai.com/index/introducing-prism/).
It is difficult to know how they will evolve and whether
they will replace or supplement current methods.

- [Co-Scientist: AI agents working in teams (DeepMind)](https://deepmind.google/blog/co-scientist-a-multi-agent-ai-partner-to-accelerate-research/)
  - [Accelerating scientific discovery with Co-Scientist (Nature)](https://doi.org/10.1038/s41586-026-10644-y)
  - [Generating novel scientific hypotheses with Co-Scientist (YouTube)](https://www.youtube.com/watch?v=aSY_vFFmkW0)
- [Claude Science (Anthropic)](https://claude.com/product/claude-science)
- [Prism (OpenAI)](https://openai.com/index/introducing-prism/)
