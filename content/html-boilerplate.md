+++
title = "My HTML boilerplate"
date = 2024-07-20

[extra]
non_note = true
+++

Starting an HTML file for a website or webapp can be a very frustrating process; it requires a lot of boilerplate. So this is one that I generally use, that I'm sharing here for hope that others might find it useful.

<!-- more -->

Here it is:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <!-- Set your page title here -->
  <title>Your title</title>
  <!-- Add in your css stylesheets here -->
  <link rel="stylesheet" href="yourstyle.css">
  <!-- Add in your favicon here or generate 
  	   from https://favycon.vercel.app/-->
  <link rel="icon" href="yourfavicon.ico">
  <!-- Meta tags - these are for webpage info, 
  	   edit to your liking -->
  <meta name="title" content="Your website title">
  <meta name="description" content="A website description">
  <!-- You can auto-generate meta tags 
  	   with a tool like https://metatags.io -->
</head>
<body>
  <div>Write your markup...</div>
  <!-- Add in your scripts here -->
  <script src="myscript.js"></script>
</body>
</html>
```
