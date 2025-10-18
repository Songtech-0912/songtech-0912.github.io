+++
title = "In-Depth Quantum Mechanics"
date = 2025-08-31
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
\Psi(x, t) = \dfrac{1}{\sqrt{2\pi}} \int_{-\infty}^\infty dk~ g(k) e^{i(k x - \omega(k) t)}
{% end %}

This is known as a **wave packet**, since it is a superposition of multiple waves and in fact it  looks like a bundle of waves (as shown by the animation below)!

![Wavepacket animation, showing a "pulse" propagating along the positive x-axis](https://upload.wikimedia.org/wikipedia/commons/d/d8/Wave_packet_propagation_%28phase_faster_than_group%2C_nondispersive%29.gif)

_Source: [Wikipedia](https://en.m.wikipedia.org/wiki/File:Wave_packet_propagation_(phase_faster_than_group,_nondispersive).gif)_

> **Reader's note:** Another nice animation can be found at [this website](https://www.cond-mat.de/teaching/QM/JSim/wpack.html).

Note that $g(k)$ is an arbitrary function that is determined by the initial conditions of the problem. In particular, using Fourier analysis we can show that it is given by:

{% math() %}
g(k) = \dfrac{1}{\sqrt{2\pi}} \int_{-\infty}^\infty dx ~\Psi(x, 0) e^{-ikx}
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
\Psi_\text{massive}(x, t) = \dfrac{1}{\sqrt{2\pi}} \int_{-\infty}^\infty dk~ g(k) e^{i(k x -\frac{\hbar k^2}{2m} t)}
{% end %}

By contrast, for massless particles, the result is much simpler: we _always_ have $\omega(k) = kc$ for massless particles in vacuum (the situation is more complicated for particles inside a material, but we won't consider that case for now). Thus the wave packet solution becomes:

{% math() %}
\begin{align*}
\Psi_\text{massless}(x, t) &= \dfrac{1}{\sqrt{2\pi}} \int_{-\infty}^\infty dk~ g(k) e^{i(k x -kc t)} \\
&= \dfrac{1}{\sqrt{2\pi}} \int_{-\infty}^\infty dk~ g(k) e^{ik(x-ct)}
\end{align*}
{% end %}

> **Note:** This is actually identical to the solution of the classical wave equation for an electromagnetic (light) wave, providing us with our first glimpse into how quantum mechanics is related to classical mechanics. The difference is that the quantum wavefunction is a probability wave, whereas the classical wave solution is a physically-measurable wave (that you can actually see!).

Now, let's consider the case where $g(k) = \delta(k - k_0)$, where $k_0$ is a constant and is related to the particle's momentum by $p = \hbar k_0$. This physically corresponds to a particle that has an **exactly-known momentum**. We'll later see that such particles are actually physically impossible (because of something known as the Heisenberg uncertainty principle that we'll discuss later), but they serve as good mathematical idealizations for simplifying calculations. Placing the explicit form for $g(k)$ into the integral, we have:

{% math() %}
\begin{align*}
\Psi(x, t) &\approx \dfrac{1}{\sqrt{2\pi}} \int_{-\infty}^\infty dk~ \delta(k - k_0) e^{i(k x - \omega t)} \\
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

This is _also_ a Gaussian function! Notice, however, that our solution now depends on a constant $\sigma$, which controls the "width" of the wave-packet. We will soon learn that it physically corresponds to the _uncertainty in position_ of the quantum particle. Keep this in mind - it will be very important later.

#### The classical limit of the free particle

Now, let us discuss the classical limit of the wavefunction. We know that $\Psi(x, t)$ describes some sort of probability wave (though we haven't exactly clarified what this probability is meant to represent). We can take a guess though - while quantum particles are waves (and all matter, as far as we know, behave like quantum particles at microscopic scales), classical particles are point-like. This means that they are almost 100% likely to be present at one and exactly one location in space, which is what we classically call the _trajectory_ of the particle. Thus, a classical particle would have the wavefunction approximately given by:

{% math() %}
\Psi(x, t) \sim \delta (x - vt)
{% end %}

This is a second example of the **correspondence principle**, which says that in the appropriate limits, _quantum mechanics approximately reproduces the predictions of classical mechanics_. This is important since we don't usually observe quantum mechanics in everyday life, so it has to reduce to classical mechanics (which we do observe) at macroscopic scales!

### Interlude: the Fourier transform

In our analysis of the free quantum particle, we relied on a powerful mathematical tool: the **Fourier transform**. The Fourier transform allows us to decompose complicated functions as a sum of complex exponentials $e^{\pm ikx}$. It gives us a straightforward way to relate a particle's wavefunction in terms of its possible momenta, and vice-versa.

A confusing fact in physics is that there are actually _two_ common conventions for the Fourier transform. The first convention, often used in electromagnetism, writes the 1D Fourier transform and inverse Fourier transform (in $k$-space, or loosely called *frequency space*) as:

{% math() %}
\tilde f(k) = \dfrac{1}{2\pi} \int_{-\infty}^\infty f(x)e^{-ikx} dx, \quad f(x) = \dfrac{1}{2\pi} \int_{-\infty}^\infty dk \tilde f(k) e^{ikx}
{% end %}

Or equivalently, for $N$ spatial dimensions:

{% math() %}
f(k) = \dfrac{1}{(2\pi)^N} \int_{-\infty}^\infty d^n k ~\tilde f(x)e^{-i\vec k \cdot \vec x}, \quad f(x) = \dfrac{1}{(2\pi)^N} \int_{-\infty}^\infty d^n k ~\tilde f(k)e^{i\vec k \cdot \vec x}
{% end %}

The other convention, more commonly used in quantum mechanics, writes the 1D Fourier transform as:

{% math() %}
\tilde f(k) = \dfrac{1}{\sqrt{2\pi}} \int_{-\infty}^\infty f(x)e^{-ikx} dx, \quad f(x) = \dfrac{1}{\sqrt{2\pi}} \int_{-\infty}^\infty dk \tilde f(k) e^{ikx}
{% end %}

The equivalent for $N$ spatial dimensions in this convention is given by:

{% math() %}
f(k) = \dfrac{1}{(2\pi)^{N/2}} \int_{-\infty}^\infty d^n k ~\tilde f(x)e^{-i\vec k \cdot \vec x}, \quad f(x) = \dfrac{1}{(2\pi)^{N/2}} \int_{-\infty}^\infty d^n k ~\tilde f(k)e^{i\vec k \cdot \vec x}
{% end %}

For reasons we'll see, $k$-space in quantum mechanics is directly related to _momentum space_. We will stick with the quantum-mechanical convention (unless otherwise stated) for the rest of this guide.

### Another look at the wave packet

Recall that our wave packet solution was given by a continuous sum of plane waves, that is:

{% math() %}
\Psi(x, t) = \int_{-\infty}^\infty dk~ g(k) e^{i(kx - \omega(k) t)}
{% end %}

> **Note:** Throughout this guide we will frequently omit the integration bounds from $-\infty$ to $\infty$ for simplicity. Unless otherwise specified, you can safely assume that any integral written without bounds is an integral over all space (that is, over $-\infty < x < \infty$).

Performing its Fourier transform yields:

{% math() %}
\Psi(x, 0) = \dfrac{1}{\sqrt{2\pi}} \int g(k) e^{ikx} ~ dk, \quad g(k) = \dfrac{1}{\sqrt{2\pi}} \int \Psi(x', 0) e^{-ikx'}dx'
{% end %}

Let us verify this calculation by now taking the inverse Fourier transform:

{% math() %}
\begin{align*}
\Psi(x, 0) &= \dfrac{1}{2\pi} \int dk \int dx' \Psi(x', 0) e^{ik(x - x')} \\
&= \dfrac{1}{2\pi} \int dx' \Psi(x', 0) \underbrace{\int dk e^{ik(x - x')}}_{= 2\pi \delta(x - x')} \\
&= \dfrac{1}{2\pi} \int dx' \Psi(x', 0) [2\pi \delta(x - x')] \\
&= \Psi(x, 0)
 \end{align*}
{% end %}

Where we used the Dirac function identity that $\displaystyle \int f(x')\delta(x - x') dx' = f(x)$ and the fact that the Fourier transform of $e^{ik(x - x')}$ is a delta function.

### The Heisenberg uncertainty principle

We're now ready to derive one of the most mysterious results of quantum mechanics: the **Heisenberg uncertainty principle**. There are a billion different ways to derive it, but the derivation we'll use is a more formal mathematical one (feel free to skip to the end of this section if this is not for you!). To start, we'll use the **Bessel-Parseval relation** from functional analysis, which requires that:

{% math() %}
\int_{-\infty}^\infty dx |\Psi(x, 0)|^2 = 1 = \int dk|g(k)|^2
{% end %}

Using the de Broglie relation $p = \hbar k \Rightarrow k = p/\hbar$ we may perform a change of variables for the integral; using $dk = dp/\hbar$, and thus:

{% math() %}
\int dk|g(k)|^2 = \dfrac{1}{\hbar}\int dp|\underbrace{g(k)/\hbar|^2}_{|\tilde \Psi(p)|^2}  = 1
{% end %}

This allows us to now write our Fourier-transformed expressions for $\Psi(x, 0)$, which were in **position-space** (as they depended on $x$), now in **momentum space** (depending on $p$):

{% math() %}
\begin{align*}
\underbrace{\Psi(x, 0)}_{\psi(x)} &= \dfrac{1}{\sqrt{2\pi \hbar}} \int dp~\tilde \psi(p) e^{ipx/\hbar} \\
\tilde \psi(p) &= \dfrac{1}{\sqrt{2\pi \hbar}} \int dx~ \Psi(x, 0) e^{-ipx/\hbar}
\end{align*}
{% end %}

Recognizing that $\Psi(x, 0) = \psi(x)$ (the time-independent wavefunction) we may equivalently write:

{% math() %}
\begin{align*}
\psi(x) &= \dfrac{1}{\sqrt{2\pi \hbar}} \int dp~\tilde \psi(p) e^{ipx/\hbar} \\
\tilde \psi(p) &= \dfrac{1}{\sqrt{2\pi \hbar}} \int dx~ \psi(x) e^{-ipx/\hbar}
\end{align*}
{% end %}

Where $\tilde{\psi}(p)$ (also confusingly often denoted $\psi(p)$) is called the **momentum-space wavefunction**, and is the Fourier transform of the position-space wavefunction!

> **Note:** It is a common (and extremely confusing!) convention in physics to represent the Fourier transform of a function with the same symbol. That is, it is common to write that the Fourier transform of $\psi(x)$ as simply $\psi(p)$ as opposed to a different symbol (like here, where we use $\tilde \psi(p)$). Due to its ubiquity in physics, we will adopt this convention from this time forward. However, remember that $\psi(x)$ and $\psi(p)$ are actually **distinct functions** that are Fourier transforms of each other, not the same function!

## Exact solutions of the Schrödinger equation

We'll now solve the Schrödinger equation for a greater variety of systems that have _exact solutions_. Since exact solutions to the Schrödinger equation are quite rare, these are systems that definitely worth studying! To start, recall that the Schrödinger equation reads:

{% math() %}
i\hbar \dfrac{\partial}{\partial t} \Psi(x, t) = -\dfrac{\hbar^2}{2m} \nabla^2\Psi + V\Psi
{% end %}

Now, the potential $V$ in the Schrödinger equation can be any function of space and time - that is, in general, $V = V(x, t)$. However, in practice, it is much easier to first start by considering only **stationary states** - that is, time-independent potentials. Thus, the Schrödinger equation now reads:

{% math() %}
i\hbar \dfrac{\partial}{\partial t} \Psi(x, t) = -\dfrac{\hbar^2}{2m} \nabla^2\Psi + V(x)\Psi
{% end %}

We will now explain a way to write out a **general solution** of the Schrödinger equation. But how is this possible? The reason why is that the Schrödinger equation is a **linear partial differential equation (PDE)**. Thus, as can be proven in it is possible to sum individual solutions together to arrive at the general solution for the Schrödinger equation for any time-independent problem.

Let us start by assuming that the wavefunction $\Psi(x, t)$ in one dimension can be written as the product $\Psi(x, t) = \psi(x) T(t)$. We can now use the method of **separation of variables**. To do so, we note that:

{% math() %}
\begin{align*}
(\nabla^2 \Psi)_\text{1D} &= \dfrac{\partial^2 \Psi}{\partial t^2} = T(t) \dfrac{\partial^2}{\partial x^2} \psi(x) = \psi''(x) T(t) \\
\dfrac{\partial \Psi}{\partial t} &= \psi(x) \dfrac{\partial^2}{\partial t^2} T(t) = \dot T(t) \psi(x)
\end{align*}
{% end %}

We will now use the shorthand $\psi'' = \psi''(x)$ and $\dot T = \dot T(t)$. Thus the Schrödinger equation becomes:

{% math() %}
i\hbar(\psi \dot T)  = -\dfrac{\hbar^2}{2m}\psi'' T + V(x)\psi T
{% end %}

If we divide by $\psi T$ from all sides we obtain:

{% math() %}
\begin{align*}
\dfrac{1}{\psi T} \left[i\hbar(\psi \dot T)\right] &= \dfrac{1}{\psi T}\left[-\dfrac{\hbar^2}{2m}\psi'' T + V(x)\psi T\right] = i\hbar \dfrac{\dot T}{T} \\
&= -\dfrac{\hbar^2}{2m} \dfrac{\psi''}{\psi} + V \\
&= E
\end{align*}
{% end %}

Where $E$ is *some* constant that we don't know the precise form of yet (if this is not making sense, you may want to review the [PDEs guide](@/intro-pdes/index.md)), and the reason it is a constant is that two combinations of derivatives (here, $\dot T/T$ and $\psi''/\psi$) can only be equal if they are both equal to a constant. Thus, if we multiply through by $\psi$, we have now reduced the problem of finding $\Psi(x, t)$ to solving 2 simpler differential equations:

{% math() %}
\begin{align*}
-\dfrac{\hbar^2}{2m} \psi'' + V\psi = E\psi \\
i\hbar \dfrac{dT}{dt} = E~ T(t)
\end{align*}
{% end %}

The second ODE is trivial to solve; its solution is given by plane waves in time, that is, $T(t) \sim e^{-iEt/\hbar}$. The first, however, is not so easy to solve, as we need to know what $V$ is given by, and there are some complicated potentials out there! However, we do know that once we have $\psi(x)$ (often called the **time-independent wavefunction** since it represents $\Psi(x, t)$ at a "snapshot" in time), then the full wavefunction $\Psi(x)$ is simply:

{% math() %}
\Psi(x, t) = \psi(x) e^{-iEt/\hbar}
{% end %}

But if $\psi(x)$ is one solution, it must be true that $c_1 \psi(x) + c_2 \psi(x)$ must also be a solution, and thus summing *any number of solutions* can be used to construct an arbitrary solution. This is what we mean by saying that we have found the **general solution** to the Schrödinger equation (at least for stationary problems, i.e. $V = V(\mathbf{x})$ and is time-independent) by just summing different solutions together! Thus, solving the ODE for $\psi(x)$ is often called the **time-independent Schrödinger equation**, and it is given by:

{% math() %}
-\dfrac{\hbar^2}{2m} \dfrac{d^2 \psi}{dx^2} + V(x)\psi = E\psi
{% end %}

The **most general form** of the time-independent Schrödinger equation holds in two and three dimensions as well, and is given by:

{% math() %}
\left(-\dfrac{\hbar^2}{2m} \nabla^2 + V(\mathbf{x})\right) \psi = E\psi
{% end %}

Consider several solutions $\psi_1, \psi_2, \psi_3, \dots \psi_n$ of the time-independent Schrödinger equation. Due to its linearity (as we discussed previously), a weighted sum of these solutions forms a **general solution**, given by:

{% math() %}
\psi(x) = \sum_{n = 1}^\infty c_n \psi_n(x), \quad c_n = \text{const.}
{% end %}

If we back-substitute each individual solution into the time-independent Schrödinger equation, we find that the right-hand side $E$ takes distinct values $E_1, E_2, E_3, \dots E_n$. Using the fact that $\Psi(x, t) = \psi(x) T(t)$, we obtain the most general form of the solution to the Schrödinger equation:

{% math() %}
\Psi(x, t) = \sum_{n = 1}^\infty c_n \psi_n(x) e^{-iE_n t/\hbar} \quad \quad c_n, E_n = \text{const.}
{% end %}

This solution is *very general* since does not require us to specify $\psi_n$ and $E_n$; indeed, this general solution is correct for *any* set of solutions $\psi_n$ of the time-independent Schrödinger equation\*. Of course, this form tells us very little about what the $c_n$'s or what the $\psi_n$'s should be. Finding the correct components $c_n$ highly depends on the initial and boundary conditions of the problem, without which it is impossible to determine the form of $\Psi(x, t)$. In the subsequent sections, we will explore a few simple cases where an analytical solution can be found.

> \*: There are some assumptions underlying this claim, without which it is not strictly true; we'll cover the details later. For those interested in knowing why right away, the reason is that $\Psi(x, t)$ should actually be understood as a **vector** in an infinite-dimensional space, and $c_n$ are its components when expressed in a particular basis, whose basis vectors are given by $\psi_n$. Since vectors are basis-independent it is possible to write $\Psi(x, t)$ in terms of any chosen basis $\psi_n$ with the appropriate components $c_n$, assuming $\psi_n$ is an orthogonal and complete set of basis vectors.

### Bound and scattering states

Solving the Schrödinger equation can be extremely difficult, if not impossible. Luckily, we often don't need to solve the Schrödinger equation to find information about a quantum system! The key is to focus on the potential $V(x)$ in the Schrödinger equation, which tells us that a solution to the Schrödinger equation comes in one of two forms: **bound states** or **scattering states**.

Roughly speaking, a **bound state** is a state where a particle is in a stable configuration, as it takes more energy to remove it from the system than keeping it in place. Meanwhile, a **scattering state** is a state where a particle is in an inherently unstable configuration, as it takes more energy to keep the particle in place than letting it slip away. Thus, bound states are situations where quantum particle(s) are _bound_ by the potential, while scattering states are situations where quantum particles are _unbound_ and are free to move. A particle in a bound state is essentially trapped in place by a potential; a particle in a scattering state, by contrast, is deflected (but not trapped!) by a potential, a collective phenomenon known as **scattering**.

At its heart, the difference between a bound state and a scattering state is in the *total energy* of a particle. A bound state occurs when the energy $E$ of a particle satisfies $E < V$ for all $x$. A scattering state occurs when $E \geq V$ for all $x$. One may show this by doing simple algebraic manipulations on Schrödinger equation. A short sketch of this proof (as explained by [Shi, 2025](https://faculty.rpi.edu/jian-shi)) is as follows. First, note that the Schrödinger equation in one dimension can be rearranged and written in the form:

{% math() %}
\dfrac{d^2\psi}{dx^2} = -\dfrac{2m}{\hbar^2} (E  - V)\psi = \dfrac{2m}{\hbar^2} (V - E)\psi
{% end %}

When $E < V$, the second derivative of the wavefunction is positive for all $x$. This means that at far distances, the Schrödinger equation approximately takes the form $\psi'' \approx \beta^2 \psi$ (where $\beta = \frac{\sqrt{2m}}{\hbar} (V(\infty) - E)$ is approximately a constant). This has solutions for $x > 0$ in terms of *real* exponentials $e^{-\beta x}$, so the wavefunction decays to infinity and is normalizable, and we have a **bound state**. Meanwhile, when $E > V$, the second derivative of the wavefunction is negative for all $x$. This means that are far distances, the Schrödinger equation approximately takes the form $\psi'' \approx - \beta^2 \psi$. This has solutions for $x>0$ in terms of _complex exponentials_ $e^{-i\beta x}$, so the wavefunction continues oscillating even at infinity and _never_ decays to zero. This means that the wavefunction is non-normalizable, and we have a **scattering state**. In theory, the means that scattering-state wavefunctions are unphysical, though in practice we can ignore the normalizability requirement _as long as_ we are aware that we're using a highly-simplified approximation.

### Normalizability

To understand another major difference between bound and scattering states, we need to examine the concept of **normalizability**. Bound states are normalizable states, meaning that they satisfy the **normalization condition**:

{% math() %}
\int_{-\infty}^\infty |\psi(x)|^2 dx = 1
{% end %}

This allows their squared modulus $\rho = |\psi(x)|^2$ to be interpreted as a **probability density** according to the Born rule. An essential part of a bound state is that it admits solutions to $\hat H \psi = E \psi$ where $E < 0$. This is required for the formation of bound states: the bound-state energy must be *negative* so that the system is stable.

However, scattering states are not necessarily normalizable. In theory, particles undergoing scattering should be described by wave packets. In practice, this leads to unnecessary mathematical complexity. Instead, it is common to use the **non-normalizable** states, typically in the form of plane waves:

{% math() %}
\psi(x) = A e^{\pm ipx/\hbar}
{% end %}

Since these scattering states are not normalizable, $|\psi|^2$ _cannot_ be interpreted as a probability distribution. Instead, they are purely used for _mathematical convenience_ with the understanding that they *approximately* describe the behavior of particles that have low uncertainty in momentum and thus high uncertainty in position. Of course, real particles are described by wave packets, which are normalizable, but using plane waves gives a good mathematical approximation to a particle whose momentum is close to perfectly-known.

We can in fact show this as follows. Consider a free particle at time $t = 0$, described by the wave packet solution, which we've seen at the beginning of this guide:

{% math() %}
\psi(x) = \Psi(x, 0) = \dfrac{1}{\sqrt{2\pi \hbar}} \int dp'~\overline \Psi(p') e^{ip'x/\hbar}
{% end %}

> **Note:** We changed the integration variable for the wavepacket from $p$ to $p'$ to avoid confusion later on. The integral expressions, however, are equivalent.

Now, assume that the particle's momentum is confined to a **small** range of values, or equivalently, has a **low uncertainty in momentum**. We can thus make the approximation that $\overline \Psi(p') \approx \delta(p - p')$, where $p$ is the particle's momentum. Thus, performing the integration, we have:

{% math() %}
\psi(x) \approx \dfrac{1}{\sqrt{2\pi \hbar}} \int dp'~ \delta(p - p') e^{ip'x/\hbar} \sim \dfrac{1}{\sqrt{2\pi}} e^{ipx/\hbar} 
{% end %}

This is exactly a plane wave in the form $\psi(x) = Ae^{ipx/\hbar}$, and a momentum eigenstate! Thus we come to the conclusion that while momentum eigenstates $\psi \sim e^{\pm ipx/\hbar}$ are non-normalizable and thus unphysical, they are a good approximation for describing particles with low uncertainty in momentum.

Likewise, wavefunctions of the type $\psi(x) \sim \delta(x-x_0)$ are also unphysical, and are just mathematical approximations to highly-localized wavepackets, where the particles' uncertainty in position is very small. Thus, we conclude that eigenstates of the position operator (which are delta functions) are also non-normalizable, which makes sense, since there is no such thing as a particle with exactly-known position (or momentum!).

### The particle in a box

We will now consider our first example of a **bound state**: a quantum particle confined within a small region by a step potential, also called the **particle in a box** or the **square well**. Despite its (relative) simplicity, the particle in a box is the basis for the [Fermi gas model](https://en.wikipedia.org/wiki/Fermi_gas) in solid-state physics, so it is very important! (It is also used in describing [polymers](https://en.wikipedia.org/wiki/Conjugated_system), [nanometer-scale semiconductors](https://en.wikipedia.org/wiki/Quantum_dot), and [quantum well lasers](https://en.wikipedia.org/wiki/Quantum_well_laser), for those curious), for those curious). The particle in a box is described by the potential:

{% math() %}
\begin{align*}
V(x) = \begin{cases}
V_0, & x < 0 \\
0, & 0 \leq x \leq L \\
V_0, & x > L
\end{cases}
\end{align*}
{% end %}

> **Note:** it is often common to use the convention that $V = 0$ for $x < 0$ and $x > L$ and $V = -V_0$ in the center region ($0 \leq x \leq L$). These two are **entirely equivalent** since they differ by only a constant energy ($V_0$) and we know that adding a constant to the potential does not change any of the physics.

We show a drawing of the box potential below:


{{ diagram(
	desc="A diagram of the square well, where a particle is constrained to move between two potential barriers"
	src="particle-square-well.excalidraw.svg"
) }}

We assume that the particle has energy $E < V_0$, meaning that it is a **bound state** and the particle is contained within the well. To start, we'll only consider the case where $V_0 \to \infty$, often called an **infinite square well**. This means that the particle is *permanently trapped* within the well and cannot possibly escape. In mathematical terms, it corresponds to the **boundary condition** that:

{% math() %}
\begin{align*}
\psi(x) \to 0, \quad x < 0 \\
\psi(x) \to 0, \quad x> L
\end{align*}
{% end %}

Equivalently, we can write these boundary conditions in more standard form as:

{% math() %}
\psi(0) = \psi(L) = 0
{% end %}

In practical terms, it simplifies our analysis so that we need only consider a *finite interval* $0 \leq x \leq L$ rather than the *infinite domain* $-\infty < x < \infty$, simplifying our normalization requirement.

#### Solving the Schrödinger equation for the infinite square well

To start, we'll use the tried-and-true method to first assume a form of the wavefunction as:

{% math() %}
\psi(x) = Ae^{ikx} + A' e^{-ikx}
{% end %}

Where $A$ is some normalization faction that we will figure out later. This may *seem* unphysical (since it's made of plane waves), but it is not actually so. The reason why is that if we pick $A' = -A$, Euler's formula $e^{i\phi} = \cos \phi + i\sin \phi$ tells us that:

{% math() %}
\begin{align*}
\psi(x) &= Ae^{ikx} - Ae^{-ikx} \\
&= A(e^{ikx} - e^{-ikx}) \\
&= A(\cos k x + i \sin k x - \underbrace{\cos (-kx)}_{\cos(-\theta) = \cos \theta} - \underbrace{i\sin(-kx)}_{\sin(-\theta) = -\sin \theta}) \\
&= A (\cos kx - \cos k x + i \sin k x - (-i \sin k x)) \\
&= A (i\sin kx + i\sin k x + \cancel{\cos k x - \cos k x}^0) \\
&= \beta\sin k x, \qquad \beta = 2A i
\end{align*}
{% end %}

We notice that $\psi(x) \sim \sin(kx)$ automatically satisfies $\psi(0) = 0$, which tells us that we're on the right track! Additionally, since cosine is a bounded function over a finite interval, we know it is a normalizable (and thus physically-possible) solution. However, we still need to find $k$ and the normalization factor $\beta = 2Ai$, which is what we'll do next.

Let's first start by finding $k$. Substituting our boundary condition $\psi(L) = 0$, we have:

{% math() %}
\psi(L) = \beta \sin(k L) = 0
{% end %}

Since the sine function is only zero at intervals of $n\pi = 0, \pi, 2\pi, 3\pi, \dots$ (where $n$ is an integer), our above equation can only be true if $kL = n\pi$. A short rearrangement then yields $k = n\pi/L$, and thus:

{% math() %}
\psi(x) = \beta \sin \dfrac{n\pi}{L}
{% end %}

To find $\beta$, we use the normalization condition:

{% math() %}
\begin{align*}
1  &= \int_{-\infty}^\infty \psi(x)\psi^* (x) dx \\
&= \underbrace{\int_{-\infty}^0 \psi(x)^2 dx}_{0} + \int_{0}^L \psi(x)^2 dx + \underbrace{\int_L^\infty \psi(x)^2 dx}_0 \\
&= \underbrace{-4A^2}_{\beta^2} \int_{0}^L \sin^2 \left(\dfrac{n\pi x}{L}\right)dx \\
&= A^2 L/2
\end{align*}
{% end %}

Where we used the integral property:

{% math() %}
\int_a^b \sin^2 \beta x = \left[\dfrac{x}{2} - \dfrac{\sin(2\beta x)}{4\beta}\right]_a^b
{% end %}

From our result, we can solve for $A$:

{% math() %}
A^2 L/2 = 1 \quad \Rightarrow \quad A = \sqrt{\dfrac{2}{L}}
{% end %}

From which we obtain our **position-space wavefunctions**:

{% math() %}
\psi(x) = \sqrt{\frac{2}{L}} \sin \left(\dfrac{n\pi x}{L}\right), \quad n =1, 2, 3, \dots
{% end %}

We note that a solution is present for every value of $n$. This means that we have technically found an infinite family of solutions $\psi_1, \psi_2, \psi_3, \dots, \psi_n$, each parameterized by a different value of $n$. We show a few of these solutions in the figure below:

![Graphical plot of the wavefunction for the infinite square well](https://www.researchgate.net/publication/337259777/figure/fig5/AS:961466974879768@1606242998239/A-graphical-representation-of-the-particle-in-a-box-as-solution-of-the-time-independent.png)

_Source: [ResearchGate](https://www.researchgate.net/figure/A-graphical-representation-of-the-particle-in-a-box-as-solution-of-the-time-independent_fig5_337259777). Note that the vertical position of the different wavefunctions is for graphical purposes only._

#### Energy of particle in a box

Now that we have the wavefunctions, we can solve for the possible values of the energies. We can find this by plugging in our solution into the time-independent Schrödinger equation:

{% math() %}
-\dfrac{\hbar^2}{2m}\dfrac{d^2 \psi}{dx^2} = E \psi(x)
{% end %}

Upon substituting, we have:

{% math() %}
\begin{align*}
-\dfrac{\hbar^2}{2m}\dfrac{d^2 \psi}{dx^2} &= -\frac{\hbar^2}{2m} \left(-\frac{n^2 \pi^2}{L^2}\right) \sqrt{\dfrac{2}{L}} \sin \dfrac{n\pi x}{L} \\
&= \underbrace{\dfrac{n^2 \pi^2 \hbar^2}{2mL^2} \psi(x)}_{E \psi}
\end{align*}
{% end %}

From which we can easily read off the energy to be:

{% math() %}
E_n = \dfrac{n^2 \pi^2 \hbar^2}{2mL^2}, \quad n = 1, 2, 3, \dots
{% end %}

We find that the particle always has a nonzero energy, even in its ground state. The lowest energy is called its **ground-state energy**, and the reason it is nonzero is that the energy-time uncertainty principle forbids a particle to have zero energy.

> **Note for the advanced reader:** Quantum field theory gives the complete explanation for why a particle can have nonzero energy even in its ground state. The reason is that the vacuum in quantum field theory is never empty; spontaneous energy fluctuations in the vacuum lead to a nonzero energy even in the ground state, and it would take an infinite amount of energy (or equivalently, infinite time) to suppress all of these fluctuations.

### The rectangular potential barrier

We will now tackle solving our first **scattering-state problem**, the famous problem of the **particle at a potential barrier** (which is a simple model that can be used to model, among other things, the mechanics of [scanning electron microscopes](https://en.wikipedia.org/wiki/Scanning_tunneling_microscope)). In this example, a quantum particle with energy $E$ is placed at some position in a potential given by:

{% math() %}
V(x) = \begin{cases} 
0 & x < 0 \\ 
V_0 & x > 0 \end{cases}, \quad E > V
{% end %}

(Note that the discontinuity in the potential at $x = 0$ is unimportant to the problem, although it is convenient to define $V(0) = V_0/2$). You can think of this as a quantum particle hitting a quantum "wall" of sorts; the potential blocks its path and changes its behavior, although what the particle does next defies classical intuition completely.

To solve this problem, we split it into two parts. For the first part, we assume that the particle initially starts from the left (that is, $x = -\infty$) and moves towards the right. This means that the particle can only be found at $x < 0$. Then, the particle's initial wavefunction can (approximately) be represented as a free particle with a plane wave:

{% math() %}
\psi_I(x) = e^{ikx}, \quad x < 0, \quad k = \frac{p}{\hbar} = \dfrac{\sqrt{2mE}}{\hbar}
{% end %}

Where $\psi_I$ denotes the _initial_ wavefunction (that is, the particle's wavefunction when it starts off from far away), and $k$ comes from $p = \hbar k$ and $E = p^2/2m$. We say "approximately" because we know that real particles are wavepackets, not plane waves (since plane waves are unphysical, as we have seen before); nevertheless, it is a suitable approximation for our case. We can also write the initial wavefunction in the following equivalent form:

{% math() %}
\psi_I(x) = \begin{cases} e^{ikx}, & x < 0 \\ 0, & x> 0 \end{cases}
{% end %}

> **Note on notation:** It is conventional to use positive-phase plane waves $e^{ikx}$ to describe *right-going particles* and negative-phase plane waves $e^{-ikx}$ to describe _left-going particles_.

Now, when the particle hits the potential barrier "wall", you may expect that the particle stops or bounces back. But remember that since quantum particles are probability waves, they don't behave like classical particles. In fact, what _actually happens_ is that they partially reflect (go back to $x \to -\infty$) and partially pass through (go to $x \to \infty$)! This would be like a person walking into a wall, then both passing through and bouncing back from the wall, which is truly bizarre from a classical point of view. However, it is perfectly possible for this to happen in the quantum world!

> **Note:** This analogy is a bit oversimplified, because quantum particles are ultimately _probability waves_ and it is not really the _particle_ that "passes through" the "wall" but rather its wavefunction that extends both beyond and behind the potential barrier "wall". When we actually measure the particle, we don't find it "midway" through the wall; instead, we sometimes find that it is behind the wall, and at other times find that it is ahead of the wall. What is significant here is that there is a **nonzero probability** of the particle passing through the potential barrier, even though classical this is impossible.

Since the particle can (roughly-speaking) exhibit both _reflection_ (bouncing back from the potential barrier and traveling away to $x \to -\infty$) and _transmission_ (passing through the potential barrier and traveling to $x \to \infty$), its *final wavefunction* would take the form:

{% math() %}
\psi_F = \begin{cases} r e^{-ikx}, & x < 0 \\ te^{ik'x}, & x > 0 \end{cases}
{% end %}

Where $k'$ is the momentum of the particle if it passes through the barrier, since passing through the potential barrier saps some of its energy; mathematically, we have:

{% math() %}
k = \dfrac{\sqrt{2mE}}{\hbar}, \quad k' = \dfrac{\sqrt{2m(V_0 - E)}}{\hbar}
{% end %}

The total wavefunction is the sum of the initial and final wavefunctions, and is given by:

{% math() %}
\psi(x) = \psi_I + \psi_F = \begin{cases} e^{ikx} + r e^{-ikx}, & x < 0 \\ te^{ik'x}, & x > 0 \end{cases}
{% end %}

The coefficients $r$ and $t$ are the **reflection coefficient** and **transmission coefficient** respectively. This is because they represents the _amplitudes_ of the particle reflecting and passing through the barrier. We also define the **reflection probability** $R$ and **transmission probability** $T$ as follows:

{% math() %}
R = |r|^2,\quad R + T = 1
{% end %}

> **Note:** The reason why $R + T = 1$ is because the particle cannot just whizz off or disappear after hitting the potential barrier; it must *either* be reflected or pass through, so conservation of probability tells us that $R + T = 1$. 

To be able to solve for what $r$ and $t$ should be, we first use the requirement that the wavefunction is **continuous** at $x = 0$. Why? Mathematically, this is because the Schrödinger equation is a differential equation, and the derivative of a function is *ill-defined* if the wavefunction is not continuous. Physically, this is because any jump in the wavefunction means that the probability of finding a particle in two adjacent areas in space abruptly changes without any probability of finding the particle somewhere in between, which, again, does not make physical sense. This means that at $t = 0$, the left ($x < 0$) and right ($x > 0$) branches of the wavefunction must be equal, or in other words:

{% math() %}
\begin{gather*}
e^{ikx} + r e^{-ikx}  = te^{ik'x}, \quad x = 0 \\
e^0 + r e^0 = te^0 \\
1 + r = t
\end{gather*}
{% end %}

Additionally, the _first derivatives_ of the left and right branches of the wavefunctions must also match for the first derivative to be continuous. After all, the Schrödinger equation is a _second-order_ differential equation in space, so for the second derivative to exist, the first derivative must _also_ be continuous. Thus we have:

{% math() %}
\begin{align*}
\dfrac{\partial \psi}{\partial x}\bigg|_{x < 0} &= \dfrac{\partial \psi}{\partial x}\bigg|_{x > 0}, \quad x = 0 \\
ik e^{ikx} - ikre^{-ikx} &= ik' te^{ik'x}, \quad x = 0 \\
ik - ikr &= ik' t \\
k(1 - r) &= k' t
\end{align*}
{% end %}

Using these two equations, we can now find $r$ and $t$ explicitly. If we substitute $1 + r = t$, we can solve for the transmission coefficient $t$:

{% math() %}
\begin{gather*}
k(1 - r) = k't = k'(1 + r) \\
k - kr = k' + k' r \\
k - k' = k'r + kr \\
k - k' = r(k + k') \\
r = \dfrac{k - k'}{k + k'}
\end{gather*}
{% end %}

Thus, we can now find the **reflection probability**, which is the probability the particle will be reflected after "hitting" the potential barrier:

{% math() %}
R = |r|^2 = \left(\dfrac{k - k'}{k + k'}\right)^2
{% end %}

(Note that since $k, k'$ are real-valued, $|r|^2 = r^2$). We can also find the transmission coefficient $t$ from $t = 1+ r$:

{% math() %}
\begin{align*}
t &= 1 + r \\
&= 1 + \dfrac{k - k'}{k + k'} \\
&= \dfrac{k + k'}{k + k'} + \dfrac{k - k'}{k + k'} \\
&= \dfrac{k + k + \cancel{k' - k'}}{k + k'} \\
&= \dfrac{2k}{k + k'}
\end{align*}
{% end %}

Thus we can calculate the **transmission probability**:

{% math() %}
T = 1 - R = \dfrac{4kk'}{(k + k')^2}
{% end %}

## The state-vector and its representations

In quantum mechanics, we have *said* that particles are probabilistic waves rather than discrete objects. This is actually only a half-truth. The more accurate picture is that quantum particles are represented by **vectors in an complex space**. "What??", you might say. But however strange this may first appear to be, recognizing that particles are represented by vectors is actually crucial, particularly for more advanced quantum physics (e.g. quantum field theory).

The fundamental vector describing a particle (or more precisely, a quantum system) is called the **state-vector**, and is written in the rather funny-looking notation $|\Psi\rangle$. This state-vector is not particularly easy to visualize, but one can think of it as an "arrow" of sorts that points not in real space, but in a complex space. As a particle evolves through time, it traces something akin to a "path" through this complex space. Unlike the vectors we might be used to, which live in $\mathbb{R}^3$ (t/hat is, Euclidean 3D space), this complex space (formally called a **Hilbert space** $\mathcal{H}$) can be of *any* number of dimensions!

Of course, visualizing all those dimensions in a Hilbert space is next to impossible. However, if we consider only two (complex) dimensions, the state-vector might look something like this:

![A visualization of the state-vector](https://substackcdn.com/image/fetch/$s_!mS9U!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5e74d8f2-3a44-4cf5-a1f2-ff1cf36c8eaa_1463x787.png)

_Credit: [Dr. Ashish Bamania](https://www.intoquantum.pub/p/an-introduction-to-the-hilbert-space)_

> **Why is this drawn in 3D?** The reason is that _each_ complex dimension is not an _axis_ (as would be the case for real dimensions), but rather a _complex plane_. This is why a two-dimensional complex space is drawn in 3D, not 2D - it is formed by taking two complex planes and placing them at 90 degrees to each other, so it has to stretch into 3D.

To practice, let's consider a complex space with *three* dimensions, which we'll call $x$ and $y$ (though remember, these dimensions are not the physical $x,y,z$ axes). A 3-dimensional complex space is unfortunately not easily drawn, but it is simple enough that the calculations don't get too hairy!

Now, like the vectors we might be used to, like the position vector $\mathbf{r} = \langle x, y, z\rangle$ or momentum vector $\mathbf{p} = \langle p_x, p_y, p_z\rangle$, the state-vector also has **components**, although (as we discussed) these components are in general complex numbers that have no relationship to the physical $x, y, z$ axes. For our three-dimensional example, we can write the state-vector $|\Psi\rangle$ in column-vector form as follows:

{% math() %}
|\Psi\rangle = \begin{pmatrix} c_1 \\ c_2 \\ c_3 \end{pmatrix}, \quad c_i \in \mathbb{C}
{% end %}

We might ask whether there is a *row-vector form* of a state-vector, just like classical vectors have, for instance, $\mathbf{r}^T$ and $\mathbf{p}^T$ as their row-vector forms (their *transpose*). Indeed there is an equivalent of the row-vector form for state-vectors, which we'll write as $\langle \Psi|$ (it can seem to be a funny notation but is actually very important). $\langle \Psi|$ can be written in row-vector form as:

{% math() %}
\langle \Psi| = \begin{pmatrix} c_1^* & c_2^* & c_3^* \end{pmatrix}
{% end %}

> **Note:** Formally, we say that $\langle \Psi|$ is called the **Hermitian conjugate** of $|\Psi\rangle$, and is just a fancy name for taking the transpose of the state-vector and then complex-conjugating every component. We will see this more later.

We now might wonder if there is some equivalent of the *dot product* for a state-vector, just like classical vectors can have dot products. Indeed, there is, although we call it the **inner product** as opposed to the dot product. The standard and also quite funny-looking notation is to write the inner ("dot") product of $\langle \Psi|$ and $|\Psi\rangle$ as $\langle \Psi|\Psi\rangle$, which is written as:

{% math() %}
\begin{align*}
\langle \Psi|\Psi\rangle &= \begin{pmatrix} c_1^* & c_2^* & c_3^* \end{pmatrix} \begin{pmatrix} c_1 \\ c_2 \\ c_3 \end{pmatrix} \\
&= c_1 c_1^* + c_2 c_2^* + c_3 c_3^* \\
&= |c_1|^2 + |c_2|^2 + |c_3|^2
\end{align*}
{% end %}

In quantum mechanics, we impose the restriction that $\langle \Psi|\Psi\rangle = 1$, which also means that $|c_1|^2 + |c_2|^2 + |c_3|^2 = 1$. This is the **normalization condition**. Indeed, it looks suspiciously-similar to our previous requirement of normalizability in wave mechanics:

{% math() %}
\langle \Psi|\Psi\rangle = 1 \quad \Leftrightarrow \quad \int_{-\infty}^\infty \psi(x) \psi^*(x) dx = 1
{% end %}

We'll actually find later that - surprisingly - these are equivalent statements!

### Basis representation of vectors

Let's return to our state-vector $|\Psi\rangle$, which we wrote in the column vector form as:

{% math() %}
|\Psi\rangle = \begin{pmatrix} c_1 \\ c_2 \\ c_3 \end{pmatrix}, \quad c_i \in \mathbb{C}
{% end %}

Is there another way that we can write out $|\Psi\rangle$? Indeed there is! Recall that in normal space, vectors can also be written as a linear sum of **basis vectors**. This is also true in quantum mechanics and complex-valued spaces! For instance, we can write it out as follows:

{% math() %}
|\psi\rangle = c_1 \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} +
c_2 \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix} + c_3 \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}
{% end %}

Here, $(1, 0, 0)$, $(0, 1, 0)$, and $(0, 0, 1)$ are the **basis vectors** we use to write out the state-vector in basis form - together, we call them a **basis** (plural _bases_). We can make this more compact and general if we define:

{% math() %}
\begin{align*}
|u_1\rangle &= \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} \\
|u_2\rangle &= \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix} \\
|u_3\rangle &= \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}
\end{align*}
{% end %}

Then, the linear sum of the three basis vectors can be written as follows:

{% math() %}
|\psi\rangle = c_1 |u_1\rangle + c_2 |u_2\rangle + c_3 |u_3\rangle
{% end %}

A basis must be *orthonormal*, which means that its set of basis vectors are normalized and are orthogonal to each other. That is to say:

{% math() %}
\langle u_i |u_j\rangle = \begin{cases}
1, & |u_i\rangle = |u_j\rangle \\
0, & |u_i\rangle \neq |u_j\rangle
\end{cases}
{% end %}

A basis must also be _complete_. This means that any vector in a particular space can be written as a sum of the basis vectors (with appropriate coefficients). In intuitive terms, you can arrange the basis vectors in such a way that they can form any vector you want. For instance, in the below diagram, a vector $\mathbf{u} = (2, 3, 5)$ is formed by the sum of vectors $\mathbf{v}_1$ and $\mathbf{v}_2$:

![Illustration of vectors spanning a vector space](https://ximera.osu.edu/la/LinearAlgebra/VEC-M-0090/main-figure0.svg)

_Source: [Ximera](https://ximera.osu.edu/la/LinearAlgebra/VEC-M-0090/main)_

A complete basis is required because otherwise, the space *cannot* be fully described by the basis vectors; there are mysterious "unreachable vectors" that exist but are "out of reach" of the basis vectors. This leads to major problems when we want to actually do physics with basis vectors, so we always want a _complete basis_ in quantum mechanics. The set of all basic vectors in the basis is called the **state space** of the system, and physically represents all the possible states the system can be in - we'll discuss more on this later.

Having a **complete and orthonormal basis** allows us to expand an arbitrary vector $|\varphi\rangle$ in the space in terms of the basis vectors of the space:

{% math() %}
|\varphi\rangle = \sum_i c_i |u_i\rangle
{% end %}

Where $c_i = \langle u_i|\varphi\rangle$ is the *probability amplitude* of measuring the $|u_i\rangle$ state. The reason we call it a probability _amplitude_ rather than the probability itself is that $c_i$ is in general complex-valued. To get the actual probability (which we denote as $\mathcal{P}_i$), we must take its absolute value (complex norm) and square it:

{% math() %}
\mathcal{P}_i = |c_i|^2 = c_i c_i^*
{% end %}

Note that this _guarantees_ that the probability is real-valued, since the complex norm $|z|$ of any complex number $z$ is real-valued. Now, all of this comes purely from the math, but let's discuss the _physical interpretation_ of our results. In quantum mechanics, we assign the following interpretations to the mathematical objects from linear algebra we have discussed:

- The state-vector $|\Psi\rangle$ contains all the information about a quantum system, and "lives" in a vector space called a _Hilbert space_ (we often just call this a "space")
- Each basis vector $|u_i\rangle$ in the Hilbert space represents a **possible state** of the system; thus, the set of all basis vectors represents _all possible states_ of the system, which is why basis vectors must *span the space*
- The set of all basis vectors is called the **state space** of the system and describes how many states the quantum system has
- The state-vector is a sum of the **basis vectors** of the space, since quantum systems (unlike classical systems) are probabilistic mixtures of different states; which particular state the system is in **cannot be determined** without measuring (and fundamentally disrupting) the quantum system
- The **probability** of measuring the $i$-th state of the system is given by $\mathcal{P}_i = |c_i|^2$, where $c_i = \langle u_i|\Psi\rangle$

### The outer product

We have already seen one way to take the product of two quantum-mechanical vectors, that being the _inner product_. But it turns out that there is another way to take the product of two vectors in quantum mechanics, and it is called the **outer product**. The outer product between two vectors $|\alpha\rangle, |\beta\rangle$ is written in one of two ways:

{% math() %}
|\beta\rangle \langle \alpha |\quad \Leftrightarrow \quad |\beta\rangle \otimes \langle \alpha|
{% end %}

(Note that the $|\beta\rangle \langle \alpha|$ notation is the most commonly used). The outer product is quite a bit different from the inner product because instead of returning a scalar, it returns a *matrix*. But how do we compute it? Well, if $|\alpha\rangle$ and $|\beta\rangle$ are both three-component quantum vectors (which means they can be complex-valued) their outer product is given by:

{% math() %}
\begin{align*}
|\beta\rangle \langle \alpha| &=
\begin{pmatrix}
\beta_1^* \\ \beta_2^* \\ \beta_3^*
\end{pmatrix}^T \otimes
\begin{pmatrix} \alpha_1 \\ \alpha_2 \\ \alpha_3 \end{pmatrix} \\
&= \begin{pmatrix}
\alpha_1 \beta_1^* & \alpha_1 \beta_2^* & \alpha_1 \beta_3^* \\
\alpha_2 \beta_1^* & \alpha_2 \beta_2^* & \alpha_2 \beta_3^* \\
\alpha_3 \beta_1^* & \alpha_3 \beta_2^* & \alpha_3 \beta_3^*
\end{pmatrix}
\end{align*}
{% end %}

In general, for two vectors $|\alpha\rangle, |\beta\rangle$ the matrix $C_{ij} = (|\beta\rangle \langle \alpha|)_{ij}$ has components given by:

{% math() %}
(|\beta\rangle \langle \alpha|)_{ij} = C_{ij} = \alpha_i \beta_j^*
{% end %}

For instance, if we use this formula, the $C_{11}$ component is equal to {% inlmath() %}\alpha_1 \beta_1^*{% end %}, and the $C_{32}$ component is equal to {% inlmath() %}\alpha_3 \beta_2^*{% end %}. The outer product is a bit hard to understand in intuitive terms, so it is okay at this point to just think of the outer product as an operation that takes two vectors and gives you a matrix, just like the inner product takes two vectors and gives you a scalar.

> **Note:** For those familiar with more advanced linear algebra, the outer product is formally the **tensor product** of a ket-vector and a bra-vector; in tensor notation one can use the alternate notation with $C_i{}^j = \alpha_i \beta^j$ which shares a [correspondence with relativistic tensor notation](https://www.kattemolle.com/QMvsGR/index.html). Another interesting article to read is this [Math StackExchange explanation](https://math.stackexchange.com/questions/4183973/intuitive-explanation-of-outer-product) of the outer product.

The outer product is very important because, among other reasons, it is used to express the **closure relation** of any vector space:

{% math() %}
\sum_i |u_i\rangle \langle u_i | = \hat I
{% end %}

Where here, $\hat I$ is the identity matrix, and $|u_i\rangle$ are the basis vectors. What does this mean? Remember that the outer product of two vectors creates a _matrix_. The closure relation tells us that the sum of all of these matrices - formed from the basis vectors - is the identity matrix $\hat I$. Roughly speaking, this means that summing all the possible matrices formed by basis vectors allows you to get the identity matrix. This is essentially an equivalent restatement of our previous definition of _completeness_, which tells us that the set of basis vectors must _span the space_ and thus any arbitrary vector can be expressed as a sum of basis vectors. This is because, assuming an arbitrary vector $|\varphi\rangle$:

{% math() %}
\begin{align*}
|\varphi\rangle &= |\varphi\rangle \\
&= \hat I |\varphi\rangle  \\
&= \sum_i |u_i\rangle \underbrace{\langle u_i|\varphi\rangle}_{c_i} \\
&= \sum_i c_i |u_i\rangle
\end{align*}
{% end %}

Thus we find that indeed, the closure relation tells us that an arbitrary vector $|\varphi\rangle$ can be expressed as a sum of basis vectors, which is just the same thing as the requirement that the basis vectors be complete and orthonormal.

> **Note:** It is also common to use the notation $\sum_i |c_i\rangle \langle c_i| = 1$ for the closure relation, with the implicit understanding that $1$ means the identity matrix.

### Interlude: classifications of quantum systems

In quantum mechanics, we use a variety of names to describe different types of quantum systems. There are a lot of different terms we use, but let's go through short number of them. First, we may encounter *finite-dimensional* systems or *infinite-dimensional* systems. Here, _dimension_ refers to the dimension of the **state space**, not the dimensions in 3D Cartesian space. A finite-dimensional system is spanned by a **finite number** of basis vectors. This means that the system can only be in a finite number of states. An analogy is that of a **perfect coin toss**: a coin can only be heads-up or heads-down. If we use quantum mechanical notation and denote $|h\rangle$ as the heads-up state and $|d\rangle$ as the heads-down state, we can write the "state-vector" of the coin as:

{% math() %}
|\psi\rangle_\text{coin} = c_1 |h\rangle + c_2 |d\rangle
{% end %}

Where $c_1, c_2$ are the probability amplitudes of measuring the heads-up and heads-down states respectively. Since we know the probability is found by squaring the probability amplitudes, the probability of measuring the coin to be heads-up is $\mathcal{P}_1 = |c_1|^2$ and likewise the probability of measuring the coin to be heads-down is $\mathcal{P}_2 = |c_2|^2$. We know that a (perfect) coin toss is equally likely to be heads-up and heads-down, or in otherwise, there is a 50% probability for either heads-up or heads down, and thus $\mathcal{P}_1 = \mathcal{P}_2 = 1/2$, so we have $c_1 = c_2 = 1/\sqrt{2}$. This gives us:

{% math() %}
|\psi\rangle_\text{coin} = \dfrac{1}{\sqrt{2}} |h\rangle + \dfrac{1}{\sqrt{2}} |d\rangle
{% end %}

An infinite-dimensional system, by contrast, is spanned by an **infinite number** of basis vectors. This means that the system can (in principle) be in an infinite number of states.  For instance, consider a free quantum particle moving along a line: its position is unconstrained, so it can be in any position $x \in (-\infty, \infty)$. Thus, there are indeed an infinite number of states $|x_1\rangle, |x_2\rangle, |x_3\rangle, \dots, |x_n\rangle$ (corresponding to positions $x_1, x_2, x_3, \dots, x_n$) that the particle can be in. The particle in a box is also an infinite-dimensional system, since it also has an infinite number of possible states (recall that the eigenstates can be written in the form $\psi_n(x)$, where $n$ can be arbitrarily large).

Another distinction between quantum systems is between **continuous systems** and **discrete systems**. A discrete system has basis vectors with _discrete eigenvalues_, while a continuous system has basis vectors with _continuous eigenvalues_. For instance, momentum basis vectors $|p_1\rangle,|p_2\rangle, |p_2\rangle$ have continuous eigenvalues, since the possible values of a particle's momentum can (usually) be any value. However, the vast majority of bases we use in quantum mechanics do _not_ have continuous eigenvalues, and can only take particular values. In fact, the _"quantum"_ in quantum mechanics refers to the fact that a measurement on a quantum particle frequently yields _discrete_ results that are multiples of a fundamental value, called a _quanta_.

> **Note:** It is important to note that an infinite-dimensional system may still be a discrete system. For instance, the eigenstates of the particle in a box form an infinite-dimensional state space, but as they have discrete (energy) eigenvalues, the system is still discrete.

Differentiating between discrete and continuous systems - as well as between finite-dimensional and infinite-dimensional systems - is very important! This is because they change the way key identities are defined. For instance, in a **continuous** system, we can write the closure relation as:

{% math() %}
\int |\alpha\rangle \langle \alpha| d\alpha = 1
{% end %}

And likewise, one can write out the basis expansion as:

{% math() %}
|\psi\rangle = \int c(\alpha)|\alpha\rangle d\alpha
{% end %}

Meanwhile, for a **discrete** system, the basis expansion instead takes the form:

{% math() %}
|\psi\rangle = \sum_\alpha c_\alpha |\alpha\rangle
{% end %}

And the closure relation is given by:

{% math() %}
\sum_\alpha |\alpha \rangle \langle \alpha| = 1
{% end %}

The crucial thing here is that these expressions are **extremely general** - they work for any set of continuous basis vectors (for a continuous system) or discrete basis vectors (for a discrete system). It doesn't matter which basis we use!

## Quantum operators

In classical mechanics, physical quantities like energy, momentum, and velocity are all given by _functions_ (typically of space and of time). For instance, the total energy of a system (more formally known as the _Hamiltonian_, see the [guide to Lagrangian and Hamiltonian mechanics](@/advanced-classical-mech/part-2.md) for more information), is given by a function $H(x, p, t)$, where $x(t)$ is the position of the particle and $p(t)$ is its momentum (roughly-speaking). However, in quantum mechanics, each physical quantity is associated with an **operator** instead of a function. For instance, there is the momentum operator $\hat p$, the position operator $\hat x$, and the Hamiltonian operator $\hat H$, where the hats (represented by the symbol $\hat{}$) tell us that these are _operators_, not functions.

So what is an operator? An operator is something that takes one vector (or function) and transforms it to another vector (or function). A good example of an operator is a transformation matrix. Applying a transformation matrix on one vector gives us another vector, which is _exactly_ what an operator does. One can also define operators that operate on _vectors_ instead of functions (as a consequence, they are usually _differential_ operators, meaning that they return some combination of the derivative(s) of a function). Some of these include the position operator ($\hat x$), momentum operator ($\hat p$), the kinetic energy operator $\hat K$, and the potential energy operator $\hat V$. They respectively have the forms:

{% math() %}
\begin{align*}
\hat x &= x \\
\hat p &= -i\hbar \nabla \\
\hat K &= \frac{\hat p^2}{2m} = -\frac{\hbar^2}{2m} \nabla^2 \\
\hat V &= V(\mathbf{x})
\end{align*}
{% end %}

Combining the kinetic and potential energy operators gives us the total energy (or _Hamiltonian_) operator ($\hat H$):

{% math() %}
\hat H = \hat K + \hat V = -\dfrac{\hbar^2}{2m} \nabla^2 + V
{% end %}

### Eigenstates of the momentum operator

For some operators, it is straightforward to find their eigenstates. For instance, if we simply solve the eigenvalue equation for the momentum operator, we have:

{% math() %}
\hat p \psi = i\hbar \dfrac{\partial \psi}{\partial x} = p \psi
{% end %}

This differential equation has the straightforward solution $\psi(x) = e^{\pm ipx/\hbar}$, which is just a plane wave. Of course, momentum eigenstates are physically cannot exist, because real particles, of course, have to be _somewhere_, and by the Heisenberg uncertainty relation a pure momentum eigenstate means a particle can be _anywhere_! However, they are a good approximation in many cases to particles with a very small range of momenta.

### Eigenstates of the position operator

Similarly, the position operator's eigenstates can also be found if we write out its eigenvalue equation:

{% math() %}
\hat x \psi = x' \psi
{% end %}

Where $x'$ is some eigenvalue of the position operator. The _only_ function that satisfies this equation is the Dirac delta "function":

{% math() %}
\psi = a\delta(x - x'), \quad a = \text{const.}
{% end %}

#### Eigenstates of the Hamiltonian

The Hamiltonian operator's eigenstates can also be found through its eigenvalue equation:

{% math() %}
\hat H \psi = \left(-\dfrac{\hbar^2}{2m}\nabla^2 + V(x)\right)\psi = E \psi
{% end %}

Notice how this is the same thing as the time-independent Schrödinger equation! Thus, the eigenstates of the Hamiltonian are the **solutions to the time-independent Schrödinger equation**, and the eigenvalues are the **possible energies** of the system.

### Generalized operators in bra-ket notation

Up to this point, we have seen operators only in wave mechanics. Let us now generalize the notion of an operator on the state-vector, which (as we know) is the more fundamental quantity. In bra-ket notation an operator $\hat A$ is written as:

{% math() %}
\hat A|\psi\rangle = |\psi'\rangle
{% end %}

In quantum mechanics, for the most part, we only consider **linear** operators. The formal definition of a *linear operator* is that the operator satisfies:

{% math() %}
\hat A(\lambda_1 |\psi_1\rangle + \lambda_2 |\psi_2\rangle) = \lambda_1 \hat A|\psi_1\rangle + \lambda_2 |\hat \psi_2\rangle
{% end %}

As a consequence, all linear operators also satisfy:

{% math() %}
(\hat A \hat B) |\psi\rangle = \hat A(\hat B |\psi\rangle)
{% end %}

Likewise, "sandwiching" a linear operator between a bra $|\psi\rangle$ and a ket $\langle \varphi|$ always produces a scalar $c$:

{% math() %}
\langle \varphi| \hat A |\psi \rangle = \langle \varphi|(\hat A |\psi\rangle)) = c
{% end %}

> **Note:** The scalar $c$ is frequently called in the literature as a **c-number** (short for "complex number"). This is to distinguish it from vectors, matrices, and operators in quantum mechanics, which are **not** scalars (even if they are complex-valued).

### Examples of abstract linear operators

The first example of a linear operator we will consider is called the **projection operator** $\hat P$. The projection operator is defined by:

{% math() %}
\hat P = |\alpha\rangle \langle \alpha|
{% end %}

If you have studied linear algebra, you may notice that this is very similar to the idea of a **vector projection**. Essentially, the projection operator tells us *how much* of one vector exists along a particular axis (although the axis is, again, in some direction in a complex Hilbert space, not real space). The component of a ket $|\psi\rangle$ in the direction of the basis vector $|\alpha\rangle$ is then given by $\hat P|\psi\rangle$. To demonstrate, let's consider a 3D ket $|\psi\rangle$ in a Hilbert space, which, in column vector form, is given by:

{% math() %}
|\psi\rangle = \begin{pmatrix}
c_\alpha \\
c_\beta \\
c_\gamma
\end{pmatrix}
{% end %}

Let us choose an orthonormal basis $\{|\alpha\rangle, |\beta\rangle, |\gamma\rangle\}$ in which we can write $|\psi\rangle$ in basis-vector form as:

{% math() %}
|\psi\rangle = c_\alpha|\alpha\rangle + c_\beta |\beta\rangle + c_\gamma|\gamma\rangle
{% end %}

Now, let us *operate* the projection operator on $|\psi\rangle$. This gives us:

{% math() %}
\begin{align*}
\hat P |\psi\rangle &= |\alpha\rangle \langle \alpha|\psi\rangle \\
&= |\alpha\rangle \big[ c_\alpha \langle \alpha|\alpha\rangle + c_\beta\langle \alpha|\beta\rangle + c_\gamma \langle \alpha|\gamma\rangle\big]\\
&= |\alpha\rangle \big[ c_\alpha \underbrace{\langle \alpha|\alpha\rangle}_{1} + c_\beta\cancel{\langle \alpha|\beta\rangle}^0 + c_\gamma \cancel{\langle \alpha|\gamma\rangle}^0\big]\\
&= c_\alpha|\alpha\rangle
\end{align*}
{% end %}

> **Note:** The above derivation works because our basis is **orthonormal**, meaning that the basis vectors are normalized ($\langle \alpha| \alpha\rangle = \langle \beta| \beta \rangle = \langle \gamma|\gamma \rangle = 1$) and orthogonal ($\langle i|j\rangle = 0$, for instance $\alpha|\beta\rangle = 0$).

Another one of the *essential* properties that defines a projection operator is that $\hat P^2 = \hat P$, which is called **idempotency**. We can show this as follows:

{% math() %}
\begin{align*}
\hat P^2|\psi\rangle &= \hat P(\hat P|\psi\rangle) \\
&= \hat P (c_\alpha|\alpha\rangle) \\
&= c_\alpha \underbrace{|\alpha\rangle \langle \alpha|}_{\hat P}\alpha\rangle \\
&= c_\alpha |\alpha\rangle \underbrace{\langle \alpha|\alpha\rangle}_1 \\
&= c_\alpha |\alpha\rangle
\end{align*}
{% end %}

This *only* works if the projection operator is the outer product of the **same state** i.e. $|\alpha\rangle \langle \alpha|$ and that $|\alpha\rangle$ is a **normalized vector**. Indeed, $\hat A = |\psi\alpha \langle \beta |$ is **not** a valid projection operator, and neither is $\hat B = |\alpha\rangle \langle \alpha|)$ if $\langle a|a\rangle \neq 1$. Likewise, it is also only true if the projection operator is **linear**, which is what allowed us to say that $\hat P^2|\psi\rangle = (\hat P \hat P)|\psi\rangle = \hat P(\hat P |\psi\rangle)$.

### The adjoint and Hermitian operators

Another important property of nearly all operators we consider in quantum mechanics is that they are **Hermitian operators**. What does that mean? Well, consider an arbitrary operator. The **adjoint** of an operator is defined as its *transpose* with all of its components *complex-conjugated*. We notate the adjoint of an operator $\hat A$ as $\hat A^\dagger$ and read it as "A-dagger" (this is for [historical reasons](https://hsm.stackexchange.com/questions/11426/who-introduced-the-daggersymbol-as-conjugate-transpose-in-quantum-mechanics) as physicists wanted a symbol that wouldn't be confused with the complex conjugate symbol, *not* because physicists like to swordfight!). The idea of adjoints may sound quite abstract, so let's see an example for a 2D Hilbert space. Let us assume that we have some operator $\hat A$, whose matrix representation is as follows:

{% math() %}
\hat A = \begin{pmatrix}
c_{11} & c_{12} \\
c_{21} & c_{22}
\end{pmatrix}
{% end %}

Then, the adjoint $\hat A^\dagger$ of $\hat A$ is given by:

{% math() %}
\hat A^\dagger =\begin{pmatrix}
c_{11}^* & c_{12}^* \\
c_{21}^* & c_{22}^*
\end{pmatrix}^T 
= \begin{pmatrix}
c_{11}^* & c_{21}^* \\
c_{12}^* & c_{22}^*
\end{pmatrix}
{% end %}

For example, let's take the adjoint of a very famous matrix operator in quantum mechanics (the Pauli $y$-matrix):

{% math() %}
\begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}^\dagger = 
\begin{pmatrix}
0& -i \\
i & 0
\end{pmatrix}
{% end %}

Notice here that to find the adjoint of $\hat A$ we **complex-conjugated** every component of the matrix, and then transposed the matrix. This procedure works for *any* operator when it is in matrix representation. This is a straightforward rule to remember - if we're given an operator in matrix form, complex-conjugation and transposing gives us the adjoint.

Unfortunately, if we consider an *abstract operator* (for instance, the projection operator) where we don't know its matrix form, there is usually **no general formula** that relates $\hat A$ and $\hat A^\dagger$. However, there are some special cases:

- A **constant** $c$ has adjoint $c^\dagger = c^*$
- A **ket** $|a\rangle$ has adjoint $|a\rangle^\dagger = \langle a|$
- A **bra** $\langle b|$ has adjoint $\langle b|^\dagger = |b\rangle$
- An **operator** $\hat A$ satisfying $\hat A|\alpha\rangle = |\beta\rangle$ has $\langle \alpha|\hat A^\dagger = \langle \beta|$
- An **inner product** $\langle a|b\rangle$ has adjoint $\langle a|b\rangle^\dagger = \langle b|a\rangle$
- An **operator inner product** $\langle a|\hat A|b\rangle$ has adjoint $\langle b|\hat A^\dagger|a\rangle^*$
- An **outer product** $|a\rangle \langle b|$ has adjoint $(|a\rangle \langle b|)^\dagger = |b\rangle \langle a|$

A few useful properties of the adjoint are also listed below:

- $(\hat A^\dagger)^\dagger = \hat A$
- $(\lambda \hat A)^\dagger = \lambda^* A^\dagger$
- $(\hat A + \hat B)^\dagger = \hat A^\dagger + \hat B^\dagger$
- $(\hat A \hat B)^\dagger = \hat B^\dagger \hat A^\dagger$

We will now introduce a special class of operators, known as **Hermitian operators**. The essential property of a Hermitian operator $\hat A$ is that it is **equal** to its adjoint:

{% math() %}
\hat A = \hat A^\dagger
{% end %}

An operator with this property is said to be _self-adjoint_, and thus Hermitian operators are often also called _self-adjoint operators_ (mathematicians are more careful with the terminology, but for physicists _self-adjoint_ and _Hermitian_ mean the same thing). While this may seem like a relatively arbitrary property, it is actually *very* useful, because it allows us to manipulate operators in very convenient ways. A Hermitian operator, for instance, satisfies:

{% math() %}
\langle \beta |\hat A|\alpha\rangle = \langle \beta |\hat A^\dagger|\alpha\rangle = \langle \alpha |\hat A|\beta\rangle^*
{% end %}

The fact that we can just "flip" bras and kets around, such that $\langle \beta |\hat A|\alpha\rangle = \langle \alpha|\hat A|\beta\rangle^*$ *only* works because $\hat A$ is a Hermitian operator! In addition, a Hermitian operator satisfies the **self-adjoint** property:

{% math() %}
\langle \varphi | \cdot \hat A|\psi\rangle =\langle \varphi | \hat A \cdot  |\psi\rangle
{% end %}

(Here $\cdot$ is the *inner product* but we write it in dot product notation for clarity). This all-important property is the bedrock for a lot of quantum mechanics, and is (one of the) reasons we demand our operators to be Hermitian!

> **Note:** Mathematicians typically use the alternative notation $\langle \varphi, \hat A \psi\rangle = \langle \varphi \hat A, \psi\rangle$ which means the same thing even though the notation is different.

### Matrix representations of operators

The idea of an operator in quantum mechanics is very abstract, and we are not always provided (indeed, there may not even exist!) the matrix form of an operator, just like we often don't know the column/row-vector form of the state-vector. However, since matrices and vectors are often much easier to work with than abstract operators and bras/kets, it is often very *useful* to find the matrix form of the operator, also known as its **matrix representation**.

First, we should note that a matrix representation of an operator can only be found when you **set your basis**. To find a matrix representation $A_{ij}$ of a discrete operator $\hat A$ in some given basis (let's call this basis $|\alpha\rangle$ for clarity), we use the formula:

{% math() %}
A_{ij} = \langle \alpha_i| \hat A |\hat \alpha_j\rangle
{% end %}

Let's take the example of the *projection operator* $\hat P = |\alpha\rangle \langle \alpha|$, where $|\alpha\rangle$ is the normalized state-vector of the system, and can be written out in the basis representation as:

{% math() %}
|\alpha\rangle = \sum_i c_i |\alpha_i\rangle = \sum_i c_j |\alpha_j\rangle
{% end %}

Plugging in the explicit form of the projection operator gives us:

{% math() %}
\begin{align*}
P_{ij} &= \langle \alpha_i |\hat P |a_j \rangle \\
&= \underbrace{\langle \alpha_i| \alpha\rangle}_{c_i} \underbrace{\langle \alpha| \alpha_j \rangle}_{c_j} \\
&= c_i\delta_{ij} c_j\delta_{ij} \\
&= c_i c_jI
\end{align*}
{% end %}

Which is simply the identity matrix. For instance, for a 3-dimensional system, $P_{ij}$ would be:

{% math() %}
P_{ij} = \begin{pmatrix}
c_1 c_1 & 0 & 0 \\
0 & c_2 c_2& 0 \\
0 & 0 & c_3 c_3
\end{pmatrix}
{% end %}

Utilizing the matrix representation of operators is often very useful for finite-dimensional and infinite-dimensional systems alike. For instance, a formula we will use very frequently later to find the matrix representation of the Hamiltonian $\hat H$ in terms of some basis $|\varphi\rangle$ is as follows:

{% math() %}
H_{ij} = \langle \varphi_i|\hat H|\varphi_j\rangle
{% end %}

Usually, we choose $|\varphi\rangle$ to be the _eigenstates_ of the Hamiltonian operator, and this method is very useful for solving many problems - but let's not get too ahead of ourselves, we'll get to there!

### Representations of continuous operators

Let's now turn our attention to situations where we have a **continuous basis** (i.e. one where the basis has continuous eigenvalues). It is also possible to find the representation of an operator in continuous bases, although these representations are not usually written out in matrix form. For instance, consider an operator that is defined as follows (in the position basis):

{% math() %}
F = \dfrac{\partial}{\partial x}
{% end %}

Then, applying the operator on some function $f(x)$ gives a new function $g(x)$, which is the _derivative_ of the original function:

{% math() %}
\hat F[f(x)] \to \dfrac{\partial f}{\partial x} = g(x)
{% end %}

This may not _look_ like the matrix forms of operators that we saw previously. But this is a false distinction that arises due to mathematical notation; the representation of an operator is really just the same thing as an infinite-dimensional matrix. This is because functions are [really just infinite-dimensional vectors](https://thenumb.at/Functions-are-Vectors/), so an operator that takes some function $f(x)$ and returns a new function $g(x)$ is really the same thing as applying a matrix to a vector, giving us a new vector. The only difference is that we're now working with _continuous_ basis vectors. Indeed, this is why we use a _Hilbert space_ in quantum mechanics, because a Hilbert space can have an _arbitrary_ number of dimensions, unlike the Euclidean space of classical mechanics.

> **Note:** Those familiar with more in-depth linear algebra will note that the most general representation of an operator in this context is more formally termed a _linear map_ between two infinite-dimensional spaces.

The two continuous bases that we will find most commonly are the **position basis** $|x\rangle$ and **momentum basis** $|p\rangle$. Just like any other basis, they satisfy orthogonality:

{% math() %}
\begin{align*}
\langle x|x'\rangle &= \delta(x'-x) \\
\langle p|p'\rangle &= \delta(p'-p)
\end{align*}
{% end %}

Likewise, they satisfy **closure**:

{% math() %}
\begin{align*}
\int dx~ |x\rangle \langle x| &= 1 \\
\int dp~ |p\rangle \langle p| &= 1
\end{align*}
{% end %}

Another essential property is that the inner product between any two basis vectors $|x\rangle, |p\rangle$ satisfies:

{% math() %}
\langle x|p\rangle = \dfrac{1}{\sqrt{2\pi}} e^{ipx/\hbar}
{% end %}

> **Note:** Depending on the text and choice of normalization, there may be a prefactor of $\dfrac{1}{\sqrt{2\pi \hbar}}$ as opposed to $\dfrac{1}{\sqrt{2\pi}}$ in the inner product.

We can prove this by solving for the eigenvectors of the position and momentum operators. The position operator is defined as $\hat x = x$, while the momentum operator is defined as $\hat p = -i\hbar \dfrac{\partial}{\partial x}$. Solving the eigenvalue equations for each gives us:

{% math() %}
\begin{align*}
\hat x|x\rangle &= x|x\rangle \quad \Rightarrow \quad |x\rangle = \delta(x - x') \\
\hat p|p\rangle &= p|p\rangle \quad \Rightarrow \quad |p\rangle = \frac{1}{\sqrt{2\pi}}e^{ipx/\hbar}
\end{align*}
{% end %}

Since the eigenvectors in our case are functions (which are the same thing as infinite-dimensional vectors), the inner product becomes an integral:

{% math() %}
\langle x|p\rangle = \int dx'\delta(x - x') \frac{1}{\sqrt{2\pi}}e^{ipx'/\hbar}= \dfrac{1}{\sqrt{2\pi}} e^{ipx/\hbar}
{% end %}

What about taking the inner product of $|x\rangle, |p\rangle$ with the state-vector $|\Psi\rangle$? Well, since the state-vector evolves with time, that is, $|\Psi\rangle = |\Psi(t)\rangle$, let's consider the state-vector at an instant in time, say, $t = 0$. Then we define $|\psi\rangle = |\Psi(0)\rangle$ to be the **time-independent state-vector**. The inner product of $|\psi\rangle$ with $|x\rangle$ then tells us the components of $|\psi\rangle$ in the position basis, so we have:

{% math() %}
\psi(x) = \langle x|\psi\rangle
{% end %}

But this is just the position-space wavefunction! Meanwhile, the inner product of $|\psi\rangle$ with $|p\rangle$ then tells us the components of $|\psi\rangle$ in the momentum basis, so: 

{% math() %}
\tilde \psi(p) = \langle p|\psi\rangle
{% end %}

We have thus uncovered the surprising fact that **the wavefunction is just the state-vector's components in a particular basis**. This is why we say that the state-vector is the more fundamental quantity! With the full power of Dirac notation, we can also use the closure relation to tell us that:

{% math() %}
\begin{align*}
\psi(x) &= \langle x|\psi\rangle \\ &= \int d^3p \langle x|p\rangle \langle p|\psi\rangle \\ &= \dfrac{1}{\sqrt{2\pi \hbar}} \int dp~\tilde \psi(p) e^{ipx/\hbar} \\
\tilde \psi(p) &= \langle p|\psi\rangle \\
&= \int d^3x \langle p|x\rangle \langle x|\psi\rangle \\
&= \dfrac{1}{\sqrt{2\pi \hbar}} \int dx~\psi(x) e^{-ipx/\hbar}
\end{align*}
{% end %}

Indeed, these are just our definitions of the position and momentum-space wavefunctions in terms of Fourier transforms of each other!

In higher dimensions, we can define the 3D versions of the position and momentum operators:

{% math() %}
\hat{\mathbf{x}} = \begin{pmatrix} \hat x \\ \hat y \\ \hat z \end{pmatrix}, \quad 
\hat{\mathbf{p}} = \begin{pmatrix} \hat p_x \\ \hat p_y \\ \hat p_z \end{pmatrix}, \quad 
{% end %}

And in $N$ dimensions, we have:

{% math() %}
\langle \mathbf{x}|\mathbf{p}\rangle = \dfrac{1}{(2\pi)^{3/N}} e^{i\mathbf{p} \cdot \mathbf{x}/\hbar}
{% end %}

> **Note on notation:** It is sometimes the case that $\hat{\mathbf{x}}$ is written as $\hat{\mathbf{R}}$ or $\hat{\mathbf{X}}$ and $\hat{\mathbf{p}}$ is written as $\hat{\mathbf{P}}$ instead. We will use these notations interchangeably.

## Observables

Having wandered far in math-land, let us return back to physics, and discuss one of the most important topics in quantum mechanics: **observables**. An observable is, roughly speaking, something you can _measure_ about a quantum particle. The position $x$ and the momentum $p$ of a particle, for instance, are observables. We already know that observables in quantum mechanics are represented by **operators**, not numbers or functions. For instance, we saw the position operator $\hat x$, the momentum operator $\hat p$, and the projection operator $\hat P$.

> **Note on notation:** We will generally denote the observable in question without the operator hat, whereas the operator _associated with_ the observable is notated with the hat. For instance, if I have an observable $A$, then its associated operator is written as $\hat A$. Similarly, if I have observable $x$ (position), then its associated operator is written as $\hat x$ (which we recognize as the position operator).

But if observables like position and momentum are associated with operators and not functions, how can we know the *physical values* of the position and momentum of a quantum particle? In other words, how can we get out a real, measurable number from complex-valued state-vectors and operators in a Hilbert space? The answer comes from **eigenvalues** - by finding the eigenvalues of an operator, we can get a scalar out, and this scalar is a number you can actually measure!

In pure mathematics, there are essentially no restrictions (other than linearity) on linear operators. But quantum mechanics stipulates that the operators with **physical significance** must satisfy an **eigenvalue equation** in the form:

{% math() %}
\hat A|\varphi\rangle = \lambda |\varphi\rangle
{% end %}

Where here, $|\varphi\rangle$ is called the **eigenvector** (or _eigenstate_) of $\hat A$ and $\lambda$ is the **eigenvalue**. Furthermore, $\hat A$ is required to be a **Hermitian operator**. Why? Since an observable is something you *measure*, it's got to be a real number! This is automatically satisfied by Hermitian operators, since one may show mathematically that:

1. The eigenvalues of a Hermitian operator are **real**
2. The eigenvectors of an Hermitian operator are **orthogonal**
3. The set of all eigenvectors of a Hermitian operator form an **orthonormal basis** in the space

Remember that we said previously that **basis vectors represent possible states of a quantum system**. Since the eigenvectors of a Hermitian operator automatically form an orthonormal basis, combining our two statements leads to several profound conclusions, which form the [fundamental postulates of quantum mechanics](https://en.wikipedia.org/wiki/Mathematical_formulation_of_quantum_mechanics):

> **Postulate I of quantum mechanics:** A quantum system is described by a **state vector** $|\Psi\rangle$, which exists in a complex-valued Hilbert space $\mathcal{H}$ of arbitrary dimensions.

> **Postulate II(a) of quantum mechanics:** Observables (physical quantities) are represented by **Hermitian operators**, whose eigenvectors are the *possible states* of a quantum system (termed its **eigenstates**), and whose eigenvalues are the *measurable values* of the observable. The state-vector $|\Psi\rangle$ is a *superposition* of the eigenstates of the system.

> **Postulate II(b) of quantum mechanics:** The **probability amplitude** of measuring some eigenstate $|u_i\rangle$ of the system is the inner product $\langle u_i|\Psi\rangle$ of the eigenstate with the state-vector, and the probability $\mathcal{P}_i$ is given by the _squared norm_ $|\langle u_i|\Psi\rangle|^2$ of the probability amplitude.

Together with the requirement of the conservation of probability, these postulates are at the heart of quantum mechanics and form the basis of the rigorous formulation of quantum mechanics from a mathematical standpoint. In other words, they're really important!

### The Born rule

Let's take a closer look at _postulate II(b)_. This postulate is more formally known as the **Born rule**:

> **Born rule (for continuous quantities):** For any continuous observable represented by operator $\hat a$, with eigenstates $|\alpha\rangle$ and eigenvalues $\alpha$, the wavefunction $\psi(\alpha)$ represents the _probability amplitude_ $c(\alpha)$ of measuring the corresponding observable's value to be $\alpha$.

> **Born rule (for discrete quantities):** For any discrete (quantized) observable represented by operator $\hat a$, with eigenstates $|\alpha\rangle$ and eigenvalues $\alpha$, the wavefunction $\psi_\alpha$ represents the _probability amplitude_ $c_\alpha$ of measuring the corresponding observable's value to be $\alpha$.



### Degeneracy and CSCOs

Let's go back to postulate II(a) of quantum mechanics, which (among other things) says that (1) eigenvectors of Hermitian operators represent possible states (*eigenstates*) of a system and that (2) eigenstates have associated *eigenvalues* that are physically-measurable (real-valued). From a simple reading, you might have the idea that quantum mechanics gives a neat, simple correspondence: each eigenstate has a unique eigenvalue, and if you solve the eigenvalue equation for some observable, you get a set of eigenvalue-eigenstate pairs. Then the state-vector just becomes a superposition of these eigenstates, and once we have that, the quantum system is - ta-da - solved!

If only it were that simple! The issue is that when solving the eigenvalue equation, *different* eigenstates can correspond to the *same* eigenvalue. The (unfortunate and very antiquated) term to describe this phenomenon is **degeneracy**, although "repeated states" communicates the same information. A common occurrence of degeneracy is when two states of a system $|\varphi_1\rangle, |\varphi_2\rangle$ have the same energy eigenvalue, i.e. $E_1 = E_2$, so you can't tell them apart from just knowing the energy of the system.

Let's demonstrate with another example. Say we have two observables $A, B$ which are represented by operators $\hat A, \hat B$. They respectively satisfy the eigenvalue equations:

{% math() %}
\begin{align*}
\hat A|\psi\rangle = a|\psi\rangle \\
\hat B|\psi\rangle = b|\psi\rangle
\end{align*}
{% end %}

As a reminder, if $\hat A, \hat B$ **commute**, then they satisfy:

{% math() %}
[\hat A, \hat B] = \hat A \hat B - \hat B \hat A = 0
{% end %}

Where $[\hat A, \hat B]$ is the **commutator** of $\hat A$ and $\hat B$. The question that now matters to us is this: is the system degenerate? Well, it is certainly _possible_ for it to be! The reason is that it is possible to have an eigenvalue $a$ where:

{% math() %}
\hat A|\psi_1\rangle = a|\psi_1\rangle, \quad \hat A|\psi_2\rangle = a|\psi_2\rangle
{% end %}

This means that the two states $|\psi_1\rangle$ and $|\psi_2\rangle$ share the **same eigenvalue** $a$. Remember that in quantum mechanics, *eigenvalues* of observables (like energy, momentum, position, etc.) are all we can physically measure, so if we naively measure our observable $A$ to have some eigenvalue $a$, we'd have no idea what state it came from. It could've been either the $|\psi_1\rangle$ or the $|\psi_2\rangle$ state, but it would be impossible to tell!

To resolve this issue, we need more information, and that information comes from our other observable $B$. This is because while $|\psi_1\rangle, |\psi_2\rangle$ share the same eigenvalue $a$ for the $\hat A$ operator, we often find that they have _different_ eigenvalues for the $\hat B$ operator. That is to say:

{% math() %}
\hat B|\psi_1\rangle = b_1 |\psi_1\rangle, \quad \hat B|\psi_2\rangle = b_2 |\psi_2\rangle
{% end %}

Now, the two states $|\psi_1\rangle$ and $|\psi_2\rangle$ share **different eigenvalues** $b_1, b_2$, so we can now tell which state is which: if we measure $b_1$, then we *know* the system must be in state $|\psi_1\rangle$, whereas if we measure $b_2$, then we *know* the system must be in state $|\psi_2\rangle$. This tells us that while a single eigenvalue $a$ might not allow us to determine the exact state of the system, a _pair of eigenvalues_ $(a, b)$ does! Thus, despite the degeneracy in the system, the ordered pairs $(a, b_1)$ and $(a, b_2)$ can be used to *uniquely* identify the states $|\psi_1\rangle$ and $|\psi_2\rangle$, solving the problem of degeneracy! This is called a **complete set of commuting observables (CSCO)**, which tells us that we can **uniquely identify** each eigenstate of a system with degeneracy, _as long as_:

1. We have two observables $A, B$, which have associated operators $\hat A, \hat B$ with respective eigenvalues $a, b$
2. The operators $\hat A, \hat B$ **commute** with each other, that is, $[\hat A, \hat B] = 0$
3. An ordered pair of eigenvalues $(a, b)$ *always corresponds* to a **unique eigenstate**

### The tensor product

Up to this point, we have assume that we are describing a **single** quantum system, which has a unique single state-vector $|\Psi\rangle$ (or equivalently, if we assume $t = 0$, then by a unique time-independent state-vector $|\psi\rangle$). But what if we want to describe a **composite system** formed by **several** quantum systems interacting with each other? Then one state-vector wouldn't be enough! In fact, to describe a composite system formed by $N$ quantum systems, we will need $N$ state-vectors! This is all very wonky to work with, so instead, we can describe such a system by a *single* state-vector that is the **tensor product** of each of the individual state-vectors.

For instance, consider a composite system formed by combining two separate quantum systems, with individual state-vectors $|\psi_1\rangle$ and $|\psi_2\rangle$. The state-vector of the composite system $|\psi_{12}\rangle$ can be written as the **tensor product** between two systems with state-vectors $|\psi_1\rangle, |\psi_2\rangle$, and is denoted as:

{% math() %}
|\psi_{12}\rangle = |\psi_1\rangle \otimes |\psi_2\rangle
{% end %}

If state $|\psi_1\rangle = \alpha_1 |u_1\rangle + \alpha_2 |u_2\rangle$ and $|\psi_2\rangle = \beta_1|u_1\rangle + \beta_2|u_2\rangle$, then the tensor product of $|\psi_1\rangle, |\psi_2\rangle$ is given by:

{% math() %}
\begin{align*}
|\psi_{12}\rangle &= (\alpha_1 |u_1\rangle + \alpha_2 |u_2\rangle) ~\otimes ~(\beta_1|u_1\rangle + \beta_2|u_2\rangle) \\
&= \alpha_1 \beta_1 |u_1\rangle \otimes |u_2\rangle + \alpha_1 \beta_2 |u_1\rangle \otimes |u_2\rangle \\
&\qquad + \alpha_2 \beta_1 |u_2\rangle \otimes |u_1\rangle + \alpha_2 \beta_2 |u_2\rangle \otimes |u_2\rangle
\end{align*}
{% end %}

### A summary of the state-vector formalism

Let's recap what we've covered so far. We have learned that the quantum state is represented as a vector, called a **state-vector**, and written using Dirac (bra-ket) notation as $|\Psi(t)\rangle$. The quantum state "lives" in a **Hilbert space** $\mathcal{H}$, which is complex-valued and can be finite or infinite-dimensional.

In general, the state-vector is a function of time, that is. But if we consider the state-vector at a particular moment in time, for instance, $t = 0$, we can define $|\Psi\rangle = |\Psi(0)\rangle$ to be the _time-independent state-vector_. Depending on the type of system, we can decompose $|\Psi\rangle$ as a superposition of basis vectors $|\alpha\rangle$ as either a sum:

{% math() %}
|\Psi\rangle = \sum_i c_i |\alpha_i\rangle
{% end %}

Or as an integral:

{% math() %}
|\Psi\rangle = \int c(\alpha)|\alpha\rangle~ d\alpha
{% end %}

Such basis vectors must be the **eigenstates** of quantum-mechanical operators that represent **physical quantities** like position, momentum, energy, and spin, which are called **observables**. Their **eigenvalues** are the possible measurable values of the operator (such as possible energies or momenta of a particle); meanwhile, the coefficients $c_i$ (in the discrete case) and $c(\alpha)$ in the continuous case are interpreted as **probability amplitudes**. One can then find the **probability** of measuring the $i$-th eigenvalue of a discrete operator with:

{% math() %}
\mathcal{P}_i = |c_i|^2, \quad c_i = \langle \alpha_i|\psi\rangle
{% end %}

In the continuous case, the probability amplitude $c(\alpha) = \langle \alpha|\psi\rangle$ becomes a continuous function (equivalently, an _infinite-dimensional vector_), which is called the **wavefunction**, and denoted $\psi(\alpha)$. One may obtain the **probability density** $\rho$ of measuring eigenvalue $\alpha$ with:

{% math() %}
\rho = |\psi(\alpha)|^2 = \psi(\alpha)\psi^*(\alpha)
{% end %}

Collectively, these two formulas comprise the **Born rule**. In the case of the special case of the position operator $\hat x$, the eigenvalues of the position $\hat x$ are possible positions $x$, and eigenstates are position eigenstates $|x\rangle$. Thus, the wavefunction takes the form $\psi(x)$, and by the Born rule, taking its squared norm $|\psi|^2$ gives the **probability per unit volume** of measuring a particle at position $x$. In the more general case, we can take the inner product of the state-vector with an arbitrary basis $|\alpha\rangle$ to find the probabilities of measuring its eigenstates.

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
E_\text{total} = \int d^3 \omega~ E_\omega = \sum_k E_k
{% end %}

### Second quantization

Action principle, etc. and then also link to the [advanced classical mechanics guide](@/advanced-classical-mech/index.md) for an overview of tensors and the Euler-Lagrange equations.

To go from classical field theory to quantum field theory:

- Classical equations of motion become _operator_ equations motion (that look the same but have very different properties)
- Classical plane-wave solutions to the field equations become single-particle states of the fields
- Fields have a nonzero energy even when in their lowest-energy state
- Classical oscillating fields become coupled quantum harmonic oscillators


### The spin-statistics theorem