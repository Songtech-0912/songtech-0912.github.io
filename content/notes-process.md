+++
title = "How I make my online notes"
date = 2024-07-12

[extra]
non_note = true
+++

In the spirit of sharing and open-source, I thought it might be helpful to share I make these free online notes.

<!-- more -->

## My tech stack

This website is self-contained, with its only dependency being [Zola](https://www.getzola.org/), a high-performance static site generator written in Rust. Zola takes a folder of mostly text files written in [markdown](https://www.markdownguide.org/getting-started/), and outputs a beautiful website. This makes for excellent developer peace of mind: I just need to focus on writing the notes, not on coding or debugging.

The website uses very few other dependencies. It embeds the [Inter](https://rsms.me/inter/) font and the [KaTeX](https://rsms.me/inter/) library for rendering math equations. It also uses a few custom markup tags for specialized content. For instance, math equations are typeset via this markup:

```jinja
# Block math
{%/* math() */%}
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
{%/* end */%}

# Inline math (more robust than the other $...$ syntax)
{%/* inlmath() */%} E = mc^2 {% end %}
```

## My general workflow

I divide creating these notes into three main steps:

- Write: get the text content of the notes down
- Transfer: do the formatting required to get the notes to properly display on the website
- Polish: look over the notes and revise them, adding and removing content as necessary

In the first step, I write these notes: sometimes in my spare time, sometimes in class, I simply like sharing what I learn. My preferred tool for this is [Obsidian](https://obsidian.md/), although if you'd prefer an open-source tool instead, see [StackEdit](https://stackedit.io/). Both use the Markdown format for typesetting, which for most intents and purposes is just typing normal text with some additional formatting text. Obsidian and Stackedit also allow entering equations via [LaTeX](@/latex-math-tutorial.md) format: if you're not familar with that, it's the same format that you can copy from [Desmos](https://www.desmos.com/calculator) equations, and a visual editor is available [here](https://cortexjs.io/mathlive/demo/). Sometimes, I directly edit in a code editor like [VS Code](https://code.visualstudio.com/) and use the live-preview feature of Zola to preview what I am editing.

In the second step, I have to actually transfer my notes to my website, which is more complicated than it seems. Due to discrepancies between the markdown format used by Zola and that used by most markdown editors, I use a regular expression to do a few replacements. For this, I simply go to <https://regex101.com>, go to substitution mode, input the regex (regular expression) `\$\$(.+?)\$\$` with options `/msg`, set the replacement string to `{% math() %}$1{%/* end */%}`, and paste in my draft copied from Obsidian. Then, in the substitution box, I can see my result, and verify that it is correct. Afterwards, I can just paste in my sections one by one, and Regex101 will automatically give me the correctly-formatted output. 

But text and equations only are boring! So I use the [Obsidian excalidraw plugin](https://github.com/zsviczian/obsidian-excalidraw-plugin) to draw diagrams. I then convert my excalidraw drawings over by using the [auto SVG export feature](https://forum.obsidian.md/t/has-anyone-succeeded-in-publishing-excalidraw-drawings/55587/9) of Obsidian's excalidraw plugin, and using the regex of `\!\[\[(.+?)\.excalidraw\]\]` with options still set as `/msg`, with the replacement string `![]($1.excalidraw.svg)`. Once I am satisfied, I can simply create another article in the `content/` folder. I can also do the same in VS Code, just with the slightly modified search regex `\$\$([\s\S\n]+?)\$\$` (thanks to [this article](https://www.waldo.be/2022/01/31/multi-line-text-search-in-vscode-with-regex/) for its tip) and enabling the regex search option, then choosing "replace all". This is convenient for batch-converting a folder of notes written in Obsidian to my website's format. Finally, it is sometimes helpful to make sure that the math blocks are delimited by a newline before any other content; this is important for ensuring consistent formatting. In VS Code, this can be automatically done with the search regex `\{% end %\}(\n\w)` and the replace regex `{% end %}\n$1` applied to all files in the `content/` folder.