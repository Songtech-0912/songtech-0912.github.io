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
\sum_{i = 1}^n i^3 = \left(\frac{n(n + 1)}{2}\right)^2
$$
## Estimating areas

The left-hand approximation of an area under the curve is given by:

$$
A_L = \sum_{i = 1}^{n} f(x_i) \Delta x
$$

Given that:

$$
\Delta x = \frac{b - a}{n}
$$

$$
x_i = a + (i - 1)\Delta x
$$

$$
x_{i + 1} = a + i \Delta x
$$

The right-hand approximation of an area under the curve is given by:

$$
A_R = \sum_{i = 1}^n f(x_{i + 1}) \Delta x
$$
The midpoint approximation to the area is given by:

$$
A_M = \sum_{i = 1}^{n} f\left(\frac{x_i + x_{i + 1}}{n}\right) \Delta x
$$

## Finding areas

The precise area under a curve is given by:

$$
A = \lim_{n \to \infty} \sum_{i = 1}^n f(x_i) \Delta x
$$

For example, consider the area under the curve $f(x) = 4 - x^2$ from -2 to 2. We would then have:

$$
A = \lim_{n \to \infty} \sum_{i = 1}^n (4 - (-2 + i \Delta x)^2) \Delta x
$$
Since $\Delta x = \frac{b - a}{n}$, where $b = 2$ and $a = -2$, we would have:

$$
A = \lim_{n \to \infty} \sum_{i = 1}^n \left(4 - \left(-2 +  \frac{4i}{n}\right)^2\right) \frac{4}{n}
$$
This simplifies to:

$$
A = \lim_{n \to \infty} \sum_{i = 1}^n \frac{64i}{n^2} - \frac{64i^2}{n^3}
$$
Using the sum rules, we get:

$$
A = \lim_{n \to \infty} \sum_{i = 1}^n \frac{64}{n^2} \frac{n(n + 1)}{2} - \frac{64}{n^3} \frac{n(n + 1)(2n + 1)}{6}
$$

Which simplifies to:

$$
A = \lim_{n \to \infty} \sum_{i = 1}^n \frac{64(n + 1)}{2n} - \frac{64 (n + 1)(2n + 1)}{6n^2}
$$
Expanding this and simplifying, we get:

$$
A = \lim_{n \to \infty} \sum_{i = 1}^n \frac{32}{3} - \frac{32}{3n^2}
$$

Now, taking the limit as $n \to \infty$, we get:

$$
A = \frac{32}{3}
$$

## Riemann sums and the definite integral

A Riemann sum is given by:

$$
\sum_{k = 1}^N f(c_k) \Delta x_k
$$
The definite integral is given by the limit of the Riemann sum, and represents the area under a curve:

$$
\int_a^b f(x)dx = \lim_{N \to \infty} \sum_{k = 1}^N f(c_k) \Delta x_k
$$
The definite integral can be evaluated in simple cases from just geometry, especially when the curve forms a semicircle, triangle, rectangle, or trapezoid with the x-axis.

## Applications of integration

Where do we use integration?

- Finding areas/surface areas/volumes/arc lengths
- Kinematics - such as finding total displacement, or finding velocity/position from acceleration  
- Solving differential equations
- Computing work/potential energy/total energy/
- Finding total charge/total current/total mass/center of mass/moment of inertia
- Finding force from potential energy
- Computing probability and finding average values
- Calculating electric fields and magnetic fields
- And many, many more places...

## Rules of definite integrals

$$
\int_a^b f(x) dx = -\int_b^a f(x) dx
$$
$$
\int_a^a f(x) dx = 0
$$
$$
\int_a^b c f(x) dx = c\int_a^b f(x) dx
$$
$$
\int_a^c f(x) dx = \int_a^b f(x) dx + \int_b^c f(x) dx
$$

## Fundamental Theorem of Calculus

There are two parts to the Fundamental Theorem of Calculus (FTC). Part 1 of the FTC states that:

$$
F(x) = \int f(x) dx \Rightarrow \int_a^b f(x) dx = F(b) - F(a) 
$$

That is, if $F(x)$ is the indefinite integral of $f(x)$, then the definite integral of $f(x)$ can be found by evaluating $F(x)$ at 2 points.

Part 2 of the FTC states that:

$$
\frac{d}{dx} \int_a^x f(t) dt = f(x)
$$

That is, the derivative of the indefinite integral of a function from any number to $x$ is equal to the same function evaluated at $x$. Or more simply, integrals are the inverse of derivatives.

## Integration by substitution

Consider a composite function of the form $f(g(x)) g'(x)$. If we make the substitution $u = g(x)$, then we can rewrite this as $f(u) u'$. Then the chain rule applies in reverse:

$$
\int f(u(x)) u'(x) dx = \int f(u) du =  F(u) + C
$$
This is called integration by **u-substitution**. The trick is to find an "inner function" $u$ in a composite function whose derivative also appears in that same composite function. 

As an example, we want to evaluate:

$$
\int \frac{2}{t- 4} dt
$$

We want to find an inner function $u$ whose derivative also appears. That is, we want to rewrite the function in the form:

$$
\int f(u) u' dt
$$

Here, we can choose $u = t - 4$, which means $f(u) = \frac{2}{u}$. So this means we have:

$$
\int f(u) u' dt = \int \frac{2}{u} u' dt
$$
But we still need to find $u'$. Taking the derivative of $u$, we have:

$$
\frac{du}{dt} = 1
$$
Then we can apply the substitution rule:

$$
\int \frac{2}{u} u' dt = \int \frac{2}{u} (1) du = 2\ln |u| + C = 2\ln | t- 4| + C
$$

For a more complicated example, we may perhaps want to integrate:

$$
\int \frac{\cos (\ln x)}{x} dx
$$
Here, we let $u = \ln x$. We can employ a notational shorthand for expediting the substitution rule that does not require rewriting the function in a form $f(u) u'$. Instead, we can say that:

$$
u = \ln x \Rightarrow \frac{du}{dx} = \frac{1}{x}
$$
$$
x\, du = dx
$$

Then, we can substitute in $x\, du$ for $dx$:

$$
\int \frac{\cos (\ln x)}{x} dx = \int \frac{\cos u}{x} x\, du = \int \cos u~du = \sin(u) + C = \sin(\ln x) + C
$$
To evaluate definite integrals with substitution, we have:

$$
\int_a^b f(u) u' dx = \int_{u(a)}^{u(b)} f(u) du
$$
## Integrals of other elementary functions

$$
\int \frac{dx}{\sqrt{1 - x^2}} = \sin^{-1}(x) + C
$$
$$
\int \frac{dx}{x^2 + 1} = \tan^{-1} (x) + C
$$
$$
\int \frac{dx}{|x| \sqrt{x^2 -1}} = \sec^{-1} |x| + C
$$
$$
\int b^x = \frac{b^x}{\ln b} + C
$$

## Average value of a function

The average value of a function is given by:

$$
\frac{1}{b-a} \int f(x) dx
$$
The mean value theorem for integrals states that if $f$ is continuous on $[a, b]$, there is at least one $c$ value that satisfies:

$$
f(c) = \frac{1}{b - a} \int f(x) dx
$$
Remember, as with the MVT for derivatives, to ignore any values not in the interval!

## Area between curves

A region is vertically simple if it is bounded on the left and right by vertical lines, and bounded on the top and bottom by functions of $x$. A region is horizontally simple if it is bounded on the top and bottom by horizontal lines, and bounded on the left and right by functions of $y$.

The area between curves $f(x)$ and $g(x)$, assuming $f(x) \geq g(x)$ for all $x \in [a, b]$, is given by:

$$
\int_a^b f(x) - g(x) dx
$$
For curves $f(y)$ and $g(y)$, just replace every $x$ with $y$.

If $f(x) \ngeq g(x)$ for all $x \in [a, b]$, the area must be split into regions that are separately evaluated to make the condition true.
