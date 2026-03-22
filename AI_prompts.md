# AI Prompt Examples

How will you later remember how you used AI to advance your project? And how will you share your learning with others?
Here are some examples of prompts that I have used with AI agents to help me with my work.
They illustrate a few principles along the way.

- [Prompt engineering](https://www.promptingguide.ai/introduction/what-is-prompt-engineering)
- [Getting Started with Prompts](https://tyson-swetnam.github.io/intro-gpt/prompts/#getting-started-basic-prompt-structure)

If you just use prompts and don't keep track of them, you are missing an opportunity to easily document your work flow.
A simple way to begin is to ask your AI agent to save your prompts in a file, e.g. `prompts.md`;
alternatively, or in addition, save the Walkthrough artifact that the AI agent creates into
a separate `walkthrough.md` file.
If you do more work within the same conversation, ask the AI agent to update these files.
Below are examples of prompts I have been developing.

## Table of Contents

- [Saving Prompts and Walkthroughs](#saving-prompts-and-walkthroughs)
- [Create a README.md for a Folder](#create-a-readmemd-for-a-folder)
- [Create a Table of Contents for a File](#create-a-table-of-contents-for-a-file)
- [Convert DOCX files to Markdown](#convert-docx-files-to-markdown)
- [Commit to GitHub multiple versions of an R file](#commit-to-github-multiple-versions-of-an-r-file)
  - [Improved Multiple Versions Prompt](#improved-multiple-versions-prompt)
  - [Key Improvements Made](#key-improvements-made)
- [Resolve Git Hell Conflicts](#resolve-git-hell-conflicts)
- [Organize a Workflow](#organize-a-workflow)
  - [Workflow Prompt](#workflow-prompt)

## Saving Prompts and Walkthroughs

**Prompts:**

- "save the prompts used in this conversation to `prompts.md`"
- "save the walkthrough to `walkthrough.md`"

You can do this at the beginning or end of a conversation.
You can do it by clicking the `Save` button in the top right corner of the conversation window, and the `Export` button on a walkthrough panel.
You can also (by hand or by prompt to AI) update or append to these files.

**Examples:**

- [sysgenAnalysis workflow walkthroughs](https://github.com/AttieLab-Systems-Genetics/sysgenAnalysis/blob/main/inst/doc/walkthrough.md#workflow-walkthroughs)
- [mkeller3Projects2: how I created this file and repo](https://github.com/AttieLab-Systems-Genetics/mkeller3Projects2/tree/master#how-i-created-this-file-and-repo)
- [sysgenDO1200 prompts](https://github.com/AttieLab-Systems-Genetics/sysgenDO1200/blob/main/prompts.md)

## Create a README.md for a Folder

**Prompts:**

- "create a `README.md` document that concisely summarizes contents of this folder at a high level"
- "update `README.md` with any additional files, obeying restrictions in `.gitignore`"

**Example:**

- [mkeller3Projects2](https://github.com/AttieLab-Systems-Genetics/mkeller3Projects2/blob/master/README.md)
- [sysgenDO1200](https://github.com/AttieLab-Systems-Genetics/sysgenDO1200/blob/main/README.md) has various examples

## Create a Table of Contents for a File

Just as you can create a `README.md` for a folder, you can create a table of contents for that `README.md` (or any markdown) file.

**Prompts:**

- "create TOC for `README.md`"
- "update TOC for `README.md`"

**Example:**

- [README for this repo](https://github.com/byandell/Documentation/blob/main/README.md)
- [Table of Contents for this file](AI_prompts.md#table-of-contents)
- [Pipelines in mkeller3Projects2](https://github.com/AttieLab-Systems-Genetics/mkeller3Projects2/blob/master/README.md#pipelines)

Once you have these and establish a "culture" of updating them, the AI will sometimes make the changes on the fly as you evolve your material.

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
The first time, I forgot to `git pull` changes I made on `GitHub` before starting. I tried to solve by myself and got lost. AI sorted it out.

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

Below is a copy of the workflow prompt used in the sysgenAnalysis repository.

### Workflow Prompt

**Goal**: Refactor a [workflow] into a modular R package structure.

**Instructions**:

0. **Set the [workflow] and [basename] variables from user input**:
    - [workflow]: The name of the workflow to refactor .
    - [basename]: The `basename` to use for the refactored workflow.

1. **Understand the workflow**: Read the [workflow] and understand what it does.

2. **Extract Functions**: Move all logical units (data processing, analysis, plotting) into `R/[basename].R`.
    - Document each function with **Roxygen2** syntax (including `@param`, `@return`, and `@export`).
    - Use R native pipes (`|>`) and explicit namespace calls (e.g., `dplyr::mutate`).
    - Centralize shared constants (like coordinate maps) if not already in `common.R`.

3. **Create Entry Script**: Create an execution script `inst/scripts/analyze_[basename].R`.
    - Use it as a clean entry point that calls the functions defined in `R/`.
    - Handle environment setup, file paths, and high-level execution flow here.

4. **Return S3 Objects**: Refactor the main "run" function to return an S3 object of class `[basename]_analysis`.
    - Implement `print`, `summary`, and `plot` methods in `R/[basename].R`.
    - Move file-saving logic (`write.csv`, `ggsave`) out of the functions and into the entry script.

5. **Verify Integration**: Check package and scripts, correcting any issues that arise.
    - Verify documents with `devtools::document()`.
    - Build the package.
    - Ask user whether or not to run the analyze_[basename].R script to make sure it works.

6. **Create Exploration Document**: Create a Quarto document `inst/scripts/explore_[basename].qmd` to explore the results saved by the analysis script.
    - Use `sysgenAnalysis::read_[basename]_analysis(output_path)` to reconstruct the S3 object from CSV files.
    - Focus on visualization and interactive summaries using the S3 methods (`print`, `summary`, `plot`).
    - This approach ensures that exploration is fast (no re-running analysis) and transparent (uses human-readable CSVs).

**Requested Files**:

- `R/[basename].R`
- `inst/scripts/analyze_[basename].R`
- `inst/scripts/explore_[basename].qmd`
