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
