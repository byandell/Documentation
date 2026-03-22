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

## Table of Contents

- [Create a README.md for a Folder](#create-a-readmemd-for-a-folder)
- [Convert DOCX files to Markdown](#convert-docx-files-to-markdown)
- [Commit to GitHub multiple versions of an R file](#commit-to-github-multiple-versions-of-an-r-file)
  - [Improved Multiple Versions Prompt](#improved-multiple-versions-prompt)
  - [Key Improvements Made](#key-improvements-made)
- [Resolve Git Hell Conflicts](#resolve-git-hell-conflicts)
- [Organize a Workflow](#organize-a-workflow)

## Create a README.md for a Folder

**Prompts:**

- "create a `README.md` document that concisely summarizes contents of this folder at a high level"
- "update README.md with any additional files, obeying restrictions in .gitignore

**Example:**

- [mkeller3Projects2](https://github.com/AttieLab-Systems-Genetics/mkeller3Projects2/blob/master/README.md)
- [sysgenDO1200](https://github.com/AttieLab-Systems-Genetics/sysgenDO1200/blob/main/README.md) has various examples

## Convert DOCX files to Markdown

**Prompt:** "find `docx` files and use pandoc to convert them to `md` versions"

**Example:**

- [mkeller3Projects2](https://github.com/AttieLab-Systems-Genetics/mkeller3Projects2/blob/master/README.md)

## Commit to GitHub multiple versions of an R file

**Prompt:**
Find files ending in `[ _]v[0-9]+.R$`
that have the same name before this version.
If there is more than one set, do the following steps for each set.
Denote by `[basename]` the part of the filename before the version number.

1. If there is not a `v1` version but there is the `[basename]`
without a version, copy `[basename].R` to
`[basename] v1.R` or `[basename]_v1.R` as appropriate.
If there is already a `[basename] v1.R` or `[basename]_v1.R`,
do not overwrite it,
but instead copy the `v1` version to `[basename].R` for this set.
2. Commit `[basename].R` with message `v1` and the date this file was created.
(Be careful with files that have implicit `v1`.)
3. For subsequent versions, copy the next highest version number
to `[basename].R` and commit
with the next version number and the date this file was created.
Continue until all versions are committed.
4. Do not include the singleton files such as `source*v2.R`.
5. Make sure to keep the versioned files intact.

***

The above prompt is a great task for an AI or an automated script. The original prompt is logically sound but can be streamlined to be more "instructional" and clear about the desired state.
Below is an improved, more concise version of the prompt:

### Improved Multiple Versions Prompt

"**Reconstruct Git history for versioned R scripts** matching `[basename][ _]v[0-9]+.R`.

1. **Make sure to do a `git pull` first.**

For each set of files:

1. **Initialize v1**: If a `v1` file is missing but `[basename].R` exists, copy `[basename].R` to create the `v1` version. If `v1` already exists, overwrite `[basename].R` with its content to start the history.
2. **Commit Sequence**: For each version ($N = 1, 2, 3...$) in order:
    - Overwrite `[basename].R` with the content of version `vN`.
    - Commit `[basename].R` with message `vN`, using the file's original creation date as the commit timestamp.
3. **Safety Rules**:
    - Ignore singleton files (e.g., `source*v2.R`).
    - Keep all original versioned files (`v1`, `v2`, etc.) intact; do not delete them."

***

### Key Improvements Made

- **Logical Grouping**: Instead of listing steps as separate actions, it frames them as a single "Workflow for each set," which is easier for an AI to parse.

- **Clearer Conditional**: The "v1" logic is simplified into a "normalization" step that ensures the git history starts correctly regardless of whether the first version was named with a suffix or not.
- **Punchy Directives**: Uses bold headers (**Initialize**, **Commit Sequence**, **Safety Rules**) to make the constraints stand out.
- **Timestamp Clarity**: Explicitly mentions using the creation date as the "commit timestamp," which is the specific instruction needed for Git-based history reconstruction.

**Would you like me to help you execute this workflow on your current files?** I can see you have several matching sets like `MafA_SNP_DEG_Integration` and `Shiny app prototype for Mafa SNP DEG analysis`.

***

**Example:**

- [mkeller3Projects2](https://github.com/AttieLab-Systems-Genetics/mkeller3Projects2/blob/master/README.md)

## Resolve Git Hell Conflicts

**Prompt:** "i messed up and forgot to do `git pull` before commiting new files. Now I am in git hell. See the message with `git status`. `Walk me through how to fix this.`"

**Example:**
This was used on the Multiple Versions prompt above.

## Organize a Workflow

**Prompt:** "build a concise prompt that captures the essence of the walkthroughs in `inst/doc/walkthrough.md`"

**Example:**
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
