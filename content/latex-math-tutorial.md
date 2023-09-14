+++
title = "LaTeX math tutorial"
date = 2023-09-14
+++

LaTeX is a powerful language used for writing academic papers. In this article, we'll focus not on the full language, but only the portions relevant to math typesetting.

<!-- more -->

In this article, there will be one code block for the LaTeX code, as well as one equation block right after with the rendered results.

## Basic equations

Variables in LaTeX can be written much as you'd expect:

```
x + y
```

$$
x + y
$$

You can add multiplication with `\times` or `\cdot`:

```
3 \times 3 = 9
```

$$
3 \times 3 = 9
$$

```
4 \cdot 1 = 4
```

$$
4 \cdot 1 = 4
$$

Fractions are written with `\frac{}{}`, with the first argument being the numerator, and second argument being the denominator:

```
\frac{3x + 1}{x^2}
```

$$
\frac{3x + 1}{x^2}
$$

Superscripts are written with `^` and subscripts are written with `_`:

```
E = mc^2
```

$$
E = mc^2
$$

```
x_i = 3
```

$$
x_i = 3
$$

If we have some content inside of a superscript or subscript, we wrap it in curly braces `{}`:

```
x_{i + 1} = x_i + 1
```

$$
x_{i + 1} = x_i + 1
$$

Sums are written with `\sum` followed by the starting index on the subscript and the ending index on the superscript:

```
\sum_{i = 0}^n i
```

$$
\sum_{i = 0}^n i
$$

Derivatives and integrals can be written like this:

```
\frac{dy}{dx}
```

$$
\frac{dy}{dx}
$$

```
\int \limits_0^5 x^2 dx
```

$$
\int \limits_0^5 x^2 dx
$$

Text can be rendered with `\text{}` or `\mathrm{}`:

```
x = 3 \text{ or } x = -5
```

$$
x = 3 \text{ or } x = -5
$$

Sine, cosine, and tangent each have their respective functions:

```
2 \sin(x) + 5 \cos(x) - \tan(x)
```

$$
2 \sin(x) + 5 \cos(x) - \tan(x)
$$

Square roots can be written with `\sqrt{}`:

```
\sqrt{x + 5}
```

$$
\sqrt{x + 5}
$$

And nth roots can be written with `\sqrt[n]{}`:

$$
\sqrt[3]{81}
$$

```
\sqrt[3]{81}
```

Natural log is denoted by `\ln` and log by `\log`:

```
\ln (x) = \log_e (x)
```

$$
\ln (x) = \log_e (x)
$$

That should be enough for a working knowledge of LaTeX math!
