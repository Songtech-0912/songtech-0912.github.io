+++
title = "Introductory Quantum Physics notes"
date = 2024-05-07
+++

This a mini-book on quantum physics, with topics covered including wavefunctions, various solutions of the time-dependent and independent Schrödinger equation, the uncertainty principle, and expectation values.

<!-- more -->

## Foreword

Familiarity with the underlying math is expected, including a background in multivariable calculus, differential equations, and some linear algebra (vectors, matrices, and eigenvalues). Don't worry if these are alien topics! There are full guides to each in the [calculus series](@/calculus-series.md). In addition, while not required, the [introductory classical dynamics series](@/classical-dynamics.md) can be very helpful as well.

## Why quantum theory?

Quantum theory is our best understanding of how the universe works at its most fundamental level. It is fundamentally paradoxical to human experience, but it is the bedrock of almost all of modern physics, and essential for many advanced technologies. In addition, it is also a very scientifically and philosophically interesting theory to learn. These notes form the basis of an introduction to quantum mechanics.  

In the following sections, we will first preview the essential features of quantum mechanics, laying out _what_ exactly quantum mechanics is. Don't worry if this does not make sense yet! We will dive into each topic in detail and gently build up an explanation of them throughout the rest of these notes.

## The fundamental postulates of quantum mechanics

As a whole, the theory of quantum mechanics can be said to originate from 5 fundamental postulates:

1. In the quantum mechanical description of a system, all physical quantities are _quantized_.
2. A quantum system is completely described by a **quantum state** $|\Psi\rangle$, which is a complex-valued vector in a Hilbert space. The time-evolution of a quantum state is described by the Schrödinger equation.
3. Physical quantities are known as **observables**, and are represented by linear Hermitian operators acting on the quantum state.
4. The _eigenvalues_ of each observable correspond to possible _measured values_ of the associated physical quantity (e.g. position, momentum, energy)
5. It is **not possible** to predict in advance the measured value a physical quantity may take. However, it is possible to predict the _probability_ of a physical quantity taking a particular value $\lambda$ through the Born rule $\rho = |\langle \lambda | \Psi\rangle |^2$

The following sections will go in-depth into what each of these postulates actually means.

> Note that quantum mechanics is a theory that describes _all objects_ including macroscopic ones. However, the theory is primarily used at very small scales (typically subatomic scales) because calculations with macroscopic objects quickly become intractable; this is because they are composed of many billions of subatomic particles, and statistical physics is often necessary to sufficiently describe them. See [this Physics SE post](https://physics.stackexchange.com/questions/567596/is-quantum-mechanics-applicable-to-only-small-things) for more details.

### Postulate 1: quantization

When a quantitiy is said to be **quantized**, it _cannot take on continuous values_; it can only come in discrete steps. In addition, all possible values of that quantity must be an integer multiple of some base indivisible value. 

For example, consider electrical charge. The base value of electric charge is the elementary charge constant $e$ (not to be confused with Euler's number), associated with a single electron. It is _only_ possible for an object in the universe to have a charge of $1e, 2e, 3e, \dots ne$. It is not possible for an object to have a charge of $3.516e$.

> Note to the advanced reader: yes, indeed, quarks have a different quantum of charge, but since quarks can never be found on their own, and are always grouped together into composite, not elementary particles, we consider $e$ the quantum of charge, associated with an electron.

Similarly, consider electromagnetic radiation. The base value of electromagnetic energy is given by $hf = \dfrac{hc}{\lambda}$, the radiation of a single photon of frequency $f$ and wavelength $\lambda$, where $h = \pu{6.626e-34 J*Hz^{-1}}$ is the Planck constant. All electromagnetic energy of a given frequency $f$ and wavelength $\lambda$ must be composed of multiples of this value.

### Postulate 2: quantum states

In classical mechanics, the future state of any system of particles can be known by knowing its current state and its equations of motion. The equations of motion are Newton's 2nd law:

{% math() %}
m \frac{d^2 \mathbf{r}}{dt^2} = \mathbf{F}(\mathbf{r}, t)
{% end %}

Which can be rewritten as system of 2 coupled first-order ODEs:

{% math() %}
\begin{align*}
\frac{d\mathbf{p}}{dt} = \mathbf{F}(\mathbf{r}, t) \\
m \frac{d\mathbf{r}}{dt} = \mathbf{p}
\end{align*}
{% end %}

The initial condition for this system is the **classical state** of the particle, and is the following 6-component vector, consisting of three components of position and three components of momentum:

{% math() %}
\mathbf{X}_0 = \begin{pmatrix}
x_0 \\
y_0 \\
z_0 \\
p_{x_0} \\
p_{y_0} \\
p_{z_0}
\end{pmatrix}
{% end %}

In quantum mechanics, the future state of a system is determined via a **quantum state**. This quantum state is typically denoted by an abstract vector $|\psi\rangle$ whose components are complex numbers, with the specialized notation (called bra-ket notation or Dirac notation) used to differentiate quantum states from classical states. Abstract vectors reside in a Hilbert space $\mathcal{H}$ which is complex, and unlike ordinary Cartesian vectors, they can be infinite-dimensional. However, since quantum states are so abstract, there is an equivalent formulation of quantum mechanics in terms of partial differential equations, as the two formulations are equivalent. In the differential equation formulation, we solve for **wavefunction** $\Psi(\mathbf{x}, t)$, which obey the Schrödinger wave equation:

{% math() %}
i\hbar \frac{\partial}{\partial t} \Psi(\mathbf{x}, t) = \left(-\frac{\hbar^2}{2m} \frac{\partial^2}{\partial x^2} + V(x, t)\right) \Psi(\mathbf{x}, t) 
{% end %}

 The physical interpretation of the Schrödinger equation is that all quantum particles (such as electrons, quarks, etc.) have wave-like properties as well as particle-like properties, and their wave nature is associated with the wavefunction $\Psi(\mathbf{x}, t)$. This allows them to exhibit effects such as wave interference and diffraction, as well as to have an associated wavelength. However, quantum particles are localized on measurement, like classical particles, and this is due to the fact that the wavefunction is associated with particle probability distributions. This fact is known as **wave-particle duality**.

## The question of observation

How do particles know they are being observed? Because the act of observation involves detecting a photon that interacts with (and disturbs) the particle.
