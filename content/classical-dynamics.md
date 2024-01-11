+++
title = "Notes on introductory classical dynamics"
date = 2024-01-08
+++

These are notes taken in RPI's Physics 1150 class, relating to introductory classical dynamics. Make sure to read the [calculus series](@/calculus-series.md) first as these notes are calculus-heavy.

<!-- more -->

## Dimensional analysis

Dimensional analysis is a method of doing a "sanity check" for _numerical computations_ with units. That is, an equation only makes sense if the units check out.

For instance, consider:

$$
x(t) = \frac{1}{2} at^2
$$
Does this make sense with dimensional analysis? Well, acceleration is in units of $ms^{-2}$ and time is in units of $s^2$, so multiplying them together and by 1/2 (a dimensionless value) gives units of $m$ (meters). And meters are a reasonable unit for a position $x(t)$.

To keep track of dimensions, it is often more useful to use general dimensions for each term - $M$ for the mass dimension, $L$ for the length dimension, $T$ for the time dimension. So, plugging in this:

$$
L = \frac{1}{2} \times LT^{-2} \times T^2 = L
$$

So it's correct!

## Newton's 2nd Law

In 1 dimension, Newton's second law relates the net force $F$ with position and time:

$$
F(x, \dot x, t) = m \frac{d^2 x}{dt^2}
$$

This is a **2nd-order ordinary differential equation of motion** that describes how an object moves.

### Special cases of Newton's 2nd Law

In a **constant-force problems**, then we assume $F$ is a constant. Therefore:

$$
F = m \frac{d^2 x}{dt^2}
$$
Which we can rewrite as:

$$
F = m \frac{dv}{dt}
$$

Using integration, we can solve:

$$
v(t) = \int \frac{F}{m} dt = v_0 + \frac{F}{m}t
$$

Then, we solve for:

$$
v = \frac{dx}{dt}
$$
We integrate again to find:

$$
x(t) = \int v(t) dt = x_0 + v_0 t + \frac{1}{2} \frac{F}{m} t^2
$$

In a **time-dependent force problem**, then:

$$
v(t) = \int \frac{F(t)}{m} dt
$$
$$
x(t) = \int v(t) dt
$$

### Drag force application

For an object falling through atmosphere, the drag force is given by $F_D = -bv$, and the gravitational force is given by $F_G = mg$.

Using the principle of superposition of forces, we can add all the individual forces acting on a falling object to obtain:

$$
m \frac{dv}{dt} = mg - bv, \quad v(0) = 0
$$

This is a **separable** first-order ordinary differential equation, which we can solve by the method of separation of variables.

Therefore, we have:

$$
\frac{dv}{dt} = g - \frac{b}{m} v
$$
$$
\frac{dv}{g - (b/m) v} = dt
$$
Now, we can integrate both sides to solve (the left-hand side uses a u-substitution):

$$
\int \frac{dv}{g - (b/m) v} = \int dt
$$

$$
-\frac{b}{m} \ln \left( g - \frac{b}{m} v \right) = t + C
$$

Solving for the initial condition $v(0) = 0$, we have:

$$
-\frac{m}{b} \ln |g| = C
$$
Using algebraic manipulation, we can solve for $v$ in terms of $t$:

$$
v(t) = \frac{mg}{b} \left(1 - e^{-\frac{b}{m}t} \right)
$$
Note that if we take the limit of $v(t)$ as $t \to \infty$, then we reach a terminal (constant) velocity:

$$
\lim_{t \to \infty} v(t) = \frac{mg}{b}
$$

## Approximation techniques

To first-order (when a point is close to $x_0$), the derivative is approximately a finite difference:

$$
\frac{df}{dx} \bigg|_{x = x_0} \approx \frac{\Delta f}{\Delta x}
$$

So a linear approximation to a function at an arbitrary point $x_0$ is:

$$
f(x) \approx f(x_0) + f'(x_0)(x - x_0)
$$

For example, $e^x \approx 1 + x$, and $\sin(x) \approx x$.
