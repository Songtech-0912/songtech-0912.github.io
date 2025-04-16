+++
title = "Advanced Classical Mechanics"
date = 2025-01-26
draft = false
+++

This is a guide to classical mechanics beyond Newtonian mechanics. Topics discussed include Lagrangian mechanics, Hamiltonian mechanics, Special Relativity, in-depth analysis of oscillations, and mechanical waves.

<!-- more -->

I thank [Professor Martin](https://faculty.rpi.edu/charles-martin) at Rensselaer Polytechnic Institute for his excellent instruction and giving the permission to make this guide freely available.

## The general ideas of classical mechanics

From the scientific revolution until 1905, physics was dominated by **classical mechanics** - a collective theory that describes how systems behave and evolve with fixed mathematical rules. The starting paradigm used by classical mechanics was **Newtonian mechanics**, which used concepts of forces, in combination with Newton's three laws of motion, to describe the physics of a system. This was later superceded in favor of **Lagrangian and Hamiltonian mechanics**, which instead focused on concepts of _energy_ and the laws governing energy to determine the motion of objects.

While we will briefly review the prerequisites, we assume a familiarity with introductory physics, multivariable calculus, and differential equations. See the [classical dynamics](@/classical-dynamics.md), [differential equations](@/differential-equations/index.md), and [multivariable calculus](@/multivariable-calculus/index.md) guides that explain these topics in detail.

### Newtonian mechanics

In Newtonian mechanics, the earliest form of classical mechanics, **Newton's three laws of motion** govern the behavior of objects:

1. Objects in motion stay in motion, and objects at rest stay at rest, unless acted upon by an external force (also called the _law of inertia_)
2. A change in an object's quantity of motion (what we would today call _momentum_) occurs when the object _is acted upon_ by an external force
3. Forces always act between _pairs_ of objects; for every force between two objects, there is _always_ another force equal in magnitude and opposite in direction

All three of Newton's laws may be written as a single differential equation between the momentum $\mathbf{p}$ of an object and the forces $\mathbf{F}_i$ *acting on* the object:

{% math() %}
\dfrac{d\mathbf{p}}{dt} = \sum \mathbf{F}_i(x, \dot x, t)
{% end %}

Which we may also write as:

{% math() %}
m\dfrac{d\mathbf{v}}{dt} = m\dfrac{d^2\mathbf{r}}{dt^2} = \sum \mathbf{F}_i(x, \dot x, t)
{% end %}

> **Note:** we generally call this Newton's _second law_ but this is somewhat misleading since it contains all the information of the other two laws. Instead, we'll call it _Newton's differential equation_ here.

Newton's laws are applied with the conjunction with _conservation laws_. In classical mechanics, momentum, angular momentum, and total (mechanical) energy are all _conserved quantities_, meaning that they _do not change_. Not all forces conserve energy in Newtonian mechanics; forces that _do_ conserve energy are known as _conservative_ forces, and require the condition that any closed line integral of the force is zero:

{% math() %}
\oint \mathbf{F} \cdot d\mathbf{r} = 0
{% end %}

Therefore, we also say that these forces are _path-independent_, which will have important implications we will discuss later.

### Applying Newton's laws

The general method of applying Newton's laws is a three-step process. First, all the forces are identified; second, each of the forces is written in vector form; and third, the forces are substituted into Newton's differential equation, which is then solved.

This procedure, unfortunately, is not as simple as it may seem, since the force can depend on position, velocity, _and_ time. In the general case, Newton's differential equation must be solved _from scratch_ for each given physical system. However, there exist special cases where general solutions can be found, and they are listed below:

| Special case                                                         | Physical meaning                   | Example                                                                |
| -------------------------------------------------------------------- | ---------------------------------- | ---------------------------------------------------------------------- |
| $\mathbf{F} = \mathbf{F}_0 = \text{const.}$                          | Constant force                     | Free fall acceleration, static/dynamic friction                        |
| $\mathbf{F} = \mathbf{F}(\mathbf{r})$                                | Force dependent on _only_ position | Gravitational force, harmonic oscillator (spring force), Coulomb force |
| $\mathbf{F} = \mathbf{F}(\mathbf{v}) = \mathbf{F}(\dot{\mathbf{r}})$ | Force dependent on *only* velocity | Magnetic force, air/water resistance (drag force)                      |
| $\mathbf{F} = \mathbf{F}(t)$                                         | Force dependent on *only* time     | Time-increasing/decreasing driving force                               |

In each of these cases, we can derive exact solutions to Newton's differential equation. In the simplest case of a constant force, Newton's differential equation becomes:

{% math() %}
m\dfrac{d^2 \mathbf{r}}{dt^2} = m \dfrac{d\mathbf{v}}{dt} = \mathbf{F}_0
{% end %}

To find $\mathbf{r}(t)$ we integrate both sides twice with respect to time, yielding the solution:

{% math() %}
\mathbf{r}(t) = \mathbf{r}_0 + \mathbf{v}_0 t + \dfrac{1}{2} \dfrac{\mathbf{F}_0}{m} t^2
{% end %}

Let us now consider a force that depends *only on time*, that is, $\mathbf{F} = \mathbf{F}(t)$. Then, we have:

{% math() %}
m\dfrac{d^2 \mathbf{r}}{dt^2} = m \dfrac{d\mathbf{v}}{dt} = \mathbf{F}(t)
{% end %}

We may use the same method of twice-integrating to have the _solution for a generic time-dependent force_:

{% math() %}
\mathbf{r}(t) = C_2 + C_1 t + \dfrac{1}{m}\int\left[\int\mathbf{F} (t) d t\right]dt
{% end %}

The integrals can be evaluated for the given force to arrive at a specific solution for a given force.

Similarly, let us consider a force that depends *only on velocity*, that is, $\mathbf{F} = \mathbf{F}(\mathbf{v})$. Newton's differential equation then becomes:

{% math() %}
m\dfrac{d\mathbf{v}}{dt} = \mathbf{F}(\mathbf{v})
{% end %}

We can perform _separation of variables_ so that we have:

{% math() %}
m \dfrac{d\mathbf{v}}{\mathbf{F}(\mathbf{v})} = d t
{% end %}

Then, integrating both sides, we have:

{% math() %}
\begin{align*}
m\int \dfrac{d\mathbf{v}}{\mathbf{F}(\mathbf{v})} = \int d t \\
t(\mathbf{v}) = m\int \dfrac{d\mathbf{v}}{\mathbf{F}(\mathbf{v})}
\end{align*}
{% end %}

After explicitly evaluating the integral on the right-hand side, the function $t(\mathbf{v})$ can be rearranged to $\mathbf{v}(t)$, which can then be integrated to find the position.

As an alternative approach, we may note that we may write Newton's differential equation in a slightly different form using the chain rule:

{% math() %}
\begin{align*}
m\dfrac{d\mathbf{v}}{dt} &= \mathbf{F}(\mathbf{v}) \\
m\dfrac{d\mathbf{v}}{dt} &= m \dfrac{d\mathbf{v}}{d\mathbf{r}}\cdot \dfrac{d\mathbf{r}}{dt}  = m \dfrac{d\mathbf{v}}{d\mathbf{r}} \cdot \mathbf{v}
\end{align*}
{% end %}

Where we note that $\mathbf{v} = \dfrac{d\mathbf{r}}{dt}$, which is what allows this simplification in the first place. Now, we again have a separable differential equation:

{% math() %}
m \dfrac{d\mathbf{v}}{d\mathbf{r}} \cdot \mathbf{v} = \mathbf{F}(\mathbf{v})
{% end %}

Whose solution is:

{% math() %}
\mathbf{r}(\mathbf{v}) = m \int \dfrac{\mathbf{v} \cdot d\mathbf{v}}{\mathbf{F}(\mathbf{v})}
{% end %}

This yields $\mathbf{r}(\mathbf{v})$, which can be rearranged to $\mathbf{v}(\mathbf{r})$. We can then solve for the position explicitly with:

{% math() %}
\mathbf{v}(\mathbf{r}) = \dfrac{d\mathbf{r}}{dt} \Rightarrow \int dt = \int \dfrac{d\mathbf{r}}{\mathbf{v}(\mathbf{r})}
{% end %}

Finally, let us consider a position-dependent force, $\mathbf{F} = \mathbf{F}(\mathbf{r})$. Recall that by the chain rule we previously found that:

{% math() %}
\mathbf{F} =m \dfrac{d\mathbf{v}}{d\mathbf{r}} \cdot \mathbf{v}
{% end %}

Substituting $\mathbf{F} = \mathbf{F}(\mathbf{r})$ yields:

{% math() %}
\mathbf{F}(\mathbf{r}) =m \dfrac{d\mathbf{v}}{d\mathbf{r}} \cdot \mathbf{v}
{% end %}

We once again have a separable differential equation, which can be integrated to have:

{% math() %}
\int \mathbf{F}(\mathbf{r}) \cdot d \mathbf{r} = \int m \mathbf{v} \cdot d\mathbf{v} = \dfrac{1}{2} m \mathbf{v}^2 \bigg |_{v_0}^{v} = \dfrac{1}{2} m\mathbf{v}^2 - \dfrac{1}{2} m \mathbf{v}_0^2
{% end %}

Note that the right-hand side is _equivalent_ to the change in kinetic energy, and the left-hand side is integral to the integral for _work_. Thus we may write the above equivalently as:

{% math() %}
W = \Delta K
{% end %}

Which is the **work-energy theorem**. By some algebraic manipulation of the previous results we have:

{% math() %}
\begin{gather*}
\dfrac{1}{2} m (\mathbf{v}^2 - \mathbf{v}_0^2 ) = \int \mathbf{F}(\mathbf{r}) \cdot d \mathbf{r} \\
\mathbf{v}^2 = \mathbf{v}_0^2 + \frac{2}{m}\int \mathbf{F}(\mathbf{r}) \cdot d \mathbf{r} \\
\mathbf{v} = \left[\mathbf{v}_0^2 + \frac{2}{m}\int \mathbf{F}(\mathbf{r}) \cdot d \mathbf{r}\right]^{1/2}
\end{gather*}
{% end %}

From $\mathbf{v}(\mathbf{r})$ we may rearrange to solve for the position, as we previously showed for a velocity-dependent force:

{% math() %}
\mathbf{v}(\mathbf{r}) = \dfrac{d\mathbf{r}}{dt} \Rightarrow \int dt = \int \dfrac{d\mathbf{r}}{\mathbf{v}(\mathbf{r})}
{% end %}

| Force                              | Velocity                                                                                                                                | Position                                                                                                          |
| ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| Constant force                     | $\mathbf{v}(t) = \mathbf{v}_0 + \dfrac{\mathbf{F}_0}{m} t$                                                                              | $\mathbf{r}(t) = \mathbf{r}_0 + \mathbf{v}_0 t + \dfrac{1}{2} \dfrac{\mathbf{F}_0}{m} t^2$                        |
| Force dependent on _only_ position | $\mathbf{v}(\mathbf{r}) = \left[\mathbf{v}_0^2 + \dfrac{2}{m}\displaystyle \int \mathbf{F}(\mathbf{r}) \cdot d \mathbf{r}\right]^{1/2}$ | $t(\mathbf{r}) = \displaystyle \int \dfrac{d\mathbf{r}}{\mathbf{v}(\mathbf{r})}$, rearrange to $\mathbf{r}(t)$    |
| Force dependent on *only* velocity | $t(\mathbf{v}) = m\displaystyle \int \dfrac{d\mathbf{v}}{\mathbf{F}(\mathbf{v})}$, rearrange to $\mathbf{v}(t)$                         | $t(\mathbf{r}) = \displaystyle \int \dfrac{d\mathbf{r}}{\mathbf{v}(\mathbf{r})}$, rearrange to $\mathbf{r}(t)$    |
| Force dependent on *only* time     | $\mathbf{v}(t) = C_1 + \dfrac{1}{m} \displaystyle \int\mathbf{F} (t) d t$                                                               | $\mathbf{r}(t) = C_2 + C_1 t + \dfrac{1}{m}\displaystyle \int\left[\displaystyle \int\mathbf{F} (t) d t\right]dt$ |

Note that these are not the only cases for forces that can be solved explicitly. A broader class of forces can be solved if they are _factorable_ into independent components of one variable. These may be called _separable forces_ and allow separation of variables to be used to find a general solution.

For instance, a separable force dependent on velocity *and* position $\mathbf{F}(\mathbf{v}, t) = f(\mathbf{v}) g(t)$ has the general solution:

{% math() %}
\int g(t) dt = m \int \dfrac{d\mathbf{v}}{f(\mathbf{v})}
{% end %}

Meanwhile, a separable force dependent on position *and* velocity $\mathbf{F}(\mathbf{r}, \mathbf{v}) = f(\mathbf{r})g(\mathbf{v})$ has the general solution:

{% math() %}
\int f(\mathbf{r})d\mathbf{r} = m\int \dfrac{\mathbf{v} d\mathbf{v}}{g(\mathbf{v})}
{% end %}

However, a force dependent on _both_ position and time in the form $\mathbf{F}(\mathbf{r}, t)$, even if separable, cannot be integrated. Thus, for such a force, no general (closed-form) solution exists.

### Potential energy and conservation of energy

In our analysis of position-dependent forces, we derived the work-energy theorem, $W = \Delta K$. We will now see that the work-energy theorem leads to a powerful tool for the analysis of motion.

Recall that the work-energy theorem is the result that:

{% math() %}
W = \int_a^b \mathbf{F} \cdot d\mathbf{r} = \dfrac{1}{2} m (\mathbf{v} - \mathbf{v}_0)^2 = \Delta K
{% end %}

That is to say, work done (i.e. energy transfered) by a force to bring an object from position $a$ to position $b$ accelerates an object from velocity $\mathbf{v}_0$ to velocity $\mathbf{v}$, thereby increasing its kinetic energy by $\Delta K$. Now, note that this may _also_ be written:

{% math() %}
\int_a^b \mathbf{F} \cdot d\mathbf{r} = \dfrac{1}{2} m \mathbf{v}^2 + K_0
{% end %}

where $K_0 = \dfrac{1}{2} m \mathbf{v}_0{}^2 = \text{const.}$ is the initial kinetic energy of the object. Now, if we define a function $U$ by $\mathbf{F} = -\nabla U$, then we find that: 

{% math() %}
-\int_a^b \nabla U \cdot d\mathbf{r} = \dfrac{1}{2} m \mathbf{v}^2 + K_0
{% end %}

By the **gradient theorem of line integrals** from vector calculus, we note that:

{% math() %}
\int_a^b \nabla U \cdot d\mathbf{r} = U(b) - U(a) = \Delta U
{% end %}

Therefore, substituting into our previous relation, we have:

{% math() %}
-\int_a^b \nabla U \cdot d\mathbf{r} = -\Delta U = \dfrac{1}{2} m \mathbf{v}^2 + K_0
{% end %}

Which we can simplify to:

{% math() %}
-\Delta U = \Delta K
{% end %}

Since the units of $\Delta U$ are the same as $\Delta K$, we know that this is a quantity that has units of **energy**. We call this energy **potential energy**. Potential energy is the energy an object possesses from its _position_, rather than its _velocity_. When an external force changes the position of an object against the other forces acting on the object, doing work in the process, such as lifting a boulder up a hill (against gravity), an object _gains_ potential energy. When an object is kept at a maxima of $U(\mathbf{r})$ (such as the top of a hill), it is unstable, and with a little nudge, the object quickly begins moving towards a minima of $U(\mathbf{r})$, _losing_ potential energy. This is the key takeaway of the equation $\Delta K = -\Delta U$:

> **As an object falls down a potential $U(\mathbf{r})$, it gains kinetic energy and therefore speeds up**.

Which follows from $\mathbf{F} = -\nabla U$, which can be rewritten $m \dfrac{d\mathbf{v}}{dt} = -\nabla U$. Furthermore, if we expand $\Delta K = -\Delta U$, we find that:

{% math() %}
\begin{align*}
\Delta K &= K(b) - K(a) \\
\Delta U &= U(b) - U(a) \\
\Delta K &= -\Delta U \Rightarrow \\
K(b) - K(a) &= -(U(b) - U(a)) \\
&= U(a) - U(b)
\end{align*}
{% end %}

That is to say, any _gain_ in kinetic energy of an object moving between two points $a$ and $b$ must result in an equal amount of _loss_ of potential object. This is known as the **law of the conservation of energy**:

> **Energy cannot be created or destroyed. The total energy of a system, given by $E = K + U$, must remain constant**.

Conservation of energy offers an alternative route to deriving the trajectories of objects that does not involve Newton's laws. To show how this is the case, let us explicitly write out the conservation of energy in 1 dimension:

{% math() %}
\begin{align*}
E &= K + U \\
&= \dfrac{1}{2} mv^2 + U(x) \\
&= \dfrac{1}{2} m \left(\dfrac{dx}{dt}\right)^2 + U(x)
\end{align*}
{% end %}

We note that we have now arrived at a separable differential equation:

{% math() %}
\dfrac{1}{2} m \left(\dfrac{dx}{dt}\right)^2 + U(x) = E
{% end %}

We may rearrange this differential equation to place it into more standard form:

{% math() %}
\dfrac{dx}{dt} = \pm \sqrt{\dfrac{2}{m}(E - U(x))}
{% end %}

By separating the variables we have:

{% math() %}
\int dt = \pm \int \dfrac{dx}{\sqrt{\dfrac{2}{m}(E - U(x))}}
{% end %}

But note that the $\pm$ sign almost always turns out to a positive. Otherwise, the trajectory would predict a trajectory propagating _backwards_ in time, which is unphysical. In addition, to prevent an imaginary term in the denominator (which would also be unphysical), the condition $E - U(x) \geq 0$ _must_ be met. Therefore, the general solution is given by:

{% math() %}
t(x) = t_0 + \int_{x_0}^x \dfrac{dx'}{\sqrt{\dfrac{2}{m}(E - U(x'))}}
{% end %}

Where we would typically want to rearrange $t(x) \to x(t)$ upon evaluating the integral and finding the solution. The initial condition can be found as long as the kinetic and potential energies are known at $t = 0$ - then one may compute $E$ at $t = 0$, and we know from conservation of energy that $E$ will stay constant.

> **Note on notation:** the primes in the integral above are due to the fact that we have to change our integration variables to not confuse ourselves with the bounds of the integral. They _are not meant to represent derivatives_.

But it is often not even necessary to solve the equation for $t(x) \rightarrow x(t)$. In fact, knowledge of $U(x)$ is often sufficient to understand a great deal about the motion of a moving object. A graph of the potential energy function, for instance, is shown below:

![A graph of a potential energy function U(x) that curves up to a local maximum, then curves down to a local minimum, then curves upwards again](http://spiff.rit.edu/classes/phys211/workshops/w_force_pote/cubic_a_label.png)

_Source: [Michael Richmond, RIT](http://spiff.rit.edu/classes/phys211/workshops/w_force_pote/pote_graph.html)_

By the equation $\mathbf{F} = -\nabla U$, objects naturally travel _down_ a potential towards minima. Therefore, maxima of the potential function $U$ are considered _unstable points_. An object with a potential energy $U = U_\mathrm{max}$, that is, a potential energy equal to a maximum of $U(\mathbf{r})$, is easy to "nudge" away from the maximum. The object proceeds to "fall" towards a minimum, which may be a local or global minimum. When the minimum is U-shaped, we frequently call it a _potential well_ - such potentials contain a minimum at their center that is a _stable point_. Thus objects with a potential energy at a minimum of a potential well actually require a force to increase their energy to "climb out" of the well. There exist many famous examples of potential wells - the **gravitational potential energy** and **electrostatic potential energy** both have potential wells that constrain the motions of massive (i.e. having mass) objects and charged objects, respectively. For those forces, it is common to define a **potential**, which is the potential energy assuming an object has unit (i.e. exactly $m = 1$) mass (for gravity) or unit charge (for electrostatics). An approximate plot of the gravitational potential looks as follows:

![A plot of the gravitational potential, showing the "U" shaped potential function, which is potential energy for a unit mass](https://upload.wikimedia.org/wikipedia/commons/d/d9/GravityPotential.jpg?20080412172341)

_Source: [Wikipedia](https://commons.wikimedia.org/wiki/File:GravityPotential.jpg)_

Before we conclude our preliminary discussion of potential energy, there is one burning question we must address: **is the potential energy truly a function?** Throughout the majority of our discussion we have treated potential energy as a _function_. Many texts would shun the idea of describing potential energy as a function, and consider only the _change_ in potential to be a real quantity. Which is correct? Actually, both. It doesn't _actually matter_ what the potential is, since the _change in potential_ is what truly matters; in $\mathbf{F} = -\nabla U$ as well as $\Delta K = -\Delta U$, we don't see $U(\mathbf{r})$ itself appear, only its derivative, which measures _changes_ in potential. So we *can* call the potential energy a function. The only caveat is that since the derivative of a constant is zero, $U(\mathbf{r}) + C$ is physically equivalent to $U(\mathbf{r})$. In fact, the potential energy can even be negative(!) since that has no effect on _changes_ in potential energy. Therefore, to specify a unique potential energy function, we typically set $U(\mathbf{r}_0) = 0$ at a specific point $\mathbf{r}_0$, meaning that we agree that at a particular point, the potential energy is zero. This often is at $\mathbf{r}_0 = \infty$, i.e. a point infinitely far away, although it depends on the problem.

## Special relativity

In the previous section, we examined _classical physics_ dating from the time of Newton and his contemporaries. By comparison, _modern physics_ began in 1905, in which Albert Einstein published his groundbreaking paper _On the Electrodynamics of Moving Bodies_ (an [excellent translation can be found at this link](https://users.physics.ox.ac.uk/~rtaylor/teaching/specrel.pdf)). By drawing intuitive arguments from electromagnetic theory, Einstein showed that different moving observers _could not agree_ on quantities that were thought to be fundamental, including velocities, distances, and time intervals. These revolutionary new ideas took the physics world by storm and gave physics one of the most successful - if mindbending - theories of science. Special relativity is a highly unintuitive subject and requires a careful treatment as well as thorough study - it is recommended to go through this section slowly.

### Rest frames and moving frames

The fundamental concept within special relativity is that of **reference frames**. A reference frame is a system of coordinates with a specific origin. For instance, one could define a reference frame next to a desk, on board a moving train, or even on a rocket (moving at constant speed) through space. Once an origin is chosen, a reference frame allows measuring lengths and angles to precise numerical values. With the addition of a clock, a reference frame also allows measuring *time intervals* - the amount of time that passes between two events.

While there may be forces and accelerating objects _within_ a reference frame, we presume in special relativity that reference frames *themselves* are moving at **constant velocity** (or stationary) with respect to each other. _Accelerating_ reference frames are outside the scope of special relativity; they require **general relativity** to be fully understood. Special relativity only deals with non-accelerating reference frames.

The fundamental issue at the heart of special relativity is to consider how measurements of lengths and times map between reference frames that are moving with respect to each other. In technical terms, this is known as the problem of **coordinate transformations**. To study this topic, we imagine that an **observer** is present in each reference frame, who possesses some sort of length-measuring device (e.g. a ruler) and some sort of time-keeping device (e.g. a clock). An observer does *not* have to be a real person, it simply represents a hypothetical person that can take measurements who is located in a particular reference frame. A given observer may be present in the middle of deep space, on the side of a rocket, or even following a relativistic neutrino moving at 99.9% of the speed of light - understandably, these are not necessarily places where _real human observers_ would go.

An observer's own reference frame is known as the observer's **rest frame**. This is the frame where the observer (unsurprisingly) is stationary, and also includes everything stationary with respect to them. An observer flying in an airplane would consider everything inside the airplane (and the airplane itself) to be within its rest frame, even though another observer on the ground would say that the airplane - and everything within it - is moving very fast over their head. Let us re-emphasize:

> **Every observer considers themselves and everything in their rest frame to be stationary, and everything else in the Universe to be moving relative to them.**

Within their rest frames, the distance an observer measures is called the **proper length**, often denoted $L$, and the time interval an observer measures is called the **proper time**, for which it is customary to use the greek letter $\tau$ ("tau"). A student sitting next to a desk (assuming this is a normal everyday desk that remains fixed in place) would be measuring the proper length of the desk, as the desk is at rest with respect to the student. Additionally, if that student were sitting in a classroom with their teacher in front of the classroom, that same student would measure the time interval until their homework deadline is due to be the **proper time** (although the student would likely think there is _no proper time_ for needing to do homework). This would be _quite unfortunate_ for the student who has not started their homework, and is told by their teacher that they have only 5 minutes (!!) until their homework is due. The teacher (as well as the teacher's clock) would both be in the student's rest frame, and thus the poor student does, indeed, measure a proper time of 5 minutes remaining to do their homework. However, we will see soon that a _moving student_ would actually measure a _different_ time until their homework is due, and a _moving student_ (perhaps flying in through the window) would also measure a different length of the desk. The distances and times measured by the moving student (of the desk and the time until their homework due-date) are referred to as the **coordinate length** and **coordinate time** respectively.

Likewise, while desks are not known to be conscious or indeed interested in physics, the teacher at the front of the classroom *is* presumably interested in when their student hands in their homework. The teacher considers everything within their classroom to be at rest with respect to them - at least, _if the student were stationary_ - and as such, all things within their classroom would be within their rest frame. This means that the teacher's measurement of the student's desk would be its **proper length**, and of the 5 minutes until the homework is due to be the **proper time**. However, should the student come flying through the window at 99.9% of the speed of light, the student would no longer be in their rest frame, but instead, in a _moving frame_. Indeed, the teacher would actually see the student _slowed down_. If the student somehow managed to pick up the desk while flying through the window - no doubt, a feat of Olympic-level skill and airmanship - the teacher would measure the length of the desk held by the student to be its **coordinate length**. Furthermore, the teacher would measure the time until the student hands in their homework as the **coordinate time**, and would be astonished to find that the student, having just started their homework 5 minutes before the deadline, finished 30 seconds _before the deadline_, as measured in the teacher's frame. What the teacher would _not_ initially realize, however, is that in the student's rest frame, the student perceives the _teacher's_ clock (and everything else in the classroom) to be running slow, allowing the student to have a leisurely 1 hour and 51 minutes to complete their homework - more than enough to get it done on time, with 30 seconds (11 minutes when measured in the student's frame) to spare.

### Length contraction and time dilation

As we have seen, special relativity results in some very bizarre predictions for objects moving close to the speed of light. We will now give the precise mathematical formulations for two of them: **length contraction** and **time dilation**.

Consider an observer within a moving reference frame, such as a passenger riding in a train, who holds a book. The passenger would consider the train car (and everything within it, including the book) to be in their rest frame. Thus, the passenger measures the length of the book to take its proper length $L_0$. But an observer in a different reference frame - such as a person on the ground watching the train go by - would measure a _different_ length for the book, which we denote $L$. The mathematical relationship between $L$ and $L_0$ is given by:

{% math() %}
L = \dfrac{1}{\gamma(v)} L_0
{% end %}

- $L$ is the length of the object, as measured by an observer that observes the object moving
- $L_0$ is the length of the object within the object's rest frame
- $\gamma(v) = \dfrac{1}{\sqrt{1 - v^2/c^2}}$ is the Lorentz factor, where $v$ is the velocity of the moving reference frame relative to the observer's rest frame

Note that the length contraction formula may also be written in differential form, where $dx$ is an infinitesimal length as measured by the observer who measures the moving object, and $ds$ is the infinitesimal proper length:

{% math() %}
dx = \dfrac{1}{\gamma(v)} ds
{% end %}

In the train and ground observer case, the observer on the ground would measure the book to be of length $L$, the passenger in the train care would measure the book to be of length $L_0$, and the observer on the ground would measure the speed of the train to be $v$ relative to their rest frame. This is known as **length contraction**.

But this goes the opposite way too. The passenger riding the train, observing the person on the ground, would consider the person on the ground to be moving and themselves (and everything else in the train) stationary. If the person on the ground were holding a ruler, which had length $L_0$ in its rest frame (the reference frame of the person on the ground), the passenger on the train would measure the ruler to have length $L$. Furthermore, the passenger on the train would observe the person on the ground to be receding away as the train moves forwards. As the passenger considers the train and everything in it to be their rest frame, the passenger would measure the speed of the person on the ground, which appears to be moving away, to _also_ be $v$ relative to their rest frame (speed is always positive as it is directionless).

In addition, observers don't just measure different lengths of moving objects. Observers also measure different _times_. More specifically, an observer measuring a moving object would measure time $t$ on their clocks, while a clock in the moving object's rest frame would measure time $\tau$. This is known as **time dilation**, and the equation for time dilation is given by:

{% math() %}
t = \gamma(v) \tau
{% end %}

- $t$ is the time shown on the clock of an observer that observes the object moving
- $L_0$ is the time shown on a clock within the object's rest frame
- Once again, $\gamma(v) = \dfrac{1}{\sqrt{1 - v^2/c^2}}$ is the Lorentz factor, where $v$ is the velocity of the moving reference frame relative to the observer's rest frame

The differential equivalent of the time dilation formula can be found by taking the derivative with respect to $\tau$ on both sides:

{% math() %}
\dfrac{dt}{d\tau} = \dfrac{d}{d\tau} \gamma (v) \tau = \gamma(v)
{% end %}

Which can also be written:

{% math() %}
dt = \gamma(v) d\tau
{% end %}

Or:

{% math() %}
dt = \int \gamma(v) d\tau
{% end %}

This means that the rate at which the observer measures all objects that were moving with respect to them to be increased - as $\gamma \geq 1$. That is to say, the observer finds that _clocks in moving reference frames run slow_. The observer measures what _would_ be a one-second time interval in their rest frame to take longer - and possibly _much longer_ - in a moving reference frame. If an Earthbound observer finds that a lightbulb turns off in 0.5 seconds after pressing the switch, the same observer would conclude that an astronaut traveling on a spaceship turning an _identical_ lightbulb to need _longer_ than 0.5 seconds to turn off.

### The Lorentz transformations

We have explored _what_ the implications of special relativity are - including the equations governing time dilation and length contractions. Now let's explore the _why_. And for special relativity, the postulates that lead to the entire theory are surprisingly straightforward:

1. The laws of physics are the **same in all reference frames**
2. There exists a fundamental speed $c$ that takes **an identical value in all reference frames**, which coincides with the speed of light

The first postulate is known as the **principle of relativity**. It establishes the fact that _motion is always relative_, since each observer possesses their own rest frame and considers everything not in their rest frame to be moving, which means that different observers will often disagree on who and what is moving. 

For instance, this means that an astronaut aboard an orbiting spaceship would say that the Earth is moving from them at some velocity $-v$ (as it is moving *away*), while a person on the ground would say that the Earth is stationary and that instead it is the _astronaut_ that is moving at velocity $v$  (moving *towards* the Earth). Is the astronaut wrong, or is the person on the ground wrong, about who is moving? The answer is **neither**. The laws of physics make the same predictions whether you take the Earth's rest frame and consider the astronaut to be moving, or if you take the astronaut's rest frame and consider the Earth to be moving. There is **no preference** for which reference frame to use. We emphasize:

> If observer $A$ measures observer $B$ to be moving (away) at velocity $v$, observer $B$ would measure observer $A$ to be moving (towards $A$) at velocity $-v$. **Both statements are equally valid. The laws of physics yield the same results, *regardless* of which reference frame is chosen as the one moving, and which one is chosen as the one stationary.**

The second postulate is easily misunderstood, because it is often quoted as _"the speed of light is identical in all reference frames"_. While this is _technically true_ (at least for light propagating through vacuum), the speed of light only coincides with the speed we know as $c$, that is, $\pu{299 792458m/s}$, due to quantum mechanical reasons, and $c$ would be a speed that would exist even if light did not exist. Further, $c$ is not just the speed of light - it is also the _speed of gravity_, which means that if the Sun happened to disappear, the Earth would still stay in its orbit for another 8 minutes, as if nothing happened. Rather, $c$ should be thought of as _the maximal speed of any propagation in the Universe_. **Nothing** can travel faster than the speed of light; it is a fundamental universal constant that determines cause and effect, and anything faster than $c$ would inevitably result in violations of causality.

The result of the two fundamental postulates of special relativity is that the coordinates $(t, x, y, z)$, measured by an observer $A$ are related to the coordinates $(t', x', y', z')$ measured by an observer $B$ by the **Lorentz transformations**:

{% math() %}
\begin{align*}
t' &= \gamma(v)\left(t - \dfrac{v x}{c^2}\right) \\
x' &= \gamma(v)\,(x - vt) \\
y' &= y \\
z' &= z
\end{align*}
{% end %}

Where $v$ is the **speed** (not velocity) at which observer $B$'s reference frame moves, relative to observer $A$ (note that the Lorentz factor is a multiplication factor to the time/space displacements, not a function composition). It is also possible to write the Lorentz transformations in a simpler form, by defining $\beta \equiv v/c$ and $\gamma(\beta) = \dfrac{1}{\sqrt{1 - \beta^2}}$, for which we have:

{% math() %}
\begin{align*}
ct' &= \gamma(\beta)\,(ct - \beta x) \\
x' &= \gamma(\beta)\,(x - \beta ct) \\
y' &= y \\
z' &= z
\end{align*}
{% end %}

For instance, imagine an observer on the Earth watching a asteroid (or maybe comet) fly by - perhaps Halley's comet, and for a more optimistic mood, we are assuming that observer is _not_ a dinosaur 65 million years ago. At a particular instant in time $t$, our Earthbound observer would measure the position of the asteroid/comet to be $(t, x, y, z)$. We call this an **event** - the specific event being that the meteor reached the spot described by coordinates $(t, x, y, z)$ in our Earthbound observer's reference frame.

> **Note:** It is typical in relativity to write out events in terms of coordinates $(ct, x, y, z)$, and indeed this will be our convention. This means that time is measured in _meters_ rather than in seconds. Why do this? We will see soon that it is a natural consequence of the inseparable nature of space and time.

Consider another observer passing by Earth in a spaceship, and, out of fascination with the asteroid/comet, the spacefaring observer decides to swoop by it at 95% the speed of light, in violation of the Solar System spacecraft speed limit - but that observer will worry about the ticket from the space police another day. This spacefaring observer would measure the comet at the same spot as the Earthbound observer with coordinates $(ct', x', y', z')$. We will make the assumption that the two observers are aligned along the $x$ axis.

The Earthbound observer would be able to find the coordinates measured by the *spacefaring observer* $(ct', x', y', z')$ of the event (the arrival of the asteroid/comet) by applying the Lorentz transformations on their own coordinates $(ct, x, y, z)$. Meanwhile, the spacefaring observer would be able to find the coordinates measured by the *Earthbound observer* by applying the _inverse_ Lorentz transformations on their coordinates $(ct', x', y', z')$. Note that the inverse transformations are given by:

{% math() %}
\begin{align*}
t &= \gamma(v)\left(t' + \dfrac{v x'}{c^2}\right) \\
x &= \gamma(v)\,(x' + vt') \\
y &= y' \\
z &= z'
\end{align*}
{% end %}

Or in the (often more useful) alternative form where we define $\beta \equiv v/c$ (remember, $v$ is **speed** not velocity) and consequently $\gamma(\beta) = \dfrac{1}{\sqrt{1 - \beta^2}}$:

{% math() %}
\begin{align*}
ct &= \gamma(\beta)\,(ct' + \beta x') \\
x &= \gamma(\beta)\,(x' + \beta ct') \\
y &= y' \\
z &= z'
\end{align*}
{% end %}

Note that the coordinates $(ct, x, y, z)$ and $(ct', x', y', z')$ _differ_, not just in space, but also in time. This is the central theme of relativity: **different observers will have different measurements of the same object (or event)**. We will see that this theme appears again and again in special relativity, as we continue our study of relativistic phenomena.

### Velocity addition

Consider the same example of a moving train, but let us now consider a _walking_ observer along the train. Let us say that the train itself moves at speed $v$ relative to an observer on the ground, and this person walks at speed $v'$ inside the train. What would be the speed $u$ of the walking person, measured by the observer on the ground?

The answer: the velocities of moving objects within a moving reference frame, as measured by an observer in their rest frame, is given by the **relativistic velocity (speed) addition** formula:

{% math() %}
u = \dfrac{v + v'}{1 + \frac{vv'}{c^2}}
{% end %}

Where:

- $v$ is the speed of the moving reference frame
- $v'$ is the speed of the object *within* the moving reference frame
- $u$ is the speed of the object, measured in the observer's rest frame (in which the observer is stationary)

> Despite its name, this formula is (at least in this form) **not** a formula for adding *velocities*, but rather a formula for adding *speeds* - that is, magnitudes of velocity. Adding vector-valued velocities requires a different set of formulas, which we will see soon.

It is convenient, when speeds are given in terms of percentages of the speed of light (such as $v = 0.8 c$ or $v = 0.65 c$), to use the modified version of the formula:

{% math() %}
\chi = \dfrac{\alpha + \beta}{1 + \alpha \beta}
{% end %}

Where:

- $\beta$ is the speed of the moving reference frame, *as a fraction of the speed of light*
- $\alpha$ is the speed of the object *within* the moving reference frame, *as a fraction of the speed of light*
- $\chi$ is the speed of the object, measured in the observer's rest frame (in which the observer is stationary), *as a fraction of the speed of light*

Note that we can also turn this formula around so that the person *walking on the train* can find the speed at which the *person on the ground* is moving away as the train passes by. This may seem rather unintuitive; but remember, in special relativity, _motion is relative_, and thus it is perfectly acceptable to speak of the person on the ground as moving and the walking passenger on the train as stationary.

#### Velocity addition in vector form

We have seen the equation for how to add _speeds_, but what about velocities? As we mentioned previously, the "velocity addition formula" actually concerns _speeds_, not velocities. So instead, we have to use the Lorentz transformations to be able to derive the equations for the addition of _velocities_.

To do so, let us first recall that the Lorentz transformations are given by:

{% math() %}
\begin{align*}
ct' &= \gamma(\beta)\,(ct - \beta x) \\
x' &= \gamma(\beta)\,(x - \beta ct) \\
y' &= y \\
z' &= z
\end{align*}
{% end %}

For brevity, we will now write $\gamma$ instead of $\gamma(\beta)$, although remember that $\gamma$ represents the _value_ of the Lorentz factor at $v/c = \beta$ (where $\beta$ is the percent of the speed of light).

Now consider a observer (say, standing on the ground) that measures another observer (say, riding on a train) as moving _with respect to_ their rest frame. For simplicity, we will call the observer on the ground as the **stationary observer** and the observer riding the train as the **moving observer**. Of course, this is only true with respect to the ground observer's rest frame; in special relativity we know that _all motion is relative_, and another observer (e.g. on an airplane) could very reasonably complain that *both* of the aforementioned observers are moving! We will simply stick to this convention to keep the clarity of the physics to a maximum and the reader's annoyance to a minimum.

Now assume that the moving observer sees an object moving in their frame (maybe their eyeglasses that they absentmindedly dropped and are now desperately trying to find). This object (the eyeglasses in this case) is measured by the moving observer to have velocity $v_x'$ as it falls (miraculously) *exactly along* the $x'$ direction. As the moving observer awkwardly tries to find their glasses with less-than-ideal eyesight, the stationary observer looks on with interest. The stationary observer bets that with their superior physics expertise, they can deduce the velocity of the falling glasses in their frame, $u_x$, and thereby calculate where the glasses will land, long before the moving observer manages to find them.

Let us now write out the Lorentz transformations. Since we consider the case of an object travelling on the $x'$ axis, we can ignore the two other transformations of $y'$ and $z'$, so we are simply left with:

{% math() %}
\begin{align*}
ct' &= \gamma(ct - \beta x) \\
x' &= \gamma (x - \beta c t)
\end{align*}
{% end %}

Here, $(ct', x')$ represent the coordinates of the object (eyeglasses) within the moving observer's frame. The velocity of the object within the moving observer's frame is thus given by $v_x' = \dfrac{dx'}{dt'}$. We want to find $u_x = \dfrac{dx}{dt}$, the velocity of the object (eyeglasses) within the *stationary observer's* reference frame in terms of $v_x'$. To start with the derivation of the formula, we differentiate the second Lorentz transformation $x' = \gamma(x - \beta c t)$ with respect to $t'$, as follows:

{% math() %}
\begin{align*}
v_x' &= \dfrac{dx'}{dt'} \\
&= \dfrac{d}{dt'} [\gamma(x - \beta c t)] \\
&= \gamma \left(\dfrac{dx}{dt'} - \beta c \dfrac{dt}{dt'}\right)\\
&= \gamma\left(\dfrac{dx}{dt} \dfrac{dt}{dt'} - \beta c \dfrac{dt}{dt'}\right) \\
&= \gamma\left(u_x \dfrac{dt}{dt'} - \beta c \dfrac{dt}{dt'}
\right) \\
&= \gamma(u_x  - \beta c)\dfrac{dt}{dt'}
\end{align*}
{% end %}

> **Be careful!** Within the Lorentz transformations, $x$ is a function of $t$, $x'$ is a function of $x$, and $t'$ is a function of $t$, so you need to use the chain rule! The only function that satisfies 

Now using $ct' = \gamma(ct- \beta x)$ which we can rearrange to $t' = \frac{\gamma}{c}(ct- \beta x)$, and differentiating with respect to time, we have:

{% math() %}
\begin{align*}
\dfrac{dt'}{dt} &= \dfrac{d}{dt} \left[\frac{\gamma}{c}(ct- \beta x)\right] \\
&=\dfrac{\gamma}{c} \left(c \dfrac{dt}{dt}- \beta \dfrac{dx}{dt}\right) \\
&= \dfrac{\gamma}{c} \left(c - \beta u_x\right) \\
\end{align*}
{% end %}

By the inverse derivatives rule $\frac{dx}{dy} = 1 / \frac{dy}{dx}$, we have:

{% math() %}
\dfrac{dt}{dt'} = \dfrac{1}{\frac{dt'}{dt}} = \dfrac{c}{\gamma} \dfrac{1}{c - \beta u_x}
{% end %}
Thus we have:

{% math() %}
\begin{align*}
v_x' &= \gamma(u_x  - \beta c)\dfrac{dt}{dt'} \\
&= \gamma(u_x  - \beta c)\dfrac{c}{\gamma} \dfrac{1}{c - \beta u_x} \\
&= \cancel{\gamma}(u_x  - \beta c)\dfrac{c}{\cancel{\gamma}} \dfrac{1}{c - \beta u_x} \\
&= \dfrac{c(u_x - \beta c)}{c - \beta u_x} \\
\end{align*}
{% end %}

We may rearrange this expression to be able to find $u_x$:

{% math() %}
\begin{align*}
v_x' &= \dfrac{c(u_x - \beta c)}{c - \beta u_x} \\
(c - \beta u_x) v_x' &= c(u_x - \beta c) \\
cv_x' - \beta u_x v_x' &= c u_x - \beta c^2 \\
cu_x + \beta u_x v_x' &= c v_x' + \beta c^2 \\
u_x(c  + \beta v_x') &= c v_x' + \beta c^2 \\
u_x &= \dfrac{c v_x' + \beta c^2}{c  + \beta v_x'} \\
&= \dfrac{c v_x' + \beta c^2}{c  + \beta v_x'} \cdot \dfrac{1/c}{1/c} \\
&= \dfrac{v_x' + \beta c}{1 + \beta v_x'/c} \\
&= \dfrac{v_x' + v}{1 + v v_x'/c^2}
\end{align*}
{% end %}

Which is the velocity-addition formula (except now _actually_ for velocities)! Incidentally, if we _don't know_ $v_x'$ (that is, the velocity of the object in the moving observer's frame), we can also rearrange our derived expression for $v_x'$ to find an expression for $v_x'$ in terms of $\beta \equiv v/c$ and $u_x$ (the speed of the moving observer's frame measured by the stationary observer):

{% math() %}
\begin{align*}
v_x' &= \dfrac{c(u_x - \beta c)}{c - \beta u_x} \\
&= \dfrac{c(u_x - \beta c)}{c - \beta u_x} \cdot \dfrac{1/c}{1/c} \\
&= \dfrac{u_x - \beta c}{1 -  \beta u_x / c} \\
&= \dfrac{u_x - v}{1- u_x v / c^2}
\end{align*}
{% end %}

Again, it is important to know what $\beta$, $v_x'$, and $u_x$ mean:

- $v$ is the **speed** of the moving observer's reference frame, measured by the stationary observer
- $\beta \equiv v/c$ is $v$ as a fraction of the speed of light. E.g. $\beta = 0.3$ is equal to 30% of the speed of light.
- $v_x' = \dfrac{dx'}{dt'}$ is the velocity along $x'$ of the object within the *moving observer's* reference frame
- $u_x = \dfrac{dx}{dt}$ is the velocity along $x$ of the object measured within the *stationary observer's reference frame*

### Minkowski spacetime

After going through so much of special relativity, it is helpful to ask the question: what is it _truly for_? What do the coordinates represent? The answer is that coordinates describe an _event_ that occurs in terms of its time and location in a particular reference frame. What is an event? An event is _anything that happens_, which may be your physics teacher shouting at you for not having your homework, your dog eating your homework, or anything in between. Each of these (rather unfortunate) events are described by a particular time and a particular location in space, and thus in special relativity, an event can be written as a 4-element vector, known as the **four-position**, which is given by:

{% math() %}
\mathbf{X} =
\begin{bmatrix}
ct \\ x \\ y \\ z
\end{bmatrix}
{% end %}

> **Note:** the time component of the four-position is $X_t = ct$ rather than $t$ to keep the units consistent for the four-vector.

Imagine we had two events happening. Perhaps we are interested in _how much time and distance_ separates the two events. For instance, at the event associated with the time and place of your dog eating your homework, you may want to know in advance how much time (and at what location) your teacher will shout at you for it. We call the _separation between events_ the **spacetime interval** (because it includes both space and time). It is written:

{% math() %}
\Delta s^2 = -c^2 \Delta t^2 + \Delta x^2 + \Delta y^2 + \Delta z^2
{% end %}

> **Note:** the notation may be somewhat confusing; here, $\Delta x^2 = (\Delta x)^2$.

In special relativity, we are often interested in the *infinitesimal* version of the spacetime interval (sometimes also called the _line element_). This is because the infinitesimal spacetime interval allows us to use calculus to calculate times and distances. The infinitesimal spacetime interval $ds^2$ is given by:

{% math() %}
ds^2 = -c^2 dt^2 + dx^2 + dy^2 + dz^2
{% end %}

Which can _also_ be written in terms of a **displacement vector** (which is the infinitesimal version of the four-position) in terms of a special matrix (that we'll see again soon) as:

{% math() %}
ds^2 =
\begin{bmatrix}
cdt \\ dx \\ dy \\ dz
\end{bmatrix}^T
\begin{pmatrix}
-1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{pmatrix}
\begin{bmatrix}
cdt \\ dx \\ dy \\ dz
\end{bmatrix}
{% end %}

> **Note:** here $T$ denotes the _transpose_ of the displacement vector.

What is special is that $ds^2$ is an **invariant quantity**. An invariant quantity is the same when measured in every reference frame. We already know of one invariant quantity - the speed of light $c$. A stationary observer would measure the speed of light to be $c$ and an observer in a  moving frame with respect to the stationary observer would _also_ measure the speed of light to be $c$. This strange fact - that positions and times are relative, but a combination of them (the spacetime interval) is not - is why special relativity (and relativistic mechanics in general) refers to **spacetime**, the combination of space and time in a way that makes them inseparable.

#### Tensors in special relativity

Let us now return to the four-position to describe events. The four-position can be used to write out the Lorentz transformations in a much more illustrative way:

{% math() %}
\begin{bmatrix}
ct' \\ x' \\ y' \\ z'
\end{bmatrix}
=
\begin{pmatrix}
\gamma & -\gamma\beta & 0 & 0 \\
-\gamma\beta & \gamma & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{pmatrix}
\begin{bmatrix}
ct \\ x \\ y \\ z
\end{bmatrix}
{% end %}

The central matrix is often writte $\Lambda$ and is the **transformation matrix** for coordinates in special relativity. Using these definitions, the Lorentz transfrmations can be written in one line:

{% math() %}
\mathbf{X}' = \Lambda \mathbf{X}
{% end %}

There is also another way to write this equation - using **tensors**. A tensor is a general class of objects that contain components - normal vectors in 3D space (we call these 3-vectors), 4-vectors, 3D matrices, and 4D matrices are all tensors. In addition, tensor components transform according to very specific mathematical laws: this is what makes them very useful for special relativity.

In tensor notation, we use an _index_ to notate a component of a vector or matrix. For instance, a vector would be written as $V^i$ and a matrix would be written as $M_{ij}$. $V^i$ would stand for $(V^0, V^1, V^2, V^3) = (V^t, V^x, V^y, V^z)$, which are the components of the four-vector along $t, x, y, z$. 

The upper and lower indices are important; in special relativity, they are related by the matrix equation:

{% math() %}
\underbrace{\begin{bmatrix}
V_t \\ V_x \\ V_y \\ V_z 
\end{bmatrix}}_{V_i} =
\underbrace{\begin{pmatrix}
-1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{pmatrix}}_{\eta_{ij}}
\underbrace{\begin{bmatrix}
V^t \\ V^x \\ V^y \\ V^z 
\end{bmatrix}}_{V^j}
{% end %}

This can also be written in a different way as follows:

{% math() %}
V_i = \sum_i \sum_j \eta_{ij} V^j
{% end %}

This formulation is powerful because it means that for instance, if you wanted to find the $V_x$ component, you can just substitute $i = 1$ to get:

{% math() %}
\underbrace{V_1}_{V_x} = \eta_{10} \underbrace{V^0}_{V^t} + \eta_{11} \underbrace{V^1}_{V^x} + \eta_{12} \underbrace{V^2}_{V^y} + \eta_{13} \underbrace{V^3}_{V^z}
{% end %}

Where that special matrix $\eta_{ij}$ is a $(4 \times 4)$ matrix called the **Minkowski metric**:

{% math() %}
\eta_{ij} = \begin{pmatrix}
-1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{pmatrix} =
\begin{pmatrix}
\eta_{00} & \eta_{01} & \eta_{02} & \eta_{03} \\
\eta_{10} & \eta_{11} & \eta_{12} & \eta_{13} \\
\eta_{20} & \eta_{21} & \eta_{22} & \eta_{23} \\
\eta_{30} & \eta_{31} & \eta_{32} & \eta_{33} \\
\end{pmatrix}
{% end %}

> **Unrelated note:** Yes, physicists have decided to emulate computer scientists in counting from zero instead of counting from 1 like everyone else; this is no joke.

Why use an abstract index instead of standard vector notation or component notation (e.g. $V_x, V_y, V_z, \dots$)? Because oftentimes, there are _preferred coordinates_ for solving a problem that may not be Cartesian + time coordinates. Sometimes, we would prefer spherical coordinates instead, for instance; sometimes we might want to use a moving reference frame, and in advanced theoretical physics there are very specialized coordinates used to study stars, black holes, and even the entire Universe. Since we can already write (Cartesian) vectors as a superposition of basis vectors in a particular coordinate system, i.e. $\vec V = \displaystyle \sum_i V_i \hat e_i = V_x \hat e_x + V_y \hat e_y + V_z \hat e_z$, we can drop the sum and just call the entire vector $V_i$ (note: in non-special-relativity $V_i = V^i$). 

"Dropping" the sum when we see an index appear twice in a term is called the **Einstein summation convention**. The reason this is possible is that the summation index doesn't really matter; whether we write $\vec V = \displaystyle \sum_i V_i \hat e_i$ or $\vec V = \displaystyle \sum_j V_j \hat e_i$, there is truly no difference because you can use whatever index you want for your summation signs. We call such indices (plural of index) as _dummy indices_ as they can be arbitrarily chosen and play no role in the _mathematical meaning_ of an equation. A popular anecdote is that Einstein got too tired of writing summation signs on his papers on relativity and decided to drop all of them, thereby inventing this convention. There is however a _practical_ benefit to the Einstein summation convention - it makes equations in physics more _elegant_ without the summation signs cluttering in the way.

> **Note:** A lot of tensor information is skipped over here for the sake of an easier explanation, so keep in mind that this as a simplified treatment of tensors and is absolutely not meant to be rigorous.

But let us return to our original topic: writing the Lorentz transformations with tensors. Tensors give us the power to write out the Lorentz transformations without needing to explicitly specify coordinates:

{% math() %}
\begin{matrix*}
X^j = \Lambda_{ij} X^i, & j = i'
\end{matrix*}
{% end %}

They can also be used to write out the infinitesimal spacetime interval as:

{% math() %}
ds^2 = \sum_i \sum_j \eta_{ij} dx^i dx^j
{% end %}

Where in accordance with the Einstein summation convention, we can drop the summation signs to write it equivalently as $ds^2 = \eta_{ij} dx^i dx^j$. But since we know that $ds^2$ is an _invariant quantity_, and $\eta_{ij}$ is a matrix that has components of _entirely constants_, then $\eta_{ij}$ must also be invariant. In fact, $\eta_{ij}$ is called the Minkowski metric for a reason; it is the **spacetime metric** in Minkowski spacetime. A spacetime metric is the unique transformation matrix that allows defining tensors (vectors with upper indices, vectors with lower indices, as well as some more exotic multidimensional objects) in space and time. Minkowski spacetime provides the fundamental structure of special relativity, and it is all based on this special matrix. 

But how do we know that $\eta_{\mu \nu}$ is the fundamental (and correct) metric of Minkowski space? The answer, for now, is that letting $\eta_{\mu \nu}$ be the metric allows for the simplest _invariant expression_ for the line element under the Lorentz transformations, that being the familiar $ds^2 = -c^2 dt^2 + dx^2 + dy^2 + dz^2$. If the Euclidean metric were the metric instead, the line element would be $ds^2 = c^2 dt^2 + dx^2 + dy^2 + dz^2$, which would **not be invariant** under the Lorentz transformations. So, since the Minkowski metric leads to the correct results, which are invariant under the Lorentz transformations, we take it as a postulate that $\eta_{\mu \nu}$ is the metric of Minkowski space.

The more technically-correct answer is that the Minkowski metric is a solution to the **Einstein field equations**. But for that, we'll need General Relativity (GR), and that is a topic for the future.

### Physical laws with 4-vectors

Special relativity requires that Newton's laws be replaced with their relativistic equivalents. In addition, the union of space and time within special relativity requires that we describe common quantities such as velocity, momentum, and position with _4-component vectors_ (four-vectors) instead of three-component vectors we are familiar with in 3D space.

> **Note:** with four-vectors it is common to use greek indices $\mu, \nu, \gamma$ etc. in addition to the roman (latin) indices $i, j, k$ etc. and both are _equivalent_ (although physicists sometimes prefer to use the greek indices for spacetime equations and roman indices for non-spacetime equations that is just a matter of convention).

For instance, we may write down the velocity of a particular object with respect to a given frame as the **four-velocity** $\mathbf{U}$ (or using tensor notation, as $U^\mu$), which has three components of space, and one of time, that is, $\mathbf{U} = \langle \frac{dt}{d\tau}, \mathbf{v}\rangle$. Note that we differentiate with respect to _proper time_ - the time the object experiences in its rest frame. Similarly, we may write down the position of a particular object with a **four-position** $\mathbf{X}$ (or using tensor notation, $X^\mu$).

> **Note:** Again, we only consider constant-velocity reference frames in special relativity. Accelerating reference frames are outside of the scope of special relativity.

#### Invariance of the scalar product

From the postulate that $c$ is a universal constant that takes the same value in all reference frames, it must be the case that the **scalar product** of 4-vectors are an invariant quantity. For given four-vector $\mathbf{X}$, the dot product $\mathbf{X} \cdot \mathbf{X} = \mathbf{X}' \cdot \mathbf{X}'$ stays invariant. Using the **GR sign convention**, the 

{% math() %}
\begin{align*}
\mathbf{X} \cdot \mathbf{X} &= -c^2 X_0 X^1 +  X_1 X^1 + X_2 X^2 + X_3 X^3 \\
&= -c^2 t^2 + x^2 + y^2 + z^2
\end{align*}
{% end %}

This is because the scalar product is defined **not** as $\vec v \cdot \vec w = \sum_i v_i w_i$, as it would be in Euclidean space. Rather, it is defined based on a **metric**, which is a $(4 \times 4)$ matrix that takes the form:

{% math() %}
\eta_{\mu \nu} = \begin{pmatrix}
-1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{pmatrix}
{% end %}

Therefore, the expression for the scalar product becomes:

{% math() %}
\begin{align*}
\mathbf{X} \cdot \mathbf{X} &= \sum_{\mu = 0}^3\sum_{\nu=0}^3 \eta_{\mu \nu} X^\mu X^\nu \\
&= \begin{pmatrix}
-1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{pmatrix}
\begin{bmatrix} ct \\ x \\ y \\ z \end{bmatrix}
\begin{bmatrix} ct & x & y & z \end{bmatrix} \\
&= -c^2 t^2 + x^2 + y^2 + z^2
\end{align*}
{% end %}

> **Sidenote:** we could omit the summation signs if we specify that we're using the Einstein summation convention, but we have included the summation signs here for clarity.

### Relativistic mechanics

To be compatible with the principles of relativity, Newton's laws of motion must be modified from their original form. We will now explore the important differences and implications of the relativistic equations as compared to the Newtonian equations.

**Newton's 1st law**, which states that an object stays in constant motion (i.e. $\mathbf{v} = \text{const.}$) if there are no external forces, must be quantified with the statement _"when measured in the rest frame of the object"_.

**Newton's 2nd law**, whose most general form is $\mathbf{F} = \dfrac{d\mathbf{p}}{dt}$, must be modified to use the _relativistic 4-momentum_ $\mathbf{P} = \gamma m \mathbf{v} = \langle E_0, \gamma p_x, \gamma p_y, \gamma p_z\rangle$ where $p_x, p_y, p_z$ are the conventional components of the 3D momentum vector, and $E_0$ is a special type of energy (that we will see shortly). Therefore, Newton's differential equation takes the form:

{% math() %}
\dfrac{d}{dt}\left(\dfrac{m\mathbf{v}}{\sqrt{1 - \left(\frac{v}{c}\right)^2}}\right) = \mathbf{F}_\mathrm{net}
{% end %}

Or with tensors:

{% math() %}
\dfrac{dP^\mu}{dt} = F^\mu
{% end %}

**Newton's 3rd law**, which mandates that all forces come in pairs of equal magnitude and opposite direction, must be restricted only to those forces _between objects in contact_. Any long-distance force mediated by a field, such as gravitational or electromagnetic force, requires time to propagate due to the finite speed of light.

Relativistic **kinetic energy** does not directly translate from its classical expression. It, however, can be derived from the work-energy theorem (which stays valid even in special relativity), and takes the form:

{% math() %}
K = mc^2(\gamma - 1) = \gamma mc^2 - mc^2
{% end %}

The famous **rest energy** of a particle is given by $E_0 = mc^2$. This is the energy a particle possesses even when it is at rest (with respect to its rest frame) purely due to its mass, and is often also called _mass-energy_. Combining the rest energy and the relativistic kinetic energy gives the relativistic **total energy**:

{% math() %}
E = K + E_0 = \gamma mc^2
{% end %}

From the inner product of the four-momentum $\mathbf{P} \cdot \mathbf{P} = P_\mu P^\mu$ (recall that the scalar products of four-vectors are invariant quantities) we are able to derive the **energy-momentum relation**:

{% math() %}
E^2 = \mathbf{p}^2 c^2 + (mc^2)^2  = \mathbf{p}^2 c^2 + E_0^2
{% end %}

Or more elegantly with tensors as well as the Einstein summation convention:

{% math() %}
E^2 = P_\mu P^\mu = \underbrace{P_t P^t}_{E_0^2} + P_xP^x + P_y P^y + P_z P^z
{% end %}

### General relativity

Up to this point, we have remained fully within the constraints of special relativity, which, as we recall, governs the behavior of _non-accelerating reference frames_. However, there are clearly accelerating reference frames in the Universe! For these, we must use the theory of **General Relativity** (GR). While we will not go into depth on General Relativity, we will take a brief tour and introduce some of its fundamental concepts.

Unlike special relativity, in which tensors are helpful but not _required_, general relativity _nearly entirely_ uses tensors. The Minkowski metric $\eta_{\mu \nu}$ is replaced with the _general_ metric $g_{\mu \nu}$, and the line element becomes (written with the Einstein summation convention):

{% math() %}
ds^2 = g_{\mu \nu} dx^\mu dx^\nu
{% end %}

In general relativity, separate space and time coordinates essentially lose most of their meaning. Clocks and rulers don't just not match up; they are _literally_ themselves distorted by spacetime. For this reason it actually becomes _impossible_ to define a coordinate system that stays physically-meaningful outside a local region of spacetime, because the coordinates themselves change as spacetime changes. For all of these reasons (and more), the Minkowski metric $\eta_{\mu \nu}$ is replaced by the more general spacetime metric $g_{\mu \nu}$. The analogous equation to $\dfrac{dP^\mu}{dt} = F^\mu$ is written with the _proper time_ and is given by:

{% math() %}
\dfrac{d^2 X^\mu}{d\tau^2} = -\Gamma^\mu_{\alpha \beta} \dfrac{dx^\alpha}{d\tau} \dfrac{dx^\beta}{d\tau}
{% end %}

The equations that govern spacetime (and correspondingly how all coordinates change) are the **Einstein Field Equations**:

{% math() %}
G_{\mu \nu} + \Lambda g_{\mu \nu} = \dfrac{8\pi G}{c^4} T_{\mu \nu}
{% end %}

Where $G_{\mu \nu}$ is a tensor that describes the _curvature_ of spacetime, $\Lambda$ is called the **cosmological constant**, and $T_{\mu \nu}$ is an extension of the four-momentum. A full explanation of general relativity is very complicated. But for those readers interested, see [this online astronomy textbook's chapter on GR](https://galaxiesbook.org/chapters/C.-General-Relativity.html), which contains a concise but still accurate summary of General Relativity.

## Lagrangian mechanics

Newtonian mechanics remained a highly successful theory in classical physics for a long time after Newton, but it always had a few fundamental issues, even before the development of relativity and quantum mechanics. These issues are related to the fact that Newtonian mechanics relies on being able to write out a **net force** using vector analysis.

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

### The Newtonian limit

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

{{ diagram(src="simple-pendulum.excalidraw.svg") }}

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

### The centrifugal "force"

When an object is placed within a rotating object, it is common to say that the object experiences a _fictitious_ centrifugal force. We will show that what appears to be a "centrifugal force" is nothing but a radial acceleration caused by a moving coordinate system, and is _not_ a real force.

Consider a moving disk of radius $R$ and mass $M$ that rotates at angular velocity $\omega$ (ignore gravity). A small mass $m$ is placed at the edge of the disk (note: the figure below shows it _slightly_ less than the edge, but it is only for visual clarity). A diagram of our physical scenario is below:

{{ diagram(src="centrifugal-force.excalidraw.svg") }}

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

{{ diagram(src="rotational-lagrangian-example.excalidraw.svg") }}

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
src="./rolling-without-slipping-lagrangian.excalidraw.svg"
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

Where here, $\mathbf{r} = |\mathbf{r} - \mathbf{r}_\text{mass}|$ where $\mathbf{r}_\text{mass}$ is the position of the mass, which we also call the **central mass**. If this describes the gravitational field generated by a single object far away from all other masses, you may ask, how is this a useful solution? The answer is that if we have a central mass ($M$) that is far greater than some other mass $m$, that is, $m \ll M$, then the smaller mass has almost no gravitational effect on the larger mass. Thus, the larger mass can effectively considered to be stationary and the solution is a good approximation to the gravitational field of the whole system of two masses. From there, we may calculate the _orbit_ $\mathbf{r}(t)$ of the smaller mass around the larger mass (in fact, we will find the exact solution to this problem soon!).

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

Recall that the stationary points (minima/maxima/saddle points) of a potential are **equilibrium points of a system** (review our section at the [start of the guide](#potential-energy-and-conservation-of-energy) about potential landscapes if this is unfamiliar). In the case of central force problems, that means that particles at some stationary point $r_0$ will _orbit_ at a fixed radius $r = r_0$. Depending on the specific form of the central force, these orbits may be stable or unstable (there is [a theorem](https://en.wikipedia.org/wiki/Bertrand%27s_theorem) that states that only central forces with associated potentials in the form $U(r) \sim r^2$ or $U(r) \sim r^{-1}$ are stable). But if $r_0$ also happens to be a _local minimum_, then it is a **stable equilibrium** and thus a **stable orbit**. If an orbiting particle strays slightly from that stable equilibrium, then it will "wiggle" around the stable orbit $r = r_0$, just like a simple harmonic oscillator.

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

## Dynamics of systems of particles

In previous examples, we discussed the motion of a few-body system. But for systems of many bodies, it is helpful to split the problem into two parts: the motion of the **center of mass** of the system, and the motion of each body _with respect_ to the center of mass.

For a system of $N$ interacting particles with masses $m_1, m_2, \dots, m_N$, the position of the center of mass $\mathbf{R}_{CM}$ can be found through:

{% math() %}
\mathbf{R}_{CM} = \dfrac{1}{\sum_{i=1}^N m_i} \sum_{i=1}^N m_i \mathbf{r}_i
{% end %}

This can be written more simply in terms of the _total mass_ of the system, $M_\text{total}$, which we may find through: 

{% math() %}
M_\text{total} = \sum_{i = 1}^N m_i
{% end %}

Thus our expression for the position of the center of mass reduces to:

{% math() %}
\mathbf{R}_{CM} = \dfrac{1}{M_\text{total}}\sum_{i=1}^N m_i \mathbf{r}_i
{% end %}

If we have a _continuous mass density_ described by a mass density function $\rho(\mathbf{r})$, the equivalent formulas are:

{% math() %}
\begin{align*}
M_\text{total} = \int \rho dV \\
\mathbf{R}_{CM} = \dfrac{1}{M_\text{total}}\int \rho\, \mathbf{r}\, dV
\end{align*}
{% end %}

The total **linear momentum** of the system of $N$ (discrete, not continous) masses is given by:

{% math() %}
\mathbf{P}_\text{total} = \sum_{i = 1}^N \mathbf{p}_i = \sum_{i = 1}^N m_i\mathbf{v}_i
{% end %}

Where $\mathbf{p}_i$ is the momentum associated with each of the individual particles. A system of particles obeys the **conservation of total momentum** if no external force is applied on the entire system. That is, we have:

{% math() %}
\dfrac{d\mathbf{P}_\text{total}}{dt} = 0
{% end %}

The *velocity* of the center of mass is given by:

{% math() %}
\mathbf{v}_{CM} =\dfrac{d\mathbf{R}_{CM}}{dt} = \dfrac{1}{M_\text{total}} \underbrace{\sum_{i = 1}^N m_i \mathbf{v}_i}_{ \mathbf{P}_\text{total}} =\dfrac{\mathbf{P}_\text{total}}{M_\text{total}}
{% end %}

The system of particles can also possess _angular momentum_ if the system is rotating (for instance, individual stars moving within a stellar cluster, which itself rotates about the galactic plane). The **total angular momentum** of the system can be written as:

{% math() %}
\mathbf{L}_\text{total} = \underbrace{\mathbf{R}_{CM} \times \mathbf{P}_\text{total}}_\text{angular momentum of CoM} + \underbrace{\sum_{i = 1}^N \mathbf{r}_i \times \mathbf{p}_i}_\text{angular momenta of particles}
{% end %}

Note that here, $\text{CoM}$ is an abbreviation for "center of mass". To simplify the problem, it is easier to choose a special coordinate system known as the **center of mass frame** with the coordinate transformations:

{% math() %}
\begin{align*}
\mathbf{r}_i' &= \mathbf{R}_{CM} + \mathbf{r}_i \\
\dot{\mathbf{r}}_i' &= \mathbf{v}_{CM} + \dot{\mathbf{r}}_i \\
\mathbf{p}_i' &= m_i \dot{\mathbf{r}}_i' = m_i(\mathbf{v}_{CM} + \dot{\mathbf{r}}_i)
\end{align*}
{% end %}

Which allows us to write the total angular momentum of the system in a much-simplified form:

{% math() %}
\mathbf{L}_\text{total} = \sum_{i = 1}^N \mathbf{r}_i' \times \mathbf{p}_i'
{% end %}

This form is also useful because expressing the conservation of angular momentum, that is, $\dfrac{d \mathbf{L}_\text{total}}{dt} = 0$, becomes much easier. This is because while the inter-particle interactions may not conserve angular momentum, the _system_ as a whole does indeed conserve angular momentum.

Now, recall that we saw earlier that the total angular momentum of an $N$-body system can be found from:

{% math() %}
\mathbf{L}_\text{total} = \mathbf{R}_{CM} \times \mathbf{P}_\text{total} + \sum_{i = 1}^N \mathbf{r}_i \times \mathbf{p}_i
{% end %}

If we differentiate this result, we have:

{% math() %}
\begin{align*}
\dfrac{d\mathbf{L}_\text{total}}{dt} &= \mathbf{R}_{CM} \times \dfrac{d\mathbf{P}_\text{total}}{dt} + \sum_{i = 1}^N \mathbf{r}_i \times \dfrac{d\mathbf{p}_i}{dt} \\
&= \underbrace{\mathbf{R}_{CM} \times \mathbf{F}_\text{ext.}}_\text{net torque} + \sum_{i = 1}^N \mathbf{r}_i \times \dfrac{d\mathbf{p}_i}{dt} \\
&= \tau_\text{net} + \sum_{i = 1}^N \left(\mathbf{r}_i \times \dfrac{d\mathbf{p}_i}{dt}\right) \\
&= \tau_\text{net} + \sum_{i = 1}^N \left(\mathbf{r}_i \times \mathbf{F}_i\right)
\end{align*}
{% end %}

This is because the rate of change of the system's total momentum is equal to the _external forces_ on the system (we know this from Newton's second law $\mathbf{F} = \dfrac{d\mathbf{p}}{dt}$), and thus we have {% inlmath() %}\dfrac{d\mathbf{P}_\text{total}}{dt}{% end %}, and the cross product of position and force is the torque. Meanwhile, the rate of the change of each _particle_'s momentum {% inlmath() %}\dot{\mathbf{p}}_i{% end %} is equal to the force {% inlmath() %}\mathbf{F}_i{% end %} experienced by the particle, which comes from the inter-particle interactions _within_ the system. But if the inter-particle forces in the system are _only_ dependent on the separation vector {% inlmath() %}\mathbf{r}_{ij}{% end %} between any two particles $i, j$, that is, {% inlmath() %}\mathbf{F}_{ij} = \mathbf{F}(\mathbf{r}_{ij}){% end %}, then {% inlmath() %}\mathbf{F}_{ij} = -\mathbf{F}_{ji}{% end %}, so the inter-particle forces cancel _as a whole_, meaning the second term vanishes in the expression of the total angular momentum of the system. Thus we have:

{% math() %}
\dfrac{d\mathbf{L}_\text{total}}{dt} = \tau_\text{net}
{% end %}

 We can also examine other characteristics of an $N$-body system. For instance, the total kinetic energy of the system is given by:

{% math() %}
K = \dfrac{1}{2} m_\text{total} \mathbf{v}_{CM}^2 + \dfrac{1}{2} \sum_{i = 1}^N m_i \mathbf{v}_i^2
{% end %}

Where {% inlmath() %}\mathbf{v}_i{% end %} is the velocity of a particle with respect to the center-of-mass frame and {% inlmath() %}\mathbf{v}_{CM}{% end %} is the velocity of the center-of-mass frame. We may also define the total _potential energy_ as:

{% math() %}
U = \underbrace{\sum_i U_{i,\ \text{ext.}}}_\text{external forces} + \underbrace{\sum_{i < j} U_{ij}}_\text{inter-particle forces}
{% end %}

The first term in the potential describes the potential arising from the _external forces_ acting on the system. The second term, meanwhile, describes the potential arising from the _internal inter-particle forces_ within the system. Thus, we may write the total force on the system as:

{% math() %}
\mathbf{F} = -\sum_i\nabla U_i - \sum_{i < j}\nabla U_{ij}
{% end %}

## Collisions and scattering

From our discussion of many-body systems, it is natural to ask how particles interact when they collide with each other, as is bound to happen when we have a many-body system of particles held together by attractive forces (such as gravity). Thankfully, collisions satisfy the **conservation of momentum**. Let us see why. By Newton's third law, when two particles collide, the contact force of the first particle against the second must be equal and opposite to the contract force of the second particle against the first. That is, we have:

{% math() %}
\mathbf{F}_{12} = -\mathbf{F}_{21}
{% end %}

Recalling that force is the time derivative of momentum, we thus have:

{% math() %}
\dfrac{d\mathbf{p}_2}{dt} = -\dfrac{d\mathbf{p}_1}{dt}
{% end %}

We can integrate both sides to get:

{% math() %}
\mathbf{p}_2 = -\mathbf{p}_1
{% end %}

But let us now consider a frame where we observe the collision between the two particles. The total momentum within the frame would then be the sum of the momenta of the two particles:

{% math() %}
\begin{align*}
\mathbf{p}_\text{total} &= \mathbf{p}_1 + \mathbf{p}_2 \\
&= \underbrace{\mathbf{p}_1 + (-\mathbf{p}_1)}_{\text{from }  \mathbf{p}_2 = -\mathbf{p}_1} \\
&= 0
\end{align*}
{% end %}

So indeed, we find that momentum is conserved for two colliding particles. The same is true for any number of colliding particles, but for simplicity, we will only consider the two-particle case here, rather than the more general $N$-body case.

### Analysis of elastic and inelastic collisions

In general, two-particle collisions can be classified as either **elastic** or **inelastic**. The names give a hint as to what they refer to: when we have an elastic collision, the two particles "bounce off" each other after colliding, while when we have a (perfectly) inelastic collision, the two particles "stick together" afterwards. Perfectly elastic collisions are very, very rare in nature, as they essentially require both colliding objects to be 100% imprenetrable or with zero volume; thus (roughly speaking) only collisions between subatomic particles are truly perfectly elastic. What about inelastic collisions? "Inelastic" means that the two colliding objects will be deformed in some way, radiating energy in the form of light, heat, and/or sound. Any collision between two macroscopic objects is bound to be inelastic, which is why kicking a soccer ball makes a (pretty obvious!) sound and why the collisions between tectonic plates in the Earth's crust causes earthquakes. But macroscopic collisions can fall into a wide range between *perfectly* elastic and *perfectly* inelastic - thus, it is possible to *model* some collisions as perfectly elastic (a good approximation when we have near-rigid objects) and model some other collisions as perfectly inelastic (a good approximation when we don't).

Elastic collisions are characterized by the fact that they _leave no trace_ of the collision. There is no sound, no heat, no light, no indication after the collision that the collision occured _at all_. This means they **perfectly conserve energy**. By contrast, inelastic collisions can leave plenty of traces of the collision, including things we typically associate with colliding objects - a loud "bang", a burst of light, and so forth. All of these come from energy that cascades away when the collision occurs, so inelastic collisions **do not conserve energy**.

Let us first consider an _elastic collision_ between two objects of masses $m_1, m_2$, whose initial velocities are $\mathbf{v}_1, \mathbf{v}_2$, and whose post-collision velocities (which we want to solve for) are $\mathbf{v}_1', \mathbf{v}_2'$. By the conservation of energy, we have $K_1 + K_2 = K_1' + K_2'$, and therefore:

{% math() %}
\dfrac{1}{2} m_1 \mathbf{v}_1^2 + \dfrac{1}{2} m_2 \mathbf{v}_2^2 = \dfrac{1}{2} m_1 \mathbf{v}_1'^2 + \dfrac{1}{2} m_2 \mathbf{v}_2'^2
{% end %}

This is rather long and unyieldy equation, so it is helpful to switch to the _center of momentum frame_. First, we write out the _total momentum_ of the system (which is _always_ conserved) as:

{% math() %}
\begin{gather*}
\mathbf{P}_\text{total} = m_1 \mathbf{v}_1 + m_2 \mathbf{v}_2 = M_\text{total} \mathbf{v}_{CM} \\
\Rightarrow \mathbf{v}_{CM} = \dfrac{m_1 \mathbf{v}_1 + m_2 \mathbf{v}_2}{m_1 + m_2}
\end{gather*}
{% end %}

Where {% inlmath() %}\mathbf{v}_{CM}{% end %} is the velocity of the center of momentum frame, and {% inlmath() %}M_\text{total} = m_1 + m_2{% end %}. This allows us to make a transformation to a set of new velocity coordinates {% inlmath() %}\mathbf{v}_1^*, \mathbf{v}_2^*{% end %}, which give the velocities of each of the two objects in the center of momentum frame, given by:

{% math() %}
\begin{align*}
\mathbf{v}_1^* = \mathbf{v}_1 - \mathbf{v}_{CM} \\
\mathbf{v}_2^* = \mathbf{v}_2 - \mathbf{v}_{CM} \\
\end{align*}
{% end %}

By substituting these definitions into our previous equation for the total momentum, we find that:

{% math() %}
\underbrace{m_1 \mathbf{v}_1^* + m_2 \mathbf{v}_2^*}_\text{initial} = \underbrace{m_1 \mathbf{v}_1'^* + m_2 \mathbf{v}_2'^*}_\text{post-collision} =0
{% end %}

Which is a much simpler result, and allows us to also derive the relationships between the sets of velocities:

{% math() %}
\begin{matrix*}
\underbrace{\mathbf{v}_2^* = -\dfrac{m_1}{m_2} \mathbf{v}_1^*}_\text{initial velocities}, &\underbrace{\mathbf{v}_2'^* = -\dfrac{m_1}{m_2} \mathbf{v}_1'^*}_\text{post-collision velocities}
\end{matrix*}
{% end %}

> **Note:** another special property is that the angles of deflection (the angle between {% inlmath() %}\mathbf{v}_1^*, \mathbf{v}_1'^*{% end %}, as well as the angle between {% inlmath() %}\mathbf{v}_2^*, \mathbf{v}_2'^*{% end %}) are the _same_ when measured in the center of momentum frame, which is _not true_ in general within the regular (untransformed) frame.

Now, if we substitute the above relations for {% inlmath() %}\mathbf{v}_2^*{% end %} and {% inlmath() %}\mathbf{v}_2'^*{% end %}, we can write out the conservation of energy equation as:

{% math() %}
\begin{gather*}
\dfrac{1}{2} m_1 {\mathbf{v}_1^*}^2 + \dfrac{1}{2} m_2 {\mathbf{v}_2^*}^2 = \dfrac{1}{2} m_1 {\mathbf{v}_1'^*}^2 + \dfrac{1}{2} {m_2 \mathbf{v}_2'^*}^2 \\
\dfrac{1}{2} m_1 {\mathbf{v}_1^*}^2 + \dfrac{1}{2} m_2 \left(\dfrac{m_1}{m_2}\right)^2 {\mathbf{v}_1^*}^2 = \dfrac{1}{2} m_1 {\mathbf{v}_1'^*}^2 + \dfrac{1}{2} m_2\left(\dfrac{m_1}{m_2}\right)^2 {\mathbf{v}_1'^*}^2 \\
\dfrac{1}{2} \left[m_1 + \left(\dfrac{m_1}{m_2}\right)^2\right] {\mathbf{v}_1^*}^2 = \dfrac{1}{2} \left[m_1 + \left(\dfrac{m_1}{m_2}\right)^2\right] {\mathbf{v}_1'^*}^2 \\
\cancel{\dfrac{1}{2} \left[m_1 + \left(\dfrac{m_1}{m_2}\right)^2\right]} {\mathbf{v}_1^*}^2 = \cancel{\dfrac{1}{2} \left[m_1 + \left(\dfrac{m_1}{m_2}\right)^2\right]} {\mathbf{v}_1'^*}^2 \\
\Rightarrow  {\mathbf{v}_1^*}^2 = {\mathbf{v}_1'^*}^2
\end{gather*}
{% end %}

So we find that {% inlmath() %}|\mathbf{v}_1^*| = |\mathbf{v}_1'^*|{% end %}, which also implies that {% inlmath() %}|\mathbf{v}_2^*| = |\mathbf{v}_2'^*|{% end %}. We would expect this: the conservation of energy would require that this be the case.

We will now examine a classic problem to be able to showcase using the center-of-momentum frame to solve problems. Consider a mass $m_1$ moving at velocity $\mathbf{v}_1$ that collides with another mass $m_2$ that istationary, so $\mathbf{v}_2 = 0$ (this is a classic billiard-ball style situation). The masses are rigid, so we may assume that the collision is close to perfectly elastic. The collision sends the two massses flying in opposite directions; the first mass is deflected by an angle $\psi$, and the second mass is deflected by an angle $\xi$. We show this scenario in the below diagram:

{{ natural_img(
src="elastic-collision-demo.excalidraw.svg"
desc="My description"
) }}

Writing out the conservation of momentum yields the following equation:

{% math() %}
m_1 \mathbf{v}_1 = m_1 \mathbf{v}_1' + m_2 \mathbf{v}_2' = M_\text{total} \dot{\mathbf{R}}
{% end %}

Where $\dot{\mathbf{R}} = \mathbf{v}_{CM}$ is the center-of-mass velocity. If we define $v_1 = |\mathbf{v}_1$ as the _speed_ of the first mass pre-collision, and $v_1' = |\mathbf{v}_1'|$ and $v_2' = |\mathbf{v}_2'|$ as the _speeds_ of the objects, post-collision, then we can write the above in component form as:

{% math() %}
\begin{bmatrix} m_1 v_1 \\ 0 \end{bmatrix} =
\begin{bmatrix} m_1 v_1' \cos \psi \\ m_1 v_1' \sin \psi \end{bmatrix} +
\begin{bmatrix} m_2 v_2' \cos \xi \\ m_2 v_2' \sin \xi \end{bmatrix}
{% end %}

Let us now switch over to the center of momentum frame. We use the transformations:

{% math() %}
\begin{matrix*}
\mathbf{v}_1^* = \mathbf{v}_1 - \dot{\mathbf{R}},
&\mathbf{v}_2^* = \mathbf{v}_2 - \dot{\mathbf{R}} \\
\mathbf{v}_1'^* = \mathbf{v}_1' - \dot{\mathbf{R}}, &\mathbf{v}_2'^* = \mathbf{v}_2' - \dot{\mathbf{R}} \\
\end{matrix*}
{% end %}

Where again, $\dot{\mathbf{R}}$ is the center-of-mass velocity, given by:

{% math() %}
\begin{align*}
\dot{\mathbf{R}} &= \dfrac{m_1 \dot{\mathbf{r}}_1 + \cancel{m_2 \dot{\mathbf{r}}_2}}{m_1 + m_2} \\
&= \dfrac{m_1}{m_1 + m_2} \mathbf{v}_1 \\
&= \dfrac{m_1}{m_1 + m_2} \begin{bmatrix} v_1 \\ 0 \end{bmatrix}
\end{align*}
{% end %}

Now, if we perform our coordinate transformations to our center-of-momentum frame coordinates, where our angle of deflection for both masses would be the transformed angle $\theta$, we have:

{% math() %}
\begin{align*}
v_1^* \cos \theta &= v_1' \cos \psi - \dfrac{m_1}{m_1 + m_2} v_1 \\
\Rightarrow v_1' &\cos \psi = v_1'^* \cos \theta + \dfrac{m_1}{m_1 + m_2} v_1 \\
v_1^* \sin \theta &= v_1' \sin \psi - 0 \\
&= v_1' \sin \psi \\
\dfrac{v_1' \sin \psi}{v_1' \cos \psi} &= \tan \psi \\ &= \dfrac{v_1'^* \sin \theta}{v_1'^* \cos \theta + \frac{m_1 v_1}{m_1 + m_2}}
\end{align*}
{% end %}

But recall that $v_1^* = v_1'^*$, as we derived before from the conservation of energy, and using the coordinate transformation equations and our definition of $\dot{\mathbf{R}}$, we find that:

{% math() %}
\begin{align*}
v_1^* &= v_1 - \dot R_x \\
&= v_1 - \dfrac{m_1}{m_1 + m_2} v_1 \\
&= \dfrac{m_1 + m_2}{m_1 + m_2}v_1 - \dfrac{m_1}{m_1 + m_2} v_1 \\
&= \dfrac{m_2}{m_1 + m_2} v_1
\end{align*}
{% end %}

And since $v_1^* = v_1'^*$, we can substitute this into our expression for $\tan \psi$ to get:

{% math() %}
\begin{align*}
\tan \psi &= \dfrac{v_1'^* \sin \theta}{v_1'^* \cos \theta + \frac{m_1 v_1}{m_1 + m_2}} \\
&= \dfrac{\sin \theta}{\cos \theta + \frac{m_1}{m_1 + m_2}\frac{m_1 + m_2}{m_2}} \\
&= \dfrac{\sin \theta}{\cos \theta + m_1/m_2} \\
\end{align*}
{% end %}

We note that if $m_1 \ll m_2$, then $\tan \psi \approx \tan \theta$ and $\psi \approx \theta$. Meanwhile, if $m_1 = m_2$, then $\tan \psi = \dfrac{\sin \theta}{\cos \theta + 1} = \tan \left(\dfrac{\theta}{2}\right)$. We will not do the derivations but we note that in the case $m_1 = m_2$, we additionally have $\tan \xi = \tan \left(\dfrac{\pi}{2} - \dfrac{\theta}{2}\right)$ and therefore we have $\xi = \dfrac{\pi}{2} - \psi$. And we can now see the significance of center-of-momentum frames: while the math to solve this problem was intense, it would have been much, much harder had we not used a center-of momentum frame to solve the problem.

### Scattering problems

Using the conservation of momentum, we can solve for collisions between two (or perhaps three or four) particles - anything beyond that is intractable. But what if we have a large number of particles, all of them colliding at some surface? That is to say, if we were to shoot a number of particles on some surface, what would be the distribution of the particle impacts on the surface (if the collision is inelastic) or where would the particles be deflected (if the collision is elastic)? This is the problem known as **scattering**.

{{ diagram(
src="https://upload.wikimedia.org/wikipedia/commons/d/dc/Differential_cross_section.svg"
desc="An illustration of scattering. A particle incident on some object at a height b above the collision axis incident on cross-sectional area sigma is deflected at solid angle d omega."
) }}

_Source: [Wikipedia](https://en.wikipedia.org/wiki/File:Differential_cross_section.svg)_

To describe scattering, we begin by defining the collision object (that the particle(s) hit and scatter off of), and draw an axis through its center - we refer to this axis as the **centerline** or **collision axis**. The particle(s)' distance _above_ the centerline is known as the **impact parameter**, which we denote as $b$. If the particle does indeed deflect, then the angle at which it deflects is called the **scattering angle**, and is denoted by $\theta$.

Now, to analyze scattering, we use something called the _scattering cross-section_. This describes the ratio of $d\sigma$, an infinitesimal cross-sectional area the particle(s) pass through, to $d\Omega$, an infinitesimal scattering angle (the $\Omega$ is due to the fact that the angle is called a **solid angle**). Using the notation in Griffiths, _Introduction to Elementary Particles_, the scattering cross-section $D(\theta)$ is therefore defined as:

{% math() %}
\begin{matrix*}
D(\theta) = \dfrac{d\sigma}{d\Omega}, &d\sigma = |b\,db\, d\phi|, & d\Omega = |\sin \theta\, d\theta\, d\phi|
\end{matrix*}
{% end %}

> **Note:** Funnily enough, while it _looks_ like a derivative, the scattering cross-section $\dfrac{d\sigma}{d\Omega}$ is not a derivative at all! It is truly just a fraction (albeit between two infinitesimal quantities), so we manipulate it like a fraction, no calculus or limit trickery needed.

Thus, by some rearrangement of $D(\theta)$ we find that we may also express the scattering cross-section as:

{% math() %}
\dfrac{d\sigma}{d\Omega} = \left|\dfrac{b}{\sin \theta} \left(\dfrac{db}{d\theta}\right)\right|
{% end %}

To find the *total* cross-section from the differential cross-section, we integrate over the total solid angle:

{% math() %}
\begin{align*}
\sigma_t &= \int \dfrac{d\sigma}{d\Omega} d\Omega \\
&= \int_0^{2\pi} \int_0^\pi \dfrac{d\sigma}{d\Omega} \sin \theta d\theta d\phi \\
&= \int_0^{2\pi} \int_0^\pi D(\theta) \sin \theta d\theta d\phi
\end{align*}
{% end %}

The scattering cross-section has rather unusual units: it is expressed in terms of $\pu{m^2/sr}$, that is, _meters squared over steradians_ (steradians are the standard unit for solid angle and are very similar to radians for regular angles). However, since steradians are dimensionless, the scattering cross-section can equivalently just be expressed in units of $\pu{m^2}$. In (quantum) particle physics, it is common to use the (funnily-named) unit of the _barn_ ($\pu{b}$), where $\pu{1b} = \pu{100 fm^2} = \pu{10^{-28} m^2}$. But for classical physics, we can just use regular meters and centimeters.

### Scattering over a hard sphere

Let us consider a particle (or stream of particles) bouncing off a hard sphere of radius $R$ (this problem is also in Griffiths, _Introduction to Elementary Particles_, example 6.1). By "hard", we mean a completely rigid, impenetrable sphere, which is of course impossible in reality, so this is an idealization. For this problem, it is always helpful to draw a diagram, so we show one below:

{{ wideimg(
src="./hard-sphere-scattering.excalidraw.svg"
desc="A diagram showing a particle of height b passing through cross-section d sigma that hits a solid impenetrable sphere and is deflected at angle theta (measured from the +x axis). The scattering solid angle is d Omega."
) }}

Recall that $\dfrac{d\sigma}{d\Omega} = \left|\dfrac{b}{\sin \theta} \left(\dfrac{db}{d\theta}\right)\right|$ is the general result that we found before (one that generalizes to other problems, it is not just true for this particular problem). Unfortunately, to be able to compute the formula explicitly, we need to know $b(\theta)$. This is where our diagram comes in. By defining the angle $\phi$ for which $\theta = \pi - 2\phi$, we have:

{% math() %}
\begin{gather*}
\sin \phi = \dfrac{b}{R} \Rightarrow b = R \sin \phi \\
\theta = \pi - 2\phi \Rightarrow \phi = \dfrac{\pi}{2} - \dfrac{\theta}{2} \\
b = R \sin \phi = R \sin \left(\dfrac{\pi}{2} - \dfrac{\theta}{2}\right)
\end{gather*}
{% end %}

Using the result that $\cos \alpha = \sin \left(\dfrac{\pi}{2} - \alpha \right)$ we have:

{% math() %}
\begin{align*}
b &= R \cos \left(\dfrac{\theta}{2}\right) \\
b'(\theta) &= -\dfrac{R}{2} \sin \left(\dfrac{\theta}{2}\right) \\
|b'(\theta)| &= \dfrac{R}{2} \sin \left(\dfrac{\theta}{2}\right)
\end{align*}
{% end %}

So our differential cross section would be:

{% math() %}
\dfrac{d\sigma}{d\Omega} = \left|\dfrac{b}{\sin \theta} \left(\dfrac{db}{d\theta}\right)\right| = \dfrac{1}{\sin \theta} R \cos \left(\dfrac{\theta}{2}\right) \dfrac{R}{2} \sin \left(\dfrac{\theta}{2}\right) = \dfrac{R^2}{2} \dfrac{\sin(2\theta/2)}{2 \sin \theta} = \dfrac{R^2}{4}
{% end %}

Where here we used the identity that $\sin \beta \cos \beta = \dfrac{1}{2} \sin(2\beta)$. Thus, we have solved the problem of scattering over a hard sphere, and we have found that the distribution of the scattered particle(s) in terms of cross-sectional area per solid angle is $\dfrac{d\sigma}{d\Omega} = \dfrac{R^2}{4}$.

> **Note:** This scattering problem may seem like it is for a very specific case. However, hard-sphere scattering is in fact more general, because it also models any scattering off any spherically-symmetric potential barrier $V_0$ that a classical particle with energy $E < V_0$ cannot pass through.

### Scattering over a force field

Scattering does not necessarily have to involve two objects hitting each other. A particle (or set of particles) could just as easily scatter off a central force field, such as an electrostatic field, in which it doesn't "hit" anything, but its direction and speed still changes. For instance, in spacecraft navigation (especially NASA space probes heading into deep space), it is common for a spacecraft to receive a _gravity assist_ from a planet (usually Jupiter). This means it essentially scatters off the gravitational field of the planet, which gives it a big velocity boost, necessary to overcome the strong gravitational pull of the Sun and travel into the furthest reaches of the Solar System (and beyond!).

In the case of a particle of mass $m$ (such as a small spacecraft) scattering over the gravitational planet caused by a much larger mass $M$ (such as a planet), we use essentially the same approach, just with some more sophisticated mathematics. The derivation is a bit difficult, but the essentials are the same. We once again define an angle $\phi$ for which $\theta = \pi - 2\phi$, where $\phi$ is given by:

{% math() %}
\phi(r) = -\int_{r_0}^{r_\text{min}} \dfrac{\ell}{r^2} \dfrac{dr}{\sqrt{2\mu(E - U(r)- \ell^2/2\mu r^2)}}
{% end %}

Where $U(r) = -\dfrac{GMm}{r}$ is the gravitational potential energy of the particle, $\mu = \dfrac{mM}{m+M}$ is the reduced mass of the two-body system, where $r_0$ is the distance from the center of the solid sphere that the particle starts off at $t  = 0$, and $r_\text{min}$ is the _point of closest approach_. Remember that since the particle is scattering off a gravitational field, there is no solid object that the particle actually "bounces off" of; rather, the particle approaches from some distance $r_0$ until it reaches the closest point $r = r_\text{min}$, before it is deflected away and goes the opposite direction. We can often get away by setting $r_0 = \infty$, meaning that the particle approaches from sufficiently far away that it can be considered to initially infinitely distant. From here, we "just" need to compute the integral, and then use $\dfrac{d\sigma}{d\Omega} = \left|\dfrac{b}{\sin \theta} \left(\dfrac{db}{d\theta}\right)\right|$ to find the differential cross-section.

> **Note:** This expression is more general than just for gravitational fields; in fact, it applies for _any_ central force field with potential $U = U(r)$, so it equally applies for harmonic potentials and electrostatic force fields!

### Non-inertial reference frames

We have seen in our study of moving reference frames that due to the constraints in a rotating coordinate system, fictitious "forces" arise when attempting to apply Newton's second law $\mathbf{F} = m \mathbf{a}$. While these are not real forces, they can be _mathematically treated_ as parts of an **effective force** to allow us to treat the problem in the same way as we would treat a problem that used a stationary (inertial) reference frame. In a rotating frame, the effective force $\mathbf{F}_\text{eff.}$ experienced by an observer is given by:

{% math() %}
\mathbf{F}_\text{eff.} = \underbrace{\mathbf{F}_\text{fixed} - m \ddot{\mathbf{R}}_F}_\text{inertial terms} - \underbrace{m \vec{\dot \omega} \times \mathbf{r}  - m \vec \omega \times(\vec \omega \times \mathbf{r}) - 2m\vec \omega \times \mathbf{v}_r}_\text{non-inertial terms}
{% end %}

Where {% inlmath() %}\mathbf{F}_\text{fixed}{% end %} describes all physical (real) forces in the _fixed reference frame_, {% inlmath() %}m \ddot{\mathbf{R}}_F{% end %} describes the acceleration due to translation of the rotating system, {% inlmath() %}m \vec{\dot \omega} \times \mathbf{r}{% end %} describes the angular acceleration, {% inlmath() %}m \vec \omega \times(\vec \omega \times \mathbf{r}){% end %} is the acceleration due to the centrifugal "force", and {% inlmath() %}2m\vec \omega \times \mathbf{v}_r{% end %} is due to the Coriolis force. Note that all terms after {% inlmath() %}\mathbf{F}_\text{fixed} - m\ddot{\mathbf{R}}_F{% end %} are terms unique to the non-inertial frame; these _non-inertial terms_ come as a result of the coordinate system. The only _real_ forces (e.g. gravity, electric force, etc.) are contained within {% inlmath() %}\mathbf{F}_\text{fixed}{% end %}; all other "force" terms arise due to the motion (translational and rotational) of the rotating frame and should be considered as **fictitious forces**.

To solve for the equations of motion, we must set {% inlmath() %}\mathbf{F}_\text{eff.} = m\mathbf{a}_r{% end %}, where we solve for {% inlmath() %}\mathbf{a}_r{% end %}, the effective force on some moving body inside the rotating reference frame. Consider, for instance, a fixed reference frame located at the center of the Earth. We are interested in what is happening within a reference frame at the Earth's surface. The surface reference frame rotates as the Earth rotates, so it is a _rotating reference frame_. We want to describe the motion of an object on the Earth's surface (which means that it is in our surface reference frame) by finding the equations of motion.

To be able to solve for the equations of motion, we begin by isolating the forces in the fixed frame. The forces in the fixed frame are:

{% math() %}
\mathbf{F}_\text{fixed} = m\ddot{\mathbf{R}}_F = \mathbf{S} + m\mathbf{g}_0
{% end %}

Where $\mathbf{g}_0 = -\dfrac{GM}{r^2} \hat r$ and $\mathbf{S}$ includes all other physical forces (e.g. geothermal pressure). These are forces that _do not arise_ as a result of the rotating coordinate system, hence why we say that they are _physical_ forces, rather than fictitious forces that are the result of a rotating reference frame.

Let us now consider the terms that *are* dependent on the rotating coordinate system. First, the Earth's rotation has an approximately constant angular velocity, which we may denote $\omega_0$, such that:

{% math() %}
\vec \omega = \omega_0 \hat z
{% end %}

We have:

{% math() %}
\ddot{\mathbf{R}}_F = \vec \omega \times (\vec \omega \times \mathbf{R}_F)
{% end %}

Such that the effective force takes the form:

{% math() %}
\begin{align*}
\mathbf{F}_\text{eff} &= \mathbf{F}_\text{fixed} - m\ddot{\mathbf{R}}_F - m \vec \omega \times(\vec \omega \times \mathbf{r}) - 2m\vec \omega \times \mathbf{v}_r \\
&= \mathbf{S} + m\mathbf{g}_0 - m\vec \omega \times (\vec \omega \times (\mathbf{R} + \mathbf{r})) - 2m\vec \omega \times \mathbf{v}_r
\end{align*}
{% end %}

We note that the gravitational acceleration interestingly does not point _directly_ towards the center of the Earth. This is because of the contribution of the centrifugal "force", which _modifies_ the direction of the gravitational acceleration away from the direction of the gravitational field $\mathbf{g}_0$. Thus, it is convenient to define the _effective_ gravitational acceleration as measured on the Earth's surface, given by:

{% math() %}
\mathbf{g} = \mathbf{g}_0 - \vec \omega \times (\vec \omega \times (\mathbf{R} + \mathbf{r}))
{% end %}

> **Note:** In general, $\mathbf{g} - \mathbf{g}_0 \approx \pu{0.034 m/s}$ (while the precise value depends on your latitude, this is the approximate maximum value). This discrepancy is the contribution due to centrifugal effects (what we call the centrifugal "force").

Using the effective gravitational acceleration, we can rewrite our expression for the effective force as:

{% math() %}
\mathbf{F}_\text{eff.} = \mathbf{S} + m\mathbf{g} - \underbrace{2m \vec \omega \times \mathbf{v}_r}_\text{coriolis "force"}
{% end %}

Let us now consider the case of a particle falling to Earth's surface from some height $h$. We will use $z$ as our radial coordinate, $x$ as the horizontal coordinate, and $\theta$ as the angle made with respect to the center of the Earth, as we show in the below diagram:

{{ diagram(
src="coriolis-earth.excalidraw.svg"
desc="A diagram of the problem's coordinate system, showing z as the distance above earth's surface, theta as the angle with respect to the center of the earth, and y as the direction tangent to the Earth's surface"
) }}

The angular velocity of the Earth about its rotational axis is given by:

{% math() %}
\vec \omega = -\omega_0 \cos \theta \hat x + \omega_0 \sin \theta \hat z
{% end %}

From here, substituting our result for the effective force on the surface of the Earth, we find that:

{% math() %}
\begin{align*}
\mathbf{F}_\text{eff.} &= m \mathbf{g} - 2m \vec \omega \times \vec{\mathbf{v}}_r \\
m\mathbf{a}_r &= m \mathbf{g} - 2m \vec \omega \times \vec{\mathbf{v}}_r \\
\mathbf{a}_r &= \mathbf{g} - 2\vec \omega \times \vec{\mathbf{v}}_r \\
\end{align*}
{% end %}

The velocity $\mathbf{v}_r$ is given, in this configuration by:

{% math() %}
\mathbf{v}_r = \begin{pmatrix} 0 \\ 0 \\ -gt \end{pmatrix}
{% end %}

From which we can calculate the cross product of the angular velocity vector with:

{% math() %}
\begin{align*}
\vec \omega \times \mathbf{v}_r &= \begin{vmatrix}
 \hat x & \hat y & \hat z \\
 -\omega_0 \cos \theta & 0 & \omega_0 \sin \theta \\
 0 & 0 & -gt
\end{vmatrix} \\
&= -g \omega_0 t \cos \theta \hat y
\end{align*}
{% end %}

Thus, expanding out $\mathbf{a}_r = \mathbf{g} - 2\vec \omega \times \vec{\mathbf{v}}_r$ in vector form, we have:

{% math() %}
\mathbf{a}_r =
\begin{pmatrix}
a_{rx} \\
a_{ry} \\
a_{rz}
\end{pmatrix} =
\begin{pmatrix}
\ddot x_r \\
\ddot y_r \\
\ddot z_r
\end{pmatrix}
=
\begin{pmatrix}
0 \\
2g\omega t \cos \theta \\
-g
\end{pmatrix}
{% end %}

These can be solved as a system of 2nd-order differential equations, with the initial conditions $\mathbf{r}(0) = \langle 0, 0, h\rangle$, $\mathbf{r}'(0) = 0$ to yield the solutions:

{% math() %}
\begin{align*}
x(t) &= 0 \\
y(t) &= \dfrac{1}{3} \omega_0 g t^3 \cos \theta \\
z(t) &= h - \dfrac{1}{2} gt^2
\end{align*}
{% end %}

Thus, the amount of deflection from a straight-line path caused by the Coriolis "force" is given by:

{% math() %}
\Delta y = \dfrac{1}{3} \omega_0 g \left(\dfrac{2h}{g}\right)^{3/2}\cos \theta
{% end %}

## Dynamics of rigid bodies

It is common to consider purely point-like particles in physics, and up to this point, we have had considered objects to be located at a definite location. However, we know that _real_ (macroscopic) objects have internal volume and size, so point particles are only an approximation to describe them. A better description uses the model of a **rigid body**, which more accurately accounts for the internal volume and nonzero size of real objects.

Rigid bodies can be thought of as a system of $n$ particles of masses $m_1, m_2, m_3, \dots$ which allows them to be modelled as such a system. Each particle would then have velocity $\mathbf{v}_i$, given by:

{% math() %}
\mathbf{v}_i = \mathbf{v}_{CM} + \vec \omega \times \mathbf{r}_i
{% end %}

where as with before, $\mathbf{v}_{CM}$ is the velocity of the center-of-mass of the system, and $\omega \times \mathbf{r}_i$ describe the particle's velocity about the center-of-mass (equivalently, the rate of rotation of the particle with respect to the rotating reference frame):

{% math() %}
\underbrace{\mathbf{r}_i = \begin{pmatrix} x_i \\ y_i \\ z_i \end{pmatrix},}_{\text{position of particle } i} \quad
\underbrace{\vec \omega = \begin{pmatrix}
\omega_x \\ \omega_y \\ \omega_z
\end{pmatrix}}_\text{angular velocity of particle w.r.t CoM}
{% end %}

For a rigid body, the distance of every point on its surface from the center of mass will remain constant in time as we assume the object cannot stretch or shrink. Rigid bodies can be analyzed by positioning our coordinate system such that the origin of our coordinate system is exactly positioned at the center of Earth's.

Let us consider the total kinetic energy of a rigid body. Using our definition of $\mathbf{v}_i$, we have:

{% math() %}
\begin{align*}
K_\text{total} &= \sum \dfrac{1}{2} m_i \mathbf{v}_i^2 \\
&= \dfrac{1}{2} \sum_i m_i (\mathbf{v}_{CM} + \vec \omega \times \mathbf{r}_i)^2 \\
&= \dfrac{1}{2} \sum_i m_i (\mathbf{v}_{CM}^2 + 2 \mathbf{v}_{CM}\cdot (\vec \omega \times \mathbf{r}) + (\vec \omega + \mathbf{r}_i)^2) \\
&= \underbrace{\dfrac{1}{2} \sum_i m_i \mathbf{v}_{CM}^2}_\text{translational KE} + \underbrace{\dfrac{1}{2} \sum_i m_i (\vec \omega \times \mathbf{r}_i)^2}_\text{rotational KE}
\end{align*}
{% end %}

Where we note that the total kinetic energy $K_\text{total} = K_\text{transl.} + K_\text{rot.}$ which is the sum of the translational and rotational kinetic energies. Note that if we use the identity $(\mathbf{A} \times \mathbf{B})^2 = \mathbf{A}^2 \mathbf{B}^2 - (\mathbf{A} \cdot \mathbf{B})^2$, we can rewrite the above expression as:

{% math() %}
\begin{align*}
K_\text{rot.} &= \dfrac{1}{2} \sum_i m_i (\vec \omega \times \mathbf{r}_i)^2 \\
&= \dfrac{1}{2} \sum_i m_i \left[\omega^2 \mathbf{r}_i^2 - (\vec \omega \cdot \mathbf{r}_i)^2\right]
\end{align*}
{% end %}

Where here, $\omega^2 = \vec \omega \cdot \vec \omega$ and {% inlmath() %}\mathbf{r}_i^2 = \mathbf{r}_i \cdot \mathbf{r}_i{% end %}. But the angular velocity is a _vector_ (technically, pseudovector, but that distinction can be ignored here), which can be written in tensor form as {% inlmath() %}\omega_j = \sum_{k=1}^3 \omega_k \delta_{jk}{% end %}, where {% inlmath() %}\delta_{jk}{% end %} is the identity matrix, given by:

{% math() %}
\delta_{ij} = \begin{pmatrix*}
\delta_{11} & \delta_{12} & \delta_{13} \\
\delta_{21} & \delta_{22} & \delta_{23} \\
\delta_{31} & \delta_{32} & \delta_{33}
\end{pmatrix*} =\begin{pmatrix*}
1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1
\end{pmatrix*}
{% end %}

If this tensor notation is unfamiliar, the idea is that when we want to compute the $j$-th component of the angular velocity (for instance, $\omega_1$, the $x$-component of $\vec \omega$), we substitute in $j = x$ and plug that into the sum, which gives:

{% math() %}
\begin{align*}
\omega_1 &= \sum_{k=1}^3 \omega_k \delta_{1k} \\
&= \omega_1 \delta_{11} + \omega_2{\delta}_{12} + \omega_3 \delta_{13} \\
&= \omega_1 (1) + 0 + 0 \\
&= \omega_1
\end{align*}
{% end %}

Similarly, notice that the position of each particle, which we referred to as {% inlmath() %}\mathbf{r}_i{% end %}, may be written as {% inlmath() %}r_b = \sum_{a = 1}^3 r_a^{(i)}\delta_{ab}{% end %}, such that {% inlmath() %}\mathbf{r}_i \cdot \mathbf{r}_i{% end %} becomes:

{% math() %}
\begin{align*}
\mathbf{r}_i \cdot \mathbf{r}_i &= r_b\, r_b \\
&= \sum_{a = 1}^3 r_a^{(i)}\delta_{ab} \sum_{a = 1}^3 r_a^{(i)}\delta_{ab} \\
&= \sum_{a = 1}^3 {r_a^{(i)}}^2
\end{align*}
{% end %}

Since $\delta_{ab} \delta_{ab} = \delta_{ab}$ (the matrix product of the identity matrix with an identity matrix is still an identity matrix) - note that this is true for the identity matrix regardless of which indices you use, so we find that:

{% math() %}
\begin{align*}
\omega^2 &= \vec \omega \cdot \vec \omega \\
&= \omega_j \,\omega_j \\
&= \sum_{k=1}^3 \omega_k \delta_{jk} \sum_{k=1}^3 \omega_k \delta_{jk} \\
&= \sum_{k=1}^3 \omega_k^2 \cancel{\delta_{jk} \delta_{jk}}^1 \\
&= \sum_{k=1}^3 \omega_k^2
\end{align*}
{% end %}

On substituting our new definitions for $\omega^2$ and $\mathbf{r}_i^2$, we have:

{% math() %}
\begin{align*}
K_\text{rot.} &= \dfrac{1}{2} \sum_i m_i \left[\omega^2 \mathbf{r}_i^2 - (\vec \omega \cdot \mathbf{r}_i)^2\right] \\
&=\dfrac{1}{2} \sum_i m_i \left[\left(\sum_{k=1}^3 \omega_k^2\right)^2 \left(\sum_{a = 1}^3 {r_a^{(i)}}^2\right) - \left(\sum_{a = 1}^3 r_a^{(i)}\omega_a\right)\left(\sum_{k = 1}^3 r_k^{(i)}\omega_k\right)\right] \\
&= \dfrac{1}{2} \sum_i m_i \sum_{a= 1}^3 \sum_{k = 1}^3\left[\omega_a \omega_k \delta_{ak} \sum_{a=1}^3 {r_a^{(i)}}^2 - \omega_a \omega_k r_a^{(i)} r_k^{(i)}\right] \\
&= \dfrac{1}{2} \sum_{a= 1}^3 \sum_{k = 1}^3 \omega_a \omega_k\underbrace{\sum_i m_i \left[\left(\delta_{ak} \sum_{a=1}^3 {r_a^{(i)}}^2\right) - r_a^{(i)} r_k^{(i)}\right]}_{I_{ak}} \\
&= \sum_{a= 1}^3 \sum_{k = 1}^3 \dfrac{1}{2} I_{ak} \omega_a \omega_k
\end{align*}
{% end %}

Note how in the second-last line, we defined a special matrix $I_{ak}$, given by:

{% math() %}
I_{ak} = \sum_i m_i \left[\left(\delta_{ak} \sum_{a=1}^3 {r_a^{(i)}}^2\right) - r_a^{(i)} r_k^{(i)}\right]
{% end %}

This is the **moment of inertia** in its _most general form_, called the _moment of inertia tensor_, or just **inertia tensor** for short. In 3D, it is written as a $(3 \times 3)$ matrix. Note that along the diagonals of the inertia tensor, since $\delta_{ak} = 1$ when $a = k$, we have:

{% math() %}
I_{aa} = \sum_i m_i \left[\left(x_a^{{(i)}^2} + y_a^{{(i)}^2} + z_a^{{(i)}^2}\right) - \left(r_a^{(i)}\right)^2\right]
{% end %}

Where $r_a = (r_1, r_2, r_3) = (x, y, z)$ is the tensor expression for the $a$-th component of the position, and $r_a^{(i)} = (r_1^{(i)}, r_2^{(i)}, r_3^{(i)}) = (x^{(i)}, y^{(i)}, z^{(i)})$ is the position of the $i$-th particle. Meanwhile, for the non-diagonals (cross terms) of the inertia tensor, since $\delta_{ak} = 0$ when $a \neq k$, we have:

{% math() %}
I_{{ak},\, \text{cross}} = -\sum_i m_i r_a^{(i)} r_k^{(i)}
{% end %}

We notice that in the limiting case, as the number of particles grows very large, this expression reduces to the familiar expression of the rotational kinetic energy:

{% math() %}
K = \dfrac{1}{2} I \omega^2
{% end %}

> **Note:** The inertia tensor $I_{ak}$ is the collective description of the moment of inertia of a _system_ of $N$ particles, where $N$ can be arbitrarily-large. This means that in our definition of the inertia tensor $I_{ak} = \displaystyle \left[\sum_i m_i \left(\delta_{ak} \sum_{a=1}^3 {r_a^{(i)}}^2 \right) - r_a^{(i)} r_k^{(i)}\right]$, we must remember to sum over every particle; that is, the index $i$ sums from the first particle to the last ($N$-th) particle.