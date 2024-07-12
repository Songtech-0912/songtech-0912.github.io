+++
title = "Solving separable partial differential equations"
date = 2023-09-30
+++

Partial differential equations have a reputation for being impossible to solve. And in many cases, this is true - they are extremely difficult to analytically solve for a general solution. However, when a partial differential equation is separable, it can be solved fairly straightforwardly, as a system of ordinary differential equations. Here is how to do so.

<!-- more -->

Consider the PDE:

{% math() %}
\frac{\partial f}{\partial x} = 3xy
{% end %}

We can write the PDE as:

{% math() %}
f(x, y) = g(x) h(y)
{% end %}

Therefore:

{% math() %}
\frac{\partial f}{\partial x} = g'(x) h(y)
{% end %}

So:

{% math() %}
g'(x) h(y) = 3xy
{% end %}

We can then separate:

{% math() %}
\frac{g'(x)}{3x} = \frac{h(y)}{y}
{% end %}

Now, an examination of this indicates that:

{% math() %}
\frac{g'(x)}{3x} = \frac{h(y)}{y} = \lambda
{% end %}

So we now have 1 ODE to solve, and one equation:

{% math() %}
g'(x) =  3x \lambda
{% end %}

{% math() %}
h(y) = \lambda y
{% end %}

The general solution of the ODE is:

{% math() %}
g(x) = \frac{3}{2} \lambda x^2 + C_1
{% end %}

Given that $f(x, y) = g(x) h(y)$, we have the general solution of the PDE:

{% math() %}
f(x, y) = \frac{3}{2} \lambda^2 x^2 y + C_1 \lambda y
{% end %}
