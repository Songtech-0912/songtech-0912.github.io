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
x^2 + 1, & x \neq 1 \\\\
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

## Direct evaluation of limits

If a function is defined and continuous, then:

$$
\lim_{x \to c} f(x) = f(c)
$$

## Algebraic limits

Limits can oftentimes be solved algebraically. Limits are linear, which means that:

$$
\lim_{x \to c} (a f(x) \pm b g(x)) = a \lim_{x \to c} f(x) \pm b \lim_{x \to c} g(x)
$$
They also can be multiplied and divided (as long as the denominator $\neq 0$), and taken to the  power of:

$$
\lim_{x \to c} [f(x)]^{p/q} = (\lim_{x \to c} f(x))^{p/q}
$$

(here note that $q \neq 0$)
Algebraic limits work for **algebraic limits** only - that is, if a function is composed of polynomials, roots, rationals (fractions), and powers.

## Continuity

A function is continuous if you can draw its graph without lifting your pencil and without retracing any part of the curve throughout an interval. Otherwise, it is said to have a **discontinuity**, which can be one of several types:

- Jump
- Hole (also called a "removable discontinuity")
- Infinite discontinuity (asymptote)
- Oscillating discontinuity

The formal test of continuity is that $f(x)$ is continuous on $[a, b]$ if:

$$
\lim_{x \to c} f(x), x \in [a, b]
$$

Suppose we have a piecewise function:

$$
\begin{cases}
x^2 - c, x < 7 \\\\
3x + 4c, x > 7
\end{cases}
$$

To find the value of $c$ that makes the function continuous, we first set the two pieces of the piecewise equal, and solve for $c$:

$$
x^2 - c = 3x + 4c \Rightarrow c = \frac{x^2 - 3x}{5} 
$$

Then we plug in $x = 7$ to get:

$$
c = \frac{7^2 - 3(7)}{5} = \frac{28}{5}
$$
