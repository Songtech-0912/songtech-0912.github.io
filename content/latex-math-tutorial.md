+++
title = "LaTeX math tutorial"
date = 2023-09-14

[extra]
notoc = true
+++

LaTeX is a powerful language used for writing academic papers. In this article, we'll focus not on the full language, but only the portions relevant to math typesetting.

<!-- more -->

In this article, there will be one code block for the LaTeX code, as well as one equation block right after with the rendered results.

> **UPDATE:** See my dedicated [8-page guide to LaTeX](https://codeberg.org/elaraproject/elara-labs/raw/branch/main/tutorial-for-latex.pdf) for a more in-depth guide.

## Basic equations

Variables in LaTeX can be written much as you'd expect:

```
x + y
```

{% math() %}
x + y
{% end %}

You can add multiplication with `\times` or `\cdot`:

```
3 \times 3 = 9
```

{% math() %}
3 \times 3 = 9
{% end %}

```
4 \cdot 1 = 4
```

{% math() %}
4 \cdot 1 = 4
{% end %}

Fractions are written with `\frac{}{}`, with the first argument being the numerator, and second argument being the denominator:

```
\frac{3x + 1}{x^2}
```

{% math() %}
\frac{3x + 1}{x^2}
{% end %}

Superscripts are written with `^` and subscripts are written with `_`:

```
E = mc^2
```

{% math() %}
E = mc^2
{% end %}

```
x_i = 3
```

{% math() %}
x_i = 3
{% end %}

If we have some content inside of a superscript or subscript, we wrap it in curly braces `{}`:

```
x_{i + 1} = x_i + 1
```

{% math() %}
x_{i + 1} = x_i + 1
{% end %}

Sums are written with `\sum` followed by the starting index on the subscript and the ending index on the superscript:

```
\sum_{i = 0}^n i
```

{% math() %}
\sum_{i = 0}^n i
{% end %}

Derivatives and integrals can be written like this:

```
\frac{dy}{dx}
```

{% math() %}
\frac{dy}{dx}
{% end %}

```
\int \limits_0^5 x^2 dx
```

{% math() %}
\int \limits_0^5 x^2 dx
{% end %}

Text can be rendered with `\text{}` or `\mathrm{}`:

```
x = 3 \text{ or } x = -5
```

{% math() %}
x = 3 \text{ or } x = -5
{% end %}

Sine, cosine, and tangent each have their respective functions:

```
2 \sin(x) + 5 \cos(x) - \tan(x)
```

{% math() %}
2 \sin(x) + 5 \cos(x) - \tan(x)
{% end %}

Square roots can be written with `\sqrt{}`:

```
\sqrt{x + 5}
```

{% math() %}
\sqrt{x + 5}
{% end %}

And nth roots can be written with `\sqrt[n]{}`:

{% math() %}
\sqrt[3]{81}
{% end %}

```
\sqrt[3]{81}
```

Natural log is denoted by `\ln` and log by `\log`:

```
\ln (x) = \log_e (x)
```

{% math() %}
\ln (x) = \log_e (x)
{% end %}

That should be enough for a working knowledge of LaTeX math!
