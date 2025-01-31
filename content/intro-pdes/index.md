+++
title = "A Gentle Guide to Partial Differential Equations"
date = 2025-01-14
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

Notice here that instead of a _constant_ of integration, we have an arbitrary _function_ of integration $F(y)$, since we are taking the partial integral.

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

For instance, suppose our area of interest is a linear region between endpoints $x_1, x_2$, and we want to solve the wave equation. We would then want to specify the **initial condition** $u(x, 0)$, the boundary conditions $u(x_1, t)$ and $u(x_2, t)$, which are **Dirichlet boundary conditions**, as well as $\dfrac{\partial u(x, 0)}{\partial x} \bigg|_{x = x_1}$ and $\dfrac{\partial u(x, 0)}{\partial x} \bigg|_{x = x_2}$ which are **Neumann boundary conditions**. This combination is called an **initial boundary-value problem** (IBVP) and allows for finding a unique solution. For partial differential equations that are time-independent, we simply refer to a combination of boundary conditions and the PDE as a **boundary-value problem** (BVP).

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
