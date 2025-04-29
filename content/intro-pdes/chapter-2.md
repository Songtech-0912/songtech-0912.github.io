+++
title = "A Gentle Guide to Partial Differential Equations, Part II"
date = 2025-01-14
+++

In this section, we continue our exploration of PDEs from the [first part of the guide](@/intro-pdes/index.md) and explore more complex PDEs and the ways to solve them.

<!-- more -->

> ### Chapter guide for PDEs
> 
> - [Part 1](@/intro-pdes/index.md) covers basics of PDEs, solving 1st-order PDEs, and the physical phenomena modelled by PDEs.
> - [Part 2](@/intro-pdes/chapter-2.md) covers classification and finding solutions to 2nd-order PDEs, and in particular, the diffusion equation, wave equation, and Laplace's equation. **You are reading this part right now.**
> - [Part 3](@/intro-pdes/chapter-3.md) concludes this guide with a discussion on Laplace's equations and a few other topics in partial differential equations.

## Initial and boundary-value problems

We have discussed previously that knowledge of only the PDE is _insufficient_ to provide a unique solution to a given physical problem. Thus, while we may have derived (or at least know) a particular PDE, we can only write down a unique solution when we are provided with **initial** and **boundary conditions**.

Let us take the example of the wave equation. Recall that the wave equation can be factored into two transport equations:

{% math() %}
\left(\dfrac{\partial^2}{\partial t^2} - c^2\dfrac{\partial^2}{\partial x^2}\right) u = \left(\dfrac{\partial}{\partial t} + c\dfrac{\partial}{\partial x}\right)\left(\dfrac{\partial}{\partial t} - c\dfrac{\partial}{\partial x}\right) u = 0
{% end %}

This means that for a solution to be found, we must provide initial and boundary conditions by specifying the values of both the function $u(x, t)$ and its derivatives at specific points along our area of interest. The possible types of initial and boundary conditions for a generalized quantity $u(\mathbf{r}, t)$ described by a PDE are as follows:

| Initial/Boundary condition   | Mathematical form                                                                                | Physical description                                                                                                                                                                                                                           | Example                                                                                                                                                                                                           |
| ---------------------------- | ------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Initial condition            | $u(\mathbf{r}, 0) = f(\mathbf{r})$                                                               | The quantity $u(\mathbf{r}, t)$ takes the value $f(\mathbf{r})$ at $t = 0$                                                                                                                                                                     | Initial heat distribution before heat flow for heat equation                                                                                                                                                      |
| Dirichlet boundary condition | $u(\mathbf{r}, t) \bigg\|_{\partial \Omega} = f(\mathbf{r})$                                     | The quantity $u(\mathbf{r}, t)$ takes a specified value at the boundaries of the area of interest                                                                                                                                              | The initial height of a vibrating membrame for Laplace's equation of a vibrating membrane                                                                                                                         |
| Neumann boundary condition   | $\dfrac{\partial u}{\partial n}(\mathbf{r}, t) \bigg\|_{\partial \Omega} = f(\mathbf{r})$        | The derivative of the quantity $u(\mathbf{r}, t)$ takes a specified value at the boundaries of the area of interest (note: $\mathbf{n}$ is the normal vector of the boundary and $\dfrac{\partial u}{\partial n} = \mathbf{n} \cdot \nabla u$) | The rate of heat spreading away from the edges of a hot object. When $\dfrac{\partial u}{\partial x} \big\|_{\partial \Omega} = 0$, the object is _perfectly insulative_, meaning no heat escapes from the object |
| Robin boundary condition     | $a\dfrac{\partial u}{\partial n} + b u(\mathbf{r}, t) \bigg\|_{\partial \Omega} = f(\mathbf{r})$ | A linear combination of the quantity $u(\mathbf{r}, t)$ and its derivative  takes a specified value at the boundaries of the area of interest                                                                                                  | A linear relation between the spread gas across the boundary and the gas density at that boundary.                                                                                                                |
| Periodic boundary condition  | $u(\mathbf{r}, t) = u(\mathbf{r} + \mathbf{b}, t)$                                               | The quantity $u(\mathbf{r}, t)$ repeats such that its vaulue at two points is the same                                                                                                                                                         | The height of a sinusoidal wave at two locations (periodic boundary conditions are often used for oscillating or wave-like phenomena)                                                                             |
| Vanishing boundary condition | $\displaystyle \lim_{\mathbf{r} \to \infty} u(\mathbf{r}, t) = 0$                                | The quantity $u(\mathbf{r}, t)$ vanishes at infinity (often used for quantities where the total amount is finite)                                                                                                                              | Normalization condition of Schrödinger's equation (which demands that $u \to 0$ as $\mathbf{r} \to 0$)                                                                                                            |

For instance, suppose our area of interest is a linear region between endpoints $x_1, x_2$, and we want to solve the wave equation. We would then want to specify the **initial condition** $u(x, 0)$, the boundary conditions $u(x_1, t)$ and $u(x_2, t)$, which are **Dirichlet boundary conditions**, as well as {% inlmath() %}\frac{\partial u(x, 0)}{\partial x} \big|_{x = x_1}{% end %} and {% inlmath() %}\frac{\partial u(x, 0)}{\partial x} \big|_{x = x_2}{% end %} which are **Neumann boundary conditions**. This combination is called an **initial boundary-value problem** (IBVP) and allows for finding a unique solution. For partial differential equations that are time-independent, we simply refer to a combination of boundary conditions and the PDE as a **boundary-value problem** (BVP).

## Solving and classifying second-order PDEs

A second-order PDE is a PDE describing a function $u(x_1, x_2)$ which has the standard form:

{% math() %}
a(x_1, x_2)\dfrac{\partial^2 u}{\partial x_1^2} + b (x_1, x_2) \dfrac{\partial u}{\partial x_1 \partial x_2} + c(x_1, x_2) \dfrac{\partial^2 u}{\partial x_2^2} + \underbrace{F\left(x_1, x_2, u, \dfrac{\partial u}{\partial x_1}, \dfrac{\partial u}{\partial x_2}\right)}_\text{lower-order terms}  = 0
{% end %}

In general, any second-order PDE can be transformed via a coordinate transformation into this standard form. Furthermore, we can distinguish between three main categories of second-order PDEs, based on the coefficients $a(x, y)$, $b(x, y)$, and $c(x, y)$:

- If $b^2 - 4ac > 0$, the equation is **hyperbolic**
- If $b^2 - 4ac = 0$, the equation is **parabolic**
- If $b^2 -4ac < 0$, the equation is **elliptic**

> **Why do we care about the coefficients?** The reason is because the qualitative behavior of second-order PDEs is _almost entirely determined_ by its second-order derivative terms. The lower order terms **do not really matter** as they do not contribute as broadly to the characteristics of the solution. Thus, we are very much interested in whether a second-order PDE is hyperbolic, parabolic, or elliptic.

As a quick non-rigorous guide, we can visually tell whether a solution is **hyperbolic, parabolic, or elliptic** by the general form they take:

{% math() %}
\begin{cases}
\text{Hyperbolic:} & C_1\dfrac{\partial^2 u}{\partial x^2} - C_2\dfrac{\partial^2 u}{\partial y^2} + \text{lower order terms} = 0  \\[10pt]
\text{Parabolic:} & C_1\dfrac{\partial^2 u}{\partial x^2} + \text{lower order terms} = 0 \\[10pt]
\text{Elliptic:} & C_1\dfrac{\partial^2 u}{\partial x^2} + C_2\dfrac{\partial^2 u}{\partial y^2} + \text{lower order terms} = 0
\end{cases}
{% end %}

_Source: [Stanford MATH220A course](https://web.stanford.edu/class/math220a/handouts/secondorder.pdf)_

However, it is worth it to familiarize ourselves with each specific type in detail. We will now look at the three standard second-order PDEs, the first one *hyperbolic*, the second one *parabolic*, and the third one *elliptic*.

> **Note:** the names hyperbolic, parabolic, and elliptic originate from the geometric terms of the hyperbola, parabola, and ellipse that are the three standard **conic sections**. It may seem like PDEs have nothing in common with geometry; on the surface level this can be presumed to be the case (although there _is_ a deeper mathematical connection that comes up in more advanced studies). One can (for now) take the main utility of the geometry-inspired classification system to be a a convenient way to distinguish between the three types of 2nd-order PDEs that is based on familiar terminology.

The standard **hyperbolic** second-order PDE is the **1D wave equation**, which (physically) describes a propagating wave $u(x, t)$:

{% math() %}
\dfrac{\partial^2 u}{\partial t^2} -c^2\dfrac{\partial^2 u}{\partial x^2} = 0
{% end %}

While the standard 1D wave equation describes a function of the form $u(x, t)$, one may also write a perfectly valid wave equation that describes a function of the form $u(x, y)$ that takes the form:

{% math() %}
\dfrac{\partial^2 u}{\partial x^2} -c^2\dfrac{\partial^2 u}{\partial y^2} = 0
{% end %}

It may not be very apparent how the wave equation fits the standard form of a second-order PDE we looked at previously. To show explicitly that the wave equation _does_ indeed fit the standard form, we may perform a coordinate transformation of the wave equation. Let our transformed coordinates $x_1, x_2$ be given by:

{% math() %}
\begin{align*}
x_1 &= x - ct \\
x_2 &= x + ct
\end{align*}
{% end %}

We then find that in these transformed coordinates, the wave equation takes the form:

{% math() %}
\dfrac{\partial^2 u}{\partial x_1 \partial x_2} = 0
{% end %}

We can show this by manually computing the coordinate-transformed partial derivatives by the chain rule:

{% math() %}
\begin{align*}
\dfrac{\partial}{\partial t} &= \dfrac{\partial x_1}{\partial t} \dfrac{\partial}{\partial x_1} + \dfrac{\partial x_2}{\partial t} \dfrac{\partial}{\partial x_2}  \\
&= -c \dfrac{\partial}{\partial x_1} + c \dfrac{\partial}{\partial x_2}  \\
&= c \left(\dfrac{\partial}{\partial x_2}- \dfrac{\partial}{\partial x_1}\right)
 \\
\dfrac{\partial}{\partial x} &= \dfrac{\partial x_1}{\partial x} \dfrac{\partial}{\partial x_1} + \dfrac{\partial x_2}{\partial x} \dfrac{\partial}{\partial x_2} \\
&= \dfrac{\partial}{\partial x_1} + \dfrac{\partial}{\partial x_2}
\end{align*}
{% end %}

From which we obtain:

{% math() %}
\begin{align*}
% time derivative
\dfrac{\partial^2}{\partial t^2} &= \dfrac{\partial}{\partial t}\left(\dfrac{\partial}{\partial t}\right) \\
&=c \left(\dfrac{\partial}{\partial x_2}- \dfrac{\partial}{\partial x_1}\right)c \left(\dfrac{\partial}{\partial x_2}- \dfrac{\partial}{\partial x_1}\right) \\
&= c^2 \left(\dfrac{\partial^2}{\partial x_2^2} - 2\dfrac{\partial^2}{\partial x_1 \partial x_2} + \dfrac{\partial^2}{\partial x_1^2}\right) \\
% spatial derivative
\dfrac{\partial^2}{\partial x^2} &= \dfrac{\partial}{\partial x}\left(\dfrac{\partial}{\partial x}\right) \\
&= \left(\dfrac{\partial}{\partial x_1} + \dfrac{\partial}{\partial x_2}\right) \left(\dfrac{\partial}{\partial x_1} + \dfrac{\partial}{\partial x_2}\right) \\
&= \left(\dfrac{\partial^2}{\partial x_1^2} + 2\dfrac{\partial^2}{\partial x_1 \partial x_2} + \dfrac{\partial^2}{\partial x_2^2}\right)
\end{align*}
{% end %}

Therefore substituting into the wave equation we have:

{% math() %}
\begin{align*}
&\dfrac{\partial^2 u}{\partial t^2} -c^2\dfrac{\partial^2 u}{\partial x^2} = 0\\
&c^2 \left(\dfrac{\partial^2}{\partial x_2^2} - 2\dfrac{\partial^2}{\partial x_1 \partial x_2} + \dfrac{\partial^2}{\partial x_1^2}\right)u - c^2 \left(\dfrac{\partial^2}{\partial x_1^2} + 2\dfrac{\partial^2}{\partial x_1 \partial x_2} + \dfrac{\partial^2}{\partial x_2^2}\right) = 0 \\
&c^2 \left(\dfrac{\partial^2}{\partial x_2^2} - 2\dfrac{\partial^2}{\partial x_1 \partial x_2} + \dfrac{\partial^2}{\partial x_1^2} -\dfrac{\partial^2}{\partial x_1^2} - 2\dfrac{\partial^2}{\partial x_1 \partial x_2} - \dfrac{\partial^2}{\partial x_2^2}\right) = 0 \\
&c^2 \left(\cancel{\dfrac{\partial^2}{\partial x_2^2}} - 2\dfrac{\partial^2}{\partial x_1 \partial x_2} + \cancel{\dfrac{\partial^2}{\partial x_1^2}} -\cancel{\dfrac{\partial^2}{\partial x_1^2}} - 2\dfrac{\partial^2}{\partial x_1 \partial x_2} - \cancel{\dfrac{\partial^2}{\partial x_2^2}}\right) = 0 \\
&-4c^2 \dfrac{\partial^2}{\partial x_1 \partial x_2} = 0\\
&\Rightarrow \dfrac{\partial^2}{\partial x_1 \partial x_2} = 0
\end{align*}
{% end %}

Thus we have $a(x, y) = c(x, y) = 0$ and $b(x, y) = 1$, making the wave equation **hyperbolic**. The hyperbolic nature of wave equation has some unique consequences for its solutions. First, in solutions to the wave equation, a disturbance (e.g. pulse) in one region propagates at a finite speed in space, where $c$ is the **propagation speed**. That is to say, information about one part of a solution can only be transmitted at a finite speed to other parts of the solution. Thus hyperbolic equations in physics typically describe _waves_, including waves of light (electromagnetic waves), vibrations of a string, and acoustic (sound) waves. Second, hyperbolic equations do not "smooth out" shocks that arise at one point in time. These shocks propagate throughout the solution, but once again, at a _finite speed_.

> **Note:** the 2D and 3D wave equations can be written as a system of 1D wave equations via a coordinate transformation, which are hyperbolic. Therefore, the 2D and 3D wave equations are _also_ hyperbolic.

The standard **parabolic** second-order PDE, meanwhile, is the **1D heat equation**, which (physically) describes a temperature distribution $u(x, t)$ through time:

{% math() %}
\dfrac{\partial u}{\partial t} = \alpha^2 \dfrac{\partial^2 u}{\partial x^2}
{% end %}

Recall that the time derivative on the left-hand side is a lower-order term, and therefore it **does not matter**. It also does not matter if the left-hand side is a first-order derivative with respect to another variable; the following would still be a heat equation (although not *the* heat equation):

{% math() %}
\dfrac{\partial u}{\partial x} = \alpha^2 \dfrac{\partial^2 u}{\partial x^2}
{% end %}

Since we ignore all lower-order terms when classifying PDEs, the first derivative can be effectively ignored. Therefore, we can place the heat equation in standard form as follows:

{% math() %}
\alpha^2 \dfrac{\partial^2 u}{\partial x^2} + \dots = 0
{% end %}

Where we use the notation that $\dots$ represents the lower order $\dfrac{\partial u}{\partial t}$ term. In this form, we can tell that $a(x, y) = \alpha^2$ while $b(x, y) = c(x, y) = 0$, and thus $b^2 - 4 ac = 0$, which is the defining characteristic of a parabolic PDE (as we would expect).

> **Note:** As with the wave equation, the 2D and 3D heat equations can also be put in parabolic form by rewriting them as a first-order system; each equation in the system would then take a parabolic form. Therefore, the 2D and 3D heat equations are _also_ parabolic.

Just as the wave equation possesses specific properties due to it being *hyperbolic*, the heat equation possesses specific properties due to it being _parabolic_. One property is that maxima and minima in the solution tend to be "smoothed out" as the solution $u(x, t)$ evolves in time, resulting in (mostly) *smooth* solutions. The behavior happens *globally (i.e. across the entire solution) at the same time. That is to say, unlike the wave equation, the heat equation assumes _infinite propagation speed_ and thus describes phenomena where a bulk quantity *uniformly* stabilizes towards equilibrium (as opposed to the non-uniform delayed propagation of information in the wave equation). Thus the heat equation physically describes **diffusion and diffusion-like phenomena**, making it the natural choice to describe heat transfer.

Lastly, the the standard **elliptic** second-order PDE is **Laplace's equation** (in 2D), which describes a wide variety of phenomena in physics. It takes the form:

{% math() %}
\dfrac{\partial^2 u}{\partial x^2} + \dfrac{\partial^2 u}{\partial y^2} = 0
{% end %}

Note that the positive sign **matters** here - if the plus sign were a negative sign, we would instead have a _hyperbolic_ PDE. Laplace's equation can also be written in terms of the **Laplacian operator** $\nabla^2$ as:

{% math() %}
\nabla^2 u = 0
{% end %}

Where the Laplacian in two dimensions takes the form $\nabla^2 = \dfrac{\partial^2}{\partial x^2} + \dfrac{\partial^2}{\partial y^2}$, and thus gives Laplace's equation:

{% math() %}
\dfrac{\partial^2 u}{\partial x^2} + \dfrac{\partial^2 u}{\partial y^2} = 0
{% end %}

The Laplace equation, in this form, is already in the standard form of a 2nd-order PDE (that we covered at the beginning of this section). As it has the coefficients $a(x, y) = c(x, y) = 1$ and $b(x, y) = 0$, we have $b^2 - 4ac < 0$, which makes the PDE **elliptic**.

> **Note:** Laplace's equation in 3D (which also takes the form $\nabla^2 u = 0$, just with the 3D Laplacian, so it reads $\dfrac{\partial^2 u}{\partial x^2} + \dfrac{\partial^2 u}{\partial y^2} + \dfrac{\partial^2 u}{\partial z^2} = 0$) is _also_ elliptic, which can be shown (again) by rewriting it as a system of PDEs). However, Laplace's equation in 1D is _not_ elliptic (rather, it is parabolic).

As the *standard elliptic PDE*, Laplace's equation demonstrates several of the defining characteristics of elliptic PDEs. First, note that Laplace's equation is usually written in a time-independent form - therefore, it describes **steady-state systems** (i.e. systems at equilibrium) that are slowly-evolving or constant in time. For instance, in electrostatics, the *electric potential* $V(x, y)$ satisfies Laplace's equation. Second, the solutions to Laplace's equation are always **smooth**. This is because, just like parabolic PDEs, information about parts of a solution can be thought of as travelling instantly between different parts of the solution; the nuance being that physical scenarios modelled by Laplace's equation are ones that _already reached equilibrium_. This also means that for $t \to \infty$, the 2D heat equation _becomes_ Laplace's equation as $\dfrac{\partial u}{\partial t} \to 0$.

The three representative 2nd-order PDEs - the **wave equation**, **heat equation**, and **Laplace's equation** - are unique in that _any_ second-order hyperbolic, parabolic, and elliptic PDE can be transformed into one of those equations (ignoring the lower-order terms, which are not significant). Thus the study of these three 2nd-order PDEs provides results that carry over to _all 2nd-order PDEs_. Therefore, we can summarize our general conclusions about 2nd-order PDEs as follows:

| Type of 2nd-order PDE | Representative equation | Representative form                                                                                                              |
| --------------------- | ----------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| Hyperbolic            | Wave equation           | $\dfrac{\partial^2 u}{\partial t^2} -c^2\nabla^2 u + F(x, y, z, t, \partial_x u, \partial_y u, \partial_z u, \partial_t u) = 0$  |
| Parabolic             | Heat equation           | $\dfrac{\partial u}{\partial t} -\alpha^2\nabla^2 u + F(x, y, z, t, \partial_x u, \partial_y u, \partial_z u, \partial_t u) = 0$ |
| Elliptic              | Laplace's equation      | $\nabla^2 u - F(x, y, z, \partial_x u, \partial_y u, \partial_z u) = 0$                                                          |

It is also possible to condense this information in a matrix, as follows:

{% math() %}
A = \begin{pmatrix}
a & b/2 \\ b/2 & c
\end{pmatrix}
=
\begin{pmatrix}
a(x, y) & b(x, y)/2 \\
b(x, y)/2 & c(x, y)
\end{pmatrix}
{% end %}

We may find the **eigenvalues** of the matrix by solving eigenvalue equation:

{% math() %}
\begin{align*}
&\det(A - \lambda I) = 0 \\
&\Rightarrow \begin{vmatrix}
a -\lambda & b/2 \\ b/2 & c-\lambda
\end{vmatrix} = 0 \\
&\Rightarrow (a-\lambda)(c - \lambda) - \dfrac{b^2}{4} = 0
\end{align*}
{% end %}

The solutions $\lambda$ to the above equation are the eigenvalues of $A$. The eigenvalues of the matrix can then be used to determine the classification of the PDE:

| Type of 2nd-order PDE | Eigenvalues of $A$              |
| --------------------- | ------------------------------- |
| Hyperbolic            | Opposite signs                  |
| Parabolic             | At least one eigenvalue is zero |
| Elliptic              | Same signs                      |

### Mixed-type 2nd-order PDEs

We have seen that 2nd-order PDEs may be classified, based on their coefficients, as _hyperbolic_, _parabolic_, or _elliptic_. But these distinctions are not as clear-cut as they may first appear; in fact, a 2nd-order PDE may be of _mixed type_, which means it can be hyperbolic in one region, parabolic in another region, and elliptic in yet another region. Consider the following 2nd-order PDE:

{% math() %}
\dfrac{\partial^2 u}{\partial x^2} + (x^2 - y^2) \dfrac{\partial^2 u}{\partial y^2} = 0
{% end %}

From first appearance, this PDE may _appear_ to be elliptic, as evidenced by the positive sign. But we must exercise caution, as this is not always so; in fact, it is *only true* for $|x| > |y|$. Notice what happens at the origin, where $|x| = |y| = 0$: then second term becomes zero, and we are left with:

{% math() %}
\dfrac{\partial^2 u}{\partial x^2} = 0
{% end %}

Which is a _parabolic_ differential equation. Finally, if we have $|x| < |y|$, the second term would then become _negative_, which is a _hyperbolic_ differential equation. This is why we classify this PDE as a mixed-type, as it is classified differently depending on region. Below is a graph of the regions in which the PDE takes each type (red represents $|x|>|y|$ and thus *elliptic*, blue represents $|x| < |y|$ and thus *hyperbolic*, and the dashed black line represents $|x| = |y|$ and thus parabolic):

{{ natural_img(
src="./mixed-type-pde.svg"
desc="A graph showing the PDE's different regions, with regions between the lines y = x and y = -x being elliptic, regions on either line being parabolic, and all other regions being hyperbolic."
) }}

### Existence, uniqueness, and stability

Up to this point, we have been solving PDEs with the assumption that _solutions always exist and are unique_ and that solutions are _stable_. That is, a solution satisfies the following characteristics:

- **Existence:** It is mathematically-possible to find the solution of a PDE for given initial (and/or boundary) conditions
- **Uniqueness:** The solution of a PDE for given initial (and/or boundary) conditions is the _one and only_ solution
- **Stability:** A PDE has solutions without shocks, discontinuities, divergent behavior, or any other instabilities that result in unpredictable behavior

It may be odd to think that solutions may not even _exist_ for a given PDE and boundary conditions, but this is possible. Typically, the most straightforward to show that a solution does not exist is to (attempt to) solve a given problem with the provided boundary conditions, and show that the boundary conditions are impossible to be satisfied.

Furthermore, even if a solution exists, there may be multiple solutions possible - a good check is to see if the trivial solution $u = 0$ is a solution to the BVP in addition to some other solution, or if a solution $u + C$ where $C$ is some constant is still a solution to the BVP. If multiple solutions are possible, then we say that the solution is _non-unique_. For example, consider the following BVP for the transport equation:

{% math() %}
\begin{gather*}
\dfrac{\partial u}{\partial x} = -\dfrac{\partial u}{\partial y} \\
u(0, y) = 0 \\
u(L, y)= 0
\end{gather*}
{% end %}

In this case through just guess-and-check we find that one particular solution to the BVP is the function $u(x, y) = \sin \left(\dfrac{\pi}{L}(x - y)\right)$. There is, however, another solution: $u(x, y) = 0$. Thus the solution is certainly **not unique**. 

In many cases, physical intuition can be enough to deduce whether the boundary conditions lead to nonexistent or non-unique solutions. If a PDE doesn't have _sufficiently many_ boundary conditions, a solution often exists but is not unique. For instance.

Finally, a PDE (and particularly hyperbolic PDEs) may have numerical instabilities that make a solution useless to compute even if found. If a problem satisfies all of the three criteria, for which we say that the problem is **well-posed**. This is particularly true for hyperbolic PDEs, which are in the form of the modified wave equation:

{% math() %}
\dfrac{\partial^2 u}{\partial x^2} - \dfrac{\partial^2 u}{\partial y^2} + \dots = 0
{% end %}

Such PDEs are highly sensitive to their initial conditions and thus stability depends on the smoothness (i.e. no abrupt jumps, discontinuities, and asymptotic behavior) of their initial conditions. The same is often true with *nonlinear* PDEs. Again, instability is hard to show without explicitly _solving_ the BVP and examining the resulting solution.

It is rarely possible to _prove_ existence, uniqueness, and stability for a general class of boundary-value (or initial-value) problems. It is often much easier to give a _counterexample_ (i.e. _disprove_ existence, uniqueness, and stability). Even when the conditions of existence, uniqueness, and stability are satisfied, it may be impossible to _prove this_ or a proof may only be possible on a case-by-case basis. In this introductory treatment of PDEs, we will not delve into the intricacies of proving existence, uniqueness, and stability, which involves very advanced mathematics.

It is, however, useful to mention several theorems for _specific PDEs_ that provide for existence and uniqueness (and in some cases, stability):

> **Theorem 1:** The solution to Poisson's equation $\nabla^2 f = 0$ (as well as its limiting case, Laplace's equation, given by $\nabla^2 f = 0$) is a **unique** solution for the boundary condition $u(\mathbf{r})_\text{boundary} = f(\mathbf{r})$ *as well as* for the boundary condition $\dfrac{\partial u}{\partial n} = g(\mathbf{r})$. That is to say, _if_ the values of $u$ are specified on the boundary, _or if_ the values of the derivative of $u$ are specified on the boundary (but **not specifying both**), then a solution will always **exist and is unique**.

> **Theorem 2:** By the **Cauchy–Kowalewskaya Theorem**, any second-order PDE in the form of the wave equation or diffusion equation with the Cauchy (initial) conditions $u(\mathbf{r}, 0)_\text{boundary} = f(\mathbf{r})$, $\dfrac{\partial u}{\partial t}(\mathbf{r}, 0) = g(\mathbf{r})$ yields a **unique solution** _if_ **both conditions** are provided and $f$ and $g$ are both functions with well-defined power series. 

> **Theorem 3:** Assuming theorem (2) holds, the solution to the diffusion equation $\dfrac{\partial^2 u}{\partial t^2} = k \nabla^2 u$ is **always stable** for $t \geq 0$ (although unstable for $t < 0$).

> **Theorem 4:** Assuming theorem (1) holds, the solution to Poisson's equation and Laplace's equation is **always stable**.

### Solutions of the wave equation

We have previously seen that the wave equation is the **prototypical hyperbolic PDE**, and is given by: 

{% math() %}
\dfrac{\partial^2 u}{\partial t^2} = c^2 \dfrac{\partial^2 u}{\partial x^2}
{% end %}

> **Note:** The fact that the equation has $c^2$ instead of $c$ as a constant is significant. $c^2$ is _guaranteed_ to be positive, while $c$ can be positive or negative, and this makes a massive difference in the behavior of the PDE (and therefore, its solutions).

As the prototypical hyperbolic PDE, the wave equation has a special significance because _any_ hyperbolic PDE can be transformed into the wave equation by a change of coordinates. In addition, it has the desirable characteristic that its general solution is actually rather simple:

{% math() %}
u(x, t) = f(x - ct) + g(x + ct)
{% end %}

Which we can find by the method of characteristics or by the method of coordinate transforms and then direct integration (which we previously showed). Particular solutions for the wave equation can be found by giving _initial conditions_. Let us consider the specific initial-value problem given by:

{% math() %}
\begin{align*}
u(x, 0) = \varphi(x) \\
\dfrac{\partial u}{\partial t}(x, 0) = \psi(x) 
\end{align*}
{% end %}

Where $\varphi(x), \psi(x)$ are arbitrary functions. This initial-value problem possesses a _particular solution_, given by:

{% math() %}
u(x, t) = \dfrac{1}{2} [\varphi(x - ct) + \varphi(x + ct)] + \dfrac{1}{2c} \int_{x - ct}^{x + ct}\psi(x')dx'
{% end %}

In the special case where we have $\dfrac{\partial u}{\partial t}(x, 0)  = \varphi(x) = 0$, then the particular solution reduces to:

{% math() %}
u(x, y) = \dfrac{1}{2} \varphi(x - ct) + \dfrac{1}{2}\varphi(x + ct)
{% end %}

Meanwhile in the special case we have $u(x, 0) = \psi(x) = 0$, then the particular solution reduces to:

{% math() %}
u(x, t) = \dfrac{1}{2c} \int_{x - ct}^{x + ct}\psi(x')dx'
{% end %}

#### Solutions of relevance in physics

One of the most useful particular solutions to the wave equation (particularly in Physics) is found by imposing the additional periodic boundary conditions that $u(x, t) = u(x + \lambda, t)$ and $u(x, t) = u(x, t + T)$. The solution then becomes:

{% math() %}
u(x, t) = A\cos \left(\dfrac{2\pi x}{\lambda} - \dfrac{2\pi}{T} t\right) + 
B \sin \left(\dfrac{2\pi x}{\lambda} + \dfrac{2\pi}{T} t\right)
{% end %}

Which can also be written in a more compact form if we define $\omega = \dfrac{2\pi}{T}$ and $k = \dfrac{2\pi}{\lambda}$, as follows:

{% math() %}
u(x, t) = A \cos (k x - \omega t) + B\sin (kx + \omega t)
{% end %}

In physics, each of these quantities has a very specific _physical interpretation_ - $\lambda$ is called the _wavelength_, $T$ is called the _period_, $\omega$ is the _angular frequency_ and $k$ is called the wavenumber. Such solutions are known as **plane-wave solutions** (also called traveling waves) as they describe waves that propagate sinusoidally to infinity, with their wavefronts being uniform (thus, planar). See the guide on [waves and oscillations in physics](@/waves-and-oscillations/index.md) for more details.

> **Note:** we can construct a more general solution if we write this solution as $u(x, t) = C e^{ikx - i\omega t}$ by _Euler's formula_ $e^{i\phi} = \cos \phi + i \sin \phi$. As the wave equation is linear, we can sum over an infinite number of plane waves spaced out in space (with different values of $k$) to have $u(x, t) = \dfrac{1}{\sqrt{2\pi}} \displaystyle \int C(k) e^{ikx - i\omega t} dk$. This is also a form often used in physics.

Note that a particular case of this particular solution can _also_ be found with the following boundary conditions:

{% math() %}
\begin{align*}
u(x, 0) &= 0 \\
\dfrac{\partial u}{\partial x}(x, 0) &= \psi(x) \\ &=\cos x
\end{align*}
{% end %}

Where we have:

{% math() %}
\begin{align*}
u(x, t) &= \dfrac{1}{2c} \int_{x - ct}^{x + ct}\psi(x')dx' \\
&= \dfrac{1}{2c} \int_{x - ct}^{x + ct} \cos x' dx' \\
&= \dfrac{1}{2c} (\sin x) \bigg|_{x - ct}^{x + ct} \\
&= \dfrac{1}{2c}[ \sin(x + ct) - \sin(x - ct)]
\end{align*}
{% end %}

We may verify that this solution does, indeed, satisfy the wave equation:

{% math() %}
\begin{align*}
\frac{\partial^2 u}{\partial x^2} &= -\dfrac{1}{2c}[\sin(x + ct) - \sin(x - ct)] \\
\frac{\partial^2 u}{\partial t^2} &= -\dfrac{1}{2}c[\sin(x + ct) - \sin(x - ct)] \\
\frac{\partial^2 u}{\partial t^2} - c^2\frac{\partial^2 u}{\partial x^2} &=
-\dfrac{1}{2}c[\sin(x + ct) - \sin(x - ct)]-c^2\sin(x + ct) \\ &-c^2\left(-\dfrac{1}{2c}\right)[ \sin(x + ct) -\sin(x - ct)] \\
&=0\quad \checkmark
\end{align*}
{% end %}

As we saw previously, solutions to the wave equation (waves) have the universal feature that the wave travels to the right, that is, $f(x - ct)$, and travels to the left, that is, $f(x +ct)$, at a _speed of propagation_ of $c$. Since $c$ is a constant, $c$ is also the _maximal speed_ at which information at a particular point $x$ of a solution can affect another particular point $x' = x \pm ct$. This has important consequences in physics: light is described in physics as an _electromagnetic wave_, and thus the $c$ is the famous _speed of light_, which is invariant (the same everywhere) and directly led to the development of the **theory of relativity**.

But remember that the wave equation describes _all types of waves_, one of which being the vibrations of a string, attached at its two ends. In this case, $u(x, t)$ represents the _displacement_ of the string from its equilibrium point. If we let the string be of length $L$ and have density $\rho$ under tension force $T$, then the boundary-value problem for the string reads:

{% math() %}
\begin{align*}
&\dfrac{\partial^2 u}{\partial t^2} =v^2 \dfrac{\partial^2 u}{\partial x^2}, \\
& v = \sqrt{\frac{T}{\rho}}, \\
&u(x, 0) = \begin{cases}
0, & x< 0 \\
f(x), &0 \leq x \leq L \\
0, & x> 0
\end{cases}, \\
&\dfrac{\partial u}{\partial t}(0, t) =  \dfrac{\partial u}{\partial t}(L, t) = 0
\end{align*}
{% end %}

We note that the wave equation for a string can be _equivalently_ written (by expanding out $v^2$ and distributing) as:

{% math() %}
\rho\dfrac{\partial^2 u}{\partial t^2} = T\dfrac{\partial^2 u}{\partial x^2}
{% end %}

The expression for the kinetic energy of the string is given by:

{% math() %}
K = \dfrac{1}{2} mv^2 = \dfrac{1}{2} \int_0^L \rho \left(\dfrac{\partial u}{\partial t}\right)^2 dx
{% end %}

Where we must integrate over $x$ as $\rho = \dfrac{dm}{dx}$ and thus to find the total mass we have to integrate the mass density across the string. If we assume constant density, we have:

{% math() %}
K = \dfrac{1}{2} \rho\int_0^L \left(\dfrac{\partial u}{\partial t}\right)^2 dx
{% end %}

If we differentiate the kinetic energy we have:

{% math() %}
\begin{align*}
\dfrac{dK}{dt} &= \dfrac{d}{dt}\left[ \dfrac{1}{2} \rho\int_0^L \left(\dfrac{\partial u}{\partial t}\right)^2 dx\right] \\
&= \dfrac{1}{2} \rho\int_0^L \underbrace{\dfrac{\partial}{\partial t}\left(\dfrac{\partial u}{\partial t}\right)^2}_\text{Leibnitz rule} dx \\
&= \rho \int_0^L \underbrace{\dfrac{\partial u}{\partial t} \dfrac{\partial}{\partial t}\left(\dfrac{\partial u}{\partial t}\right)}_\text{Chain rule}dt \\
&= \rho \int_0^L \dfrac{\partial u}{\partial t} \dfrac{\partial^2 u}{\partial t^2}dt
\end{align*}
{% end %}

But remember the wave equation for a string reads $\rho\dfrac{\partial^2 u}{\partial t^2} = T\dfrac{\partial^2 u}{\partial x^2}$. Therefore, substituting in, we have:

{% math() %}
\begin{align*}
\dfrac{dK}{dt} &=\rho \int_0^L \dfrac{\partial u}{\partial t} \dfrac{\partial^2 u}{\partial t^2}dt \\
&= T \int_0^L \dfrac{\partial u}{\partial t} \dfrac{\partial^2 u}{\partial x^2}dt \\
&= \underbrace{T \dfrac{\partial u}{\partial t}\dfrac{\partial u}{\partial x}\bigg|_0^L - T \int_0^L \dfrac{\partial}{\partial x}\left(\dfrac{\partial u}{\partial t}\right) \dfrac{\partial u}{\partial x} dx}_\text{integration by parts} \\
&= T \dfrac{\partial u}{\partial t}\dfrac{\partial u}{\partial x}\bigg|_0^L - T \int_0^L \dfrac{\partial^2 u}{\partial x \partial t} \dfrac{\partial u}{\partial x} dx \\
&= \underbrace{\cancel{T \dfrac{\partial u}{\partial t}\dfrac{\partial u}{\partial x}\bigg|_0^L}}_{\text{since } u(0, t) = u(0, t) = 0} - T \int_0^L \dfrac{\partial^2 u}{\partial x \partial t} \dfrac{\partial u}{\partial x} dx \\
&= - T \int_0^L \dfrac{\partial^2 u}{\partial x \partial t} \dfrac{\partial u}{\partial x} dx \\
&= \underbrace{-T\dfrac{d}{dt}\int_0^L \dfrac{1}{2}\left(\dfrac{\partial u}{\partial x}\right)^2 dx}_\text{total derivative - reverse chain rule}
\end{align*}
{% end %}

Meanwhile, the potential energy of a string (which we will not derive, but it comes from the work-energy theorem $K = -U$) is given by:

{% math() %}
U = -\dfrac{dK}{dt} =\dfrac{1}{2} T\int_0^L \left(\dfrac{\partial u}{\partial x}\right)^2 dx
{% end %}

Thus we find that the **total mechanical energy**, given by the sum of the kinetic and potential energies, is given by:

{% math() %}
\begin{align*}
E &= K + U \\
&= \dfrac{1}{2} \rho\int_0^L \left(\dfrac{\partial u}{\partial t}\right)^2 dx +
\dfrac{1}{2} T\int_0^L \left(\dfrac{\partial u}{\partial x}\right)^2 dx \\
&= \dfrac{1}{2} \int_0^L \rho \left(\dfrac{\partial u}{\partial t}\right)^2 + T\left(\dfrac{\partial u}{\partial x}\right)^2\, dx
\end{align*}
{% end %}

But since $K = -U$, then $\dfrac{dK}{dt} = -\dfrac{dU}{dt}$, and therefore $\dfrac{dE}{dt} = \dfrac{dK}{dt} + \dfrac{dU}{dt} = 0$. Therefore, total mechanical energy is *always constant*, as required by the law of the **conservation of energy**, and this constant value of energy is equal to:

{% math() %}
E = \dfrac{1}{2} \int_0^L \rho \left(\dfrac{\partial u}{\partial t}\right)^2 + T\left(\dfrac{\partial u}{\partial x}\right)^2\, dx
{% end %}

### Solutions of the diffusion equation

As we recall, the diffusion equation is the **prototypical parabolic equation**. It is given by:

{% math() %}
\dfrac{\partial u}{\partial t} = k \dfrac{\partial^2 u}{\partial x^2}
{% end %}

As the prototypical parabolic PDE, the wave equation has a special significance because _any_ hyperbolic PDE can be transformed into the diffusion equation by a change of coordinates. 

> **Note:** A special case of the diffusion equation is the well-studied *heat equation*, which many texts use in place of the diffusion equation. The diffusion equation, however, is more general.

Let us consider the following intial-boundary-value problem (IVBP) for the diffusion equation:

{% math() %}
\begin{gather*}
\dfrac{\partial u}{\partial t} = k \dfrac{\partial^2 u}{\partial x^2} \\[10pt]
u(x, 0) = \varphi(x) \\
u(L_1, t) = g(t) \\
u(L_2, t) = f(t) \\
t \geq 0, L_1 \leq x \leq L_2
\end{gather*}
{% end %}

The first (initial) condition for $u(x, 0)$ describes the initial spatial distribution of the function $u(x, t)$ at $t = 0$, whereas the second and third (boundary) conditions describe the value of $u$ through time on the _boundaries_ $x = L_1, x = L_2$. The two boundary conditions must satisfy the _consistency condition_ $f(0) = \varphi(L_2), g(0) = \varphi(L_1)$. The heat equation satisfies four important conditions (which we will not prove and simply state, as the proofs are very lengthy):

> **Maximum principle:** For any solution $u(x, t)$ for a well-posed initial-boundary-value problem, then $u(x, t) \leq u(x, 0)$ at all times $t \geq 0$. The maximum of $u(x, t)$ must lie on either $t = 0$ or at one of the boundaries $x \in [0, L]$

> **Minimum principle:** For any solution $u(x, t)$ for a well-posed initial-boundary-value problem, then $\operatorname{min}u(x, t) \geq \operatorname{min} [\varphi(x), f(t), g(t)]$. The minimum must lie on either $t = 0$ or at one of the boundaries $x \in [0, L]$

> **Well-posedness theorem for the heat equation:** For the aforementioned boundary-value problem, a solution always exists, is unique, and is stable: a small perturbation $u(x + \delta x, 0)$ does not strongly affect the solution $u(x, t)$. That is, for two given points $(x_1, 0), (x_2, 0)$ for which $\|(x_1, 0) - (x_2, 0)\| \leq \epsilon_1$ (where $\epsilon_1$ is a small number), then one may always find a _unique solution_, and $\|u(x_1, t) - u(x_2, t)\| \leq \epsilon_2$ for all times $t$ (i.e. two points initially close together stay together).

> **Linear property of solutions:** For any solution $u(x, t)$, then $u(x - a, t)$ and $u(\sqrt{a}x, a t)$ is also a solution.

> **Differentiation and integration of solutions:** For any solution $u(x, t)$ that possesses a derivative $v = \dfrac{\partial u}{\partial t}$, $v$ _also_ satisfies a diffusion equation $\dfrac{\partial v}{\partial t} = k\dfrac{\partial^2 v}{\partial t^2}$. Likewise, for any solution $u(x, t)$ that possesses an integral $I = \displaystyle \int_a^b u(x, t) dx$, $I$ _also_ satisfies a diffusion equation $\dfrac{\partial I}{\partial t} = k\dfrac{\partial^2 I}{\partial t^2}$. The same applies for {% inlmath() %}I = \displaystyle \int_a^b u(x - y, t)g(y)\,dy{% end %} This directly results from the linearity of the diffusion equation (i.e. the sum $u_1 + u_2$ of two solutions $u_1, u_2$ is also a solution).

Intuitively, these results makes the diffusion equation extremely easy (and powerful) to work with. In addition, they allow us to write the general solution of the diffusion equation either in terms of an infinite series:

{% math() %}
u(x, t) = \sum_{i = 1}^n a_n u_n(x, t) = a_1 u_1(x, t) + a_2 u_2(x, t) + \dots + a_n u_n(x, t)
{% end %}

Or in terms of an integral:

{% math() %}
u(x, t) = \int_{-\infty}^\infty u(x', t)\, dx'
{% end %}

> **Note:** Whether the general solution should be written as a sum or integral typically depends on the boundary conditions (though it can also depend on other factors).

Let us now consider solving the initial-boundary-value problem for the diffusion equation, as shown:

{% math() %}
\begin{gather*}
\dfrac{\partial u}{\partial t} = \alpha \dfrac{\partial^2 u}{\partial x^2} \\
u(x, 0) = \varphi(x) \\
\lim_{x \to \pm \infty} \varphi(x) = 0
\end{gather*}
{% end %}

This initial-boundary-value problem is often called _diffusion on the real line_. We may solve this problem as follows. It should be noted that this is _not_ the conventional way it is derived and is not a rigorous derivation at all. To start, let us assume a solution in the form $u(x, t) = \varphi(x) Q(t)$ (this is actually a valid assumption because the diffusion equation is separable). In this form, if we differentiate, we find that:

{% math() %}
\begin{matrix*}
\dfrac{\partial u}{\partial t} = Q'(t) \varphi(x), 
&\dfrac{\partial^2 u}{\partial x^2} = Q(t) \varphi''(x)
\end{matrix*}
{% end %}

Where we can effectively treat $\varphi$ as a constant when differentiating with respect to $t$ since $Q$ doesn't depend on time, and likewise, we can treat $Q(t)$ as a constant when differentiating with respect to $x$ since $Q$ doesn't depend on position. If we substitute into the PDE then divide both sides by $Q \varphi$, we have:

{% math() %}
\begin{gather*}
\dfrac{\partial u}{\partial t} = \alpha \dfrac{\partial^2 u}{\partial x^2} \\
Q' \varphi = \alpha Q \varphi'' \\
\dfrac{1}{Q\varphi}Q' \varphi = \dfrac{1}{Q\varphi}\alpha Q \varphi'' \\
\dfrac{Q'}{Q} = \dfrac{\varphi''}{\alpha \varphi} = \text{const.}
\end{gather*}
{% end %}

The last line arises from the property that when two derivatives are equal, both must be equal to a constant. This means we now have two differential equations, $Q'/Q = \text{const.}$ and $\varphi'' / \alpha \varphi = \text{const.}$ Let us look at just the first equation. If we call the constant in the equation $-\kappa$ (the sign does not matter as the constant is arbitrary), then we have:

{% math() %}
Q' = -\kappa Q
{% end %}

Which has the solution:

{% math() %}
Q(t) = e^{-\kappa t}
{% end %}

Thus our solution becomes:

{% math() %}
u(x, t) = \varphi(x) e^{-\kappa t}
{% end %}

But this is not a general solution (yet) because due to the property of linearity of the diffusion equation (which we showed previously), $u_1 + u_2$ is *also* a solution. Therefore, the more general solution is a linear sum of solutions:

{% math() %}
u(x, t) = \sum_n A_n \varphi(x) e^{-\kappa_n t}
{% end %}

In the limiting case, this becomes the **general solution** (at least for the given initial and boundary conditions):

{% math() %}
u(x, t) = \int_{-\infty}^\infty A(x) \varphi(\tilde x) e^{-\kappa t} d \tilde x
{% end %}

Where we must switch the bounds for the $\varphi$ term from $x \to y$ to distinguish the variables we are integrating over versus the variables that represent the coordinates of $u(x, t)$ - this is due to the fundamental theorem of calculus $\displaystyle \int_0^x f'(\tilde x) dy = f'(\tilde x)$. The above equation is true for *any* $A(x)$ that allows $u(x, t)$ to satisfy the given boundary conditions. An intuitive explanation is as follows: if we sum infinitely-many "clones" of the solution $\varphi(x)$ spaced-out at different positions $x$ and different times $t$ (as governed by $A(x)$), then the solutions can add up to form an arbitrary function (in some ways, similar to Taylor series or Fourier series if that is familiar).

Now, recall the property (which we showed before) that for any solution $v(x, t)$, any shift of the solution $u(x, t) = v(x -a, t)$ is also a solution. If we let our previous solution be written $v(x, t)$, that is:

{% math() %}
v(x, t) = \int_{-\infty}^\infty A(x) \varphi(\tilde x) e^{-\kappa t} d \tilde x
{% end %}

then we have:

{% math() %}
u(x, t) = \int_{-\infty}^\infty A(x-a) \varphi(\tilde x-a) e^{-\kappa t} d \tilde x
{% end %}

We can write this in a simpler form if we use the change of variables $y = \tilde x- a$, for which the solution simplifies to:

{% math() %}
u(x, t) = \int_{-\infty}^\infty A(y(x)) \varphi(y) e^{-\kappa t} dy
{% end %}

The final step is require that the solution does indeed satisfy the boundary conditions - that is, $\varphi \to 0$ for $x \to \pm \infty$ (the other boundary condition $u(x, 0) = \varphi(x)$ is automatically-satisfied from our separation of variables procedure). A specific $A(x, y, t)$ that does indeed satisfy the boundary conditions is the **Gaussian** (which in this case is a shifted Gaussian to accomodated our shifted solution):

{% math() %}
A(x) = \dfrac{1}{\sqrt{4\pi \kappa t}}e^{-(x-y)^2/4\kappa t + \kappa t}
{% end %}

Therefore substituting $A(k)$ we have:

{% math() %}
\begin{align*}
u(x, t) &= \int_{-\infty}^\infty \left[\dfrac{1}{\sqrt{4\pi \kappa t}}e^{-(x-y)^2/4\kappa t + \kappa t}\right] \varphi(y) e^{-\kappa t} d y \\
&= \int_{-\infty}^\infty \dfrac{1}{\sqrt{4\pi \kappa t}} e ^{-(x - y)^2/4\kappa t + \cancel{\kappa t - \kappa t}} \varphi(y) dy \\
&= \int_{-\infty}^\infty \dfrac{1}{\sqrt{4\pi \kappa t}} e ^{-(x - y)^2/4\kappa t} \varphi(y) dy
\end{align*}
{% end %}

Since $t$ is not integrated over, we can pull out the factor in $t$ outside the integral:

{% math() %}
u(x, t) = \dfrac{1}{\sqrt{4\pi \kappa t}}\int_{-\infty}^\infty e ^{-(x - y)^2/4\kappa t} \varphi(y) dy
{% end %}

Thus the particular solution to the diffusion equation for the given initial-boundary-value problem is then:

{% math() %}
u(x, t) = \dfrac{1}{\sqrt{4\pi \kappa t}} \int_{-\infty}^\infty e^{-(x - y)^2 / (4 \kappa t)} \varphi(y) dy
{% end %}

Where the integrand $\dfrac{1}{\sqrt{4\pi \kappa t}}  e^{-(x - y)^2 / (4 \kappa t)}$ is known as a **Green's function** (other names include _source function_, _propagator_, _kernel_, or _fundamental solution_). The Green's function may be thought of as something that "pushes" (evolves) the initial condition $u(x, 0) = \varphi(x)$ to bring it to $u(x, t)$ by time $t$ (for those familiar with the term, it can be thought of as an _operator_). This may be a bit easier to see if we write the solution as follows:

{% math() %}
u(x, t) = \int_{-\infty}^\infty \underbrace{\dfrac{1}{\sqrt{4\pi \kappa t}} e^{-(x - x')^2 / (4 \kappa t)}}_{\text{at } t = 0 \text{ this is equal to }\delta(x - x')} u(x', 0) dx'
{% end %}

In this form, we can see that the Green's function serves as a multiplication factor that starts out at $e^{-(x - x')^2/(4\kappa (0))} = \infty$ at $t = 0$ (but luckily, since it also starts out as infinitely thin, the integral is finite). We call this initial state of the Green's function as the **Dirac delta** or _delta function_, written as $\delta(x - x')$. The delta function has the special property that:

{% math() %}
\int_{-\infty}^\infty \delta(x - x') u(x', 0) = u(x, 0)
{% end %}

Which means that if we evaluate $u(x, t)$ at $t = 0$ we do indeed get back the initial condition. Now, as $t$ increases, the value of $e^{-(x - x')^2/(4\kappa t)}$ rapidly diminishes. Thus, we find that the _maximum principle_ is also satisfied - that $u(x, t) \leq u(x, 0)$. Since our Green's function $e^{-(x - x')^2/(4\kappa t)}$ smoothly decays to infinity as $x \to \pm \infty$, multiplying $u(x, 0)$ by it and integrating results in the solution being "spread out" over time, exactly analogous to our intuitive understanding of diffusion. Our way of writing the general solution previously was just a renaming - $\varphi(x) = u(x, 0)$, and we changed integration variable we used from $x'$ to $y$, as well as pulling out the factor at the front outside the integral, but otherwise the mathematics are identical:

{% math() %}
u(x, t) = \dfrac{1}{\sqrt{4\pi \kappa t}} \int_{-\infty}^\infty e^{-(x - y)^2 / (4 \kappa t)} \varphi(y) dy
{% end %}

We may use this solution to solve the initial-boundary-value problem given by:

{% math() %}
\begin{gather*}
\dfrac{\partial u}{\partial t} = \kappa \dfrac{\partial^2 u}{\partial x^2}  \\
u(x, 0) =\varphi(x) = \begin{cases} 1, & |x| \leq 1 \\ 0, & |x| > 1\end{cases} \\
\lim_{x \to \pm \infty} \varphi(x) = 0
\end{gather*}
{% end %}

This is simply a matter of substituting $\varphi(y) = 1$ in the integral (as long as we also remember the constraint that this is true for only $|x| \leq 1$, i.e. within $-1 \leq x \leq 1$). Since this is a piecewise initial condition, we need to use the integral rule for piecewise functions. For a piecewise function given by:

{% math() %}
H(x) =\begin{cases}
f(x) & |x| < 1 \\
g(x) & |x| > 1
\end{cases}
{% end %}

The integral of the function over $x \in (-\infty, \infty)$ is equal to:

{% math() %}
\begin{align*}
\int_{-\infty}^\infty H(x) dx &= \int_{-\infty}^{-1} H(x) dx + \int_{-1}^1 H(x) dx +\int_1^\infty H(x) dx \\
&=  \int_{-\infty}^{-1} g(x) dx + \int_{-1}^1 h(x) dx+ \int_1^\infty g(x) dx \\
\end{align*}
{% end %}

Using this identity, and substituting into the Green's function solution, we have:

{% math() %}
\begin{align*}
u(x, t) &= \dfrac{1}{\sqrt{4\pi \kappa t}} \int_{-\infty}^\infty e^{-(x - y)^2 / (4 \kappa t)} \varphi(y) dy \\
&= \dfrac{1}{\sqrt{4\pi \kappa t}} \bigg[\cancel{\int_{-\infty}^{-1} e^{-(x - y)^2 / (4 \kappa t)} (0) dy}^0 \\
&\qquad +\int_{-1}^{1} e^{-(x - y)^2 / (4 \kappa t)} (1) dy \\
&\qquad + \cancel{\int_{1}^\infty e^{-(x - y)^2 / (4 \kappa t)} (0) dy\bigg]}^0 \\
&= \int_{-1}^{1} e^{-(x - y)^2 / (4 \kappa t)} dy
\end{align*}
{% end %}

Thus our solution is given by:

{% math() %}
u(x, t) = \int_{-1}^{1} e^{-(x - y)^2 / (4 \kappa t)} dy
{% end %}

There is, however, a slightly nicer-looking way to write out this solution, and that is using the **error function**. The error function, denoted $\operatorname{Erf}(x)$, is given by:

{% math() %}
\operatorname{Erf}(x) = \dfrac{2}{\sqrt{\pi}} \int_0^x e^{-p^2} dp
{% end %}

To cast the solution into this "nicer" form, we start by dividing the integral into two parts, one between $[0, 1]$ and the other between $[-1, 0]$:

{% math() %}
u(x, t) = \int_{-1}^0 e^{-(x - y)^2 / (4 \kappa t)} dy + \int_0^1 e^{-(x - y)^2 / (4 \kappa t)} dy
{% end %}

Now, let $p^2 = \dfrac{(x - y)^2}{4\kappa t}$, for which we have $p = \dfrac{x-y}{\sqrt{4\kappa t}}$ and $dp = -\dfrac{1}{\sqrt{4\kappa t}}dy$. Additionally, we must also change the integral's bounds on substitution, so we must adjust the bounds as follows:

{% math() %}
\begin{align*}
y_1 = 0 &\to p_1 = \dfrac{x}{\sqrt{4\kappa t}} \\
y_2 = 1 &\to p_2 = \dfrac{x-1}{\sqrt{4\kappa t}} \\
y_3 = -1 &\to p_3 = \dfrac{x+1}{\sqrt{4\kappa t}}
\end{align*}
{% end %}


Thus, after substitution our integral becomes:

{% math() %}
\begin{align*}
u(x, t) &= \left(-\sqrt{4\kappa t} \int_{(x + 1)/\sqrt{4\kappa t}}^{x/\sqrt{4\kappa t}}e^{-p^2}dp\right) + \left(-\sqrt{4\kappa t} \int_{x/\sqrt{4\kappa t}}^{(x - 1)\sqrt{4\kappa t}} e^{-p^2} dp\right) \\
&= -\sqrt{4\kappa t} \int_{(x + 1)/\sqrt{4\kappa t}}^0 e^{-p^2} dp - \sqrt{4\kappa t} \int_0^{x/\sqrt{4\kappa t}} e^{-p^2}dp \\
&\qquad \quad -\sqrt{4\kappa t} \int_{x/\sqrt{4\kappa t}}^0 e^{-p^2} dp - \sqrt{4\kappa t} \int_0^{(x - 1)\sqrt{4\kappa t}} e^{-p^2} dp \\
&= \sqrt{4\kappa t} \int_0^{(x + 1)/\sqrt{4\kappa t}} e^{-p^2} dp - \sqrt{4\kappa t} \int_0^{x/\sqrt{4\kappa t}} e^{-p^2}dp \\
&\qquad \quad +\sqrt{4\kappa t} \int_0^{x/\sqrt{4\kappa t}} e^{-p^2} dp - \sqrt{4\kappa t} \int_0^{(x - 1)\sqrt{4\kappa t}} e^{-p^2} dp \\
&= \sqrt{4\kappa t} \int_0^{(x + 1)/\sqrt{4\kappa t}} e^{-p^2} dp - \cancel{\sqrt{4\kappa t} \int_0^{x/\sqrt{4\kappa t}} e^{-p^2}dp} \\
&\qquad \quad + \cancel{\sqrt{4\kappa t} \int_0^{x/\sqrt{4\kappa t}} e^{-p^2} dp} - \sqrt{4\kappa t} \int_0^{(x - 1)\sqrt{4\kappa t}} e^{-p^2} dp \\
&= \sqrt{4\kappa t} \left[\int_0^{(x + 1)/\sqrt{4\kappa t}} e^{-p^2} dp - \int_0^{(x - 1)\sqrt{4\kappa t}} e^{-p^2} dp\right] \\
&= \sqrt{4\kappa t}\operatorname{Erf} \left(\dfrac{x+1}{\sqrt{4\kappa t}}\right) - \sqrt{4\kappa t} \operatorname{Erf} \left(\dfrac{x-1}{\sqrt{4\kappa t}}\right) \\
&= \sqrt{4\kappa t}\left[\operatorname{Erf} \left(\dfrac{x+1}{\sqrt{4\kappa t}}\right) - \operatorname{Erf} \left(\dfrac{x-1}{\sqrt{4\kappa t}}\right)\right]
\end{align*}
{% end %}

Which is the solution to our boundary value problem for our chosen initial condition $u(x, 0) = \varphi(x) = \begin{cases} 1, & |x| \leq 1 \\ 0, & |x| > 1\end{cases}$. Note that this is one of the few cases in which an analytical solution can be written out; in most cases, the integral is simply impossible to evaluate by hand and can only be solved numerically.

> **Note for the interested reader:** the solution of the diffusion equation on the _half-line_ (where the domain is $0 \leq x \leq \infty$) is very similar to diffusion on the real line, *except* that it requires the additional boundary condition $u(0, t) = 0$, is given by $u(x, t) = \dfrac{1}{\sqrt{4\pi \kappa t}} \displaystyle \int_{-\infty}^\infty (e ^{-(x - y)^2/4\kappa t} + e^{-(x + y)^2/4\kappa t} )\varphi(y) dy$

### Concluding remarks to the diffusion and wave equation

We have studied the diffusion and wave equation in detail and constructed particular solutions to several initial-boundary value problems (IBVPs). As well as solving specific IBVPs, we have found that the wave equation and diffusion equation satisfy particular characteristics:

| PDE                                               | Speed of propagation | Singularities (i.e. shocks/other "not smooth" disturbances) | Energy        | Requirements for well-posedness                   |
| ------------------------------------------------- | -------------------- | ----------------------------------------------------------- | ------------- | ------------------------------------------------- |
| Diffusion equation (and all other parabolic PDEs) | Infinite             | Smoothed out immediately                                    | Not conserved | Only for $t \geq 0$; *not well-posed* for $t < 0$ |
| Wave equation (and all other hyperbolic PDEs)     | $c$                  | Lost (smoothed-out) immediately                             | Conserved     | Well-posed for all time                           |

### Separation of variables for boundary-value problems

At the beginning of the guide, we gave a brief overview of the **separation of variables** procedure. Separation of variables is a powerful technique for solving PDEs, so to develop our understanding of it further, let us now re-examine the same procedure in more detail.

#### Separation of variables for the wave equation

To start, let us consider the wave equation in one dimension on the domain $x \in [0, L], t \in [0, \infty)$, with the following boundary conditions:

{% math() %}
\begin{gather*}
\dfrac{\partial^2 u}{\partial t^2} = c^2 \dfrac{\partial^2 u}{\partial x^2} \\
u(0, t) = 0, \quad u(L, t) = 0 \\
u(x, 0) = \varphi(x), \quad \dfrac{\partial u}{\partial t}(x, 0) = \psi(x)
\end{gather*}
{% end %}

We assume a solution in the form $u(x, t) = X(x) T(t)$, for which we find that upon taking the derivatives, we have:

{% math() %}
\begin{align*}
\dfrac{\partial^2 u}{\partial t^2} &= X(x)T''(t) \\
\dfrac{\partial^2 u}{\partial x^2} &= X''(x) T(t)
\end{align*}
{% end %}

> **Note:** You can verify this by direct calculation; the reason why the partial derivatives are so simple is that $X$ only depends on $x$, and $T$ only depends on $t$. This means that when taking the partial derivative with respect to $x$, $T$ can be treated as a constant; similarly, when taking the partial derivative with respect to $t$, $X$ can be treated as a constant.

Therefore, substituting into the wave equation and dividing by $X(x)T(t)$ yields:

{% math() %}
\begin{gather*}
XT'' = c^2 X''T \\
\dfrac{1}{c^2} XT'' = X''T \\
\dfrac{1}{X(x)T(t)}\dfrac{1}{c^2}XT'' = \dfrac{1}{X(x)T(t)} X''T \\
\dfrac{T''}{c^2 T} = \dfrac{X''}{X}
\end{gather*}
{% end %}

Note how that, in the last line, we have two combinations of derivatives _equal_ to each other. This can only happen if both derivatives are a constant, so it must be the case that:

{% math() %}
\dfrac{T''}{c^2 T} = \dfrac{X''}{X} = \text{const.} \quad \Rightarrow \quad
\begin{align*}
T'' &= c^2 T \times \text{const.} \\
X'' &= X \times \text{const.}
\end{align*}
{% end %}

This constant is what we call the **separation constant**; we now find that the wave equation, a _partial_ differential equation, has reduced (relief!) to two _ordinary_ differential equations that are much easier to solve. Let us name our _separation constant_ $k^2$ (the square does _not_ matter, since the square of a constant is still a constant, it just makes the mathematics easier). Since it is a constant, its value is arbitrary; $k^2$ can have a positive or negative sign, or be zero or complex. This is one of the cases where choosing the appropriate answer requires a fair bit of intuition about what the solution to the ODEs will be. In this particular case, the right choice is for $k^2$ to have a negative sign, as shown:

{% math() %}
\begin{matrix*}
T'' = -k^2 c^2 T, & X''=-k^2 X
\end{matrix*}
{% end %}

The reason for this is the boundary conditions. The solution to ODEs in the form $y'' = -a^2 y$ (where $a$ is a constant) is either a sine or cosine wave (or a sum of both). Such solutions can be zero at _finite_ values. However, the solutions to ODEs in the form $y'' = a^2 y$ are exponential functions (or sum of exponential functions). Such solutions can only be zero at infinity. Additionally, the solutions to ODEs in the form $y'' = 0$ are linear functions, which can only be zero at one point. Since our boundary conditions are $u(0, t) = u(L, t) = 0$, that is, $u(x, t)$ is zero at $x = 0$ and $x = L$ (which are not at infinity and are zero at two locations), we must choose $-k^2$, not $k^2$ or zero. This means that our solutions are:

{% math() %}
\begin{align*}
X(x) &= A \cos k x + B \sin k x \\
T(t) &= C \cos (kc t) + D \sin (kct)
\end{align*}
{% end %}

We may make the solutions look "prettier" by defining $\omega \equiv kc$, so we can rewrite the solutions as follows:

{% math() %}
\begin{align*}
X(x) &= A \cos k x + B \sin k x \\
T(t) &= C \cos \omega t + D \sin \omega t
\end{align*}
{% end %}

Recall that we expressed our solution in the form $u(x, t) = X(x)T(t)$. Thus, substituting our found solutions for $X(x)$ and $T(t)$, we have:

{% math() %}
\begin{align*}
u(x, t) &= X(x)T(t) \\
&= (A \cos k x + B \sin k x)( C \cos \omega t + D \sin \omega t)
\end{align*}
{% end %}

To determine the values of our coefficients $A, B, C, D$, we must apply the boundary conditions. Applying our first boundary condition $u(0, t) = 0$, we have:

{% math() %}
\begin{align*}
u(0, t) &= (A \cancel{\cos(0)}^1 + \cancel{B \sin (0)}^0)(C \cos \omega t + D \sin \omega t) = 0 \\
&= A(C \cos \omega t + D \sin \omega t) = 0
\end{align*}
{% end %}

To satisfy this boundary condition, since $\cos \omega t, \sin \omega t \neq 0$, it must be the case that $A = 0$. Therefore our solution simplifies to:

{% math() %}
u(x, t) = B \sin k x( C \cos \omega t + D \sin \omega t)
{% end %}

Applying our second boundary condition $u(L, t) = 0$, we have:

{% math() %}
u(L, t) = B \sin (k L)( C \cos \omega t + D \sin \omega t) = 0
{% end %}

Again, since $\cos \omega t, \sin \omega \neq 0$, this can only be satisfied if $B \sin k L = 0$. We find that this condition can be satisfied if $kL = n\pi$, i.e. if $kL$ is equal to an integer multiple of $\pi$, since we know that $\sin(\pi) = \sin(2\pi) = \sin(3\pi) = \dots = \sin(n\pi) = 0$. Therefore, we have found that $k = n\pi/L$, and now our solution becomes:

{% math() %}
u(x, t) = B \sin \left(\dfrac{n\pi x}{L}\right)( C \cos \omega t + D \sin \omega t)
{% end %}

We will now take the step of distributing the constant factor of $B$ into each of the two terms. Defining $J \equiv B\cdot C, K \equiv B \cdot D$, we can rewrite the above solution as:

{% math() %}
u(x, t) = \sin\left(\dfrac{n\pi x}{L}\right)(J \cos \omega t + K \sin \omega t)
{% end %}

The remaining two initial-boundary conditions are both initial conditions: one for $u(x, 0)$, and one for $\dfrac{\partial u}{\partial t}(x, 0)$. One might wonder how these conditions can be satisfied when our solution is entirely written in terms of sines and cosines. The answer is that because the diffusion equation is _linear_, we can sum solutions together to form new solutions. In fact, we can sum as many solutions as we'd like! This results in a _more general solution_ given by:

{% math() %}
\begin{align*}
u(x, t) &= \sum_{n = 1}^\infty \sin\left(\dfrac{n\pi x}{L}\right)(J_n \cos \omega t + K_n \sin \omega t) \\
&=\sum_{n = 1}^\infty \sin\left(\dfrac{n\pi x}{L}\right)\left[J_n \cos \left(\dfrac{n\pi c t}{L}\right) + K_n \sin \left(\dfrac{n\pi c t}{L}\right)\right]
\end{align*}
{% end %}

Where we wrote the second form of the solution (in the previous line) via our definition from before, $\omega \equiv kc$. This is the **solution** to our boundary-value problem. From here, if we substitute $u(x, 0)$, we have:

{% math() %}
u(x, 0) = \sum_{n = 1}^\infty J_n \sin \left(\dfrac{n\pi x}{L}\right) = \varphi(x)
{% end %}

This is called a **Fourier sine series**, and any "well-behaved" function can be written using this series expansion. For instance, if we had $\varphi(x) = x$, then the series expansion reads:

{% math() %}
\varphi(x) = \dfrac{2L}{\pi}\left[\sin \pi x - \dfrac{1}{2} \sin 2\pi x + \dfrac{1}{3} \sin 3\pi x - \dfrac{1}{4} \sin 4\pi x + \dots\right]
{% end %}

Similarly, if we take the derivative with respect to time, we can write a Fourier series expansion for $\dfrac{\partial u}{\partial t}(x, 0) = \psi(x)$. Using these series, we can effectively write out a solution to _any_ choice of $u(x, 0)$ and $\dfrac{\partial u}{\partial t}(x, 0)$. This is, indeed, one of the reasons why the separation of variables technique is so powerful.

> **Note:** how do we _determine_ what the correct coefficients $K_n, J_n$ should be? We will discover this later, but for now (for just $J_n$) we will provide a formula without proof: $J_n = \dfrac{2}{L} \displaystyle \int_0^L \varphi(x) \sin\left(\dfrac{n\pi x}{L}\right) dx$.

#### Separation of variables for the diffusion equation

Let us now consider the very similar boundary-value problem for the diffusion equation across the domain $x \in [0, L], t \in [0, \infty)$:

{% math() %}
\begin{gather*}
\dfrac{\partial u}{\partial t} = \kappa^2 \dfrac{\partial^2 u}{\partial x^2} \\
u(0, t) = 0, \quad u(L, t) = 0 \\
u(x, 0) = \varphi(x)
\end{gather*}
{% end %}

Here, we again assume a solution in the form $u(x, t) = X(x) T(t)$, for which we have:

{% math() %}
\begin{align*}
\dfrac{\partial u}{\partial t} &= X(x)T'(t) \\
\dfrac{\partial^2 u}{\partial x^2} &= X''(x)T(t)
\end{align*}
{% end %}

Therefore, substituting into the diffusion equation, and dividing by $X(x)T(t)$, we have:

{% math() %}
\begin{gather*}
XT' = \kappa^2 X''T \\
\dfrac{1}{\kappa^2}XT' = X''T\\
\dfrac{1}{XT} \dfrac{1}{\kappa^2}XT' = \dfrac{1}{XT}X''T \\
\dfrac{T'}{\kappa^2 T} = \dfrac{X''}{X} = \text{const.}
\end{gather*}
{% end %}

We choose our separation constant to be $\beta^2$ with a negative sign (with the same reasoning as before, due to our pair of finite boundary conditions). We could've equivalently called it $k^2$, but since $k$ and $\kappa^2$ look too similar, we will use the letter $\beta$ instead. Thus we have reduced the diffusion equation into the set of two ordinary differential equations, given by:

{% math() %}
\begin{align*}
T' &= -\beta^2\kappa^2 T \\
X'' &= -\beta^2 X
\end{align*}
{% end %}

The general solutions to the differential equations are:

{% math() %}
\begin{align*}
T(t) &= Ae^{\beta \kappa t} + Be^{-\beta \kappa t} \\
X(x) &= C \cos \beta x + D \sin \beta x
\end{align*}
{% end %}

Our solution for $u(x, t)$ therefore becomes:

{% math() %}
\begin{align*}
u(x, t) &= X(x)T(t) \\
&= (Ae^{\beta \kappa t} + Be^{-\beta \kappa t})(C \cos \beta x + D \sin \beta x)
\end{align*}
{% end %}

We can now individually substitute our boundary conditions. But first, there is a way that we can simplify the solution just by inspection (that is, by "being clever"). We solve on the domain $t \in [0, \infty)$, which means that we would want our solution to not blow up for large values of $t$. This automatically means that $A$ must be zero; otherwise the $Ae^{\beta x t}$ term grows exponentially as $t$ increases! So we have deduced that the solution must be in the following form if it is to be "reasonable":

{% math() %}
u(x, t) = Be^{-\beta \kappa t}(C \cos \beta x + D \sin \beta x)
{% end %}

Which we can write in a "prettier" way by defining $Q \equiv B \cdot C, P \equiv B \cdot D$, with which the solution becomes:

{% math() %}
u(x, t) = e^{-\beta \kappa t} (Q \cos \beta x + P \sin \beta x)
{% end %}

Now, we substitute in our boundary conditions $u(0, t) = 0$ and $u(L, t) = 0$. For the first boundary condition, our solution reduces to:

{% math() %}
\begin{align*}
u(0, t) &= e^{-\beta \kappa t} (Q \cancel{\cos (0)}^1 + \cancel{P \sin (0)}^0) \\
&= Q e^{-\beta \kappa t} \\
&= 0
\end{align*}
{% end %}

From which we deduce that $Q = 0$, and with which we are left with:

{% math() %}
u(x, t) = P \sin(\beta x)\,e^{-\beta \kappa t} 
{% end %}

For our other boundary condition $u(L, t) = 0$, we substitute to find:

{% math() %}
\begin{align*}
u(L, t) &= P \sin(\beta L) e^{-\beta \kappa t} \\
&= 0 \\
&\Rightarrow \sin \beta L = 0,\quad \beta L = n\pi
\end{align*}
{% end %}

Thus we find that $\beta = n\pi/L$, just as we did for the wave equation. Our solution now becomes:

{% math() %}
u(x, t) = P \sin\left(\dfrac{n\pi x}{L}\right) \exp\left(-\kappa\dfrac{n\pi t}{L}\right)
{% end %}

To satisfy the final boundary condition $u(x, 0) = \varphi(x)$, we again write our solution as a Fourier series:

{% math() %}
u(x, t) = \sum_{n = 1}^\infty P_n \sin\left(\dfrac{n\pi x}{L}\right) \exp\left(-\kappa\dfrac{n\pi t}{L}\right)
{% end %}

Thus, we can also write $\varphi(x)$ in terms of a series:

{% math() %}
u(x, 0) = \sum_{n = 1}^\infty A_n \sin\left(\dfrac{n\pi x}{L}\right) = \varphi(x)
{% end %}

And we find that, indeed, we have found the solution to the diffusion equation for the given boundary-value problem.

### The heat and wave equations with Neumann boundary conditions

We have seen how to solve the diffusion equation for zero Dirichlet boundary conditions, i.e. where $u(0, t) = u(L, t) = 0$. Let us now examine the more _general_ constant boundary conditions given by $\frac{\partial u}{\partial x}(0, t) = \frac{\partial u}{\partial x}(L, t) = 0$. Then the complete initial-boundary value problem for the diffusion equation becomes:

{% math() %}
\begin{gather*}
\dfrac{\partial u}{\partial t} = \kappa^2 \dfrac{\partial^2 u}{\partial x^2} \\
u(x, 0) = \psi(x) \\
\frac{\partial u}{\partial x}(0, t) = \frac{\partial u}{\partial x}(L, t) = 0
\end{gather*}
{% end %}

To start, we begin with the same method of separation of variables, which result in the following ODEs:

{% math() %}
\begin{align*}
T' &= -\beta^2\kappa^2 T \\
X'' &= -\beta^2 X
\end{align*}
{% end %}

Which have the general solutions:

{% math() %}
\begin{align*}
T(t) &= Je^{\beta \kappa t} + Ke^{-\beta \kappa t} \\
X(x) &= C \cos \beta x + D \sin \beta x
\end{align*}
{% end %}

From which we can find $u(x, t) = X(x)T(t)$:

{% math() %}
\begin{align*}
u(x, t) &= X(x)T(t) \\
&= (Je^{\beta \kappa t} + Ke^{-\beta \kappa t})(C \cos \beta x + D \sin \beta x)
\end{align*}
{% end %}

The time derivative of our solution is given by:

{% math() %}
\dfrac{\partial u}{\partial x} = (Je^{\beta \kappa t} + Ke^{-\beta \kappa t})\beta(D \cos \beta x - C \sin \beta x)
{% end %}

Let us start with the two (spatial) boundary conditions: $u(0, t) = A, u(L, t) = B$. For the first, setting $x = 0$, we have:

{% math() %}
\begin{align*}
\dfrac{\partial u}{\partial x}(0, t) = (Je^{\beta \kappa t} + Ke^{-\beta \kappa t})\beta D = 0 \\
\Rightarrow D = 0
\end{align*}
{% end %}

Thus our solution simplifies to:

{% math() %}
u(x, t) = (Je^{\beta \kappa t} + Ke^{-\beta \kappa t})\cos \beta x
{% end %}

Where we made the implicit transform $J = J \cdot C, K = K \cdot C$ to absorb in the constant $C$. This also means that the spatial derivative is now:

{% math() %}
\dfrac{\partial u}{\partial x} = (Je^{\beta \kappa t} + Ke^{-\beta \kappa t})(-\beta \sin \beta x)
{% end %}

So, setting $x = L$, we have:

{% math() %}
\begin{align*}
\dfrac{\partial u}{\partial x}(L, t) = (Je^{\beta \kappa t} + Ke^{-\beta \kappa t})(-\beta \sin \beta x) = 0 \\
\Rightarrow \beta = n\pi/L
\end{align*}
{% end %}

We therefore have:

{% math() %}
u(x, t) = (Je^{\beta \kappa t} + Ke^{-(n\pi/L) \kappa t})\cos \left(\dfrac{n\pi x}{L}\right)
{% end %}

Lastly, if we have $J \neq 0$, then the solution would grow exponentially large in time, which would be unphysical behavior. So we let $J = 0$, and thus our solution becomes:

{% math() %}
u(x, t) = Ke^{-(n\pi/L) \kappa t}\cos \left(\dfrac{n\pi x}{L}\right)
{% end %}

Which we can write in the most general form as a Fourier series, given by:

{% math() %}
u(x, t) = \sum_{n = 0}^\infty K_n e^{-(n\pi/L) \kappa t}\cos \left(\dfrac{n\pi x}{L}\right)
{% end %}

It is customary to "shift" the series to start from $n = 1$, like the solutions we previously found for Dirichlet boundary conditions. This does mean that we will need to include a constant-valued term at the front, giving the **solution to the heat equation** in its most general form for Neumann boundary conditions to be:

{% math() %}
u(x, t) = \dfrac{1}{2}K_0 + \sum_{n = 1}^\infty K_n e^{-(n\pi/L) \kappa t}\cos \left(\dfrac{n\pi x}{L}\right)
{% end %}

As a side note, we can perform the same to find the **solution of the wave equation** for Neumann boundary conditions, which comes out to be:

{% math() %}
\begin{align*}
u(x, t) &= \dfrac{1}{2} A_0 + \dfrac{1}{2}B_0 t \\
&\quad + \sum_{n = 1}^\infty \left(A_n \cos \dfrac{n\pi ct}{L} + B_n \sin \dfrac{n\pi ct}{L}\right)\cos \dfrac{n\pi x}{L}
\end{align*}
{% end %}

## Fourier series

Previously, we found that solutions to several boundary-value problems for the wave and diffusion equation could be written as a **series solution**. We also briefly mentioned that these series were called **Fourier series**. 

A Fourier series takes advantage of the fact that many sine and cosine waves can be added together to create a good approximation for a non-sinusoidal function. In theory, a Fourier series can be used to expand any periodic function in terms of sines and cosines. But - you may say - not all functions are periodic! While you are right, we can always expand a function across _one single period_ and disregard all of the others. For finite (spatial) boundary conditions in one dimension in which the function vanishes outside of $[-L, L]$, we can regard $[-L, L]$ as our only region of interest for the Fourier series expansion. A Fourier series defined over $[-L, L]$ takes the general form:

{% math() %}
f(x) = \dfrac{A_0}{2} + \sum_{n = 1}^\infty A_n \cos \dfrac{n\pi x}{L} + B_n \sin \dfrac{n\pi x}{L} 
{% end %}

Where the coefficients $A_n, B_n$ and $A_0$ are respectively given by:

{% math() %}
\begin{align*}
A_0 &= \dfrac{1}{L} \int_{-L}^L f(x)dx \\
A_n &= \dfrac{2}{L} \int_0^L f(x) \cos \dfrac{n\pi x}{L} dx \\
B_n &= \dfrac{2}{L} \int_0^L f(x) \sin \dfrac{n\pi x}{L} dx
\end{align*}
{% end %}

> **Note:** We must emphasize again that when using Fourier series for solving partial differential equations, we usually **only care** about the region $[0, L]$ and ignore the series for all other regions.

Such functions $f(x)$, as mentioned, often arise from the _initial conditions_ $u(x, 0) = f(x)$ and/or $\frac{\partial u}{\partial t}(x, 0) = g(x)$ defined over a finite boundary $[-L, L]$, and thus are very useful in expressing solutions to parabolic and hyperbolic PDEs, which commonly have these initial conditions. In addition, boundary-value problems that have _periodic_ boundary conditions also often require solutions in terms of Fourier expansions.

In some cases, it is possible to simplify the Fourier series into one of two simpler series. If $f(x)$ is an **even function** (symmetric about the $y$ axis), then the Fourier series reduces to the **cosine series**:

{% math() %}
\begin{align*}
f(x) = \dfrac{A_0}{2} + \sum_{n = 1}^\infty A_n \cos \dfrac{n\pi x}{L} \\
A_n = \dfrac{2}{L} \int_0^L f(x)\cos \dfrac{n\pi x}{L} dx
\end{align*}
{% end %}

Whereas if $f(x)$ is an **odd function** (symmetric about the origin, but "flipped" about the $y$ axis), then the Fourier series reduces to the **sine series**:

{% math() %}
\begin{align*}
f(x) &= \sum_{n = 1}^\infty B_n \sin \dfrac{n\pi x}{L} \\
B_n &= \dfrac{2}{L} \int_0^L f(x) \sin \dfrac{n\pi x}{L} dx
\end{align*}
{% end %}

We may also view this in another way: the complete Fourier series is a *combination* of the cosine and sine series that respectively describe even and odd parts of a function. Put together, the Fourier series is then able to describe the _complete_ function, which includes both the odd and even parts.

### The general theory of Fourier series

The Fourier series relies on the key property that over a finite interval $[-L, L]$, (nearly) any integrable function can be represented by a finite sum of sines and cosines. That is to say, (nearly) any function may be represented as an infinite series of the form:

{% math() %}
f(x) = \dfrac{A_0}{2} + \sum_{n = 1}^\infty \left[A_n \cos \dfrac{n\pi x}{L} + B_n \sin \dfrac{n\pi x}{L}\right]
{% end %}

What is important is that this is a **convergent series**, meaning that the equality is **exact**, not simply an approximation. And when we _are_ indeed interested in truncating the (infinite) series to a finite number of terms to get an approximate answer, we can calculate as many terms as necessary to achieve our desired accuracy.

To calculate the terms in the series it is necessary to have knowledge of $A_n, B_n$. Luckily, there is a straightforward means to do so. Let us integrate the function across the domain $[-L, L]$.

{% math() %}
\int_{-L}^L f(x)dx = \int_{-L}^L\dfrac{A_0}{2}dx + \int_{-L}^L\sum_{n = 1}^\infty \left[A_n \cos \dfrac{n\pi x}{L} + B_n \sin \dfrac{n\pi x}{L}\right] d x
{% end %}

Since $A_n$ and $B_n$ are constants that don't depend on $x$, we can factor them out of the integral:

{% math() %}
\int_{-L}^L f(x)dx = \int_{-L}^L\dfrac{A_0}{2}dx + \sum_{n = 1}^\infty \left[A_n\int_{-L}^L \cos \dfrac{n\pi x}{L}dx + B_n\int_{-L}^L \sin \dfrac{n\pi x}{L}dx\right] d x
{% end %}

We will now use the two very important properties of the sine and cosine functions, which comes from the even and odd identities of the sine and cosine. They are, respectively:

{% math() %}
\begin{gather*}
\int_{-L}^L \sin \dfrac{n\pi x}{L} dx = 0 \\
\int_{-L}^L \cos \dfrac{n\pi x}{L} dx = 0
\end{gather*}
{% end %}

This means that entire second term goes to zero, giving us:

{% math() %}
\begin{align*}
\int_{-L}^L f(x)dx &= \int_{-L}^L\dfrac{A_0}{2}dx + \cancel{\sum_{n = 1}^\infty \left[A_n\int_{-L}^L \cos \dfrac{n\pi x}{L}dx + B_n\int_{-L}^L \sin \dfrac{n\pi x}{L}dx\right] dx}^0 \\
&= \int_{-L}^L\dfrac{A_0}{2}dx \\
&= \dfrac{A_0}{2} (L - (-L)) \\
&= \dfrac{A_0}{2} (2L)  \\
&= A_0 L
\end{align*}
{% end %}

Therefore, rearranging yields an exact expression for $A_0$:

{% math() %}
A_0 = \dfrac{1}{L} \int_{-L}^L f(x)dx
{% end %}

To obtain $A_n$ and $B_n$, we use the integral identities:

{% math() %}
\begin{align*}
\int_{-L}^L \cos \dfrac{n\pi x}{L} \cos \dfrac{m\pi x}{L} dx &= \begin{cases}
L, & n = m, \text{ where } n, m \neq 0 \\
0, & n \neq m \\
2L, & n = m, n = m = 0 \\
\end{cases}  \\
\int_{-L}^L \cos \dfrac{n\pi x}{L} \sin \dfrac{m\pi x}{L} dx &= 0 \\
\int_{-L}^L \sin \dfrac{n\pi x}{L} \sin \dfrac{m\pi x}{L} dx &= \begin{cases}
1, & n = m \text{ where } n, m \neq 0 \\
0, & n \neq m
\end{cases}
\end{align*}
{% end %}

The $A_n$ coefficient can be found by multiplying $f(x)$ by $\cos \dfrac{m\pi x}{L}$ and integrating both sides. Upon then applying the integral identities, we have:

{% math() %}
\begin{align*}
f(x) &= \dfrac{A_0}{2} + \sum_{n = 1}^\infty \left[A_n \cos \dfrac{n\pi x}{L}  + B_n \sin \dfrac{n\pi x}{L}\right] \\
f(x) \cos \dfrac{m\pi x}{L} &= \dfrac{A_0}{2}\cos \dfrac{m\pi x}{L} + \sum_{n = 1}^\infty \bigg[A_n \cos \dfrac{n\pi x}{L}\cos \dfrac{m\pi x}{L} \\ &\qquad+ B_n \sin \dfrac{n\pi x}{L}\cos \dfrac{m\pi x}{L}\bigg] \\
\int_{-L}^L  f(x) \cos \dfrac{n\pi x}{L} dx &= \int_{-L}^L\dfrac{A_0}{2}dx + \sum_{n = 1}^\infty \bigg[A_n\int_{-L}^L \cos \dfrac{n\pi x}{L} \cos \dfrac{m\pi x}{L}dx \\
&\qquad + B_n\int_{-L}^L \sin \dfrac{n\pi x}{L}\cos \dfrac{m\pi x}{L}dx\bigg] dx \\
&= \cancel{\int_{-L}^L\dfrac{A_0}{2}dx}^0 + \sum_{n = 1}^\infty \bigg[A_n\int_{-L}^L \cos \dfrac{n\pi x}{L} \cos \dfrac{m\pi x}{L}dx \\
&\qquad + B_n\cancel{\int_{-L}^L \sin \dfrac{n\pi x}{L}\cos \dfrac{m\pi x}{L}dx}^0\bigg] dx \\
&= \sum_{n = 1}^\infty A_n\int_{-L}^L \cos \dfrac{n\pi x}{L} \cos \dfrac{m\pi x}{L}dx
\end{align*}
{% end %}

Notice that with the above trigonometric identities, since the integral of $\cos(n\pi x/L) \cos (m\pi x/L)$ is zero _unless_ $m = n$, all the terms in the infinite series collapse other than those for which $m = n$ (which evaluates to $L$ by our above integral identities). We ignore the case that $m = n = 0$ since our series sums from $n = 1$. In mathematical terms, since:

{% math() %}
\begin{align*}
A_n\int_{-L}^L \cos \dfrac{n\pi x}{L} \cos \dfrac{m\pi x}{L}dx &=
\begin{cases}
A_nL, & m = n \\
0, & m \neq n \\
\end{cases}
\end{align*}
{% end %}

Then it follows that the _only_ term in the series that is nonzero is the term for which $m = n$, and the series converges to:

{% math() %}
\begin{align*}
\sum_{n = 1}^\infty A_n\int_{-L}^L \cos \dfrac{n\pi x}{L} \cos \dfrac{m\pi x}{L}dx &= 0 + 0 + \dots + 0 + A_n L \\
&= A_n L
\end{align*}
{% end %}

But we know that above infinite series is _also_ equal to $\displaystyle \int_{-L}^L  f(x) \cos \dfrac{n\pi x}{L} dx$. Thus, we have:

{% math() %}
\begin{align*}
\int_{-L}^L  f(x) \cos \dfrac{n\pi x}{L} dx = A_n L \\
\Rightarrow A_n = \dfrac{1}{L} \int_{-L}^L f(x) \cos \dfrac{n\pi x}{L} dx
\end{align*}
{% end %}

Almost the exact same process can be used to find $B_n$: multiply $f(x)$ by $\sin \dfrac{n\pi x}{L}$, and then integrate both sides, leading to an infinite series that is all zero except for the term for which $n = m$, meaning it converges to zero. This process is what leads to the formulas:

{% math() %}
\begin{gather*}
A_n = \dfrac{1}{L} \int_{-L}^L f(x) \cos \dfrac{n\pi x}{L} dx \\
B_n = \dfrac{1}{L} \int_{-L}^L f(x) \sin \dfrac{n\pi x}{L} dx \\
\end{gather*}
{% end %}

### Even and odd functions

Having discussed the importance of a function's _parity_ (whether it is an even or odd function) for Fourier series, let us now take a more detailed look. Recall that even and odd functions are defined as follows:

- **Odd** functions satisfy $f(-x) = -f(x)$
- **Even** functions satisfy $g(x) = g(-x)$

Additionally, for Fourier series in particular, we are also interested in another _class_ of function:

- **Periodic** functions satisfy {% inlmath() %}h(x) = H(x\, \text{mod}\, 2L){% end %} (or more simply, $h(x) = h(x + 2L)$) where $2L$ is the **period** of the function

For Fourier series, we often want to _extend_ a function to make it even or odd across a symmetric interval. For instance, if we wanted to describe a triangle-shaped function, it would be natural to _extend_ the function $f(x) = x$ so that it is symmetric about the $y$-axis. The **even extension** of a function about $x = 0$ is given by:

{% math() %}
F_\text{even}(x) = \begin{cases}
F(x),& x > 0 \\
0, & x = 0 \\
F(-x),& x < 0
\end{cases}
{% end %}

Meanwhile, the **odd extension** of a function about $x = 0$ is given by:

{% math() %}
F_\text{odd}(x) = \begin{cases}
F(x), & x > 0 \\
0, & x = 0 \\
-F(-x), & x < 0
\end{cases}
{% end %}

In general, an *arbitrary* function can be decomposed into purely even and odd parts, as follows:

{% math() %}
\varphi(x) = \underbrace{\dfrac{1}{2}(\varphi(x) + \varphi(-x))}_\text{even part} + \underbrace{\dfrac{1}{2} (\varphi(x) - \varphi(-x))}_\text{odd part}
{% end %}

### Complex form of the Fourier Series

We have extensively discussed the Fourier Series in its most conventional trigonometric form, as an infinite sum of sines and cosines. But there is also an _alternative_ form of the Fourier series, expressed using complex-valued functions. To show why this is the case, recall **Euler's formula**, which relates sinusoids to complex exponential functions:

{% math() %}
e^{i\phi} = \cos \phi + i \sin \phi
{% end %}

Euler's formula leads to following _complex-valued_ definitions for the sine and cosine:

{% math() %}
\begin{matrix*}
\cos \phi = \dfrac{e^{i\phi} + e^{-i\phi}}{2}, & \sin \phi = \dfrac{e^{i\phi} - e^{-i\phi}}{2i}
\end{matrix*}
{% end %}

Using these formulas allows us to find the **complex form** of the Fourier Series, given by:

{% math() %}
\begin{gather*}
f(x) = \sum_{n = -\infty}^\infty C_n \exp \left(i\dfrac{n\pi x}{L}\right), \\
C_n = \dfrac{1}{2L} \int_{-L}^L f(x) \exp \left(-i\dfrac{n\pi x}{L}\right)
\end{gather*}
{% end %}

> **Note:** If $f(x)$ is a **real-valued** function, then its Fourier series representation must have coefficients that satisfy $C_n = C_{-n}^*$, where the asterisk represents the complex conjugate.

The complex form of the Fourier series has a number of advantages over the conventional trigonometric form. First, one needs to only compute one coefficient ($C_n$) rather than three ($A_0, A_n, B_n$). In addition, the unique properties of the exponential function, given that it follows the  properties of exponents and has a very simple derivative (and integral), make it much easier to work with. So, it is often preferred over the trigonometric form. For instance, let us compute the coefficients $C_n$ of the exponential function $f(x) = e^x$. We have:

{% math() %}
\begin{align*}
C_n &= \dfrac{1}{2L} \int_{-L}^L f(x) \exp \left(-i\dfrac{n\pi x}{L}\right) \\
&= \dfrac{1}{2} \int_{-1}^1 e^x e^{-i (n\pi x)} dx \\
&= \dfrac{1}{2} \int_{-1}^1 \exp(x(1 - i\pi n)) dx \\
&= \dfrac{1}{2}\left[\dfrac{\exp(x(1 - in\pi))}{1- in\pi}\right]_{-1}^1 \\
&= \dfrac{1}{2} \dfrac{\exp(1 - i n\pi) - \exp(in\pi - 1)}{1 - in\pi} \\
&= \dfrac{\sinh(1 - in\pi)}{1-in\pi}
\end{align*}
{% end %}

Note how the integrals are significantly easier, and in addition, we only needed to solve for one single coefficient $C_n$. But the complex form still carries the same information as the real-valued sinusoidal form; for all real-valued functions, the complex form of the Fourier series (which we will call from this point on as just the "complex form") provides the same information as the sinusoidal form of the Fourier series we have seen so far. In fact, the coefficients $C_n$ in the complex form of the Fourier series can be _directly related_ to the coefficients $A_0, A_n, B_n$ in the trigonometric form:

{% math() %}
C_n = \begin{cases}
\dfrac{A_0}{2}, n = 0 \\
\frac{1}{2}(A_n + B_n), & n = 1, 2, 3, \dots \\
\dfrac{1}{2}(A_n - B_n), & n = -1, -2, -3, \dots
\end{cases}
{% end %}

### Orthogonality and general Fourier Series

The Fourier series written in terms of sines and cosines is not the most general expression of the Fourier series. This is because while we picked sine and cosine to be our basis functions for our Fourier series (or complex exponentials for the generalization to complex-valued functions), _any_ set of orthogonal bases can be expressed as a linear superposition of any other set. For instance, consider the basis of _Legendre polynomials_. These polynomials form a complete, orthogonal set of bases; the first few Legendre polynomials take the form:

{% math() %}
\begin{align*}
P_0(x) &= 1 \\
P_1(x) &= x \\
P_2(x) &= \dfrac{3x^2 - 1}{2} \\
P_3(x) &= \dfrac{5x^3 - 3x}{2} \\
P_4(x) &= \dfrac{35 x^4 - 30x^2 +3}{8} \\
P_5(x) &= \dfrac{63x^5 - 70x^3 + 15x}{8}
\end{align*}
{% end %}

The crucial property of the Legendre polynomials, which allows them to form an orthogonal basis, is their _orthogonality relation_:

{% math() %}
\int_{-1}^1 P_\ell(x) P_{\ell'}(x) dx = \dfrac{2}{2\ell + 1} \delta_{\ell' \ell} =\begin{cases}
0, & \ell \neq \ell' \\
\dfrac{2}{2\ell + 1}, & \ell = \ell'
\end{cases} 
{% end %}

In general, the bases of all Fourier series (including sine series, cosine series, full trigonometric series & complex exponential form) are _all_ orthogonal, and therefore we can interchange them freely by a change of basis. For this, we write one basis as a linear superposition of the basis functions of another basis. For instance, for the Legendre polynomials, we may write:

{% math() %}
\sin(n\pi x) = \sum_{\ell = 1}^\infty A_\ell P_\ell(x)
{% end %}

More general Fourier series can be composed from *any* orthogonal functional basis, which include the Chebyshev polynomials, Laguerre polynomials, Legendre polynomials, spherical harmonics, and other special functions that possess the properties of **orthogonality** and **completeness**. For some arbitrary functional basis $Y_n(x)$, we may therefore express a given function $f(x)$ in series form as:

{% math() %}
f(x) = \sum_{n = 1}^\infty A_n Y_n(x)
{% end %}

And because of orthogonality it must be the case that:

{% math() %}
\int_a^b f(x) Y_m^*(x)dx = \int_a^b \sum_{n = 1}^\infty A_n Y_n(x) Y_m^*(x) dx = A_m \int_a^b |Y_m(x)|^2 dx
{% end %}

Therefore, we have a straightforward, if tedious, way to find any coefficient $A_m$. Indeed, _if_ the functional basis is also _orthonormal_, meaning that on an interval $[a, b]$ it obeys $N = \displaystyle \int_a^b |Y_m(x)|^2 dx = 1$, then the expression for $A_m$ becomes simply:

{% math() %}
A_m = \int_a^b f(x) Y_m^*(x)dx
{% end %}

Whereas if the functional basis is not orthonormal, we simply divide by $N$, to have:

{% math() %}
A_m = \dfrac{1}{N}\int_a^b f(x) Y_m^*(x)dx
{% end %}

As we can see, Fourier series are not limited to sinusoids. Using the more general form of the Fourier series allows us to express nearly _any_ function as a series expansion in any functional basis of our choice, making them extremely powerful mathematical tools.

## Next steps

We've reached the end of the second part of the PDEs guide. Now is the time to continue to [the final part](@/intro-pdes/chapter-3.md)!