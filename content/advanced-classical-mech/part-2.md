+++
title = "Advanced Classical Mechanics, Part II"
date = 2025-01-26
draft = false
+++

In this second part of the advanced classical mechanics guide, we go over the Lagrangian and Hamiltonian formulations of classical mechanics. These formulations introduced powerful mathematical and physical tools that helped revolutionize our understanding of physics. We will then see how we can apply Lagrangian and Hamiltonian methods to describe all sorts of systems, from springs all the way to planets.

<!-- more -->

Again, remember that this is part of the **advanced classical mechanics series**, which I have split into several parts to not be overly long. A complete catalogue of the entire three-part guide is shown below:

> ### Chapter guide for classical mechanics
>
> - [Go to part 1 of the series](@/advanced-classical-mech/index.md) for Newtonian mechanics and special relativity
> - [Go to part 2 of the series](@/advanced-classical-mech/part-2.md) for Lagrangian and Hamiltonian formulations of classical mechanics (**this is the part you're reading right now**)
> - [Go to part 3 of the series](@/advanced-classical-mech/part-3.md) for rigid-body dynamics, many-body systems, the harmonic oscillator, and systems of coupled oscillators

## Lagrangian mechanics

Newtonian mechanics remained a highly successful theory in classical physics for a long time after Newton, but it always had a few fundamental issues, even before the development of relativity and quantum mechanics. These issues are related to the fact that Newtonian mechanics relies on being able to write out a **net force** using vector analysis - an often nontrivial task when there are a large number of forces, or when working with a non-Cartesian coordinate system.

Lagrangian mechanics, developed in the 18th-century, provides an alternative and _complementary_ approach to solve for the equations of motion of the system. In Lagrangian mechanics, we define a quantity known as the **Lagrangian** that is the difference between the kinetic energy and the potential energy of an object:

{% math() %}
\mathcal{L}(x, \dot x, t) = K - U
{% end %}

Once a Lagrangian is found, the **Euler-Lagrange equation** is used to find the equations of motion:

{% math() %}
\dfrac{d}{dt} \dfrac{\partial \mathcal{L}}{\partial \dot x} - \dfrac{\partial \mathcal{L}}{\partial x} = 0
{% end %}

The Lagrangian formalism (also called _Lagrangian mechanics_) has a number of advantages compared to the Newtonian formalism. Being formulated in terms of energy, the Lagrangian is composed of _scalar quantities_, so it is less easy to mess up the sign, which happens frequently when needing to use vectors. Additionally the Lagrangian has the characteristic that _any constant added or subtracted from the Lagrangian_, as well as any function of a constant, **does not affect the Lagrangian**. That is to say, $\mathcal{L}_2 = K - U + f(C)$ is **physically equivalent** to $\mathcal{L}_1 = K - U$, where $C = \text{const.}$ This means that Lagrangians can be greatly simplified as any constant terms can simply be dropped.

Furthermore, using the Lagrangian approach means that once the potential energy and kinetic energy is defined with respect to a particular coordinate system (e.g. Cartesian, etc.), no vector analysis is necessary. For many systems, this is a prerequisite to making the system tracatable, and further simplifies the analysis. For systems where a rotating or moving coordinate system is the preferred choice of coordinates (such as a double pendulum or a child on a merry-go-round), Lagrangian mechanics truly comes into its own and allows solving problems that would be extremely difficult otherwise.

### A basic example

Consider a free particle (a particle moving under the influences of no forces) moving along the $x$ axis. For a free particle, Newton's differential equation reads:

{% math() %}
m \dfrac{d^2x}{dt^2} = \mathbf{F}_\mathrm{net} = 0
{% end %}

We can solve this differential equation using relatively straightforward means:

{% math() %}
\begin{align*}
\dfrac{d^2x}{dt^2} &= 0 \\
\int \dfrac{d^2x}{dt^2} dt &= \int 0\, dt \\
\dfrac{dv}{dt} &= v_0 \\
\int \dfrac{dv}{dt} dt &= \int v_0\, dt \\
x(t) &= x_0 + v_0\, t
\end{align*}
{% end %}

Thus the solution to the differential equation is $x(t) = x_0 + v_0\, t$. Again, this is nothing surprising - we already knew this from when we first examined Newton's differential equation.

Now, let us try to solve the same problem using the _Lagrangian approach_. To do so, we first write down the Lagrangian of a free particle (noting that the potential energy is zero, or a constant, but again a constant potential energy has no effect on the Lagrangian):

{% math() %}
\begin{align*}
\mathcal{L} &= K - U \\
&= \dfrac{1}{2} mv^2 - \cancel{U(x)}^0 \\
&= \dfrac{1}{2} m \dot x^2
\end{align*}
{% end %}

We can now take the partial derivatives of the Lagrangian:

{% math() %}
\begin{align*}
\dfrac{\partial \mathcal{L}}{\partial x} &= \dfrac{\partial}{\partial x} \underbrace{\left(\dfrac{1}{2} m \dot x^2\right)}_{\mathcal{L}\ \text{does not depend on}\ x} \\ &= 0 \\
\dfrac{\partial \mathcal{L}}{\partial x} &= \dfrac{\partial}{\partial \dot x}\left(\dfrac{1}{2} m \dot x^2\right) = m \dot x \\
\dfrac{d}{dt} \dfrac{\partial \mathcal{L}}{\partial x} &= \dfrac{d}{dt}(m \dot x) = m \ddot x
\end{align*}
{% end %}

Therefore, by substitution into the Euler-Lagrange equation, we have $m \ddot x = 0$, which also has the same solution $x(t) = x_0 + v_0\, t$. We have demonstrated that the Lagrangian and Newtonian approaches are **completely equivalent** and yield the same results. In this case, the Lagrangian approach may seem like a bit of overkill. There are some situations, however, where the Lagrangian approach is much superior to the Newtonian approach and greatly speeds up the process of solving a problem.

### 2D and 3D Lagrangians

In the case of Lagrangians in 2D or 3D, we must include the velocity components of every dimension in the Lagrangian - for instance, we might have $K = \dfrac{1}{2} m(v_x^2 + v_y^2 + v_z^2)$. While there is **one Lagrangian** (that may, however, involve multiple coordinates), there is a _separate_ Euler-Lagrange equation for each coordinate $x_i$, that is:

{% math() %}
\begin{align*}
\dfrac{d}{dt} \dfrac{\partial \mathcal{L}}{\partial \dot x_1} &- \dfrac{\partial{L}}{\partial x_1} = &0 \\
\dfrac{d}{dt} \dfrac{\partial \mathcal{L}}{\partial \dot x_2} &- \dfrac{\partial{L}}{\partial x_2} = &0 \\
& \vdots & \vdots \\
\dfrac{d}{dt} \dfrac{\partial \mathcal{L}}{\partial \dot x_i} &- \dfrac{\partial{L}}{\partial x_i} = &0
\end{align*}
{% end %}

> **Note:** $x_i$ does **not** have to be in Cartesian coordinates. It is just as possible to use spherical coordinates $(r, \theta, \phi)$ or cylindrial coordinates $(\rho, \phi, z)$ as the coordinates $x_1, x_2, \dots x_i$. In fact, this is one of the advantages of Lagrangian mechanics - it generalizes to _all coordinates_ and thus we only need to perform a coordinate transformation of $K$ and $U$ to switch the coordinates to whichever are most convenient for the problem.

Let us, for instance, consider the case of a particle of mass $m$ slowly falling close to the Earth's surface, assuming no air resistance. Given that the gravitational potential energy close to the Earth's surface is $U = mgy$, we have:

{% math() %}
\begin{align*}
\mathcal{L} &= \dfrac{1}{2} m(v_x^2 + v_y^2) - m g y \\
&= \dfrac{1}{2} m(\dot x^2 + \dot y^2) - mg y
\end{align*}
{% end %}

The Euler-Lagrange equations for the $x$ and $y$ coordinates are given by:

{% math() %}
\begin{align*}
\dfrac{d}{dt} \dfrac{\partial \mathcal{L}}{\partial \dot x} &- \dfrac{\partial{L}}{\partial x} = 0 \\
\dfrac{d}{dt} \dfrac{\partial \mathcal{L}}{\partial \dot y} &- \dfrac{\partial{L}}{\partial y} = 0 \\
\end{align*}
{% end %}

We will first analyze the $y$ (vertical) component. In $y$, the partial derivatives of the Lagrangian are given by:

{% math() %}
\begin{align*}
 \\
\dfrac{\partial \mathcal{L}}{\partial y} = -mg \\
\dfrac{\partial \mathcal{L}}{\partial \dot y} = m \dot y\\
\dfrac{d}{dt} \dfrac{\partial \mathcal{L}}{\partial \dot y} = m \ddot y
\end{align*}
{% end %}

Therefore, upon substitution into the the Euler-Lagrange equation in the $y$ component, we have $m \ddot x = -mg$, which we may rearrange to $\ddot x = -g$, the equation of free-fall. This has the solution:

{% math() %}
y(t) = y_0 + v_{0y} t - \dfrac{1}{2} gt^2
{% end %}

We can now turn our attention to the $x$ (horizontal) component. In $x$, the partial derivatives of the Lagrangian are given by:

{% math() %}
\begin{align*}
\dfrac{\partial \mathcal{L}}{\partial x} &= \dfrac{\partial}{\partial x} \left(\dfrac{1}{2} m \dot x^2\right) \\ &= 0 \\
\dfrac{\partial \mathcal{L}}{\partial x} &= \dfrac{\partial}{\partial \dot x}\left(\dfrac{1}{2} m \dot x^2\right) = m \dot x \\
\dfrac{d}{dt} \dfrac{\partial \mathcal{L}}{\partial x} &= \dfrac{d}{dt}(m \dot x) = m \ddot x
\end{align*}
{% end %}

Thus, upon substitution into the Euler-Lagrange equation in the $x$ component, we have $m \ddot x = 0$, which has the solution $x(t) = x_0 + v_{0x} \, t$. Thus the complete solutions to the equations of motion for the falling particle becomes:

{% math() %}
\begin{align*}
x(t) &= x_0 + v_{0x} \, t \\
y(t) &= y_0 + v_{0y} t - \dfrac{1}{2} gt^2
\end{align*}
{% end %}

Which is indeed the expected result that we would also find by application of Newton's laws.

### The harmonic oscillator

Let us now examine problem in which the usefulness of the Lagrangian formalism becomes more evident: the **harmonic oscillator**. For a harmonic oscillator, such as a mass $m$ on a spring of spring constant $k$, we have $K = \dfrac{1}{2} m v^2 = \dfrac{1}{2} m \dot x^2$ and $U = \dfrac{1}{2} k(x - x_0)^2$. Therefore, our Lagrangian becomes:

{% math() %}
\begin{align*}
\mathcal{L} &= K - U \\
&= \dfrac{1}{2} m\dot x^2 - \dfrac{1}{2} k(x - x_0)^2
\end{align*}
{% end %}

Taking the partial derivatives of $\mathcal{L}$ we have:

{% math() %}
\begin{align*}
\dfrac{\partial \mathcal{L}}{\partial x} &= -k(x - x_0) \\
\dfrac{\partial \mathcal{L}}{\partial \dot x} &= m \dot x \\
\dfrac{d}{dt} \dfrac{\partial \mathcal{L}}{\partial \dot x} &= m \ddot x
\end{align*}
{% end %}

Therefore, upon substitution into the Euler-Lagrange equations we have:

{% math() %}
\begin{align*}
m \ddot x - (-k(x - x_0)) = 0 \\
m \ddot x + k (x - x_0) = 0 \\
\ddot x +\dfrac{k}{m} (x - x_0) = 0 \\
\dfrac{d^2 x}{dt^2} = -\dfrac{k}{m} (x - x_0)
\end{align*}
{% end %}

Indeed, this is the expected result for the differential equation of the simple harmonic oscillator. But what if we include _gravity_? Let us now consider a harmonic oscillator under the influence of gravity, such as a mass hanging on a spring from a ceiling. Our kinetic energy becomes $K = \dfrac{1}{2} m\dot y^2$, and our potential energy must now be modified to $U = \dfrac{1}{2} k(y - y_0)^2 - mg y$. Thus our Lagrangian becomes:

{% math() %}
\begin{align*}
\mathcal{L} &= K - U \\
&= \dfrac{1}{2} m \dot y^2 - \left(\dfrac{1}{2} k(y - y_0)^2 - mg y\right) \\
&= \dfrac{1}{2} m \dot y^2 -\dfrac{1}{2} k(y - y_0)^2+ mg y
\end{align*}
{% end %}

We may now calculate the partial derivatives of the Lagrangian in $y$, as previous:

{% math() %}
\begin{align*}
\dfrac{\partial \mathcal{L}}{\partial y} &= -k(y - y_0) + mg \\
\dfrac{\partial \mathcal{L}}{\partial \dot y} &= m\dot y \\
\dfrac{d}{dt} \dfrac{\partial \mathcal{L}}{\partial \dot y} &= m\ddot y \\
\end{align*}
{% end %}

Thus the differential equation of motion becomes:

{% math() %}
\begin{align*}
m \ddot y = mg - k(y - y_0) \\
\ddot y = g - \dfrac{k}{m} (y - y_0) \\
\dfrac{d^2 y}{dt^2} = g - \dfrac{k}{m} (y - y_0)
\end{align*}
{% end %}

### The equivalence of Newtonian and Lagrangian mechanics

We have already seen that Lagrangian mechanics yields the same equations of motion as Newtonian mechanics in several examples, but what about the general case? Does Lagrangian mechanics _always_ make the same predictions as Newtonian mechanics? The answer is yes, and we will show why.

Consider a particle under the influence of some conservative force, whose potential energy is given by $U(x)$ (we work in one dimension but the same argument can be made for any number of dimensions). Then, the particle's Lagrangian would be given by:

{% math() %}
\begin{align*}
\mathcal{L} &= K - U \\
&= \dfrac{1}{2} m \ddot x^2 - U(x)
\end{align*}
{% end %}

Thus, the derivatives of the Lagrangian are given by:

{% math() %}
\begin{matrix*}
\dfrac{\partial \mathcal{L}}{\partial x} = -U'(x), & \dfrac{\partial \mathcal{L}}{\partial \dot x} = m\dot x, & \dfrac{d}{dt} \left(\dfrac{\partial \mathcal{L}}{\partial \dot x}\right) = m \ddot x
\end{matrix*}
{% end %}

So the Euler-Lagrange equation for our only coordinate $x$ would be given by:

{% math() %}
m \ddot x = -U'(x)
{% end %}

But this is exactly Newton's second law, $m\dfrac{d^2 x}{dt^2} = -\dfrac{dU}{dx}$! Thus, in _all cases_, Lagrangian mechanics _always_ gives the same results as Newtonian mechanics. So Lagrangian mechanics doesn't actually introduce any new physics; it is better to think of it as simply an alternative way to solve problems that sometimes works better or makes finding a solution easier than using the Newtonian method.

## More problems in Lagrangian mechanics

Because of how _different_ Lagrangian mechanics is from the traditional Newtonian approach to solving physical systems, it may be quite difficult to get adjusted to it. For this reason, here are a few additional fully-solved problems for Lagrangian mechanics that might be helpful to practice on.

### The simple pendulum

In this problem, a pendulum is attached to a string of length $\ell$ which makes an angle of $\theta$ with the vertical axis. The pendulum swings up and down under the action of gravity. We want to find the equations of motion for the pendulum.

Let us set up the coordinates to make this problem as convenient as possible. First, let us set our $+y$ axis to be the *downward-pointing* direction. Let our $x$ axis be centered at the position at which the pendulum is attached (i.e. its origin is at the pendulum's attachment point).

{{ diagram(src="../simple-pendulum.excalidraw.svg") }}

With this information, then the position of the pendulum at time $t$ is given by:

{% math() %}
\begin{align*}
x &= \ell \sin \theta(t) \\
y &= \ell \cos \theta(t)
\end{align*}
{% end %}

Where again, the $y$ coordinate is actually the _downward-pointing_ coordinate due to the way we defined our coordinate system. Taking differentiation, we have:

{% math() %}
\begin{align*}
\dot x &= (\ell \cos \theta)\dot \theta \\
\dot y &= (-\ell \sin \theta) \dot \theta
\end{align*}
{% end %}

So, the kinetic energy becomes:

{% math() %}
\begin{align*}
K &= \dfrac{1}{2} m(\dot x^2 + \dot y^2) \\
&= \dfrac{1}{2} m[(\ell \cos \theta\, \dot \theta)^2 + (-\ell \sin \theta\, \dot \theta)^2] \\
&= \dfrac{1}{2} m\ell^2 \dot \theta^2 \cancel{(\cos^2 \theta + \sin^2 \theta)}^1 \\
&= \dfrac{1}{2} m \ell^2 \dot \theta^2
\end{align*}
{% end %}

The (purely-gravitational) potential energy, due to how we have defined our coordinate system, is given by $U = -mgy = -mg(\ell \cos \theta)$. Thus our Lagrangian becomes:

{% math() %}
\begin{align*}
\mathcal{L} &= K - U \\ &= \dfrac{1}{2} m \ell^2 \dot \theta^2 + mg \ell \cos \theta
\end{align*}
{% end %}

Since our Lagrangian only involves one generalized coordinate (in this case, $\theta$) there is only one Euler-Lagrange equation corresponding to that coordinate:

{% math() %}
\dfrac{\partial \mathcal{L}}{\partial \theta} - \dfrac{d}{dt} \left(\dfrac{\partial \mathcal{L}}{\partial \dot \theta}\right) = 0
{% end %}

The derivatives are given by:

{% math() %}
\begin{align*}
\dfrac{\partial \mathcal{L}}{\partial \theta} &= -mg \ell \sin \theta \\
\dfrac{\partial \mathcal{L}}{\partial \dot \theta} &= m \ell^2 \dot \theta\\
\dfrac{d}{dt}\left(\dfrac{\partial \mathcal{L}}{\partial \dot \theta}\right) &= m \ell^2 \ddot \theta
\end{align*}
{% end %}

Thus, substituting into the Euler-Lagrange equation we wrote down previously, we have:

{% math() %}
-mg\ell \sin \theta - m \ell^2 \ddot \theta = 0
{% end %}

Which, after simplification and rearranging, becomes:

{% math() %}
\ddot \theta = -\dfrac{g}{\ell} \sin \theta 
{% end %}

Or, rewritten:

{% math() %}
\dfrac{d^2 \theta}{dt^2} = -\dfrac{g}{\ell} \sin \theta
{% end %}

This is the differential equation of a **simple pendulum**. Despite looking rather simple, it is surprisingly hard to solve, but it is still useful, because it completely describes the simple pendulum, and it possesses approximate solutions that still yield important quantitative insights.

> **Note:** Interested in a more complicated pendulum problem? See the [worked-out solution to the elastic pendulum](@/elastic-pendulum/index.md).

### The centrifugal "force"

When an object is placed within a rotating object, it is common to say that the object experiences a _fictitious_ centrifugal force. We will show that what appears to be a "centrifugal force" is nothing but a radial acceleration caused by a moving coordinate system, and is _not_ a real force.

Consider a moving disk of radius $R$ and mass $M$ that rotates at angular velocity $\omega$ (ignore gravity). A small mass $m$ is placed at the edge of the disk (note: the figure below shows it _slightly_ less than the edge, but it is only for visual clarity). A diagram of our physical scenario is below:

{{ diagram(src="../centrifugal-force.excalidraw.svg") }}

If the disk was non-spinning, the position of the mass, relative to the center of the spinnning disk (which is the origin of our rotating coordinate system), would be given by:

{% math() %}
\begin{matrix*}
x = R \cos \phi, & y = R \sin \phi \\
\dot x = -R \sin \phi\, \dot \phi, & \dot y = R \cos \phi\, \dot \phi \\
\end{matrix*}
{% end %}

But the disk _is_ spinning, and thus, since we are using a rotating coordinate system that co-rotates with the disk, we must also include the "nudge" caused by the spinning disk on which the mass rests (which contributes an additional angular component $\theta = \omega t$ to the angular displacement of the mass). We therefore have:

{% math() %}
\begin{matrix*}
x = R \cos \phi  + R \cos \omega t, & y = R \sin \phi + R \sin \omega t \\
\dot x = -R \sin \phi\, \dot \phi- R \omega \sin \omega t, 
& \dot y = R \cos \phi\, \dot \phi + R \omega \cos \omega t \\
\end{matrix*}
{% end %}

Thus the total kinetic energy is given by:

{% math() %}
\begin{align*}
K &= \dfrac{1}{2} m(\dot x^2 + \dot y^2) \\ &= \dfrac{1}{2} m[(-R \sin \phi\, \dot \phi- R \omega \sin \omega t)^2 + (R \cos \phi\, \dot \phi + R \omega \cos \omega t)^2] \\
&= \dfrac{1}{2} m \bigg[R^2 \dot \phi^2 \sin^2 \phi + 2 R^2 \omega \sin \phi\, \dot \phi  \sin \omega t + R^2 \omega^2 \sin^2 \omega t \\
&\qquad \qquad + R^2 \dot \phi^2 \cos^2 \phi + 2 R^2\omega \cos \phi\, \dot \phi \cos \omega t + R^2 \omega^2 \cos^2 \omega t] \\
&= \dfrac{1}{2} m(R^2 \dot \phi^2(\cancel{\sin^2 \phi + \cos^2 \phi}^1) + 2R^2 \omega \dot \phi\,(\sin \phi \sin \omega t + \cos \phi \cos \omega t) \\
&\qquad \qquad + R^2 \omega^2 (\cancel{\sin^2 \omega t + \cos^2 \omega t)}^1) \\
&= \dfrac{1}{2} m(R^2 \dot \phi^2 + 2 R^2 \omega \dot \phi \cos(\phi - \omega t) + R^2 \omega^2)
\end{align*}
{% end %}

Where at the end we used the trigonometric identity $\sin A \sin B + \cos A \cos B = \cos(A - B)$. Since we are not considering gravity (imagine this spinning disk was in deep space) then the Lagrangian is:

{% math() %}
\begin{align*}
\mathcal{L} &= K - \cancel{U} \\
&= \dfrac{1}{2} m(R^2 \dot \phi^2 + 2 R^2 \omega \dot \phi \cos(\phi - \omega t) + \cancel{R^2 \omega^2})
\end{align*}
{% end %}

Where we can effectively ignore the $R^2 \omega^2$ term since it is a constant and constants do not change the Lagrangian. The Euler-Lagrange equation for the only generalized coordinate $\phi$ becomes:

{% math() %}
\dfrac{\partial \mathcal{L}}{\partial \phi} = \dfrac{d}{dt} \left(\dfrac{\partial \mathcal{L}}{\partial \dot \phi}\right)
{% end %}

Taking the partial derivatives of our Lagrangian, we find that:

{% math() %}
\begin{align*}
\dfrac{\partial \mathcal{L}}{\partial \phi} &= -mR^2 \omega \dot \phi \sin(\phi - \omega t) \\
\dfrac{\partial \mathcal{L}}{\partial \dot \phi} &= m R^2 \dot \phi \\
\dfrac{d}{dt}\left(\dfrac{\partial \mathcal{L}}{\partial \dot \phi}\right) &= m R^2 \ddot \phi
\end{align*}
{% end %}

If we substitute into the Euler-Lagrange equation we have:

{% math() %}
\begin{align*}
m R^2 \ddot \phi &= -mR^2 \omega \dot \phi \sin (\phi - \omega t) \\
\ddot \phi &= - \omega \dot \phi \sin(\phi - \omega t)
\end{align*}
{% end %}

We can write this in terms of an angular acceleration $\vec \alpha$:

{% math() %}
\vec \alpha = - \omega \dot \phi \sin(\phi - \omega t)
{% end %}

The negative sign means that the angular acceleration vector is actually pointing vertically _downwards_. Now, the acceleration vector $\vec a$ is related to the angular acceleration by:

{% math() %}
\vec \alpha = \dfrac{1}{r^2} \vec r \times \vec a
{% end %}

Where $\vec r$ is the radial vector that points from the axis of rotation to the mass. Thus by the right-hand rule, since the angular acceleration is pointing downards, we find that the acceleration vector actually points _outwards_, as shown in the below diagram:

{{ diagram(src="../rotational-lagrangian-example.excalidraw.svg") }}

Thus we find that there _appears_ to be a "force" that pushes the particle outwards and produces the acceleration $\vec a$ observed. In reality, such a force _does not exist_. We can prove this as follows: from the expression $\vec \alpha = - \omega \dot \phi \sin(\phi - \omega t)$, if we take the limit as $\omega \to 0$ (that is, the disk is no longer spinning), then $\vec \alpha \to 0$ and we recover the equations of uniform circular motion (that is, $\ddot \phi = 0$). The "force" (often called the _centrifugal force_) is merely a consequence of our rotating reference frame (remember, we chose a coordinate system that co-rotated with the disk), and if we choose an alternate frame of reference that is _not rotating_, this force vanishes. Thus we have shown that the centrifugal "force" is a fictitious force.

### Getting off a bus

Consider a situation that may be familiar: you were riding a bus (or train) moving at speed $v_0$ that suddenly undergoes a constant deceleration of magnitude $a$ until it comes to a stop. This catches you by surprise, and you end up dropping the precious physics textbook you borrowed from your physics professor. To appease your professor after this unfortunate incident, you intend to demonstrate your understanding of Lagrangian mechanics to calculate your equations of motion and thus explain that the deceleration was substantial enough to make you fall.

In this case, it is again easiest to use a _co-moving_ coordinate system - in this case, we can consider a coordinate system that moves along with the bus. Let $x$ denote your position with respect to a coordinate system centered at the front of the bus. Since the bus (presumably) does not fly into the air, we need only consider the $x$ coordinate. In theory, if the bus was absolutely stationary, then your kinetic energy would be given by:

{% math() %}
K = \dfrac{1}{2} m\dot x^2
{% end %}

But because the bus is _also_ moving (in fact, it is decelerating!), we must add an additional contribution from the moving bus. The bus has $\dot v = -a$ and thus $\dot x_\text{bus} = v_0 - a t$.

{% math() %}
K = \dfrac{1}{2}m(\dot x + v_0 - at)^2
{% end %}

The Lagrangian in this case contains only the kinetic energy (since the bus is at a constant height above the ground, its gravitational potential energy is a constant, and therefore makes no difference in the Lagrangian). Therefore:

{% math() %}
\mathcal{L} = \dfrac{1}{2}m(\dot x + v_0 - at)^2
{% end %}

The derivatives of the Lagrangian become:

{% math() %}
\begin{align*}
\dfrac{\partial \mathcal{L}}{\partial x} &= 0 \\
\dfrac{\partial \mathcal{L}}{\partial \dot x} &= m (\dot x + v_0 - at) \\
\dfrac{d}{dt} \left(\dfrac{\partial \mathcal{L}}{\partial \dot x}\right)
&=m (\ddot x - a)
\end{align*}
{% end %}

Therefore the singular Euler-Lagrange equation in this case, given by $\dfrac{\partial \mathcal{L}}{\partial x} = \dfrac{d}{dt} \left(\dfrac{\partial \mathcal{L}}{\partial \dot x}\right)$, then simply becomes:

{% math() %}
m(\ddot x - a) = 0 \quad \Rightarrow \quad \dfrac{d^2 x}{dt^2} = a
{% end %}

This is interesting - you experience a positive acceleration $a$ that _appears_ to come from a force that pushes you and makes you fall. But there is no force! The "force" actually arises from our choice of a moving coordinate system. Just as with the centrifugal "force", this "force" is also a _fictitious force_.

This is a powerful aspect of Lagrangian mechanics: once you choose your coordinates and write down your Lagrangian in terms of your chosen coordinates, the equations of motion that follow are _guaranteed to hold_ in your coordinate system, without needing to consider any fictitious forces.

### The general procedure

Now that we have worked through several problems, let us distill our insights to determine how to do Lagrangian mechanics in the _general case_. To be able to solve an _arbitrary_ problem using Lagrangian mechanics, we follow these steps:

1. Define a coordinate system using whichever reference frame is _most convenient_ for the problem. For instance, in problems with radial symmetry, polar coordinates may be better (i.e. $x = r \cos \theta, y = r \sin \theta$), and in problems where the reference frame is itself moving (e.g. child jumping on a rotating carousel) it may be helpful to choose a _co-moving coordinate system_ (i.e. a coordinate system that moves with the object)
	1. For systems of multiple objects (many-body systems), you would have a set of coordinates for every object, e.g. a two-body system would have coordinates $(x_1, y_1, z_1), (x_2, y_2, z_2)$. It is important to explicitly define the _origin_ and the _orientation_ of the axes of each of the coordinates for multi-body systems (in many cases, the origins of the coordinate systems for different objects will _not_ be the same, or the coordinate systems will be oriented differently)
2. Write down the total kinetic energy of the object(s) you are analyzing
	1. The kinetic energy of a (single) object is (classically) always $\dfrac{1}{2} mv^2 = \dfrac{1}{2} m (\dot x^2 + \dot y^2 + \dot z^2)$, but if you are using different coordinates, you would want to express $\dot x, \dot y, \dot z$ in terms of those coordinates (especially if there is a constraint on the system e.g. uniform circular motion in which case $\dot x^2 + \dot y^2 = r^2 \dot \theta^2$). In addition, $x(t)$ may include more than one terms if you define your coordinates with respect to a (co-)moving coordinate system. 
	2. The kinetic energy of a system of objects is the sum of the kinetic energies of each individual object, so you would have $K = K_1 + K_2 + \dots + K_n$, or more explicitly-written (in 1D), $K = \dfrac{1}{2} m\dot x_1^2 + \dfrac{1}{2} m \dot x_2^2 + \dots + \dfrac{1}{2}m \dot x_n^2$.
3. Write down the total potential energy of the object(s) you are analyzing. Note that this highly depends on what type of potential energy you have (e.g. harmonic oscillator, gravitational, electrostatic, etc.) and be careful to express the potential energy _in terms of your chosen coordinates_ if they are not $x, y, z$ coordinates or not oriented in standard (Cartesian 3D) position
4. Substitute into the Lagrangian with $\mathcal{L} = K - U$. Note that every system, whether single-body or many-body, should have just _one_ Lagrangian
5. Take the partial derivatives of the Lagrangian and substitute into the Euler-Lagrange equations $\dfrac{d}{dt} \dfrac{\partial \mathcal{L}}{\partial \dot x_i} - \dfrac{\partial{L}}{\partial x_i} = 0$. There is one Euler-Lagrange equation for _every coordinate_, so if you chose to use coordinates $(x, y, z)$, then you'd have three Euler-Lagrange equations, one for $x$, one for $y$, one for $z$. Thankfully, this process is pretty much just math, not physics; as long as you get the math right, your solution should be sound.
6. From there, find the equations of motion you get from each of the Euler-Lagrange equations. Then you're done!

## The brachistochrone problem and the stationary-action principle

We have spent quite some time developing the theory of Lagrangian mechanics, but it is also important to discuss its origins in a branch of mathematical physics known as the **calculus of variations**. The calculus of variations sprang from a classic optimization problem, known as the problem of the **branchistochrone**.

The problem statement is this: assume that a particle of mass $m$, falling only under the influence of gravity, is constrained to move along a curved path. The questions asks to find *which path* would lead the particle to travel between two points $A =(x_1, y_1)$ and $B = (x_2, y_2)$ in the shortest time.

To solve this problem, we use a classic argument from the calculus of variations. We first choose our coordinate system such that it has its origin at point $A$, with the $+y$ axis aligned along the direction of gravity (i.e. positive $y$ is pointing down towards the ground). Now recall that the speed of a particle is given by:

{% math() %}
v = \left|\dfrac{d\mathbf{r}}{dt}\right| = \dfrac{ds}{dt}
{% end %}

And therefore we can rearrange this such that:

{% math() %}
\begin{align*}
dt = \dfrac{ds}{v}\\
\int_0^\tau dt = \int_A^B \dfrac{ds}{v} \\
\tau = \int_A^B \dfrac{ds}{v}
\end{align*}
{% end %}

Where $\tau$ is the total travel time of the particle. We also know that:

{% math() %}
\begin{align*}
ds^2 &= dx^2 + dy^2 \\
ds &= \sqrt{dx^2 + dy^2} \\
&= \sqrt{1 + \left(\dfrac{dy}{dx}\right)^2} dx \\
&= \sqrt{1 + y'(x)}dx
\end{align*}
{% end %}

Therefore, we have:

{% math() %}
\tau = \int_A^B \dfrac{\sqrt{1 + y'(x)}dx}{v}
{% end %}

The speed $v$, meanwhile, can be found through the conservation of energy. Since $K = \dfrac{1}{2} mv^2$ and $U = -mgy$ (negative sign is due to our coordinate system), and given that at $t = 0$ the particle is at rest at $x_0 = 0, y_0 = 0$, we have a total energy of:

{% math() %}
E_0 = \cancel{K_0}^0 + U_0 = \cancel{mgy_0}^0 = 0
{% end %}

But this is true for _all times $t$_ due the conservation of energy. Therefore, we have:

{% math() %}
\begin{align*}
K + U &= 0 \\
\dfrac{1}{2} mv^2 - mgy &= 0 \\
\dfrac{1}{2} mv^2 = mgy \\
v^2 = 2gy \\
v = \sqrt{2gy}
\end{align*}
{% end %}

Which, if we substitute into our integral expression, becomes:

{% math() %}
\begin{align*}
\tau &= \int_A^B \dfrac{\sqrt{1 + y'(x)}dx}{\sqrt{2gy}} \\
&= \int_A^B \sqrt{\dfrac{1 + y'(x)}{2gy}}dx \\
&= \int_A^B f (y, y', x) dx, \quad f(y, y', x) = \sqrt{\dfrac{1 + y'(x)}{2gy}}
\end{align*}
{% end %}

We recognize that $\tau[y, y', x]$ is a **functional** (we write it in square brackets accordingly), since it takes a function $y(x)$ and returns its integral, making it a "function of functions". We may now use the familiar Euler-Lagrange equations to minimize the functional by finding the solution to:

{% math() %}
\dfrac{\partial f}{\partial y} - \dfrac{d}{dx} \left(\dfrac{\partial f}{\partial y'}\right) = 0
{% end %}

The derivatives are rather complicated, so we will not compute them here, but we will simply state the result: the functional is minimized by the path $y(x)$ given by:

{% math() %}
\begin{gather*}
y = a(\theta - \sin \theta), \\
\theta = \cos^{-1} \left(1 - \dfrac{x}{a}\right), \\
\end{gather*}
{% end %}

This path is called a **cycloid** of radius $a$, and interestingly, it _isn't_ a straight line. The *point* of this exercise is not to do a lot of complicated math, but rather, to understand that the Euler-Lagrange equations are much more general than their use in Lagrangian mechanics, and that Lagrangian mechanics is simply an application of the Euler-Lagrange equations towards finding the trajectories that minimize a specific functional. This functional is called the **action** $S$, and is given by the integral of the Lagrangian over time:

{% math() %}
S[x, \dot x, t] = \int_{t_1}^{t_2} \mathcal{L}(x, \dot x, t)\, dt = \int_{t_1}^{t_2}K - U\, dt
{% end %}

> **Note on notation:** Here we consider the one-dimensional action; in general the action requires all spatial coordinates so we would have $S = S[\mathbf{r}, \dot{\mathbf{r}}, t]$ instead.

Further, the _reason_ why Lagrangian mechanics works in the first place is that the action functional obeys the **principle of stationary action** (or sometimes called "stationary action"). This is a fundamental physical law, as fundamental as energy conservation and momentum conservation, and it says that the allowed (classical) trajectories of a particle travelling between two points $x(t_1)$ and $x(t_2)$ must be the one that makes the action **stationary** (that is, the rate of change of the action must be zero - this can occur at a minimum, maximum, or saddle point, but usually is the minimum). Classical physics offers no explanation for why the principle of stationary action exists - a full explanation requires quantum mechanics - but the principle is the physical basis for Lagrangian mechanics and explains why it makes the correct predictions about the motion of physical objects.

> **Note for the advanced reader:** For more information on the quantum explanation of the principle of stationary action, read about the [Feynmann path integral](https://en.wikipedia.org/wiki/Path_integral_formulation) and in general the [sum-over-paths formulation](https://www.quantamagazine.org/how-our-reality-may-be-a-sum-of-all-possible-realities-20230206/) of quantum mechanics.

## The Euler-Lagrange equations under coordinate transformation

Continuing on the theme of the Euler-Lagrange equations, recall that we have observed that they have several special properties. For instance, we noted that a Lagrangian is independent of any additive constant, so any constant terms can be dropped from a Lagrangian. We will now show that these characteristics are not simply quirks of math; they arise from **symmetries** in the Lagrangian.

Consider two coordinate systems, $q_i'$ and $q_i$. These represent generic coordinates - $q_i, q_i'$ can be $x, y, z$ or $r, \theta, \phi$, the index just represents some arbitrary coordinate. What is important is that we can write **coordinate transformations** to express $q_i'$ in terms of $q_i$, that is:

{% math() %}
q_i' = q_i'(q_i(t), t)
{% end %}

> **Note on notation:** for the remainder of this section, all the primes (e.g. $q_i', \dot q_i'$) represent the _transformed coordinates_, not derivatives. That is to say, $q_i' \neq \dfrac{dq_i}{dt}$.

This may represent, for instance, the coordinate transformations from Cartesian to spherical coordinates, but again, it represents an _arbitrary coordinate transform_ $q_i \to q_i'$ from one coordinate system $q_i$ to another coordinate system $q_i'$. But how would the velocities transform? Using the chain rule, we can write $\dot q_i$ in terms of $\dot q_i'$:

{% math() %}
\begin{align*}
\dot q_i' &=\dfrac{dq_i'}{dt} \\&= \dfrac{d}{dt} q_i'(q_i(t), t) \\
&= \dfrac{\partial q_i'}{\partial t} + \dfrac{\partial q_i'}{\partial q_i} \dfrac{dq_i}{dt} \\
&= \dfrac{\partial q_i'}{\partial t} + \dfrac{\partial q_i'}{\partial q_i} \dot q_i
\end{align*}
{% end %}

Why is this significant? Because it means that:

{% math() %}
\dfrac{\partial \dot q_i'}{\partial \dot q_i} = \dfrac{\partial q_i'}{\partial q_i}
{% end %}

We are interested in how the _Euler-Lagrange equations_ transform under this coordinate transformation. To do so, let us take the Lagrangian expressed in our original coordinates $\mathcal{L}(q_i, \dot q_i, t)$ and express it in terms of new coordinates. We have:

{% math() %}
\mathcal{L}(q_i, \dot q_i, t) = \mathcal{L}(q_i(q_i', t), \dot q_i(\dot q_i', t), t) = \tilde{\mathcal{L}}(q_i', \dot q_i', t)
{% end %}

Let us show that this transformed Lagrangian $\tilde{\mathcal{L}}$ gives the completely equivalent equations of motion to the original Lagrangian $\mathcal{L}$. First, we will take the partial derivatives of our new Lagrangian $\tilde{\mathcal{L}}$ with respect to the _original_ coordinates $q_i$. This we can do by the multivariablef chain rule. Since the transformed Lagrangian is a function of the position and velocity coordinates $(q_i', \dot q_i')$, the multivariable chain rule yields:

{% math() %}
\begin{align*}
\dfrac{\partial \tilde{\mathcal{L}}}{\partial q_i} &= \dfrac{\partial \mathcal{L}}{\partial q_i'} \dfrac{\partial  q_i'}{\partial q_i} + \dfrac{\partial \mathcal{L}}{\partial \dot q_i'} \dfrac{\partial \dot q_i'}{\partial q_i} \\
\dfrac{\partial \tilde{\mathcal{L}}}{\partial \dot q_i} &= \dfrac{\partial \mathcal{L}}{\partial \dot q_i'} \dfrac{\partial \dot q_i'}{\partial \dot q_i} = \underbrace{\dfrac{\partial \mathcal{L}}{\partial \dot q_i'} \dfrac{\partial q_i'}{\partial q_i}}_\text{we derived earlier} \\
\end{align*}
{% end %}

Where we used the result we derived earlier, $\dfrac{\partial \dot q_i'}{\partial \dot q_i} = \dfrac{\partial q_i'}{\partial q_i}$. We can now substitute these partial derivatives into the Euler-Lagrange equations:

{% math() %}
\begin{align*}
\dfrac{\partial \tilde{\mathcal{L}}}{\partial q_i}- \dfrac{d}{dt} \left(\dfrac{\partial \tilde{\mathcal{L}}}{\partial \dot q_i}\right)
&= \left(\dfrac{\partial \mathcal{L}}{\partial q_i'} \dfrac{\partial  q_i'}{\partial q_i} + \dfrac{\partial \mathcal{L}}{\partial \dot q_i'} \dfrac{\partial \dot q_i'}{\partial q_i} \right) 
- \dfrac{d}{dt}\left(\dfrac{\partial \mathcal{L}}{\partial \dot q_i'} \dfrac{\partial q_i'}{\partial q_i}\right) \\
&= \left(\dfrac{\partial \mathcal{L}}{\partial q_i'} \dfrac{\partial  q_i'}{\partial q_i} + \dfrac{\partial \mathcal{L}}{\partial \dot q_i'} \dfrac{\partial \dot q_i'}{\partial q_i} \right) 
- \dfrac{d}{dt}\dfrac{\partial \mathcal{L}}{\partial \dot q_i'}\bigg[\dfrac{\partial^2 q_i'}{\partial t \partial q_i} + \dfrac{\partial^2 q_i'}{\partial q_i^2}\underbrace{\dfrac{dq_i}{dt}}_{\dot q_i}\bigg] \\
&= \left(\dfrac{\partial \mathcal{L}}{\partial q_i'} \dfrac{\partial  q_i'}{\partial q_i} + \dfrac{\partial \mathcal{L}}{\partial \dot q_i'} \dfrac{\partial \dot q_i'}{\partial q_i} \right) 
- \dfrac{d}{dt}\dfrac{\partial \mathcal{L}}{\partial \dot q_i'} \bigg[\dfrac{\partial}{\partial q_i}\underbrace{\left(\dfrac{\partial q_i'}{\partial t} + \dfrac{\partial q_i'}{\partial q_i} \dot q_i\right)}_{q_i'}\bigg] \\
&= \left(\dfrac{\partial \mathcal{L}}{\partial q_i'} \dfrac{\partial  q_i'}{\partial q_i} + \dfrac{\partial \mathcal{L}}{\partial \dot q_i'} \dfrac{\partial \dot q_i'}{\partial q_i} \right) - \dfrac{d}{dt}\left(\dfrac{\partial \mathcal{L}}{\partial \dot q_i'} \dfrac{\partial q_i'}{\partial q_i}\right)
\end{align*}
{% end %}

This becomes:

{% math() %}
\begin{gather*}
\left(\dfrac{\partial \mathcal{L}}{\partial q_i'} \dfrac{\partial  q_i'}{\partial q_i} + \cancel{\dfrac{\partial \mathcal{L}}{\partial \dot q_i'} \dfrac{\partial \dot q_i'}{\partial q_i}} \right) 
- \underbrace{\dfrac{d}{dt} \left(\dfrac{\partial \mathcal{L}}{\partial \dot q_i'}\right) \dfrac{\partial q_i'}{\partial q_i} - \cancel{\dfrac{\partial \mathcal{L}}{\partial \dot q_i'} \dfrac{\partial \dot q_i'}{\partial q_i}}}_\text{product rule} \\
=\dfrac{\partial \mathcal{L}}{\partial q_i'} \dfrac{\partial q_i'}{\partial q_i} - \left(\dfrac{d}{dt} \dfrac{\partial \mathcal{L}}{\partial \dot q_i'}\right)\dfrac{\partial q_i'}{\partial q_i} \\
= \left[\dfrac{\partial \mathcal{L}}{\partial q_i'} - \dfrac{d}{dt} \left(\dfrac{\partial \mathcal{L}}{\partial \dot q_i'}\right)\right]\dfrac{\partial q_i'}{\partial q_i}
\end{gather*}
{% end %}

We have therefore shown that:

{% math() %}
\dfrac{\partial \tilde{\mathcal{L}}}{\partial q_i} - \left(\dfrac{d}{dt} \dfrac{\partial \tilde{\mathcal{L}}}{\partial \dot q_i}\right) =
\left[\dfrac{\partial \mathcal{L}}{\partial q_i'} - \dfrac{d}{dt} \left(\dfrac{\partial \mathcal{L}}{\partial \dot q_i'}\right)\right]\dfrac{\partial q_i'}{\partial q_i} = 0
{% end %}

Which means that _either_ one of the two following statements must be true:

{% math() %}
\dfrac{\partial \mathcal{L}}{\partial q_i'} - \dfrac{d}{dt} \left(\dfrac{\partial \mathcal{L}}{\partial \dot q_i'}\right) = 0 \quad \text{or} \quad \dfrac{\partial q_i'}{\partial q_i} = 0
{% end %}

But if the second is true, that means $q_i'$ is _independent_ of $q_i$, which would be a logical contradiction, because it would imply that $q_i'$ _can't be expressed_ as a coordinate transform of $q_i$. Thus, the only possibility is the first, meaning that under a _valid_ coordinate transformation, the Lagrangian expressed in transformed coordinates still follows the same Euler-Lagrange equations:

{% math() %}
\dfrac{\partial \mathcal{L}}{\partial q_i'} - \dfrac{d}{dt} \left(\dfrac{\partial \mathcal{L}}{\partial \dot q_i'}\right) = 0
{% end %}

It may have taken a long way, but we have now *proved* the result that the Euler-Lagrange equations of motion are **invariant under coordinate transformations**. Why is this meaningful? Aside from the fact that it permits us to shift our coordinates by an additive constant (which is very helpful, for instance, if we want to define our potential energy relative to a specific reference point), it also means that **we can choose arbitrary coordinates** to express the Lagrangian; the choice of coordinates has **no effect** on the equations of motion. Thus, we can freely choose whichever coordinates are most suitable for the problem - polar coordinates for rotational symmetry, spherical coordinates for spherical symmetry, and so forth. By contrast, we _don't_ have the freedom to choose our coordinates for Newton's differential equation (second law) $m \ddot{\mathbf{r}} = \mathbf{F}(\mathbf{r}, t)$, which changes form under coordinate transformations, meaning that there are all sorts of fictitious "forces" that we have to account for. The ability to generalize to all sorts of coordinate systems is a strength of Lagrangian mechanics that is absent from Newtonian mechanics, and makes it especially powerful in solving difficult problems.

### Constraints and generalized coordinates

We have seen that due to the invariance of the Euler-Lagrange equations under coordinate of transformations, we may always choose the most suitable coordinates for a problem. Now, let's ask ourselves a curious question: how many coordinates, exactly, do we need? It would appear that for a 3D problem that involves $n$ particles, we would need $3n$ coordinates (and therefore $3n$ Euler-Lagrange equations) to completely describe the motion of all the particles. However, the answer is not so simple, because the coordinates may not be independent from each other. Indeed, in many problems, we find that our coordinates are _related_ by some form of constraint. We will consider a few problems before analyzing the general case to illustrate what this means.

Consider the problem of a mass $m$ traveling around the origin in uniform circular motion at constant radius $R$. That is to say, the particle is **constrained** to move in a circle of radius $R$, which we can write as:

{% math() %}
\begin{align*}
x = R\cos \theta \\
y = R\sin \theta
\end{align*}
{% end %}

where:

{% math() %}
r^2 = x^2 + y^2 = R^2
{% end %}

We can choose to use conventional $(x, y)$ coordinates to solve the problem, but due to the symmetries of the problem arising from the _constraint on the system_, that is, $r = \text{const.}$ it is easier to use the angular coordinate $\theta$, since we know that (a) the problem is 2D, so there are are two nominal degrees of freedom but (b) the constraint reduces the two degrees of freedom to just *one* coordinate $\theta$ that is sufficient for the complete description of the system. Recall that the Lagrangian in 2D for a free particle is conventionally given by:

{% math() %}
\mathcal{L} = \dfrac{1}{2} m (\dot x^2 + \dot y^2)
{% end %}

Since we have our constraints $x = R \cos \theta(t)$ and $y = R \sin \theta(t)$, where $\theta = \theta(t)$ (as it is a _coordinate_ which is a variable, not a constant), by differentiating we have $\dot x = -R \sin \theta \dot \theta$ and $\dot y =  R \cos \theta \dot \theta$, and $\dot x^2 + \dot y^2 = (-R\sin \theta \dot \theta)^2 + (R \cos \theta \dot \theta)^2 = R^2 \dot \theta^2$. Thus:

{% math() %}
\mathcal{L} = \dfrac{1}{2} m R^2 \dot \theta^2
{% end %}

Our Euler-Lagrange equation for our only coordinate $\theta$ reads:

{% math() %}
\begin{align*}
\dfrac{\partial \mathcal{L}}{\partial \theta} - \dfrac{d}{dt} \left(\dfrac{\partial \mathcal{L}}{\partial \dot \theta}\right) = 0
\end{align*}
{% end %}

Which, after taking the partial derivatives (we have $\dfrac{\partial \mathcal{L}}{\partial \theta} = 0$ and $\dfrac{\partial \mathcal{L}}{\partial \dot \theta} = m R^2 \dot \theta$) and substituting, we get:

{% math() %}
m R^2 \ddot \theta = 0 \quad \Rightarrow \quad \ddot \theta = 0
{% end %}

Which has the solution:

{% math() %}
\theta(t) = \theta_0 + \omega_0 t
{% end %}

Similarly, consider a ball of mass $m$ that is confined to move along a bar that rotates around the $xy$ plane with constant angular velocity $\omega$. Thus we have the constraint that the ball is confined to travel along the bar:

{% math() %}
x(t)^2 + y(t)^2 = r(t)^2
{% end %}

Where $r(t) \neq \text{const.}$ but is subject to the above constraint. Meanwhile, we also note that due to the constraint, we have $\theta(t) = \omega t$. 

{% math() %}
\begin{align*}
x &= r(t) \cos \theta(t) \\
&= r(t) \cos \omega t \\
y &= r(t) \sin \theta(t) \\
&= r(t) \sin \omega t
\end{align*}
{% end %}

Thus we have, for $\dot x$ and $\dot y$:

{% math() %}
\begin{align*}
\dot x = \dot r \cos \omega t - r\omega \sin \omega t \\
\dot y = \dot r \sin \omega t + r\omega \cos \omega t
\end{align*}
{% end %}

Where here we must use the product rule when differentiating since $r$ is a _function_ of $t$, not a constant. Substituting into the Lagrangian, we have:

{% math() %}
\begin{align*}
\mathcal{L} &= \dfrac{1}{2} m(\dot x^2 + \dot y^2) \\
&= \dfrac{1}{2} m [(\dot r \cos \omega t - r\omega \sin \omega t)^2 + (\dot r \sin \omega t + r\omega \cos \omega t)^2] \\
&= \dfrac{1}{2} m[\dot r^2 \cos^2 \omega t - 2 \dot r r \omega \sin \omega t \cos \omega t + r^2 \omega^2 \sin^2 \omega t \\
&\quad \quad + \dot r \sin^2 \omega t + 2\dot r r \omega\sin \omega t \cos \omega t + r^2 \omega^2 \cos^2 \omega t] \\
&=\dfrac{1}{2} m[\dot r\cos^2 \omega t \cancel{- 2 \dot r r \sin \omega t \cos \omega t + 2\dot r \sin \omega t \cos \omega t} + 2 r^2 \omega^2 \sin^2 \omega t] \\
&= \dfrac{1}{2} m(\dot r^2 \cos^2 \omega t + \dot r \sin^2 \omega t + r^2 \omega^2 \sin^2 \omega t) \\
&= \dfrac{1}{2} m(\dot r^2 \cancel{(\cos^2 \omega t + \sin^2 \omega t)}^1 + r^2 \omega^2 \cancel{(\sin^2 \omega t)}^1 \\
&= \dfrac{1}{2} m (\dot r^2 + r^2 \omega^2)
\end{align*}
{% end %}

Let us now take a careful look at our Lagrangian and write it in a form that reveals more information about the physics of the problem:

{% math() %}
\begin{align*}
\mathcal{L} &= \dfrac{1}{2} m(\dot r^2 + r^2 \omega^2) \\
&= \underbrace{\dfrac{1}{2} m\dot r^2}_\text{standard kinetic energy} + \underbrace{\dfrac{1}{2} m r^2 \omega^2}_\text{angular kinetic energy}
\end{align*}
{% end %}

Thus we find that our Lagrangian consists of a kinetic energy and angular kinetic energy term; this second angular kinetic energy term is what we would consider the "centripetal force" in Newtonian mechanics. Since we only have one coordinate, that is, $r(t)$, we only have one Euler-Lagrange equation:

{% math() %}
\dfrac{\partial \mathcal{L}}{\partial r} - \dfrac{d}{dt} \left(\dfrac{\partial \mathcal{L}}{\partial \dot r}\right) = 0
{% end %}

Which, after the taking the derivatives and substitution, results in:

{% math() %}
\ddot r^2 + \omega^2 r = 0
{% end %}

This is simply the differential equation of simple harmonic motion and therefore has a general solution in the form:

{% math() %}
r(t) = A \cos \omega t + B \sin \omega t
{% end %}

From both problems, we have found a shared (and universal) principle: a constrained system arises when there are two or more coordinates that are dependent on each other, as they are related by some type of constraint. When this occurs, we may eliminate the inter-dependent coordinates until only independent coordinates remain. The coordinates left are called the **generalized coordinates**, and they are the most suitable set of coordinates to completely describe the motion of each object in the system.

So, to answer our question at the start, an *unconstrained* 3-dimensional system of $n$ bodies would indeed require $3n$ generalized coordinates to completely describe the motion of each object in the system, but a *constrained* 3-dimensional system of $n$ bodies with $m$ constraints would only require $3n-m$ generalized coordinates. This is a specific case (in 3 dimensions) of a more general principle:

> **A constrained $n$-body system in $k$ dimensions with $m$ constraints needs $kn-m$ generalized coordinates to describe the motion of all bodies in the system. The number of generalized coordinates is equal to the _degrees of freedom_ of the system.**

This is why, in the case of uniform circular motion, which was a one-body system in two dimensions (so $n=1, k = 2$), our single constraint $x^2 + y^2 = R^2$ reduced the number of coordinates from our two original coordinates $x, y$ to $kn -m = (2)(1) - (1) = 1$ coordinate $\theta$. The number of Euler-Lagrange equations is always equal to the number of coordinates, and since we only had one generalized coordinate, we only needed one Euler-Lagrange equation and thus ended up with one equation of motion ($\ddot \theta = 0$).

We will now prove _why_ that is the case. To start, there are _two general kinds_ of constraints: constraints that are holomonic and non-holomonic constraint. A _non-holonomic constraint_ is a function that relates position, velocity and time (here we use generalized coordinates $x_i, \dot x_i$):

{% math() %}
F(x_i, \dot x_i, t)  = 0
{% end %}

A holomonic constraint has a stricter requirement that we will now examine. A general constraint can also be written in the form:

{% math() %}
\sum_i A_i \dot x_i + B = 0
{% end %}

This is in general _non-integrable_ with the _exception_ if:

{% math() %}
\begin{matrix*}
A_i = \dfrac{\partial}{\partial x_i} f(x_i, t),
& B = \dfrac{\partial}{\partial t}f(x_i, t)
\end{matrix*}
{% end %}

Therefore, substituting, we have:

{% math() %}
\sum_i A_i \dot x_i + B = \sum_i \dfrac{\partial f}{\partial x_i}\dot x_i + \dfrac{\partial f}{\partial t} = 0 \Rightarrow \dfrac{d f(x_i, t)}{dt} = 0
{% end %}

Where $\dfrac{d f(x_i, t)}{dt} = 0$ is a _total derivative_. Therefore, a holomonic constraint _with this specific restriction_ must then satisfy $f = f(x_i, t) = 0$ and naturally leads to integrability.

But what if the constraint is non-holomonic? We may then use the method of _Lagrange multipliers_, which are a natural way to express constraints in a mathematical form. Consider a Lagrangian written in an equivalent form:

{% math() %}
\begin{align*}
\tilde{\mathcal{L}} &= \mathcal{L} + \sum_i \lambda_i F_i \\ 
&=\mathcal{L}(x_i, \dot x_i, t) + \sum_i \lambda_i F_i(x_i, \dot x_i, t)
\end{align*}
{% end %}

where $F_i$ is a generalized constraint (i.e. we can have several constraints $F_1, F_2, \dots F_n$ that we represent with the generalized $F_i$) and $\lambda_i$ is a _Lagrange multiplier_. (And yes, this is the same thing as the Lagrange multiplier that we encounter in [introductory multivariable calculus](@/multivariable-calculus/index.md)). It may not be obvious _why_ this is equivalent to the standard Lagrangian $\mathcal{L}(x_i, \dot x_i, t)$. But remember that we saw that a non-holonomic constraint obeys:

{% math() %}
F_i (x_i, \dot x_i, t) = 0
{% end %}

Therefore if we substitute the Lagrangian $\tilde{\mathcal{L}}$ into the Euler-Lagrange equations, we have

{% math() %}
\dfrac{\partial \mathcal{L}}{\partial \dot x_i} + \dfrac{d}{dt} \left(\dfrac{\partial \mathcal{L}}{\partial \dot x_i}\right)
- \sum_i \left(\lambda_i(t) \dfrac{\partial F_i}{\partial x_i}
- \dfrac{d}{dt}\left[\lambda_i(t) \dfrac{\partial F_i}{\partial \dot x_i}\right]\right) = 0
{% end %}

This is the _generalized Euler-Lagrange equation_ that incorporates the non-holomonic constraints $F_i(x, \dot x_i, t)  = 0$. But the _much easier_ and completely equivalent form (remember, because of how we showed that the Euler-Lagrange equation is symmetric under transformations) is given by:

{% math() %}
\dfrac{\partial \tilde{\mathcal{L}}}{\partial q_i} - \dfrac{d}{dt} \left(\dfrac{\partial \tilde{\mathcal{L}}}{\partial \dot q_i}\right) = 0
{% end %}

Thus, by simply using the modified version of the Euler-Lagrange equations that contains a transformed Lagrangian $\mathcal{L} \to \mathcal{L} + \sum_i \lambda_i F_i$, we are able to solve for constrained systems (relatively) straightforwardly!

### Rolling without slipping with constraints

Consider a problem where this form of the Euler-Lagrange equation is very useful: the problem of a rolling disk of radius $R$ and mass $m$ moving along the $x$ axis that **rolls without slipping** down an inclined plane due to static friction between the disk and the plane. For this problem, we choose our $x$ axis to be parallel to the surface of the inclined plane. The inclined plane is angled at angle $\phi = \text{const.}$ with respect to the horizontal:

{{ diagram(
src="../rolling-without-slipping-lagrangian.excalidraw.svg"
desc="A diagram showing a disk of radius R rolling down an inclined plane, where the x coordinate points down the plane and is parallel to it, and where theta is the angle of the disk's rotation"
)}}

The consequence of rolling without slipping is that the translational velocity $v_t$ is equal to the rotational velocity about the center of mass $v_{CM}$ (see the [classical dynamics guide](@/classical-dynamics.md) for more in-depth explanations on why this is the case). We therefore have:

{% math() %}
v_t = v_{CM}
{% end %}

But we also know that $v_t = \dot x$ (since it is translational i.e. along the $x$ axis) and $v_{CM} = R\dot \theta$. Thus we have:

{% math() %}
\begin{align*}
\dot v &= R \dot \theta \\ &\Rightarrow \int \dot x \, dt 
= \int R\, \dot \theta\, dt \\
& \Rightarrow x =  R \theta
\end{align*}
{% end %}

Thus our constraint $f$ can be written as $f(x, \theta) = x - R \theta = 0$, and thus with a rearrangement and differentiating both sides, we have $\dot x = R \dot \theta$. We may now write down the kinetic and potential energies:

{% math() %}
\begin{align*}
K &= \dfrac{1}{2} m \dot x^2 + \dfrac{1}{2} I \underbrace{\omega^2}_{\dot \theta^2} \\
U &= mg(L - x) \sin \phi
\end{align*}
{% end %}

Where $I$ is the moment of inertia, and for our disk it is $I = \dfrac{1}{2} mR^2$ about its axis of rotation. Thus we have:

{% math() %}
\begin{align*}
\mathcal{L} &= K - U \\
&= 
\dfrac{1}{2} m \dot x^2 + \dfrac{1}{2} I \dot \theta^2 -mg(L - x) \sin \phi
\end{align*}
{% end %}

This is, however, not the most optimal set of coordinates, because it involves two coordinates $(x, \theta)$, but $x$ and $\theta$ are _not_ independent coordinates, since (as we found before) we had $\dot x = R \dot \theta$. Therefore, the _generalized coordinates_ of the problem - the set of the most optimal _independent_ coordinates - would be given by just one coordinate $\theta$. If we substitute in our constraint $\dot x = R \dot \theta$ (and the associated non-differential form $x = R \theta$), then we have:

{% math() %}
\begin{align*}
\mathcal{L} &= \dfrac{1}{2} m R^2 \dot \theta^2 + \dfrac{1}{2} I \dot \theta^2 -mg(L - R \theta) \sin \phi \\
&= \dfrac{1}{2} m R^2 \dot \theta^2 + \dfrac{1}{2} I \dot \theta^2 -mgL \sin \phi + mg R \theta \sin \phi 
\end{align*}
{% end %}

Remember that any constant-valued terms can always be dropped from the Lagrangian, so the $mgL \sin \phi$ term is not _technically_ necessary, so we can drop it to get:

{% math() %}
\mathcal{L} = \dfrac{1}{2} m R^2 \dot \theta^2 + \dfrac{1}{2} I \dot \theta^2 + (mg R \sin \phi)\theta
{% end %}

We can then take the derivatives, find the Euler-Lagrange equations, and thereby get the equations of motion. This is indeed _one way_ to solve the problem, and it does give all the correct results: to use our constraints to reduce the number of coordinates into the least number necessary to describe the system. In this case, our remaining set of coordinates automatically *incorporates* our constraints.

But the more powerful way to solve is using the Lagrange multipliers. This is possible because our constraint is _holonomic_ in nature. To use the method of Lagrange multipliers, we write a transformed Lagrangian in the form $\tilde{\mathcal{L}} = \mathcal{L} + \sum_n \lambda_n F_n$, where $F_n = F_1, F_2, \dots$ are equations in the form $F(q, \dot q, t) = 0$ that express each of the constraints in terms of the coordinates. From this transformed Lagrangian, the Euler-Lagrange equations become:

{% math() %}
\dfrac{d}{dt} \left(\dfrac{\partial \tilde{\mathcal{L}}}{\partial \dot q_i}\right) - \dfrac{\partial \tilde{\mathcal{L}}}{\partial q_i} = 0
{% end %}

We can alternatively write the modified Euler-Lagrange equations for Lagrange multipliers in terms of the original Lagrangian:

{% math() %}
\dfrac{d}{dt} \left(\dfrac{\partial \mathcal{L}}{\partial \dot q_i}\right) - \dfrac{\partial \mathcal{L}}{\partial q_i} - \sum_n \lambda_n \dfrac{\partial F}{\partial q_i} = 0
{% end %}

Where our original Lagrangian, remember, was:

{% math() %}
\begin{align*}
\mathcal{L} &= \dfrac{1}{2} m \dot x^2 + \dfrac{1}{2} I \dot \theta^2 -mg(L - x) \sin \phi \\
&=\dfrac{1}{2} m \dot x^2 + \dfrac{1}{2} I \dot \theta^2 + mg\,x \sin \phi
\end{align*}
{% end %}

(We dropped the constant-valued term as we did before). Since we only have one constraint, we have only one Lagrange multiplier, so we have:

{% math() %}
\dfrac{d}{dt} \left(\dfrac{\partial \mathcal{L}}{\partial \dot q_i}\right) - \dfrac{\partial \mathcal{L}}{\partial q_i} - \lambda \dfrac{\partial F}{\partial q_i} = 0
{% end %}

Remember that $F(q, \dot q, t) = 0$ is the standard form of a constraint here, so in our case that would be $F(x, \theta) = x - R \theta = 0$. If we find the derivatives of our (untransformed) Lagrangian using the modified Euler-Lagrange equations we showed above and substitute them in (not shown here), the equations of motion we find are given by:

{% math() %}
\begin{align*}
m \ddot x - mg \sin \phi - \lambda = 0 \\
I \ddot \theta + R \lambda = 0
\end{align*}
{% end %}

Let us now solve for $\lambda$. By rearranging the second equation we have $\lambda = -\dfrac{I\ddot x}{R^2}$. Combining this with the first equation, we have:

{% math() %}
\begin{gather*}
\ddot x \left(m + \dfrac{I}{R^2}\right) = mg \sin \phi \\
\ddot x = \dfrac{mg \sin \phi}{m + I/R^2} = \text{const.} \\
\lambda = -\dfrac{I\ddot x}{R^2} = -\dfrac{I}{R^2}\dfrac{mg \sin \phi}{m + I/R^2}
\end{gather*}
{% end %}

As our object is a rolling disk, which has $I = \dfrac{1}{2} mR^2$, the Lagrange multiplier $\lambda$ and our expression for $\ddot x$ become respectively:

{% math() %}
\begin{align*}
\ddot x &= \dfrac{mg\sin \phi}{m + \frac{1}{2} mR^2/R^2} = \dfrac{2}{3} g \sin \phi \\
\lambda &= -\dfrac{I \ddot x}{R^2} = -\dfrac{1}{3} mg \sin \phi
\end{align*}
{% end %}

But notice that the units of $\lambda$ are in fact that of _force_. So this suggests a physical interpretation for $\lambda$ - it gives the _force of friction_ that is maintaining the disk's motion to roll without slipping! Indeed, this is why we denoted our constraint as $F(q_i, \dot q_i, t)$ earlier, because the constraint often represents a _constraint force_. The constraint force here - friction - _modifies_ the disk's trajectory such that its original equation of motion $\ddot x = g\sin \phi$ becomes $\ddot x = g \sin \phi + \lambda/m = \dfrac{2}{3} g \sin \phi$. Note that we would not be able to find this critical aspect of the system if we just solved in the standard Lagrangian method (that we showed before doing Lagrange multipliers) where we only substitute in the constraint! This gives a major advantage to solving constrained systems with Lagrangian mechanics: by incorporating the constraints as _Lagrange multipliers_, we can give physical interpretations as to what is _causing_ the constraint rather than second-guessing ourselves.

## Noether's theorem: conservation laws from Lagrangian mechanics 

We know from Newtonian mechanics that there exist certain **conserved quantities**, most particularly energy, momentum, and angular momentum. We will now show how these follow naturally in Lagrangian mechanics if we take the Lagrangian to satisfy some specific conditions, and thus resultingly have a Lagrangian in a particular form.

> **Note:** This is also known as **Noether's theorem**, by the mathematician [Emmy Noether](https://en.wikipedia.org/wiki/Emmy_Noether). If you have time, I highly recommend reading more about Noether; she is certainly one of greatest mathematicians in history and her story as a female and Jewish mathematician in the 19th century makes it all the more impressive.

### Energy conservation

For energy conservation, **four conditions** are required, and they are all interrelated:

| Conserved quantity | Required condition # | Necessary condition (s)                        | Textual description                                                                                                                                                                                                                                                                                                                     |
| ------------------ | -------------------- | ---------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Energy             | 1                    | $\dfrac{\partial \mathcal{L}}{\partial t} = 0$ | Lagrangian is _invariant_ under a transformation in time. **Note:** this does **not** mean $\mathcal{L}$ is time-independent, but it does mean that the Lagrangian is *constant* in time. That is to say, changes in kinetic energy must be countered by changes in potential energy such that $\mathcal{L}$ does not change in time)_. |
| Energy             | 2                    | $K = f(\dot q_i)$                              | The kinetic energy is a function of the time-derivatives of generalized coordinates $\dot q_i$ _only_, and does not depend on time or $q_i$.                                                                                                                                                                                            |
| Energy             | 3                    | $U = f(q_i)$                                   | The potential energy is only dependent on the generalized coordinates $q_i$, _not_ on time or $\dot q_i$. That is, the potential energy is velocity- and time-independent                                                                                                                                                               |
| Energy             | 4                    | $F_i(\dot q, \dot q_i) = 0$                    | There are no time-dependent constraints on the system.                                                                                                                                                                                                                                                                                  |

We may thus write the generalized Lagrangian for a time-invariant Lagrangian that conserves energy as:

{% math() %}
\begin{align*}
\mathcal{L} &= \mathcal{L}(q_i, \dot q_i) \\
&= \sum_j \sum_i a_{ij} \dot q_i \dot q_j - U(q_i) \\
&= \sum_j \sum_i\underbrace{a_{ij} \dot q_i \dot q_j}_\text{kinetic} - \underbrace{U(q_i)}_\text{potential}
\end{align*}
{% end %}

Where $a_{ij}$ is a coefficient matrix that ensures the units for kinetic energy are consistent - in the special case of Cartesian coordinates, we have $a_{ij} = \dfrac{1}{2} m \delta_{ij}$ which reproduces the familiar expression $K = \dfrac{1}{2} m (\dot x^2 + \dot y^2 + \dot z^2)$.

> **Note:** we can write our time-invariant Lagrangian more compactly using the Einstein summation convention as $\mathcal{L}(q_i, \dot q_i)=a_{ij} \dot q^i \dot q^j - U(q_i)$. Note that we work in Euclidean space so $\dot q^i = \dot q_i$. We will however put the sums back in during the remaining portions of this section for clarity. The expression for the Lagrangian is _not necessarily_ $K - U$ in other coordinate systems.

We may show that this is indeed invariant of time as follows. If we take $\dfrac{\partial {\mathcal{L}}}{\partial t}$, and _if_ we assume that the Lagrangian is the form above, we find that:

{% math() %}
\begin{align*}
\dfrac{\partial \mathcal{L}}{\partial t} &= \dfrac{\partial}{\partial t}\mathcal{L}(q_i, \dot q_i) \\
&= \sum_i \dfrac{\partial \mathcal{L}}{\partial q_i} \dot q_i + \dfrac{\partial \mathcal{L}}{\partial \dot q_i} \ddot q_i \\
&= \sum_i \left[\dfrac{d}{dt}\left(\dfrac{\partial \mathcal{L}}{\partial \dot q_i}\right)\right]q_i + \dfrac{\partial \mathcal{L}}{\partial \dot q_i} \ddot q_i
\end{align*}
{% end %}

Note that the last step follows from the Euler-Lagrange equations $\dfrac{\partial \mathcal{L}}{\partial q_i} = \dfrac{d}{dt} \left(\dfrac{\partial \mathcal{L}}{\partial q_i}\right)$. Now, if we apply the product rule backwards, we can find that the previous expression arises from taking the (total) derivative of:

{% math() %}
\dfrac{\partial \mathcal{L}}{\partial t} =\sum_i \underbrace{\left[\dfrac{d}{dt}\left(\dfrac{\partial \mathcal{L}}{\partial \dot q_i}\right)\right]q_i + \dfrac{\partial \mathcal{L}}{\partial \dot q_i} \ddot q_i}_\text{expanded product rule} = \underbrace{\dfrac{d}{dt} \left[\dot q_i \dfrac{\partial \mathcal{L}}{\partial \dot q_i}\right]}_\text{total derivative}
{% end %}

Therefore we have:

{% math() %}
\begin{align*}
\dfrac{\partial \mathcal{L}}{\partial t} = \dfrac{d}{dt} \left[\dot q_i \dfrac{\partial \mathcal{L}}{\partial \dot q_i}\right] \\
\dfrac{d}{dt} \left[\dot q_i \dfrac{\partial \mathcal{L}}{\partial \dot q_i}\right] - \dfrac{d\mathcal{L}}{dt} = 0 \\
\dfrac{d}{dt} \left[\dot q_i \dfrac{\partial \mathcal{L}}{\partial \dot q_i} - \mathcal{L}(q_i, \dot q_i)\right] = 0
\end{align*}
{% end %}

But if the derivative is zero, then the quantity in the brackets must be a constant! We call this constant the **Hamiltonian**, and it has units of energy:

{% math() %}
H(q_i, \dot q_i) = \dot q_i \dfrac{\partial \mathcal{L}}{\partial \dot q_i} - \mathcal{L}(q_i, \dot q_i)
{% end %}

It is tempting to call this constant the **total energy**, and in the case of a Lagrangian that is invariant in transformations of time this is indeed true (although not true in the general case when the Lagrangian does change in time. But let us rigorously show that the Hamiltonian is the total energy when we have a time-invariant Lagrangian. To do so, recall that our time-invariant Lagrangian is given by:

{% math() %}
\mathcal{L}(q_i, \dot q_i)= \sum_j \sum_i a_{ij} \dot q_i \dot q_j - U(q_i)
{% end %}

Thus, if we explicitly compute the first term of the Hamiltonian $\dot q_i \dfrac{\partial \mathcal{L}}{\partial \dot q_i}$, we have:

{% math() %}
\begin{align*}
\dot q_i \dfrac{\partial \mathcal{L}}{\partial \dot q_i} &= \dot q_i \dfrac{\partial}{\partial \dot q_i}\bigg[\underbrace{\sum_j \sum_i}_\text{dummy indices} a_{ij} \dot q_i \dot q_j - U(q_i)\bigg] \\
&= \dot q_i \dfrac{\partial}{\partial \dot q_i}\bigg[\underbrace{\sum_i a_{ii} \dot q_i \dot q_i}_\text{change indices} - U(q_i)\bigg] \\
&= 2\dot q_i \underbrace{a_{ii}}_\text{const.}\sum_i \dot q_i  \\
&= 2 \sum_i \sum_j a_{ij} \dot q_i  \dot q_j \\
&= 2K
\end{align*}
{% end %}

Thus we have obtained the important result $\dot q_i \dfrac{\partial \mathcal{L}}{\partial \dot q_i} = 2K$, that is, _twice the kinetic energy_. Note that in the previous steps, since $i, j$ are dummy indices (summation indices), we can freely swap/rename them, compute the derivative, and then swap them back - it does not change the mathematics at all. In addition, we were able to factor out $a_{ii}$ due to the fact that it is a _constant-coefficient matrix_ that ensures the kinetic energy has the correct units. Substituting our results into the Hamiltonian, we have:

{% math() %}
\begin{align*}
H(q_i, \dot q_i) &= \dot q_i \dfrac{\partial \mathcal{L}}{\partial \dot q_i} - \mathcal{L}(q_i, \dot q_i) \\
&= 2K - (K - U) \\
&= K + U \\
& = E
\end{align*}
{% end %}

Thus we have shown that _when the Lagrangian is constant in time_, the Hamiltonian reduces to the **total energy** of the system.

### Momentum conservation

For momentum conservation, unlike energy conservation, we have only one requirement for the Lagrangian:

| Conserved quantity | Required condition # | Necessary condition (s)                          | Textual description                                                                                                                              |
| ------------------ | -------------------- | ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| Momentum           | 1                    | $\dfrac{\partial \mathcal{L}}{\partial q_i} = 0$ | The Lagrangian is invariant under translations in space (again, it _can_ have spatial dependence, but the Lagrangian must be _constant_ in time) |

Let us show why this is the case. If we substitute the momentum conservation relation into the Euler-Lagrange equations, we have:

{% math() %}
\begin{align*}
\dfrac{d}{dt} \left(\dfrac{\partial \mathcal{L}}{\partial \dot q_i}\right) &= \dfrac{\partial \mathcal{L}}{\partial q_i} \\
\dfrac{d}{dt} \left(\dfrac{\partial \mathcal{L}}{\partial \dot q_i}\right) &= \cancel{\dfrac{\partial \mathcal{L}}{\partial q_i}}^0 \\
\dfrac{d}{dt} \underbrace{\left(\dfrac{\partial \mathcal{L}}{\partial \dot q_i}\right)}_\text{constant} &= 0
\end{align*}
{% end %}

Again, since the derivative of a constant is zero, then the quantity inside the brackets $\dfrac{\partial \mathcal{L}}{\partial \dot q_i}$ must be a **constant**. We call this quantity the **generalized momentum**, and we express it as:

{% math() %}
p_i = \dfrac{\partial \mathcal{L}}{\partial \dot q_i}
{% end %}

Note that if we substitute $p_i = \dfrac{\partial \mathcal{L}}{\partial \dot q_i}$ into $\dfrac{d}{dt} \left(\dfrac{\partial \mathcal{L}}{\partial \dot q_i}\right)$ we have:

{% math() %}
\dfrac{dp_i}{dt} = 0
{% end %}

We can write it in a more suggestive form as:

{% math() %}
\dfrac{\vec dp}{dt} = \vec F = 0
{% end %}

Therefore, we come to the conclusion that when the _total (net) force on a system is zero_, we have the **conservation of momentum**, just as we'd expect from Newton's laws. 

### Angular momentum conservation

From the generalized momentum and examining a special case, we can show that _angular momentum_ is also a conserved quantity. Consider a (simple) pendulum of mass $m$ hanging on a string of length $\ell$, where $y$ is the horizontal (left-right) and $x$ is the vertical (up-down) axis where $+x$ points in the _downwards_ direction. We therefore have $x = \ell \sin \theta, y = -\ell \cos \theta$ and $U = mgy = -mg \ell \cos \theta$ and thus we find that the Lagrangian becomes:

{% math() %}
\mathcal{L} = \dfrac{1}{2} m \ell^2 \dot \theta^2 + mgl \cos \theta
{% end %}

In this case we have $\dfrac{\partial \mathcal{L}}{\partial \theta} = -mg\ell \sin \theta \neq 0$, so momentum is definitely not conserved. But note that if we compute the generalized momentum, we find that:

{% math() %}
p_i = \dfrac{\partial \mathcal{L}}{\partial \dot \theta} = m \ell^2 \dot \theta
{% end %}

Thus, even though momentum is _not_ conserved, we still have a generalized momentum that is _independent of time_ (and thus $\dfrac{dp_i}{dt} = 0$).  Notice that in this case the generalized momentum depends on the $\dot \theta$ coordinate, and therefore the generalized momentum "points" in the $\theta$ direction. Thus, we call $p_i$ a special name - the **angular momentum**, and this is indeed _conserved_.

> **Note:** the simple (free) pendulum also obeys _energy_ conservation. However, a _driven pendulum_ (where the pendulum is driven by an external force that produces acceleration $a$) _does not_ obey energy conservation.

We may derive the conservation of angular momentum in the more general case by requiring that the Lagrangian exhibit **invariance under rotations**. For this, consider transforming the Lagrangian $\mathcal{L}$ such that:

{% math() %}
\mathcal{L}(\mathbf{r}) \to \mathcal{L}(\mathbf{r} + d\vec \theta \times \dot{\mathbf{r}})
{% end %}

It may not be obvious at first as to how this describes a rotation. But remember that when an object undergoes rotation, the infinitesimal _arc length_ it traverses is $d\mathbf{r} = d\vec \theta \times \mathbf{r}$ (this comes from the arc length formula $s = r \theta$). Thus, if we shift the Lagrangian with our infinitesimal rotation, the difference between the transformed Lagrangian and the original Lagrangian is given by:

{% math() %}
\begin{align*}
d\mathcal{L} &= \mathcal{L}(\mathbf{r} + d\mathbf{r}) - \mathcal{L}(\mathbf{r}) \\
&=\mathcal{L}(\mathbf{r} + d\vec \theta \times \mathbf{r}) - \mathcal{L}(\mathbf{r})
\end{align*}
{% end %}

Which we can write in terms of coordinates $x_i$ as:

{% math() %}
d\mathcal{L} = \mathcal{L}(x_i + d\vec \theta \times x_i) - \mathcal{L}(x_i)
{% end %}

Now, we also know (from the total differential formula in multivariable calculus) that:

{% math() %}
d\mathcal{L} = \sum_i \dfrac{\partial \mathcal{L}}{\partial x_i} dx_i + \dfrac{\partial \mathcal{L}}{\partial \dot x_i} d\dot x_i
{% end %}

This may not look all that enlightening yet. But remember that in our definitions of the generalized momentum, we said that:

{% math() %}
\begin{matrix*}
p_i = \dfrac{\partial \mathcal{L}}{\partial \dot x_i}, & \dot p_i = \underbrace{\dfrac{d}{dt} \left(\dfrac{\partial \mathcal{L}}{\partial \dot x_i}\right) =\dfrac{\partial \mathcal{L}}{\partial x_i}}_\text{from Euler-Lagrange eqs.}
\end{matrix*}
{% end %}

The second identity may be slightly confusing, but the reason why the time derivative of the generalized momentum is equal to the spatial derivative of the Lagrangian is due to the Euler-Lagrange equations:

{% math() %}
\dfrac{\partial \mathcal{L}}{\partial x_i} = \dfrac{d}{dt} \left(\dfrac{\partial \mathcal{L}}{\partial \dot x_i}\right)
{% end %}

Thus, substituting our definitions, we can rewrite our expression for the total differential of the Lagrangian as:

{% math() %}
\begin{align*}
d\mathcal{L} &= \sum_i \dfrac{\partial \mathcal{L}}{\partial x_i} dx_i + \dfrac{\partial \mathcal{L}}{\partial \dot x_i} d\dot x_i \\
&= \sum_i \dot p_i\, dx_i + p_i\, d\dot x_i \\
&= \sum_i \underbrace{\dfrac{d}{dt} (p_i \, dx_i)}_\text{reverse product rule}
\end{align*}
{% end %}

Where in the last line, we applied the product rule in reverse to collapse the two terms into one term. To make this result more illustrative, note that in more conventional vector notation it can also be written as:

{% math() %}
d\mathcal{L} = \dfrac{d}{dt}(\mathbf{p} \cdot d\mathbf{r}) = \dfrac{d}{dt}(\mathbf{p} \cdot (d\vec \theta \times \mathbf{r})) = d\vec \theta \cdot \dfrac{d}{dt} (\mathbf{r} \times \mathbf{p})
{% end %}

Where the last simplification comes from the vector triple product identity $\mathbf{A} \cdot (\mathbf{B} \times \mathbf{C}) = \mathbf{B} \cdot (\mathbf{C} \times \mathbf{A})$. Now, since we required that our Lagrangian stays _invariant_ under rotational transformations, then $d\mathcal{L}$ _must_ be zero. Thus:

{% math() %}
d\mathcal{L} = d\vec \theta \cdot \dfrac{d}{dt} (\mathbf{r} \times \mathbf{p}) = 0
{% end %}

This can either be true if $d\vec \theta = 0$ (but that would be nonsensical since that means there wasn't any rotation!) _or_ if $\dfrac{d}{dt}(\mathbf{r} \times \mathbf{p}) = 0$. It is the latter case which is important to us, because whenever a derivative is zero, that can only mean that we have a constant:

{% math() %}
\dfrac{d}{dt}(\mathbf{r} \times \mathbf{p}) = 0 \Rightarrow \mathbf{r} \times \mathbf{p} = \text{const.}
{% end %}

This constant is a vector since the cross product always gives a vector, and it has a familiar name: $\mathbf{L}$, the **angular momentum**. Thus, any system that possesses some form of symmetry about an axis of rotation (.e. uniform circular motion in the $xy$ plane) obeys the **conservation of angular momentum**.

### A summary of Noether's theorem

Based on our derivations, we have seen that the Lagrangian's symmetries under various types of transformations lead to conservation laws. Specifically:

- If the Lagrangian is invariant (constant) in _time_, then the system it describes satisfies the **conservation of energy**
- If the Lagrangian is invariant (constant) in _space_, then the system it describes satisfies the **conservation of momentum**
- If the Lagrangian is invariant (constant) on _rotations_, then the system it describes satisfies the **conservation of angular momentum**

This was the genius realization of Noether: If we demand the **invariance** of the Lagrangian under a particular transformation, a **conserved quantity** always arises. In more general terms, given an arbitrary (smooth) transformation operator $\hat Q$ acting on the Lagrangian, such that $d\mathcal{L} = \hat Q \mathcal{L} - \mathcal{L}$, then if the Lagrangian is _invariant_ under this transformation, that is, if it satisfies $d\mathcal{L} = 0$, then there *must* be a conserved quantity $q$ for which $\dfrac{dq}{dt} = 0$, which we can find by explicitly computing the form of $d\mathcal{L}$ and solving for it being equal to zero. So, rather than just _assuming_ conservation of energy (or momentum or angular momentum), Lagrangian mechanics _shows_ that it comes naturally from the form of the Lagrangian (and therefore of the physical system) itself!

## Hamiltonian mechanics

Previously, we saw the symmetries of the Lagrangian allow defining a **Hamiltonian** that encodes the _energy_ of the system (and in the case of time-invariant systems, _is_ the total mechanical energy of the system). We have previously seen that we were able to transform the Lagrangian $\mathcal{L}(q, \dot q, t)$ into the Hamiltonian $H(q, p_i, t)$ with the following transformation (called a _Legendre transformation_):

{% math() %}
H = \sum_i \dot q_i \underbrace{\dfrac{\partial \mathcal{L}}{\partial \dot q_i}}_{p_i} - \mathcal{L}
{% end %}

Where $p_j = \dfrac{\partial \mathcal{L}}{\partial \dot q_i}$ is the _generalized momentum_. Unlike the Lagrangian, which is a function of position and velocity through time, the Hamiltonian is a function of position and _momentum_, and this is a crucial difference. These two coordinates uniquely determine the state of a system at a given time, and at all future times. In fact, they are so essential that they have a special name: the combined set of the position and momentum coordinates $(q_i, p_i)$ are known as the **canonical coordinates** of the system, and the set of all positions and all momenta $\{q_i(t),\, p_i(t)\}$ for all $t$ is known as the _phase space_. A single particle moving through Cartesian 3D space, for instance, would have 3 position coordinates $x, y, z$ and 3 momentum coordinates $p_x, p_y, p_z$, meaning that it has a total of 6 canonical coordinates and moves through a 6-dimensional phase space.

> **Note:** Be careful to not confuse **generalized coordinates** and **canonical coordinates**. General coordinates come from Lagrangian mechanics, and they are the most optimal number of coordinates that can fully describe the motion of all objects in a system. **Canonical coordinates**, on the other hand, come from Hamiltonian mechanics, and they are the combination of position and momentum coordinates that describes the state of the system as a path in a 6-dimensional (phase) space.

### Deriving Hamilton's equations

We may now show that we can derive equations of motion from the Hamiltonian and our knowledge of Lagrangian mechanics. To do this, we express the velocity in terms of position and momentum, that is $\dot q_i = \dot q_i(q_k, p_k, t)$. Remember we are working in index notation, so $q_k = \mathbf{r}, p_k = \mathbf{p}$, and $\dot q_i$ ranges over each component of the velocity. For instance, in Cartesian coordinate where $i = x, y, z$, then $\dot q_i = \dot q_i(q_k, p_k, t)$ expands to the following:

{% math() %}
\begin{align*}
\dot x = \dot x(\mathbf{r}, \mathbf{p}, t) \\
\dot y = \dot y(\mathbf{r}, \mathbf{p}, t) \\
\dot z = \dot z(\mathbf{r}, \mathbf{p}, t)
\end{align*}
{% end %}

Let us first take the total derivative of the Hamiltonian with respect to time - after all, knowing how the Hamiltonian evolves in time would allow us to determine how the system's energy changes, and perhaps could provide bring us closer to the equations of motion. By the chain rule, we find that:

{% math() %}
\begin{align*}
d H &= \sum_k \left[\dfrac{\partial H}{\partial q_k} dq_k + \dfrac{\partial H}{\partial p_k} dp_k \right] + \dfrac{\partial H}{\partial t} dt \\
\dfrac{dH}{dt} &= \sum_k \left[\dfrac{\partial H}{\partial q_k} \dfrac{dq_k}{dt} + \dfrac{\partial H}{\partial p_k} \dfrac{dp_k}{dt} \right] + \dfrac{\partial H}{\partial t}  \\
&= \sum_k \left[\dfrac{\partial H}{\partial q_k} \dot q_k + \dfrac{\partial H}{\partial p_k} \dot p_k \right] + \dfrac{\partial H}{\partial t}  \\
\end{align*}
{% end %}

Let us now evaluate $\dfrac{\partial H}{\partial q_k}$ and $\dfrac{\partial H}{\partial p_k}$. Remember that the Hamiltonian takes the form $H(q_k, p_k, t) = \dot q_k \dfrac{\partial \mathcal{L}}{\partial \dot q_k} - \mathcal{L}$. Taking the partial derivative with respect to $q_k$, we find that:

{% math() %}
\begin{align*}
\dfrac{\partial H}{\partial q_k} &= p_k \dfrac{\partial \dot q_k}{\partial q_k} - \dfrac{\partial \mathcal{L}}{\partial q_k}
-\underbrace{\dfrac{\partial \mathcal{L}}{\partial \dot q_k}}_{p_k} \dfrac{\partial \dot q_k}{\partial q_k} \\
&= p_k \dfrac{\partial \dot q_k}{\partial q_k} - \dfrac{\partial \mathcal{L}}{\partial q_k}
-p_k \dfrac{\partial \dot q_k}{\partial q_k} \\
&= \cancel{p_k \dfrac{\partial \dot q_k}{\partial q_k}} - \dfrac{\partial \mathcal{L}}{\partial q_k}
-\cancel{p_k \dfrac{\partial \dot q_k}{\partial q_k}} \\
&= -\dfrac{\partial \mathcal{L}}{\partial q_k} \\
&= -\dot p_k
\end{align*}
{% end %}

Where we used $p_k = \dfrac{\partial \mathcal{L}}{\partial \dot q_k}$ to simplify the expression, allowing everything to cancel out. In the last step, we used the Euler-Lagrange equations to find that $\dfrac{\partial \mathcal{L}}{\partial q_k} = \dfrac{d}{dt} \bigg(\underbrace{\dfrac{\partial \mathcal{L}}{\partial \dot q_k}}_{p_k}\bigg) = \dfrac{dp_k}{dt} = \dot p_k$.
Let us now find $\dfrac{\partial H}{\partial p_k}$. Note that we can rewrite the Hamiltonian $H = \dot q_k \dfrac{\partial \mathcal{L}}{\partial \dot q_k} - \mathcal{L}$ into the more useful form $H = \dot q_k p_k - \mathcal{L}$. By applying the chain rule to $H(q_k, p_k, t)$ and differentiating (we need to use the product rule for the first term), we have: 

{% math() %}
\begin{align*}
\dfrac{\partial H}{\partial p_k} &= \dot q_k + p_k \dfrac{\partial \dot q_k}{\partial p_k} - \underbrace{\dfrac{\partial \mathcal{L}}{\partial \dot q_k}}_{p_k} \dfrac{\partial \dot q_k}{\partial q_k} = \dot q_k \\
&= \dot q_k + p_k \dfrac{\partial \dot q_k}{\partial p_k} - p_k \dfrac{\partial \dot q_k}{\partial q_k} = \dot q_k \\
&= \dot q_k + \cancel{p_k \dfrac{\partial \dot q_k}{\partial p_k}} - \cancel{p_k \dfrac{\partial \dot q_k}{\partial q_k}} \\ &= \dot q_k
\end{align*}
{% end %}

Thus, we have derived **Hamilton's equations of motion**:

{% math() %}
\begin{matrix*}
\dfrac{\partial H}{\partial q_k} = -\dot p_k, &\dfrac{\partial H}{\partial p_k} = \dot q_k
\end{matrix*}
{% end %}

Hamilton's equations of motion are useful because they are first-order differential equations which are often easier to solve than the second-order differential equations obtained from the Lagrangian. In addition, they possess [special numerical properties](https://en.wikipedia.org/wiki/Symplectic_geometry) that guarantee properties such as energy conservation in a numerical solution. This is why, even two centuries after Hamilton introduced his equations of motion, they are still used extensively for numerical methods for solving ODEs (and PDEs).

> **Note** Be very careful in the physical interpretation of the _generalized momentum_. The generalized momentum $p_k$ in Hamiltonian mechanics does **not** always correspond to the Newtonian momentum $p = mv$. It is instead defined through $p_k = \dfrac{\partial \mathcal{L}}{\partial \dot q_k}$ and that is the foolproof way to find the generalized momentum. Do **not** assume you can just plug in $p_k = m \dot q_k$ or some other variation of $p = mv$!

### The free particle in Hamiltonian mechanics

Let us demonstrate our use of Hamiltonian mechanics with an introductory example: the **free particle** in one dimension moving along coordinate $q$. The Lagrangian for this particle is given by:

{% math() %}
\mathcal{L} = K - \cancel{U} = \dfrac{1}{2} m \dot q^2
{% end %}

The Hamiltonian (for this one coordinate) is then given by:

{% math() %}
\begin{align*}
H &= \dot q \dfrac{\partial \mathcal{L}}{\partial \dot q} - \mathcal{L} \\ &= \dot q(m \dot q) - \dfrac{1}{2} m \dot q^2 \\ &= m \dot q^2 - \dfrac{1}{2} m \dot q^2 \\
&= \dfrac{1}{2} m \dot q^2
\end{align*}
{% end %}

But this is not _exactly_ our Hamiltonian - because the Hamiltonian is a function of position and _momentum_, **not velocity**. We must therefore find the momentum as follows:

{% math() %}
\begin{matrix*}
p = \dfrac{\partial \mathcal{L}}{\partial \dot q} = m \dot q & \Rightarrow & \dot q = p/m
\end{matrix*}
{% end %}

Which, if we substitute into the Hamiltonian, becomes:

{% math() %}
\begin{align*}
H &= \dfrac{1}{2} m \dot q^2 \\
&= \dfrac{1}{2} m \left(\dfrac{p}{m}\right)^2 \\
&=\dfrac{p^2}{2m}
\end{align*}
{% end %}

Which is equal to the kinetic energy, as we would expect. Taking the partial derivatives of the Hamiltonian yields:

{% math() %}
\begin{align*}
\dfrac{\partial H}{\partial p} &= \frac{p}{m} \\
\dfrac{\partial H}{\partial q} &=0
\end{align*}
{% end %}

And thus substituting into Hamilton's equations, the equations of motion are (as expected):

{% math() %}
\begin{matrix*}
\dfrac{dp}{dt} = 0, &\dfrac{dq}{dt} = p/m
\end{matrix*}
{% end %}

We note that if we let $q = x$ (that is, if we choose Cartesian coordinates) and thus $p = m\dfrac{dq}{dt} = mv = m \dot x$, this reduces simply to $\dot x = p/m = v, \dot p = 0$, which is simply a rewritten version of Newton's second law ($m\ddot x = 0, \dot x = v$) for a free particle.

### Conservation laws and the Poisson bracket

Just as we found with the Lagrangian, we can show that the Hamiltonian _guarantees_ conseration of particular quantities. Let us consider some quantity $A$ (perhaps this is energy) that may be dependent on any one (or all) of $q_i, p_i, t$. If we take the _total derivative_ of $A$ with respect to $t$, by the chain rule, we have:

{% math() %}
\dfrac{dA}{dt} = \dfrac{\partial A}{\partial t} + \sum_i\bigg[\underbrace{\dfrac{\partial A}{\partial \dot q_i} \dfrac{\partial H}{\partial p_i} - \dfrac{\partial A}{\partial p_i}\dfrac{\partial H}{\partial q_i}}_{\text{often written }\{H, A\}}\bigg]
{% end %}

If $\dfrac{dA}{dt} = 0$, then $A$ must be constant in time, and is thus *conserved*. This can _only_ be the case if the quantity within the square brackets (which we write as $\{H, A\}$, this is called a **Poisson bracket**) is **zero**. Indeed, this has great resemblance to the _quantum mechanical_ equation of motion (in the Heisenberg picture):

{% math() %}
\dfrac{d\hat A}{dt} = \dfrac{\partial \hat A}{\partial t} + \dfrac{i}{\hbar} [\hat H, \hat A]
{% end %}

The only replacement we need to make is that the classical quantity $A$ becomes a quantum mechanical _operator_ $\hat A$, i.e. $A \to \hat A$, and the Poisson bracket becomes the _commutator_ $[\hat H, \hat A] = \hat H \hat A - \hat A \hat H$. Thus, we often say that Hamiltonian mechanics is the starting point of quantum mechanics, as it allows us to take classical concepts and turn them into their quantum equivalents in a straightforward way.

## Introduction to gravitation

Among the biggest achievements of classical mechanics was a complete explanation of the motion of celestial bodies, including (most notably) the motion of planets around the Sun. In fact, the classical predictions of the motion of celestial bodies are so accurate that even though classical mechanics has since been superceded by the theories of Special and General Relativity, the classical theory of orbits is still used today for spacecraft orbit planning and astronomy! Thus, we will take a detailed look at how the problem of gravity was solved.

### The gravitational force and field

In the classical description of gravity, all massive objects (that is, any object with mass, it doesn't mean they are "heavy"!) are bound to each other by an attractive force, known as the **gravitational force**. The gravitational force between two bodies of masses $m_1, m_2$ is described by **Newton's law of universal gravitation**, given by:

{% math() %}
\mathbf{F}_g = -\dfrac{Gm_1 m_2}{|\mathbf{r}_2 - \mathbf{r}_1|^2} \hat r_{21} = -\dfrac{Gm_1 m_2}{|\mathbf{r}_2 - \mathbf{r}_1|^3} (\mathbf{r}_2 - \mathbf{r}_1)
{% end %}

Where $\mathbf{F}_g$ is the **gravitational force** and $G$ is the **universal gravitational constant**, which is approximately $\pu{6.674E−11 m^3*kg^{−1}*s^{−2}}$. The gravitational force, being a force, is a vector quantity, but it is also common to express Newton's law of universal gravitation in terms of the _magnitude_ of the gravitational force:

{% math() %}
\begin{matrix*}
F_g = |\mathbf{F}_g| = \dfrac{Gm_1 m_2}{r^2}, & r \equiv |\mathbf{r}_2 - \mathbf{r}_1|
\end{matrix*}
{% end %}

> **Note:** You may also see this in yet _another_ form, where instead of $m_1, m_2$ the two masses are instead denoted by $M$ and $m$, such that the magnitude of the gravitational force becomes $F_g = \dfrac{GMm}{r^2}$.

The gravitational force is significant for several important reasons. The first is that it is a **long-distance force**, one of only two in nature (the other being the electromagnetic force). The second is that it is a **conservative force**, meaning that it satisfies the conservation of energy. And the third is that gravitational effects do not propagate instantly, but instead, at the speed of light; that means, for instance, if the Sun were to suddenly vanish, the Earth would actually orbit as if everything was normal for another few minutes, until the last light from the Sun reached us! (of course, afterwards, everything would be chaos). These features can be explained by associating the gravitational force with a **gravitational field**. We have already discussed fields a bit previously, but remember that a field is characterized by the following property:

> **Definition of physical fields:** A field is a physical quantity that fills space and mediates (carries) interactions between different particles in space.

In the case of gravity, the gravitational field can be mathematically-described by a vector-valued function $\mathbf{g}(\mathbf{r}) = \mathbf{g}(x, y, z)$. The gravitational field fills all space, which is why it has infinite range (and therefore gravity is a long-distance forces). It carries interactions between masses, meaning that the gravitational force between two objects is transmitted by the gravitational field - however, this interaction is not instant, but rather carried at the speed of light $c$. Thus, the gravitational force may be written as $\mathbf{F}_g = m \ddot{\mathbf{r}} = m\mathbf{g}$, where $m$ is a particle with mass within a gravitational field, and $\ddot{\mathbf{r}}$ is the acceleration of the particle. In addition, the gravitational field is _generated_ by the presence of masses, and changes as the distribution of masses changes. Thus, it is natural to describe the gravitational field in terms of a differential equation. Indeed, there is one: it is known as **Gauss's law for gravity**:

{% math() %}
\begin{align*}
\nabla \cdot \mathbf{g} &= -4\pi G \rho & \text{(differential form)} \\
\oint \mathbf{g} \cdot d\mathbf{A} &= -4\pi G M_\text{total} & \text{(integral form)}
\end{align*}
{% end %}

Where $\rho = \rho(x, y, z)$ is the mass density throughout space. The fundamental solution to Gauss's law for gravity, describing the gravitational field in vacuum of a single spherically-symmetric object (or point particle) with mass $M$ located far away from all other masses, is the following expression for the gravitational field:

{% math() %}
\mathbf{g} = -\dfrac{GM}{r^2} \hat r
{% end %}

Where here, {% inlmath() %}\mathbf{r} = |\mathbf{r} - \mathbf{r}_\text{mass}|{% end %} where $\mathbf{r}_\text{mass}$ is the position of the mass, which we also call the **central mass**. If this describes the gravitational field generated by a single object far away from all other masses, you may ask, how is this a useful solution? The answer is that if we have a central mass ($M$) that is far greater than some other mass $m$, that is, $m \ll M$, then the smaller mass has almost no gravitational effect on the larger mass. Thus, the larger mass can effectively considered to be stationary and the solution is a good approximation to the gravitational field of the whole system of two masses. From there, we may calculate the _orbit_ $\mathbf{r}(t)$ of the smaller mass around the larger mass (in fact, we will find the exact solution to this problem soon!).

> **Note:** For spherically-symmetric problems we usually express orbits using in polar coordinates, so the orbit would be described by $r(\theta)$. This can be converted back to $\mathbf{r}(t)$ with $\mathbf{r}(t) = \langle r(t) \cos \theta, r(t) \sin \theta\rangle$.

Let us formalize this idea mathematically. The _true_ gravitational field of this system of two masses (called a _two-body_ system) would actually be given by:

{% math() %}
\begin{align*}
\mathbf{g} &= -\dfrac{GM}{r^2} \hat r_{12} + \left(-\dfrac{Gm}{r^2}\right) \hat r_{12} \\
&= -\dfrac{G(M + m)}{r^2} \hat r_{12}
\end{align*}
{% end %}

Where {% inlmath() %}\mathbf{r}_M{% end %} is the larger mass's position, {% inlmath() %}\mathbf{r}_m{% end %} is the smaller mass's position, {% inlmath() %}r = |\mathbf{r}_M - \mathbf{r}_m|{% end %} is the separation between the two masses, and {% inlmath() %}\hat r_{12} = \dfrac{\mathbf{r}_M - \mathbf{r}_m}{|\mathbf{r}_M - \mathbf{r}_m|}{% end %} is the unit vector pointing between the masses. Thus, the equations of motion are given by:

{% math() %}
\begin{align*}
\ddot{\mathbf{r}}_M = M \mathbf{g} = -\dfrac{GM(M + m)}{r^2} \hat r_{12} \\
\ddot{\mathbf{r}}_m = m \mathbf{g} = -\dfrac{Gm(M + m)}{r^2} \hat r_{12} \\
\end{align*}
{% end %}

Thus, the differential equations of motion indicate that the big mass $M$ and smaller mass $m$ actually orbit around their collective _center of mass_. However, in the case that the big mass is _much greater_ than the smaller mass (for example, the Sun has a mass over 300,000 times that of Earth's) then the gravitational effect of the smaller mass may be considered negligible, and the gravitational field reduces to:

{% math() %}
\begin{align*}
\mathbf{g} &= -\dfrac{GM}{r^2} \hat r_{12} + \underbrace{\left(-\dfrac{Gm}{r^2}\right) \hat r_{12}}_\text{very small contribution} \\
&\approx -\dfrac{GM}{r^2} \hat r_{12} \qquad (\text{when } m \ll M)
\end{align*}
{% end %}

In this limit, the larger mass may be considered effectively stationary, that is, $\mathbf{r}_M = \mathbf{r}_0 = \text{const.}$, and the differential equations of motion of the smaller mass becomes:

{% math() %}
\ddot{\mathbf{r}}_m = m\mathbf{g} = -\dfrac{GMm}{r^2} \hat r_{12}
{% end %}

This can be simplified further if we define the _reduced mass_ (effective mass) of the two-body system to be $\mu = \dfrac{Mm}{m_t} = \dfrac{Mm}{m + M}$, where $m_t \equiv m + M$ is the **total mass** of the system. Thus the equations of motion of the smaller mass reduce to simply:

{% math() %}
\ddot{\mathbf{r}}_m = -\dfrac{G\mu m_t}{r^2} \hat r_{12}
{% end %}

This is the essential differential equation that we will soon derive from Lagrangian mechanics, and solve to find the classical solution to a two-body gravitational system.

> **Note for the advanced reader:** Uniquely, we observe that gravity is actually the _predominant_ force acting on celestial bodies. This is a by-product of an interesting quirk of nature: while the electromagnetic force acts on _charges_, most large objects (asteroids, planets, stars, etc.) in the Universe are neutrally-charged, so they have little to zero effective charge; meanwhile the gravitational force acts on _masses_, and large masses have a _lot_ of mass, so gravity wins out over the electromagnetic force over astronomical distances and in the case of large (typically celestial!) bodies. But the force of gravity between everyday objects (such as a coffee cup or a car) is very weak!

### The gravitational potential

Aside from all the characteristics of gravity we mentioned earlier, we should also mention one more _very important_ characteristic: the gravitational field is a **conservative field**, meaning that objects in gravitational fields conserve energy. Mathematically speaking, the gravitational field obeys:

{% math() %}
\oint_C \mathbf{g}\cdot d\mathbf{r} = 0 \Leftrightarrow \nabla \times \mathbf{g} = 0
{% end %}

Thus, by the **gradient theorem** of vector calculus, we may write the gravitational field in terms of a scalar-valued _potential_ $\varphi$, where $\mathbf{g} = -\nabla \varphi$. This potential is mathematically easier to work with, since it is a scalar, and also, it obeys the differential equation $\nabla^2 \varphi = 4\pi G\rho$, a well-studied differential equation in mathematical physics (especially in the special case of $\rho = 0$, where it reduces to Laplace's equation $\nabla^2 \varphi = 0$, which you may have seen before if you have studied electromagnetic theory). 

This potential $\varphi(\mathbf{r})$ is more commonly called the **gravitational potential**, and it is more than just a mathematical trick to make the equations easier. The _physical interpretation_ of the gravitational potential is that a mass $m$ placed in a gravitational field would have a **gravitational potential energy** given by $U_g = m\varphi$. Since all particles naturally want to attain a minimum potential energy reach a stable equilibrium, we can equivalently say that they "descend" down the potential $\varphi(\mathbf{r})$ until they reach a "valley" (local minimum) of the potential, where they can maintain stable orbits. This provides another, more elegant way to write out the _exact_ equations of motion for the trajectory $\mathbf{r}(t)$ of a mass in a gravitational field, one that is generally preferred in physics today:

{% math() %}
\ddot{\mathbf{r}} = -m \nabla \varphi
{% end %}

## Gravitation in Lagrangian mechanics

Of all the problems that can be analyzed with Lagrangian mechanics, one of the most significant is the problem of two masses (which we denote as $M$ and $m$, where $M \gg m$) bound to each other gravitationally. The gravitational potential energy of the system (relative to a point infinitely-far away) is given by:

{% math() %}
U(r) = -\dfrac{GMm}{r}
{% end %}

The problem of gravitation is the classical example of a **radial potential problem**. It is helpful, therefore, to examine the nature of a _general radial potential problem_, for which we know that the potential $U$ is purely a function of the radial distance $r$, but the potential $U(r)$ can be arbitrary. We wish to find the equations of motion for mass $m$ that orbits around the larger mass $M$. It is useful to effectively consider the two masses to form a single **effective mass**, which we call the _reduced mass_, and denote by $\mu$, as shown below:

{% math() %}
\mu = \dfrac{mM}{m + M}
{% end %}

While the radial potential problem was already solved, even before the development of Lagrangian mechanics, solving it with Lagrangian mechanics provides unique insights that are difficult to see when solving using the Newtonian approach. This allows us to write the Lagrangian in polar coordinates for the radial potential:

{% math() %}
\mathcal{L} = \dfrac{1}{2} \mu (\dot r^2 + r^2 \dot \theta^2) - U(r)
{% end %}

Where once again, $\mu$ is the reduced mass. We have two Euler-Lagrange equations for our two generalized coordinates, one for $r$ and one for $\theta$. The Euler-Lagrange equation in $r$ yields:

{% math() %}
\mu \ddot r - \mu r \dot \theta^2 + \dfrac{dU}{dr} = 0
{% end %}

Meanwhile, the Euler-Lagrange equation in $\theta$ yields:

{% math() %}
\begin{align*}
\dfrac{d}{dt}(\underbrace{\mu r^2 \dot \theta}_\text{const.}) &= 0 \\
\text{const.} &= \ell \\
\Rightarrow \dot \theta &= \dfrac{\ell}{\mu r^2}
\end{align*}
{% end %}

We find that there is a _conserved quantity_ (which we call $\ell$) that is intrinsic to the radial system (it is conserved, since it is **constant**). This quantity, $\ell$, has units, which we may determine by dimensional analysis, to be $\pu{kg \cdot m^2 \cdot s^{-1}}$ - _exactly_ those of the classical **angular momentum**. Thus, if we now use our expression we obtained for $\dot \theta$ into our Euler-Lagrange equation for $r$, then we have:

{% math() %}
\mu \ddot r - \mu r \left(\dfrac{\ell}{\mu r^2}\right)^2 + \dfrac{dU}{dr} = 0
{% end %}

By slight rearrangement and expansion, we have:

{% math() %}
\mu \dfrac{d^2 r}{dt^2} - \dfrac{\ell^2}{\mu r^3} = -\dfrac{dU}{dr}
{% end %}

If we define $F(r) \equiv -\dfrac{dU}{dr}$ as the ***central force*** defined by the radial potential, then we can write this in a simpler form as:

{% math() %}
\mu \dfrac{d^2 r}{dt^2} - \dfrac{\ell^2}{\mu r^3} = F(r)
{% end %}

Now, this equation of motion, while still _useful_, has a problem: it is defined with derivatives with respect to $t$. Thus, we can use it to find the radial distance of the orbiting body over time, but it is no good for finding the actual _shape_ of the orbit, for which we need to find $r(\theta)$, the radial distance of the orbiting body as a function of $\theta$. 

So, we must find some way to convert this differential equation to one expressed in terms of derivatives with respect to $\theta$ instead of derivatives with respect to $t$. The first step in doing so is utilizing our equation $\dot \theta = \dfrac{\ell}{\mu r^2}$. We may write this equivalently, using the chain rule, as:

{% math() %}
\begin{align*}
\dfrac{d}{dt} &= \dfrac{d\theta}{dt} \dfrac{d}{d\theta}\\
&= \dot \theta \dfrac{d}{d\theta} \\
&= \dfrac{\ell}{\mu r^2} \dfrac{d}{d\theta}
\end{align*}
{% end %}

Therefore:

{% math() %}
\begin{align*}
\dfrac{d}{dt} &= \dfrac{\ell}{\mu r^2} \dfrac{d}{d\theta} \\
\dfrac{d^2}{dt^2} &= \dfrac{d}{dt} \left(\dfrac{d}{dt}\right) = \dfrac{\ell}{\mu r^2} \dfrac{d}{d\theta}\left(\dfrac{\ell}{\mu r^2} \dfrac{d}{d\theta}\right)
\end{align*}
{% end %}

Thus, we have:

{% math() %}
\dfrac{d^2 r}{dt^2} = \dfrac{d^2}{dt^2} r(t) = \dfrac{\ell}{\mu r^2} \dfrac{d}{d\theta}\left(\dfrac{\ell}{\mu r^2} \dfrac{dr}{d\theta}\right)
{% end %}

And substituting our found expression for $\ddot r$ back into the central-force equation of motion we derived before, we have:

{% math() %}
\begin{gather*}
\mu \dfrac{d^2 r}{dt^2} - \dfrac{\ell^2}{\mu r^3} = F(r) \\
\Rightarrow \mu \left[\dfrac{\ell}{\mu r^2} \dfrac{d}{d\theta}\left(\dfrac{\ell}{\mu r^2} \dfrac{dr}{d\theta}\right)\right] - \dfrac{\ell^2}{\mu r^3} = F(r) \\
\Rightarrow \left[\dfrac{\ell}{r^2} \dfrac{d}{d\theta}\left(\dfrac{\ell}{\mu r^2} \dfrac{dr}{d\theta}\right)\right] - \dfrac{\ell^2}{\mu r^3} = F(r) \\
\Rightarrow \left[\dfrac{\ell^2}{\mu r^2} \dfrac{d}{d\theta}\left(\dfrac{1}{r^2} \dfrac{dr}{d\theta}\right)\right] - \dfrac{\ell^2}{\mu r^3} = F(r) \\
\end{gather*}
{% end %}

We can choose to write this in expanded form, if we so wish. The first term requires the product rule to expand:

{% math() %}
\dfrac{d}{d\theta} \left(\dfrac{1}{r^2}\dfrac{dr}{d\theta}\right) = \dfrac{1}{r^2}\dfrac{d^2 r}{d\theta^2} - \dfrac{2}{r^3} \left(\dfrac{dr}{d\theta}\right)^2
{% end %}

From which we have:

{% math() %}
\dfrac{\ell^2}{\mu r^2}\left[\dfrac{1}{r^2}\dfrac{d^2 r}{d\theta^2} - \dfrac{2}{r^3} \left(\dfrac{dr}{d\theta}\right)^2\right] - \dfrac{\ell^2}{\mu r^3} = F(r)
{% end %}

But it is often much more helpful to _not_ expand the derivatives, and instead multiply all sides through by $\dfrac{\mu r^2}{\ell^2}$, which gives us:

{% math() %}
\begin{gather*}
\left[\dfrac{\ell^2}{\mu r^2} \dfrac{d}{d\theta}\left(\dfrac{1}{r^2} \dfrac{dr}{d\theta}\right)\right] - \dfrac{\ell^2}{\mu r^3} = F(r) \\
\dfrac{d}{d\theta}\left(\dfrac{1}{r^2} \dfrac{dr}{d\theta}\right)- \dfrac{1}{r} = \dfrac{\mu r^2}{\ell^2}F(r) = -\dfrac{\mu r^2}{\ell^2}\dfrac{dU}{dr}
\end{gather*}
{% end %}

We have simplified the problem as much as we can without specifying what exactly $U(r)$ is. But to solve the problem for gravitation, or in general for _any_ central force, we must explicitly specify $U(r)$, or alternatively the central force $F(r) = -\dfrac{dU}{dr}$. A few examples of such potentials are listed in the table below:

| Potential               | Mathematical form of $U(r)$                                   | Physical scenario                                                                                                                                                                                                                            |
| ----------------------- | -------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Gravitational           | $-\dfrac{GMm}{r}$                                 | Two bodies $M, m$ orbiting under gravitational attraction                                                                                                                                                                                    |
| Coulomb (electrostatic) | $\dfrac{1}{4\pi \varepsilon_0} \dfrac{Qq}{r}$     | Two charges $Q, q$ interacting through the electrostatic force                                                                                                                                                                               |
| Harmonic                | $\dfrac{1}{2} kr^2$ or equivalently $\dfrac{1}{2} m \omega^2 r^2$ | Two masses attached by a spring, where the smaller mass $m$ exhibits sinusoidal motion around the larger mass. This is also a good model for diatomic (two-atom) molecules that vibrate in a form that can be described by the spring force. |

> **Note:** The gravitational potential, as well as the Coulomb potential for $Q, q$ having opposite signs, are both **negative**. This means that these systems are **stable** as the system has a lower potential energy than a reference point infinitely-far away; the system must be perturbed (for instance, by applying an external acceleration to $m$) to be able to increase its potential energy enough to "break apart" the system to send the two masses (or charges in the latter case) to fly apart from each other.

Using the definition of the gravitational potential $U(r) = -\dfrac{GMm}{r}$, we find that:

{% math() %}
F_\text{gravity} = -\dfrac{dU}{dr} = -\dfrac{GMm}{r^2}
{% end %}

So our _specific_ equation of motion, assuming $\mu \approx m$ (since we imposed the restriction at the start that $M \gg m$) becomes:

{% math() %}
\begin{align*}
\dfrac{d}{d\theta}\left(\dfrac{1}{r^2} \dfrac{dr}{d\theta}\right)- \dfrac{1}{r} &= \dfrac{\mu r^2}{\ell^2}F(r) \\
&\approx \dfrac{mr^2}{\ell^2} \left(-\dfrac{GMm}{r^2}\right) \\
&= \underbrace{\dfrac{GMm^2}{\ell^2}}_\text{const.}
\end{align*}
{% end %}

We notice that in this problem, the right-hand side evaluates to a _constant_ given by $b \equiv \dfrac{GMm^2}{\ell^2}$. Thus, we have:

{% math() %}
\dfrac{d}{d\theta}\left(\dfrac{1}{r^2} \dfrac{dr}{d\theta}\right)- \dfrac{1}{r} = b
{% end %}

The trick typically used to actually _solve_ this differential equation is to use the coordinate transform $u = 1/r$. Then this highly-nonlinear differential equation can be reduced to a much simpler differential equation, which possesses an analytical solution. 

For this, however, we need to transform $\dfrac{dr}{d\theta}$, which is in terms of $r(\theta)$, into its equivalent form written in terms of $u(\theta)$. By the chain rule, we know that $\dfrac{dr}{d\theta} = \dfrac{dr}{du} \dfrac{du}{d\theta}$. Using $r = 1/u$, which follows from $u = 1/r$, we can differentiate to find that $\dfrac{dr}{du} = -\dfrac{1}{u^2} = -r^2$. Thus, we have:

{% math() %}
\dfrac{dr}{d\theta} = -\dfrac{1}{u^2} \dfrac{du}{d\theta} = -r^2 \dfrac{du}{d\theta}
{% end %}

Which, after substitution into our differential equation, becomes:

{% math() %}
\begin{gather*}
\dfrac{d}{d\theta}\left(\dfrac{1}{r^2} \dfrac{dr}{d\theta}\right)- \dfrac{1}{r} = b \\
\Rightarrow \dfrac{d}{d\theta}\left(\dfrac{1}{r^2}\left(-r^2 \dfrac{du}{d\theta}\right)\right)- u = b \\
\Rightarrow -\dfrac{d^2 u}{d\theta^2} - u = b \\
\Rightarrow \dfrac{d^2 u}{d\theta^2}+ u = -b
\end{gather*}
{% end %}

We can now solve using the conventional techniques of ODEs. Since this is an _inhomogenous_ 2nd-order ODE, its solution is a sum of the general solution to the homogeneous differential equation $u'' + u = 0$ and the particular solution to $u'' + u = -b$. But $u'' + u = 0$, we know, is the equation of a simple harmonic oscillator, which has the solution:

{% math() %}
\begin{align*}
u_\text{homogenous} &= A \cos \theta + B \sin \theta \\
&= C \cos (\theta - \theta_0)
\end{align*}
{% end %}

Where $C \equiv \sqrt{A^2 + B^2}, \theta_0 \equiv \tan^{-1}\dfrac{B}{A}$, which comes from applying trigonometric identities - refer to [the following trigonometric proof](https://www.mathcentre.ac.uk/resources/uploaded/mc-ty-rcostheta-alpha-2009-1.pdf) for more details. Meanwhile, a particular solution to $u'' + u = -b$ is simply $u = -b = \text{const}$ (really, this is a solution! You can check for yourself). Thus the _general_ solution to $u'' + u = -b$ is given by:

{% math() %}
\begin{align*}
u(\theta) &= - b + C \cos (\theta - \theta_0) \\
&= - b[1 + e \cos (\theta - \theta_0)], \quad e \equiv C/b
\end{align*}
{% end %}

Where $e$ is a constant known as the **eccentricity**, a constant that can be determined observationally, or calculated theoretically from energy of the orbit with $e = \sqrt{1 + \dfrac{2E\ell^2}{G^2 M^2 m^3}}$ (we will not prove this). Since $r = 1/u$, we have the solution:

{% math() %}
\begin{align*}
r(\theta) &= -\dfrac{b}{1 + e \cos (\theta - \theta_0)} \\
&=-\dfrac{GMm^2}{\ell^2}\dfrac{1}{1 + e \cos (\theta - \theta_0)}
\end{align*}
{% end %}

This solution (typically referred to as an _orbit_) takes the form of a **conic section** (which may be a hyperbola, parabola, circle, or ellipse, depending on the eccentricity) and conserves energy and angular momentum, characteristics that govern the motion of all celestial bodies.

### Effective potential and centripetal force

Returning to the central force problem we have been examining in our study of gravitation, we recalled that the central-force problem with associated radial potential $U(r)$ could be written in the following form:

{% math() %}
\dfrac{\ell^2}{\mu r^2} \left[\dfrac{d^2}{d\theta^2}\left(\dfrac{1}{r}\right) + \dfrac{1}{r}\right] = \dfrac{dU}{dr}
{% end %}

Notice that if we expand, we may rearrange this equation as follows:

{% math() %}
\begin{gather*}
\dfrac{\ell^2}{\mu r^2} \dfrac{d^2}{d\theta^2} \left(\dfrac{1}{r}\right) + \dfrac{\ell^2}{\mu r^3} = \dfrac{dU}{dr} \\
\dfrac{\ell^2}{\mu r^2} \dfrac{d^2}{d\theta^2} \left(\dfrac{1}{r}\right) - \underbrace{\dfrac{d}{dr}\left(\dfrac{\ell^2}{2\mu r^2}\right)}_{\text{same as}\ \ell^2/\mu r^3} = \dfrac{dU}{dr} \\
\dfrac{\ell^2}{\mu r^2} \dfrac{d^2}{d\theta^2} \left(\dfrac{1}{r}\right) = \dfrac{dU}{dr} + \dfrac{d}{dr}\left(\dfrac{\ell^2}{2\mu r^2}\right) \\
\dfrac{\ell^2}{\mu r^2} \dfrac{d^2}{d\theta^2} \left(\dfrac{1}{r}\right) = \dfrac{d}{dr}\left(U + \dfrac{\ell^2}{2\mu r^2}\right) 
\end{gather*}
{% end %}

Where in the above, $\dfrac{\ell^2}{\mu r^3} = -\dfrac{d}{dr}\left(\dfrac{\ell^2}{2\mu r^2}\right)$. This rewriting may appear to be unmotivated, but there is a reason for this. If we define an **effective potential** given by:

{% math() %}
U_\text{eff.}(r) = U(r) + \dfrac{\ell^2}{2\mu r^2}
{% end %}

Then the above equation can be rewritten as:

{% math() %}
\dfrac{\ell^2}{\mu r^2} \dfrac{d^2}{d\theta^2} \left(\dfrac{1}{r}\right) = \dfrac{dU_\text{eff.}}{dr}
{% end %}

Expanding the second derivative on the left yields:

{% math() %}
\begin{gather*}
\dfrac{\ell^2}{\mu r^2} \left[\dfrac{2}{r^3} \left(\dfrac{dr}{d\theta}\right)^2 - \dfrac{1}{r^2} \dfrac{d^2 r}{d\theta^2}\right] = \dfrac{dU_\text{eff.}}{dr} \\
\underbrace{\dfrac{\ell^2}{\mu r^2} \left[\dfrac{1}{r^2} \dfrac{d^2 r}{d\theta^2}-\dfrac{2}{r^3} \left(\dfrac{dr}{d\theta}\right)^2\right]}_{F_\text{eff.}} = -\dfrac{dU_\text{eff.}}{dr}
\end{gather*}
{% end %}

The left-hand side has units of force, so we can call it (times a negative sign) the _effective force_, $F_\text{eff.}$ where the above equation becomes:

{% math() %}
F_\text{eff.} = -\dfrac{dU_\text{eff.}}{dr}
{% end %}

Or even more simply:

{% math() %}
\mu \ddot r = -\dfrac{dU_\text{eff.}}{dr}
{% end %}

Which reproduces the form of Newton's second law $F = m \ddot r = -\dfrac{dU}{dr}$ (just with effective potential and reduced mass)! And this is not all. Let us take another look at the effective potential:

{% math() %}
U_\text{eff.}(r) = U(r) + \dfrac{\ell^2}{2\mu r^2}
{% end %}

Let's focus on the second term. For reasons that will soon become apparent, let us take its derivative and multiply by a negative sign, and call this quantity $F_c$:

{% math() %}
F_c = \dfrac{d}{dr}\left(\dfrac{\ell^2}{2\mu r^2}\right) = \dfrac{\ell^2}{\mu r^3}
{% end %}

But recall that we previously derived that $\dot \theta = \dfrac{\ell}{\mu r^2}$. Thus, we can rewrite $F_c$ in terms of $\dot \theta$ with:

{% math() %}
F_c = \dfrac{\ell^2}{\mu r^3} = \mu r \dot \theta^2
{% end %}

Writing this in a slightly-different form by defining $\omega = \dot \theta$ where $\omega$ is the angular velocity, we have:

{% math() %}
F_c = \mu r \omega^2
{% end %}

If we take $\mu \approx m$, where $m$ is the mass of the orbiting, and use the relationship $v = r \omega \Leftrightarrow \omega = \dfrac{v}{r}$, then we can rewrite this as:

{% math() %}
F_c = m \dfrac{v^2}{r}
{% end %}

Which is just the Newtonian centripetal force! Additionally, if we expand our effective potential as a Taylor series around some point $r_0$ for $U_\text{eff.}(r)$ up to second order, we have:

{% math() %}
U_\text{eff.}(r) \approx U_\text{eff.}(r_0) + U_\text{eff.}'(r_0)(r - r_0) + \dfrac{1}{2} U_\text{eff.}''(r_0)(r - r_0)^2
{% end %}

Recall that the stationary points (minima/maxima/saddle points) of a potential are **equilibrium points of a system** (review the section in [part 1 of the guide](@/advanced-classical-mech/index.md#potential-energy-and-conservation-of-energy) about potential landscapes if this is unfamiliar). In the case of central force problems, that means that particles at some stationary point $r_0$ will _orbit_ at a fixed radius $r = r_0$. Depending on the specific form of the central force, these orbits may be stable or unstable (there is [a theorem](https://en.wikipedia.org/wiki/Bertrand%27s_theorem) that states that only central forces with associated potentials in the form $U(r) \sim r^2$ or $U(r) \sim r^{-1}$ are stable). But if $r_0$ also happens to be a _local minimum_, then it is a **stable equilibrium** and thus a **stable orbit**. If an orbiting particle strays slightly from that stable equilibrium, then it will "wiggle" around the stable orbit $r = r_0$, just like a simple harmonic oscillator.

In fact, we can prove this. If we expand $U_\text{eff.}(r)$ about a point $r_0$, which is _also_ a local minimum, then (since we're at a local minimum) $U_\text{eff.}'(r_0) \approx 0$. Thus our expansion for the effective potential becomes:

{% math() %}
\begin{align*}
U_\text{eff.}(r) &\approx U_\text{eff.}(r_0) + U_\text{eff.}'(r_0)(r - r_0) \\
&= U_\text{eff.}(r_0) + \cancel{U_\text{eff.}'(r_0)(r - r_0)} + \dfrac{1}{2} U_\text{eff.}''(r_0)(r - r_0)^2 \\
&= U_\text{eff.}(r_0) + \dfrac{1}{2} U_\text{eff.}''(r_0)(r - r_0)^2 \\
&\approx U_\text{eff.}(r_0) + \dfrac{1}{2} U_\text{eff.}''r^2
\end{align*}
{% end %}

Where our last simplification comes from the fact that since our orbiting particle strays only a short distance from the stable equilibrium $r = r_0$, then $(r - r_0)^2 \approx r^2$ (you can show this with the binomial expansion if you're not satisfied with this argument). If we substitute our expansion into our equation of motion $\mu \ddot r = -\dfrac{dU_\text{eff.}}{dr}$, we have:

{% math() %}
\begin{align*}
\mu \ddot r &= -\dfrac{d}{dr} \left[U_\text{eff.}(r_0) + \dfrac{1}{2} U_\text{eff.}''r^2\right] \\
&= -U_\text{eff.}''(r_0)r \\
\Rightarrow \ddot r &= -U_\text{eff.}''(r_0)r \\
\Rightarrow \ddot r &= -\underbrace{\dfrac{U_\text{eff.}''(r_0)}{\mu}}_\text{const.} r
\end{align*}
{% end %}

This looks like the differential equation of a simple harmonic oscillator, $\ddot r = -\omega^2 r$! And indeed, it is! In fact, by comparing terms, we find that $\omega^2$ corresponds to $U_\text{eff.}''(r_0)/\mu$, and thus the _frequency_ of oscillations is given by:

{% math() %}
f = \dfrac{\omega}{2\pi} = \dfrac{1}{2\pi} \sqrt{\dfrac{U_\text{eff.}''(r_0)}{\mu}}
{% end %}

From our Lagrangian examination of the central-force problem, we have therefore seen that we can write an _effective potential_ that can be used to reproduce Newton's second law. From here, the familiar forces of Newtonian mechanics naturally appear.

## Next steps

We've reached the end of the second part of the guide to classical mechanics. Now is the time to continue to [part 3](@/advanced-classical-mech/part-3.md)!