---
title: "Embed Objects in GitHub Pages"
parent: "GitHub Pages"
nav_order: 1
---

# Embed Objects in GitHub Pages

The way to link an object file, such as a image, PDF, or dynamic HTML,
is to save it in a portfolio repo that is rendered via GitHub pages,
such as using a `[homepage].github.io`.
HTML files (ending in `.html`) do not display well in GitHub,
but will display via GitHub Pages.
This can be done using the `![ ]( )` markdown syntax
or an HTML
[iframe tag](https://www.w3schools.com/TAGS/tag_iframe.asp).
(Note that the HTML tag `embed` is deprecated and should not be used.)

## Displaying an Image

An image stored for GitHub Pages use is displayed using
`![QR Code](../images/adobe-express-qr-code.png)`
as shown with

![QR Code](../images/adobe-express-qr-code.png)

Simply linking to the image file
`[QR Code](../images/adobe-express-qr-code.png)`
will display it in another page when clicked.

[QR Code](../images/adobe-express-qr-code.png)

## Linking and Embedding PDFs

Use the following HTML code to link to the PDF in your webpage:

```
<a href="path/to/yourfile.pdf" target="_blank">View PDF</a>
```

Optionally, embed the PDF directly,
with options to adjust size and appearance,
using an
[iframe tag](https://www.w3schools.com/TAGS/tag_iframe.asp):

```
<iframe src="path/to/yourfile.pdf" title="Title for the PDF" width="100%" height="600px"></iframe>
```

## Linking an HTML Page

We use Western Meadowlark (_Tasiyagnunpa_) migration from
[cu-esiil-edu/stars-03-migration-template](https://github.com/cu-esiil-edu/stars-03-migration-template)
to explore access an HTML object.
We try to display the remote file,
then using GitHub Pages rendering the locally stored in this repo.
The
[local copy](tasiyagnunpa_migration.html)
does not display well in github, preview mode, or on the portfolio page.

Here are 2 versions of the same HTML file with an explicit link.
The latter does display as it is located in a GitHub repo rather than
published via GitHub Pages.

- [portfolio page](https://byandell.github.io/Documentation/images/tasiyagnunpa_migration.html) (renders in separate page)
- [portfolio repo](https://github.com/byandell/Documentation/blob/main/images/tasiyagnunpa_migration.html) (does not display on page)

## Embedding a Dynamic HTML Page

Here we embed the dynamic HTML page in this page:

<iframe src="../images/tasiyagnunpa_migration.html" title="Tasiyagnunpa Migration" width="100%" height="600px"></iframe>

**Note:**
This image will not display properly in `Preview` mode or in the GitHub repo,
but it will display on the published page
<https://byandell.github.io/Documentation/github/embed.html>
once the edits are committed to GitHub.

Here is the code used in this `README.md` document.
It is actually written in HTML that can be included in a markdown document.
Note the `width` and `height`, which can be tweeked.

```
<iframe src="../images/tasiyagnunpa_migration.html" title="Tasiyagnunpa Migration" width="100%" height="600px"></iframe>
```
