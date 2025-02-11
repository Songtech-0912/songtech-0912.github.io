+++
title = "Advanced Classical Mechanics"
date = 2025-01-26
draft = false
+++

This is a guide to classical mechanics beyond Newtonian mechanics. Topics discussed include Lagrangian mechanics, Hamiltonian mechanics, Special Relativity, in-depth analysis of oscillations, and mechanical waves.

<!-- more -->

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

---

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
\dfrac{d^2 X^\mu}{d\tau^2} = -\Gamma^\mu_{\alpha \beta} \dfrac{dx^\mu}{d\tau} \dfrac{dx^\nu}{d\tau}
{% end %}

The equations that govern spacetime (and correspondingly how all coordinates change) are the **Einstein Field Equations**:

{% math() %}
G_{\mu \nu} + \Lambda g_{\mu \nu} = \dfrac{8\pi G}{c^4} T_{\mu \nu}
{% end %}

Where $G_{\mu \nu}$ is a tensor that describes the _curvature_ of spacetime, $\Lambda$ is called the **cosmological constant**, and $T_{\mu \nu}$ is an extension of the four-momentum. A full explanation of general relativity is very complicated. But for those readers interested, see https://galaxiesbook.org/chapters/C.-General-Relativity.html, which contains a concise but still accurate summary of General Relativity.

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
