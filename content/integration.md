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

## Solids of revolution

Solids of revolution are obtained by the rotation of a region in the xy-plane about an axis. 

Note: Unlike many other areas of calculus, they are not very widely used in physics or applied math areas, but they are a good teaching/learning tool to practice integration.

### Disk method

Using the disk method of finding the volume of a solid of revolution, the solid of revolution created from the region underneath the curve $f(x)$ has the volume:

$$
V = \int_a^b \pi [f(x)]^2 dx
$$

And for a function $f(y)$, the volume is given by:

$$
V = \int_a^b \pi [f(y)]^2 dy
$$

For example, say we wanted to find the volume of a sphere. A sphere is simply the solid of revolution created by rotating the curve $f(x) = \sqrt{r^2 - x^2}$ about the x-axis. So, we would have:

$$
V = \pi \int_{-r}^r (\sqrt{r^2 - x^2})^2~dx
$$
Which becomes:

$$
V = \pi \int_{-r}^r r^2 - x^2 dx
$$
Since $r$ is a constant, the integral becomes:

$$
V = \frac{4}{3} \pi r^3
$$
Which is the volume of a sphere!

### Washer method

Using the washer method of finding the volume of a solid of revolution, the solid of revolution created by the region between two curves $f(x)$ and $g(x)$ is given by:

$$
V = \int_a^b \pi [f(x)]^2 - \pi [g(x)]^2 dx
$$
And similarly for $y$:

$$
V = \int_a^b \pi [f(y)]^2 - \pi [g(y)]^2 dy
$$

### Shells method

Using the shells method of finding the volume of a solid of revolution, the solid of revolution created by the region underneath the curve $f(x)$ is given by:

$$
V = \int_a^b 2\pi rf(x) dx
$$

And similarly for $y$:

$$
V = \int_a^b 2\pi rf(y) dy
$$
If the region is instead between two curves $f(x)$ and $g(x)$, then the volume is instead given by:

$$
V = \int_a^b 2\pi r[f(x) - g(x)] dx
$$

Or for $y$:

$$
V = \int_a^b 2\pi r[f(y) - g(y)] dy
$$

For instance, suppose we were to find the volume of the solid of revolution created by revolving the region bound by $f(x) = x^3, x \in [0, 2]$ and the x-axis about the line $x = 3$. A visualization of this region can be found at <https://www.desmos.com/calculator/ymuwqk1xk7>.

To compute the area, we'll first find the radii of the shells, and set that. In this case, the radius would be $3 - x$, as that is the distance from the rotational axis to the edge of the shell. The bounds of integration would be from 0 to 2, as we want to create shells that fill up the space of the region, and the region is bounded by $x = 0$ and $x = 2$. Therefore, the integral is:

$$
2\pi \int_0^2  (3 - x) x^3 dx = \frac{56\pi}{5}
$$

## Integration by Parts

**Integration by parts** is analagous to the product rule for derivatives. It is given by:

$$
\int udv = uv - \int vdu
$$

where:

$$
v = \int dv
$$

Typically, we want $u$ to be a function that has a simple derivative (such as a polynomial or $\ln x$), and $v$ to be a function that has a simple integral (such as $\cos x$ or $\sec^2 x$ or $e^x$). It's typically much harder to integrate than differentiate, so pick $dv$ first, and $u$ second.

In addition, integration by parts can be done multiple times over and over to repeatedly expand out an integral until it can be solved.

As an example of integration by parts, consider:

$$
\int x \cos (2x) dx
$$

Here, we want our $u$ to be $x$ (because that's easy to differentiate), and $dv = \cos 2x$. This means that $du = dx$. To find $v$, we simply do:

$$
v = \int dv = \int \cos (2x) = \frac{1}{2} \sin(2x)
$$

After substitution, we obtain:

$$
\int udv = \frac{1}{2}x \sin(2x) - \int \frac{1}{2} \sin(2x) dx
$$

Which evaluates to:

$$
\frac{1}{2} x \sin(2x) + \frac{1}{4} \cos(2x) + C
$$

For a faster method of integration by parts, we can use the tabular method, which works so long as $u$ is a polynomial. For instance, consider:

$$
\int x^3 e^x dx
$$

We construct a table of $u$ and all its derivatives on the left, and $dv$ and all its integrals (I) on the right, and alternating signs in front, until the derivative is zero:

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
| + | ... | ... |

In front of each derivative term we put the sign associated with it. Therefore, our result is:

$$
(+) x^3 e^x (-) 3x^2 e^x (+)6x e^x (-) 6e^x + C
$$

Or simplified:

$$
x^3 e^x - 3x^2 e^x + 6xe^x - 6e^x + C
$$

A third type of integration-by-parts integrals utilize a specialized technique. Consider:

$$
\int e^x \cos x dx
$$
Doing a first integration by parts with $u = e^x$ and $dv = \cos x$, we get:

$$
\int e^x \cos x dx = e^x \sin x - \int e^x \sin x dx
$$
Now repeating the integration by parts on the second integral with $u = e^x$ and $dv = \sin x$, we get:

$$
\int e^x \cos x dx = e^x \sin x - \left(-e^x \cos x - \int(-e^x\cos x dx)\right)
$$

Or simplifying:

$$
\int e^x \cos x dx = e^x \sin x + e^x \cos x - \int e^x \cos x dx
$$
Notice how the integral appears twice in the expression. If we say that:

$$
I = \int e^x \cos x dx
$$
We can rewrite the integral as:

$$
I = e^x \sin x + e^x \cos x- I
$$

Solving for $I$, we get:

$$
I = \frac{e^x \sin x + e^x \cos x}{2} + C
$$
which is the solution to the integral.

## Trigonometric integrals

Trigonometric integrals are integrals that involve combination of trigonometric functions.

The first general category of trigonometric integrals are in the form:

$$
\int \sin^m x \cos^n x dx
$$

There are several common approaches for such integrals:

- If $m$ is odd ($n = 2k + 1$), rewrite $\sin^m x = (\sin^2 x)^k \sin x = (1 - \cos^2 x)^k \sin x$, then use u-substitution
- If $n$ is odd ($n = 2k + 1$), rewrite $\cos^n x = (\cos^2 x)^k \cos x = (1 - \sin^2 x)^k \cos x$, then use u-substitution
- If both $m$ and $n$ are even, use the half-angle identities:

$$
\sin^2x = \frac{1 - \cos 2x}{2}
$$

$$
\cos^2 x = \frac{1 + \cos 2x}{2}
$$

$$
\sin x \cos x = \frac{\sin 2x}{2}
$$

Meanwhile, for trigonometric integrals in the general form:

$$
\int \tan^m x \sec^n x dx
$$

- If $n$ is even ($n = 2k, k \geq 2$), rewrite $\sec^n x = (\sec^2 x)^{k - 1} \sec^2 x = (\tan^2 x + 1)^{k - 1} \sec^2 x$, then use u-substitution with $u = \tan x$
- If $m$ is odd ($m = 2k + 1$), rewrite $\tan^m x = (\tan^2 x)^k \tan x = (\sec^2 x - 1)^k \tan x$, then use u-substitution with $u = \sec x$

For instance, consider:

$$
\int \sin^5 x \cos^4 x dx
$$

We can break this into:

$$
\int \sin^4 x \sin x \cos^4 xdx
$$

Which we can simplify into:

$$
\int (\sin^2 x)^2 \sin x \cos^4 x dx
$$

And again, into:

$$
\int (1 - \cos^2 x)^2 \sin x \cos^4 x dx
$$

Now, we can use $u = \cos x$, thus the integral becomes:

$$
-\int (1 - u^2)^2 u^4 du
$$

Or expanded and with the negative sign distributed:

$$
\int 2u^6 - u^4 - u^8 du
$$

This becomes:

$$
\frac{2u^7}{7} - \frac{u^5}{5} - \frac{u^9}{9} + C
$$

And substituting back, we have:

$$
\frac{2 \cos^7 x}{7} - \frac{\cos^5 x}{5} - \frac{\cos^9 x}{9} + C
$$

## Trigonometric substitutions

For integrals in the form:

$$
\int (a^2 \pm x^{2n})^m dx
$$

or generally, any integrals that have $\sqrt{a^2 - u^2}$, $\sqrt{a^2 + u^2}$, or $a^2 + u^2$, a trigonometric substitution is often helpful.

The substitutions make use of the 3 Pythagorean identities:

$$
\begin{cases}
\sin^2 \theta + \cos^2 \theta = 1 \\\\
1 + \tan^2 \theta = \sec^2 \theta \\\\
1 + \cot^2 \theta = \csc^2 \theta
\end{cases}
$$

Performing a trigonometric substitution involves fitting an integrand into one of these forms. For instance, consider the integral:

$$
\int \frac{\sqrt{4 - x^2}}{x^2} dx
$$

Here, we see the square root, which suggests the use of a trigonometric substitution. We first simplify the integral with:

$$
\int \frac{\sqrt{4(1 - \frac{x^2}{4})}}{x^2} dx
$$

We now have an expression in the form $1 - u^2$. It makes sense to use the first Pythagorean identity. We say that:

$$
\frac{x^2}{4} = \sin^2 \theta
$$

Which means:

$$
1 - \frac{x^2}{4} = 1 - \sin^2 \theta = \cos^2 \theta
$$

If we solve for $x$, we get:

$$
x = 2\sin \theta
$$

So:

$$
dx = 2\cos \theta d\theta
$$

Plugging in $1 - \frac{x^2}{4} = \cos^2 \theta$ and $dx = 2\cos \theta d\theta$ into the integral, we get:

$$
\int \frac{\sqrt{4\cos^2 \theta}}{4\sin^2 \theta} 2 \cos \theta d\theta
$$

Which simplifies to:

$$
\int \cot^2 \theta d\theta
$$

We use the identity $\cot^2 \theta + 1 = \csc^2 \theta$ to get:

$$
\int \csc^2\theta - 1 d\theta
$$

Whose solution is:

$$
-\cot \theta - \theta + C
$$

We now need to convert the answer in terms of $\theta$ back into an answer in terms of $x$. To do so, remember that:

$$
x = 2 \sin \theta
$$

Therefore:

$$
\sin \theta = \frac{x}{2} = \frac{\text{Opposite}}{\text{Hypotenuse}}
$$

We also know that:

$$
\cot \theta = \frac{1}{\tan \theta} = \frac{\text{Adjacent}}{\text{Opposite}}
$$

And by Pythagoras:

$$
\text{Adjacent}^2 = \text{Hypotenuse}^2 - \text{Opposite}^2 = 2^2 - x^2 = 4 - x^2
$$

So:

$$
\text{Adjacent} = \sqrt{4 - x^2}
$$

And:

$$
\cot \theta = \frac{\sqrt{4 - x^2}}{x}
$$

$$
\theta = \operatorname{arcsin} \left(\frac{x}{2}\right)
$$

We can now rewrite the solution in terms of $x$:

$$
-\frac{\sqrt{4 - x^2}}{x} - \operatorname{arcsin} \left(\frac{x}{2}\right) + C
$$

Similarly, we can solve the following integral by trigonometric substitution:

$$
\int \frac{dt}{(9t^2 + 4)^2}
$$

We first factor:

$$
\int \frac{dt}{(4(\frac{9}{4}t^2 + 1))^2}
$$

We set:

$$
1 + \frac{9}{4} t^2 = \sec^2 \theta
$$

$$
\frac{9}{4} t^2 = \tan^2 \theta
$$

Therefore:

$$
t = \frac{2}{3} \tan \theta
$$

$$
dt = \frac{2}{3} \sec^2 \theta d \theta
$$

Subtituting, we get:

$$
\frac{2}{3} \int \frac{dt}{(4\sec^2 \theta)^2)} \sec^2 \theta d \theta
$$

Which becomes:

$$
\frac{1}{48} \int \cos^2 \theta d \theta
$$

Trigonometric substitutions are incredibly easy to mess up, so be careful with them, and make sure to avoid these errors:
- Not cancelling out the powers correctly
- Using the incorrect trigonometric identity
- Calculating the incorrect differential
- Forgetting to carry over constants
- Simplification errors in the trigonometric integrand
- Errors in converting the solution in $\theta$ back to a solution in $x$, often due to forgetting a square root or a square when using Pythagoras
