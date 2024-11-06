+++
title = '"Faster than light" travel in GR'
date = 2024-07-30
draft = true
+++

Einstein's theories of relativity tell us that nothing can move faster than light. $c$ is a speed limit of the universe. But while this is a straightforward rule in special relativity, the nuances of general relativity mean that in some cases, one can _appear_ to travel "faster" than light.

<!-- more -->

## A review of special and general relativity

To understand this apparent contradiction (which will eventually turn out to not be one at all), it is important to review Einstein's two theories of relativity: special relativity (SR) and general relativity (GR).

Special relativity was the first theory of the two, and it introduced physics that was a complete departure from the classical physics prior. First, time and space were not distinct, but were interrelated and needed to be considered on an equal footing. The ordinary three-vectors of physics had to be supplemented with a time coordinate; for instance, position became four-position $\mathbf{x} = (ct, x, y, z)$. Second, measurements from and ofa moving coordinate system could yield different results as compared to a stationary coordinate system. Clocks in moving coordinate systems would tick more slowly, and distances would contract. These bizarre features required that space and time be described together within a four-dimensional **spacetime** that did not follow the rules of Euclidean geometry, and a set of transformations known as the **Lorentz transformations** to be used to convert between measurements in non-moving and moving coordinate systems.

General relativity extended the spacetime of special relativity into spacetimes that could be dynamical. Spacetime in GR does not have to be static and flat; it can be curved,and the matter-energy content of spacetime creates this curvature. It is mathematically described by the **Einstein field equations**, which are highly nontrivial to solve, but can be understood on a basic level as a system of partial differential equations. Luckily, solutions to the Einstein Field equations are often very general and widely studied.

The appearance of spacetime curvature in GR means that measurements get even more complex. First, curved spacetimes required a correction to the special relativistic form of Newton's second law. An addition term must be added to account for the spacetime curvature, resulting in:

{% math() %}
F^\mu = m\frac{d^2 x^\mu}{d\tau^2} \rightarrow m\left(\frac{d^2 x^\mu}{d\tau^2} + \Gamma^\lambda {}_{\mu \nu} \frac{dx^\mu}{d\tau} \frac{dx^\nu}{d\tau}\right)
{% end %}

The paths particles take through four-dimensional curved spacetime are known as **geodesics** and are the solutions to the above equation, which reproduce the effect we conventionally associate with gravity. However, since spacetime is curved, measurements from two different locations in spacetime of the same thing can be wildly different. Notions of position, velocity, and momentum become very hard to quantify and must be specified very carefully.

## A conceptual explanation of "faster than light" in GR

General relativity preserves the postulate of $c$ being the absolute speed limit of the universe. That is, it is **always** true that any observer will observe a photon to be moving at the speed of light and cannot exceed the speed of light. However, this posulate holds only _locally_; due to the fact that spacetime is curved, comparing two velocity vectors at two different points in spacetime is not possible, and so it is not possible to formulate a **global** statement of the same.

This, means that in highly-curved spacetimes, a geodesic of a particle can appear to be faster than light, when measured in a distant coordinate system. Note the word _appear_ to be; coordinates in different parts of a curved spacetime are fundamentally incompatible, and so measurements of time and distance are different. The curvature of spacetime, which distorts time and space, can make effective distances shorter than they would be in flat spacetime. Should a particle be travelling between two points in such a highly-curved spacetime, a faraway observer can measure the particle to be travelling **faster** than the speed of light.

## Proving apparent faster-than-light travel

All of this may sound extremely tentative, so let's formulate it in a mathematically precise fashion. This assumes prior knowledge of the mathematics of GR; if not, see the [introduction to general relativity](https://preposterousuniverse.com/wp-content/uploads/2015/08/grtinypdf.pdf) by famed physicist Sean Carroll.

Consider a particle moving very close to a Schwarzschild black hole, described by the Schwarzschild metric, where we will use the $-, +, +, +$ signature convention and natural units where $c = 1$:

{% math() %}
ds^2 = -\left(1 - \frac{2GM}{r}\right) dt^2 + \left(1 - \frac{2GM}{r}\right)^{-1} dr^2 + r^2 (d\theta^2 + \sin^2 \theta d\phi^2)
{% end %}

For a radial orbit, let $d\theta = d\phi = 0$, that is, the particle moves in a single orbital plane. This can be proven to be true but the proof is not necessary to understand the problem. In this case, the metric simplifies to:

{% math() %}
ds^2 = -\left(1 - \frac{2GM}{r}\right) dt^2 + \left(1 - \frac{2GM}{r}\right)^{-1} dr^2
{% end %}

In natural units, the proper time $d\tau$ is related to the spacetime interval by $d\tau^2 = -ds^2$. Therefore we have:

{% math() %}
d\tau^2 = \left(1 - \frac{2GM}{r}\right) dt^2 - \left(1 - \frac{2GM}{r}\right)^{-1} dr^2
{% end %}

Dividing by $d\tau^2$ from all sides yields:

{% math() %}
1 = \left(1 - \frac{2GM}{r}\right) \left(\frac{dt}{d\tau}\right)^2 - \left(1 - \frac{2GM}{r}\right)^{-1} \left(\frac{dr}{d\tau}\right)^2
{% end %}

The speed of the particle is conventionally given by the norm of its three-velocity, but since we are considering radial orbits and thus $\dot \theta = \dot \phi = 0$, it reduces simply to the derivative of the radial component of the position:

{% math() %}
v = \sqrt{\left(\frac{dr}{d\tau}\right)^2 + \cancel{r^2 \left(\frac{d\theta}{d\tau}\right)^2} + \cancel{r^2\sin^2\theta \left(\frac{d\phi}{d\tau}\right)^2} } = \left|\frac{dr}{d\tau}\right|
{% end %}

## Caveats 

First, this effect can _only_ be present when the spacetime itself is curved. A spaceship's engines alone will not produce this effect, unless if said spaceship happens to a black hole you tow along (not recommended!). In addition, this effect is only applicable if the spacetime curvature is significant. Even so, apparent faster-than-light travel would still be very very hard because unless if the spacetime curvature is extreme, you would likely need the spacecraft to already start off moving at a significant fraction of the speed of light.

Could we harness this effect for producing spaceships that can traverse vast interstellar distances rapidly? Maybe.
