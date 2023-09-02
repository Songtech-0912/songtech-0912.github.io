+++
title = "Waves and oscillations notes"
+++

These are notes taken during RPI's PHYSICS 1140 course, relating to a review of waves and oscillations.

<!-- more -->

It is recommended to use `Ctrl F` or the equivalent search function to find the relevant section, as these notes are quite long.

## Oscillating systems

A system that **oscillates** is described as undergoing **periodic motion** - motion that repeats. 

## Periodic waves

**Periodic waves** that satisfy the following characteristics:

- They repeat with the same period $T$
- Each repeat has the same amplitude $A$

## Harmonic waves

A harmonic wave is a 1D period wave that can be represented mathematically as:

$$
y(t) = A \sin (\omega t + \phi_0)
$$

Where $\phi_0$ is the phase shift (in radians), $A$ is the amplitude (in meters), and $\omega = \frac{2\pi}{T} = 2\pi f$ is the angular frequency (in radians per second).

## Traveling waves

Traveling waves are waves that move through space. Unlike non-traveling waves, which describe 1D motion, they describe 2D motion. They take a wide variety of forms, from mechanical waves to electromagnetic waves. Waves (or at least ideal waves) can be expressed as:
$$
u(x, t) = f(x - vt)
$$
if traveling in the positive x-direction, or:
$$
u(x, t) = f(x + vt)
$$
if traveling in the negative x-direction. The reason for the opposite sign is that $f(x - C$) describes a rightward shift in a graph, and $f(x - C)$ describes a leftward shift in a graph.
Traveling harmonic waves are a special case of traveling waves that are described by:
$$
y(x, t) = y_m \sin\left(\frac{2\pi}{\lambda} (x - vt) + \phi_0\right)
$$
where $\omega = 2\pi f$ and  $v = \lambda f$. If we let $k = \frac{2\pi}{\lambda}$, we can more simply write this equation as:
$$
y(x, t) = y_m \sin(k(x - vt) + \phi_0)
$$
Note that unlike non-traveling harmonic waves, which are functions of time, traveling waves are functions of position _and_ time.
To find the values of each of the constants describing harmonic traveling waves:

| Constant | Method (if given a graph) | Method (if given a function) |
|---|---|---|
| $y_m$ | Looking at amplitude of graph | Reading it off the standard form of the function |
| $\lambda$ | Looking at the horizontal distance between 2 high peaks | Deriving it from the wavenumber given $\lambda = \frac{2\pi}{k}$ |
| $k$ (wavenumber) | Calculating using $k = \frac{2\pi}{\lambda}$ | Reading it off the standard form of the function |
| $v$ | Cannot be calculated from just a graph | Reading it off the standard form of the function |
| $\phi_0$ (phase shift) | Find the initial height $y_0$ and the amplitude $y_m$, then use $\phi = \sin^{-1} (y_m / y_0)$ | Reading it off the standard form of the function |
| $\omega$ | Cannot be calculated from just a graph | Deriving it from the frequency given $\omega = 2\pi f$ |
| $T$ | Cannot be calculated from just a graph | Deriving it from the frequency given $f = \frac{1}{T}$ |
| $f$ | Cannot be calculated from just a graph | Deriving it from velocity given $f = \frac{v}{\lambda}$ |

## Phase and Phase Difference

**Phase** is an angular measure of how much of the graph is covered up to a certain point, and is given by (for a traveling wave):
$$
\phi = \frac{2\pi}{\lambda} (x - x_0)
$$
A phase of $2\pi$, for instance, indicates that the graph has covered $\lambda$ units of distance and completed one full cycle.
Phase changes through time and through space for a traveling harmonic wave. The change in phase $\Delta \phi$ between two times is given by:
$$
\Delta \phi = \frac{2\pi}{\lambda} v\Delta t
$$
And between two points separated in space is given by:
$$
\Delta \phi = \frac{2\pi}{\lambda} v\Delta x
$$
## Superposition

Traveling waves that pass through each other can be added to form a **superposition**:
$$
y(x, t) = y_1(x, t) + y_2(x, t)
$$
