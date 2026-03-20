# AI Prompt Examples

How will you later remember how you used AI to advance your project? And how will you share your learning with others?
Here are some examples of prompts that I have used with AI agents to help me with my work.
They illustrate a few principles along the way.

- [Prompt engineering](https://www.promptingguide.ai/introduction/what-is-prompt-engineering),
- [Getting Started with Prompts](https://tyson-swetnam.github.io/intro-gpt/prompts/#getting-started-basic-prompt-structure).

If you just use prompts and don't keep track of them, you are missing an opportunity to easily document your work flow.
A simple way to begin is to ask your AI agent to save your prompts in a file, e.g. `prompts.md`;
alternatively, or in addition, save the Walkthrough artifact that the AI agent creates into
a separate `walkthrough.md` file.
If you do more work within the same conversation, ask the AI agent to update these files.
Below are examples of prompts I have been developing.

## Create a README.md for a Folder

Prompt: "create a `README.md` document that concisely summarizes contents of this folder at a high level"

Examples:

- [mkeller3Projects2](https://github.com/AttieLab-Systems-Genetics/mkeller3Projects2/blob/master/README.md) [private for now]
- [sysgenDO1200](https://github.com/AttieLab-Systems-Genetics/sysgenDO1200/blob/main/README.md) has various examples [private for now]

## Organize a Workflow

Prompt: "build a concise prompt that captures the essence of the walkthroughs in `inst/doc/walkthrough.md`"

Example:
The
[sysgenAnalysis](https://github.com/AttieLab-Systems-Genetics/sysgenAnalysis/)
workflow for organizing workflows (!) was developed organically.
Each day, I advanced the project through a series of prompts;
at the end of the session, I asked the AI agent to save the
[workflow walkthroughs](https://github.com/AttieLab-Systems-Genetics/sysgenAnalysis/blob/main/inst/doc/walkthrough.md#workflow-walkthroughs),
including the date of that step.
At some point, I asked AI the above prompt, which resulted in a comprehensive
[workflow prompt](https://github.com/AttieLab-Systems-Genetics/sysgenAnalysis/blob/main/inst/doc/walkthrough.md#workflow-prompt).
I later asked the AI agent to modify the workflow prompt as I added subsequent workflow steps.
This is still subject to some further refinement.

This particular prompt, which is described conceptually in
[Prompts to Organize Workflows](AI.md#prompts-to-organize-workflows),
transforms an R workflow into functions in an R package,
including a function to run the workflow and another function to explore the results.

- [sysgenAnalysis](https://github.com/AttieLab-Systems-Genetics/sysgenAnalysis/)
  - [workflow walkthroughs](https://github.com/AttieLab-Systems-Genetics/sysgenAnalysis/blob/main/inst/doc/walkthrough.md#workflow-walkthroughs)
  - [workflow prompt](https://github.com/AttieLab-Systems-Genetics/sysgenAnalysis/blob/main/inst/doc/walkthrough.md#workflow-prompt)
