+++
title = "Notes on Differential Equations"
date = 2024-01-10
+++

These are notes taken in RPI's MATH 2400 course, on an introduction to differential equations.

<!-- more -->

## Introduction

A _differential equation_ is an equation that contains derivatives of an unknown function. They are a powerful tool to describe a variety of physical processes.

Differential equations are classified via three main characteristics.

- Ordinary vs partial
- Order
- Linear vs nonlinear

These characteristics determine how they should be solved.

First, we can classify differential equations as either ordinary (ODE) or partial (PDE). ODEs contain an unknown function, typically $y$, of only one independent variable, typically $x$ or $t$. Meanwhile PDEs contain an unknown function, typically $u$, or more than one independent variable, such as $x, y, z$. How to distinguish? Just look for the derivative sign - if it contains $\partial$ (the partial derivative symbol), then it's a PDE, otherwise it's most likely an ODE.

For instance, an ODE could be:

$$
\frac{d^2 y}{dx^2} + x \frac{dy}{dx} = 2y
$$

Note that an ODE could contain several unknown functions (especially in systems of differential equations) so long as each function has only one independent variable:

$$
\frac{d^2 x}{dt^2} + 3 \frac{dy}{dt} = 3x + 5y
$$

And a PDE could be:

$$
\frac{\partial^2 z}{\partial x^2} + \frac{\partial^2 z}{\partial y^2} = 1
$$

Note that partial derivatives can also be denoted by subscripts (i.e. $\frac{\partial^2 z}{\partial x^2} = z_{xx}$) and ordinary derivatives can also be denoted by primes (i.e. $\frac{dy}{dx} = y'$).

Second, we can classify differential equations by order. The order is the order of the highest derivative. For instance, if the differential equation contains at most a 1st derivative, then it is of first-order. If it contains at most a 2nd derivative, then it is of second-order. Note: if you have something like $(\frac{dy}{dx})^2$, this is still a first-order derivative, despite the square!

Third, we can classify differential equations as either linear or nonlinear. In general, linear differential equations are easier to solve and analyze. A linear equation is **only** composed of derivative terms multiplied by functions of $x$ (or whatever the independent variable is). This is the most important distinguishing factor of a linear differential equation: there are **no functions of $y$ or functions of the derivatives of $y$ present**. 

The general form of a linear ordinary differential equation is:

$$
f(x) \frac{d^n y}{dx^n} + \dots + g(x) \frac{d^2 y}{dx^2} + h(x) \frac{dy}{dx} + k(x) y = a(x)
$$



If the equation can be rewritten such that $a(x) = 0$, then the differential equation is called _homogeneous_; otherwise, it is called _non-homogeneous_. Homogeneity only applies for linear ODEs; any nonlinear ODE cannot be classified in this way.

In addition, if a differential equation doesn't follow the general form of a linear differential equation, it is called _nonlinear_. For instance, the following is a nonlinear differential equation, because there is a function of the derivative $y'$ present:

$$
\left(\frac{dy}{dx}\right)^3 + xy = 0
$$

Similarly, the following is a nonlinear differential equation, because there is a function of $y$ present:

$$
3y' + \sin(y) x^3 = 5x
$$

Meanwhile, the following differential equation is linear and non-homogenous, because it has a term involving only $x$, but doesn't have any functions of $y$ or functions of derivatives of $y$:

$$
x\frac{dy}{dx} + 3xy = 5x
$$

Modifying it makes it homogeneous:

$$
x \frac{dy}{dx} + 3xy = 0
$$

Partial differential equations can also be linear so long as they don't have functions that depend on the dependent variable. For example, if the dependent variable is $u$, then the following is linear, because there is no function $f(u)$ in the equation:

$$
\frac{\partial u}{\partial x} + 2 \frac{\partial u}{\partial y} + xy = 0
$$

To solve a differential equation, there are 3 general steps:

- Is there a solution at all? (existence)
- How many solutions are there? (uniqueness)
- Can we determine the solutions? If so, how?

Generally, existence and uniqueness are topics handled by pure mathematicians, and one only usually needs to determine the solution via the appropriate method. The general idea typically involves matching the differential equation with a known case (i.e. a type of differential equation that has already been solved before). To check that the solution is correct, it is possible to verify by putting the solution back into the equation.

Solutions can be of two main types - explicit and implicit. An explicit solution is in the form of $y = y(x)$, such as $y = 3e^x$. An implicit solution is in the form $f(y) = g(x)$, such as $\sin(y) = 5x^3$. Explicit solutions are usually preferred, but sometimes only implicit solutions can be found.

Finally, differential equations are by no means a finished field. New methods of solving them and analyzing them are constantly being developed, but even so, there are many differential equations that simply have not yet been solved.

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

As an example, consider the differential equation of a falling object undergoing drag, where $m$ and $k$ are constants:

$$
m \frac{dv}{dt} = mg - kv
$$

We want to use separation of variables to solve. To do this, we first divide by $m$ to get:

$$
\frac{dv}{dt} = g - \frac{k}{m} v
$$

Now, we can multiply $dt$ to both sides to get:

$$
dv = \left(g - \frac{k}{m} v\right) dt
$$

And then dividing by the term on the RHS in brackets, we get:

$$
\frac{dv}{g - \frac{k}{m} v} = dt
$$

We can now integrate both sides (and this is why integration techniques are useful):

$$
\int \frac{dv}{g - \frac{k}{m} v} = \int dt
$$

The integration requires just a u-substitution on the LHS, and results in:

$$
-\frac{m}{k} \ln \left | g - \frac{kv}{m} \right | + C_1 = t + C_2
$$

Here, $C_1$ and $C_2$ are respectively the constants of integration from each integral - note that they are **not** the same. To clean up the equation, we can set a new constant of integration $C_3$, where $C_3 = C_2 - C_1$. Therefore, we have:

$$
-\frac{m}{k} \ln \left | g - \frac{kv}{m} \right | = t + C_3
$$

Now, we can multiply both sides by $-\frac{k}{m}$ to remove the constant from the LHS:

$$
\ln \left | g - \frac{kv}{m} \right | = -\frac{k}{m} t - \frac{k}{m} C_3
$$

We can define a new constant $C_4$, where $C_4 = -\frac{k}{m} C_3$:

$$
\ln \left | g - \frac{kv}{m} \right | = -\frac{k}{m} t + C_4
$$

Finally, we can raise both sides to the exponential to cancel out the natural log (here using the notation that $\exp(x) = e^x$):

$$
\exp \left(\ln \left | g - \frac{kv}{m} \right |\right) = \exp \left(-\frac{k}{m} t + C_4 \right)
$$

We know that the exponential of a natural log is just the argument to the natural log, so the LHS simplifies readily:

$$
g - \frac{kv}{m} = e^{-\frac{k}{m} t + C_4}
$$

Using properties of exponentials, we know that $e^{a + b} = e^a e^b$:

$$
g - \frac{kv}{m} = e^{-\frac{k}{m} t} e^{C_4}
$$

We'll now define a final constant $C$ where $C = e^{C_4}$, so:

$$
g - \frac{kv}{m} = C e^{-\frac{k}{m} t}
$$

Finally, solving for $v$, we get:

$$
v(t) = \frac{m}{k} \left(g - C e^{-\frac{k}{m}t} \right)
$$

First - is our solution _correct_? To verify it is correct, we can take its derivative and plug that derivative back into the original differential equation. Recall that the original equation was:

$$
m\frac{dv}{dt} = mg - kv
$$

If we take our solution $v(t)$, and differentiate it, we get:

$$
\frac{dv}{dt} = Ce^{-\frac{k}{m} t}
$$

Now, we can plug it back into the original differential equation:

$$
mCe^{-\frac{k}{m} t} = mg - k \cdot \frac{m}{k} \left(g - C e^{-\frac{k}{m}t} \right)
$$

If we simplify, we get:

$$
m Ce^{-\frac{k}{m} t} = m Ce^{-\frac{k}{m} t}
$$

The two sides match, so we can now declare that we have found a **general explicit solution** to this differential equation - general because $C$ is an arbitrary constant, so the solution really represents a _family_ of solutions:

$$
v(t) = \frac{m}{k} \left(g - C e^{-\frac{k}{m}t} \right)
$$

Suppose we are given the **initial condition** that $v(0) = 0$. If we substitute this into the equation, we have:

$$
0 = \frac{m}{k} \left(g - C e^{-\frac{k}{m} \cdot 0} \right)
$$

This simplifies to:

$$
0 = \frac{mg}{k} - C
$$

Therefore, given our specified initial condition, it must be true that:

$$
C = \frac{mg}{k}
$$

If we substitute this value of $C$ back into the equation, we get the _particular_ (or unique) solution of the differential equation, given the initial values:

$$
v(t) = \frac{m}{k} \left(g - \frac{mg}{k} e^{-\frac{k}{m}t} \right)
$$

## The method of integrating factors

Consider the first-order linear ODE:

$$
\frac{dy}{dx} + p(x)y = q(x)
$$

The method of integrating factors works only for 1st-order linear ODEs. To do so, we multiply the ODE by an **integrating factor** $\mu(x)$:

$$
\mu(x) \frac{dy}{dx} + \mu(x)p(x)y = \mu(x) q(x)
$$
Or in simplified notation:

$$
\mu y' + \mu p y = \mu q
$$
Now we're going to impose the restriction that $\mu(x)$ can't just be any function - it has to satisfy $\mu'(x) = \mu(x) p(x)$. Therefore we can say that $\mu p y = \mu' y$, so if we substitute that in, we have:

$$
\mu y' + \mu'y = \mu q
$$

Notice now that the LHS looks a lot like the expanded version of the product rule! Indeed it is, so we can rewrite it as:

$$
(\mu y)' = \mu q
$$

We can integrate both sides to get:

$$
\mu y = \int \mu(x) q(x) dx
$$

We can isolate $y$ by solving $\mu'(x) = \mu(x) p(x)$. This is a separable differential equation, which we can easily solve (here we call the integration constant $A$):

$$
\frac{d\mu}{dx} = \mu p
$$

$$
\int \frac{d\mu}{\mu} = \int pdx
$$

$$
\ln|\mu| = \int pdx
$$

$$
\mu = Ae^{\int p(dx)}
$$

If we substitute this back in, we have:

$$
Ae^{\int p(x) dx} y = \int q(x) Ae^{\int p(x)dx} dx
$$

The two integration constants on the LHS and RHS cancel out to have:

$$
e^{\int p(x) dx} y = \int q(x) e^{\int p(x) dx} dx
$$

Which we can solve for $y$ with:

$$
y = e^{-\int p(x) dx} \int q(x) e^{\int p(x) dx} dx + Ce^{-\int p(x) dx}
$$

## 2nd-order ODE general forms

The general form of a 2nd-order linear ODE is given by:

$$
a_2(x) \frac{d^2 y}{dx^2} + a_1 (x) \frac{dy}{dx} + a_0(x)y = g(x)
$$

Or in Lagrange notation:

$$
a_2(x) y'' + a_1(x) y' + a_0(x) y = g(x)
$$

Note that this means that any 2nd-order linear ODE can be written as a system of 2 first-order differential equations. If we let $v = y'$, then we can say:

$$
\begin{align}
a_2(x) v' + a_1(x) v + a_0(x)y &= g(x) \\\\
y' &= v
\end{align}
$$

Each of these two first-order differential equations has a unique solution given an initial condition - $v(0)$ (which is equal to $y'(0)$) for the first and $y(0)$ for the second. This means that the original 2nd-order linear ODE must have two solutions and two initial conditions. The two solutions, denoted $y_1(x)$ and $y_2(x)$, must also be _linearly independent_. Linearly independent means that $y_1(x) \neq c y_2(x)$ and $y_2(x) \neq c y_1(x)$ - one cannot be expressed as a constant multiple of the other. The general solution is obtained by a linear combination of both solutions:

$$
y(x) = c_1 y_1(x) + c_2 y_2(x)
$$

To find whether two solutions $y_1(x)$ and $y_2(x)$ are linearly independent, we check the **Wronskian**. Suppose the IVP has two solutions $y_1$ and $y_2$:

$$
\begin{align}
c_1 y_1 (x) + c_2 y_2 (x) &= 0 \\\\
c_2 y_1'(x) + c_2 y_2'(x) &= 0
\end{align}
$$

We can write this as a matrix $A \mathbf{x} = \mathbf{b}$:

$$
\begin{pmatrix}
y_1 & y_2 \\\\
y_1' & y_2'
\end{pmatrix}
\begin{pmatrix}
c_1 \\\\
c_2
\end{pmatrix} =
\begin{pmatrix}
0 \\\\
0
\end{pmatrix}
$$
The Wronskian is the determinant of $A$:

$$
W = \det(A) = \begin{vmatrix}
y_1 & y_2 \\\\
y_1' & y_2'
\end{vmatrix} = y_1 y_2' - y_1' y_2
$$
If $W \neq 0$, then the solutions are linearly independent. The derivation is straightforward but long and won't be presented here.

### Abel's formula

Abel's formulas says that if $y_1(x)$ and $y_2(x)$ are solutions of $y''' + p(x) y' + q(x) y = 0$, then:

$$
W = c \exp \left(-\int p(x) dx\right)
$$
Note that the general form of a linear 2nd-order ODE can be cast into this form by dividing by $a_2(x)$:

$$
y'' + \frac{a_1(x)}{a_2(x)} y'' + \frac{a_0(x)}{a_2(x)}y = 0 \Rightarrow p(x) = \frac{a_1(x)}{a_2(x)}, q(x) = \frac{a_0(x)}{a_2(x)}
$$

To prove this, we first know that:

$$
\begin{align}
y_1'' + py_1' + qy_1 &= 0 \\\\
y_2'' + py_2' + qy_2 &= 0
\end{align}
$$
If we eliminate $q$ by multiplying the top equation by $y_2$ and the bottom equation by $y_1$, we get:

$$
y_2 y_1 '' + py_2 y_1' - y_1 y_2'' - py_1 y_2' = 0
$$

We recognize the Wronskian $W = y_1 y_2' - y_2 y_1'$ if we factor out the second term:

$$
(y_2 y_1'' - y_1 y_2'') - p(y_2 y_1' + y_1 y_2')
$$
$$
(y_2 y_1'' - y_1 y_2'') + p(-W) = 0
$$
In addition, given the definition of the Wronskian, we can find that $W' = y_1 y_2'' - y_2 y_1''$. Therefore, the entire equation reduces down to:

$$
-W' -pW = 0
$$

Or:

$$
W' + pW = 0
$$
Solving this results in:

$$
W = C \exp \left(-\int p(x) dx \right)
$$
