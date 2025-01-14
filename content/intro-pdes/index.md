+++
title = "A gentle guide to partial differential equations"
date = 2024-01-14
+++

This is a short guide/mini-book on introducing various topics in partial differential equations, including analytical methods of finding solutions, boundary-value problems, and discussions of widely-known PDEs.

<!-- more -->

These notes are dedicated to [Professor Yuri Lvov](https://faculty.rpi.edu/yuri-lvov) of Rensselaer Polytechnic Institute, who teaches the course on which this guide is based, and to whom I am greatly thankful. They are freely-sharable and released to the public domain.

Note: familiarity with vector calculus and ordinary differential equations is assumed. Full length guides for both are available if a refresher is needed; they can be found on the [vector calculus guide](@/vector-and-advanced-calculus.md) and the [introduction to differential equations](@/differential-equations/index.md).


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

## Solutions to linear PDEs

### Solving for homogenous vs. inhomogenous PDEs

Consider a linear differential operator $\mathcal{L}$, similar to the ones we have already studied. A **solution** to a homogenous linear PDE is a function $u(x, y, z)$ that satisfies:

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