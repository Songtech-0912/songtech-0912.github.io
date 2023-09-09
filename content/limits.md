+++
title = "Notes on limits for calculus"
+++

These are notes taken during RPI's MATH 1010 course, on the topic of limits in calculus.

<!-- more -->

It is recommended to use `Ctrl F` or the equivalent search function to find the relevant section, as these notes are quite long.

## Investigating limits

The **limit** $L$ of a function as it approaches $c$ is the value the function tends towards as it approaches $x = c$:

$$
\lim_{x \to c} f(x) = L
$$

Note that $f(c)$ doesn't _have_ to equal $L$, only that the function tends to approach $L$ as $x$ approaches $c$.

For instance:

$$
g(x) = \begin{cases}
x^2 + 1, & x \neq 1 \\
0, & x = 1
\end{cases}
$$

Here, we see that $g(1) = 0$. However, as $x$ approaches 1, $g(x)$ approaches 2, so the limit is 2. So the value of the limit doesn't depend on the actual value of the function at a point (in fact many functions are undefined at certain points), only the value the function _approaches_ as it reaches a certain point.

## One-sided limits

One-sided limits are when a function only approaches $c$ from a certain direction.

The left-hand limit is defined as:

$$
\lim_{x \to c^-} f(x) = L_1
$$

The right-hand limit is defined as:

$$
\lim_{x \to c^+} f(x) = L_2
$$

A limit only exists if the left-hand and right-hand limits are **equal**.
