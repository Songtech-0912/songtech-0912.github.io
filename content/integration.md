+++
title = "Notes on integrals for calculus"
date = 2023-11-07
+++

These are notes taken during RPI's MATH 1010 course, on the topic of integrals and their applications in calculus.

<!-- more -->

## Antiderivatives

An antiderivative is the original function that a derivative came from. For example, $x^2$ is the antiderivative of $2x$, because the $x^2$ was the original function whose derivative is $2x$.

Antiderivatives are represented by the "curly S" integral sign, with a $dx$ representing the variable to take the antiderivative with respect to - in this case $x$:

$$
\int f(x) dx = F(x) + C
$$
Since the derivative of a constant is zero, the antiderivative of $f(x) + 1$, $f(x) + 3$, or $f(x) + 100$ is the same. Thus we add the $C$ known as the constant of integration to remind us that multiple antiderivatives differing by a constant have the same derivative.

The rules of antiderivatives are the inverse of the rules for derivatives:

$$
\int k~dx = kx + C
$$
$$
\int x^n~dx = \frac{x^{n + 1}}{n + 1} + C
$$
$$
\int \frac{1}{x}~dx = \ln |x| + C
$$
$$
\int e^x~dx = e^x + C
$$
$$
\int \cos(x)~dx = \sin(x) + C
$$
$$
\int \sin(x)~dx = -\cos(x) + C
$$

### Initial value problems

To find the value of the $C$ when doing derivatives, we can use an initial value problem. For instance, say:

$$
f(0) = 1,~f(x) = \int 2x~dx
$$

Thus, $f(x) = x^2 + C$. Then, plugging in the initial value, $f(0) = 1$, so $(0^2) + C = 1$, so $C = 1$. Therefore:

$$
f(x) = x^2 + 1
$$

## Summation notation

Summation notation is denoted by the summation sign:

$$
\sum_{i = 0}^n a_i
$$

This means to sum from $a_0$ to $a_n$ - that is:

$$
\sum_{i = 0}^n a_i = a_0 + a_1 + a_2 + a_3 + \dots + a_{n - 1} + a_n
$$
## Rules of sums

$$
\sum_{i = 1}^n c a_i = c \sum_{i = 1}^n a_i
$$
$$
\sum_{i = 1}^n c = cn
$$
$$
\sum_{i = 1}^n a_i \pm b_i = \sum_{i = 1}^n a_i \pm \sum_{i = 1}^n b_i
$$
### Formulas for sums

$$
\sum_{i = 1}^n i = \frac{n(n + 1)}{2}
$$
$$
\sum_{i = 1}^n i^2 = \frac{n(n + 1)(2n + 1)}{6}
$$
$$
\sum _{i = 1}^n i^3 = \left(\frac{n(n + 1)}{2}\right)^2
$$
## Estimating areas

The left-hand approximation of an area under the curve is given by:

$$
A = \sum_{i = 0}^n f(x_i) \Delta x
$$

Given that:

$$
\Delta x = \frac{b - a}{n}
$$
$$
x_i = a + i\Delta x
$$
$$
x_{i + 1} = a + (i + 1) \Delta x
$$

The right-hand approximation of an area under the curve is given by:

$$
A = \sum_{i = 0}^n f(x_{i + 1}) \Delta x
$$
The midpoint approximation to the area is given by:

$$
A = \sum_{i = 0}^n f\left(\frac{x_i + x_{i + 1}}{n}\right) \Delta x
$$
## Finding areas

The precise area under a curve is given by:

$$
A = \lim_{n \to \infty} \sum_{i = 0}^n f(x_i) \Delta x
$$

For example, consider the area under the curve $f(x) = 4 - x^2$ from -2 to 2. We would then have:

$$
A = \lim_{n \to \infty} \sum_{i = 0}^n (4 - (-2 + i \Delta x)^2) \Delta x
$$
Since $\Delta x = \frac{b - a}{n}$, where $b = 2$ and $a = -2$, we would have:

$$
A = \lim_{n \to \infty} \sum_{i = 0}^n \left(4 - \left(-2 +  \frac{4i}{n}\right)^2\right) \frac{4}{n}
$$
This simplifies to:

$$
A = \lim_{n \to \infty} \sum_{i = 0}^n \frac{64i}{n^2} - \frac{64i^2}{n^3}
$$
Using the sum rules, we get:

$$
A = \lim_{n \to \infty} \sum_{i = 0}^n \frac{64}{n^2} \frac{n(n + 1)}{2} - \frac{64}{n^3} \frac{n(n + 1)(2n + 1)}{6}
$$

Which simplifies to:

$$
A = \lim_{n \to \infty} \sum_{i = 0}^n \frac{64(n + 1)}{2n} - \frac{64 (n + 1)(2n + 1)}{6n^2}
$$
Expanding this, we get:

$$
A = \lim_{n \to \infty} \sum_{i = 0}^n \frac{32}{3} - \frac{32}{3n^2}
$$

Now, taking the limit as $n \to \infty$, we get:

$$
A = \frac{32}{3}
$$
