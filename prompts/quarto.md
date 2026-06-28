# Quarto Prompts

The
[detailed prompt](#detailed-prompt)
was developed over multiple iterations to convert
[prompts/](https://github.com/byandell/Documentation/blob/main/prompts/)
into a quarto slide deck using AI.
The `.gitignore` file was updated early on, but is listed at the end.
The second-to-last prompt in the list below was for
[AI/](https://github.com/byandell/Documentation/blob/main/AI/).
Once developed and in the AI context window, the
[simpler prompt](#simpler-prompt)
was used to create other quarto slide decks.
The
[update prompt](#update-prompt)
was used to update an existing quarto slide deck.

## Prompts

### Detailed Prompt

- Create a quarto slide deck  using `/prompts/README.md` and place it in folder `quarto/prompt.qmd`.
- Change quarto/prompt.qmd from dark to light mode.
- Modify quarto slide deck to use smaller font in slide contents to fit on each slide.
- The purple quoted text is the wrong size in the slides.
- Remove numbering from markdown boxes. Wrap long lines on slides 9 and 13.
- On "CRAFT Framework" slide, "Example: Grant Proposal" markdown block needs some line brakes. Similarly for "GitHub Prompts" slide "Multi-Version" markdown.
- For CRAFT Framework slide, put markdown below the unordered list and widen it. Compress unordered list so all fits neatly on one slide.
  - No. Unordered list on that slide should be one per line.
  - You had more information on what what CRAFT elements were in unordered list. Please add that back in.
- Change Organizing a Workflow slide to have one column.
- Please put callouts at bottom of each slide when possible, avoiding 2-column layouts.
- Update `.gitignore` for quarto documents.

### Simpler Prompt

- Create a quarto slide deck from `[docname]` in light mode and place it in folder
  `quarto/[docname].qmd`.
- Adjust slide styling to use a more compact layout so that content fits neatly on each slide.

### Update Prompt

Modify `quarto/github.qmd` using updated `github/`. Include links where possible.

**Response:**

## Create quarto slide deck

I have created a Quarto slide deck based on the contents of [AI_prompts.md](file:///Users/brianyandell/Documents/GitHub/Documentation/AI_prompts.md).

Here is a summary of the files created and configured:

1. **Quarto Slide Deck**: [quarto/prompt.qmd](file:///Users/brianyandell/Documents/GitHub/Documentation/quarto/prompt.qmd)
   - Converted to the modern web-based **Reveal.js** format.
   - Structured into logical sections using background-colored slide breaks (`# Section Title {background-color="..."}`).
   - Utilizes advanced Quarto features such as column layouts (`::: {.columns}`), callout boxes, and incremental lists (`::: {.incremental}`).
   - Adjusted all relative file links to match the new subdirectory structure.

2. **Custom Presentation Styling**: [quarto/custom.scss](file:///Users/brianyandell/Documents/GitHub/Documentation/quarto/custom.scss)
   - Designed a premium dark-mode aesthetic using Slate and Sky/Rose accents.
   - Customized typography using modern sans-serif fonts (`Outfit`, `Inter`).
   - Added glowing shadows and rounded borders to code blocks, and styled Quarto callouts nicely to pop against the dark background.

3. **Rendered Output**: [quarto/prompt.html](file:///Users/brianyandell/Documents/GitHub/Documentation/quarto/prompt.html)
   - Compiled using `quarto render` to ensure syntax validity. It rendered successfully without errors.

### Slide Structure Overview

- **Section 1: Introduction & Core Concepts**
  - *Documenting AI Workflows*: Core principles of saving prompt/walkthrough files.
  - *Prompt Engineering Resources*: Reference links and guides.

- **Section 2: Saving Prompts & Agent Conversations**
  - *Saving Prompts and Walkthroughs*: Practical commands and real-world repository examples.
  - *AI Agent Conversation Structure*: Multi-turn prompt chaining and version control.
  - *System Instructions*: Config examples for Python (`scikit-learn` & `pandas`) and R (`tidyverse`).
  - *The CRAFT Framework*: Context, Role, Action, Format, and Tone, with the grant proposal example.
- **Section 3: Practical Prompt Examples**
  - *Documenting Files & Folders*: Automated README and TOC generation prompts.
  - *Convert DOCX to Markdown & Slides*: Pandoc conversion and Reveal.js slide deck generation.
  - *GitHub Prompts (Versioning Files)*: R file multi-version commit workflow.
  - *GitHub Prompts (Git Conflict Resolution)*: The "Git Hell" walkthrough prompt.
  - *Organizing a Workflow*: Transforming R workflows into functions in packages.
  - *Folder Documentation in ResearchDrive*: Balancing private RD directories with public GitHub documentation.

## Light Mode

I have updated the presentation to light mode:

1. **Slide YAML & Sections**: Updated [quarto/prompt.qmd](file:///Users/brianyandell/Documents/GitHub/Documentation/quarto/prompt.qmd):
   - Configured `theme: [default, custom.scss]` (shifting the base from `dark` to `default` light).
   - Changed the slide section divider backgrounds from `#0f172a` (dark slate) to a soft, contrast-friendly light sky blue (`#e0f2fe`).

2. **Custom CSS Styling**: Completely rebuilt [quarto/custom.scss](file:///Users/brianyandell/Documents/GitHub/Documentation/quarto/custom.scss) to match light-theme guidelines:
   - **Background & Text**: Slate-50 background (`#f8fafc`) with Slate-800 text (`#1e293b`).
   - **Links**: High-contrast Sky-600 (`#0284c7`) and Rose-600 (`#e11d48`) on hover.
   - **Code Blocks**: Light-theme styled blocks (`#f1f5f9` backgrounds with Slate-900 border and code coloring).
   - **Callouts**: Styled borders and backgrounds with dark header text.

The slides rendered successfully to [quarto/prompt.html](file:///Users/brianyandell/Documents/GitHub/Documentation/quarto/prompt.html). Your running `quarto preview` process will automatically rebuild and refresh the browser slide preview with these changes!

## Compact Layout

I have adjusted the slide styling in [quarto/custom.scss](file:///Users/brianyandell/Documents/GitHub/Documentation/quarto/custom.scss) to use a more compact layout so that content fits neatly on each slide:

1. **Base Font Size**: Reduced the base `.reveal` font size from `38px` to `30px`.
2. **Headers**:
   - Shrinked `h2` headings to `1.4em` (with reduced padding and margins).
   - Shrinked `h3` subheadings to `1.0em`.
3. **Code Blocks**: Reduced code font size inside preformatted blocks from `0.75em` to `0.65em` (with tighter line-height and padding).
4. **Lists**: Tighter margins for list items (`0.3em` instead of `0.4em`) and overall block margins.
5. **Callout Boxes**: Reduced margins (`0.5rem` instead of `1rem`) and slightly smaller header/body text sizes to conserve vertical space.

The presentation compiled successfully, and your running `quarto preview` will automatically reload the refreshed, compact light-mode slides!

## Resolve blockquote formatting

I have resolved the issue with the blockquote (quoted text) formatting in the slides by adding explicit custom rules in [quarto/custom.scss](file:///Users/brianyandell/Documents/GitHub/Documentation/quarto/custom.scss):

1. **Blockquotes (`blockquote`)**:
   - Fixed the size issue by scaling it down to `0.85em` relative to the slide's parent font size (the default Reveal.js blockquote is a very large `1.25em`).
   - Removed the default styling constraints (like centered text alignment and heavy shadows) and styled it as a clean callout box with a slate color (`#64748b`), light background (`#f1f5f9`), and a solid left border (`#cbd5e1`).

2. **Inline Code (`code:not(pre code)`)**:
   - Explicitly locked the font size of inline code elements to `0.85em` so it stays perfectly proportional to the surrounding text on all slides.

The presentation has compiled successfully to [quarto/prompt.html](file:///Users/brianyandell/Documents/GitHub/Documentation/quarto/prompt.html), and your live preview has been updated!

## Resolve markdown list and line wrapping issues

I have updated [quarto/prompt.qmd](file:///Users/brianyandell/Documents/GitHub/Documentation/quarto/prompt.qmd) as requested:

1. **Markdown Box Numbering**: Removed the numeric list `1.`, `2.`, `3.`, `4.` inside the ` ```markdown ` prompt code block under the *GitHub Prompts: Versioning Files* slide and replaced them with standard `-` bullets.
2. **Line Wrapping on Slides**: Inserted manual `<br>` breaks to wrap long prompt strings and blockquotes across the following slides:
   - **Slide 9 (Documenting Files & Folders)**: Split the folder README and TOC prompts.
   - **Slide 11 (Convert DOCX to Markdown & Slides)**: Split the PowerPoint generation prompt.
   - **Slide 13 (GitHub Prompts: Git Conflict Resolution)**: Split the multi-line "Git Hell" blockquote.
   - **Slide 14 (Organizing a Workflow)**: Split the workflow extraction blockquote.

The slides compiled without errors to [quarto/prompt.html](file:///Users/brianyandell/Documents/GitHub/Documentation/quarto/prompt.html) and your live preview browser tab has refreshed with the updated layout.

## Slide line breaks

I have introduced manual line breaks inside the code blocks on the **CRAFT Framework** and **GitHub Prompts** slides inside [quarto/prompt.qmd](file:///Users/brianyandell/Documents/GitHub/Documentation/quarto/prompt.qmd):

1. **CRAFT Framework slide (Example: Grant Proposal)**:

   ```markdown
   Context: Grant proposal for NSF funding
            on AI in education  
   Role: Experienced grant writer & researcher  
   Action: Review draft introduction
           and suggest improvements  
   Format: Feedback as tracked changes
           with explanations  
   Tone: Professional, constructive,
         and encouraging
   ```

2. **GitHub Prompts slide (Multi-Version Commit Prompt)**:

   ```markdown
   Find files ending in `[ _]v[0-9]+.R$`
   with matching base name.
   - If no `v1` exists but `basename.R`
     does, copy to `v1.R`.
   - Commit `basename.R` with message `v1`
     and original date.
   - For subsequent versions, copy the
     next version to `basename.R` and commit.
   - Keep versioned files intact.
   ```

The Quarto build successfully updated [quarto/prompt.html](file:///Users/brianyandell/Documents/GitHub/Documentation/quarto/prompt.html) and your live preview browser tab will now reflect these aligned line breaks!

## CRAFT Framework slide

I have modified the **CRAFT Framework** slide inside [quarto/prompt.qmd](file:///Users/brianyandell/Documents/GitHub/Documentation/quarto/prompt.qmd) as requested:

1. **Compressed CRAFT Elements**: Condenced the elements list into a single, compact inline list item:
   `**C**ontext (background) · **R**ole (persona) · **A**ction (task) · **F**ormat (structure) · **T**one (style)`
2. **Stacked Layout**: Removed the two-column division to stack the example block vertically below the compressed elements list.
3. **Widen Example Code Block**: Restored the wider, single-line format for the prompts in the code block since they now span the full width of the slide.

These modifications ensure that both the concepts and the example fit neatly on a single slide. The presentation has successfully rebuilt to [quarto/prompt.html](file:///Users/brianyandell/Documents/GitHub/Documentation/quarto/prompt.html).

### No. list items stacked on that slide

I have updated the **CRAFT Framework** slide layout inside [quarto/prompt.qmd](file:///Users/brianyandell/Documents/GitHub/Documentation/quarto/prompt.qmd):

1. **Vertical List**: Restored the list of CRAFT elements to be one item per line:
   - **C**ontext: Background
   - **R**ole: Persona
   - **A**ction: Task
   - **F**ormat: Structure
   - **T**one: Style
2. **Compressed Content**: Kept the definitions brief to minimize vertical space usage.
3. **Widen Example Code Block**: The full-width, single-line "Example: Grant Proposal" markdown block is positioned directly beneath the list.

The slide deck has successfully rebuilt to [quarto/prompt.html](file:///Users/brianyandell/Documents/GitHub/Documentation/quarto/prompt.html).

### Add definition of each element of CRAFT Framework

I have restored the original, detailed descriptions for each element of the **CRAFT Framework** in the vertical list structure on that slide:

- **C**ontext: Background information.
- **R**ole: Person/identity the AI assumes.
- **A**ction: The specific task to perform.
- **F**ormat: Deliverable structure.
- **T**one: Style of response.

The full-width "Example: Grant Proposal" code block remains positioned directly underneath it.

The slides successfully rebuilt to [quarto/prompt.html](file:///Users/brianyandell/Documents/GitHub/Documentation/quarto/prompt.html) and your live preview browser tab has refreshed to display the restored details. Solid styling overrides will ensure everything fits on this slide. Let me know if you would like any other adjustments!

Here is the updated narrative of changes in [quarto/narrative.md](file:///Users/brianyandell/Documents/GitHub/Documentation/quarto/narrative.md) for your records. (If you need me to help commit this, just let me know!)

Have a great rest of your day! Let me know if there are any other modifications needed. :)

*(To explore goals and long-running schedules in the future, you can always use the `/goal` or `/schedule` commands!)*

## Change Organizing a Workflow slide to have one column

I have updated the **Organizing a Workflow** slide in [quarto/prompt.qmd](file:///Users/brianyandell/Documents/GitHub/Documentation/quarto/prompt.qmd):

1. **Removed Columns**: Removed the two-column division tags (`::: {.columns}` and `::: {.column}`) so that the slide content is laid out in a single column.
2. **Vertical Stack**: The slide now flows sequentially from top to bottom:
   - **The Goal**: Details on R workflow packaging.
   - **The Prompt**: The file walkthrough prompt.
   - **Key Packages**: The callout block containing the package dependencies is now full-width below the prompt.

The slides successfully rebuilt without errors, and the output is located at [docs/quarto/prompt.html](file:///Users/brianyandell/Documents/GitHub/Documentation/docs/quarto/prompt.html). Your live preview has refreshed to show the updated single-column view!

## Callouts at bottom to avoid 2-column layouts

Following refers to [quarto/AI.qmd](https://byandell.github.io/Documentation/quarto/AI.html).

1. **Stacked Callout Layouts**: Removed the 2-column formatting on the following slides to place the callouts full-width at the bottom:
   - **How Might We Think About AI?** (*Social Collaboration* note at bottom)
   - **The Disrupted & Rethought Workforce** (*Core References* tip at bottom)
   - **Ethics & Environmental Impact** (*Call for Guardrails* warning at bottom)
   - **Connected Development Environments** (*Interactive Workflow* note at bottom)
   - **Google Gemini & Antigravity** (*Transition Note* warning at bottom)
   - **Prompt Engineering Fundamentals** (*Core References* tip at bottom)
   - **Context Engineering** (*Context Inflation* warning at bottom)
2. **Kept Non-Callout Columns**: Side-by-side structures that only display parallel lists (like the *Data Center Resources*, *Agentic AI*, *LLMs*, and *ResearchDrive* slides) remain in the side-by-side format.

The presentation has successfully re-compiled to [docs/quarto/AI.html](file:///Users/brianyandell/Documents/GitHub/Documentation/docs/quarto/AI.html).

## Update github slide deck

I have updated [quarto/github.qmd](file:///Users/brianyandell/Documents/GitHub/Documentation/quarto/github.qmd) using the details from [github.md](file:///Users/brianyandell/Documents/GitHub/Documentation/github.md) and compiled it back to [quarto/github.html](file:///Users/brianyandell/Documents/GitHub/Documentation/quarto/github.html).

### Summary of Changes

1. **Slide 1 (GitHub Pages & Blogging)**:
   - Replaced the single ESIIL subpage entry with the expanded subpage list containing clickable links to both pages and source repositories for:
     - [Documentation](https://byandell.github.io/Documentation) ([source](https://github.com/byandell/Documentation))
     - [geyser](https://byandell.github.io/geyser/) ([source](https://github.com/byandell/geyser))
     - [landmapyr](https://byandell-envsys.github.io/landmapyr/) ([source](https://github.com/byandell-envsys/landmapyr))
     - [esiil-stars](https://byandell.github.io/esiil-stars) ([source](https://github.com/byandell/esiil-stars))
     - [ESIIL](https://byandell.github.io/ESIIL) ([source](https://github.com/byandell/ESIIL))
   - Added links to **GitHub Pages Docs**, **GitHub Page Themes & Other Themes**, and **GitHub Actions** in the *Core References* callout box.

2. **Slide 2 (Jekyll, MkDocs & Git Resources)**:
   - Added a link to [Deploying your docs](https://www.mkdocs.org/user-guide/deploying-your-docs/) in the MkDocs section.
   - Restructured the *Git Troubleshooting & Help* list to incorporate specific Happy Git with R guides ([Get Started with GitHub](https://happygitwithr.com/usage-intro#usage-intro), [Git Troubleshooting](https://happygitwithr.com/troubleshooting)) and the [UW-Madison Data Science GitHub Links](https://github.com/UW-Madison-DataScience/R_for_data_sciences/blob/master/organize/github.md).

3. **Slide 3 (Posit Connect & Package Locking)**:
   - Added a link to [Manage dependencies with renv](https://www.r-bloggers.com/2021/03/new-on-techguides-manage-dependencies-with-renv/) in the *Documentation Links* callout box.

4. **Slide 5 (GitHub Codespaces)**:
   - Added a link to general [Codespaces Documentation](https://docs.github.com/en/codespaces) in the *Useful Links* section.

5. **Compilation**:
   - Successfully rendered the presentation to [quarto/github.html](file:///Users/brianyandell/Documents/GitHub/Documentation/quarto/github.html).

## Update .gitignore

I have updated the [.gitignore](file:///Users/brianyandell/Documents/GitHub/Documentation/.gitignore) file to ignore typical temporary and generated Quarto files:

```diff
 *.Rproj
+
+# Quarto
+.quarto/
+*_files/
+*_cache/
```

This ensures that Quarto's cache directories (`.quarto/`), auto-generated resource folders (like `prompt_files/`), and code execution caches (`*_cache/`) will not be tracked by Git.
