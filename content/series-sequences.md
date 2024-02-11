+++
title = "Series and sequences"
date = 2024-02-11
+++

These are notes taken in MATH 1020 (Calculus II) at RPI, covering sequences, series, Taylor expansions, convergence and divergence tests, and examples of each.

<!-- more -->

## Sequences

A **sequence** can be thought of as a list of numbers written in a definite order. They are notated $\{ a_n \}$ where $a_n$ is the formula for the _nth_ term, or $\{a_1, a_2, a_3, \dots, a_n\}$. Unlike a function, which can have continuous inputs, sequences must always use integer values of $n$ as input. For instance:

$$
\{ 2n + 1\}_{n = 0}^\infty = \{1, 3, 5, 7, 9, 11, \dots\}
$$

A series $\{ a_n \}$ is said to _converge_ if it approaches a number $L$:
$$
\lim_{n \to \infty} a_n = L
$$
and is said to _divergence_ otherwise. Several important theorems hold for sequences:

- If $\displaystyle \lim_{n \to \infty} |a_n| = 0$, then $\displaystyle \lim_{n \to \infty} a_n = 0$.
- If $\displaystyle \lim_{n \to \infty} a_n = L$ and the function $f(x)$ is continuous at $L$, then $\displaystyle \lim_{n \to \infty} f(a_n) = f(L)$.
- The geometric sequence $\{cr^n\}$ converges if $-1 < r < 1$; if it converges, $\displaystyle \lim_{n \to \infty} cr^n = c$ if $c = 1$ and $\displaystyle \lim_{n \to \infty} cr^n = 0$ for all other values of $c$. Note that $\frac{a^n}{b^n}$ can be written as $\left(\frac{a}{b}\right)^n$ and can then be treated as a geometric sequence.
- Every bounded (never exceeding one number or going below one number) and monotonic (only increasing or only decreasing) sequence is **convergent**.
