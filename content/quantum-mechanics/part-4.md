+++
title = "In-Depth Quantum Mechanics, Part IV"
date = 2026-10-20
+++

In our last installment of the quantum mechanics series, we conclude with an exploration of advanced topics in quantum physics: particle physics, quantum field theory, and the path integral.

<!--more -->

> ### Chapter guide for Quantum Mechanics
> 
> - [Part 1](@/quantum-mechanics/index.md) covers the basic ideas of quantum mechanics and its fundamental formalism.
> - [Part 2](@/quantum-mechanics/part-2.md) covers applications of quantum mechanics as well as more advanced quantum-mechanical systems.
> - [Part 3](@/quantum-mechanics/part-3.md) covers approximation methods in quantum mechanics, as well as applications to a variety of systems.
> - [Part 4](@/quantum-mechanics/part-4.md) covers advanced topics in quantum mechanics, including relativistic quantum mechanics, second quantization, and quantum field theory. **You are reading this part right now.**

_Note: this section is currently incomplete; in particular, scattering (in the Born approximation as well as with the S-matrix approach), relativistic QED, and the path integral are not covered. Despite this, it is hoped that the existing content will be of educational interest._

## Second quantization

Previously, we saw that the Pauli Hamiltonian described electromagnetic interactions in quantum mechanics, but this is not the full story. The Pauli Hamiltonian is ultimately just an approximation, because it assumes classical electromagnetic fields. In reality, the electromagnetic field - and indeed all fundamental fields - are quantum in nature.

The process of going from _classical_ electrodynamics to _quantum_ electrodynamics is called **second quantization**, a term to differentiate it from **first quantization**, where we take classical variables (e.g. position, momentum, and angular momentum) and translate them into quantum operators.

> **Note:** In this section, we will not analyze the _full_ relativistic theory of quantum electrodynamics, which we'll cover later on. Rather, we will discuss the non-relativistic theory of quantum electrodynamics (often referred to as NRQED for short), which nonetheless has many applications, including quantum optics and quantum information theory.

To start, we note that an arbitrary electromagnetic field with electric potential $\phi$ and magnetic potential $\mathbf{A}$ can be decomposed as a sum (or integral) of plane waves (called _modes_), each of different wavevector $\mathbf{k}$ (this is just the Fourier series):

{% math() %}
\begin{align*}
\phi(\mathbf{r}, t) &= \sum_\mathbf{k}A_\mathbf{k} e^{i(\mathbf{k} \cdot \mathbf{r} + \omega t)} \\
\mathbf{A}(\mathbf{r}, t) &= \sum_\mathbf{k} \vec B_\mathbf{k} e^{i(\mathbf{k} \cdot \mathbf{r} + \omega t)} \\
\end{align*}
{% end %}

Where $A_\mathbf{k}, \vec B_\mathbf{k}$ are constant coefficients in the series expansion over all modes. To quantize the electromagnetic field, it is necessary to sum over all the modes of the system....

{% math() %}
\hat H  =  \sum_\mathbf{k}\hbar \omega_\mathbf{k} \left(\hat a_\mathbf{k}^\dagger \hat a_\mathbf{k} + \dfrac{1}{2}\right)
{% end %}

Note that since we have decomposed the electromagnetic field into modes, and each mode represents an _exact momentum_ (by $\mathbf{p} = \hbar \mathbf{k}$), this means that by the Heisenberg uncertainty principle, photons are completely delocalized in space. Thus, the Fock states are states in the **momentum basis**, where particle states are plane waves of the form $e^{i\mathbf{p} \cdot \mathbf{x}}$.

One might ask, how do states in conventional quantum mechanics fit in to the quantum electrodynamics picture? For instance, if we had a hydrogen atom interacting with a quantized electromagnetic field, how could we model this? The answer is that as long as we're working with energies that are not high enough to require us to consider the effects of relativity (which we can assume to be true most of the time), we can just use the normal $|n, m, \ell\rangle$ states of the hydrogen atom. We know that ultimately, the hydrogen atom is made of elementary particles that come from quantum fields, but for our purposes, we can use the _first-quantized_ hydrogen atom together with the _second-quantized_ electromagnetic field.


## Relativistic wave equations

The Dirac equation describes a relativistic spin-1/2 particle (like an electron). For a **free particle** it takes the form:

{% math() %}
(i\hbar \gamma^\mu \partial_\mu - mc)\psi = 0
{% end %}

The Dirac equation with the electromagnetic four-potential $A_\mu = (A_0, \mathbf{A}) = (\frac{1}{c} V, \mathbf{A})$ takes a very similar form, except the partial derivative $\partial_\mu$ is replaced by a new differential operator $D_\mu$:

{% math() %}
(i\hbar \gamma^\mu D_\mu - mc)\psi = 0, \quad D_\mu = \partial_\mu + \dfrac{ie}{\hbar} A_\mu
{% end %}

### Relativity, the Dirac equation, and the road to QFT

Unfortunately, the Dirac equation, despite its successes, has limited applicability. Why? Primarily, because at the relativistic energies it describes, new particles can be created from pure energy (remember Einstein's famous equation $E = mc^2$, this means that a particle of mass $m$ can be created from energy $E$ if $E/c^2 > m$). Additionally, particles can annihilate with each other and be destroyed, and particles can turn into new (and often different types of) particles. The number of particles is never constant - new particles are being created all the time, and old particles are getting annihilated or turn into new particles. This makes the utility of a quantum wave equation that describes fixed numbers of particles rather limited; after a few nanoseconds (or shorter still), the electron you were describing no longer exists, and its wavefunction also vanishes.

## Quantum field theory

### The emergence of field quanta

Quantum field theory tells us that all matter in the Universe is composed of quantum fields. These fields are said to be _quantized_ as they can only come in distinct states. Mathematically, this corresponds to quantum fields being _operator-valued_ as opposed to classical fields, which are functions of space and time.


Free particles, which have a very small range of momenta, can be approximated as plane waves $\psi(x) = e^{\pm ipx}$.

The energy of the lowest excited state of a quantum field is given (relative to the ground state) by:

{% math() %}
E_\omega = \hbar \omega
{% end %}

In the case of massive fields (that is, fields describing particles with mass), this result can be written as:

{% math() %}
E_\omega = E_k = \sqrt{(pc)^2 + (mc^2)^2} = \sqrt{(\hbar kc)^2 + (mc^2)^2}
{% end %}

This is a special case of the quantized energies of a massive field (that is, fields describing particles with mass), which comes from the relativistic energy-momentum relation:

{% math() %}
E^2 = (pc)^2 + (mc^2)^2, \quad p = \hbar k
{% end %}

If we switch back to natural units, our expression reads:

{% math() %}
E_k = \sqrt{k^2 + m^2}
{% end %}

> **Note:** For massless particles (like photons), this simplifies to $E_k = k = \omega$

We can show this result

{% math() %}
p^2 + m^2 = E^2
{% end %}

The total energy is of course simply the sum of all of the modes (so sum over $\omega$ for the first and sum over $k$ for the second).

Note how both $\omega$ and $k$ describe oscillations - in fact, in natural units, we know that for massless particles, $\omega = k$. This tells us that **stable particles are just long-lived vibrational modes in quantum fields**. It is similar to how phonons in solid-state physics appear as quasiparticles from vibrational modes.

The total energy of a quantum field is given by summing over all the energy fluctuations of the field, which becomes an integral:

{% math() %}
E_\text{total} = \int d^3 \omega~ E_\omega = \sum_k E_k
{% end %}

### Second quantization from Lagrangian field theory

We'll now examine another perspective of second quantization: as the quantum extension of a _classical_ Lagrangian describing a _classical_ field theory.

To go from classical field theory to quantum field theory:

- Classical equations of motion become _operator_ equations motion (that look the same but have very different properties)
- Classical plane-wave solutions to the field equations become single-particle states of the fields
- Fields have a nonzero energy even when in their lowest-energy state
- Classical oscillating fields become coupled quantum harmonic oscillators

Action principle, etc. and then also see the [advanced classical mechanics guide](@/advanced-classical-mech/index.md) for an overview of tensors and the Euler-Lagrange equations.

### The free scalar field

### The Dirac field

### The spin-statistics theorem

### Fundamentals of quantum electrodynamics