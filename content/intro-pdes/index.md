+++
title = "A Gentle Guide to Partial Differential Equations"
date = 2025-01-14
+++

This is a short guide/mini-book on introducing various topics in partial differential equations, including analytical methods of finding solutions, boundary-value problems, and discussions of widely-known PDEs.

<!-- more -->

This guide is dedicated to [Professor Yuri Lvov](https://faculty.rpi.edu/yuri-lvov) of Rensselaer Polytechnic Institute, who teaches the course on which this guide is based, and to whom I am greatly thankful. They are freely-sharable and released to the public domain. This guide also closely follows the book _Partial Differential Equations, 2nd. Ed._ by Walter A. Strauss, which is highly recommended for following on while reading the guide.

Note: familiarity with vector calculus and ordinary differential equations is assumed. Full length guides for both are available if a refresher is needed; they can be found on the [vector calculus guide](@/vector-and-advanced-calculus/index.md) and the [introduction to differential equations](@/differential-equations/index.md).


## Introduction to partial differential equations

A partial differential equation (PDE) is an equation that describes a function of _several variables_ in terms of its _partial derivatives_. For instance, let $u(x, y, z, \dots)$ be an arbitrary function of several variables; a PDE takes the form:

{% math() %}
F\left(u, \nabla u, \nabla^2u, \dfrac{\partial u}{\partial x_i \partial x_j}\right) = g(\mathbf{r})
{% end %}

A few of the most well-known partial differential equations are listed in the table below:

| PDE name                         | Mathematical form                                                                                                                              |
| -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| 1D heat equation                 | $\dfrac{\partial u}{\partial t} = \alpha^2 \dfrac{\partial^2 u}{\partial x^2}$                                                                 |
| 1D transport equation            | $\dfrac{\partial u}{\partial t} + c\dfrac{\partial u}{\partial x} = 0$                                                                         |
| 1D inviscid Burger's equation    | $\dfrac{\partial u}{\partial t} + u \dfrac{\partial u}{\partial x} = 0$                                                                        |
| 1D viscous Burger's equation     | $\dfrac{\partial u}{\partial t} + u\dfrac{\partial u}{\partial x} = \nu \dfrac{\partial^2 u}{\partial x^2}$                                    |
| 1D Wave equation                 | $\dfrac{\partial^2 u}{\partial t^2} = c^2 \dfrac{\partial^2 u}{\partial x^2}$                                                                  |
| Korteweg–De Vries (KdV) equation | $\dfrac{\partial u}{\partial t} + \dfrac{\partial^3 u}{\partial x^3} - 6 u \dfrac{\partial u}{\partial x} = 0$                                 |
| 2D Laplace's equation            | $\dfrac{\partial^2 u}{\partial x^2} + \dfrac{\partial^2 u}{\partial y^2} = 0$                                                                  |
| 3D Laplace's equation            | $\dfrac{\partial^2 u}{\partial x^2} + \dfrac{\partial^2 u}{\partial y^2} + \dfrac{\partial^2 u}{\partial z^2} = 0$                             |
| Incompressible Euler equations   | $\dfrac{\partial u}{\partial t} + (\mathbf{u} \cdot \nabla) \mathbf{u} + \dfrac{1}{\rho} \nabla p = \mathbf{g}$, $\nabla \cdot \mathbf{u} = 0$ |

We want to solve PDEs because they provide _mathematical descriptions_ which allow us to understand the dynamics of a physical system. The processes of solving and analyzing PDEs are the focus of this guide.

### Linearity

A crucial distinction that must be made before attempting any solution of a PDE is whether it is _linear_ or _nonlinear_. A linear PDE has _no terms involving its unknown function_ multiplied to partial derivatives, and only _linear terms involving its unknown function_ anywhere else. For instance, consider the PDE shown:

{% math() %}
x \dfrac{\partial u}{\partial x} = y \dfrac{\partial u}{\partial y} + 3u
{% end %}
It may be illuminating to write it in expanded form:

{% math() %}
x\dfrac{\partial u(x, y)}{\partial x} = y\dfrac{\partial u(x, y)}{\partial y}+ 3u(x, y)
{% end %}

Notice that the PDE consists of an unknown function $u(x, y)$. On each of the derivatives, there is _no term_ involving $u$. The _only_ time $u(x, y)$ appears is the term $3u(x, y)$ (which is not multiplied to a derivative, and is linear in form). We therefore say that the PDE is **linear.** All of the following cases are similarly linear:

| Linear modification                                                                | Reason for linearity                                                                                                                               |
| ---------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| $x^2 \dfrac{\partial u}{\partial x} = xy \dfrac{\partial u}{\partial y} + 3 u$     | Only terms involving $u$ (the unknown function) matter when analyzing linearity; any terms in $x, y$, etc. don't matter                            |
| $x \dfrac{\partial u}{\partial x} = y \dfrac{\partial u}{\partial y} + (1 - x^2)u$ | Same; only terms involving $u$ matter when analyzing linearity, so the $1 - x^2$ factor does not change the linearity of the differential equation |
| $x \dfrac{\partial^2 u}{\partial x^2} = y \dfrac{\partial u}{\partial y} + 3u$     | It doesn't matter whether the partial derivatives are first derivatives, second-derivatives, nth-derivatives, etc.                                 |

By contrast, _any_ of the following cases are nonlinear:

| Nonlinear modification                                                                      | Reason for nonlinearity                                                                    |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| $u \dfrac{\partial u}{\partial x} = y \dfrac{\partial u}{\partial y} + 3u$                  | There is a term in $u$ multiplied to the first derivative $\dfrac{\partial u}{\partial x}$ |
| $x \dfrac{\partial u}{\partial x} = y \dfrac{\partial u}{\partial y} + 3u^2$                | There is a squared term in $u$ (the $u^2$ term) which is not a linear term                 |
| $u x \dfrac{\partial u}{\partial x} = y \dfrac{\partial u}{\partial y} + 3\cos(u)$          | Both a term in $u$ on one of the derivatives and a nonlinear term in $u$                   |
| $\left(x \dfrac{\partial u}{\partial x}\right)^3 = y \dfrac{\partial u}{\partial y} + 3u^2$ | Taking powers of derivatives makes a PDE nonlinear                                         |

Linear differential equations allow us to write a PDE in terms of a **linear differential operator**, denoted $\mathcal{L}$. For instance, consider the heat equation:

{% math() %}
\dfrac{\partial u}{\partial t} = \alpha^2 \dfrac{\partial^2 u}{\partial x^2}
{% end %}

We note that we can rewrite the heat equation as follows:

{% math() %}
\left(\dfrac{\partial}{\partial t} - \alpha^2 \dfrac{\partial^2}{\partial x^2}\right) u(x, t) = 0
{% end %}

The quantity in the brackets on the left-hand side of the equation is the _linear operator_. If we let:

{% math() %}
\mathcal{L} = \left(\dfrac{\partial}{\partial t} - \alpha^2 \dfrac{\partial^2}{\partial x^2}\right)
{% end %}

Then we may write the heat equation as $\mathcal{L} u = 0$. As $\mathcal{L}$ is a linear operator, it has the properties that for two solutions $u$ and $v$ and a constant $c$, $\mathcal{L}(c u) = c\mathcal{L}u$ and $\mathcal{L}(u + v) = \mathcal{L}(u) + \mathcal{L}(v)$. Linearity means that any _sum of two solutions is a solution_ to a PDE, so it is possible to write a _general solution_ as:

{% math() %}
u(x, t) = \sum_n c_n u_n(x, t)
{% end %}

### Homogeneity

Linear PDEs can further be divided into two main types: _homogenous_ linear PDEs, which take the form $\mathcal{L} u = 0$, or *inhomogenous* (also called _nonhomogenous_) linear PDEs, which take the form $\mathcal{L} u = f(\mathbf{x})$. That is to say, roughly speaking, if one rearranges a linear PDE such that every term involving derivatives is moved to the left-hand side, then the right-hand side will be zero for homogenous PDEs and some function $f(\mathbf{x})$ for inhomogenous PDEs.

For instance, the following PDE is a _homogenous_ linear PDE:

{% math() %}
\dfrac{\partial^2 u}{\partial x^2} + \dfrac{\partial^2 u}{\partial y^2} = 0
{% end %}

Whereas the following PDE is an _inhomogenous_ linear PDE:

{% math() %}
\dfrac{\partial^2 u}{\partial x^2} + \dfrac{\partial^2 u}{\partial y^2} = k^2 u
{% end %}

Note how in both cases, all the terms involving derivatives have been moved over to the left-hand side of the equation, and the value of the right-hand side of the equation determines the *homogeneity* (whether the equation is homogeneous or inhomogeneous).

### Solving by direct integration

Without any additional knowledge, we may begin our study of PDEs by examining the _direct integration_ approach, which is applicable to a few very simple PDEs. Consider, for instance, the following PDE:

{% math() %}
\dfrac{\partial^2 u}{\partial x^2} = 0
{% end %}

If we take the partial integral once with respect to $x$ twice, we have:

{% math() %}
\begin{align*}
u(x, y) &=\iint\left( \dfrac{\partial^2 u}{\partial x^2} + u \right) dx \\
&= \iint 0 \, dx \\
&= \int 0 + A(y) \, dy \\
&= x A(y) + B(y)
\end{align*}
{% end %}

Thus our general solution is:

{% math() %}
u(x, y)= x A(y) + B(y)
{% end %}

The reason for why the general solution contains two functions of $y$, namely $A(y)$ and $B(y)$, is because we are performing _partial integration_ since this is a _partial_ differential equation. Thus, the constants of integration are actually _functions_ $A(y)$ and $B(y)$, these can be _arbitrary_ functions of $y$. For instance, the following are **all** valid solutions to our PDE:

{% math() %}
\begin{gather*}
u(x, y) = 3xy + 5y^2 \\
u(x, y) = x \cos y + e^y \sin y \\
u(x, y) = x \ln y + y^2(5 + 3y)^{3/2} \\
u(x, y) = 0
\end{gather*}
{% end %}

Similarly, consider the PDE:

{% math() %}
\dfrac{\partial^2 u}{\partial x^2} + k^2 u = 0
{% end %}

The general solution is given by $u(x, y) = A(y) \sin k x + B(y) \cos k x$, which means that all of the following are _also_ solutions:

{% math() %}
\begin{gather*}
u(x, y) = 3y^2 \sin kx + \sqrt{y-4} \cos k x \\
u(x, y) = \dfrac{5}{y} \sin kx + 574y^3 \cos k x \\
u(x, y) = y^{1/4} \cos k x \\
u(x, y) = \sin k x
\end{gather*}
{% end %}

The sheer diversity of solutions - and yes, **all** of these are valid solutions - means that finding general solutions is not very useful when solving PDEs, since there are always degrees of freedom from the arbitrary functions that could make the particular solution _very, very different_. Therefore, we usually need to specify **boundary conditions**, specific mathematical requirements that PDEs must satisfy on a particular domain, to find a unique (and useful) solution.

### Boundary conditions

As we have seen, when solving PDEs, one must be careful to recognize that a general solution to a PDE does not uniquely specify the solution to a given physical scenario. A particular solution (which is usually synonymous with _unique solution_) can only be found if one additionally requires that the solution take a certain value at the boundaries of the PDE's domain.

Let us consider an example. Consider solving Laplace's equation $\dfrac{\partial^2 u}{\partial x^2} = \dfrac{\partial^2 u}{\partial y^2} = 0$ on a **unit square**, i.e. the domain defined by $0 \leq x \leq 1, 0\leq y \leq 1$. We will call this domain $\Omega$. The _boundary_ of the domain would be the perimeter of the unit square. We will call this boundary $\partial \Omega$ for "boundary of $\Omega$". 

A boundary condition for finding a unique equation to Laplace's equation could be specifiying that:

{% math() %}
u(x, y) \big |_{\partial \Omega} = C
{% end %}

This means that $u(x, y) = C$ at all points along the boundary (which is the perimeter of the unit square). Using this information, the PDE can be solved for exactly, and a (much more useful) _unique_ solution can be found.

## Separation of variables

For any PDE more complex than the most basic examples, direct integration no longer suffices. Another technique is necessary to tackle these more complicated PDEs, and this is the method of **separation of variables**.

To demonstrate this method, let us consider the **wave equation**:

{% math() %}
\dfrac{\partial^2 u}{\partial t^2} = c^2 \dfrac{\partial^2 u}{\partial x^2}
{% end %}

When performing the separation of variables, we first assume that the solution $u(x, t)$ may be written as a product of two functions _of a single variable_, which we will call $v(t)$ and $w(x)$. That is:

{% math() %}
u(x, t) = w(x) v(t)
{% end %}

In this form, we are able to take the partial derivatives explicitly:

{% math() %}
\begin{align*}
\dfrac{\partial^2 u}{\partial t^2} = \dfrac{\partial^2}{\partial t^2} w(x) v(t) = w(x)\dfrac{d^2v}{dt^2} \\
\dfrac{\partial^2 u}{\partial x^2} = \dfrac{\partial^2}{\partial x^2} w(x) v(t) = v(t) \dfrac{d^2w}{dx^2}
\end{align*}
{% end %}

By substitution of these partial derivatives into the wave equation we have:

{% math() %}
w(x)\dfrac{d^2v}{dt^2} = c^2 v(t) \dfrac{d^2w}{dx^2}
{% end %}

If we divide by $c^2 w(x) v(t)$ from both sides, we have:

{% math() %}
\begin{gather*}
\dfrac{1}{c^2 w(x)v(t)}w(x)\dfrac{d^2v}{dt^2} = \dfrac{1}{c^2 w(x)v(t)}c^2 v(t) \dfrac{d^2w}{dx^2} \\
\dfrac{1}{c^2 v(t)}\dfrac{d^2v}{dt^2} = \dfrac{1}{w(x)}\dfrac{d^2w}{dx^2}
\end{gather*}
{% end %}

We now have an expression with only $t$ and derivatives of $t$ on the left-hand side and only $x$ and derivatives of $x$ on the right-hand side. This is only possible if both expressions are equal to an **arbitrary constant** $k^2$, called the _separation constant_ (we could just as well choose $k$ or $s$ or $a$ but this form simplifies the mathematical analysis later on). So now we have _separated_ the variables and are left with two _ordinary_ differential equations:

{% math() %}
\begin{align*}
\dfrac{1}{c^2 v(t)}\dfrac{d^2v}{dt^2} &= k^2 \\
\dfrac{1}{w(x)}\dfrac{d^2w}{dx^2} &= k^2
\end{align*}
{% end %}

These can be written in more traditional form as:

{% math() %}
\begin{align*}
\dfrac{d^2 v}{dt^2} &= k^2 c^2 v \\
\dfrac{d^2 w}{dx^2} &= k^2 w
\end{align*}
{% end %}

Which have the general solutions:

{% math() %}
\begin{align*}
v(t) = A_1\cos(k c t) + B_1 \sin (k c t) \\
w(x) = A_2 \cos(kx ) + B_2 \sin (kx)
\end{align*}
{% end %}

Where $A_1, A_2, B_1, B_2$ are undetermined constants that can be solved for by applying the boundary conditions. It is common to write $\omega \equiv kc$ (the greek letter omega, not to be confused with $w$) to simplify the equations: 

{% math() %}
\begin{align*}
v(t) = A_1\cos(\omega t) + B_1 \sin (\omega t) \\
w(x) = A_2 \cos(kx ) + B_2 \sin (kx)
\end{align*}
{% end %}

So the general solution to the wave equation is:

{% math() %}
u(x, t) = w(x) v(t) = (A_2 \cos(kx ) + B_2 \sin (kx))(A_1\cos(\omega t) + B_1 \sin (\omega t))
{% end %}

This can be simplified further using trigonometric identities, and is the end result of our successful separation of variables.

> **Note:** In many cases, a PDE may be separable in one coordinate system and _not_ separable in another. This is famously the case for the Schrödinger equation, which is an inhomogeneous linear PDE; when its inhomogeneous term is a term that is proportional to $\dfrac{1}{r}$, as is the case for many atomic solutions, then the Schrödinger equation is no longer separable in Cartesian coordinates, but _remains separable_ in _spherical_ coordinates.

## Useful calculus identities for PDEs

By nature of partial differentiation, there are several results that are incredibly crucial for the study of PDEs. First, the _order of differentiation_ does not matter. That is to say:

{% math() %}
\dfrac{\partial^2 f}{\partial x \partial y} = \dfrac{\partial^2 f}{\partial y \partial x}
{% end %}

Second, integration and partial differentiation can (in some cases) be order-swapped:

{% math() %}
\dfrac{d}{dt} \int_{x=a}^{x=b} f(x, t) dx = \int_{x=a}^{x=b} \dfrac{\partial}{\partial t} f(x, t) dx
{% end %}

This is known as the **Leibnitz rule**. Note that when applying the Leibnitz rule, it is important to recognize that the above rule applies _only_ in the case of **definite integrals** where $f(x, t)$ is integrated over $x$. Notice that integrating $f(x, t)$ over bounds in $x$ results in a new function we may call $G(t)$ that is purely in terms of $t$, by the Fundmental Theorem of Calculus:

{% math() %}
\int_{x=a}^{x=b} f(x, t) dx = F(b, t) - F(a, t) = G(t)
{% end %}

Therefore, we write $\dfrac{d}{dt}$ for the left-hand-side integral, as $G(t)$ is only in terms of $t$, whereas we write $\dfrac{\partial}{\partial t}$ for the right-hand-side integral, as $f(x, t)$ is in terms of both $x$ and $t$. In the more general form, where $a = a(t)$ and $b = b(t)$ rather than constants, we have:

{% math() %}
\dfrac{d}{dt} \int_{x=a(t)}^{x=b(t)} f(x, t) dx = f(b, t) \dfrac{db}{dt} - f(a, t) \dfrac{da}{dt}  + \int_{x=a(t)}^{x=b(t)} \dfrac{\partial}{\partial t} f(x, t) dx
{% end %}

Another very useful relationship used extensively in studying PDEs is the divergence theorem, which relates the volume integral of the _divergence_ of a vector-valued function over a volume $\Omega$ to its surface integral across the _boundary surface_ of $\Omega$, written $\partial \Omega$:

{% math() %}
\oiint \limits_{\partial \Omega} \mathbf{F} \cdot d\mathbf{A} = \iiint \limits_\Omega (\nabla \cdot \mathbf{F})\, dV
{% end %}

Note that this can also be written with slightly different but mathematically-equivalent notation as:

{% math() %}
\oint \limits_{\partial \Omega} \mathbf{F} \cdot d\mathbf{A} = \int \limits_\Omega (\nabla \cdot \mathbf{F})\, dV
{% end %}

That is to say, the number of integral signs does not matter, that is a notational choice; only the integration variables ($d\mathbf{A}$ and $dV$) matter. However, the multiple-integral notation often used since it is sometimes more illustrative to write a volume integral with triple integral signs to signify it is computed over a three-dimensional volume, and a surface integral with double integral signs to signify it is computed over a two-dimensional surface.

From the divergence theorem, it is possible to derive the **vanishing theorem**:

{% math() %}
\begin{matrix*}
\displaystyle \iiint \limits_\Omega F(\mathbf{r})\, dV = 0& \Leftrightarrow &F(\mathbf{r}) = 0
\end{matrix*}
{% end %}

## Solutions to 1st-order linear PDEs

Up to this point, we have discussed two methods of solving PDEs: direct integration and separation of variables. We will now examine a few more ways to solve PDEs of a specific form: first-order linear PDEs.

### Solving for homogenous vs. inhomogenous PDEs

Before we actually solve a PDE, it is important to first identify whther it is _homogenous_, _inhomogenous_, or _neither_. Consider a linear differential operator $\mathcal{L}$, similar to the ones we have already studied. A **solution** to a homogenous linear PDE is a function $u(x, y, z)$ that satisfies:

{% math() %}
\mathcal{L}u = 0
{% end %}

For an *inhomogenous* linear PDE in the form $\mathcal{L}u = f(\mathbf{x})$, the general solution $u(x, y, z)$ to the PDE is a combination of the *general solution* $u_0$ to the corresponding _homogenous_ PDE $\mathcal{L}u_0 = 0$ and the *particular solution* $u_1$ to the *inhomogenous* PDE $\mathcal{L} u_1 = f(\mathbf{x})$. That is:

{% math() %}
u = u_0 + u_1
{% end %}

In simpler terms, to solve for the **general solution** to a inhomogenous linear PDE $\mathcal{L} u = f(\mathbf{x})$ (e.g., $\left(\dfrac{\partial}{\partial x} + \dfrac{\partial}{\partial y}\right)u = f(x, y)$ where $\mathcal{L} = \left(\dfrac{\partial}{\partial x} + \dfrac{\partial}{\partial y}\right)$:

- First, you solve for the *general* solution to its homogenous version $\mathcal{L} u = 0$, which we'll call $u_0$. In our case, it would be equivalent to finding the general solution to $\left(\dfrac{\partial}{\partial x} + \dfrac{\partial}{\partial y}\right)u = 0$
- Then, you find _any_ solution to its inhomogenous version, which we'll call $u_1$. In our case, it would be equivalent to finding the _particular_ solution to $\left(\dfrac{\partial}{\partial x} + \dfrac{\partial}{\partial y}\right) u = f(x, y)$ 
- Finally, you add $u_0$ and $u_1$ together. This gives you the *general* solution to the inhomogeneous PDE $u(x, y) = u_0(x, y) + u_1(x, y)$

### The method of characteristics

The method of characteristics is a technique to solve first-order linear PDEs. We will first overview the simplest case, where we additionally require that the PDE is _homogenous_ and has _constant coefficients_ That is, we consider PDEs similar to the _transport equation_:

{% math() %}
a \dfrac{\partial u}{\partial x} + b \dfrac{\partial u}{\partial y}  = 0
{% end %}

Note that this may be cast in an _alternative form_ (this will be important later) given by:

{% math() %}
\dfrac{\partial u}{\partial x} + \dfrac{b}{a} \dfrac{\partial u}{\partial y} = 0
{% end %}

To solve this PDE, we use a geometric argument from vector calculus. Recall that the directional derivative $\nabla_\mathbf{v} u$ is given by:

{% math() %}
\begin{align*}
\nabla_\mathbf{v} u &= \nabla u \cdot \mathbf{v} \\
&= v_x \dfrac{\partial u}{\partial x} + v_y \dfrac{\partial u}{\partial y}
\end{align*}
{% end %}

We can therefore _reinterpret_ the transport PDE $a \dfrac{\partial u}{\partial x} + b \dfrac{\partial u}{\partial y}  = 0$ as the equation of a directional derivative $v_x \dfrac{\partial u}{\partial x} + v_y \dfrac{\partial u}{\partial y}$, such that $a, b$ are the components of a vector $\mathbf{v}$, and $v_x = a, v_y = b$. Therefore, the transport equation reduces to:

{% math() %}
\nabla_\mathbf{v} u = \nabla u \cdot \langle a, b\rangle = 0
{% end %}

Notice how this equation is equivalent to saying that _the directional derivative of $u$ along the vector $\mathbf{v} = \langle a, b\rangle$ is zero_. This means that $u(x, y)$ _does not change_ along $\mathbf{v}$, and thus for all points $(x, y)$ along the direction $\mathbf{v}$, $u(x, y)$ must be equal to a constant $C$, or more generally, some function of a constant $f(C)$ (because if $C$ is a constant, then $f(C)$ is _also_ a constant). 

The curves traced by the collection of these points $(x, y)$ are known as **characteristic curves** (sometimes also called _integral curves_). Each curve would mathematically take the form $(x, y(x))$, where $y$ is some function of $x$, so the solution $u(x, y)$ can be found by just substituting in $y(x)$ to have $u(x, y(x))$. Therefore, once we can determine the expression for the characteristic curve $y(x)$, we know the solution $u(x, y)$. Thus the method of characteristics *reduces* the problem of solving a PDE into a problem of finding the *characteristic curves* $y(x)$ along which $u(x, y) = \text{const.}$

But how do we go about finding $y(x)$? Let us consider moving along $u(x, y)$ following a characteristic curve $y(x)$. Since $u(x, y) = \text{const.}$ along the characteristic curve, we know that $\dfrac{du}{dx} = 0$. But we also know that we may expand $\dfrac{du}{dx}$ using the chain rule to have:

{% math() %}
\dfrac{du}{dx} = \frac{\partial u}{\partial x} + \dfrac{\partial u}{\partial y}\dfrac{dy}{dx} = 0
{% end %}

If we compare this with the alternate form (given previously) of our PDE:

{% math() %}
\dfrac{\partial u}{\partial x} + \dfrac{b}{a} \dfrac{\partial u}{\partial y} = 0
{% end %}

We immediately notice that $\dfrac{b}{a} = \dfrac{dy}{dx}$, then:

{% math() %}
\dfrac{du}{dx} = \dfrac{\partial u}{\partial x} + \dfrac{b}{a} \dfrac{\partial u}{\partial y}
{% end %}

Which perfectly matches our PDE! Thus we have reduced the PDE to a problem of finding the characteristic curves $y(x)$. To be able to solve for the characteristic curves, we need only solve the system of _ordinary_ differential equations we have derived:

{% math() %}
\begin{align*}
\dfrac{du}{dx} = 0 \\
\dfrac{dy}{dx} = \dfrac{b}{a}
\end{align*}
{% end %}

The second differential equation has the straightforward solution, by inspection, of $y(x) = \dfrac{b}{a}x + c$, where $c$ is some arbitrary constant of integration. For the first differential equation, however, we must be more careful, because $\dfrac{du}{dx} = \dfrac{du(x, y)}{dx}$ is a _total derivative_ of the multivariable function $u(x, y)$. Therefore, we must perform _partial integration_:

{% math() %}
\begin{align*}
\dfrac{du}{dx} &= 0 \\
\dfrac{du(x, y)}{dx} &= 0 \\
\int \dfrac{du(x, y)}{dx}\, dx &= \int 0\, dx \\
u(x, y) &= F(y)
\end{align*}
{% end %}

> Notice here that instead of a _constant_ of integration, we have an arbitrary _function_ of integration $F(y)$, since we are taking the **partial integral**.

Now, let us recall that since $u(x, y) = \text{const.}$ for *all points along the characteristic curve*, then this must be true for the point $(0, y(0))$ as well, meaning that $u(x, y) = u(0, y(0)) = \text{const.}$ Therefore:

{% math() %}
\begin{matrix*}
&x = 0& \Rightarrow & y = \cancel{\dfrac{b}{a} x} + c & \Rightarrow & y=c
\end{matrix*}
{% end %}

By substitution into $u(x, y) = F(y)$, we have:

{% math() %}
\begin{gather*}
u(0, y(0))= F(y) = F(c) \\
u(x, y) = u(0, y(0)) = F(c) \\
\end{gather*}
{% end %}

But we know that $y(x) = \dfrac{b}{a}x + c$, which we can rearrange to $y - \dfrac{b}{a} x = c$. Therefore:

{% math() %}
u(x, y) = F(c) = F\left(y - \dfrac{b}{a}x\right)
{% end %}

Since $F$ is a completely arbitrary function, we can define a new (and also arbitrary) function $f(s) = F(-s/a)$, where $s = y - \dfrac{b}{a}x$ (here $s$ is a substitution variable). Thus we have:

{% math() %}
f(bx - ay) = F\left(-\dfrac{1}{a}(bx - ay)\right) =  F\left(y - \dfrac{b}{a}x\right)
{% end %}

So that we may write our *generalized* solution as:

{% math() %}
u(x, y) = f(bx - ay)
{% end %}

This is a _general solution_, meaning that $f$ is a yet-to-be determined function and substituting in provided boundary conditions is necessary to determine the exact expression for $f$.

> **Note:** An important theme when studying general solutions of PDEs is to remember that arbitrary compositions of arbitrary functions _make no difference in writing the general solution to a PDE_, just like the addition of a different constant of integration makes no difference to the general solution to an ODE. The choice of arbitrary function is purely stylistic, since the solution to a PDE **cannot** be determined without provided boundary and initial conditions.

We may verify that our general solution is indeed a solution to our PDE $a \dfrac{\partial u}{\partial x} + b \dfrac{\partial u}{\partial y}  = 0$ by taking the derivatives of $u$ and substituting them back into our PDE:

{% math() %}
\begin{align*}
\dfrac{\partial u}{\partial x} &= bf'(bx - ay) \\
\dfrac{\partial u}{\partial y} &= -af'(bx - ay) \\
a \dfrac{\partial u}{\partial x} + b \dfrac{\partial u}{\partial y} &=
a [bf'(bx - ay)] + b[-af'(bx - ay)] \\
&= ab f'(bx - ay) - ab f'(bx - ay) \\
&= 0 \quad \checkmark
\end{align*}
{% end %}

Again, note that the solution $u(x, y) = f(bx - ay)$ is a _general solution_ for arbitrary $f$. To find a unique solution, we must be provided with a condition that constrains $f$. For instance, such a condition may be:

{% math() %}
u(0, y) = \tan(-ky)
{% end %}

If we substitute $u(0, y)$ into our general solution, we find that:

{% math() %}
\begin{align*}
u(0, y) &= f\left(\cancel{bx}^0 - ay\right) \\
&= f(-a y) \\
\end{align*}
{% end %}

Therefore we have:

{% math() %}
\begin{align*}
f(-ay) &= \tan(-ky) \\
f(\xi) &= \tan (k \xi / a)
\end{align*}
{% end %}

where we used the substitution $\xi = -ay$ to solve. Therefore, the _particular solution_ given the condition that $u(0, y) = \tan(-ky)$ becomes:

{% math() %}
\begin{align*}
u(x, y) &= \tan\left(\dfrac{k}{a}(bx - a y)\right) \\
&= \tan \left(k \left(\dfrac{b}{a} x -  y\right)\right)
\end{align*}
{% end %}

### Coordinate transformation method

We may alternately solve the transport equation by another means: a **coordinate transformation**. If we define the following transformed coordinates:

{% math() %}
\begin{align*}
\tilde x = a x + by \\
\tilde y = bx - ay
\end{align*}
{% end %}

Then by the chain rule, we may translate the derivatives with respect to $x$ and $y$ to derivatives with respect to $\tilde x$ and $\tilde y$:

{% math() %}
\begin{align*}
\dfrac{\partial}{\partial x} &= \dfrac{\partial \tilde x}{\partial x} \dfrac{\partial}{\partial \tilde x} + \dfrac{\partial \tilde y}{\partial x} \dfrac{\partial}{\partial \tilde y} \\
&= a \dfrac{\partial}{\partial \tilde x} + b \dfrac{\partial}{\partial \tilde y} \\
\dfrac{\partial}{\partial y} &= \dfrac{\partial \tilde x}{\partial y} \dfrac{\partial}{\partial \tilde x} + \dfrac{\partial \tilde y}{\partial y} \dfrac{\partial}{\partial \tilde y} \\
&= b \dfrac{\partial}{\partial \tilde x} - a\dfrac{\partial}{\partial \tilde y}
\end{align*}
{% end %}

Now if we _substitute_ these expressions back into the equation, we find that:

{% math() %}
\begin{align*}
a\dfrac{\partial u}{\partial x} + b \dfrac{\partial u}{\partial y} = 0 \\
\left(a\dfrac{\partial}{\partial x} + b \dfrac{\partial}{\partial y}\right)u(x, y) = 0 \\
\left[a\left( a \dfrac{\partial}{\partial \tilde x} + b \dfrac{\partial}{\partial \tilde y}\right) + b\left(b \dfrac{\partial}{\partial \tilde x} - a\dfrac{\partial}{\partial \tilde y}\right)\right]u(x, y) = 0 \\
\left[a^2 \dfrac{\partial}{\partial \tilde x} + a b \dfrac{\partial}{\partial \tilde y} + b^2 \dfrac{\partial}{\partial \tilde x} - a b \dfrac{\partial}{\partial \tilde y}\right]u(x, y) = 0 \\
\left[a^2 \dfrac{\partial}{\partial \tilde x} + \cancel{a b \dfrac{\partial}{\partial \tilde y}} + b^2 \dfrac{\partial}{\partial \tilde x} - \cancel{a b \dfrac{\partial}{\partial \tilde y}}\right]u(x, y) = 0 \\
\left[a^2 \dfrac{\partial}{\partial \tilde x} + b^2 \dfrac{\partial}{\partial \tilde x} \right]u(x, y) = 0 \\
(a^2 + b^2) \dfrac{\partial}{\partial \tilde x} u(x, y) = 0
\end{align*}
{% end %}

Where we notice how this transformation of coordinates means that the equation _greatly_ simplifies. Since $a, b \neq 0$, then the only way for $(a^2 + b^2) \dfrac{\partial}{\partial \tilde x} u(x, y) = 0$ to be true is if $\dfrac{\partial}{\partial \tilde x} u(x, y) = 0$. Now, if we take the partial integral, we find that:

{% math() %}
\begin{align*}
\dfrac{\partial}{\partial \tilde x} u(x, y) = 0 \\
\int \dfrac{\partial}{\partial \tilde x} u(x, y)\, d\tilde x = \int 0\, d\tilde x \\
u(x, y) = f(\tilde y)
\end{align*}
{% end %}

Where we remember that we _always_ have to add a constant of integration (technically, _function of integration_, which we represent with $f$ here) when taking the partial integral. Recall now that we defined our transformed coordinates such that:

{% math() %}
\begin{align*}
\tilde x = a x + by \\
\tilde y = bx - ay
\end{align*}
{% end %}

Therefore, by substitution of the bottom equation for $\tilde y$, we have:

{% math() %}
u(x, y) = f(\tilde y) = f(bx - ay)
{% end %}

Where the function $f$ must be determined by the _boundary conditions_ supplied to the problem. Note that this is the **same solution** as we arrived by the method of characteristics, showing that the two methods yield _identical results_ (it would be mathematically inconsistent if they didn't!)

### Generalized method of characteristics

We may generalize the method of characteristics for first-order linear PDEs with variable coefficients (rather than constant ones). These PDEs are in the form:

{% math() %}
f(x, y) \dfrac{\partial u}{\partial x} + g(x, y) \dfrac{\partial u}{\partial y} = 0
{% end %}

As with before, we can interpret the left-hand side of the PDE as the directional derivative $\nabla_\mathrm{v} u$ along the direction of $\mathbf{v} = \langle f(x, y), g(x, y)\rangle$. Since the directional derivative is equal to zero, there exist **characteristic curves** along which $u(x, y)$ _does not change_, instead taking a **constant value**, just as we saw previously.

To be able to solve for the characteristic curves, we again rewrite the equation into the form:

{% math() %}
\dfrac{\partial u}{\partial x} + \dfrac{g(x, y)}{f(x, y)} \dfrac{\partial u}{\partial y} = 0
{% end %}

And we still use the multivariable chain rule to find that:

{% math() %}
\dfrac{du}{dx} = \dfrac{\partial u}{\partial x} + \dfrac{\partial u}{\partial y} \dfrac{dy}{dx}
{% end %}

From which we make the identification that if we set $\dfrac{dy}{dx} = \dfrac{g}{f}$, then $\dfrac{du}{dx}$ becomes identical to the left-hand side of the PDE. Thus, we need only solve for the differential equation:

{% math() %}
\dfrac{dy}{dx} = \dfrac{g(x, y)}{f(x, y)}
{% end %}

This results in some solution in the form $y(x) = G(x) + c$ where $c$ is a constant. Afterwards, the steps match near-identically from prior discussion of the simpler case.

## PDEs from physical phenomena

One of the motiving reasons for the study of partial differential equations is in their close relationship with **physics**. PDEs model many physical phenomena, such as flows, vibrations, oscillations, diffusion, advection, and heat conduction, just to name a few. In many cases, PDEs can be derived from physical principles, and we will show that this is the case with several examples.

### The transport equation

We will first derive the **transport equation**, with a derivation partially based on [the following guide](https://www.ndsu.edu/pubweb/~novozhil/Teaching/483%20Data/02.pdf). The transport equation is given by:

{% math() %}
\dfrac{\partial u}{\partial t} + c\dfrac{\partial u}{\partial x} = 0
{% end %}

To begin our analysis, consider a moving distribution of mass (for instance, spreading cement or some syrup slowly flowing down a spoon), modelled by a _mass density function_ $u(\mathbf{r}, t)$, which varies with time as the distribution moves. For simplicity, we can consider a _linear_ distribution of mass, such that the distribution is confined to move along one axis. Thus, the mass density function depends only on one spatial and one time coordinate, and simplifies to $u(x, t)$. Let us call the _velocity_ at which $u(x, t)$ moves as $c$ (which we will call the _speed of propagation_).

Let the mass density at time $t$ be distributed between two endpoints $x = a$ and $x = b$. The total mass at $t$ is found by integrating the mass density between the endpoints $x = a$ and $x = b$. That is:

{% math() %}
M = \int_a^b u(x, t) dx
{% end %}

We may find the rate of change of the mass within the region of $x = a$ to $x = b$ as follows:

{% math() %}
\dfrac{dM}{dt} = \dfrac{d}{dt}\int_a^b u(x, t)\, dx =\int_a^b \dfrac{\partial u}{\partial t}\, dx
{% end %}

But by the law of the **conservation of mass**:

{% math() %}
\dfrac{dM}{dt} = -\Phi_M
{% end %}

The quantity on the right-hand side is the **mass flux**, meaning the net amount of mass flow from the amount of mass leaving the region $x = [a, b]$ and the amount of mass entering the region at the same time. The flux is thus given by:

{% math() %}
\Phi_M = c\underbrace{\dfrac{dM}{dx}\bigg|_{x = b}}_\text{mass flow out} - c\underbrace{\dfrac{dM}{dx} \bigg|_{x = a}}_\text{mass flow in}
{% end %}

Where $c$ is a factor to ensure the units are dimensionally consistent. But $\dfrac{dM}{dx}$, that is, the mass per unit length, is simply the mass density! Thus we may equivalenly write:

{% math() %}
\Phi_M = c[u(b, t) - u(a, t)]
{% end %}

Where $u(b, t)$ is the mass density at $x = b$ at time $t$, and $u(a, t)$ is the mass density at $x = a$ at the same time. We note that by the fundamental theorem of calculus, we have:

{% math() %}
c[u(b, t) - u(a, t)] = \int_a^b c\dfrac{\partial u}{\partial x} dx
{% end %}

So we have:

{% math() %}
\Phi_M = \int_a^b c\dfrac{\partial u}{\partial x} dx
{% end %}

Recall from earlier that $\dfrac{dM}{dt} = -\Phi_M$. If we now substitute our derived expressions for $\dfrac{dM}{dt}$ and $\Phi_M$, we have

{% math() %}
\dfrac{dM}{dt} = \int_a^b \dfrac{\partial u}{\partial t}\, dx = -\int_a^b c\dfrac{\partial u}{\partial x} dx
{% end %}

And therefore we have:

{% math() %}
\begin{gather*}
\int_a^b \dfrac{\partial u}{\partial t}\, dx = -\int_a^b c\dfrac{\partial u}{\partial x} dx \\
\int_a^b \left(\dfrac{\partial u}{\partial t} + c\dfrac{\partial u}{\partial x}\right) d x = 0 \\
\dfrac{\partial u}{\partial t} + c\dfrac{\partial u}{\partial x} = 0
\end{gather*}
{% end %}

We have arrived at the **transport equation**. More advanced readers may note that the transport equation is actually the 1D case of the more general **continuity equation**:

{% math() %}
\begin{align*}
\dfrac{\partial \rho}{\partial t} &= -\left(\dfrac{\partial J_x}{\partial x} + \dfrac{\partial J_y}{\partial y} + \dfrac{\partial J_z}{\partial z}\right) \\
&= \nabla \cdot \mathbf{J}
\end{align*}
{% end %}

Various forms of the continuity equation appear in nearly all fields in physics, from fluid dynamics to electromagnetic theory to special and general relativity to even quantum mechanics. Thus, studying the transport equation is crucial to understanding its more complex derivatives.

### The wave equation

The next PDE we will derive is the **wave equation**. In its most common form, the one-dimensional wave equation is given by:

{% math() %}
\dfrac{\partial^2 u}{\partial t^2} - c^2 \dfrac{\partial^2 u}{\partial x^2} = 0
{% end %}

The standard derivation of the wave equation comes from the study of a vibrating string, in which the tensile force of a string, together with a fair bit of mathematical wizardry, is used to arrive at the PDE. We will take an alternative route and offer a simpler - although less mathematically-rigorous - derivation.

Recall that Newton's second law, in one dimension, is given by:

{% math() %}
m\dfrac{d^2 x}{dt^2} = F_x(x, t)
{% end %}

where $F_x$ is a force in the $x$ direction. Now once again, consider a _distribution of mass_ that can be modelled as a mass density function $u(x, t)$. Since we are considering a mass density (i.e. mass _over_ length) rather than a singular mass, the left-hand side of Newton's second law becomes:

{% math() %}
m \dfrac{d^2 x}{dt^2} \Rightarrow \dfrac{\partial^2 u}{\partial t^2}
{% end %}

Now suppose that at time $t = 0$, an external force is applied that causes a disturbance in the mass distribution. In the traditional derivation of the wave equation, this is stretching a string under tension; but our mass distribution doesn't _have to be_ a string. The mass distribution would _respond_ to the disturbance with a **restoring force** that "smooths out" the disturbance throughout the mass distribution to try to restore itself to equilibrium. Thus we would expect this force to be proportional to the _curvature_ of the function $u(x, t)$ in space. But recall that the second derivative encodes information about curvature - this is why we use it to determine concavity (concave-up or concave-down) in optimization problems. So we could expect the restoring force to take the form:

{% math() %}
F \Rightarrow  c^2 \dfrac{\partial^2 u}{\partial x^2}
{% end %}

Where $c^2$ is some constant to get the units right (we will discuss its physical significance later). Now, susbtituting everything into Newton's second law, we have:

{% math() %}
m\dfrac{d^2 x}{dt^2} = \dfrac{\partial^2 u}{\partial t^2} = c^2 \dfrac{\partial^2 u}{\partial x^2}
{% end %}

Thus, with just a bit of rearrangement, we have arrived at the **wave equation**:

{% math() %}
\dfrac{\partial^2 u}{\partial t^2} - c^2 \dfrac{\partial^2 u}{\partial x^2} = 0
{% end %}

Note that interestingly, the wave equation can be factored into _two_ transport equations, one that gives leftward-traveling (i.e. $-x$ direction) solutions and one that gives rightward-traveling (i.e. $x$ direction) solutions:

{% math() %}
\begin{gather*}
\dfrac{\partial^2 u}{\partial t^2} - c^2 \dfrac{\partial^2 u}{\partial x^2} =
\left(\dfrac{\partial u}{\partial t} + c\dfrac{\partial u}{\partial x}\right)\left(\dfrac{\partial u}{\partial t} - c\dfrac{\partial u}{\partial x}\right) \\
\left(\dfrac{\partial u}{\partial t} + c\dfrac{\partial u}{\partial x}\right)\left(\dfrac{\partial u}{\partial t} - c\dfrac{\partial u}{\partial x}\right) = 0 \\
\Rightarrow
\dfrac{\partial u}{\partial t} + c\dfrac{\partial u}{\partial x} = 0, \\
\dfrac{\partial u}{\partial t} - c\dfrac{\partial u}{\partial x} = 0
\end{gather*}
{% end %}

This is a tremendously-helpful fact, as it means that solving the transport equation already brings us halfway to solving the wave equation.

### The diffusion equation

Consider some distribution of mass given by mass density $u(\mathbf{r}, t)$ confined in a volume $\Omega$. For instance, this may be a gas, which has regions of varying density. The total mass of the gas within the volume would be given by the volume integral of $u$ over the region:

{% math() %}
M = \int_\Omega u(\mathbf{r}, t)\, dV
{% end %}

By the conservation of mass, any gas that flows out of the volume must flow across the boundary of the volume. For instance, some gas flowing out of an (imaginary) spherical region must flow across the surface of the (imaginary) sphere. The rate at which gas flows, or _diffuses_, per unit area, is given by **Fick's law**:

{% math() %}
j = -\mathbf{n} \cdot k \nabla u
{% end %}

To find the total rate of diffusion across the entire boundary of the volume (this is called the **flux**, denoted $\Phi$), we need to take the surface integral across the entire surface area of the volume's boundary:

{% math() %}
\Phi = \oint_{\partial \Omega} j \, dA = -\oint_{\partial \Omega} \mathbf{n} \cdot k\nabla u\, dA
{% end %}

To ensure the conservation of mass, the reduction in mass of the gas within the volume must be equal to the flux (amount of diffusion out of the volume). Therefore, we have:

{% math() %}
\Phi = -\dfrac{dM}{dt}
{% end %}

Therefore, by substitution of the expression for $M$ and $\Phi$:

{% math() %}
-\oint_{\partial \Omega} \mathbf{n} \cdot k\nabla u\, dA = -\dfrac{d}{dt}\int_\Omega u(\mathbf{r}, t)\, dV
{% end %}

Now, recalling the divergence theorem, we can rewrite the surface integral on the left-hand side as a _volume integral_, as follows:

{% math() %}
-\oint_{\partial \Omega} \mathbf{n} \cdot k\nabla u\, dA \Rightarrow -\int_\Omega \nabla \cdot (k \nabla u)\, dV
{% end %}

Therefore we have:

{% math() %}
-\int_\Omega \nabla \cdot (k \nabla u)\, dV = -\dfrac{d}{dt}\int_\Omega u(\mathbf{r}, t)\, dV
{% end %}

We may combine this into one integral by using the Leibnitz rule (for differentiation under the integral sign):

{% math() %}
\dfrac{d}{dt}\int_\Omega u(\mathbf{r}, t)\, dV = \int_\Omega \dfrac{\partial}{\partial t} u(\mathbf{r}, t)\, dV
{% end %}

So that we have:

{% math() %}
\int_\Omega \left(\dfrac{\partial}{\partial t} u(\mathbf{r}, t) - \nabla \cdot (k \nabla u)\right)\, dV = 0
{% end %}

By the vanishing theorem, the quantity inside the brackets must also be zero. Therefore, we have:

{% math() %}
\dfrac{\partial u}{\partial t} - \nabla \cdot (k \nabla u) = 0
{% end %}

Written slightly differently, we have the **diffusion equation**:

{% math() %}
\dfrac{\partial u}{\partial t} = \nabla \cdot (k \nabla u) 
{% end %}

Note that this is the _homogeneous case_. In the case where there is a source $f(\mathbf{r}, t)$ and $k = k(\mathbf{r})$, the linear inhomogeneous case becomes:

{% math() %}
\dfrac{\partial u}{\partial t} = \nabla \cdot (k(\mathbf{r}) \nabla u) + f(\mathbf{r}, t)
{% end %}

In the other case, if there is no source $f(\mathbf{r}) = 0$, and $k = \text{const.}$, then we have $\nabla \cdot (k \nabla u) = k\nabla^2 u$ and thus we have:

{% math() %}
\dfrac{\partial u}{\partial t} = k \nabla^2 u 
{% end %}

If $u$ does not change with time, then $\dfrac{\partial u}{\partial t} = 0$ and thus we have _Laplace's equation_:

{% math() %}
\nabla^2 u = 0
{% end %}

Another particular case of the diffusion equation is the **heat equation**, where the diffusing substance is heat. The distribution of heat is given by the temperature $T(\mathbf{r}, t)$ and the heat equation takes the form:

{% math() %}
\dfrac{\partial T}{\partial t} = \alpha^2 \nabla^2 T
{% end %}

> The heat equation's physical basis is **Fourier's law**: for two regions of temperatures $T_1, T_2$, the rate of heat flow between the regions is proportional to the gradient of the temperature $T$. This is very similar to Fick's law for diffusion, and thus the heat equation is classified as a type of diffusion equation.

Finally, a famous case of the diffusion equation (albeit where $u = \Psi(\mathbf{r}, t)$ is a complex-valued function) is the **Schrödinger equation**, which takes the form:

{% math() %}
i\hbar \dfrac{\partial \Psi}{\partial t} = -\dfrac{\hbar^2}{2m} \nabla^2 \Psi + V(\mathbf{r}) \Psi
{% end %}

Due to the conservation of probability, the Schrödinger equation requires that the _normalization condition_ to be satisfied:

{% math() %}
\int_\Omega |\Psi (\mathbf{r})|^2 dV = 1
{% end %}

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

> **Differentiation and integration of solutions:** For any solution $u(x, t)$ that possesses a derivative $v = \dfrac{\partial u}{\partial t}$, $v$ _also_ satisfies a diffusion equation $\dfrac{\partial v}{\partial t} = k\dfrac{\partial^2 v}{\partial t^2}$. Likewise, for any solution $u(x, t)$ that possesses an integral $I = \displaystyle \int_a^b u(x, t) dx$, $I$ _also_ satisfies a diffusion equation $\dfrac{\partial I}{\partial t} = k\dfrac{\partial^2 I}{\partial t^2}$. The same applies for $I = \displaystyle \int_a^b u(x - y, t)g(y)\,dy$ This directly results from the linearity of the diffusion equation (i.e. the sum $u_1 + u_2$ of two solutions $u_1, u_2$ is also a solution).

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