+++
title = "Introduction to Integral Calculus"
date = 2023-11-07
+++

These are notes taken during RPI's MATH 1010 course, on the topic of integrals and their applications in calculus.

<!-- more -->

## Antiderivatives

To introduce the topic of integral calculus, we must begin with understanding the notion of an _antiderivative_. An antiderivative (also called an _indefinite integral_, and we'll see why later) is the opposite of a derivative. The antiderivative of a particular function $f(x)$ is the function whose _derivative_ is $f(x)$. For example, $x^2$ is the antiderivative of $2x$, because $2x$ is the _derivative_ of $x^2$.

Antiderivatives are represented by the "curly S" integral sign (again for reasons that will make sense later), with a $dx$ representing the variable to take the antiderivative with respect to - in this case $x$:

{% math() %}
\int f(x) dx = F(x) + C
{% end %}

Since the derivative of a constant is zero, the antiderivative of $f(x) + 1$, $f(x) + 3$, or $f(x) + 100$ is the same. Thus we add the $C$ known as the constant of integration to remind us that multiple antiderivatives differing by a constant have the same derivative.

### Rules for antiderivatives (indefinite integral formulas)

The rules of antiderivatives (indefinite integrals) are the inverse of the rules for derivatives:

{% math() %}
\begin{align*}
\int k~dx &= kx + C \\
\int x^n~dx &= \frac{x^{n + 1}}{n + 1} + C \\
\int \frac{1}{x}~dx &= \ln |x| + C \\
\int e^x~dx &= e^x + C \\
\int b^x &= \frac{b^x}{\ln b} + C \\
\int \cos(x)~dx &= \sin(x) + C \\
\int \sin(x)~dx &= -\cos(x) + C \\
\int \frac{dx}{\sqrt{1 - x^2}} &= \operatorname{arcsin}(x) + C \\
\int \frac{dx}{1 + x^2} &= \operatorname{arctan}(x) + C \\
\int \frac{dx}{|x|\sqrt{x^2 - 1}} &= \operatorname{arcsec}(x) + C
\end{align*}
{% end %}

Note that the last few formulas for inverse trigonometric functions can be generalized to the following:

{% math() %}
\begin{align*}
\int \frac{du}{\sqrt{a^2 - u^2}} &= \operatorname{arcsin} \left(\frac{u}{a}\right) + C \\
\int \frac{du}{a^2 + u^2} &= \frac{1}{a} \operatorname{arctan} \left(\frac{u}{a}\right) + C \\
\int \frac{du}{|u|\sqrt{u^2 - a^2}} &= \frac{1}{a} \operatorname{arcsec} \left(\frac{u}{a}\right) + C
\end{align*}
{% end %}

Where $u = u(x)$ is some function of $x$, and $du = u'(x) dx$. For more formulas of integrals, a good resource to reference is <https://www.integral-table.com/>.

### Initial value problems

To find the value of the $C$ when doing derivatives, we can use an initial value problem. For instance, say:

{% math() %}
f(0) = 1,~f(x) = \int 2x~dx
{% end %}

Thus, $f(x) = x^2 + C$. Then, plugging in the initial value, $f(0) = 1$, so $(0^2) + C = 1$, so $C = 1$. Therefore:

{% math() %}
f(x) = x^2 + 1
{% end %}

## Sums

We will now jump to a topic that might _initially_ appear to be completely unrelated - sums and areas. A sum is just what it means - adding a group of numbers (or variables) together. Sums are denoted by the summation sign $\displaystyle \sum$. For instance, one sum could be:

{% math() %}
\sum_{i = 0}^n a_i
{% end %}

This means to sum from $a_0$ to $a_n$ - that is:

{% math() %}
\sum_{i = 0}^n a_i = a_0 + a_1 + a_2 + a_3 + \dots + a_{n - 1} + a_n
{% end %}

### Rules of sums

If we are given a sum, we might be interested in what the sum evaluates to (or we might not, but pretend that we are for the time being). Evaluating sums is actually _not possible_ in many cases. However, in cases where a sum _can_ be evaluated, it often helps to use the below identities:

{% math() %}
\begin{align*}
\sum_{i = 1}^n c a_i &= c \sum_{i = 1}^n a_i \\
\sum_{i = 1}^n c &= cn \\
\sum_{i = 1}^n a_i \pm b_i &= \sum_{i = 1}^n a_i \pm \sum_{i = 1}^n b_i
\end{align*}
{% end %}

There also exist special sums that have well-known solutions - these are extremely helpful for evaluating more complicated sums, and they are given below:

{% math() %}
\begin{align*}
\sum_{i = 1}^n i &= \frac{n(n + 1)}{2} \\
\sum_{i = 1}^n i^2 &= \frac{n(n + 1)(2n + 1)}{6} \\
\sum_{i = 1}^n i^3 &= \left(\frac{n(n + 1)}{2}\right)^2
\end{align*}
{% end %}

### Finding and estimating areas

We will now turn to a very useful application of sums - finding _areas_. The idea is this: if we had some shape modelled by a function $f(x)$, then we can approximate the area under the curve by "slicing" the area under the curve into small rectanges, each of width $\Delta x$ (which is some small number) and of height $f(x_i)$. This is called the **left-hand approximation** of an area under the curve, and is given by:

{% math() %}
A_L = \sum_{i = 1}^{n} f(x_i) \Delta x
{% end %}

Given that:

{% math() %}
\begin{matrix*}
\Delta x = \dfrac{b - a}{n},
&x_i = a + (i - 1)\Delta x.
&x_{i + 1} = a + i \Delta x
\end{matrix*}
{% end %}

The right-hand approximation of an area under the curve is given by:

{% math() %}
A_R = \sum_{i = 1}^n f(x_{i + 1}) \Delta x
{% end %}

The midpoint approximation to the area is given by:

{% math() %}
A_M = \sum_{i = 1}^{n} f\left(\frac{x_i + x_{i + 1}}{n}\right) \Delta x
{% end %}

Now, these are approximations for finite sums, but in the limit as we sum over increasingly many and increasingly tiny rectangles, we obtain a formula for the _exact_ area under a curve:

{% math() %}
A = \lim_{n \to \infty} \sum_{i = 1}^n f(x_i) \Delta x
{% end %}

For example, consider the area under the curve $f(x) = 4 - x^2$ from -2 to 2. We would then have:

{% math() %}
A = \lim_{n \to \infty} \sum_{i = 1}^n (4 - (-2 + i \Delta x)^2) \Delta x
{% end %}

Since $\Delta x = \frac{b - a}{n}$, where $b = 2$ and $a = -2$, we would have:

{% math() %}
A = \lim_{n \to \infty} \sum_{i = 1}^n \left(4 - \left(-2 +  \frac{4i}{n}\right)^2\right) \frac{4}{n}
{% end %}

This simplifies to:

{% math() %}
A = \lim_{n \to \infty} \sum_{i = 1}^n \frac{64i}{n^2} - \frac{64i^2}{n^3}
{% end %}

Using the sum rules, we get:

{% math() %}
A = \lim_{n \to \infty} \sum_{i = 1}^n \frac{64}{n^2} \frac{n(n + 1)}{2} - \frac{64}{n^3} \frac{n(n + 1)(2n + 1)}{6}
{% end %}

Which simplifies to:

{% math() %}
A = \lim_{n \to \infty} \sum_{i = 1}^n \frac{64(n + 1)}{2n} - \frac{64 (n + 1)(2n + 1)}{6n^2}
{% end %}

Expanding this and simplifying, we get:

{% math() %}
A = \lim_{n \to \infty} \sum_{i = 1}^n \frac{32}{3} - \frac{32}{3n^2}
{% end %}

Now, taking the limit as $n \to \infty$, we get:

{% math() %}
A = \frac{32}{3}
{% end %}

### Riemann sums and the definite integral

From our previous discussion of the limit of sums, we can now formalize the idea of computing the area under a curve. A Riemann sum is given by:

{% math() %}
\sum_{k = 1}^N f(x_k) \Delta x_k
{% end %}

The **definite integral** is given by the limit of the Riemann sum, and represents the area under a curve, where $A$ is the area and $y = f(x)$ is the equation of the curve:

{% math() %}
A = \int_a^b f(x)dx = \lim_{N \to \infty} \sum_{k = 1}^N f(x_k) \Delta x_k
{% end %}

The definite integral also has some convenient properties that will come in handy later:

{% math() %}
\begin{gather*}
\int_a^b f(x) dx = -\int_b^a f(x) dx \\
\int_a^a f(x) dx = 0 \\
\int_a^b c f(x) dx = c\int_a^b f(x) dx \\
\int_a^c f(x) dx = \int_a^b f(x) dx + \int_b^c f(x) dx
\end{gather*}
{% end %}

Evaluating the definite integral is called **integration**. The definite integral can be evaluated in simple cases from just geometry, especially when the curve forms a semicircle, triangle, rectangle, or trapezoid with the x-axis. However, in most cases, integration is not an easy task - some definite integrals are almost impossible to solve!

## Applications of integration

We described integration from the point of view of finding the area under a curve, but integration is far more general than an area-finding method. Indeed, integration is ubiquitous in the mathematical sciences, with myriad applications:

- Finding areas/surface areas/volumes/distances
- Kinematics - such as finding total displacement, or finding velocity/position from acceleration  
- Solving differential equations
- Computing work/potential energy/total energy/
- Finding total charge/total current/total mass/center of mass/moment of inertia
- Finding force from potential energy
- Computing probability and finding average values
- Calculating electric fields and magnetic fields
- And many, many more places...

## The Fundamental Theorem of Calculus

There are two parts to the Fundamental Theorem of Calculus (FTC). Part 1 of the FTC states that:

{% math() %}
F(x) = \int f(x) dx \Rightarrow \int_a^b f(x) dx = F(b) - F(a) 
{% end %}

That is, if $F(x)$ is the indefinite integral of $f(x)$, then the definite integral of $f(x)$ can be found by evaluating $F(x)$ at 2 points.

Part 2 of the FTC states that:

{% math() %}
\frac{d}{dx} \int_a^x f(t) dt = f(x)
{% end %}

That is, the derivative of the indefinite integral of a function from any number to $x$ is equal to the same function evaluated at $x$. Or more simply, integrals are the inverse of derivatives.

## Integration by substitution

Consider a composite function of the form $f(g(x)) g'(x)$. If we make the substitution $u = g(x)$, then we can rewrite this as $f(u) u'$. Then the chain rule applies in reverse:

{% math() %}
\int f(u(x)) u'(x) dx = \int f(u) du =  F(u) + C
{% end %}

This is called integration by **u-substitution**. The trick is to find an "inner function" $u$ in a composite function whose derivative also appears in that same composite function. 

As an example, we want to evaluate:

{% math() %}
\int \frac{2}{t- 4} dt
{% end %}

We want to find an inner function $u$ whose derivative also appears. That is, we want to rewrite the function in the form:

{% math() %}
\int f(u) u' dt
{% end %}

Here, we can choose $u = t - 4$, which means $f(u) = \frac{2}{u}$. So this means we have:

{% math() %}
\int f(u) u' dt = \int \frac{2}{u} u' dt
{% end %}

But we still need to find $u'$. Taking the derivative of $u$, we have:

{% math() %}
\frac{du}{dt} = 1
{% end %}

Then we can apply the substitution rule:

{% math() %}
\int \frac{2}{u} u' dt = \int \frac{2}{u} (1) du = 2\ln |u| + C = 2\ln | t- 4| + C
{% end %}

For a more complicated example, we may perhaps want to integrate:

{% math() %}
\int \frac{\cos (\ln x)}{x} dx
{% end %}

Here, we let $u = \ln x$. We can employ a notational shorthand for expediting the substitution rule that does not require rewriting the function in a form $f(u) u'$. Instead, we can say that:

{% math() %}
u = \ln x \Rightarrow \frac{du}{dx} = \frac{1}{x}
{% end %}
{% math() %}
x\, du = dx
{% end %}

Then, we can substitute in $x\, du$ for $dx$:

{% math() %}
\int \frac{\cos (\ln x)}{x} dx = \int \frac{\cos u}{x} x\, du = \int \cos u~du = \sin(u) + C = \sin(\ln x) + C
{% end %}

To evaluate definite integrals with substitution, we have:

{% math() %}
\int_a^b f(u) u' dx = \int_{u(a)}^{u(b)} f(u) du
{% end %}

### Integration of functions using the natural log trick

A direct consequence of the substitution method for integrals is the "natural log trick":

{% math() %}
\int \frac{u'}{u} = \ln | u | + C
{% end %}

As an example to illustrate why this formula is the case, let us take the example of evaluating the following integral:

{% math() %}
\int \tan(5x) dx
{% end %}

We first rewrite tangent in terms of sine and cosine:

{% math() %}
\int \frac{\sin x}{\cos x} dx
{% end %}

If we use the substitution $u = \cos x$, we have::

{% math() %}
\begin{gather*}
\frac{du}{dx} = -\sin x
dx = \frac{du}{-\sin x}
\end{gather*}
{% end %}

This means that:

{% math() %}
\begin{align*}
\int \frac{\sin x}{\cos x} dx &= \int \frac{\sin x}{-\sin x} \frac{1}{u} du \\
&= -\int \frac{1}{u} du \\
&= -\ln | \cos(u) | + C
\end{align*}
{% end %}

#### Differential equations with the natural log trick

We may use the natural log trick to solve not only integrals, but also _differential equations_. Differential equations specify a derivative of an unknown function as a function of $x$, $y$, or some other variables; the goal is to find the exact form of the unknown function. Consider, for instance, the differential equation: 

{% math() %}
\frac{dy}{dx} = \frac{2x}{x^2 - 9}
{% end %}

To solve this differential equation, we can multiply by $dx$ on both sides. However, this must be done in secret because this operation is technically "illegal" in mathematical terms (derivatives _are not fractions_; it just happens that sometimes they can be treated as such). One must then leave the scene of the mathematical crime and erase all the evidence used to find the answer. So we shall now commit the crime in question, and multiply by $dx$ on both sides, which results in:

{% math() %}
dy = \frac{2x}{x^2 - 9} dx
{% end %}

If we integrate both sides, we then have:

{% math() %}
\int dy = y = \int \frac{2x}{x^2 - 9} dx
{% end %}

This is where we can use the natural log trick. Let $u = x^2 - 9$. Then:

{% math() %}
\begin{align*}
\frac{du}{dx} &= 2x \\
\frac{du}{2x} &= dx \\
y &= \int \frac{2x}{2x} \frac{1}{u} du \\
&= \int \frac{1}{u} du \\
&= \ln|x^2 - 9| + C
\end{align*}
{% end %}

Which is the _general solution_ to our differential equation.

## Average value of a function

We may also use integration to find the _average_ value of a function, which is very useful for continuously-varying data (like velocity or position). The average value of a function is given by:

{% math() %}
\frac{1}{b-a} \int f(x) dx
{% end %}

The mean value theorem for integrals states that if $f$ is continuous on $[a, b]$, there is at least one $c$ value that satisfies:

{% math() %}
f(c) = \frac{1}{b - a} \int f(x) dx
{% end %}

Remember, as with the MVT for derivatives, to ignore any values not in the interval!

## Area between curves

A region is vertically simple if it is bounded on the left and right by vertical lines, and bounded on the top and bottom by functions of $x$. A region is horizontally simple if it is bounded on the top and bottom by horizontal lines, and bounded on the left and right by functions of $y$.

The area between curves $f(x)$ and $g(x)$, assuming $f(x) \geq g(x)$ for all $x \in [a, b]$, is given by:

{% math() %}
\int_a^b f(x) - g(x) dx
{% end %}

> **Other specific cases:** For curves $f(y)$ and $g(y)$, just replace every $x$ with $y$. If $f(x) \ngeq g(x)$ for all $x \in [a, b]$, the area must be split into regions that are separately evaluated to make the condition true.

## Solids of revolution

Another application of integrals generalizes the area-finding process to finding the surface area and volume of a particular shape. Such shapes must have a specific requirement: they have to be **rotationally-symmetric**, and thus we call them **solids of revolution**. By nature of their rotational symmetry, they are obtained by the rotation of a region in the xy-plane about an axis. 

> **Note:** Unlike many other uses of integration, this particular application of integrals is not very widely used in physics or applied math areas, but they are a good teaching/learning tool to practice integration.

### Disk method

Using the disk method of finding the volume of a solid of revolution, the solid of revolution created from the region underneath the curve $f(x)$ has the volume:

{% math() %}
V = \int_a^b \pi [f(x)]^2 dx
{% end %}

And for a function $f(y)$, the volume is given by:

{% math() %}
V = \int_a^b \pi [f(y)]^2 dy
{% end %}

For example, say we wanted to find the volume of a sphere. A sphere is simply the solid of revolution created by rotating the curve $f(x) = \sqrt{r^2 - x^2}$ about the x-axis. So, we would have:

{% math() %}
V = \pi \int_{-r}^r (\sqrt{r^2 - x^2})^2~dx
{% end %}

Which becomes:

{% math() %}
V = \pi \int_{-r}^r r^2 - x^2 dx
{% end %}

Since $r$ is a constant, the integral becomes:

{% math() %}
V = \frac{4}{3} \pi r^3
{% end %}

Which is the volume of a sphere!

### Washer method

Using the washer method of finding the volume of a solid of revolution, the solid of revolution created by the region between two curves $f(x)$ and $g(x)$ is given by:

{% math() %}
V = \int_a^b \pi [f(x)]^2 - \pi [g(x)]^2 dx
{% end %}

And similarly for $y$:

{% math() %}
V = \int_a^b \pi [f(y)]^2 - \pi [g(y)]^2 dy
{% end %}

### Shells method

Using the shells method of finding the volume of a solid of revolution, the solid of revolution created by the region underneath the curve $f(x)$ is given by:

{% math() %}
V = \int_a^b 2\pi rf(x) dx
{% end %}

And similarly for $y$:

{% math() %}
V = \int_a^b 2\pi rf(y) dy
{% end %}

If the region is instead between two curves $f(x)$ and $g(x)$, then the volume is instead given by:

{% math() %}
V = \int_a^b 2\pi r[f(x) - g(x)] dx
{% end %}

Or for $y$:

{% math() %}
V = \int_a^b 2\pi r[f(y) - g(y)] dy
{% end %}

For instance, suppose we were to find the volume of the solid of revolution created by revolving the region bound by $f(x) = x^3, x \in [0, 2]$ and the x-axis about the line $x = 3$. A visualization of this region can be found at <https://www.desmos.com/calculator/ymuwqk1xk7>.

To compute the area, we'll first find the radii of the shells, and set that. In this case, the radius would be $3 - x$, as that is the distance from the rotational axis to the edge of the shell. The bounds of integration would be from 0 to 2, as we want to create shells that fill up the space of the region, and the region is bounded by $x = 0$ and $x = 2$. Therefore, the integral is:

{% math() %}
2\pi \int_0^2  (3 - x) x^3 dx = \frac{56\pi}{5}
{% end %}

## Integration by Parts

**Integration by parts** is analagous to the product rule for derivatives. It is given by:

{% math() %}
\int udv = uv - \int vdu
{% end %}

where:

{% math() %}
v = \int dv
{% end %}

Typically, we want $u$ to be a function that has a simple derivative (such as a polynomial or $\ln x$), and $v$ to be a function that has a simple integral (such as $\cos x$ or $\sec^2 x$ or $e^x$). It's typically much harder to integrate than differentiate, so pick $dv$ first, and $u$ second.

In addition, integration by parts can be done multiple times over and over to repeatedly expand out an integral until it can be solved.

As an example of integration by parts, consider:

{% math() %}
\int x \cos (2x) dx
{% end %}

Here, we want our $u$ to be $x$ (because that's easy to differentiate), and $dv = \cos 2x$. This means that $du = dx$. To find $v$, we simply do:

{% math() %}
v = \int dv = \int \cos (2x) = \frac{1}{2} \sin(2x)
{% end %}

After substitution, we obtain:

{% math() %}
\int udv = \frac{1}{2}x \sin(2x) - \int \frac{1}{2} \sin(2x) dx
{% end %}

Which evaluates to:

{% math() %}
\frac{1}{2} x \sin(2x) + \frac{1}{4} \cos(2x) + C
{% end %}

For a faster method of integration by parts, we can use the tabular method, which works so long as $u$ is a polynomial. For instance, consider:

{% math() %}
\int x^3 e^x dx
{% end %}

We construct a table of $u$ and all its derivatives (D) on the left, and $dv$ and all its integrals (I) on the right, and alternating signs in front, until the derivative is zero:

| Sign | D | I |
|----|---|---|
| + | $x^3$ | $e^x $ |
| - | $3x^2$ | $e^x$ |
| + | $6x$ | $e^x$ |
| - | $6$ | $e^x$ |
| + | $0$ | $e^x$ |

Now, we start from the first "D" term, and match terms crosswise down diagonally like this:

| Sign | D | I |
|----|---|----|
| + | 1 | |
| - | 2 | 1 |
| + | 3 | 2 |
| - | 4 | 3 |
| + | 5 | 4 |
| ... | ... | ... |

In front of each derivative term we put the sign associated with it. Therefore, our result is:

{% math() %}
(+) x^3 e^x (-) 3x^2 e^x (+)6x e^x (-) 6e^x + C
{% end %}

Or simplified:

{% math() %}
x^3 e^x - 3x^2 e^x + 6xe^x - 6e^x + C
{% end %}

A third type of integration-by-parts integrals utilize a specialized technique. Consider:

{% math() %}
\int e^x \cos x dx
{% end %}

Doing a first integration by parts with $u = e^x$ and $dv = \cos x$, we get:

{% math() %}
\int e^x \cos x dx = e^x \sin x - \int e^x \sin x dx
{% end %}

Now repeating the integration by parts on the second integral with $u = e^x$ and $dv = \sin x$, we get:

{% math() %}
\int e^x \cos x dx = e^x \sin x - \left(-e^x \cos x - \int(-e^x\cos x dx)\right)
{% end %}

Or simplifying:

{% math() %}
\int e^x \cos x dx = e^x \sin x + e^x \cos x - \int e^x \cos x dx
{% end %}

Notice how the integral appears twice in the expression. If we say that:

{% math() %}
I = \int e^x \cos x dx
{% end %}

We can rewrite the integral as:

{% math() %}
I = e^x \sin x + e^x \cos x- I
{% end %}

Solving for $I$, we get:

{% math() %}
I = \frac{e^x \sin x + e^x \cos x}{2} + C
{% end %}

which is the solution to the integral.

## Trigonometric integrals

Trigonometric integrals are integrals that involve combination of trigonometric functions.

The first general category of trigonometric integrals are in the form:

{% math() %}
\int \sin^m x \cos^n x dx
{% end %}

There are several common approaches for such integrals:

- If $m$ is odd ($n = 2k + 1$), rewrite $\sin^m x = (\sin^2 x)^k \sin x = (1 - \cos^2 x)^k \sin x$, then use u-substitution
- If $n$ is odd ($n = 2k + 1$), rewrite $\cos^n x = (\cos^2 x)^k \cos x = (1 - \sin^2 x)^k \cos x$, then use u-substitution
- If both $m$ and $n$ are even, use the half-angle identities:

{% math() %}
\begin{align*}
\sin^2x &= \frac{1 - \cos 2x}{2} \\
\cos^2 x &= \frac{1 + \cos 2x}{2} \\
\sin x \cos x &= \frac{\sin 2x}{2}
\end{align*}
{% end %}

Meanwhile, for trigonometric integrals in the general form:

{% math() %}
\int \tan^m x \sec^n x dx
{% end %}

- If $n$ is even ($n = 2k, k \geq 2$), rewrite $\sec^n x = (\sec^2 x)^{k - 1} \sec^2 x = (\tan^2 x + 1)^{k - 1} \sec^2 x$, then use u-substitution with $u = \tan x$
- If $m$ is odd ($m = 2k + 1$), rewrite $\tan^m x = (\tan^2 x)^k \tan x = (\sec^2 x - 1)^k \tan x$, then use u-substitution with $u = \sec x$

For instance, consider:

{% math() %}
\int \sin^5 x \cos^4 x dx
{% end %}

We can break this into:

{% math() %}
\int \sin^4 x \sin x \cos^4 xdx
{% end %}

Which we can simplify into:

{% math() %}
\int (\sin^2 x)^2 \sin x \cos^4 x dx
{% end %}

And again, into:

{% math() %}
\int (1 - \cos^2 x)^2 \sin x \cos^4 x dx
{% end %}

Now, we can use $u = \cos x$, thus the integral becomes:

{% math() %}
-\int (1 - u^2)^2 u^4 du
{% end %}

Or expanded and with the negative sign distributed:

{% math() %}
\int 2u^6 - u^4 - u^8 du
{% end %}

This becomes:

{% math() %}
\frac{2u^7}{7} - \frac{u^5}{5} - \frac{u^9}{9} + C
{% end %}

And substituting back, we have:

{% math() %}
\frac{2 \cos^7 x}{7} - \frac{\cos^5 x}{5} - \frac{\cos^9 x}{9} + C
{% end %}

## Trigonometric substitutions

For integrals in the form:

{% math() %}
\int (a^2 \pm x^{2n})^m dx
{% end %}

or generally, any integrals that have $\sqrt{a^2 - u^2}$, $\sqrt{a^2 + u^2}$, or $a^2 + u^2$, a trigonometric substitution is often helpful.

The substitutions make use of the 3 Pythagorean identities:

{% math() %}
\begin{cases}
\sin^2 \theta + \cos^2 \theta = 1 \\
1 + \tan^2 \theta = \sec^2 \theta \\
1 + \cot^2 \theta = \csc^2 \theta
\end{cases}
{% end %}

Performing a trigonometric substitution involves fitting an integrand into one of these forms. For instance, consider the integral:

{% math() %}
\int \frac{\sqrt{4 - x^2}}{x^2} dx
{% end %}

Here, we see the square root, which suggests the use of a trigonometric substitution. We first simplify the integral with:

{% math() %}
\int \frac{\sqrt{4(1 - \frac{x^2}{4})}}{x^2} dx
{% end %}

We now have an expression in the form $1 - u^2$. It makes sense to use the first Pythagorean identity. We say that:

{% math() %}
\frac{x^2}{4} = \sin^2 \theta
{% end %}

Which means:

{% math() %}
1 - \frac{x^2}{4} = 1 - \sin^2 \theta = \cos^2 \theta
{% end %}

If we solve for $x$, we get:

{% math() %}
x = 2\sin \theta
{% end %}

So:

{% math() %}
dx = 2\cos \theta d\theta
{% end %}

Plugging in $1 - \frac{x^2}{4} = \cos^2 \theta$ and $dx = 2\cos \theta d\theta$ into the integral, we get:

{% math() %}
\int \frac{\sqrt{4\cos^2 \theta}}{4\sin^2 \theta} 2 \cos \theta d\theta
{% end %}

Which simplifies to:

{% math() %}
\int \cot^2 \theta d\theta
{% end %}

We use the identity $\cot^2 \theta + 1 = \csc^2 \theta$ to get:

{% math() %}
\int \csc^2\theta - 1 d\theta
{% end %}

Whose solution is:

{% math() %}
-\cot \theta - \theta + C
{% end %}

We now need to convert the answer in terms of $\theta$ back into an answer in terms of $x$. To do so, remember that:

{% math() %}
x = 2 \sin \theta
{% end %}

Therefore:

{% math() %}
\sin \theta = \frac{x}{2} = \frac{\text{Opposite}}{\text{Hypotenuse}}
{% end %}

We also know that:

{% math() %}
\cot \theta = \frac{1}{\tan \theta} = \frac{\text{Adjacent}}{\text{Opposite}}
{% end %}

And by Pythagoras's theorem, we have:

{% math() %}
\begin{align*}
\text{Adjacent}^2 &= \text{Hypotenuse}^2 - \text{Opposite}^2 \\
&= 2^2 - x^2 \\ &= 4 - x^2
\end{align*}
{% end %}

So:

{% math() %}
\text{Adjacent} = \sqrt{4 - x^2}
{% end %}

And:

{% math() %}
\begin{align*}
\cot \theta &= \frac{\sqrt{4 - x^2}}{x} \\
\theta &= \operatorname{arcsin} \left(\frac{x}{2}\right)
\end{align*}
{% end %}

We can now rewrite the solution in terms of $x$:

{% math() %}
-\frac{\sqrt{4 - x^2}}{x} - \operatorname{arcsin} \left(\frac{x}{2}\right) + C
{% end %}

Similarly, we can solve the following integral by trigonometric substitution:

{% math() %}
\int \frac{dt}{(9t^2 + 4)^2}
{% end %}

We first factor:

{% math() %}
\int \frac{dt}{(4(\frac{9}{4}t^2 + 1))^2}
{% end %}

We set:

{% math() %}
\begin{align*}
1 + \frac{9}{4} t^2 &= \sec^2 \theta \\
\frac{9}{4} t^2 &= \tan^2 \theta
\end{align*}
{% end %}

Therefore:

{% math() %}
\begin{align*}
t &= \frac{2}{3} \tan \theta \\
dt &= \frac{2}{3} \sec^2 \theta d \theta
\end{align*}
{% end %}

Subtituting, we get:

{% math() %}
\frac{2}{3} \int \frac{dt}{(4\sec^2 \theta)^2)} \sec^2 \theta d \theta
{% end %}

Which becomes:

{% math() %}
\frac{1}{48} \int \cos^2 \theta d \theta
{% end %}

Trigonometric substitutions are incredibly easy to mess up, so be careful with them, and make sure to avoid these errors:
- Not cancelling out the powers correctly
- Using the incorrect trigonometric identity
- Calculating the incorrect differential
- Forgetting to carry over constants
- Simplification errors in the trigonometric integrand
- Errors in converting the solution in $\theta$ back to a solution in $x$, often due to forgetting a square root or a square when using Pythagoras

## Integration by long division and partial fractions

Consider an integral in the form:

{% math() %}
\int \frac{P(x)}{Q(x)} dx
{% end %}

If the degree of $P(x)$ is higher than the degree of $Q(x)$, then the integrand can be simplified by dividing $P(x)$ by $Q(x)$ using polynomial long division. The process is analogous to arithmetic long division.

When doing long division, be very careful of signs while subtracting. It is easy to get the wrong result just by forgetting a negative sign when doing a subtraction. Also, don't forget to carry over the remainder. Whenever possible, split up the resulting fraction when you integrate, so for instance, something like:

{% math() %}
\int 2x dx + \frac{5x + 3}{x - 1} dx
{% end %}

becomes:

{% math() %}
\int 2x dx + \int \frac{5x}{x - 1} dx + \frac{3}{x - 1} dx
{% end %} 

In cases where long division cannot be done, a partial fraction decomposition can be performed instead. The goal of partial fraction decomposition is to write the integrand as a sum of simpler fractions. That is:

{% math() %}
\frac{P(x)}{Q(x)} = \frac{A}{F_1(x)} + \frac{B}{F_2(x)} + \frac{C}{F_3(x)} + \dots + \frac{Z}{F_n(x)}
{% end %}

The first step of a partial fraction decomposition is to factor $Q(x)$ as completely as possible. That is, the integrand should take the following form:

{% math() %}
\frac{P(x)}{Q(x)} = \frac{P(x)}{F_1(x)F_2(x)F_3(x)\dots F_n(x)}
{% end %}

Where $F_1, F_2, F_3, \dots, F_n$ are the factors of $Q(x)$. If a factor of $Q(x)$ is in the form $(x - a)^n$, where $a$ is not a complex number or radical, it is called a **linear factor**. Such a factor contributes a partial fraction decomposition of the form:

{% math() %}
\frac{1}{(x - a)^n} = \frac{A}{x - a} + \frac{B}{(x - a)^2} + \frac{C}{(x - a)^3} + \dots + \frac{Z}{(x - a)^n}
{% end %}

Note that a factor in the form $x^n$ (such as $x^2$ or $x$) can technically be written in the form $(x - 0)^n$, and so also qualifies as a linear factor.

Meanwhile, if the factor is in the form $(x^2 + ax + b)^n$, and cannot be simplified further without using radicals or complex numbers, it is called an **irreducible quadratic factor**. Such a factor contributes a partial fraction decomposition of the form:

{% math() %}
\frac{1}{(x^2 + ax + b)^n} = \frac{Ax + C_1}{x^2 + ax + b} + \frac{Bx + C_2}{(x^2 + ax + b)^2} + \dots + \frac{Zx + C_n}{(x^2 + ax + b)^n}
{% end %}

As an example, consider the integral:

{% math() %}
\int \frac{x + 5}{x^2 + x - 2} dx
{% end %}

We first factor:

{% math() %}
\int \frac{x + 5}{(x - 1)(x + 2)} dx
{% end %}

Now we perform a partial fraction composition of the integrand. Since we see that the factors are linear, we propose that the integrand take the form:

{% math() %}
\frac{x + 5}{(x - 1)(x + 2)} = \frac{A}{x - 1} + \frac{B}{x + 2}
{% end %}

If we distribute by multiplying every term by $(x - 1)(x + 2)$, we get:

{% math() %}
x + 5 = A(x + 2) + B(x - 1)
{% end %}

We can now substitute in convenient values to find $A$ and $B$. For instance, if we evaluate with $x = 1$, then:

{% math() %}
(1 + 5) = A(1 + 2) + B(1 - 1)
{% end %}

which simplifies to:

{% math() %}
6 = 3A
{% end %}

Therefore $A = 2$. Similarly, if we evaluate with $x = -2$, then:

{% math() %}
(-2 + 5) = A(-2 + 2) + B(-2 - 1)
{% end %}

which simplifies to:

{% math() %}
3 = -3B
{% end %}

Therefore $A = 2, B = -1$. Placing the partial fraction decomposition back into the integrand, we have:

{% math() %}
\int \frac{2}{x - 1} - \frac{1}{x + 2}~dx
{% end %}

which becomes:

{% math() %}
2 \ln | x - 1 | - \ln | x + 2 | + C
{% end %}

When doing partial fraction decompositions, make sure that if the fraction is improper, that you first do long division, and then (if the result isn't simple enough to directly integrate) decompose using partial fractions. In addition, be careful about identifying factors - sometimes factors that might look linear factorable might be irreducible quadratics, and factors that look like quadratics are linear factorable.

Finally, when convenient cancelling isn't possible, use variations of x-values (e.g. evaluate when $x = 0$, then $x = 1$, then $x = 2$) for getting partial fraction decompositions when there are multiple repeated factors. This allows you to setup a system of equations that you can solve to find the coefficients of the partial fraction decomposition.

After finding the partial fraction decomposition of a rational function, it is always best to plug in a value of $x$ (such as $x = 0$ or $x = 1$) and check that the partial fraction outputs the same value as the original integrand. This means the partial fraction decomposition is correct.

## Improper integrals

A improper integral is an integral defined either on an unbounded domain, or a domain that is not integratable, then:

{% math() %}
\int_a^k f(x) dx = \lim_{b \to k} \int_a^b f(x) dx
{% end %}

An improper integral satisfies the identities:

{% math() %}
\begin{align*}
\int_0^\infty f(x)dx &= \lim_{b \to \infty} \int_0^b f(x) dx \\
\int_{-\infty}^0 f(x)dx &= \lim_{b \to -\infty} \int_b^0 f(x) dx \\
\int_{-\infty}^\infty f(x) dx &= \lim_{a \to -\infty} \int_a^0 f(x) dx + \lim_{b \to \infty} \int_0^b f(x) dx
\end{align*}
{% end %}

If the limit exists (evaluates to a finite number), then the integral is said to **converge**; otherwise, the integral is said to **diverge**.

For instance, consider the integral:

{% math() %}
\int_1^\infty \frac{1}{x^2} dx
{% end %}

Using the approach outlined previously, we rewrite as a limit:

{% math() %}
\lim_{b \to \infty} \int_1^b \frac{1}{x^2} dx = \lim_{b \to \infty} -\frac{1}{x} \bigg |_1^b = \lim_{b \to \infty} 1 - \frac{1}{b} = 1
{% end %}

### The p-integral test

For an improper integral of the function $x^{-p}$, there are three possible cases.

| Value of $p$ | Convergent integral | Divergent integral |
| ---- | ---- | ---- |
| $p > 1$ | $\displaystyle \int_a^\infty \frac{dx}{x^p}$ | $\displaystyle \int_0^a \frac{dx}{x^p}$ |
| $p < 1$ | $\displaystyle \int_0^a \frac{dx}{x^p}$ | $\displaystyle \int_a^\infty \frac{dx}{x^p}$ |
| $p = 1$ | None | All integrals diverge |


## Arc length

We will cover one last application of integration: finding the total length (called the _arc length_) of a curve. For a curve $y = f(x)$, an infinitesimal segment can be found by the Pythagorean theorem:

{% math() %}
ds^2 = dx^2 + dy^2
{% end %}

The right-hand side can be expressed purely in terms of $dx$ by factoring (here note that $dy^2 = (dy)(dy)$ and similarly for $dx$):

{% math() %}
ds^2 = dx^2 \left(1 + \frac{dy^2}{dx^2}\right)
{% end %}

Square rooting both sides, we have:

{% math() %}
ds = \sqrt{1 + \left(\frac{dy}{dx}\right)^2} dx
{% end %}

Now taking the integral of this infinitesimal arc length, we find the length $S$ of the complete curve:

{% math() %}
S = \int ds = \int_a^b \sqrt{1 + \left(\frac{dy}{dx}\right)^2} dx
{% end %}

### Finding the surface area of a surface of revolution from arc length

We may combine our technique for finding the arc length and the methods we used for finding volumes of solids of revolution to find their _surface areas_ instead. To start, we can write out the area of an infinitesimal portion of a rotationally-symmetric surface by:

{% math() %}
dA = 2\pi r ds
{% end %}

where $ds$ is the infinitesimal arc length, and $r = f(x)$. The complete surface area is given by:

{% math() %}
A = \int dA
{% end %}

Therefore, the surface area of a surface of revolution is given by:

{% math() %}
A = \int_a^b 2\pi r ds = \int_a^b 2\pi f(x) \sqrt{1 + \left(\frac{dy}{dx}\right)^2} dx
{% end %}