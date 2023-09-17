+++
title = "Notes on limits for calculus"
date = 2023-09-08
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

## Indeterminate forms

If the formula for $f(c)$ at a point yields $\frac{0}{0}$, $\frac{\infty}{\infty}$, $\infty \cdot 0$ or $\infty - \infty$ then it is called an indeterminate form. There are several ways to evaluate such limits.

### Factor and eliminate

We can factor the numerator and simplify:

$$
\lim_{x \to 2} \frac{x^2 - 7x + 10}{x - 2} = \lim_{x \to 2} \frac{(x-2)(x - 5)}{x-2} = \lim_{x \to 2} x-5 = -3
$$

Note that factors are not always so evident. For example, $e^{2x} - 1 = (e^x - 1)(e^x + 1)$. Use u-substitution for factoring if convenient.

### Conjugate

We can multiply by the conjugate $(a - b)$ and simplify:

$$
\lim_{h \to 0} \frac{\sqrt{h + 1} - 1}{h} \frac{\sqrt{h + 1} + 1}{\sqrt{h + 1} + 1} = \lim_{h \to 0} \frac{(h + 1) - 1}{h (\sqrt{h + 1} + 1)} = \lim_{h \to 0} \frac{1}{\sqrt{h + 1} + 1} = \frac{1}{2} 
$$

### Rewrite as fraction

We can rewrite as a fraction and/or find a common denominator, and then use one of the three above methods:

$$
\lim_{t \to 0^+} \sin(t) \cot(t) = \lim_{t \to 0^+} \frac{\sin(t)}{\tan(t)} = \lim_{t \to 0^+} \sin(t) \frac{\cos(t)}{\sin (t)} = \lim_{t \to 0^+} \cos(t) = 1
$$

$$
\lim_{\theta \to \frac{\pi}{4}} \frac{1}{\tan \theta - 1} - \frac{2}{\tan^2 \theta - 1} = \lim_{\theta \to \frac{\pi}{4}} \frac{\tan \theta + 1 - 2}{(\tan \theta + 1) (\tan \theta - 1)} = \lim_{\theta \to \frac{\pi}{4}} \frac{\tan \theta - 1}{(\tan \theta + 1) (\tan \theta - 1)} = \frac{1}{2}
$$

## Infinite limits

If a limit is in the form $\frac{n}{0}$, then check if the left-hand and right-hand limits match by using a number line and substituting a number to the left and right of the limit to check the sign. If the one-sided limits match, then the limit is either $\infty$ or $-\infty$, meaning the function has an **asymptote** at that point. Otherwise, the limit does not exist. 

## Squeeze Theorem

The **squeeze theorem** states that if $g(x) \leq f(x) \leq h(x)$, and $\lim_{x \to c} g(x) = h(x) = L$, then $\lim_{x \to c} f(x) = L$. For instance:

$$
\lim_{x \to 0} x^2 \cos \left(\frac{1}{x}\right)
$$

We know that $-1 \leq \cos(\frac{1}{x}) \leq 1$, so $-x^2 \leq x^2 \cos (\frac{1}{x}) \leq x^2$. We also know that $\lim_{x \to 0} -x^2 = \lim_{x \to 0} x^2 = 0$. Thus:

$$
\lim_{x \to 0} x^2 \cos \left(\frac{1}{x}\right) = 0
$$

Using the squeeze theorem, we can know that:

$$
\lim_{x \to 0} \frac{\sin x}{x} = 1
$$

$$
\lim_{x \to 0} \frac{1 - \cos x}{x} = 0
$$

## Using special limits and limit properties

First, we break up the limit using our special limit and limit properties:
$$
\lim_{x \to 0} \frac{\sin^2(2x)}{x^2} = \lim_{x \to 0} \left(\frac{\sin 2x}{x}\right)^2 = \lim_{x \to 0} \left(\frac{2\sin 2x}{2x}\right)^2
$$
Then, we do the substitution $u = 2x$:

$$
\lim_{x \to 0} \left(\frac{2\sin 2x}{2x}\right)^2 = \lim_{u \to 0} \left(\frac{2\sin u}{u}\right)^2 = 2^2 = 4
$$
Similarly, we can do the same in this example:

$$
\lim_{t \to 0} \frac{\tan (4t)}{9t} = \lim_{t \to 0} \frac{\sin(4t)}{9t} \frac{1}{\cos(4t)} = \lim_{t \to 0} \frac{4\sin(4t)}{4 \cdot 9t} \frac{1}{\cos(4t)}
$$

We switch $4 \cdot 9t$ into $9 \cdot 4t$ in the denominator, then do that substitution $u = 4t$:

$$
\lim_{t \to 0} \frac{4\sin(4t)}{9 \cdot 4t} \frac{1}{\cos(4t)} = \lim_{u \to 0} \frac{1}{9} \frac{4\sin(u)}{u} \frac{1}{\cos u} = \frac{4}{9}
$$


