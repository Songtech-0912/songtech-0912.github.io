+++
title = "In-Depth Quantum Mechanics"
date = 2025-08-31
draft = false
+++

This is a guide to quantum mechanics beyond the basics, and is a follow-up to [introductory quantum physics](@/intro-quantum-phys.md). Topics convered include state-vectors, Hilbert spaces, intrinsic spin and the Pauli matrices, the hydrogen atom in detail, the quantum harmonic oscillator, time-independent perturbation theory, and a basic overview of second quantization and relativistic quantum mechanics.

<!-- more -->

I thank [Professor Meng](https://www.xmeng.io) at Rensselaer Polytechnic Institute, without whom this guide would not have been possible.

## Prerequisites

This guide will assume considerable prior knowledge, including multivariable & vector calculus, linear algebra, basic quantum mechanics, integration with delta functions, classical waves, Fourier series, solving boundary-value problems, and (in later chapters) tensors and special relativity. If you don't know some (or all) of these, that's okay! There are dedicated guides about each of these topics on this site:

- For a review of calculus (in particular multivariable and vector calculus), see the [calculus series](@/calculus-series.md)
- For a review of the classical theory of waves, see the [waves and oscillations guide](@/waves-and-oscillations/index.md)
- For a review of basic quantum mechanics, see the [introductory quantum mechanics guide](@/intro-quantum-phys.md)
- For a review of electromagnetic theory, see the [fundamentals of electromagnetism guide](@/electromagnetism/index.md) as well as the [in-depth electromagnetism guide](@/classical-electromagnetism/index.md)
- For a review of boundary-value problems, Fourier series, and see the [PDEs guide](@/intro-pdes/index.md)
- For a review of special relativity and tensors, see the [advanced classical mechanics guide](@/advanced-classical-mech/index.md)

## Foreword

Quantum mechanics is a fascinating subject. Developed primarily in the early 20th-century, it is a theory that (at the time of writing) is barely a hundred years old, but its impact on physics and technology is immense. Without quantum mechanics, we would not have solid-state hard drives, phones, LED lights, or MRI scanners. Quantum mechanics has revolutionized the world we live in, and this is despite the fact that it governs the behavior of particles smaller than we could ever possibly see. But understanding how matter behaves at tiny, microscopic scales is the key to understanding how matter on macroscopic scales behaves. Quantum mechanics unlocks the secrets of the microscopic world, and however unintuitive it may be, it is the best (nonrelativistic) theory we have to understand this strange, mysterious world.

## Basics of wave mechanics

In classical physics, it was well-known that there was a clear distinction between two phenomena: _particles_ and _waves_. Waves are oscillations in some medium and are not localized in space; particles, by contrast, are able to move freely and are localized. We observe, however, in the quantum world, that "waves" and "particles" are both _incomplete descriptions_ of matter at its most fundamental level. Quantum mechanics (at least without the inclusion of quantum field theory) does **not** answer _why_ this is the case, but it offers a powerful theoretical framework to *describe* the wave nature of matter, called **wave mechanics**. In turn, understanding the wave nature of matter allows us to make powerful predictions about how matter behaves at a fundamental level, and is the foundation of modern physics.

### Introduction to wave mechanics

From the classical theory of waves and classical dynamics, we can build up some basic (though not entirely correct) intuition for quantum theory. Consider a hydrogen atom, composed of a positively-charged nucleus, and a negatively-charged electron. Let us assume that the nucleus is so heavy compared to the electron that it may be considered essentially a classical point charge. Let us also assume that the electron orbits the nucleus at some known distance $R$. For the electron to not decay and fall into the nucleus, classical mechanics tells us that its potential energy and kinetic energy must balance each other. Thus, the electron must both be moving and have some amount of potential energy, which comes from the electrostatic attraction of the electron to the nucleus. This bears great resemblance to another system: the orbital motion of the planets around the solar system.

However, experiments conducted in the early 20th century revealed that atoms emit light of specific wavelengths, meaning that they could only carry discrete energies, and therefore only be found at certain locations from the nucleus. This would not be strange in and of itself, but these experiments *also* found that electrons could "jump" seemingly randomly between different orbits around the nucleus. That is to say, an electron might initially be at radius $R_1$, but then it suddenly jumps to $R_3$, then jumps to $R_2$, but cannot be found anywhere between $R_1$ and $R_2$ or between $R_2$ and $R_3$. This meant that electrons could _not_ be modelled in the same way as planets orbiting the Sun - this jumpy "orbit" would be a very strange one indeed!

Instead, physicists wondered if it would make more sense to model electrons as _waves_. This may seem absolutely preposterous on first inspection, but it makes more sense when you think about it more deeply. First, a wave isn't localized in space; instead, it *fills all space*, so if the electron was indeed a wave, it would be possible to find the electron at different points in space ($R_1, R_2, R_3$) throughout time. In addition, waves also *oscillate* through space and time at very particular frequencies. It is common to package the _spatial frequency_ of a wave via a **wavevector** $\mathbf{k} = \langle k_x, k_y, k_z\rangle$ and the *temporal frequency* of a wave via an **angular frequency** $\omega$ (for reasons we'll soon see). Since these spatial and temporal frequencies can only take particular values, the shape of the wave is also restricted to particular functions, meaning the pulses of the wave could only be found at particular locations. If we guess the pulses of the wave to be somehow linked to the position of the electron (and this is a correct guess!), that would neatly give an explanation for why electrons could only be found at particular orbits around the nucleus and *never* between two orbits.

The simplest types of waves are **plane waves**, which may be described by complex-valued exponentials $e^{i(\mathbf{k} \cdot \mathbf{x} + \omega t)}$, or by equivalent real-valued sinusoids $\cos(\mathbf{k}\cdot \mathbf{x} + \omega t)$. Thus, it would make sense to describe such waves with a complex-valued wave equation, where we use complex numbers for mathematical convenience (it is much easier to take derivatives of complex exponentials than real sinusoids). To start, let's assume that our electron is a wave whose spatial and time evolution are described by a certain function, which we'll call a **wavefunction** and denote $\Psi(x, t)$. We'll also assume for a free electron far away from any atom, the wavefunction has the mathematical form of a plane wave:

{% math() %}
\Psi(x,t) = e^{i(\mathbf{k} \cdot \mathbf{x} - \omega t)}
{% end %}

Note that if we differentiate our plane-wave with respect to time, we find that:

{% math() %}
\dfrac{\partial \Psi}{\partial t} = \dfrac{\partial}{\partial t}e^{i(\mathbf{k} \cdot \mathbf{x} - \omega t)} = \dfrac{\partial}{\partial t} e^{i\mathbf{k} \cdot \mathbf{x}} e^{-i\omega t} = -i\omega  e^{i(\mathbf{k} \cdot \mathbf{x} - \omega t)} = -i\omega \Psi(x, t)
{% end %}

We'll now introduce a historical discovery in physics that transforms this interesting but not very useful result into a powerful lead for quantum mechanics. In 1905, building on the work by German physicist Max Planck, Albert Einstein found that atoms emit and absorb energy in the form of light with a fixed amount of energy. This energy is given by the equation $E = h\nu$ (the **Planck-Einstein relation**), where $h = \pu{6.62607015E-34 J*s}$ is known as the [Planck constant](https://en.wikipedia.org/wiki/Planck_constant), and $\nu$ is the frequency of the light wave. Modern physicists usually like to write the Planck-Einstein relation in the equivalent form $E = \hbar \omega$, where $\omega = 2\pi \nu$. Armed with this information, we find that we can slightly rearrange our previous result to obtain an expression for the energy!

{% math() %}
\omega \Psi(x, t) = \frac{1}{-i}\dfrac{\partial}{\partial t} \Psi(x, t) = i\dfrac{\partial}{\partial t} \Psi(x, t) \quad \Rightarrow \quad \hbar \omega = i\hbar\dfrac{\partial}{\partial t} \Psi(x, t) = E
{% end %}

> **Note:** here, we used the fact that $\dfrac{1}{-i} = i$. You can prove this by multiplying $\dfrac{1}{-i}$ by $\dfrac{i}{i}$, which gives you $\dfrac{i}{1} = i$.

Meanwhile, we know that the classical expression for the total energy is given by $E = K + V$, where $K$ is the kinetic energy and $V$ is the potential energy (in quantum mechanics, we often just call this the _potential_ for short). The kinetic energy is related to the *momentum* $p$ of a classical particle by $K = \mathbf{p}^2/2m$ (where $\mathbf{p}^2 = \mathbf{p} \cdot \mathbf{p}$). This may initially seem relatively useless - we are talking about a quantum particle, not a classical one! - but let's assume that this equation still holds true in the quantum world.

Now, from experiments done in the early 20th-century, we found that all quantum particles have a fundamental quantity known as their [de Broglie wavelength](https://en.wikipedia.org/wiki/Matter_wave) (after the French physicist Louis de Broglie who first theorized their existence), which we denote as $\lambda$. This wavelength is *tiny* - for electrons, $\lambda = \pu{167pm} = \pu{1.67E-10m}$, which is about ten million times smaller than a grain of sand. The momentum of a *quantum particle* is directly related to the de Broglie wavelength; in fact, it is given by $\mathbf{p} = \hbar \mathbf{k}$, where $|\mathbf{k}| = 2\pi/\lambda$. Combining $\mathbf{p} = \hbar \mathbf{k}$ and $K = \mathbf{p}^2/2m$, we have:

{% math() %}
E = K + V = \dfrac{\mathbf{p}^2}{2m} + V(x) = \dfrac{(\hbar \mathbf{k})^2}{2m} + V(x)
{% end %}

Can we find another way to relate $\Psi$ and the energy $E$ using this formula? In fact, we can! If we take the *gradient* of our wavefunction, we have:

{% math() %}
\nabla\Psi = \nabla e^{i\mathbf{k} \cdot \mathbf{x}} e^{-i\omega t} = e^{-i\omega t} \nabla e^{i\mathbf{k} \cdot \mathbf{x}}= e^{-i\omega t}i\mathbf{k} (e^{i\mathbf{k} \cdot \mathbf{x}}) = i\mathbf{k}  \Psi
{% end %}

Then, taking the divergence of the gradient (which is the *Laplacian operator* $\nabla^2 = \nabla \cdot \nabla$) we have:

{% math() %}
\nabla^2 \Psi = (i\mathbf{k})^2 \Psi = -\mathbf{k}^2 \Psi \quad \Rightarrow \quad \mathbf{k}^2 = -\nabla^2 \Psi
{% end %}

Combining this with our classical-derived expression for the total energy, we have:

{% math() %}
E = \dfrac{(\hbar \mathbf{k})^2}{2m} + V(x) = -\dfrac{\hbar^2}{2m}\nabla^2 \Psi + V \Psi
{% end %}

Where $V \Psi$ is some term that we presume (rightly so) to capture the *potential energy* of the quantum particle. Equating our two expressions for $E$, we have:

{% math() %}
E = i\hbar\dfrac{\partial}{\partial t} \Psi(x, t) = -\dfrac{\hbar^2}{2m} \nabla^2 \Psi + V\Psi
{% end %}

Which gives us the **Schrödinger equation**:

{% math() %}
i\hbar\dfrac{\partial}{\partial t} \Psi(x, t) = \left(-\dfrac{\hbar^2}{2m} \nabla^2 + V\right)\Psi(x,t)
{% end %}

What we have been calling $\Psi(x, t)$ can now be properly termed the **wavefunction**. But what is it? The predominant opinion is that the wavefunction should be considered a **probability wave**. That is to say, the wave is not a physically-observable quantity! We'll discuss the implications (and consequences) of this in time, but for now, we'll discuss 2 *real-valued* quantities that can be found

1. The **amplitude** $|\Psi(x, t)|$ is the magnitude of the wavefunction
2. The **phase** $\phi = \text{arg}(\Psi) = \tan^{-1}\left(-\dfrac{\text{Im}(\Psi)}{\text{Re}(\Psi)}\right)$ describes how far along each oscillation the wavefunction has elapsed in space and time. (Here, $\text{arg}$ is the [complex-valued argument function](https://en.wikipedia.org/wiki/Argument_(complex_analysis)).)

> **Note:** In quantum field theory, the probability interpretation of the wavefunction is no longer the case; rather, $\Psi(x, t)$ is reinterpreted as a **field** and its real and imaginary parts are required to describe both particles and anti-particles. However, we will wait until later to introduce quantum field theory.

### The free particle

We already know one basic solution to the Schrodinger equation (in the case $V = 0$): the case of plane waves $e^{i(kx - \omega t)}$. Because the Schrodinger equation is a linear PDE, it is possible to sum several different solutions together to form a new solution; indeed, the _integral_ of a solution is also a solution! Thus, we have arrived at the solution to the Schrodinger equation for a free particle (in one dimension):

{% math() %}
\Psi(x, t) = \dfrac{1}{\sqrt{2\pi}} \int_{-\infty}^\infty dk\, g(k) e^{i(k x - \omega(k) t)}
{% end %}

This is known as a **wave packet**, since it is a superposition of multiple waves and in fact it  looks like a bundle of waves (as shown by the animation below)!

![Wavepacket animation, showing a "pulse" propagating along the positive x-axis](https://upload.wikimedia.org/wikipedia/commons/d/d8/Wave_packet_propagation_%28phase_faster_than_group%2C_nondispersive%29.gif)

_Source: [Wikipedia](https://en.m.wikipedia.org/wiki/File:Wave_packet_propagation_(phase_faster_than_group,_nondispersive).gif)_

> **Reader's note:** Another nice animation can be found at [this website](https://www.cond-mat.de/teaching/QM/JSim/wpack.html).

Note that $g(k)$ is an arbitrary function that is determined by the initial conditions of the problem. In particular, using Fourier analysis we can show that it is given by:

{% math() %}
g(k) = \dfrac{1}{\sqrt{2\pi}} \int_{-\infty}^\infty dx \,\Psi(x, 0) e^{-ikx}
{% end %}

In the wave packet solution, $\omega(k)$ is called the **dispersion relation** and is a fundamental object of study in many areas of condensed-matter physics and diffraction theory. It relates the angular frequency (which governs the _time oscillation_ of the free particle's wavefunction) to the wavenumber (which governs the _spatial oscillation_ of the free particle's wavefunction). The reason we use the angular frequency rather than the "pure" frequency $\nu$ is because $\omega$ is technically the frequency at which the _phase_ of the wavefunction evolves, and complex-exponentials in quantum field theory almost always take the phase as their argument. But what is $\omega(k)$? To answer this, we note that the speed of a wave is given by $v = \omega/k$. For massive particles (e.g. electrons, "massive" here means "with mass" _not_ "very heavy") we can use the formula for the kinetic energy of a free particle, the de Broglie relation $p = \hbar k$ (in one dimension), and the Planck-Einstein relation $E = \hbar \omega$:

{% math() %}
K = \dfrac{1}{2} mv^2 =  \dfrac{p^2}{2m} = \dfrac{\hbar^2 k^2}{2m} = \hbar \omega
{% end %}

Rearranging gives us:

{% math() %}
\omega(k) = \dfrac{\hbar k^2}{2m}
{% end %}

And thus the wave packet solution becomes:

{% math() %}
\Psi_\text{massive}(x, t) = \dfrac{1}{\sqrt{2\pi}} \int_{-\infty}^\infty dk\, g(k) e^{i(k x -\frac{\hbar k^2}{2m} t)}
{% end %}

By contrast, for massless particles, the result is much simpler: we _always_ have $\omega(k) = kc$ for massless particles in vacuum (the situation is more complicated for particles inside a material, but we won't consider that case for now). Thus the wave packet solution becomes:

{% math() %}
\begin{align*}
\Psi_\text{massless}(x, t) &= \dfrac{1}{\sqrt{2\pi}} \int_{-\infty}^\infty dk\, g(k) e^{i(k x -kc t)} \\
&= \dfrac{1}{\sqrt{2\pi}} \int_{-\infty}^\infty dk\, g(k) e^{ik(x-ct)}
\end{align*}
{% end %}

> **Note:** This is actually identical to the solution of the classical wave equation for an electromagnetic (light) wave, providing us with our first glimpse into how quantum mechanics is related to classical mechanics. The difference is that the quantum wavefunction is a probability wave, whereas the classical wave solution is a physically-measurable wave (that you can actually see!).

Now, let's consider the case where $g(k) = \delta(k - k_0)$, where $k_0$ is a constant and is related to the particle's momentum by $p = \hbar k_0$. This physically corresponds to a particle that has an **exactly-known momentum**. We'll later see that such particles are actually physically impossible (because of something known as the Heisenberg uncertainty principle that we'll discuss later), but they serve as good mathematical idealizations for simplifying calculations. Placing the explicit form for $g(k)$ into the integral, we have:

{% math() %}
\begin{align*}
\Psi(x, t) &\approx \dfrac{1}{\sqrt{2\pi}} \int_{-\infty}^\infty dk\, \delta(k - k_0) e^{i(k x - \omega t)} \\
&= \dfrac{1}{\sqrt{2\pi}} e^{i(k_0 x - \omega _0 t)}, \quad \omega_0 = \omega(k_0)
\end{align*}
{% end %}

> **Note:** This comes from the principal identity of the Dirac delta function, which is that $\displaystyle \int_{-\infty}^\infty dx~\delta(x - x_0) f(x) = f(x_0)$.

Where the approximate equality is due to the fact that, again, particles with exactly-known momenta are physically impossible. This is (up to an amplitude factor) the **plane-wave solution** that we started with, when deriving the Schrödinger equation! From this, we have a confirmation that our derivation is indeed physically-sound and describes (idealized) quantum particles.

Now, let us consider the case where $g(k)$ is given by a Gaussian function:

{% math() %}
g(k) = \dfrac{1}{(2\pi)^{1/4} \sigma} e^{-(k-k_0)^2/4\sigma}, \quad \sigma = \text{const.}
{% end %}

This may _look_ complicated, but the constant factors are there to simplify calculations. If we substitute this into the integral, this gives us:

{% math() %}
\Psi(x, t) = \dfrac{1}{\sqrt{2 \pi \sigma}} e^{-x^2/\sigma^2}e^{i(k_0 x - \omega_0 t)}
{% end %}

This is _also_ a Gaussian function! Notice, however, that our solution now depends on a constant $\sigma$, which controls the "width" of the wave-packet. Keep this in mind - it will be very important later.

#### The classical limit of the free particle

Now, let us discuss the classical limit of the wavefunction. We know that $\Psi(x, t)$ describes some sort of probability wave (though we haven't exactly clarified what this probability is meant to represent). We can take a guess though - while quantum particles are waves (and all matter, as far as we know, behave like quantum particles at microscopic scales), classical particles are point-like. This means that they are almost 100% likely to be present at one and exactly one location in space, which is what we classically call the _trajectory_ of the particle. Thus, a classical particle would have the wavefunction approximately given by:

{% math() %}
\Psi(x, t) \sim \delta (x - vt)
{% end %}

This is a second example of the **correspondence principle**, which says that in the appropriate limits, _quantum mechanics approximately reproduces the predictions of classical mechanics_. This is important since we don't usually observe quantum mechanics in everyday life, so it has to reduce to classical mechanics (which we do observe) at macroscopic scales!

### Quantum operators

In classical mechanics, physical quantities like energy, momentum, and velocity are all given by _functions_ (typically of space and of time). For instance, the total energy of a system (more formally known as the _Hamiltonian_, see the [guide to Lagrangian and Hamiltonian mechanics](@/advanced-classical-mech/part-2.md) for more information), is given by a function $H(x, p, t)$, where $x(t)$ is the position of the particle and $p(t)$ is its momentum (roughly-speaking). However, in quantum mechanics, each physical quantity is associated with an **operator** instead of a function. For instance, there is the momentum operator $\hat p$, the position operator $\hat x$, and the Hamiltonian operator $\hat H$, where the hats (represented by the symbol $\hat{}$) tell us that these are _operators_, not functions.

So what is an operator? An operator is something that takes one vector (or function) and transforms it to another vector (or function). A good example of an operator is a transformation matrix.

#### The uncertainty principle

Heisenberg uncertainty principle means that momentum and position cannot be measured at once. It comes straight from the definition of the momentum and position operators and the fact that their commutator is nonzero.

#### Eigenstates of the momentum operator

There is another interesting characteristic of the free particle - its wavefunction is an eigenstate of the momentum operator. To see why, simply solve the eigenvalue equation for the momentum operator:

$$
\hat p \psi = i\hbar \dfrac{\partial \psi}{\partial x} = p \psi
$$

This has the straightforward solution $\psi(x) = e^{\pm ipx}$.

Momentum eigenstates are physically cannot exist, because real particles, of course, have to be _somewhere_, and by the Heisenberg uncertainty relation a pure momentum eigenstate means a particle can be _anywhere_! However, they are a good approximation in many cases to particles with a very small range of momenta.

#### Eigenstates of the position operator

#### Eigenstates of the Hamiltonian

### The Born rule

> **Born rule (for continuous quantities):** For any continuous observable represented by operator $\hat a$, with eigenstates $|\alpha\rangle$ and eigenvalues $\alpha$, the wavefunction $\psi(\alpha)$ represents the _probability amplitude_ $c(\alpha)$ of measuring the corresponding observable's value to be $\alpha$.

> **Born rule (for discrete quantities):** For any discrete (quantized) observable represented by operator $\hat a$, with eigenstates $|\alpha\rangle$ and eigenvalues $\alpha$, the wavefunction $\psi_\alpha$ represents the _probability amplitude_ $c_\alpha$ of measuring the corresponding observable's value to be $\alpha$.

### Bound and scattering states

Bound states are normalizable states, meaning that they satisfy:

$$
\int_{-\infty}^\infty |\psi(x)|^2 dx = 1
$$

This allows their squared modulus $\rho = |\psi(x)|^2$ to be interpreted as a **probability density** according to the Born rule. An essential part of a bound state is that it admits solutions to $\hat H \psi = E \psi$ where $E < 0$. This is required for the formation of bound states.

Since scattering states are not normalizable, $|\psi|^2$ _cannot_ be interpreted as a probability distribution. Instead, they are purely used for _mathematical convenience_ with the understanding that they *approximately* describe the behavior of particles that have low uncertainty in momentum and thus high uncertainty in position. Of course, real particles are described by wave packets, which are normalizable, but using plane wave solutions $\psi \sim e^{\pm ipx}$ gives a good mathematical approximation to a particle whose momentum is close to perfectly-known.

We can in fact show this as follows. Consider a free particle, described by the wave packet at $t=0$:

$$
\psi(x) = \dfrac{1}{\sqrt{2\pi}} \int_{-\infty}^\infty dp\, \phi(p)e^{ipx}
$$

Now, let us assume a Gaussian profile, such that:

$$
\phi(p) = \dfrac{1}{\sqrt{2\pi \sigma}} e^{-p^2/\sigma}, \quad \lim_{\sigma \to 0} \phi(p) = \delta(p)
$$

Where $\sigma$ is a constant that constrains the range of momenta possible: a higher value of $\sigma$ means a greater variability of the momentum. Substituting, we have:

$$
\psi(x) = \dfrac{1}{2\pi\sqrt{\sigma}} \int_{-\infty}^\infty dp\, e^{ipx- p^2/\sigma}
$$

Now, assume that the particle's momentum is confined to a **small** range of values, meaning that $\sigma$ is very small. Thus, the wavefunction would _approximately_ take the form:

$$
\psi(x) \approx \lim_{\sigma \to 0} \dfrac{1}{2\pi\sqrt{\sigma}} \int_{-\infty}^\infty dp\, e^{ipx- p^2/\sigma} = \int_{-\infty}^\infty dp\,\delta(p) e^{ipx} = e^{ipx}
$$

> **Note:** Likewise, wavefunctions of the type $\psi(x) \sim \delta(x)$ are also nonphysical, and are just mathematical approximations to highly-localized wavepackets.



## The abstract state-vector formalism

### Review of linear algebra

### Introduction to Dirac's bra-ket notation

### The state-vector and unitary time evolution

In this formalism, the quantum state is represented as a vector, called a **state-vector**, and written using Dirac notation as $|\Psi(t)\rangle$. The quantum state "lives" in a **Hilbert space** $\mathcal{H}$, which is complex-valued and can be finite or infinite-dimensional.

Now consider the state-vector at a particular moment in time, for instance, $t = 0$. Then, let $|\Psi\rangle = |\Psi(0)\rangle$ be the time-independent state-vector. We can decompose $|\Psi\rangle$ as a superposition of basis vectors $|\alpha\rangle$ as either a sum:

{% math() %}
|\Psi\rangle = \sum_i c_i |\alpha_i\rangle
{% end %}

Or as an integral:

{% math() %}
|\Psi\rangle = \int c(\alpha)|\alpha\rangle\, d\alpha
{% end %}

Such basis vectors must be the **eigenstates** of quantum-mechanical operators that represent **physical quantities** like position, momentum, energy, and spin. Discrete operators (such as spin $\hat S$) have eigenstates that are (finite-dimensional) vectors; continuous operators (such as position $\hat x$ and momentum $\hat p$) have eigenstates that are continuous functions (alternatively, infinite-dimensional vectors). The **eigenvalues** of such operators are the possible measurable values of the operator (such as possible energies or momenta of a particle); meanwhile, the coefficients $c_i$ (in the discrete case) and $c(\alpha)$ in the continuous case are interpreted as **probability amplitudes**. One can then find the **probability** of measuring the $i$-th eigenvalue of a discrete operator with:

{% math() %}
P = |c_i|^2, \quad c_i = \langle \alpha_i|\psi\rangle
{% end %}

In the continuous case, the probability amplitude $c(\alpha) = \langle \alpha|\psi\rangle$ becomes a continuous function (equivalently, an _infinite-dimensional vector_), which is called the **wavefunction**, and denoted $\psi(\alpha)$. one may obtain the **probability density** $\rho$ of measuring eigenvalue $\alpha$ with:

{% math() %}
\rho = |\psi(\alpha)|^2 = \psi(\alpha)\psi^*(\alpha)
{% end %}

Collectively, these two formulas are known as the **Born rule**. In the case of the position operator $\hat x$, the eigenvalues of the position $\hat x$ are possible positions $x$, and eigenstates are position eigenstates $|x\rangle$. Thus, the wavefunction takes the form $\psi(x)$, and by the Born rule, taking its squared norm $|\psi|^2$ gives the **probability per unit volume** of measuring a particle at position $x$.

And it is not only the probabilities of positions that we are able to calculate. Recall that while we chose the position basis for the wavefunction, there is no reason why we are restricted to just the position basis. We can define a wavefunction in any orthonormal basis we would like in quantum mechanics, so wavefunctions that are a function of momentum $\psi(p)$ (or any other continuous basis) are also perfectly valid.

---

For instance, the probability a particle is in its $|E_1 \rangle$ state corresponding to having an energy of $E_1$ is given by;

{% math() %}
P = \Psi_1 \Psi_1^*
{% end %}

Recall that the Schrödinger equation is given by:

{% math() %}
i \hbar \frac{\partial}{\partial t} | \Psi \rangle = \hat H | \psi \rangle
{% end %}

And remember Newton's 2nd law as the key equation governing how a classical state can evolve? Quantum states evolve too, but under a partial differential equation called the **Schrödinger equation**:

{% math() %}
i \hbar \frac{\partial}{\partial t} | \Psi \rangle = \hat H | \psi \rangle
{% end %}

Where $\hat H$ can be thought of as a type of matrix that acts on the state-vector $| \Psi \rangle$. What is its physical interpretation? That is what we'll see in the next section.



{% math() %}
E | \Psi \rangle = \hat H | \psi \rangle
{% end %}

Where $E$ is a constant associated with, understandably, the energy. This form is easier to solve, and can be used to find explicit analytical solutions for a variety of quantum systems.

Thus the Schrödinger wave equation simplifies to something far more familiar, a partial differential equation:

{% math() %}
i\hbar \frac{\partial}{\partial t} \psi(x, t) = \left(-\frac{\hbar^2}{2m} \frac{\partial^2}{\partial x^2} + V(x, t)\right) \psi(x, t) 
{% end %}

{% math() %}
\psi(x) = \langle x | \Psi \rangle \Rightarrow \psi(p) = \langle p | \Psi \rangle 
{% end %}

## Intrinsic spin

### What exactly is intrinsic spin?

"Intrinsic spin" (or just _spin_) is a shortened version of "intrinsic spin angular momentum", which is what we're _really_ talking about when we say "spin" - a form of angular momentum that is a fundamental property of subatomic particles, like protons and electrons.

### The Stern-Gerlach experiment

### Application to electronics

Cover content in <https://en.wikipedia.org/wiki/Spintronics>.

## Advanced quantum theory

### Relativistic wave equations and the Dirac equation

Thus, we arrive at the Dirac equation for a **free particle**:

{% math() %}
(i\hbar \gamma^\mu \partial_\mu - mc)\psi = 0
{% end %}

The Dirac equation with the electromagnetic four-potential $A_\mu = (A_0, \mathbf{A}) = (\frac{1}{c} V, \mathbf{A})$ takes a very similar form, except the partial derivative $\partial_\mu$ is replaced by a new differential operator $D_\mu$:

{% math() %}
(i\hbar \gamma^\mu D_\mu - mc)\psi = 0, \quad D_\mu = \partial_\mu + \dfrac{ie}{\hbar} A_\mu
{% end %}

### Second quantization and quantum electrodynamics

In this section, we will not analyze the _full_ relativistic theory of quantum electrodynamics. For that, see my [quantum field theory book](https://www.learntheoreticalphysics.com/quantum-field-theory/). Rather, we will discuss the non-relativistic theory of quantum electrodynamics (often referred to as NRQED for short), which nonetheless has many applications, including quantum optics and quantum information theory.

The process of going from _classical_ electrodynamics to _quantum_ electrodynamics is called **second quantization**, a term to differentiate it from **first quantization**, where we take classical variables (e.g. position, momentum, and angular momentum) and translate them into quantum operators.

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

### Relativity, the Dirac equation, and the road to QFT

Unfortunately, the Dirac equation, despite its successes, has limited applicability. Why? Primarily, because at the relativistic energies it describes, new particles can be created from pure energy (remember Einstein's famous equation $E = mc^2$, this means that a particle of mass $m$ can be created from energy $E$ if $E/c^2 > m$). Additionally, particles can annihilate with each other and be destroyed, and particles can turn into new (and often different types of) particles. The number of particles is never constant - new particles are being created all the time, and old particles are getting annihilated or turn into new particles. This makes the utility of a quantum wave equation that describes fixed numbers of particles rather limited; after a few nanoseconds (or shorter still), the electron you were describing no longer exists, and its wavefunction also vanishes.

### The emergence of field quanta

Quantum field theory tells us that all matter in the Universe is composed of quantum fields. These fields are said to be _quantized_ as they can only oscillate between distinct states. Mathematically, this corresponds to quantum fields being _operator-valued_ as opposed to classical fields, which are functions of space and time.


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
E_\text{total} = \int d^3 \omega\, E_\omega = \sum_k E_k
{% end %}

### Second quantization

Action principle, etc. and then also link to the [advanced classical mechanics guide](@/advanced-classical-mech/index.md) for an overview of tensors and the Euler-Lagrange equations.

To go from classical field theory to quantum field theory:

- Classical equations of motion become _operator_ equations motion (that look the same but have very different properties)
- Classical plane-wave solutions to the field equations become single-particle states of the fields
- Fields have a nonzero energy even when in their lowest-energy state
- Classical oscillating fields become coupled quantum harmonic oscillators


### The spin-statistics theorem