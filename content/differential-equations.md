+++
title = "Notes on Differential Equations"
date = 2024-01-10
+++

These are notes taken in RPI's MATH 2400 course, on an introduction to differential equations.

<!-- more -->

## Introduction

A _differential equation_ is an equation that contains derivatives of an unknown function. They are a powerful tool to describe a variety of physical processes.

Differential equations are classified via three characteristics.
- Ordinary vs partial
- Order
- Linear vs nonlinear
These characteristics determine how they should be solved.

First, we can classify differential equations as either ordinary (ODE) or partial (PDE). ODEs contain only one independent variable, whereas PDEs contain more than one independent variable. How to distinguish? Just look for the derivative sign - if it contains $\partial$ (the partial derivative symbol), then it's a PDE, otherwise it's an ODE.

For instance, an ODE could be:

$$
\frac{d^2 y}{dx^2} + x \frac{dy}{dx} = 2y
$$

And a PDE could be:

$$
\frac{\partial^2 z}{\partial x^2} + \frac{\partial^2 z}{\partial y^2} = 1
$$

Note that partial derivatives can also be denoted by subscripts (i.e. $\frac{\partial^2 z}{\partial x^2} = z_{xx}$) and ordinary derivatives can also be denoted by primes (i.e. $\frac{dy}{dx} = y'$).

Second, we can classify differential equations by order. The order is the order of the highest derivative. For instance, if the differential equation contains at most a 1st derivative, then it is of first-order. If it contains at most a 2nd derivative, then it is of second-order. Note: if you have something like $(\frac{dy}{dx})^2$, this is still a first-order derivative, despite the square!

Third, we can classify differential equations as either linear or nonlinear. In general, linear differential equations are easier to solve and analyze. A linear equation is only composed of derivative terms multiplied by functions of $x$ (or whatever the independent variable is). That is, it is in the form:

$$
f(x) \frac{d^n y}{dx^n} + \dots + g(x) \frac{d^2 y}{dx^2} + h(x) \frac{dy}{dx} + k(x) y = a(x)
$$

If $a(x) = 0$, then the differential equation is called _homogeneous_; otherwise, it is called _non-homogeneous_. In addition, if a differential equation doesn't follow the general form of a linear differential equation, it is called _nonlinear_.

For instance, the following differential equation is linear and non-homogenous:

$$
x\frac{dy}{dx} + 3xy = 5x
$$

Modifying it makes it homogeneous:

$$
x \frac{dy}{dx} + 3xy = 0
$$
Whereas the following differential equation is nonlinear, due to the fact that we have derivative terms multiplied by functions of $y$, not $x$:

$$
y \frac{d^2 y}{dx^2} + \sin(y) y^2 = 0
$$

To solve a differential equation, there are 3 general steps:

- Is there a solution at all? (existence)
- How many solutions are there? (uniqueness)
- Can we determine the solutions? If so, how?

Generally, existence and uniqueness are topics handled by formal proofs, and one only usually needs to determine the solution via the appropriate method. To check that the solution is correct, it is possible to verify by putting the solution back into the equation.

## Separation of variables

Consider a first-order ODE in the form:

$$
\frac{dy}{dx} = g(x) f(y)
$$
Such an ODE can be rewritten in the form:

$$
a(y) dy = b(x) dx
$$

And with integration, it can be solved:

$$
\int a(y) dy = \int b(x) dx
$$

The idea is to move all the terms in $x$ to one side, move all the terms in $y$ to the other side, and integrate both sides. This gives a **general solution** to the differential equation, which is a family of functions. A particular solution (a single exact function) can be found if initial conditions are provided.

