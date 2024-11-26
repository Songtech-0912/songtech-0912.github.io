+++
title = "Advanced quantum mechanics"
date = 2024-07-19
draft = true
+++

This is a mini-book on advanced quantum mechanics, including perturbation theory, applications of quantum mechanics, nuclear physics, semiconductor physics, relativistic quantum mechanics, and quantum field theory.

> **Note:** _It is a work-in-progress. Some sections are not yet complete._

<!-- more -->

## Introduction

Welcome! This is a self-learning guide for all readers that want to venture beyond an introductory quantum mechanics course, targetted for advanced physics students and anyone who is curious and wants a challenge.

The topics covered here will be very broad. 

Quantum field theory (QFT) is the our most accurate description of the universe. The **Standard Model**, a comprehensive quantum field theory, is the backbone of modern physics, and has been tested to extreme precision. Despite this, quantum field theory has a reputation for not being very accessible, in part due to its scary-long Lagrangians and incredibly formidable integrals. So this is an informal self-learning guide to QFT, targetted for 

## Why learn quantum field theory?

All matter in the universe is quantum in nature. Quantum mechanics governs the behavior of all matter, and at an introductory and intermediate level, the dynamics of quantum systems is typically solved with the Schrödinger equation:

{% math() %}
i\hbar \dfrac{\partial}{\partial t} \Psi(\mathbf{r}, t) = \left(-\dfrac{\hbar^2}{2m} \nabla^2 + V(\mathbf{r})\right) \Psi(x, t)
{% end %}

However, relativistic quantum field theory is a far more accurate theory of quantum mechanics than the Schrödinger equation. In fact, while we may use approximations like (semi-)classical theory and nonrelativistic or single-particle quantum mechanics, quantum field theory, and specifically the Standard Model, offers the best and most accurate results. 

That is to say, any quantum system may be solved for by the Schrödinger equation, but doing the same calculations with quantum field theory offers results with unparalleled precision. Predictions of the [magnetic moment of electrons](https://en.wikipedia.org/wiki/Magnetic_moment), [energy levels of the hydrogen atom](https://en.wikipedia.org/wiki/Lamb_shift), a variety of [previously-unknown elementary particles](https://physics.info/standard/), and the [Rydberg constant](https://en.wikipedia.org/wiki/Rydberg_constant) made through quantum field theory have been experimentally tested and confirmed very well. 

These are not meaningless predictions either; our understanding of the emission and absorption of light, subatomic magnetism, and even our standard of time in the [definition of a second](https://en.wikipedia.org/wiki/Second) are based on these predictions. In turn, numerous scientific experiments, material science, laser technology, and electronics depend on applying these predictions, without which they would likely not progress to how they are today.

Quantum field theory is a very rewarding, if difficult, theory to learn. But given its place as the best theory of matter physics ever devised - learning it is worth it.

## What you should know

We'll be working with natural units where $c = \hbar = 1$ simply out of convenience. As this is an informal guide I won't be going through everything in detail. Also, everything will be in tensors, see the [tensors guide](@/tensors-guide.md) if you're not familiar with those. We will be working in the formalism of Lagrangian and Hamiltonian field theory as is standard in physics.

## A few things to clear up

Quantum field theory has a lot of confusing parts, and so it's best to understand these before going too far into it:

- Quantum field theory is **not** string theory, they are distinct theories that share some similarities but are not extensions of each other
- Even though it is mostly used in very specific cases due to its complexity, quantum field theory is a **more fundamental theory** than classical field theory and classical field theory is its limiting case
- The interpretations of PDEs (equations of motion) is **different** in quantum field theory as compared to quantum mechanics; quantum field theory PDEs, even complex-valued ones, have none of the probability interpretation of the Schrödinger equation

## Canonical quantization

Start with a suitable classical Lagrangian of the fields to be studied. If you don't know one and can't copy one from a book or ask someone, then just propose one (i.e. make an educated guess). For instance, if you were studying the electron field, then maybe you would want to use this Lagrangian:

{% math() %}
\mathscr{L} = \overline \psi (i \gamma^\mu \partial_\mu - m) \psi
{% end %}

Plug that Lagrangian into Euler-Lagrange equations, here with $\varphi = \psi(x^\nu)$:

{% math() %}
\frac{\partial \mathscr{L}}{\partial \varphi} - D_\mu \left(\frac{\partial \mathscr{L}}{\partial (\partial_\mu \varphi)}\right) = 0
{% end %}

Then you get the equations of motion of the field (PDEs). E.g. for Higgs field this is the complex-valued Klein-Gordon equation, for quarks & electrons this is the Dirac equation, for photons this is Maxwell's equations. In our case this is the Dirac equation, which describes all matter fields (i.e. those of electrons and quarks, which make up all atoms):

{% math() %}
(i \gamma^\mu D_\mu - m) \psi = 0
{% end %}

The associated quantum fields obey the operator equations of motion, which are the **same** as the PDE equations of motion but operator-valued. For the electron field this is:

{% math() %}
(i \gamma^\mu D_\mu - m) \hat \psi = 0
{% end %}

Where we just made the change $\psi \to \hat \psi$ to get an operator-valued equation of motion. Meanwhile, the electromagnetic field $A^\mu$ satisfies Maxwell's equations:

{% math() %}
\begin{align*}
\partial^\nu \partial_\nu A^\mu = \mu_0 J^\mu
\end{align*}
{% end %}

It is important to note that the Dirac equation takes on a special interpretation in QFT. It in fact becomes a _classical equation of motion_ of a Dirac field $\psi$, rather than a wavefunction. The complex-valued $\psi$ can be thought of as a combination of two real fields $\psi_\alpha$ and $\psi_\beta$ where $\psi = \psi_\alpha + i \psi_\beta$. The physical interpretation of the Dirac field is that it is a field of electrons within space, where the 4-current produced by the electrons is $J^\mu = \psi \gamma^\mu \bar \psi$.

You solve for those operator equations of motion by first solving the PDE equation of motion for the field. Then from there you can promote the field to an operator. I mean, you could solve the operator equation of motion directly but that's annoying, like what does a partial derivative of an operator mean??? so it's easier to just solve the PDE equation of motion and then promote the solution to an operator rather than directly trying to solve the operator equation of motion. For quantum electrodynamics the field operator is:

{% math() %}
\begin{align*}
\hat A^\mu(x) = \int \frac{d^3k}{(2\pi)^3} \sum_{\lambda=1,2} \left( \epsilon^\mu(\mathbf{k}, \lambda) a(\mathbf{k}, \lambda) e^{-ik \cdot x} + \epsilon^{\mu *}(\mathbf{k}, \lambda) a^\dagger(\mathbf{k}, \lambda) e^{ik \cdot x} \right)
\end{align*}
{% end %}

Where $a, a^\dagger$ are creation and annihilation operators, more on that later. 

> **Note:** Remember that this is an _operator_, not a state or function.

After you get the field operator, you then want to construct the series of (eigen)states of the field, from which you can calculate the probability amplitudes of processes. To do so, you find the field Hamiltonian, which has the same expression as the Hamiltonian density in classical field theory, except substituting the classical field with the field operator. For quantum electrodynamics this is:

{% math() %}
\hat{\mathcal{H}}=\sum _{\mathbf {k} ,\mu }\hbar \omega \left({a^{\dagger }}^{(\mu )}(\mathbf {k} )a^{(\mu )}(\mathbf {k} )+{\frac {1}{2}}\right)
{% end %}

Now you want to find the eigenstates of the Hamiltonian (which are the possible states of the field), and specifically, you want to find the ground state. Analogous to the quantum harmonic oscillator's ladder operators, you then find the annihilation (lowering) and creation (raising) operators by commutation relations. Then, by imposing the condition that the annihilation operator applied to the ground state creates the zero (vacuum) state. In the case of quantum electrodynamics the ground state is given by $|0 \rangle$ where:

{% math() %}
\hat a (\mathbf{k}, \lambda)| 0 \rangle = 0
{% end %}

The raising operator can then be used to find all the excited states of the quantum field, just like the quantum harmonic oscillator. Then, we can calculate energy eigenvalues and expectation values associated with each energy eigenstate, and we can calculate the probability of the fields going from one state to another state, which is fundamental to the study of scattering processes. For scattering specifically, we calculate an _S-matrix_ $\hat S$ defined as the operator that acts on an initial state $|i \rangle$ to produce a final state $|f\rangle$ where the probability amplitude is $C$:

{% math() %}
C = \langle f | \hat S | i \rangle
{% end %}

The _S-matrix_ is calculated through what is known as a **Feynman diagram** that represents, graphically, the contributions to the S-matrix integral. For instance, below is the representation of an electron-position annihilation, which produces two photons (in the gamma ray wavelengths):

![A Feynman diagram, showing the electron-positron annihilation interaction in terms on ingoing and outgoing lines](https://upload.wikimedia.org/wikipedia/commons/f/fb/Feynman-diagram-ee-scattering.png)

The ground state, meanwhile, gives the **zero-point energy** of the electromagnetic field. It is not possible in quantum mechanics to have a zero energy vacuum state, because that would violate the energy-time uncertainty principle. Thus, the zero-point energy exists even in a vacuum. In quantum electrodynamics, the expression of the zero-point energy is given by:

{% math() %}
E_0 = \sum_{\lambda = 1, 2} \int \dfrac{d^3 k}{(2\pi)^3} \dfrac{\hbar \omega_\mathbf{k}}{2} - \int \dfrac{d^3 p}{(2\pi)^3} \hbar \omega_\mathbf{p}
{% end %}

This zero-point energy has important implications for cosmology, primarily because while we understand it perfectly well in terms of quantum field theory, we don't understand it well in terms of cosmology. In addition, it gives rise to many quantum effects such as the **Casimir effect**, where a force is observed that acts as a negative pressure pulling two plates together, even in vacuum.

## Effective field theory

So you realize immediately when doing QFT for any amount of time that a lot of calculations end up with integrals that are divergent. Sometimes, there are clever ways to evaluate those integrals to end up with a reasonable value, but sometimes, there isn't. When that's the case, we can use something called **effective field theory**.

Effective field theory is the idea that whenever we are trying to apply quantum field theory, we ask ourselves "how precise do we need the results to be?" From there, we can set an upper bound for the theory in terms of the precision required, and remove all the terms that are suppressed by that upper bound.

As a classical analogy, consider the expression of the kinetic energy in classical mechanics. From a quick wikipedia search, the _relativistic_ kinetic energy is given by the expression:

{% math() %}
K = (\gamma - 1) mc^2 = \frac{mc^2}{\sqrt{1 - (v /c)^2}} - mc^2
{% end %}

Using a Taylor expansion we can write this as:

{% math() %}
K = \frac{1}{2} mv^2 + \frac{3}{8} m \frac{v^4}{c^2} + \dots
{% end %}

But suppose we were interested in scales where $v \ll c$. In this case we can set an upper bound for $v$, what is known in QFT as a [cutoff](https://en.wikipedia.org/wiki/Cutoff_(physics)). Then we can ignore the higher-order terms in the expression of kinetic energy, so it simply becomes:

{% math() %}
K = \frac{1}{2} mv^2
{% end %}

A similar procedure works in QFT. In the perturbative expansion, we ignore higher-order terms.

## Other formulations of quantum field theory

There are other formulations of quantum field theory that I won't cover here:

- Lattice grid QFT
- Algebraic QFT
- Topological QFT
- Conformal field theory
- And, many, many others that each would take a whole book to properly explain

## Computational quantum field theory

Analytical calculations have been the mainstay of quantum field theory for many decades, and it makes sense why: the number of mathematical tricks and divergences to remove makes QFT integrals a nightmare for numerical (computational) methods. Despite this, it is possible to do some parts of QFT computationally.

## An exercise for the reader

You know how some textbooks like to say "the full solution is left as an exercise to the reader?" Well, let's work out a fun exercise for the reader: quantizing gravity!

For gravity, we start with the Lagrangian:

{% math() %}
\mathscr{L} = \frac{1}{16 \pi G} R \sqrt{-g} + \mathscr{L}_{SM} \sqrt{-g}
{% end %}

Solving the Euler-Lagrange equations results in the most general form of the Einstein field equation:

{% math() %}
G_{\mu \nu} + \Lambda g_{\mu \nu} = 8\pi G T_{\mu \nu (SM)}
{% end %}

where $T_{\mu \nu (SM)}$ is the stress-energy tensor (mass-energy field) of all the matter content within spacetime. In QFT, the Einstein field equation becomes an operator-valued equation, so we promote all the fields to operators, resulting in:

{% math() %}
\hat G_{\mu \nu} + \Lambda \hat g_{\mu \nu} = 8\pi G \hat T_{\mu \nu (SM)}
{% end %}

Up to this point, we have been operating within the realm of known physics. We know the right-hand side of this equation: it is simply the combined stress-energy of the standard model. And we know that the left-hand side must hold true, due to the correspondence principle. But we _don't_ know what form the left-hand side must take, that is, what the operators have to be to satisfy this operator equation.

## Referenced sources

- https://www.quora.com/What-is-the-most-complex-Feynman-Diagram
