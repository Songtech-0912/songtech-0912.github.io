+++
title = "A Gentle Guide to Partial Differential Equations, Part III"
date = 2025-01-14
+++

In this section, we finish our exploration of PDEs, building on what we learned in the [first part](@/intro-pdes/index.md) and [second part](@/intro-pdes/chapter-2.md) of the guide to solve Laplace's equation and extend our knowledge of PDEs.

<!-- more -->

> ### Chapter guide for PDEs
> 
> - [Part 1](@/intro-pdes/index.md) covers basics of PDEs, solving 1st-order PDEs, and the physical phenomena modelled by PDEs.
> - [Part 2](@/intro-pdes/chapter-2.md) covers classification and finding solutions to 2nd-order PDEs, and in particular, the diffusion equation, wave equation, and Laplace's equation.
> - [Part 3](@/intro-pdes/chapter-3.md) concludes this guide with a discussion on Laplace's equations and a few other topics in partial differential equations. **You are reading this part right now.**

## Laplace's equation and harmonic functions

Laplace's equation $\nabla^2 f = 0$ is one of the most fundamental PDEs in mathematical physics. It describes everything from the gravitational attraction of masses in classical mechanics, to the electric potential in electromagnetic theory, to the shape of a thin film, to the distribution of heat for an object in equilibrium, to irrotational flows of gases for aircraft wing design. Naturally, solving the Laplace equation is extremely crucial to many, many different fields. We will therefore devote this entire section to studying the Laplace equation.

### Properties of harmonic functions

From naive inspection of Laplace's equation, one may _think_ that $\nabla^2 f = 0$ _implies_ $f = 0$. This is an **incorrect assumption**, because while in many cases, the trivial solution $f = 0$ is _a possible solution_, there exist **non-trivial solutions** that also satisfy Laplace's equation. Notably, all functions of the form $f(r) = \pm\dfrac{k}{r}$ for some constant $k$ satisfy Laplace's equation, which has very important consequences in physics, although solutions in this form are **definitely not the only type** of solutions. In mathematical terminology, all solutions to Laplace's equation are formally known as **harmonic functions**, and other than sharing a few general features (such as time independence and generally being expressible as an infinite series of some sort) they are quite different.

But those shared general features are quite significant. For instance in complex analysis, the **Cauchy-Riemann theorem** says that for any analytic complex-valued function $f(z) = u + i v$ (analytic means that it can be expressed as a power series), the functions $u = u(x, y)$ and $v=v(x, y)$ satisfy:

{% math() %}
\begin{align*}
\dfrac{\partial u}{\partial x} = \dfrac{\partial v}{\partial y} \\
\dfrac{\partial u}{\partial y} = -\dfrac{\partial v}{\partial x}
\end{align*}
{% end %}

And $u$ and $v$ respectively both satisfy Laplace's equation:

{% math() %}
\nabla^2 u = 0, \quad \nabla^2 v=0
{% end %}

Furthermore, harmonic functions are **unique** - for well-posed boundary-value problems, Laplace's equation yields **one and only one solution**. It is one of the rare cases where we can **prove** that a PDE's solutions are _guaranteed_ to be unique - finding [a similar proof for the Navier-Stokes PDEs](https://www.claymath.org/millennium/navier-stokes-equation/) will give you $1 million dollars!

Finally, harmonic functions satisfy a **maximum principle** and a **minimum principle**. We won't prove either here; we will just state the results:

> **The maximum principle for Laplace's equation:** A solution $u$ to Laplace's equation on a domain $D$ attains its maximum value (if one exists) on the **boundary** of $D$.

> **The minimum principle for Laplace's equation:** A solution $u$ to Laplace's equation on a domain $D$ also attains its minimum value (if one exists) on the **boundary** of $D$.

### The Laplace operator in Cartesian coordinates

Like any linear partial differential equation, the Laplace equation can be written in terms of a _linear operator_ $\mathcal{L}$ such that $\mathcal{L} f = 0$. In our case, the linear operator for the Laplace equation is the **Laplacian**, also called the Laplace operator, written as $\nabla^2$ (it is also common to use the symbol $\Delta$). In two dimensions, it takes the form:

{% math() %}
\nabla^2_\text{(2D)} = \dfrac{\partial^2}{\partial x^2} + \dfrac{\partial^2}{\partial y^2}
{% end %}

Meanwhile, in three dimensions, it takes the form:

{% math() %}
\nabla^2_\text{(3D)} = \dfrac{\partial^2}{\partial x^2} + \dfrac{\partial^2}{\partial y^2} + \dfrac{\partial^2}{\partial z^2}
{% end %}

> **Note:** it is very important to note that the Laplace operator only contains spatial derivatives, meaning that Laplace equation is **time-independent**, unlike the wave equation and heat equation (which are time-dependent PDEs). This is why Laplace's equation is often used for describing **steady-state systems** where the system has settled to an equilibrium state and no longer changes with time.

### 2D Laplace operator in polar coordinates

We now derive the 2D Laplace operator (Laplacian) in two dimensions in polar coordinates. Recall that using $x = r\cos \theta, y = r\sin \theta$, where we have $r = \sqrt{x^2 + y^2}$ and $\theta = \tan^{-1}(y/x)$. Thus, we can rewrite the  

{% math() %}
\begin{align*}
\dfrac{\partial}{\partial x} &= \dfrac{\partial r}{\partial x} \dfrac{\partial}{\partial r} + \dfrac{\partial \theta}{\partial x} \dfrac{\partial}{\partial \theta} \\
&= \cos \theta \dfrac{\partial}{\partial r} - \dfrac{\sin \theta}{r} \dfrac{\partial}{\partial \theta} \\
\dfrac{\partial}{\partial y} &= \dfrac{\partial r}{\partial y} \dfrac{\partial}{\partial r} + \dfrac{\partial \theta}{\partial y} \dfrac{\partial}{\partial \theta} \\
&= \sin \theta \dfrac{\partial}{\partial r} + \dfrac{\cos \theta}{r} \dfrac{\partial}{\partial \theta}
\end{align*}
{% end %}

Thus, substituting these formulas for the partial derivatives into the Laplacian operator, we have:

{% math() %}
\begin{align*}
\nabla^2_\text{(2D)} &= \dfrac{\partial^2}{\partial x^2} + \dfrac{\partial^2}{\partial y^2} \\
&= \dfrac{\partial}{\partial x} \left(\dfrac{\partial}{\partial x}\right) + \dfrac{\partial}{\partial y}\left(\dfrac{\partial}{\partial y}\right) \\
\end{align*}
{% end %}

We'll calculate the two second partial derivatives one by one. For the 2nd partial derivative in $x$ we have: 

{% math() %}
\begin{align*}
\dfrac{\partial}{\partial x} \left(\dfrac{\partial}{\partial x}\right) &= \cos^{2}\theta\frac{\partial^{2}}{\partial r^{2}}-2\left(\frac{\sin\theta\cos\theta}{r}\right)\frac{\partial^{2}}{\partial r\partial\theta} \\
 & \qquad +\frac{\sin^{2}\theta}{r^{2}}\frac{\partial^{2}}{\partial\theta^{2}}+\frac{2\sin\theta\cos\theta}{r^{2}}\frac{\partial}{\partial\theta}+\frac{\sin^{2}\theta}{r}\frac{\partial}{\partial r}
\end{align*}
{% end %}

Meanwhile, for the 2nd partial derivative in $y$ we have:

{% math() %}
\begin{align*}
\dfrac{\partial}{\partial y} \left(\dfrac{\partial}{\partial y}\right) &= \sin^{2}\theta\frac{\partial^{2}}{\partial r^{2}}+2\left(\frac{\sin\theta\cos\theta}{r}\right)\frac{\partial^{2}}{\partial r\partial\theta} \\
 & \qquad+\frac{\cos^2\theta}{r^2}\frac{\partial^2}{\partial\theta^2}-\frac{2\sin\theta\cos\theta}{r^2}\frac{\partial}{\partial\theta}+\frac{\cos^2\theta}{r}\frac{\partial}{\partial r}
\end{align*}
{% end %}

Putting it all together, we have:

{% math() %}
\begin{align*}
\nabla^2_\text{(2D)} &= \dfrac{\partial}{\partial x} \left(\dfrac{\partial}{\partial x}\right) + \dfrac{\partial}{\partial y}\left(\dfrac{\partial}{\partial y}\right) \\
&= \cos^{2}\theta\frac{\partial^{2}}{\partial r^{2}}
-\cancel{2\left(\frac{\sin\theta\cos\theta}{r}\right)\frac{\partial^{2}}{\partial r\partial\theta}} \\
 & \qquad +\frac{\sin^{2}\theta}{r^{2}}\frac{\partial^{2}}{\partial\theta^{2}}
 +\cancel{\frac{2\sin\theta\cos\theta}{r^{2}}\frac{\partial}{\partial\theta}}+\frac{\sin^{2}\theta}{r}\frac{\partial}{\partial r} \\
 & \qquad + \sin^{2}\theta\frac{\partial^{2}}{\partial r^{2}}
 +\cancel{2\left(\frac{\sin\theta\cos\theta}{r}\right)\frac{\partial^{2}}{\partial r\partial\theta}} \\
 & \qquad+\frac{\cos^2\theta}{r^2}\frac{\partial^2}{\partial\theta^2}
 -\cancel{\frac{2\sin\theta\cos\theta}{r^2}\frac{\partial}{\partial\theta}}
 +\frac{\cos^2\theta}{r}\frac{\partial}{\partial r} \\
 &= \cancel{(\sin^2 \theta + \cos^2 \theta)}^1 \dfrac{\partial^2}{\partial r^2}
 + \dfrac{\cancel{(\sin^2 \theta + \cos^2 \theta)}^1}{r} \dfrac{\partial}{\partial r}
 + \dfrac{\cancel{\sin^2 \theta + \cos^2 \theta}^1}{r^2} \dfrac{\partial^2}{\partial \theta^2} \\
 &= \dfrac{\partial^2}{\partial r^2} + \dfrac{1}{r} \dfrac{\partial}{\partial r} + \dfrac{1}{r^2} \dfrac{\partial^2}{\partial \theta^2}
\end{align*}
{% end %}

And thus we have derived the 2D Laplacian in polar coordinates:

{% math() %}
\nabla^2_\text{(2D)} = \dfrac{\partial^2}{\partial r^2} + \dfrac{1}{r} \dfrac{\partial}{\partial r} + \dfrac{1}{r^2} \dfrac{\partial^2}{\partial \theta^2}
{% end %}

Note that it is common to write the 2D polar Laplacian in a condensed form as:

{% math() %}
\nabla^2_\text{2D} = \dfrac{1}{r} \dfrac{\partial}{\partial r} \left(r \dfrac{\partial}{\partial r}\right) + \dfrac{1}{r^2} \dfrac{\partial^2}{\partial \theta^2}
{% end %}

### 3D Laplace operator in cylindrical coordinates

Let us now move forward to three dimensions. In 3D, the two most common non-Cartesian coordinates are **cylindrical coordinates** and **spherical coordinates**. We will examine the Laplace operator for both, but we'll start with cylindrical coordinates.

Thankfully, the expression of the Laplace operator in cylindrical coordinates is fairly straightforward to find. This is because cylindrical coordinates are essentially just polar coordinates extended to 3D; its coordinate conversions to Cartesian are simply $x = r \cos \theta, y = r \sin \theta, z = z$. Thus, we can express the Laplace operator in 3D as:

{% math() %}
\begin{align*}
\nabla^2_\text{(3D)} &= \dfrac{\partial^2}{\partial x^2} + \dfrac{\partial^2}{\partial y^2} + \dfrac{\partial^2}{\partial z^2} \\
&= \nabla^2_\text{2D} + \dfrac{\partial^2}{\partial z^2} \\
&= \dfrac{\partial^2}{\partial r^2} + \dfrac{1}{r} \dfrac{\partial}{\partial r} + \dfrac{1}{r^2} \dfrac{\partial^2}{\partial \theta^2} + \dfrac{\partial^2}{\partial z^2} \\ \\
&= \dfrac{1}{r} \dfrac{\partial}{\partial r} \left(r \dfrac{\partial}{\partial r}\right) + \dfrac{1}{r^2} \dfrac{\partial^2}{\partial \theta^2} + \dfrac{\partial^2}{\partial z^2}
\end{align*}
{% end %}

### 3D Laplace operator in spherical coordinates

As the last part in our _tour de force_, let us calculate the formidable Laplace operator in spherical coordinates. Or rather, let's not. Unfortunately, the mathematics are so long and complicated that we will just state the end result:

{% math() %}
\nabla^2_\text{(3D)} = {1 \over r^{2}}{\partial  \over \partial r}\!\left(r^{2}{\partial f \over \partial r}\right)\!+\!{1 \over r^{2}\!\sin \theta }{\partial  \over \partial \theta }\!\left(\sin \theta {\partial f \over \partial \theta }\right)\!+\!{1 \over r^{2}\!\sin ^{2}\theta }{\partial ^{2}f \over \partial \varphi ^{2}}
{% end %}

> **Note:** Here, we use $(r, \theta, \phi)$ as our coordinates, where $\theta \in [0, \pi]$ and $\phi \in [0, 2\pi]$, which is predominantly used in physics and engineering. However, take caution, because (especially in mathematics literature) it is common to switch $\theta, \phi \to \phi, \theta$, and for $r$ to be denoted $\rho$.

## Finding solutions to Laplace's equation

The Laplace equation is very nice in the sense that it is **separable** in Cartesian, polar, cylindrical, and spherical coordinates - very unusual among PDEs! This gives us a lot of flexibility in which coordinate system to use in solving a problem, and assures us that an exact solution can (nearly) always be found for (simple) boundary conditions. Furthermore, solutions to Laplace's equation are _pure_ boundary-value problems, since Laplace's equation is purely spatial, and thus no initial conditions are necessary. So let's dive in!

### Solving Laplace's equation in 2D and 3D Cartesian coordinates

To start, let us solve the following boundary-value problem for the 2D Laplace equation in Cartesian coordinates:

{% math() %}
\begin{gather*}
\dfrac{\partial^2 u}{\partial x^2} + \dfrac{\partial^2 u}{\partial y^2} = 0, \\
u(x, 0) = F(x), \, F(0) = F(\pi) = 0 \\
u(0, y) = u(\pi, y) = 0, \\
0 \leq x \leq \pi, 0 \leq y \leq \pi
\end{gather*}
{% end %}

> **Note:** $F(x)$ is a generic function that represents **any** function for which $F(x) = 0$ at $x = 0$ and $x = \pi$ (this condition is needed for the boundary conditions to be consistent). For instance, $F(x) = \sin x$ would be a valid choice, since sine is zero at $x = 0$ and $x = \pi$. In fact, so would $F(x) = \sin(2x), \sin(3), \dots, \sin (nx)$, and even $F(x) = -\left(x-\frac{\pi}{2}\right)^{2}+\frac{\pi^{2}}{4}$ would be possible choices for $F(x)$.

We use the standard separation of variables procedure, in which we let $u(x, y) = X(x) Y(y)$. This allows us to find that $\dfrac{\partial^2 u}{\partial x^2} = X''Y$ and $\dfrac{\partial^2 u}{\partial y^2} = XY''$. By substitution we then have:

{% math() %}
X''Y + XY'' = 0
{% end %}

Dividing by $XY$ on both sides, we have:

{% math() %}
\dfrac{X''}{X} + \dfrac{Y''}{Y} = 0 \Rightarrow \dfrac{X''}{X} =- \dfrac{Y''}{Y}
{% end %}

As with what we have seen before, since the derivatives are equal, they must be equal to a constant; we arbitrarily choose a separation constant $-\beta^2$. This leads to the system of ODEs:

{% math() %}
\begin{align*}
X'' = -\beta^2 X, \quad Y'' = \beta^2 Y
\end{align*}
{% end %}

Which have the general solutions:

{% math() %}
\begin{align*}
X(x) &= A \sin \beta x + B \cos \beta x, \\
Y(y) &= C e^{\beta y} + D e^{-\beta y}
\end{align*}
{% end %}

From which we can write down the solution $u(x, y)$, as follows:

{% math() %}
\begin{align*}
u(x, y) &= X(x)Y(y) \\
&= (A \sin \beta x + B \cos \beta x)(C e^{\beta y} + D e^{-\beta y})
\end{align*}
{% end %}
We can then substitute in our boundary conditions $u(0, y) = u(\pi, y) = 0$ to find the particular solution for the boundary-value problem. Substituting for $x = 0$, we have:

{% math() %}
\begin{align*}
u(0, y) &= B (Ce^{\beta y} + De^{-\beta y}) = 0 \\
&\Rightarrow B = 0 \\
u(\pi, y) &= A \sin(\pi \beta) (Ce^{\beta y} + De^{-\beta y}) = 0 \\
&\Rightarrow A \sin(\pi \beta) = 0 \\
&\Rightarrow \beta = n
\end{align*}
{% end %}

Substituting these results simplifies our solution to:

{% math() %}
u(x, y) = A \sin (nx) (C e^{n y} + D e^{-n y})
{% end %}

Now we will substitute the second boundary condition, $u(x, 0) = F(x)$, where $F(0) = F(\pi) = 0$. This is a more challenging boundary condition, as we don't know the exact form of $F(x)$, which immediately hints that we would need to express the solution as a series expansion. But since we _do_ know that $F(0) = F(\pi) = 0$, then we _at least_ know that $u(0, 0) = u(0, \pi) = 0$. Substituting these results, we have:

{% math() %}
\begin{align*}
u(0, 0) &= A \sin (0) (C e^{n y} + D e^{-n y}) = 0 \\
u(0, \pi) &= A \sin (n\pi) (C e^{n y} + D e^{-n y}) = 0
\end{align*}
{% end %}

So our solution is consistent with the second boundary conditions at the boundaries $x = 0$ and $x = \pi$. Since we have two exponentials, however, we have two undetermined constants $C, D$. But given that they are arbitrary, we can absorb them into $A$. This is especially convenient to write the solution in terms of the hyperbolic sine function $\sinh(x) = (e^x - e^{-x})/2$, for which we have:

{% math() %}
u(x, y) = A \sin (nx) \sinh(ny)
{% end %}

But we still need to satisfy $u(x, 0) = F(x)$. Thus the most general form of this solution would be a **series solution**, so we have:

{% math() %}
u(x, y) = \sum_{n = 1}^\infty A_n \sin (nx) \sinh(ny)
{% end %}

Where the coefficients $A_n$ would be given by:

{% math() %}
F(x) = \dfrac{2}{\pi} \int_0^\pi F(x) \sin (nx)
{% end %}

Which we have plotted below:

{{ natural_img(
src="../laplace-2d-solution.svg"
desc="A surface plot of the solution to Laplace's equation for our boundary-value problem"
) }}

We can also sketch out the solution procedure for a three-dimensional boundary-value problem. For instance, consider solving Laplace's equation on a 3D cube with each side having a length of $\pi$. Then Laplace's equation reads:

{% math() %}
\begin{gather*}
\dfrac{\partial^2 u}{\partial x^2} + \dfrac{\partial^2 u}{\partial y^2} + \dfrac{\partial^2 u}{\partial z^2} = 0, \\
x \in [0, \pi], y \in [0, \pi], z \in [0, \pi]
\end{gather*}
{% end %}

We use the typical trick for solving Laplace's equation by assuming a solution in the form $u(x, y, z) = X(x)Y(y)Z(z)$. Thus, taking the partial derivatives with respect to $x, y, z$, we have:

{% math() %}
X'' YZ + XY'' Z + XYZ'' = 0
{% end %}

Dividing all three terms by $XYZ$, we find our first separation constant, which we name $\alpha^2$:

{% math() %}
\begin{align*}
\dfrac{X''}{X} + \dfrac{Y''}{Y} + \dfrac{Z''}{Z} = 0 \\
\dfrac{X''}{X} + \dfrac{Y''}{Y} = - \dfrac{Z''}{Z} = \pm\alpha^2 \\
\end{align*}
{% end %}

Where we choose the sign of $\alpha^2$ based on whichever sign allows us to satisfy the given problem's boundary conditions (hint: if you have $u = 0$ at the boundaries $z = [0, \pi]$, you'd almost always want $\alpha^2$). From here, we can further simplify, to get our second separation constant, which we name $\beta^2$:

{% math() %}
\begin{align*}
\dfrac{X''}{X} + \dfrac{Y''}{Y} = \pm\alpha^2 \\
\dfrac{X''}{X} =- \dfrac{Y''}{Y} \pm \alpha^2 = \pm \beta^2
\end{align*}
{% end %}

This gives us a system of three ODEs, in total:

{% math() %}
\begin{align*}
X'' = \pm \beta^2 X \\
Y'' \mp \alpha^2 Y = \mp \beta^2 Y \\
Z'' = \mp \alpha^2 Z
\end{align*}
{% end %}

Which we can solve for given boundary conditions (we will not set specific boundary conditions to solve for here, to avoid making this section overly-long). The same techniques can be used to solve for more complex boundary conditions, including Neumann, Robin, and periodic boundary conditions.

Note that while solving in Cartesian coordinates is appropriate for a wide range of problems, especially those that have boundary conditions along a straight line or flat plate, we do not always want to use Cartesian coordinates. For problems that involve other geometries, such as those problems that have radial, cylindrical, or spherical symmetry, it is more useful to solve Laplace's equation in different coordinate systems. This will be what we'll be going through next.

### Solving Laplace's equation in polar coordinates

We will now proceed to solving in **polar coordinates** - a slightly more challenging task. The solutions to Laplace's equation in polar coordinates is useful in many areas of physics and engineering: for instance, to describe the electric potential on a charged disc, the shape of a thin film (e.g. soap bubble), or the vibrations of a circular drum. Consider the boundary-value problem for Laplace's equation in the domain $\,\{r \in [0, a], \theta \in [0, 2\pi]\,\}$ given by:

{% math() %}
\begin{gather*}
\nabla^2_\text{(polar)} = 0, \\
u(r, \theta) = u(r + 2\pi, \theta) \\
u(a, \theta) = h(\theta), \\
r \in [0, a], \theta \in [0, 2\pi]
\end{gather*}
{% end %}

Recall that the Laplacian (Laplace operator) in polar coordinates takes the form:

{% math() %}
\nabla^2 = \dfrac{1}{r} \dfrac{\partial}{\partial r} \left(r \dfrac{\partial}{\partial r}\right) + \dfrac{1}{r^2} \dfrac{\partial^2}{\partial \theta^2}
{% end %}

Thus, Laplace's equation in polar coordinates becomes:

{% math() %}
\left[\dfrac{1}{r} \dfrac{\partial}{\partial r} \left(r \dfrac{\partial}{\partial r}\right) + \dfrac{1}{r^2} \dfrac{\partial^2}{\partial \theta^2}\right]u(r, \theta) = 0
{% end %}

We can then do separation of variables by assuming a solution in the form $u(r, \theta) = F(r) G(\theta)$. If we then take the derivatives of $u$ and plug them into Laplace's equation (the steps aren't shown here, but it is fairly straightforward, just tedious math) we have:

{% math() %}
F'' G + \dfrac{1}{r} F'G + \dfrac{1}{r^2} FG'' = 0
{% end %}

Now, if we multiply the whole expression by $\dfrac{r^2}{FG}$, we get:

{% math() %}
\begin{align*}
\dfrac{r^2 F''}{F}  + \dfrac{rF'}{F} + \dfrac{G''}{G} = 0 \\
\Rightarrow \dfrac{r^2 F''}{F}  + \dfrac{rF'}{F} = -\dfrac{G''}{G} = n^2
\end{align*}
{% end %}

Where $n^2$ is our chosen separation constant (we will later see that a positive choice of separation constant is necessary for a solution consistent with our boundary conditions in polar coordinates). This leads us to the following set of ODEs:

{% math() %}
\begin{align*}
r^2 F'' + rF' = n^2 F \\
G'' = -n^2 G 
\end{align*}
{% end %}

The ODE for $G(\theta)$ is fairly straightforward to solve. We already know how to solve ODEs of this sort - the general solution is:

{% math() %}
G(\theta) = A \sin n \theta + B \cos n \theta
{% end %}

However, the ODE for $F(r)$ is more complicated, because while it is still a linear ODE, it has _non-constant_ coefficients. This particular differential equation is actually called the **Euler differential equation**. If you don't know (or need a reminder) for how to solve it, see the relevant section on [the intro differential equations guide](@/differential equations/index.md#special-cases-of-linear-second-order-odes). Here, we will simply state the solution:

{% math() %}
F(r) = r^n + C + D \ln r
{% end %}

Thus, our general solution becomes:

{% math() %}
\begin{align*}
u(r, \theta) &= F(r) G(\theta) \\
&= (A \cos n \theta + B \sin n \theta)(r^n + C + D \ln r)
\end{align*}
{% end %}

Since our solution $u(r, \theta)$ is sinusoidal in $\theta$, it is automatically periodic and thus automatically satisfies $u(r, \theta) = r(\theta + 2\pi)$. We also want to make sure our solution is defined for all $r$, because otherwise $u(r, \theta)$ is defined at not differentiable over the whole domain, and thus would not satisfy Laplace's equation (we would say that the solution would be _unphysical_ in physics). We notice in our solution that as $r \to 0$, $D \ln (r) \to -\infty$, so the solution diverges and becomes non-differentiable at $r = 0$. The only way we can avoid this if we set $D = 0$. We can then absorb the constant $C$ into the rest of the constants $A, B$, so our solution becomes:

{% math() %}
u(r, \theta) = r^n (A \cos n \theta + B \sin n \theta)
{% end %}

We can write this as a _series solution_ with a Fourier series as:

{% math() %}
\begin{align*}
u(r, \theta) &= \sum_{n = 0}^\infty r^n(A_n \cos n \theta + B_n \sin n \theta) \\
&= \dfrac{A_0}{2} + \sum_{n = 1}^\infty r^n(A_n \cos n \theta + B_n \sin n \theta)
\end{align*}
{% end %}

(the $A_0/2$ term is because we switch to summing from $n = 1$ rather than $n = 0$). We can then find the coefficients $A_n, B_n$ by exploiting orthogonality, as before, and substituting our boundary condition $u(a, \theta)$. Thus we find that:

{% math() %}
\begin{align*}
A_n &= \dfrac{1}{\pi} a^{-n} \int_0^{2\pi} h(\theta) \cos n \theta\, d \theta \\
B_n &= \dfrac{1}{\pi} a^{-n} \int_0^{2\pi} h(\theta) \sin n \theta\, d\theta
\end{align*}
{% end %}

### Solving Laplace's equation in cylindrical coordinates

The method of solving Laplace's equation in **cylindrical coordinates** is a generalization of the solution in polar coordinates. This is because Laplace's equation in cylindrical coordinates is essentially the same as its form in polar coordinates, plus a second partial derivative in $z$:

{% math() %}
\nabla^2_\text{(cylindrical)}u(r, \theta, z) = \nabla^2_\text{(polar)}u(r, \theta, z=0) + \dfrac{\partial^2 u}{\partial z^2} = 0
{% end %}

Using the separation of variables procedure, where $u(r, \theta, z) = F(r)G(\theta) Z(z)$, this gives us (after substituting the partial derivatives of $u$ back into Laplace's equation):

{% math() %}
F'' GZ + \dfrac{1}{r} F'GZ + \dfrac{1}{r^2} FG''Z + FGZ'' = 0
{% end %}

Now multiplying by $1/FGZ$ gives us:

{% math() %}
\begin{align*}
\dfrac{F''}{F}  + \dfrac{1}{r} \dfrac{F'}{F} + \dfrac{1}{r^2}\dfrac{G''}{G} + \dfrac{Z''
}{Z} = 0 \\
\Rightarrow \left(\dfrac{F''}{F}  + \dfrac{1}{r} \dfrac{F'}{F} + \dfrac{1}{r^2}\dfrac{G''}{G}\right) = -\dfrac{Z''
}{Z} = -k^2 \\
\Rightarrow \dfrac{F''}{F}  + \dfrac{1}{r} \dfrac{F'}{F} + \dfrac{1}{r^2}\dfrac{G''}{G} + k^2 = 0 \\
\Rightarrow r^2 \left[\dfrac{F''}{F}  + \dfrac{1}{r} \dfrac{F'}{F} + \dfrac{1}{r^2}\dfrac{G''}{G} + k^2\right] = 0 \\
r^2\dfrac{F''}{F} +r\dfrac{F'}{F} + \dfrac{G''}{G} + k^2 r^2 = 0 \\
\Rightarrow r^2\dfrac{F''}{F} +r\dfrac{F'}{F} - k^2 r^2 = -\dfrac{G''}{G} = n^2
\end{align*}
{% end %}

Where $-k^2, n^2$ are our separation constants. Therefore, we now have a system of three ODEs:

{% math() %}
\begin{gather*}
Z'' = k^2 Z \\
G'' = -n^2 \\
r^2F'' +rF' - (k^2 r^2 + n^2) = 0
\end{gather*}
{% end %}

The first two differential equations are fairly simply to solve:

{% math() %}
\begin{align*}
G(\theta) &= A \cos n\theta + B \sin n\theta \\
Z(z) &= C e^{k z} + D e^{-kz}
\end{align*}
{% end %}

By contrast, the third ODE, which is for $F(r)$, is absolutely **not easy** to solve. The solution can only be expressed in terms of [Bessel function](https://en.wikipedia.org/wiki/Bessel_functions), which are special transcendental functions, typically denoted $J_n(r)$. The solution for $F(r)$ is given by:

{% math() %}
F_n(r) = K_1 r^n + K_2 r^{-n} + K_3\ln(r) + K_4 J_n(kr)
{% end %}

Where we write $F(r)$ as $F_n(r)$ to capture the $n$ in the Bessel function, and $K_1, K_2, K_3, K_4$ are undetermined constant coefficients. The general solution is therefore:

{% math() %}
\begin{align*}
u(r, \theta, z) &= F_n(r) G(\theta) Z(z) \\
&= \bigg[K_1 r^n + K_2 r^{-n} + K_3\ln(r) + K_4 J_n(kr)\bigg](A \cos n\theta + B \sin n\theta)(C e^{k z} + D e^{-kz})
\end{align*}
{% end %}

Again, we may write the most general solution in terms of a series (although in this case, it would be a _generalized Fourier series_, not a traditional sinusoidal Fourier series). It is also convenient to express the $\theta$ part of the solution using complex exponentials (the Bessel functions have real-valued forms and complex-valued forms), giving us:

{% math() %}
\begin{align*}
u(r, \theta, z) &= \sum_{n = 1}^\infty F_n(r) G(\theta) Z(z) \\
&= \sum_{n = 1}^\infty \bigg[K_1 r^n + K_2 r^{-n} + K_3\ln(r) + K_4 J_n(kr)\bigg](A e^{i(n\theta)} + B e^{-i(n\theta)})(C e^{k z} + D e^{-kz})
\end{align*}
{% end %}

## Bonus: solving linear inhomogeneous PDEs

In our previous analysis, we focused almost exclusively on _homogeneous_ PDEs. We haven't examined **inhomogeneous PDEs**, such as **Poisson's equation**, the inhomogeneous version of Laplace's equation:

{% math() %}
\nabla^2 u = f(\mathbf{x})
{% end %}

Where $f(\mathbf{x}) = f(x, y, z)$. The way to solve such inhomogeneous PDEs is to first find the solution to the corresponding _homogeneous_ PDE. In the case of Poisson's equation, its corresponding homogeneous PDE is simply Laplace's equation $\nabla^2 u_h = 0$, where we denoted the solution as $u_h$ to remind us that it is the solution to the _homogeneous_ PDE. 

Then, we add the _particular solution_ to $\nabla^2 u_p = f(\mathbf{x})$, which is _a solution_ that satisfies the inhomogeneous PDE as well as the given boundary conditions. In many cases we can just guess a solution and _as long as_ it satisfies both the PDE (in this case, $\nabla^2 u_p = f(\mathbf{x})$) and the boundary conditions, it is a _valid_ particular solution.

Finally, combining the two together, the _general solution_ for $u(\mathbf{x})$ given a specific boundary-value problem is given by:

{% math() %}
u(x, t) = u_h(x, t) + u_p(x, t)
{% end %}

> **Note:** This procedure **only** works for **linear PDEs**. It **does not work** if the PDE is nonlinear. In fact, this is one of the reasons why nonlinear PDEs are so particularly hard to solve!

To recap, we use a 3-step process for finding a general solution to the boundary-value problem for an inhomogeneous PDE:

1. Identify the *homogeneous* version of the inhomogeneous PDE. For instance, for Poisson's equation $\nabla^2 u = f(\mathbf{x})$, its inhomogeneous version is $\nabla^2 u = 0$.
2. Find the general solution to the _homogeneous_ PDE with the given boundary conditions of the problem. In our example, we would solve $\nabla^2 u_h = 0$, which gives the solution $u_h(\mathbf{x})$ for the _homogeneous_ PDE.
3. Find a particular solution to the _inhomogeneous_ PDE (our original PDE) with the given boundary conditions of the problem. In our example, this means finding a particular solution $\nabla^2 u_p = f(\mathbf{x})$, which gives the solution $u_p(\mathbf{x})$ for the _inhomogeneous_ PDE.
	1. In many cases, we can just guess a solution, and as long we check that it satisfies the problem's boundary conditions, it is a perfectly suitable solution
4. Add the particular solution $u_p$ and the homogeneous general solution $u_h$ to get the _general solution_ $u(\mathbf{x}) = u_p + u_h$ for the boundary-value problem.

A similar process works for the case of inhomogeneous _boundary conditions_, where $u(\mathbf{x})$ (and/or its partial derivatives) _does not vanish_ at the boundaries. For instance, consider the 1D wave equation solved over $x \in [0, L], t \in [0, t_\text{end}]$, where we may have inhomogeneous Dirichlet boundary conditions $u(0, 0) = A$ and $u(L, 0) = B$, where $A, B$ are constants as well as an initial condition $u(x, 0) = \psi(x)$. To solve, we add the general solution for the PDE for the _homogeneous_ boundary conditions $u_h(0, 0) = u_h(L, 0) = 0$, and the particular solution for the _inhomogeneous_ boundary conditions $u_p(0, 0) = A, u_p(L, 0) = B$. The sum gives us the **general solution** $u(x, t) = u_h(x, t) + u_p(x, t)$ for the inhomogeneous boundary-value problem.

> **Note:** Be careful, because the **initial condition** for finding the **homogeneous general solution** may not be zero; rather, it is $u_p(x, 0) = \psi(x) - u_h(x, 0)$. So it is useful to **find the particular solution first**. Of course, this doesn't matter if our PDE is purely spatial (e.g. Poisson's equation), but for the heat equation with sources $\dfrac{\partial u}{\partial t} + \dfrac{\partial^2 u}{\partial x^2} + Q(x, t)$ we definitely want to find the particular solution first, and then solve the homogeneous general solution.

### Generalized series solutions to Laplace's equation

We saw previously that the particular solutions to Laplace's solution in Cartesian coordinates for a variety of boundary-value problems can be expressed in terms of Fourier series. We can generalize these particular solutions for a _more general_ Fourier series that describes _generalized_ boundary-value problems for the Laplace equation. We will find these generalized series solutions in both Cartesian and polar coordinates.

#### Generalized series solutions in 2D and 3D Cartesian coordinates

In 3D Cartesian coordinates, we may write out the generalized series solution, using a generalized set of basis functions $u_{mn}(\mathbf{r})$:

{% math() %}
\begin{align*}
u_{mn} &= A_{mn} \sinh(\sqrt{m^2 + n^2}x)\sin(my) \sin(nz) \\
u(x, y, z) &= \sum_{n = 1}^\infty \sum_{m = 1}^\infty u_{mn} \\
&= \sum_{n = 1}^\infty \sum_{m = 1}^\infty A_{mn} \sinh(\sqrt{m^2 + n^2}x)\sin(my) \sin(nz)
\end{align*}
{% end %}

> **Note:** for 2D Cartesian coordinates, simply reduce by one coordinate by removing the $\sin (nz)$ term, so that the solution only depends on $x$ and $y$.

Where we may find the $A_{mn}$ coefficients, as usual, by exploiting orthogonality. For instance, if we wanted to find the $A_{mn}$ coordintes for the boundary conditionb $u(\pi, y, z) = f(y, z)$, we would have:

{% math() %}
\begin{align*}
A_{mn} \int_0^\pi &\int_0^\pi \, u_{mn}(\pi, y, z) u_{mn}^*(\pi, y, z)\, dz\,dy \\
&= \int_0^\pi \int_0^\pi f(y, z) u_{mn}(\pi, y, z)\, dz\, dy
\end{align*}
{% end %}

For which we may be able to solve for $A_{mn}$ by computing the integral, since the functions $u_{mn}$ form a **complete basis** and are **orthogonal**. This method is general and suitable for not just one specific boundary-value problem, but a variety of boundary-value problems.

#### Generalized series solutions in polar coordinates

We can now do the same thing we did in Cartesian coordinates in _polar coordinates_ instead. In this case, the generalized solution is:

{% math() %}
u(r, \theta) = \dfrac{A_0}{2} + \sum_{n = 1}^\infty (A_n r^n + B_n r^{-n})(C_n \cos n \theta + D_n \sin n \theta)
{% end %}

Where, as a reminder, the coefficients are given by:

{% math() %}
\begin{align*}
C_n &= \dfrac{1}{\pi} a^{-n} \int_0^{2\pi} h(\theta) \cos n \theta\, d \theta \\
D_n &= \dfrac{1}{\pi} a^{-n} \int_0^{2\pi} h(\theta) \sin n \theta\, d\theta
\end{align*}
{% end %}

A special case for this solution is when we are solving Laplace's equation on the **inside of a circle** which has radius $a$, in which case the boundary conditions are defined by:

{% math() %}
\begin{gather*}
u(a, \theta) = h(\theta) \\
r \in [0, a],\ \theta \in [0, 2\pi]
\end{gather*}
{% end %}

Remarkably, in this case, the infinite series not only converges, but we can explicitly evaluate it - it becomes:

{% math() %}
u(r, \theta) = \dfrac{r^2 - a^2}{2\pi} \int_0^{2\pi} \dfrac{h(\phi) d\phi}{r^2 + a^2 - 2 a r \cos (\theta - \phi)} 
{% end %}

We _won't_ go over generalized solutions in cylindrical and spherical coordinates, as they are quite complicated. However, we may use similar methods to what we have already seen.

## Appendix: reference table of common linear PDEs

| Type of PDE                                             | General form                                                                                       | Solution method(s)                                                                                                        |
| ------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| Linear first-order PDE with single derivative           | $\small f(x, y) \frac{\partial u}{\partial x} + g(x, y) u = 0$                                           | Direct (partial) integration                                                                                              |
| Linear first-order constant-coefficient PDE             | $\small \alpha \frac{\partial u}{\partial x} + \beta \frac{\partial u}{\partial y} = 0$                 | Method of chacteristics, coordinate transformation (change of variables)                                                  |
| Linear first-order variable-coefficient PDE             | $\small \alpha(x, y) \frac{\partial u}{\partial x} + \beta(x, y) \frac{\partial u}{\partial y} = 0$     | Method of chacteristics, coordinate transformation (change of variables)                                                  |
| Linear constant-coefficient second-order parabolic PDE  | $\small \alpha \frac{\partial^2 u}{\partial x^2} + \dots = 0$                                            | Coordinate transform to diffusion equation (heat equation), separation of variables, express solution as series expansion |
| Linear constant-coefficient second-order hyperbolic PDE | $\small \alpha \frac{\partial^2 u}{\partial x^2} - \beta \frac{\partial^2 u}{\partial y^2} + \dots = 0$ | Coordinate transform to wave equation, separation of variables, express solution as series expansion                      |
| Linear constant-coefficient second-order elliptic PDE   | $\small \alpha \frac{\partial^2 u}{\partial x^2} + \beta \frac{\partial^2 u}{\partial y^2} + \dots = 0$ | Coordinate transform to Laplace's equation, separation of variables, express solution as series expansion                 |


## Concluding remarks

Congratulations, you've made it through the PDEs guide! But this is just a start to learning about PDEs. Many people dedicate their whole lives to the study of partial differential equations - and for good reason, because our understanding of the world depends on them. Some areas that this guide did not cover, but are significant areas of the study of PDEs, are the following:

- Numerical methods for PDEs, such as the finite difference and finite element method
- Nonlinear PDEs, which are very important in fluid mechanics and aerodynamics
- Further applications of partial differential equations in science and engineering
- Software for solving PDEs

If you're interested, please feel free to read more about those topics. And last but not least - I hope you enjoyed this guide, and that you gained something from it.