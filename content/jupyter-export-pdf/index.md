+++
title = "How to export PDFs from Jupyter notebooks"
date = 2025-02-12
+++

It can be a huge hassle trying to export a jupyter notebook to a PDF - there are some ways that involve needing to download hundreds of megabytes (or even gigabytes!) of packages! So I thought I would share the way I use, a very simple way that doesn't involve needing to install _anything_ and is incredibly fast and simple.

<!-- more -->

In the past, Jupyter notebooks allowed printing the notebook directly from the browser. This was very convenient; exporting PDFs from the browser took just 2 clicks. But starting with Jupyter notebook version 7, this option no longer worked. So instead, I came up with another method based on [this StackOverflow answer](https://stackoverflow.com/a/78390381).

The first step is to export your Jupyter notebook as an HTML file. To do so, go to the toolbar, and press `File > Save and Export Notebook As > HTML`. A picture of this is shown below:

{{ natural_img(
 src="./export-html-demo.png",
 desc="A picture of the toolbar in Jupyter notebook's interface, where you click the File > Save and Export Notebook As > HTML"
) }}

Jupyter should then automatically prepare an HTML file and download it for you. Locate the downloaded HTML file and move it to **the same directory as your Jupyter notebook**. This is important to make sure that you don't break any relative links (especially for images). Then, you can just use `Ctrl + P` (or `Command + P` on macs) to print the webpage as a PDF. I recommend setting the scale in the print dialog to be ~85% as the default setting makes for very large text on the PDF. Then save the PDF wherever you want - and you're done! A quick, easy method that is (relatively) hassle-free and doesn't require installing _anything_ whatsoever.