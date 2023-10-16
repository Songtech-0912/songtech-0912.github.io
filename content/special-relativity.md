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

A **reference frame** is a specific place you designate as an origin. By constructing a coordinate system from that origin, measurements can be made. An inertial reference frame is a reference frame that isn't accelerating.

The two postulates of special relativity are that 1) the laws of physics are the same for observers in all inertial reference frames, and that 2) the speed of light is **constant** in all reference frames.

The proper frame is the reference frame attached to the comoving observer - the observer that "travels along" with the event. The proper frame for a set of measurements are different depending on whether the value being measured is proper time or proper length.

**Proper time** can be thought of as the time measured by an observer's own clock as the observer travels, and is the time the observer actually experiences.

**Coordinate time** can be thought of time measured by a distant observer that is not traveling.

Coordinate time $\Delta t$ is related to proper time $\Delta \tau$ by:

$$
\Delta t = \gamma \Delta \tau
$$

where:

$$
\gamma = \frac{1}{\sqrt{1 - \left(\frac{v}{c}\right)^2}}
$$

Using a Taylor series expansion, $\gamma \approx 1$ at very low speeds, and $\gamma \approx 1 + \frac{v^2}{2c^2}$ at low speeds.

**Proper length** is the length of an object as measured in its rest frame. **Coordinate length** is the length of an object as measured when it is moving. Proper length $\Delta \ell$ is related to coordinate length $\Delta L$ by:

$$
\Delta \ell  = \frac{\gamma}{\Delta L}
$$
Relativistic equations are often analogous to the equations of classical mechanics:

$$
p = \gamma mv
$$

$$
E = \gamma mc^2
$$
