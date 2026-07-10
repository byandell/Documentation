---
title: "Check External Links"
parent: "Prompt Examples"
nav_order: 6
---

# Check External Links

This was developed to maintain the integrity of external links across the repository's documentation. Since the documentation site references many third-party tools, tutorials, packages, and research papers, it is essential to periodically scan all files and verify that these references are still valid and active.

The process parses all `.md`, `.qmd`, and `.Rmd` files, extracts HTTP/HTTPS URLs, cleans formatting and punctuation (including nested parentheses in Wikipedia links), and runs parallel network checks to identify dead or misconfigured links.

**Use**:
Run the script directly on the terminal to check external links across the repo. If you want an AI agent to check links, improve the tool, or scan specific files, use the prompt below.

**Prompt**:
"Use the link checker in
[scripts/check_links.py](../scripts/check_links.py)
to scan all documentation files (`.md`, `.qmd`, `.Rmd`) for broken links, or run `python3 scripts/check_links.py` to identify any broken URLs and check the generated report."

---

**Goal**: Extract and verify the validity of all external HTTP/HTTPS links in the repository.

**Instructions**:

1. **Scans Documentation files**:
   - Recursively search the repository for `.md` (Markdown), `.qmd` (Quarto), and `.Rmd` (R Markdown) files.
   - Skip hidden directories like `.git`, `.quarto`, `.Rproj.user`, and output dirs like `_site` or `site_libs`.

2. **Extracts and Cleans URLs**:
   - Identify all strings starting with `http://` or `https://`.
   - Clean trailing punctuation (`.`, `,`, `:`, `;`, `!`) and markdown formatting characters (`_`, `*`, `` ` ``, `~`).
   - Intelligently balance brackets/parentheses to correctly extract links containing parentheses (like Wikipedia pages: `https://en.wikipedia.org/wiki/R_(programming_language)`).
   - Ignore internal links, anchor hashes, and localhost domains (`localhost`, `127.0.0.1`).

3. **Verifies URLs in Parallel**:
   - Send requests concurrently using Python's `ThreadPoolExecutor` to speed up checking across thousands of URLs.
   - First, try an HTTP `HEAD` request with a custom web browser `User-Agent` (to prevent bot blocking).
   - If the `HEAD` request fails or returns a status code $\ge 400$, fall back to a `GET` request (using `stream=True` to avoid downloading full page bodies).
   - Classify responses with status codes $< 400$ as successful. Flag timeouts, connection issues, SSL errors, and status codes $\ge 400$ as broken.

4. **Outputs Results**:
   - Print a terminal summary of scan statistics.
   - If any broken links are found, write a detailed table in `link_check_report.md` detailing the file, line number, URL, status code or connection error, and optionally the Wayback Machine snapshot link if `--wayback-year` was specified.
   - Exit with code `1` if broken links exist, or code `0` if all links are working.

## Execution Guide

To run the link checker manually, execute the following command in the workspace root:

```bash
python3 scripts/check_links.py
```

### Advanced Usage

- **Check a single file**:

  ```bash
  python3 scripts/check_links.py --file README.md
  ```

- **Ignore SSL certificate errors** (useful if sites have expired certs but are otherwise active):

  ```bash
  python3 scripts/check_links.py --ignore-ssl
  ```

- **Increase/Decrease parallel threads** (default is 16):

  ```bash
  python3 scripts/check_links.py --threads 30
  ```

- **Set a custom timeout** (default is 10 seconds):

  ```bash
  python3 scripts/check_links.py --timeout 5
  ```

- **Specify a custom report output path**:

  ```bash
  python3 scripts/check_links.py --report custom_report.md
  ```

- **Fetch historical snapshots from the Wayback Machine**:
  To look up Wayback snapshots close to a specific year (e.g. 2017) for all broken links and append them as a column in the report:

  ```bash
  python3 scripts/check_links.py --wayback-year 2017
  ```

### Report Location

The report `link_check_report.md` is automatically created in the repository root if there are broken links. It is added to `.gitignore` so it will not be checked into Git commits.

## Addressing Broken Links

Here is a structured strategy for addressing the broken links identified in the file `link_check_report.md`. We can categorize them by the root cause and handle them accordingly:

### 1. Structure/Slug Changes (404 Not Found)

Many websites reorganize their documentation, causing old paths to break.
- **Examples from report**:
  - `https://www.promptingguide.ai/introduction/what-is-prompt-engineering` $\rightarrow$ now located at `https://www.promptingguide.ai/introduction` or `https://www.promptingguide.ai/basics/prompting`.
  - `https://esiil.org/working_groups` $\rightarrow$ renamed to use a hyphen: `https://esiil.org/working-groups`.
- **Fix**: Search the root domain of the site to locate the new path, then update the target file.

### 2. Scraping Block / Bot Prevention (403 Forbidden)

Some servers (e.g., Columbia University's `~gelman` directory) actively block programmatic/headless requests to prevent scraping, returning a `403 Forbidden` status even though the page works perfectly in a browser.
- **Fix**: Verify them manually in a browser. If they work, they do not need to be updated.
- **Enhancement**: We can update [check_links.py](file:///Users/brianyandell/Documents/GitHub/Documentation/scripts/check_links.py) to support an **Allowlist/Ignore List** for specific domains (like `columbia.edu` or `mcmaster.ca`) so they are skipped in future scans.

### 3. Expired or Misconfigured SSL Certificates

Links like `https://docs.cursor.sh/mcp` fail verification due to certificate expiry or custom domain configurations.
- **Fix**: Run the link checker with SSL verification disabled to see if the link is otherwise responsive:

  ```bash
  python3 scripts/check_links.py --ignore-ssl
  ```

  If it succeeds, the link is alive and can be left as-is.

### 4. Permanently Dead / Removed Content

Some tutorial files or academic papers (e.g., `http://www.stat.columbia.edu/~martin/W2024/R10.pdf`) may have been deleted or archived by their authors.
- **Fix Options**:
  - Check the `Wayback {Year} Link` column in `link_check_report.md` (generated by passing `--wayback-year` to the link checker) to find a working historical snapshot. If available, you can replace the broken link in the source document with this archive URL.
  - Search GitHub or Google for another host/mirror of the same document.
  - Replace the link with a newer, equivalent reference.

## Annotating Broken Links with Warning Glyphs

To make broken links visually identifiable to readers of the documentation site, you can append a warning glyph (like `⚠️`) to all broken URLs in the repository.

A utility script [add_glyphs.py](../scripts/add_glyphs.py) is provided to automate this:

```bash
python3 scripts/add_glyphs.py
```

### How it Works
1. Parses `link_check_report.md` to locate the files, line numbers, and broken URLs.
2. Appends a yellow warning sign glyph (` ⚠️`) directly to each broken URL's location.
3. Automatically inserts the glyph **outside** the markdown link parenthesis (i.e. `[Link text](url) ⚠️` or `<url> ⚠️`) to keep the markdown structural validity intact.
4. Safely handles multiple broken URLs on a single line by modifying them from right to left.
5. Is idempotent and prevents adding duplicate glyphs on subsequent runs.

---

### How we can proceed

If you want to start updating these, you can instruct me to fix a specific file or folder. For example:
> *"Help me fix the broken links in [AI/prompt.md](file:///Users/brianyandell/Documents/GitHub/Documentation/AI/prompt.md) and [AI/env.md](file:///Users/brianyandell/Documents/GitHub/Documentation/AI/env.md)"*

I will then use web search to find the correct active URLs, verify them, and update the markdown files directly. Would you like to do that for some of the files?

