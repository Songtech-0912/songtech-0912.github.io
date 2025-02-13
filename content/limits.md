+++
title = "Notes on limits for calculus"
date = 2023-09-08
+++

These are notes taken during RPI's MATH 1010 course, on the topic of limits in calculus.

<!-- more -->

Note: some problems are taken Rogawski 4e Calculus Early Transcendentals, the questions are not original work.

It is recommended to use `Ctrl F` or the equivalent search function to find the relevant section, as these notes are quite long.

## Investigating limits

The **limit** $L$ of a function as it approaches $c$ is the value the function tends towards as it approaches $x = c$:

{% math() %}
\lim_{x \to c} f(x) = L
{% end %}

Note that $f(c)$ doesn't _have_ to equal $L$, only that the function tends to approach $L$ as $x$ approaches $c$.

For instance:

{% math() %}
g(x) = \begin{cases}
x^2 + 1, & x \neq 1 \\
0, & x = 1
\end{cases}
{% end %}

Here, we see that $g(1) = 0$. However, as $x$ approaches 1, $g(x)$ approaches 2, so the limit is 2. So the value of the limit doesn't depend on the actual value of the function at a point (in fact many functions are undefined at certain points), only the value the function _approaches_ as it reaches a certain point.

## One-sided limits

One-sided limits are when a function only approaches $c$ from a certain direction.

The left-hand limit is defined as:

{% math() %}
\lim_{x \to c^-} f(x) = L_1
{% end %}

The right-hand limit is defined as:

{% math() %}
\lim_{x \to c^+} f(x) = L_2
{% end %}

A limit only exists if the left-hand and right-hand limits are **equal**.

## Direct evaluation of limits

If a function is defined and continuous, then:

{% math() %}
\lim_{x \to c} f(x) = f(c)
{% end %}

## Algebraic limits

Limits can oftentimes be solved algebraically. Limits are linear, which means that:

{% math() %}
\lim_{x \to c} (a f(x) \pm b g(x)) = a \lim_{x \to c} f(x) \pm b \lim_{x \to c} g(x)
{% end %}

They also can be multiplied and divided (as long as the denominator $\neq 0$), and taken to the  power of:

{% math() %}
\lim_{x \to c} [f(x)]^{p/q} = (\lim_{x \to c} f(x))^{p/q}
{% end %}

(here note that $q \neq 0$)
Algebraic limits work for **algebraic limits** only - that is, if a function is composed of polynomials, roots, rationals (fractions), and powers.

## Continuity

A function is continuous if you can draw its graph without lifting your pencil and without retracing any part of the curve throughout an interval. Otherwise, it is said to have a **discontinuity**, which can be one of several types:

- Jump
- Hole (also called a "removable discontinuity")
- Infinite discontinuity (asymptote)
- Oscillating discontinuity

The formal test of continuity is that $f(x)$ is continuous on $[a, b]$ if:

{% math() %}
\lim_{x \to c} f(x), x \in [a, b]
{% end %}

Suppose we have a piecewise function:

{% math() %}
\begin{cases}
x^2 - c, x < 7 \\
3x + 4c, x > 7
\end{cases}
{% end %}

To find the value of $c$ that makes the function continuous, we first set the two pieces of the piecewise equal, and solve for $c$:

{% math() %}
x^2 - c = 3x + 4c \Rightarrow c = \frac{x^2 - 3x}{5} 
{% end %}

Then we plug in $x = 7$ to get:

{% math() %}
c = \frac{7^2 - 3(7)}{5} = \frac{28}{5}
{% end %}

## Indeterminate forms

If the formula for $f(c)$ at a point yields $\frac{0}{0}$, $\frac{\infty}{\infty}$, $\infty \cdot 0$ or $\infty - \infty$ then it is called an indeterminate form. There are several ways to evaluate such limits.

### Factor and eliminate

We can factor the numerator and simplify:

{% math() %}
\lim_{x \to 2} \frac{x^2 - 7x + 10}{x - 2} = \lim_{x \to 2} \frac{(x-2)(x - 5)}{x-2} = \lim_{x \to 2} x-5 = -3
{% end %}

Note that factors are not always so evident. For example, $e^{2x} - 1 = (e^x - 1)(e^x + 1)$. Use u-substitution for factoring if convenient.

### Conjugate

We can multiply by the conjugate $(a - b)$ and simplify:

{% math() %}
\lim_{h \to 0} \frac{\sqrt{h + 1} - 1}{h} \frac{\sqrt{h + 1} + 1}{\sqrt{h + 1} + 1} = \lim_{h \to 0} \frac{(h + 1) - 1}{h (\sqrt{h + 1} + 1)} = \lim_{h \to 0} \frac{1}{\sqrt{h + 1} + 1} = \frac{1}{2} 
{% end %}

### Rewrite as fraction

We can rewrite as a fraction and/or find a common denominator, and then use one of the three above methods:

{% math() %}
\begin{align*}
\lim_{t \to 0^+} \sin(t) \cot(t) &= \lim_{t \to 0^+} \frac{\sin(t)}{\tan(t)} \\
&= \lim_{t \to 0^+} \sin(t) \frac{\cos(t)}{\sin (t)} \\ 
&= \lim_{t \to 0^+} \cos(t) \\
&= 1
\end{align*}
{% end %}

{% math() %}
\begin{align*}
\lim_{\theta \to \frac{\pi}{4}} \frac{1}{\tan \theta - 1} - \frac{2}{\tan^2 \theta - 1} &= \lim_{\theta \to \frac{\pi}{4}} \frac{\tan \theta + 1 - 2}{(\tan \theta + 1) (\tan \theta - 1)} \\ 
&= \lim_{\theta \to \frac{\pi}{4}} \frac{\tan \theta - 1}{(\tan \theta + 1) (\tan \theta - 1)} \\
&= \frac{1}{2}
\end{align*}
{% end %}

## Infinite limits

If a limit is in the form $\frac{n}{0}$, then check if the left-hand and right-hand limits match by using a number line and substituting a number to the left and right of the limit to check the sign. If the one-sided limits match, then the limit is either $\infty$ or $-\infty$, meaning the function has an **asymptote** at that point. Otherwise, the limit does not exist. 

## Squeeze Theorem

The **squeeze theorem** states that if $g(x) \leq f(x) \leq h(x)$, and $\lim_{x \to c} g(x) = h(x) = L$, then $\lim_{x \to c} f(x) = L$. For instance:

{% math() %}
\lim_{x \to 0} x^2 \cos \left(\frac{1}{x}\right)
{% end %}

We know that $-1 \leq \cos(\frac{1}{x}) \leq 1$ (to prove this you can use the substitution $u = \frac{1}{x}$, then $-1 \leq \cos(u) \leq 1$, and then substituting gives this result). Therefore, it follows that $-x^2 \leq x^2 \cos (\frac{1}{x}) \leq x^2$. We also know that $\lim_{x \to 0} -x^2 = \lim_{x \to 0} x^2 = 0$. Thus:

{% math() %}
\lim_{x \to 0} x^2 \cos \left(\frac{1}{x}\right) = 0
{% end %}

Using the squeeze theorem, we can know that:

{% math() %}
\lim_{x \to 0} \frac{\sin x}{x} = 1
{% end %}

{% math() %}
\lim_{x \to 0} \frac{1 - \cos x}{x} = 0
{% end %}

## Using special limits and limit properties

First, we break up the limit using our special limit and limit properties:
{% math() %}
\lim_{x \to 0} \frac{\sin^2(2x)}{x^2} = \lim_{x \to 0} \left(\frac{\sin 2x}{x}\right)^2 = \lim_{x \to 0} \left(\frac{2\sin 2x}{2x}\right)^2
{% end %}

Then, we do the substitution $u = 2x$:

{% math() %}
\lim_{x \to 0} \left(\frac{2\sin 2x}{2x}\right)^2 = \lim_{u \to 0} \left(\frac{2\sin u}{u}\right)^2 = 2^2 = 4
{% end %}

Similarly, we can do the same in this example:

{% math() %}
\lim_{t \to 0} \frac{\tan (4t)}{9t} = \lim_{t \to 0} \frac{\sin(4t)}{9t} \frac{1}{\cos(4t)} = \lim_{t \to 0} \frac{4\sin(4t)}{4 \cdot 9t} \frac{1}{\cos(4t)}
{% end %}

We switch $4 \cdot 9t$ into $9 \cdot 4t$ in the denominator, then do that substitution $u = 4t$:

{% math() %}
\lim_{t \to 0} \frac{4\sin(4t)}{9 \cdot 4t} \frac{1}{\cos(4t)} = \lim_{u \to 0} \frac{1}{9} \frac{4\sin(u)}{u} \frac{1}{\cos u} = \frac{4}{9}
{% end %}

## Limits at infinity

Limits at infinity are used to define **horizontal asymptotes**. Polynomials always either tend to $+\infty$ or $-\infty$ as $x \to \pm \infty$. The highest degree term of a polynomial dominates when $x \to \infty$ or $x \to -\infty$, so we can just focus on the highest degree term and discard all other terms.

For example:

{% math() %}
\lim_{x \to \infty} -x^5 + 5x^2 + 6
{% end %}

We can take away all the lower-degree terms:

{% math() %}
\lim_{x \to \infty} -x^5
{% end %}

Here, we use the rule that $\lim_{x \to \infty} x^n = \infty$, so:

{% math() %}
\lim_{x \to \infty} -(\infty) = -\infty
{% end %}

Now, let's work on the limit at $-\infty$:

{% math() %}
\lim_{x \to -\infty} -x^5 + 5x^2 + 6
{% end %}

Once again, we can take away all the lower degree terms:

{% math() %}
\lim_{x \to -\infty} -x^5
{% end %}

When approaching $-\infty$, then we can use the degree test. If the degree is even, then $\lim_{x \to -\infty} x^n = \infty$, and if the degree is odd, $\lim_{x \to -\infty} x^n = -\infty$. Thus, we have:

{% math() %}
\lim_{x \to -\infty} -(-\infty) = \infty
{% end %}

For trig functions, as they are periodic, the limit as you approach infinity does not exist.

For exponential functions, one side tends to infinity, and the other side tends to zero. Typically the left-hand side tends to infinity for a base $b > 1$, and the left hand side tends to zero for a base $b < 1$.

For rational functions, we divide by the highest degree term in denominator of the rational function, and use the relation $\lim_{x \to \pm \infty} \frac{1}{x^n} = 0$. For instance:

{% math() %}
\lim_{x \to \pm \infty} \frac{20 x - 3x^2}{4x^2 + 9}
{% end %}

Here, the highest degree term is $x^2$, so we divide every term by $x^2$ to get:

{% math() %}
\lim_{x \to \pm \infty} \frac{\frac{20}{x} - 3}{4 + \frac{9}{x^2}}
{% end %}

The parts with $\frac{1}{x^n}$ cancel out to zero, which gives:

{% math() %}
\lim_{x \to \pm \infty} \frac{0 - 3}{4 + 0} = -\frac{3}{4}
{% end %}

With exponential functions, we want to take apart the fraction until we can find the limit. Take, for instance:

{% math() %}
\lim_{t \to \infty} \frac{5e^t}{3-e^{-t}}
{% end %}

If we rewrite $e^{-t}$ as $\frac{1}{e^t}$, then the limit becomes:

{% math() %}
\lim_{t \to \infty} \frac{5e^t}{3 - \frac{1}{e^t}}
{% end %}

As $\lim_{t \to \infty} e^t = \infty$, $\lim_{t \to \infty} \frac{1}{e^t} = 0$, so we have:

{% math() %}
\lim_{t \to \infty} \frac{5e^t}{3} = \infty
{% end %}

We can do the same with negative infinity:

{% math() %}
\lim_{t \to -\infty} \frac{5e^t}{3 - \frac{1}{e^t}} = \frac{5e^{-\infty}}{3} = 0
{% end %}

However, note that as the limit $\lim_{t \to \infty}$ is infinite, we _don't_ have a horizontal asymptote there (as a horizontal asymptote must approach a finite number), so the only horizontal asymptote is $y = 0$.

Sometimes, we have a messier limit, such as:

{% math() %}
\lim_{x \to \infty} \frac{\sqrt{x^3 + 3x}}{5x^4+4}
{% end %}

Remember that we need to divide by the greatest power of $x$ on the denominator. However, because we have a square root, we need to factor out the _square_ of the greatest power of $x$ from the square root, which will reduce to the power once we finish the square root. Here, the greatest power is $x^4$, so its square is $x^8$. We can then factor:

{% math() %}
\lim_{x \to \infty} \frac{\sqrt{x^8 \left(\frac{1}{x^5} + \frac{3}{x^7}\right)}}{x^4 \left(5 + \frac{4}{x^4}\right)}
{% end %}

Using the rules of square roots, we can then simplify to:

{% math() %}
\lim_{x \to \infty} \frac{x^4\sqrt{\frac{1}{x^5} + \frac{3}{x^7}}}{x^4 \left(5 + \frac{4}{x^4}\right)}
{% end %}

Remember that if you have a square that is $x^2$ (we don't here, but just if you do), then $\sqrt{x^2} = |x| \neq x$. 

Now, if we continue simplifying, we have:

{% math() %}
\lim_{x \to \infty} \frac{\sqrt{\frac{1}{x^5} + \frac{3}{x^7}}}{\left(5 + \frac{4}{x^4}\right)} = \frac{\sqrt{0}}{\sqrt{5}} = 0
{% end %}

As a final example, sometimes we can have limits in the form:

{% math() %}
\lim_{x \to \infty} \sqrt{x^4+2x} - 2x
{% end %}

We'd be tempted to say this is just equal to $\infty$, but if we plug it in, we get $\infty - \infty$, which is an indeterminate form. So instead, we need to rewrite it as a fraction of itself over one, and multiply by the conjugate:

{% math() %}
\lim_{x \to \infty} \frac{x^4-4x^2 - 2x}{\sqrt{x^4 + 2x} -2x}
{% end %}

Now, we can use the greatest power cancelling method as with earlier - we cancel out the greatest power from the denominator:

{% math() %}
\lim_{x \to \infty} \frac{x^4-4x^2 - 2x}{\sqrt{x^4 (1 + \frac{2}{x^3})} - 2x}
{% end %}

{% math() %}
\lim_{x \to \infty} \frac{x^4(1 - \frac{1}{x^2} - \frac{2}{x^3})}{x^2\left(\sqrt{ 1 + \frac{2}{x^3}} - \frac{2}{x}\right)}
{% end %}

We end up with (after canceling the zeroes):

{% math() %}
\lim_{x \to \infty} \frac{x^4}{x^2} = \lim_{x \to \infty} x^2 = \infty
{% end %}

## L'Hôpital's Rule

See [derivative notes](@/differentiation.md) for discussion of this limit evaluation technique.

## The Epsilon-Delta definition of a limit

Up to this point, our discussion of limits has largely left out _what defines a limit_. The idea of a value that a function "approaches" but never reaches - while intuitive - is logically unsatisfactory and non-rigorous. To rigorously define what a limit is, we must turn to the _formal_ definition of a limit: the **epsilon-delta definition**:

> **Epsilon-Delta ($\varepsilon-\delta$) definition of a limit:** for $\varepsilon > 0$, there exists $\delta > 0$ such that $0 < |x - c| < \delta$ implies $0 < |f(x) - L| < \varepsilon$. Then, $L = \displaystyle \lim_{x \to c} f(x)$.

What this means is that as we approach (but don't actually reach) some value $x=c$, such that we are a tiny (but nonzero!) _distance_ $\delta$ away from $x = c$, then we find that $f(x)$ is a *tiny difference* from $L$, the limiting value of $f(x)$ at $x = c$. We can make the distance $\delta$ as small as we want and approach as close to $x = c$ as we want, such that the difference $\varepsilon$ between $f(x)$ and its limit $L$ becomes as small as we want. Thus we say that the limit $L = \displaystyle \lim_{x \to c} f(x)$.

We may use the epsilon-delta definition to _prove_ that $\displaystyle \lim_{x \to 4} (5x - 3) = 17$. To do so, let us first define $L = 17$ as the limiting value of $5x - 3$ as $x \to 4$. With the epsilon-delta definition, we can follow these steps:

{% math() %}
\begin{gather*}
|5x - 3 - L| < \varepsilon \\
|5x - 3 - 17 | < \varepsilon \\
|5x - 20| < \varepsilon \\
|5(x - 4) | < \varepsilon \\
|x - 4 | < \frac{\varepsilon}{5} \\
\delta = \frac{\varepsilon}{5}
\end{gather*}
{% end %}

And thus we have found a value of $\delta$ which we can make as small as we want such that $f(x)$ is an arbitrarily small difference $\varepsilon$ from the value $L$. For instance, given $\varepsilon = 0.1$, then $\delta = \frac{\varepsilon}{5} = 0.02$. We can show that this works. Since we require the condition that $0 < |x - 4 | < 0.02$, we can pick the value $x = 4.01$ which satisfies this condition. We then indeed find that:

{% math() %}
|f(4.01) - 17| = 0.05 \Rightarrow 0.05 < \varepsilon
{% end %}