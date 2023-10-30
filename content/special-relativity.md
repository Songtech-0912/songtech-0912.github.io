+++
title = "Notes on special relativity"
date = 2023-10-06
+++

These are notes taken in RPI's Physics 1140 class, relating to special relativity.

<!-- more -->

## The standard model

The standard model is one of the most successful theories in physics. Within the standard model, there are several categories of particles. The standard model describes a number of elementary particles - point particles that have no volume and are indivisible. The elementary particles include:

- Fermions (spin-1/2 particles, which include 6 quarks, 6 leptons, and their antiparticles)
- Gauge bosons (these are force carriers with integer spin, which are the photon, gluon, W, and Z)
- Scalar bosons (the Higgs boson)

Quarks are the building blocks of hadrons, such as protons and neutrons. They are never found in isolation, and always found within hadrons. They have half-integer spin, but unlike leptons, they interact with the strong force as well as the weak force.

Leptons are composed of electrons, muons, and tauons, as well as their respective neutrinos. They also have half-integer spin, but do not interact with the strong force.

Gauge bosons are massless with exception of the W and Z bosons. Each carries a fundamental interaction - the photon is the force carrier of electromagnetism, the gluon carries the strong force, and the W & Z bosons carry the weak force.

Composite particles are composed of elementary particles, and include hadrons (mesons and baryons), and everything made of them (such as atoms and molecules). Elementary particles are thought to be point particles that have mass but no volume, whereas composite particles do have a volume.

## Units in physics

Velocity is often measured relative to the speed of light, such as $0.8c$. Charge is often measured with respect to the elementary charge, such as $5e$. Energy is often measured in terms of electron volts (eV), where $1 \text{ eV} = 1.6 \times 10^{-19} \text{ J}$.

## Overview of Special Relativity

A **reference frame** is a specific place you designate as an origin. By constructing a coordinate system from that origin, measurements can be made. An inertial reference frame is a reference frame that isn't accelerating. The laws of special relativity **only** apply to inertial reference frames.

Every observer considers themselves to be at rest with respect to their own reference frame, and everyone else to be moving. For example, an astronaut would consider themselves to not be moving, and the Earth to be moving away from them. Similarly, an observer on Earth would consider themselves to not be moving, and the astronaut in the rocket as moving away from them.

The two postulates of special relativity are that 1) the laws of physics are the same for observers in all inertial reference frames, and that 2) the speed of light is **constant** in all reference frames.

A **proper frame** is a reference frame chosen such that the observer and object being measured are in the same frame. You can think of it as inserting an imaginary observer to "travel along" with a measured object, with a clock to measure times and a ruler to measure distances. For instance, an observer travelling within a spaceship would be in the proper frame of the moving spaceship. An observer travelling along with a muon would be in the proper frame of the muon. Everything in a proper frame is considered stationary by the observer.

A **non-proper frame** is any reference frame in which the observer and object being measured are **not** in the same frame. For instance, an observer on Earth would be in a non-proper frame of an astronaut in a rocket moving relative to Earth.

**Proper time** is the time measured by an observer in a proper frame. **Coordinate time** is the time experienced by an observer in a non-proper frame. Coordinate time $\Delta t$ is related to proper time $\Delta \tau$ by:

$$
\Delta t = \gamma \Delta \tau
$$

where:

$$
\gamma = \frac{1}{\sqrt{1 - \left(\frac{v}{c}\right)^2}}
$$

Using a Taylor series expansion, $\gamma \approx 1$ at very low speeds, and $\gamma \approx 1 + \frac{v^2}{2c^2}$ at low speeds.

**Proper length** is the length of an object as measured by an observer in a proper frame. **Coordinate length** is the length of an object measured by an observer in a non-proper frame. Proper length $\Delta \ell$ is related to coordinate length $\Delta L$ by:

$$
\Delta \ell  = \frac{\Delta L}{\gamma}
$$

## Time dilation and length contraction

Consider an observer to be in the proper frame of a moving spaceship. The observer observes the ship's length as the proper length $\Delta \ell$ and the ship's time as proper time $\Delta \tau$. That observer considers the ship (and everything on it) to be stationary with respect to themselves. Meanwhile, consider a distant observer in a non-proper frame, perhaps situated away on Earth. That distant observer observes the ship's length as the coordinate length $\Delta L$, and the ship's time as the coordinate time $\Delta t$.  We use the familiar equation:

$$
\Delta t = \gamma \Delta \tau
$$

Recall that $\gamma > 1$ for all moving objects. That means for the distant observer who measured a time interval of $\Delta t = 1$ second, the proper time of the observer in the spaceship must be $\Delta \tau < 1$ second. Therefore, the observer in the spaceship's clock ticks slow.

This is the principle of _time dilation_ - **time ticks slow for moving objects**. Recall that any observer would measure every other observer as moving with respect to their own reference frame, however. This means an observer on a rocket would measure a person on Earth as having a slower clock, whereas a person on Earth would _also_ measure the person on the spaceship as having a slower clock!

One area where this has been demonstrated is with muon decay, where muons are measured to be able to travel longer distances than they possibly could given their short lifetimes, as the "internal decay clock" of a muon ticks slow and allows it to travel longer.
