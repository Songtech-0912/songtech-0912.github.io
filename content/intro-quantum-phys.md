+++
title = "Introductory Quantum Physics notes"
date = 2024-05-07
+++

These are notes taken in preparation of and during Quantum Physics I (PHYS 2210) at RPI, with topics covered including wavefunctions, various solutions of the time-dependent and independent Schrödinger equation, the uncertainty principle, and expectation values.

<!-- more -->

## Foreword

Familiarity with the underlying math is expected, including a background in multivariable calculus, differential equations, and some linear algebra (vectors, matrices, and eigenvalues). Don't worry if these are alien topics! There are full guides to each in the [calculus series](@/calculus-series.md). In addition, while not required, the [introductory classical dynamics series](@/classical-dynamics.md) can be very helpful as well.

## The fundamental postulates of quantum mechanics

As a whole, the theory of quantum mechanics can be said to originate from 5 fundamental postulates:

1. In the quantum mechanical description of a system, all physical quantities are _quantized_.
2. A quantum system is completely described by a **quantum state** $|\Psi\rangle$. The time-evolution of a quantum state is described by the Schrödinger equation $\displaystyle i\hbar \frac{\partial}{\partial t} |\Psi\rangle = \hat H |\Psi\rangle$. 
3. Physical quantities are known as **observables**, and are represented by linear operators acting on the quantum state
4. The _eigenvalues_ of each observable correspond to possible _measured values_ of the associated physical quantity (e.g. position, momentum, energy)
5. It is **not possible** to predict in advance the measured value a physical quantity may take. However, it is possible to predict the _probability_ of a physical quantity taking a particular value $\lambda$ through the Born rule $\rho = |\langle \lambda | \Psi\rangle |^2$

The following sections will go in-depth into what each of these postulates actually means.

> Note that quantum mechanics is a theory that describes _all objects_ including macroscopic ones. However, the theory is primarily used at very small scales (typically subatomic scales) because calculations with macroscopic objects quickly become intractable; this is because they are composed of many billions of subatomic particles, and statistical physics is often necessary to sufficiently describe them. See [this Physics SE post](https://physics.stackexchange.com/questions/567596/is-quantum-mechanics-applicable-to-only-small-things) for more details.

### Postulate 1: quantization

When a quantitiy is said to be **quantized**, it _cannot take on continuous values_; it can only come in discrete steps. In addition, all possible values of that quantity must be an integer multiple of some base indivisible value. 

For example, consider electrical charge. The base value of electric charge is the elementary charge constant $e$ (not to be confused with Euler's number). It is _only_ possible for an object in the universe to have a charge of $1e, 2e, 3e, \dots ne$. It is not possible for an object to have a charge of $3.516e$. 

### Postulate 2: quantum states

In classical mechanics, the future state of any system can be known by knowing its current state and its equations of motion. The equations of motion are Newton's 2nd law:

$$
m \frac{d^2 \mathbf{r}}{dt^2} = \mathbf{F}(\mathbf{r}, t)
$$

Which can be rewritten as system of 2 coupled first-order ODEs:

$$
\frac{d\mathbf{p}}{dt} = \mathbf{F}(\mathbf{r}, t)
$$

$$
m \frac{d\mathbf{r}}{dt} = \mathbf{p}
$$

The initial condition for this system is the **classical state** of the particle, and is the following 6-vector, consisting of three components of position and three components of momentum:

$$
\mathbf{X}\_0 = \begin{pmatrix}
x_0 \\\\
y_0 \\\\
z_0 \\\\
p\_{x_0} \\\\
p\_{y_0} \\\\
p\_{z_0}
\end{pmatrix}
$$

## The question of observation

How do particles know they are being observed? Because the act of observation involves detecting a photon that interacts with (and disturbs) the particle.
