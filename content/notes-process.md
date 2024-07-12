+++
title = "How I make my online notes"
date = 2024-07-12
+++

In the spirit of sharing and open-source, I thought it might be helpful to share I make these free online notes.

<!-- more -->

## My tech stack

## My general workflow

I divide creating these notes into three main steps:

- Write: get the text content of the notes down
- Transfer: do the formatting required to get the notes to properly display on the website
- Polish: look over the notes and revise them, adding and removing content as necessary

In the first step, I write these notes: sometimes in my spare time, sometimes in class, I simply like sharing what I learn. My preferred tool for this is [Obsidian](https://obsidian.md/), although if you'd prefer an open-source tool instead, see [StackEdit](https://stackedit.io/). Both use the Markdown format for typesetting, which for most intents and purposes is just typing normal text with some additional formatting text. Obsidian and Stackedit also allow entering equations via [LaTeX](@/latex-math-tutorial.md) format: if you're not familar with that, it's the same format that you can copy from [Desmos](https://www.desmos.com/calculator) equations, and a visual editor is available [here](https://cortexjs.io/mathlive/demo/). Sometimes, I directly edit in a code editor and use the live-preview feature of Zola to preview what I am editing.

In the second step, I have to actually transfer my notes to my website, which is more complicated than it seems. Due to discrepancies between the markdown format used by Zola and that used by most markdown editors, I use a regular expression to do a few replacements. For this, I simply go to <https://regex101.com>, go to substitution mode, input the regex (regular expression) `\$\$(.+?)\$\$` with options `/msg`, the replacement `{% math() %}$1{% end %}`, and paste in my draft in Obsidian. Then, in the substitution box, I can see my result, and verify that it is correct. Once I am satisfied, I can simply create another article in the `content/` folder. I can also do the same in VS Code, just with the slightly modified search regex `\$\$([\s\S\n]+?)\$\$` (thanks to [this article](https://www.waldo.be/2022/01/31/multi-line-text-search-in-vscode-with-regex/) for its tip) and enabling the regex search option, then choosing "replace all". This is convenient for batch-converting a folder of notes written in Obsidian to my website's format.