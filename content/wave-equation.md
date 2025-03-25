+++
title = "Solving the wave equation"
date = 2023-10-03

[extra]
notoc = true
+++

The wave equation is a ubiquitous partial differential equation found in many areas of physics. In this guide, we will sketch out the basic approach to solving it.

<!-- more -->

First, let's state the problem. The wave equation is given by:

{% math() %}
\frac{\partial^2 u}{\partial t^2} - c^2 \frac{\partial^2 u}{\partial x^2} = 0
{% end %}

Unlike many partial differential equations, the wave equation is actually solvable, and as such it not only carries significant physical importance, but also serves as a useful demonstration of the methods of solving PDEs.

First, notice that the equation is **linear**. That means all the terms of $u(x, t)$ and its derivatives are at most, scaled by a constant, and added (or subtracted) together. This is a powerful fact, because that means any two solutions can be added (or subtracted) together and scaled by constants to form a new solution that satisfies the equation:

{% math() %}
u_1(x, t) \pm u_2(x, t) = u_3(x, t)
{% end %}

We are going to prove that a solution to the wave equation can be put in the general form:

{% math() %}
u(x, t) = A \sin(x - vt + \phi_0) \pm B \sin(x + vt + \phi_0)
{% end %}

To do this, we will first say that our solution $u(x, t)$ can be written as a product of two functions, one of time, and one of space:

{% math() %}
u(x, t) = f(x) g(t)
{% end %}

Now, we can take the derivatives of $u(x, t)$ with respect to each variable:

{% math() %}
\begin{align*}
\frac{\partial^2 u}{\partial x^2} = \frac{d^2 f}{dx^2} g(t) = f'' g \\
\frac{\partial^2 u}{\partial t^2} = \frac{d^2 g}{dt^2} f(x) = g'' f
\end{align*}
{% end %}

We can plug these derivatives into the equation, to have:

{% math() %}
g''f - c^2 f''g = 0
{% end %}

We can move the second term to the right side of the equation:

{% math() %}
g''f = c^2 f''g
{% end %}

And we can rearrange the terms to make each side in terms of only one variable - this is called **separation of variables**:

{% math() %}
\frac{g''}{g} \frac{1}{c^2} = \frac{f''}{f}
{% end %}

Now, recognize that the left hand side depends on $g$, and the right hand side depends on $f$, but the values of the derivatives are the same, up to a scaling constant. The only way two derivatives of otherwise unrelated variables would be the same is if both yield a constant, which we'll call $C_1$:

{% math() %}
\frac{f''}{f}  = \frac{g''}{g}\frac{1}{c^2} = C_1
{% end %}

This yields a set of two ordinary differential equations:

{% math() %}
\begin{align*}
f'' &= C_1 f \\
g'' &= c^2 C_1 g
\end{align*}
{% end %}

If we set $C_2 = -C_1$, and rewrite both equations in terms of $C_2$, the equations immediately start to look familiar: they are the differential equations of both the sine and cosine functions.

{% math() %}
\begin{align*}
f'' &= -C_2 f \\
g'' &= -c^2 C_2 g
\end{align*}
{% end %}

The solution to the first differential equation is:

{% math() %}
f(x) = C_2 \sin (x)
{% end %}

And that of the second is:

{% math() %}
g(t) = C_2 \sin(ct)
{% end %}

So if we plug that back into $u(x, t)$, we have:

{% math() %}
u(x, t) = f(x) g(t) = C_2 \sin (x)C_2 \sin(ct)
{% end %}

If we use a trig identity, where $C_3 = \frac{(C_2)^2}{2}$, this becomes:

{% math() %}
u(x, t) = C_3 \cos(x - ct) - C_3\cos (x + ct))
{% end %}

Since we can write any cosine as a sine with a phase shift, we have:

{% math() %}
u(x, t) = C_3 \sin(x - ct + \phi_0) - C_3 \sin(x + ct + \phi_0)
{% end %}

Replacing $C_3$ with arbitrary constants $A$ and $B$, and changing the subtraction to $\pm$, which we can do by simply defining $B = -C_3$, we have:

{% math() %}
u(x, t) = A \sin (x - vt + \phi_0) \pm B \sin(x + vt + \phi_0)
{% end %}

Which is the **solution** of the wave equation. Note that it is not the only solution, as the specific solution to the wave equations depends on the _boundary conditions_, which are additional constraints on the form of $u(x, t)$ - we did not provide boundary conditions to the problem for simplicity. However, it is a solution, and indeed, an important solution, because it describes **standing waves** in physics, like the vibrations of a string or a drumhead, as well as radio waves in a metal box. To learn more, please feel free to take a look at the [full guide to PDEs](@/intro-pdes/index.md).

