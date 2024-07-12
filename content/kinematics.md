+++
title = "The more general kinematic equations"
date = 2023-10-30
+++

Kinematics is one of the most fundamental parts of physics. In fact, determining the motion of objects is essentially where physics originated. Today, we'll take a close look at kinematics, and in particular, a more nonstandard formulation of kinematics.

<!-- more -->

We've all seen the typical kinematic equations. But those are only for the case of constant acceleration. The more general kinematic equations are given by:

{% math() %}
v(t) = v_0 + \int_0^t a(u) du
{% end %}
{% math() %}
x(t) = x_0 + v_0 t + \int_0^t v(u)du
{% end %}

Let's explain what that means. First, we start with the acceleration function:

{% math() %}
a = a(t)
{% end %}

Acceleration here is not a constant - it is a function. To get velocity, we simply integrate the acceleration:

{% math() %}
v(t) = \int a(t) dt
{% end %}

Using the fundamental theorem of calculus, we can rewrite this indefinite integral as a definite integral:

{% math() %}
v(t) = \int_0^t a(u) du
{% end %}

Note that because the definite integral from 0 to 0 is always zero, while not every function starts at $(0, 0)$, we need to shift the function by the initial value, thus we add the $v_0$. You can also think of $v_0$ as the constant of integration.

We can do the same with velocity to get position.

Does this have many applications in physics? No, not many. This isn't because an acceleration function is hard to determine analytically. Indeed, using Newton's second law $a = \frac{F}{m}$, an acceleration function is often readily determined. The issue is that usually, the acceleration function usually isn't in terms of $t$. For instance, using Hooke's law $F = -kx$, we can determine that $a(t) = -\frac{k}{m} x(t)$. The issue is, this isn't an explicit equation in terms of $t$, so we can't integrate to find the solution.

So rather, the more useful equation is usually the differential equation form of Newton's second law:

{% math() %}
\frac{d^2 x}{dt^2} = \frac{F(x, t)}{m}
{% end %}

Or:

{% math() %}
\frac{d^2 x}{dt^2} = -\frac{1}{m} \frac{dU}{dx}
{% end %}

These are tremendously more helpful, but requires differential equation solving techniques, making them more difficult to compute. So again, the general kinematic equations aren't exactly very useful, but they are an interesting quirk of physics.
