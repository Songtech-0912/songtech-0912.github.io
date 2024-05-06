+++
title = "Series and sequences"
date = 2024-02-11
+++

These are notes taken in MATH 1020 (Calculus II) at RPI, covering sequences, series, Taylor expansions, convergence and divergence tests, and examples of each.

<!-- more -->

## Sequences

A **sequence** can be thought of as a list of numbers written in a definite order. They are notated $\{ a_n \}$ where $a_n$ is the formula for the _nth_ term, which expands to $\{a_1, a_2, a_3, \dots, a_n\}$. Unlike a function, which can have continuous inputs, sequences must always use integer values of $n$ as input. For instance:

$$
\\{ 2n + 1\\}_{n = 0}^\infty = \\{1, 3, 5, 7, 9, 11, \dots\\}
$$

A sequence $\\{ a_n \\}$ is said to _converge_ if it approaches a number $L$:
$$
\lim_{n \to \infty} a_n = L
$$
and is said to _divergence_ otherwise. Several important theorems hold for sequences:

- If $\displaystyle \lim_{n \to \infty} |a_n| = 0$, then $\displaystyle \lim_{n \to \infty} a_n = 0$.
- If $\displaystyle \lim_{n \to \infty} a_n = L$ and the function $f(x)$ is continuous at $L$, then $\displaystyle \lim_{n \to \infty} f(a_n) = f(L)$.
- The geometric sequence $\\{cr^n\\}$ converges if $-1 < r < 1$; if it converges, $\displaystyle \lim_{n \to \infty} cr^n = c$ if $c = 1$ and $\displaystyle \lim_{n \to \infty} cr^n = 0$ for all other values of $c$. Note that $\frac{a^n}{b^n}$ can be written as $\left(\frac{a}{b}\right)^n$ and can then be treated as a geometric sequence.
- Every bounded (never exceeding one number or going below one number) and monotonic (only increasing or only decreasing) sequence is **convergent**.

## Infinite series

An **infinite series**, often just referred to as a series, is a sum of a sequence. The general form of a series is given by:

$$
\sum_{n = 1}^\infty a_n
$$

A series, just like a sequence, can be convergent or divergent. The **nth-term divergence test** states that a series is _guaranteed_ to be divergent if:

$$
\lim_{n \to \infty} a_n \neq 0
$$

Note that the nth-term test does **not** guarantee convergence. It can only guarantee divergence.

### Why does convergence (or divergence) matter?

It might seem strange that one feature of an infinite series - that is, its convergence or divergence - would be so important. Why care?

There are two reasons - a theoretical and a practical reason. The theoretical reason is that if a series does not converge, then it is essentially meaningless. That is, divergent series are pretty much the same category of expressions as $\frac{1}{0}$ or $\frac{\infty}{\infty}$ or $0^0$; they hold no value.

The practical reason is that in many applications of series, an infinite series is truncated by only computing a finite number of terms. If a series does not converge, then a finite number of terms could not be used to approximate the series. For instance, one of the definitions of $\pi$:

$$
\sum_{n = 1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6}
$$

only holds true because the series is convergent; otherwise the series would be mathematically meaningless and numerically impossible to compute.

For more on this topic, [this question post](https://math.stackexchange.com/questions/1692062/what-is-the-importance-of-knowing-if-a-series-converges-or-diverges) would be good reading.

### Interlude on shifts

An infinite series can be shifted up or down by changing the starting index. The two most common starting indices are 0 and 1. To convert between them, recall that:

$$
\sum_{i = 1}^\infty a_n = \sum_{i = 0}^\infty a_{n + 1}
$$

And:

$$
\sum_{i = 0}^\infty a_n = \sum_{i = 1}^\infty a_{n - 1}
$$

## Geometric series

The geometric series is given by:

$$
\sum_{n = 0}^\infty cr^n = c + cr + cr^2 + cr^3 + cr^4 + \dots + cr^n
$$

So long as $|r|<1$, then the geometric series converges to a value given by:

$$
\sum_{n = 0}^\infty cr^n = \frac{c}{1 - r}
$$

In all other cases, the geometric series diverges.

## Nth-partial sums test

The nth partial sum of an infinite series is given by:

$$
S_n = \sum_{i = 1}^n a_i = a_1 + a_2 + \dots + a_n
$$

The **nth partial sum test** states that if the nth partial sum converges, the series converges as well, and if the nth partial sum diverges, the series diverges as well. This is however often not an easy test to use, because finding a formula for the nth partial sum is itself often a difficult task.

**Example:** find whether the following series converges, and if it converges, find its sum:

$$
\sum_{n = 2}^\infty \frac{1}{n^2 -1}
$$

**Answer:**

First, to test for possible convergence, we can use the nth term test. Given that:

$$
\lim_{n \to \infty} \frac{1}{n^2 - 1} = 0
$$

we can tell that the series **may** converge.

Then, we can use the nth partial sum test. To do so, recall that:

$$
S_n = \sum_{i = 2}^n \frac{1}{i^2 - 1}
$$

We can use partial fraction decomposition to have:

$$
S_n = \sum_{i = 2}^n \left(\frac{1/2}{i - 1} + \frac{1/2}{i + 1}\right)
$$

Then factor out the $\frac{1}{2}$ to have:

$$
S_n = \frac{1}{2} \sum_{i = 2}^n \left(\frac{1}{i - 1} + \frac{1}{i + 1}\right)
$$

We can expand out the terms to find the pattern:

$$
S_n = \left[\left(1 + \frac{1}{3}\right) + \left(\frac{1}{2} + \frac{1}{4}\right) + \left(\frac{1}{3} + \frac{1}{5}\right) + \dots \right] 
$$

From which we can see that the fractions cancel to find:

$$
S_n = \frac{1}{2} \left[1 + \frac{1}{2} + \frac{1}{n + 1}\right]
$$

Taking the limit of the nth partial sum yields:

$$
\lim_{n \to \infty} S_n = \frac{1}{2} \left[1 + \frac{1}{2} + 0\right] = \frac{3}{4}
$$

So, the series converges, and its value is:

$$
\sum_{n = 2}^\infty \frac{1}{n^2 -1} = \frac{3}{4}
$$

## Integral test

The **integral test** for convergence states that if $f$ is positive, continuous, and decreasing and $a_n = f(n)$, then $\displaystyle \sum_{n = 1}^\infty a_n$ and $\displaystyle \int \limits_1^\infty f(x) dx$ either both converge or both diverge.

**Example:**

Determine the convergence of the following series:

$$
\sum_{n = 1}^\infty \frac{2}{3n + 5}
$$

**Answer:**

To test for convergence, we can use the integral test. To do this, as $f(n) = \frac{2}{3n + 5}$, we need to compute:

$$
\int \limits_1^\infty \frac{2}{3x + 5} dx
$$

The integral can be computed as follows:

$$
\int \limits_1^\infty = \lim_{k \to \infty} \int \limits_1^k \frac{2}{3x + 5} dx
$$

$$
= \frac{2}{3} \lim_{k \to \infty} \int \limits_1^k \frac{1}{3x + 5} dx
$$

$$
= \frac{2}{3} \lim_{k \to \infty} \int \limits_8^{3k+5} \frac{1}{u} du
$$

$$
= \frac{2}{3} \lim_{k \to \infty} \ln(u) \bigg|_8^{3k + 5}
$$

$$
= \frac{2}{3} \lim_{k \to \infty} \ln(3k+5) - \ln(8)
$$

$$
= \infty
$$

Therefore, as the integral is unbounded and does not converge, the series also diverges.

## _P_-series test

The **p-series test** states that the series:

$$
\sum_{n = 1}^\infty \frac{1}{n^p} = 1 + \frac{1}{2^p} + \frac{1}{3^p} + \frac{1}{4^p} + \frac{1}{5^p} + \dots
$$

converges if $p > 1$ and diverges if $0 < p \leq 1$. Note that if $p = 1$, the series is called the harmonic series.

## Direct comparison test

A series can be compared to another series (typically a known series such as a geometric series) to establish convergence or divergence. Any series that is term-by-term **smaller** than a convergent series is **also convergent**, and any series that is term-by-term **larger** than a divergence series is **also divergent**.

The **direct comparison test** for series is a rigorous formulation of this principle - it states that given two series $\displaystyle \sum_{n = i}^\infty a_n$ and $\displaystyle \sum_{n = i}^\infty b_n$, given that $a_n \leq b_n$ for all $n$:

- If $\displaystyle \sum_{n = i}^\infty b_n$ converges, $\displaystyle \sum_{n = i}^\infty a_n$ converges
- If $\displaystyle \sum_{n = i}^\infty b_n$ diverges, $\displaystyle \sum_{n = i}^\infty a_n$ diverges

**Example question:**

Determine the convergence of:

$$
a = \sum_{n = 1}^\infty \frac{1}{3n^2 +2}
$$

**Answer:**

We can compare the series to another series $b$:

$$
\sum_{n = 1}^\infty \frac{1}{3n^2}
$$

Notice that $b$ is a p-series with $p = 2$, thus it converges. Given that $a_n < b_n$, both series converge. Therefore, the series $a$ converges.

## Limit comparison test

The **limit comparison test** for series states that given two series $\displaystyle \sum_{n = 1}^\infty a_n$ and $\displaystyle \sum_{n = 1}^\infty b_n$, if $\displaystyle \lim_{n \to \infty} \frac{a_n}{b_n} = L$ where $L$ is finite and positive, then the two series either both converge or both diverge.

Note that for the limit comparison test, a suitable comparison series $\displaystyle \sum_{n = 1}^\infty b_n$ might be chosen from either a known series (geometric, p-series, etc.) or just a series that is easy to check for convergence (or divergence). For instance, consider the series:

$$
\sum_{n = 1}^\infty \frac{n^{1/6}}{n + 8}
$$

A convenient series to compare against (that can be easily checked to show it is divergent) could be:

$$
\sum_{n = 1}^\infty n
$$

Using the limit comparison test with these two series shows that the first series, like the second (comparison) series, is divergent.

**Example question:**

Determine the convergence of:

$$
a = \sum_{n = 0}^\infty \frac{5n - 3}{n^2 - 2n + 5}
$$

**Answer:**

We can compare the series to another series $b$:

$$
b = \sum_{n = 0}^\infty \frac{5n}{n^2} = \frac{5}{n}
$$

Given that $b$ is a p-series with $p = 1$, $b$ is divergent. Then, we take the limits of the quotients:

$$
\lim_{n \to \infty} \frac{a_n}{b_n} = \frac{\frac{5n - 3}{n^2 - 2n + 5}}{\frac{5}{n}} = 1
$$

Given that $L$ is finite and positive, the two series both diverge. Therefore, $a$ diverges.

## Alternating series test

An alternating series is a series in the form:

$$
\sum_{n = 1}^\infty (-1)^n a_n
$$

or in the form:

$$
\sum_{n = 1}^\infty (-1)^{n + 1} a_n
$$

The **alternating series test** states that an alternating series converges only if $\displaystyle \lim_{n \to \infty} a_n = 0$ and $a_{n + 1} \leq a_n$ for all $n$. To check that $a_{n + 1} \leq a_n$ for all $n$, let $f(n) = a_n$, and ensure that $f'(n) \leq 0$ for all $n$.

**Example question:**

Determine the convergence of:

$$
\sum_{n = 1}^\infty \frac{(-1)^{n + 1}n}{2n-1}
$$

**Answer:**

Given that $a_n = \frac{n}{2n - 1}$, we can find the limit:

$$
\lim_{n \to \infty} \frac{n}{2n-1} = \frac{1}{2} \neq 0
$$

Thus the series diverges.

### Approximating alternating series

For a convergent alternating series, the partial sum $S_n$ can be used to approximate the sum $S$ of the series. The error (or remainder) in estimating $S$ with the partial sum $S_n$, $R_n$, obeys:

$$
|R_n| \leq a_{n + 1}
$$

**Example question:**

Find the error of the 6-term approximation to:

$$
\sum_{n = 1}^\infty (-1)^{n + 1} \left(\frac{1}{n!}\right)
$$

**Answer:**

Given the remainder $|R_n| \leq a_n + 1$, then $|R_6| \leq a_7$ and $a_7 \approx 0.0002$, thus $|R_6| \approx 0.0002$.

If a series has both negative and positive terms but they don't alternate, then:

- If $\displaystyle \sum_{n = 1}^\infty |a_n|$ converges, then $\displaystyle \sum_{n = 1}^\infty a_n$ is **absolutely convergent**
- If $\displaystyle \sum_{n = 1}^\infty a_n$ converges but $\displaystyle \sum_{n = 1}^\infty |a_n|$ diverges, then $\displaystyle \sum_{n = 1}^\infty a_n$ is **conditionally convergent**

## Ratio test

The **ratio test** states that for a series $a$, let the ratio $r = \displaystyle \lim_{n \to \infty} \left|\frac{a_{n + 1}}{a_n}\right|$. Then:

- If $|r| < 1$, the series converges
- If $|r| > 1$, the series diverges
- If $|r| = 1$, the test is inconclusive

**Example question:**

Determine the convergence of:

$$
\sum_{n=0}^{\infty}\frac{3^{n}}{n!}
$$

**Answer:**

The ratio $r$ can be found through:

$$
\lim_{n \to \infty} \left|\frac{a_{n + 1}}{a_n}\right| = \frac{3^{n + 1}}{(n + 1)!} \frac{n!}{3^n}
$$

First, we know that:

$$
\frac{3^{n + 1}}{3^n} = 3
$$

We also know that:

$$
\frac{n!}{(n + 1)!} = \frac{1}{n + 1}
$$

Therefore, combined:

$$
r = \lim_{n \to \infty} \left|\frac{a_{n + 1}}{a_n}\right| = \lim_{n \to \infty} \frac{3}{n + 1} = 0
$$

Given that $r < 1$, the series converges.

## Root test

The **root test** states that for a series $\displaystyle \sum_{n = 1}^\infty a_n$, let the root be given by $p = \displaystyle \lim_{n \to \infty} \sqrt[n]{|a_n|}$. Then:

- If $p < 1$, the series converges
- If $p > 1$, the series diverges
- If $p = 1$, the test is inconclusive

**Example question:**

Determine the convergence or divergence of:

$$
\sum_{n = 0}^\infty e^{-n}
$$

**Answer:**

We can find $p$ from:

$$
p = \lim_{n \to \infty} \sqrt[n]{|a_n|} = \lim_{n \to \infty} \sqrt[n]{e^{-n}} = \lim_{n \to \infty} e^\frac{-n}{n}
= \lim_{n \to \infty} e^{-1} = \frac{1}{e}
$$

Since $p = \frac{1}{e} < 1$, the series converges.

## Taylor series

The Taylor series for a function is given by:

$$
\sum_{n = 0}^\infty \frac{f^{(n)}(a)}{n!} (x-a)^n
$$

The nth-degree Taylor polynomial for a function is given by:

$$
\begin{align*}
P_n(x) = f(a) &+ f′(a)(x−a) +\dfrac{f''(a)}{2!}(x−a)^2 \\\\
&+ \dfrac{f'''(a)}{3!}(x−a)^3 \dots+\dfrac{f^{(n)}(a)}{n!}(x−a)^n
\end{align*}
$$

If the Taylor series is centered at $a = 0$, then the series is called a **Maclaurin series**.

**Example question:** Find the approximating Maclaurin polynomial of degree 5 for $f(x) = e^{-3x}$

**Answer:**

First, we compute all the derivatives:

$$
f'(0) = -3
$$

$$
f''(0) = 9
$$

$$
f'''(0) = -27
$$

$$
f^{(4)}(0) = 81
$$

$$
f^{(5)}(0) = -243
$$

Then, we plug in the values of the derivatives to the Taylor series formula:

$$
P_5(x) = f(0) -3 (x - 0) + \frac{9(x - 0)^2}{2!} - \frac{27(x - 0)^3}{3!} + \frac{81(x - 0)^4}{4!} - \frac{243(x - 0)^5}{5!}
$$

Simplifying, we get:

$$
P_5(x) = 1 - 3x + \frac{9x^2}{2} - \frac{9x^3}{2} + \frac{81x^4}{12} - \frac{243x^5}{120}
$$

There are several important Taylor series that it would be useful to memorize:

$$
e^x = \sum_{n = 0}^\infty \frac{x^n}{n!}
$$

$$
\cos x = \sum_{n = 0}^\infty \frac{(-1)^n x^{2n}}{(2n)!}
$$

$$
\sin x = \sum_{n = 0}^\infty \frac{(-1)^n x^{2n+1}}{(2n+1)!}
$$

The **remainder theorem** for Taylor polynomials states that there exists a value $z$ between $x$ and $c$ such that the error bound for a Taylor polynomial of order $n$ is given by:

$$
R_n(x) \leq \text{max}|f^{n + 1}(z)|\frac{(x - c)^{n + 1}}{(n + 1)!}
$$

Thus, to compute the Lagrange error bound, we compute the $(n + 1)$th derivative of $f(x)$, find the maximum value of $f^{(n + 1)}(z)$, and then compute the error bound using the formula.

**Example question:** Determine the upper bound in approximating $\sin(0.1)$ with the 3rd-degree Maclaurin polynomial 

$$
P_3(x) = x - \frac{x^3}{3!}
$$

**Answer:**

First, we compute the $(n + 1)$the derivative of $f(x)$. Given that $n = 3$ as it is a 3rd-degree polynomial,we compute the 4th-derivative of $f(x)$:

$$
f^{(4)}(x) = \sin(x)
$$

The maximum value of the 4th-derivative of $f(x)$ is 1, as $\sin(x)$ oscillates between -1 and 1. Now, we can plug into the formula to get:


$$
R_n(0.1) \leq (1) \frac{(0.1 - 0)^4}{4!}
$$

Which simplifies to:

$$
R_n(0.1) \leq 0.000004
$$

Thus, the value of $P_3(0.1)$ must be equal to $\sin(0.1) \pm 0.000004$.

**Example question:** Find the degree of the Maclaurin polynomial $P_n(x)$ such that the error of the approximation of the function $f(x) = e^x$ at $x = 0.6$ is less than 0.001.

**Answer:**

We set $R_n(x) < 0.001$. Therefore: 

$$
\text{max}|f^{n + 1}(z)| \frac{(0.6 - 0)^{n + 1}}{(n + 1)!} < 0.001
$$

The derivatives of $e^x$ are all $e^x$, so the maximum value of $f^{n + 1}(z)$ in $z \in [0, 0.6]$ is $e^{0.6} = 1.8221$. Therefore:

$$
\frac{1.8221 \cdot (0.6 - 0)^{n + 1}}{(n + 1)!} < 0.001
$$

Plugging in values of $n$ allows us to find that $n = 5$ is the first polynomial with the desired accuracy.

## Power series

A series of the form $\displaystyle \sum_{n = 0}^\infty a_n x^n$ is called a **power series**. When centered at constant $c$, the power series becomes the form $\displaystyle \sum_{n = 0}^\infty a_n (x - c)^n$.

We can write a power series as a function of $x$:

$$
f(x) = \sum_{n=0}^\infty a_n (x-c)^n
$$

Power series are widely used to approximate known functions and solve for unknown functions, as a convergent infinite power series is equivalent to the function it approximates. Taylor series are a special type of power series, but power series can generalize to approximate almost any type of function imaginable.

## Radius of convergence

If given a power series $\displaystyle \sum_{n = 0}^\infty a_n (x-c)^n$, then the _common ratio_ $r$ is given by the ratio test:

$$
r = \lim_{n \to \infty} \left| \frac{a_{n + 1} (x - c)^{n + 1}}{a_n (x - c)^n} \right | = \lim_{n \to \infty} \left| \frac{a_{n + 1}}{a_n} \right| \cdot |x - c|
$$
By the ratio test, a series can only converge if $r < 1$. Therefore, if we substitute in the obtained value of $r$:

$$
r < 1 \Rightarrow \lim_{n \to \infty} \left| \frac{a_{n + 1}}{a_n} \right| \cdot |x - c| < 1
$$
If we rearrange the terms so that the left-hand side is $|x - c|$ (by dividing by the limit), we have:

$$
|x - c| < \lim_{n \to \infty} \left| \frac{a_n}{a_{n + 1}} \right|
$$

We may rewrite this as $|x - c| < R$, where $R$ is called the **radius of convergence**, and is simply the right-hand side of the above equation:

$$
R = \lim_{n \to \infty} \left| \frac{a_n}{a_{n + 1}} \right|
$$
Note that this is only true if the limit exists (the limit can be finite or infinite, but must exist). The interpretation of the radius of convergence is that the power series in the general form $\displaystyle \sum_{n = 0}^\infty a_n (x-c)^n$ _must_ converge for all values $x \in (c - R, c + R)$ and _may_ converge at $x = c - R$ and $x = c + R$. The two cases where the series may converge are called the _endpoints_ and their convergence must be checked separately.

> Note: here $r$ and $R$ are different things. $r$ is the common ratio, which is the result of the ratio test; $R$ is the radius of convergence, which is the distance from the center $c$ for which the series converges.

In general, given a power series with radius of convergence $R$:

- If $R = 0$, the series only converges at $x = c$
- If $R > 0$, the series converges for $|x - c| < R$
- If $R = \infty$, the series converges for all real numbers

**Example question:** Determine the radius of convergence for the following power series, _without_ using the radius of convergence formula:

$$
\sum_{n = 0}^\infty \frac{(-1)^n x^n}{2^n}
$$

**Answer:**

To find the radius of convergence, we can use the ratio test. Recall that $r$ is the ratio such that:

$$
r = \lim_{n \to \infty} \left|\frac{a_{n + 1}}{a_n}\right|
$$

In this case, the ratio $r$ is given by:

$$
r = \lim_{n \to \infty} \left|\frac{\frac{x^{n + 1}}{2^{n + 1}}}{\frac{x^n}{2^n}}\right| = \lim_{n \to \infty} \left| \frac{x^{n + 1}}{2^{n + 1}} \frac{2^n}{x^n}\right| = \lim_{n \to \infty} \left|\frac{x}{2}\right|
$$

Now, recall that the series only converges if $r < 1$, thus $|x| < 2$. This means that the **radius of convergence** of the power series is 2.

**Example question:** Determine the radius of convergence for the power series given below, with use of the radius of convergence formula:

$$
\sum_{n = 0}^\infty \frac{(-1)^n (x - 4)^n}{n^2}
$$

**Answer:**

Since the general power series is given by $\displaystyle \sum_{n = 0}^\infty a_n (x - c)^n$, then here:

$$
a_n = \frac{(-1)^n}{n^2}
$$

The radius of convergence formula is given by:

$$
R = \lim_{n \to \infty} \left| \frac{a_n}{a_{n + 1}} \right|
$$

If we substitute, noting that $|(-1)^n| = 1$, we have:

$$
R = \lim_{n \to \infty} \frac{1}{n^2} \frac{(n + 1)^2}{1} = 1
$$

Therefore the power series has the radius of convergence $R = 1$.

**Example question:** Determine the interval of convergence for the power series:

$$
\sum_{n = 0}^\infty \left(\frac{x}{k}\right)^n
$$

**Answer:**

The given power series is a geometric series, which converges if its common ratio is less than one. Thus, to converge:

$$
\left|\frac{x}{k}\right| < 1
$$

Which we can rearrange to find:

$$
|x| < k
$$

Thus:

$$
-k < x < k
$$

We then check the endpoints with $x = k$ and $x = -k$ to find the actual interval of convergence. We first check $x = k$:

$$
\sum_{n = 0}^\infty \left(\frac{k}{k}\right)^n = \sum_{n = 0}^\infty 1^n = \sum_{n = 0}^\infty 1 = \infty
$$

Clearly this diverges. Then we check $x = -k$:

$$
\sum_{n = 0}^\infty \left(\frac{-k}{k}\right)^n = \sum_{n = 0}^\infty (-1)^n = \infty
$$

As both endpoints diverge, the interval of convergence is $(-k, k)$.

### Derivatives and integrals of power series

The derivative of a power series is given by:

$$
\frac{df}{dx} = \sum_{n = 1}^\infty n a_n(x - c)^{n - 1}
$$

And the integral of a power series is given by:

$$
\int f(x) dx = C + \sum_{n = 0}^\infty \frac{a_n}{n + 1} (x - c)^{n + 1}
$$

The power series, its derivative, and its integral all have the **same** radius of convergence (though not necessary same _interval_ of convergence - the value of $c$ about which they converge can be different).

> Note that in both integration and differentiation, any $(-1)^n$ term stays constant and is not differentiated or integrated over. Also note that differentiation causes a shift of one index to the right.

### Power series representations of functions

The power series representation of $f(x) = \frac{1}{1 - x}$ is:

$$
f(x) = \sum_{n = 0}^\infty x^n
$$

We can turn a function into a similar form to write it as a power series.

**Example question:**

Write the following function as a power series:

$$
f(x) = \frac{1}{1 + x^3}
$$

**Answer:**

Note that we can rewrite the function as:

$$
f(x) = \frac{1}{1 - (-x^3)}
$$

We can then substitute everywhere we have $x$ with $(-x^3)$. So, the power series becomes:

$$
f(x) = \sum_{n = 0}^\infty (-x^3)^n
$$

Which can be rewritten as:

$$
f(x) = \sum_{n = 0}^\infty (-1)^n x^{3n}
$$

**Example question:**

Write the following function as a power series:

$$
f(x) = \frac{1}{x + 2}
$$

**Answer:**

We can rewrite the function as:

$$
f(x) = \frac{1}{2 + x} = \frac{1}{2} \left(\frac{1}{1 - -\frac{x}{2}}\right)
$$

If we sub $x$ as $-\frac{x}{2}$ and multiply by $1/2$, we have:

$$
f(x) = \frac{1}{2} \sum_{n = 0}^\infty \left(-\frac{x}{2}\right)^n
$$

which can be rewritten as:

$$
f(x) =\sum_{n = 0}^\infty \frac{(-1)^n x^n}{2^{n + 1}}
$$

**Example question:**

Write the following function as a power series:

$$
f(x) = \frac{1}{(1 - x)^2}
$$

**Answer:**

Note that $f(x)$ is the derivative of $\frac{1}{1 - x}$. Therefore, we just need to take the derivative of the original power series to have:

$$
\frac{d}{dx} \sum_{n = 0}^\infty x^n = \sum_{n = 1}^\infty nx^{n - 1}
$$

**Example question:**

Write the following function as a power series:

$$
f(x) = \ln(1 - x)
$$

**Answer:**

Note that $f(x)$ is the integral of $\frac{-1}{1 - x}$. Thus:

$$
\ln(1 - x) = -\int \frac{1}{1 - x} = -\int \sum_{n = 0}^\infty x^n dx = C - \sum_{n = 0}^\infty \frac{x^{n + 1}}{n + 1}
$$

## Applications of series

Series have many, many uses in both pure and applied math. Most obviously, they can be used to solve problems that are defined by infinite sums - including the famous problem of Achilles and the tortoise from classical antiquity. However, they can also be used to approximate functions so that they can be calculated on a computer - see [this excellent article](https://zachartrand.github.io/SoME-3/) for details on how this works. They can also be able to express exact solutions to differential equations and do integrals that are very difficult to solve in any other ways, and these series solutions can then be programmed into a computer to do calculations. Pure math heavily uses series as well - one of the _definitions_ of Euler's number $e$ is $e = \displaystyle \sum_{n = 0}^\infty \frac{1^n}{n!}$, and there are numerous other examples available [here](https://en.wikipedia.org/wiki/List_of_mathematical_series) for the curious.
