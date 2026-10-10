+++
title = "In-Depth Quantum Mechanics, Part II"
date = 2025-09-01
+++

We continue our exploration of quantum mechanics in detail in this second part of our series on quantum mechanics. Here, we'll cover the quantum harmonic oscillator, spin, quantization of angular momentum, perturbation theory, and more!

> ### Chapter guide for Quantum Mechanics
> 
> - [Part 1](@/quantum-mechanics/index.md) covers the basic ideas of quantum mechanics and its fundamental formalism.
> - [Part 2](@/quantum-mechanics/part-2.md) covers applications of quantum mechanics as well as more advanced techniques for solving quantum-mechanical systems. **You are reading this part right now.**

_Note: this section is currently incomplete; in particular, advanced quantum theory, scattering (in the Born approximation), and the path integral are not covered. Despite this, it is hoped that the existing content will be of educational interest._

## Introduction to intrinsic spins

To start off, let's get (back) into quantum mechanics by examining the quantum phenomenon of **spin** (more accurately termed _intrinsic spin_, although it is common to just call it "spin" for short).

Intrinsic spin is one of the most important and most fundamentally _quantum_ phenomena, which cannot be explained in classical terms. It refers to the fact that there is a mysterious form of angular momentum that is a fundamental property of subatomic particles, like protons and electrons. This means that certain quantum particles *behave* like tiny spinning magnets, just like classical rotating charged spheres. A full explanation of what spin _is_ in a physical sense, however, is very difficult, since it is so far from any sort of everyday intuition that trying to explain it in terms of concepts of rotation that are familiar to us would be a gross oversimplification.

Historically, spin was accidentally discovered by the **Stern-Gerlach experiment**, first proposed by German physicist [Otto Stern](https://en.wikipedia.org/wiki/Otto_Stern) and then experimentally conducted by [Walther Gerlach](https://en.wikipedia.org/wiki/Walther_Gerlach). 

> **Note:** Despite its name, spin *does not correspond* to the concept of "spinning" particles. The quantum notion of particles - which have no well-defined volume and are essentially zero-dimensional points - means that the very idea of "spinning" quite nonsensical. Even if quantum particles could spin, theoretical calculations quickly show that they would spin faster than the speed of light, which of course is unphysical. In essence, the name "spin" was coined as a historical accident and unfortunately has stuck around to confuse every generation of physicists afterwards.

For particles like electrons (which are called _spin-1/2_ particles for complicated reasons), there are *precisely* two basis states of the spin operators, which are usually called "spin-up" and "spin down" and notated with $|\uparrow \rangle$ and $\langle \downarrow|$ respectively. Thus, we can write out the state-vector of a **spin-1/2 system** as:

{% math() %}
|\Psi\rangle = \alpha |\uparrow\rangle + \beta |\downarrow\rangle
{% end %}

Where $\alpha, \beta$ are the probability amplitudes of measuring the spin-up and spin-down states. Note that the two spin states are orthonormal (that is, $\langle \uparrow|\downarrow\rangle = 0$ and $\langle \uparrow|\uparrow\rangle = \langle \downarrow|\downarrow\rangle = 1$. The **spin operator** $\mathbf{\hat S} = (\hat S_x, \hat S_y, \hat S_z)^T$, which we have already seen, have a very important *physical* meaning: they give the **spin angular momentum** of a spin-1/2 particle. Specifically, they predict that all spin-1/2 particles have an additional angular momentum associated with their intrinsic spin, called the _spin angular momentum_. This is usually represented by $\mathbf{S} = (S_x, S_y, S_z)$, which is a vector of the spin angular momentum of the particle in each coordinate direction.

To accommodate this decidedly non-classical behavior, physicists invented a new operator $\mathbf{\hat S}$, the **spin operator**. The spin operator also has components, which are given by $\mathbf{\hat S} = (\hat S_x, \hat S_y, \hat S_z)$. This gives us three eigenvalue equations, one each for each component of the spin operator:

{% math() %}
\begin{align*}
\hat S_x|\psi\rangle = S_x|\psi\rangle \\
\hat S_y|\psi\rangle = S_y|\psi\rangle \\
\hat S_z|\psi\rangle = S_z|\psi\rangle
\end{align*}
{% end %}

This tells us that $S_x, S_y, S_z$ are the **eigenvalues** of the spin operators along the $x$, $y$, and $z$ axes (respectively). A remarkable result that defies all classical intuition is that these eigenvalues are constrained to only one of two values: $\hbar/2$ or $-\hbar/2$. That is to say:

{% math() %}
S_x = \pm \dfrac{\hbar}{2}, \quad S_y = \pm \dfrac{\hbar}{2}, \quad S_z = \pm \dfrac{\hbar}{2}
{% end %}

> **Note:** We will rarely refer to the spin operator $\mathbf{\hat S}$ and usually just discuss its components $\hat S_x, \hat S_y, \hat S_z$. Thus, if we say "spin operator along $x$" we mean $\hat S_x$, not $\mathbf{\hat S}$.

Meanwhile, the _direction_ of the spin angular momentum depends on the specific eigenstate. For instance, the **spin-up eigenstate** of the $\hat S_z$ operator tells us that the particle's spin angular momentum points along $+z$. Similarly, the **spin-down eigenstate** of the $\hat S_z$ operator tells us that the particle's spin angular momentum points along $-z$. It is important to note that the direction of the spin angular momentum vector has _no correspondence_ with a particle's actual orientation. It *only* tells us information about where the particle's *spin angular momentum* points and is (usually) only relevant for understanding a particle's interaction with magnetic fields.

> **Note:** It is often the case that we just say "spin" as opposed to "spin angular momentum", although technically the latter is the correct terminology. However, in the interest of simplicity, we will call both "spin" wherever convenient.

To make things more concrete, the spin operators in the matrix representation are given by:

{% math() %}
\begin{align*}
\hat S_x = \frac{\hbar}{2} \sigma_x, \quad \sigma_x &= \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \\
\hat S_y = \frac{\hbar}{2} \sigma_y, \quad \sigma_y &= \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix} \\
\hat S_z = \frac{\hbar}{2} \sigma_z, \quad \sigma_z &= \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}
\end{align*}
{% end %}

> **Note:** $\sigma_x, \sigma_y, \sigma_z$ are the **Pauli matrices**, which have eigenvalues $\pm 1$. Since the spin operators are just the Pauli matrices multiplied by a factor of $\hbar/2$, the eigenvalues of the all three spin operators are just a factor of $\hbar/2$ multiplied by the eigenvalues of the Pauli matrices (which are $\pm 1$). It is also useful to note that all three have **determinant** of $-1$ and **zero trace**. Other information can be found on its [wikipedia page](https://en.wikipedia.org/wiki/Pauli_matrices)

Meanwhile, the eigenstates of the spin operators are called **spinors** (or [eigenspinors](https://en.wikipedia.org/wiki/Eigenspinor)). They are often written as $|\uparrow_x\rangle$ and $|\downarrow_x \rangle$ to indicate whether they are spin-up or spin down eigenstates (indicated by the direction of the arrows), which corresponds directly to what direction the spin angular momentum points towards ($x$, $y$, or $z$).

> **Note:** Another common notation is to use $|+\rangle_x, |-\rangle_x$ for spin-up and spin-down states respectively, though this can clutter things up so we'll avoid it.

The explicit forms of the spinors associated with the spin operators $\hat S_x, \hat S_y, \hat S_z$ are given by:

{% math() %}
\begin{align*}
|\uparrow_x\rangle &= \dfrac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ 1 \end{pmatrix}, \quad
|\downarrow_x\rangle = \dfrac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ -1 \end{pmatrix} \\
|\uparrow_y\rangle &= \dfrac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ i \end{pmatrix}, \quad
|\downarrow_y\rangle = \dfrac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ -i \end{pmatrix} \\
|\uparrow_z\rangle &= \begin{pmatrix} 1 \\ 0 \end{pmatrix},\quad\qquad 
|\downarrow_z\rangle = \begin{pmatrix} 0 \\ 1 \end{pmatrix} \\
\end{align*}
{% end %}

For calculations, it is frequently useful to reference certain identities of the Pauli matrices and spin operators. For instance, a very useful one is that:

{% math() %}
\sigma_x^2 = \sigma_y^2 = \sigma_z^2 = \hat I
{% end %}

Where $\hat I$ is the identity matrix. The spin operators and Pauli matrices also satisfy the below commutation relations:

{% math() %}
\begin{align*}
[\sigma_x, \sigma_y] &= 2i\sigma_z \\
[\sigma_j, \sigma_k] &= 2i\varepsilon_{jkl}\sigma_l \\
[\hat S_x, \hat S_y] &= i\hbar \hat S_z \\
[\hat S_y, \hat S_z] &= i\hbar S_x \\
[\hat S_z, \hat S_x] &= i\hbar \hat S_y
\end{align*}
{% end %}

In addition, some other useful identities are:

{% math() %}
\begin{gather*}
\sigma_j \sigma_k + \sigma_k \sigma_j = 2\delta_{jk} \\
[\hat S^2, \hat S_x] = [\hat S^2, \hat S_y] = [\hat S^2, \hat S_z] = 0
\end{gather*}
{% end %}

Where $\hat S^2 = \mathbf{\hat S}\cdot\mathbf{\hat S}$ is the squared spin operator, which will be *very* important when we discuss more types of angular momentum in quantum mechanics. Finally, we have the all-important **Pauli identity**:

{% math() %}
\sigma_i \sigma_j = \delta_{ij} + i\varepsilon_{ijk}\sigma_k, \quad i,j \in (x, y, z)
{% end %}

Where $\delta_{ij}$ (as we've seen before) is the Kronecker delta, defined as:

{% math() %}
\delta_{ij} = \begin{cases}
1 & i = j \\
0 & i \neq j
\end{cases}
{% end %}

And $\varepsilon_{ijk}$ is called the [Levi-Civita symbol](en.wikipedia.org/wiki/Levi-Civita_symbol) (or _Levi-Civita tensor_), and is given by:

{% math() %}
\varepsilon_{ijk}=
\begin{cases}+1&{\text{if }}(i,j,k){\text{ is }}(1,2,3),(2,3,1),{\text{ or }}(3,1,2),\\-1&{\text{if }}(i,j,k){\text{ is }}(3,2,1),(1,3,2),{\text{ or }}(2,1,3),\\\;\;\,0&{\text{if }}i=j,{\text{ or }}j=k,{\text{ or }}k=i
\end{cases}
{% end %}

> **Note:** A very useful property of the Levi-Civita symbol is that it can be used to define the cross product of two vectors $\mathbf{A} \times \mathbf{B}$ via {% inlmath() %}(\mathbf{A} \times \mathbf{B})_i = \varepsilon_{ijk} A_i B_j{% end %}. There is also the so-called [permutation definition](https://en.wikipedia.org/wiki/Levi-Civita_symbol#Three_dimensions) of the Levi-Civita symbol, although we will not cover that here.

While the eigenstates of the $\hat S_x, \hat S_y, \hat S_z$ operators are distinct, it is possible to express eigenstates in one particular spin basis as a superposition of eigenstates in another spin basis. For instance, the eigenstates of the $\hat S_x$ operator can be written in terms of the eigenstates of the $\hat S_z$ operator:

{% math() %}
\begin{align*}
|\uparrow_x\rangle &= \frac{1}{\sqrt{2}} \left(|\uparrow_z\rangle + |\downarrow_z\rangle\right) \\ 
|\downarrow_x\rangle &= \frac{1}{\sqrt{2}} \left(|\uparrow_z\rangle - |\downarrow_z\rangle \right)
\end{align*}
{% end %}

Likewise, the eigenstates of the $\hat S_y$ operator can be written in terms of the eigenstates of the $\hat S_z$ operator:

{% math() %}
\begin{align*}
|\uparrow_y\rangle &= \frac{1}{\sqrt{2}} \left(|\uparrow_z\rangle + i |\downarrow_z\rangle\right) \\ |\downarrow_y\rangle &= \frac{1}{\sqrt{2}} \left(|\uparrow_z\rangle - i |\downarrow_z\rangle\right)
\end{align*}
{% end %}

> **Historical note:** Interestingly, Wolfgang Pauli, for which the Pauli matrices are named, did not initially even like matrices (or linear algebra for that matter) being there in quantum mechanics! He once said of Schrödinger (to Max Born), _"Yes, I know you are fond of tedious and complicated formalism. You are only going to spoil Heisenberg's physical idea by your futile mathematics"_. Funnily enough, he would eventually be most remembered for the his contribution to matrix mechanics and in describing spin, something he had once furiously railed against! (See the [first comment on this Physics SE answer](https://hsm.stackexchange.com/a/17997)).

### Spin and the Stern-Gerlach experiment

The fact that the spin operator tells us that spin-1/2 particles have *additional* angular momentum not predicted by classical physics has a profound implication: it means that any two otherwise identical spin-1/2 particles (for instance, electrons) will behave *differently* in a magnetic field. The magnetic force exerted on a classical charged particle with [magnetic moment](https://en.wikipedia.org/wiki/Magnetic_moment) $\vec{\boldsymbol{\mu}}$ is given by $\mathbf{F}_B = -\nabla(\vec{\boldsymbol{\mu}} \cdot \mathbf{B})$, where $\mathbf{B}$ is the magnetic field, and $\vec{\boldsymbol{\mu}}$ is given by:

{% math() %}
\vec{\boldsymbol{\mu}} = g\dfrac{q}{2m} \mathbf{S}, \quad g \approx 2
{% end %}

> **Note:** The **magnetic moment** $\vec{\boldsymbol{\mu}}$ is the vector that measures the orientation of the magnetic field associated with an electric charge. A *nonzero* magnetic moment causes a charge to *align* with (or against) an external magnetic field, an effect that can be measured very precisely and is used in a variety of applications.

Since two randomly-chosen electrons would most likely have (and in some cases, *must have*) different spins, they would have opposite magnetic moments, and thus be deflected in different ways due to the magnetic force. Unknowingly taking advantage of the phenomenon, Stern and Gerlach conducted an experiment (shown in the diagram below) that showed a beam of silver atoms would split into two in a magnetic field, experimentally confirming the prediction of spin from quantum theory. This, again, is because electrons with different spins are deflected in *opposite directions* by the magnetic field, leading to the beam splitting into two (one of spin-up electrons and one of spin-down electrons).

![A diagram of the Stern-Gerlach experiment. A beam of silver atoms is passed through a magnetic field, leading to the beam diverging due to the opposite angular momenta of spin-up and spin-down particles](https://www.informationphilosopher.com/solutions/experiments/stern_gerlach/Stern-Gerlach.png)

_A diagram of the Stern-Gerlach experiment. Source: [The Information Philosopher](https://www.informationphilosopher.com/solutions/experiments/stern_gerlach/)_

### Repeated measurements of spin

We saw previously that all three spin operators **don't commute** with each other; for instance, $[\hat S_x, \hat S_y] = i\hbar \hat S_z$. This is not just a mathematical peculiarity! In quantum mechanics, remember that any two operators that *do not commute* represent observables that **cannot be simultaneously measured to arbitrary precision**. In formal terms, the uncertainty principle tells us that for two non-commuting operators $\hat A, \hat B$, where $[\hat A, \hat B] = i\hat C$, then:

{% math() %}
\Delta A \Delta B \geq \dfrac{|\langle \hat C\rangle|}{2}
{% end %}

For instance, in the case of the position and momentum operators (where $[\hat x, \hat p] = i\hbar$), this reduces to the famous **Heisenberg uncertainty principle**:

{% math() %}
\Delta x \Delta p \geq \frac{\hbar}{2}
{% end %}

The consequence of the uncertainty principle is that if you measure one observable $A$ and then measure another observable $B$, if $\hat A, \hat B$ *do not commute*, then:

1. They cannot *both be measured simultaneously* to perfect accuracy, and
2. A measurement of one observable *tells you nothing* about the other observable

Let's break down what this means. Suppose you had an electron which initially is know to be spin-up along $z$. Mathematically, you know the precise value of the $\hat S_z$ operator (spin operator in the z direction): there is **100% probability** that the electron is in the spin-up state along the $z$ axis. What happens if you measure the electron's spin along $x$? Well, the electron is **equally likely** to be spin-up or spin-down along the $x$ axis because of rule (2). We already saw that $[\hat S_z, \hat S_x] \neq 0$ (that is, the spin operators along $z$ and $x$ *do not* commute), so knowing $S_z$ (the electron's spin along $z$) tells you nothing about $S_x$.

Now, what happens if you measure the electron's spin along $z$ again? "This is a pointless question!", you may say, "since I already measured the electron to be in the spin-up state along $z$, so it must certainly be in that same state!" However, things are not *quite* so simple. Remember that since the spin operators along $z$ and $x$ do not commute, measuring $S_x$ tells you nothing about $S_z$ (and vice-versa). This means that if you know $S_x$, you would not know *anything* about $S_z$ prior to measuring it. Since you had measured $S_x$, if you then choose to measure $S_z$, it would be a contradiction if the electron's spin along $z$ could also be precisely known to be in one state. Thus we are left with the profound and puzzling conclusion that upon measuring $S_z$ after $S_x$, the electron is again **equally likely** to be spin-up or spin-down along the $z$ axis. The previous information you had about the electron - namely, that it was in the spin-up state along $z$ - has now been erased!

### Larmor precession

If we think about a spinning top rotating on a table, it will rotate round and round in a circle tilted at an angle (until it inevitably falls). This phenomenon is known as **precession**, and is shown in the animation below:

![A gyroscope rotating at an angle, showcasing precession](https://upload.wikimedia.org/wikipedia/commons/8/82/Gyroscope_precession.gif)

_Source: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Gyroscope_precession.gif)_

The reason why everyday precession happens is that the Earth's gravity produces a torque on the spinning top. But since it is also spinning, the top has *angular momentum* which resists the torque, leading to the gyroscope rotating at an angle. In physics, the gyroscope is said to _precess_. But angular momentum is not just found in the classical world: it is *also* found in the quantum world, and it leads to an effect called **Larmor precession**.

To understand Larmor precession, recall that we earlier noted that spin-1/2 particles have an *intrinsic angular momentum* that comes from their spin. We have notated this angular momentum as $\mathbf{S}$, as it is the **spin angular momentum**, and we know it must have a magnitude of $\pm \hbar/2$ along any axis (so long as it is a spin-1/2 particle). This angular momentum creates a magnetic moment $\vec{\boldsymbol{\mu}}$ associated with the particle, given by:

{% math() %}
\vec{\boldsymbol{\mu}} = \gamma \mathbf{S}
{% end %}

Here, $\gamma$ is known as the **gyromagnetic ratio**, and it is a constant that can be calculated from the mass, charge, and other characteristics of the particle in question. From the magnetic moment, we can construct a Hamiltonian for a spin-1/2 particle placed in an applied magnetic field $\mathbf{B}$ with the spin operator $\mathbf{\hat S}$, given by:

{% math() %}
\hat H = -\vec{\boldsymbol{\mu}} \cdot \mathbf{B} = -\gamma(\mathbf{\hat S} \cdot \mathbf{B})
{% end %}

It is usually easiest to consider a magnetic field aligned along the $z$-direction, and thus we have:

{% math() %}
\hat H = -\gamma \hat S_z B_z
{% end %}

By solving for the eigenvalues and eigenstates of the Hamiltonian, we get two spin eigenstates, which are respectively given by:

{% math() %}
|\uparrow_z\rangle = \begin{pmatrix} 1 \\ 0 \end{pmatrix},\quad 
|\downarrow_z\rangle = \begin{pmatrix} 0 \\ 1 \end{pmatrix}
{% end %}

Meanwhile, the energy eigenvalues are given by:

{% math() %}
E_{\pm z} = \pm \frac{1}{2}\hbar \gamma B_z
{% end %}

This tells us that we have two distinct energy eigenstates: the first one with higher energy, and the second one with lower energy. The energy difference between the two energy levels can be written in terms of the **Larmor frequency** $\omega_0$ via:

{% math() %}
\begin{align*}
\Delta E &= E_+ - E_- \\
&= \hbar \gamma B_z \\
&= \hbar \omega_0, \quad \omega_0 \equiv |\gamma B_z|
\end{align*}
{% end %}

Physically, when a magnetic field is applied, we say that the magnetic moments of a spin-1/2 particle **precess**, since they rotate (just like a gyroscope) to line up along or against the magnetic field. This type of precession is called **Larmor precession**, and it is very similar to the classical precession of a gyroscope, with some notable differences being that there is nothing physically "rotating" at an angle; rather, it is the *magnetic moment vector* that becomes tilted off-axis, which is why we term it as _precession_. 

![A diagram showing Larmor precession, where the magnetic moment vector rotates in a circle at an angle due to spin-magnetic-field interactions](https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Precession_in_magnetic_field.svg/120px-Precession_in_magnetic_field.svg.png)

_A diagram of Larmor precession. Source: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Precession_in_magnetic_field.svg)_

Precise measurements of Larmor precession are essential in many areas of science, especially in **nuclear magnetic resonance (NMR) spectroscopy**, which is used in the medical sciences, as well as biotechnology and biochemistry. Additionally, many electronic devices (like hard disk storage) relies on exploiting the effects of spin, with an entire field of [spintronics]([https://en.wikipedia.org/wiki/Spintronics](https://en.wikipedia.org/wiki/Spintronics) devoted to research in this area. With so many observations proving the existence of spin, we know for certain that even if spin runs counter to our intuitions (pun intended!), it is nevertheless a very real aspect of the quantum world.

### Generalized two-level systems

We will close our introductory discussion of spin and the ways to analyze spin by quickly discussing the generalization of a spin-1/2 system: **two-level systems**. Two-level systems (that is, a quantum system with two degrees of freedom) are found throughout quantum mechanics. Since spin-1/2 particles can either be spin-up or spin-down, which are the only two possible states in a spin-1/2 system, it is the **prototypical two-level system**. However, it is by no means unique: there are other two-level systems out there, and they can often be modelled using the same tools. For instance, it is very common to see Hamiltonians of the form:

{% math() %}
\hat H \propto \sigma_i
{% end %}

Where $\sigma_i \in [\sigma_x, \sigma_y, \sigma_z]$ is a Pauli matrix, and they obey: 

{% math() %}
\begin{align*}
[\sigma_x, \sigma_y] =  \sigma_z \\
[\sigma_y, \sigma_z] =  \sigma_x \\
[\sigma_z, \sigma_x] =  \sigma_y
\end{align*}
{% end %}

### The Bloch sphere

A common generalization of the spin-1/2 system we have discussed at length is known as the **Bloch sphere**. The Bloch sphere is a formulation of a generalized two-level system with two states, which we notate as $|0\rangle$ and $|1\rangle$. Here, $|0\rangle$ is the ground state, so it is associated with a lower energy, whereas $|1\rangle$ is the excited state, so it is associated with a higher energy.

The Bloch sphere (illustrated in the diagram below) allows us to visualize the abstract space in which these states "live", much like the complex plane can be drawn as a 2D coordinate grid. The state space of the system is parametrized in spherical coordinates by the angles $(\theta, \phi)$ - it is important to note that these _aren't_ physical locations in space, but are rather located in the abstract Hilbert space of the two-state system.

{{ diagram(
  src="https://upload.wikimedia.org/wikipedia/commons/f/f0/Bloch_Sphere_representation.svg"
  desc="A visualization of the Bloch sphere"
) }}

_An illustration of the Bloch sphere. Source: [Wikipedia](https://en.wikipedia.org/wiki/File:Bloch_Sphere_representation.svg)_

On the Bloch sphere, $|0\rangle$ "lives" at the north pole of the Bloch sphere, and $|1\rangle$ "lives" at the south pole. Other states of the system lie somewhere between the two poles. The general state-vector of the system can thus be written as:

{% math() %}
|\psi\rangle = \cos\left( \frac{\theta}{2} \right) |0\rangle + e^{i\phi} \sin\left( \frac{\theta}{2} \right) |1\rangle
{% end %}

Where $e^{i\phi}$ is the phase of the state-vector, and where the basis states are given by:

{% math() %}
|0\rangle = 
\begin{pmatrix}
1 \\ 0
\end{pmatrix}, \quad
|1\rangle =
\begin{pmatrix}
0 \\ 1
\end{pmatrix}
{% end %}

> **Note:** in the standard convention, the $x$ axis represents the **real part** of the phase, whereas the $y$ axis represents the **imaginary part** of the phase.

In the case that the two-level system models a spin-1/2 particle (a very common but not universal case), then we have:

{% math() %}
|\psi\rangle = \cos\left( \frac{\theta}{2} \right) |\uparrow\rangle + e^{i\phi} \sin\left( \frac{\theta}{2} \right) |\downarrow\rangle
{% end %}

> **Note:** the choice is mathematically-arbitrary, so it does not matter whether we call $|0\rangle$ the spin-up or spin-down state, as long as our choice is consistent. However, $|\uparrow\rangle$ is usually associated with $|0\rangle$ in physics and engineering, and likewise $|\downarrow\rangle$ is usually associated with $|1\rangle$.

Along the "equator" of the Bloch sphere, we have $\theta = \pi/2$, and thus the state-vector takes the simpler form:

{% math() %}
|\psi\rangle = \frac{1}{\sqrt{ 2 }}\big(|0\rangle + e^{i\phi}|1\rangle\big)
{% end %}

Note that this corresponds to a state with 50% probability of measuring $|0\rangle$ and $|1\rangle$ since the complex phase factor has unit magnitude (you can check it for yourself by computing $P_0 = |\langle 0|\psi\rangle|^2$ and $P_1 = |\langle 1|\psi\rangle|^2$). However, the phase is still physically-relevant

#### Hamiltonian of a generalized two-level system

A very common basic Hamiltonian for a generalized two-level system is given by:

{% math() %}
\hat{H} = \frac{\hbar \omega}{2} \sigma_{z}
{% end %}

The energy eigenvalues are then $E = \pm \frac{1}{2} \hbar \omega$, with an energy difference of $\Delta E = \hbar \omega$ between the ground state and the excited state. Thus, the general time-dependent state-vector of the system, valid for all $t$, is given by:

{% math() %}
|\psi(t)\rangle = \cos\left( \frac{\theta}{2} \right) |0\rangle e^{-i \omega t/2} + e^{i\phi} \sin\left( \frac{\theta}{2} \right) |1\rangle e^{i \omega t/2}
{% end %}

This comes from tacking on a factor of $e^{-i E t/\hbar}$ to each of the eigenstates, and substituting in our known values of $E = \pm \frac{1}{2}\hbar\omega$. It is standard to factor out the phase factor of $e^{-i\omega t/2}$, giving us:

{% math() %}
\begin{align*}
|\psi(t)\rangle &= e^{-i \omega t/2}\left[\cos\left( \frac{\theta}{2} \right) |0\rangle  + e^{i\phi} \sin\left( \frac{\theta}{2} \right) |1\rangle e^{i \omega t} \right] \\
&= e^{-i \omega t/2}\left[\cos\left( \frac{\theta}{2} \right) |0\rangle  + e^{i(\phi +  \omega t)} \sin\left( \frac{\theta}{2} \right) |1\rangle\right]
\end{align*}
{% end %}

Since the factor $e^{-i\omega t/2}$ is a phase factor, its magnitude is one, and thus it is not directly observable; thus, the physics of the system are identical if it is dropped. Defining $\phi_{r}(t) = \phi + \omega t$ as the **relative phase** of the system (since it is a phase that comes from the _difference_ in energy of the two states, which is a relative quantity), we can rewrite the state-vector as:

{% math() %}
|\psi(t)\rangle = \cos\left( \frac{\theta}{2} \right) |0\rangle  + e^{i\phi_{r}(t)} \sin\left( \frac{\theta}{2} \right) |1\rangle
{% end %}

As long as the system is undisturbed and the Hamiltonian is time-independent, the relative phase $\phi_r$ changes by a *constant* rate $\omega$ (the **Larmor frequency**) as the state-vector precesses along the Bloch sphere - note this is independent of the $\theta$ coordinate! If we imagine the state-vector of the system to be represented by an arrow, the change in the relative phase can be visualized as the rotation of this "arrow" as it precesses (i.e. rotates) around the Bloch sphere.

> **Note:** For an application of the Bloch sphere in quantum optics, please see [these lecture notes](https://www.wbt.uni-rostock.de/storages/uni-rostock/Alle_MNF/Physik_Qms/Lehre_Scheel/quantenoptik/Quantenoptik-Vorlesung10.pdf).

### Conclusion to two-level systems

Two-level systems are the fundamental model behind a vast variety of quantum systems, including [qubits](https://qubit.guide) in quantum computing, [optically-pumped lasers](https://en.wikipedia.org/wiki/Rabi_cycle), and [molecular ions](https://web1.eng.famu.fsu.edu/~dommelen/quantum/style_a/hion.html), as well as playing an important role in understanding the emission and absorption of radiation at the quantum level. We will discuss more examples of them throughout this guide - stay tuned!

## The quantum harmonic oscillator

One of the simplest, but most important quantum systems is the **quantum harmonic oscillator**. At face value, it describes a particle in a harmonic potential well. To start, let us recall that the classical harmonic potential is given by:

{% math() %}
V(x) = \dfrac{1}{2} kx^2 = \dfrac{1}{2} m\omega^2 x^2, \quad \omega \equiv \sqrt{k/m} 
{% end %}

The classical solutions to the (classical) harmonic oscillator are in terms of sinusoidal functions, which is why it is indeed called the *harmonic* oscillator. However, on a basic level, a harmonic potential is nothing more than a basic quadratic potential, one that we show in the below diagram:

{{ diagram(
	src="harmonic-potential.excalidraw.svg"
	desc="A plot of the harmonic potential, showing that it has an energy that is quadratic with the potential and symmetric about the x-axis"
) }}

In quantum mechanics, we retain the same form of the harmonic potential, except we perform the substitution $x \to \hat x$, where $\hat x$ is the position operator. Thus the Hamiltonian is given by:

{% math() %}
\hat H = \dfrac{\hat p^2}{2m} + V(x) = \dfrac{\hat p^2}{2m} + \dfrac{1}{2} m\omega^2 \hat x^2
{% end %}

Note that we can also write this in the position representation (where $\hat x = x$ and $\hat p = -i\hbar \frac{d}{dx}$ in 1D) as:

{% math() %}
\hat H = -\frac{\hbar^2}{2m} \dfrac{d^2}{dx^2} + \frac{1}{2} m \omega^2 x^2
{% end %}

The quantum harmonic oscillator is a very useful model in quantum mechanics, since it is one of the few problems that can be solved exactly. This *does not* mean it is trivial - the quantum harmonic oscillator finds numerous applications in molecular and atomic physics. The quantum harmonic oscillator can first be used as an approximation for a complicated potential. This is because the Taylor expansion of an *arbitrary* potential centered at $x = x_0$ is given by:

{% math() %}
V(x) = V_0 + V'(x-x_0) + \dfrac{1}{2} V''(x-x_0)^2 + \dfrac{1}{6} V'''(x-x_0)^3 + \dots
{% end %}

Another application is to describe the interaction of a charged (quantum) particle with an *standing electromagnetic waves*, something we will discuss later. When an electromagnetic field is trapped in some cavity, it decomposes into a series of modes, whose wavelength can only come in quantized values:

{% math() %}
\omega = \dfrac{2\pi c}{\lambda}, \quad \lambda = \dfrac{2L}{n}, \quad n = 1,2,3, \dots
{% end %}

Thus, any charged particle within such a cavity will interact with the standing waves of the electromagnetic field, leading to its energy levels being quantized. This is the origin of uniquely quantum phenomena such as the [Stark effect](https://en.wikipedia.org/wiki/Stark_effect), but we'll explain this in more detail later.

The third main application of the quantum harmonic oscillator is to describe the interaction of a particle with a quantized electromagnetic field, which is the realm of **quantum electrodynamics** and _second quantization_. While this can get complicated very quickly, the essence is to describe the quantized electromagnetic field as a series of coupled harmonic oscillators. We will cover this more at the very end of this guide.

To solve the quantum harmonic oscillator we begin with the same general methods as for essentially any quantum system - to write out the eigenvalue equation for the Hamiltonian:

{% math() %}
\hat H|\psi\rangle = E|\psi\rangle
{% end %}

This is the starting point, and there are several different ways to proceed from here. For instance, we can solve the eigenvalue equation in the position basis by taking the inner product with a position basis ket:

{% math() %}
\begin{gather*}
\langle x|\hat H|\psi\rangle = \langle x|E|\psi\rangle \\
\langle x|\hat H|\psi\rangle = E\langle x|\psi\rangle \\
\left\langle x \left|-\dfrac{\hbar^2}{2m}\dfrac{d^2}{dx^2} + \dfrac{1}{2} m\omega^2 \hat x^2\right|\psi\right\rangle = E\langle x|\psi\rangle \\
\Rightarrow -\dfrac{\hbar^2}{2m}\dfrac{d^2 \psi}{dx^2} + \dfrac{1}{2} m\omega^2 x^2 \psi(x) = E \psi(x)
\end{gather*}
{% end %}

This is a differential equation that can indeed be solved, although it is not very easy to solve. Indeed, a much better approach is to use the so-called _algebraic approach_, which originated with the physicist Paul Dirac, which we'll now discuss.

### The ladder operator approach

Dirac's key insight in solving the quantum harmonic oscillator is to "factor" the Hamiltonian by defining two new operators $\hat a$ and $\hat a^\dagger$, given by:

{% math() %}
\begin{align*}
\hat a &= \dfrac{1}{\sqrt{2}}(\hat x'+ i\hat p') \\
\hat a^\dagger &= \dfrac{1}{\sqrt{2}}(\hat x' - i\hat p')
\end{align*}
{% end %}

Where $\hat x', \hat p'$ are related to the position and momentum operators $\hat x, \hat p$ as follows:

{% math() %}
\hat x' = \sqrt{\dfrac{m\omega}{\hbar}} \hat x, \quad \hat p' = \dfrac{1}{\sqrt{m\hbar \omega}} \hat p
{% end %}

It is also useful to note that:

{% math() %}
\begin{align*}
\hat x' &= \frac{1}{\sqrt{2}}(\hat a^\dagger + \hat a) \\ 
\hat p' &= \dfrac{i}{\sqrt{2}}(\hat a^\dagger - \hat a) \\
\end{align*}
{% end %}

$\hat a$ and $\hat a^\dagger$ are conventionally called the **ladder operators**. These two operators satisfy $[\hat a, \hat a^\dagger] = 1$, an important identity to keep in mind for later. While many steps avoid using this approach and write $\hat a$ and $\hat a^\dagger$ _purely_ in terms of $\hat x$ and $\hat p$, by defining our new operators $\hat x', \hat p'$ we can *non-dimensionalize* the problem, making it easier to solve. This is essentially the same thing as a change of variables in a classical mechanics problem, only here we're using operators, not classical functions.

> **Note:** While $\hat a$ and $\hat a^\dagger$ are indeed adjoints of each other, it is common to consider them essentially separate operators (for reasons we'll soon see). It is also common to use the notation $(\hat a_-, \hat a_+)$ instead of $(\hat a, \hat a^\dagger)$ (where $\hat a_- = \hat a$ and $\hat a_+ = \hat a^\dagger$) which is a completely equivalent notation.

Thus, with our operators $\hat x'$ and $\hat p'$, the Hamiltonian can be written as:

{% math() %}
\hat H = \hbar \omega \hat H', \quad \hat H' = \dfrac{1}{2}(\hat x'^2 + \hat p'^2)
{% end %}

These operators allow us to simplify the Hamiltonian down greatly, since we find that:

{% math() %}
\begin{align*}
\hbar \omega\left(\hat a^\dagger \hat a + \frac{1}{2}\right) &= \hbar \omega\left(\frac{1}{2}(\hat x' + i\hat p')(\hat x' - i\hat p') + \frac{1}{2}\right)\\
&= \dfrac{1}{2}\hbar \omega \left(\hat x'^2 - i\hat x' \hat p' + i\hat x' \hat p' + \hat p'^2 + 1\right) \\
&= \dfrac{1}{2}\hbar \omega(\hat x'^2 + \hat p'^2 + i[\hat x', \hat p'] + 1) \\
&= \dfrac{1}{2}\hbar \omega(\hat x'^2 + \hat p'^2 -1 + 1) \\
&= \hbar \omega H' \\
&= \hat H
\end{align*}
{% end %}

If one defines another new operator $\hat N$ (we will discuss what this means later), given by $\hat N = \hat a^\dagger \hat a$, then the Hamiltonian takes the form:

{% math() %}
\hat H = \hbar \omega \left(\hat N + \dfrac{1}{2}\right)
{% end %}

> **Note:** Be careful of the order of the $\hat a$ and $\hat a^\dagger$ operators! This is because $\hat N = \hat a^\dagger \hat a$, but $\hat a^\dagger \hat a \neq \hat a \hat a^\dagger$ so $\hat N \neq \hat a \hat a^\dagger$! Indeed we find that $\hat a \hat a^\dagger = 1 + \hat N$, which can be derived from the commutation relation $[\hat a, \hat a^\dagger] = 1$.

The genius of using this operator-based "algebraic" approach to solving the quantum harmonic oscillator is that the $\hat a, \hat a^\dagger$ operators satisfy:

{% math() %}
\hat a|\psi_0\rangle = 0, \quad \hat a^\dagger |\psi_0\rangle = |\psi_1\rangle
{% end %}

In fact, in the general case, we find that for the $n$-th eigenstate $|\psi_n\rangle$ we have:

{% math() %}
\hat a|\psi_n\rangle = \sqrt{n}|\psi_{n - 1}\rangle, \quad \hat a^\dagger|\psi_n\rangle = \sqrt{n + 1}~|\psi_{n + 1}\rangle
{% end %}

It is common convention to indicate the $n$-th eigenstate of the quantum harmonic oscillator with $|n\rangle = |\psi_n\rangle$, in which case one may write the more elegant expression:

{% math() %}
\hat a|n\rangle = \sqrt{n}~|n-1\rangle, \quad \hat a^\dagger|n\rangle = \sqrt{n+1}~|n + 1\rangle
{% end %}

Thus we again find that $\hat a|0\rangle = \hat a|\psi_0\rangle = 0$ and $\hat a^\dagger |0\rangle = \hat a|\psi_0\rangle = |\psi_1\rangle$. These are indeed the chief identities of the quantum harmonic oscillator, because if we substitute in the definitions of the $\hat a, \hat a^\dagger$ operators, we have:

{% math() %}
\begin{align*}
\hat a^\dagger \hat a|n\rangle &= \hat a^\dagger(\sqrt{n}~|n+1\rangle) \\
&= \sqrt{n^2} |(n + 1) - 1\rangle \\
&= n|n\rangle
\end{align*}
{% end %}

But we already know that $\hat a^\dagger \hat a$ is just the $\hat N$ operator, so we therefore have:

{% math() %}
\hat
N|n\rangle = n|n\rangle
{% end %}

In addition, we have:

{% math() %}
\begin{align*}
\hat a^\dagger\hat a|n\rangle &= \hat N|n\rangle 
= n|n\rangle \\
\hat a \hat a^\dagger|n\rangle &= (\hat N + \hat I)|n\rangle 
= (n + 1)|n\rangle
\end{align*}
{% end %}

 The $\hat N$ operator is often called the **number operator** since it returns the index $n$ corresponding to the *nth* eigenstate. For instance, for the first eigenstate $|0\rangle$ (in more traditional notation, this can be written as $|\psi_0\rangle$, which is equivalent), $\hat N|0\rangle = 0$, which tells us that (as we expect) the first eigenstate is labelled with index $n = 0$. Likewise, for the eigenstate $|3\rangle$ then $\hat N|3\rangle = 3 |n\rangle$, which indeed returns its index $n = 3$. What makes it *particularly* special is how the number operator can be defined solely in terms of the $\hat a$ and $\hat a^\dagger$ operators, which is a very non-trivial result. Thus, if we substitute $\hat N|n\rangle = n|n\rangle$ into our Hamiltonian, we have:

{% math() %}
\hat H|n\rangle = \hbar \omega \left(\hat N + \dfrac{1}{2}\right)|n\rangle = \underbrace{\hbar \omega \left(n + \dfrac{1}{2}\right)}_{E_n}|n\rangle
{% end %}

Where by comparison our expression with the Hamiltonian's eigenvalue equation $\hat H|n\rangle = E_n|n\rangle$, we find that:

{% math() %}
E_n = \hbar \omega\left(n + \dfrac{1}{2}\right)
{% end %}

Thus, we have found the energy eigenvalues without needing to solve any differential equation, which is quite an enormous feat! Additionally, since the energies are only dependent on $n$, the energies are **non-degenerate**, meaning that each energy eigenvalue is associated with a *distinct* eigenstate. This is incredibly important because it's uncommon to encounter fully non-degenerate systems in quantum mechanics, where each eigenstate can be labelled by a single eigenvalue (think about our previous discussion of CSCOs).

In addition, we can also calculate the eigenstates in the position (or momentum) bases, so the algebraic formalism helps us get the wavefunctions too. To do so, let us recognize that if we take the $n = 0$ state (often called the _ground state_, and notated as $|0\rangle$), we have $\hat a |0\rangle = 0$. Keep this in mind! Now, recall that we *defined* our relevant operators to take the following forms:

{% math() %}
\begin{align*}
\hat a &= \dfrac{1}{\sqrt{2}}(\hat x'+ i\hat p') \\
&= \sqrt{\dfrac{m\omega}{2\hbar}}\hat x + \frac{i}{\sqrt{2m\omega \hbar}}\hat p  \\
\hat a^\dagger &= \dfrac{1}{\sqrt{2}}(\hat x' - i\hat p') \\
&= \sqrt{\dfrac{m\omega}{2\hbar}}\hat x + \frac{i}{\sqrt{2m\omega \hbar}}\hat p
\end{align*}
{% end %}

Thus, the explicit forms of $\hat a$ and $\hat a^\dagger$ can be found in the position basis by substituting in $\hat x = x$ and $\hat p = -i\hbar \dfrac{d}{dx}$, giving us:

{% math() %}
\begin{align*}
\hat a &= \sqrt{\frac{m\omega}{2\hbar}} \left(x + \frac{\hbar}{m\omega} \dfrac{d}{dx}\right) \\
\hat a^\dagger &= \sqrt{\frac{m\omega}{2\hbar}} \left(x - \frac{\hbar}{m\omega} \dfrac{d}{dx}\right)
\end{align*}
{% end %}

Now substituting these the explicit form of $\hat a$ in the position basis, we have:

{% math() %}
\begin{gather*}
\hat a|0\rangle = 0 \\
\Rightarrow ~ \hat a\langle x|0\rangle = \hat a\psi_0(x)  = 0 \\
\Rightarrow ~ \left(x + \dfrac{\hbar}{m\omega}  \dfrac{d}{dx}\right)\psi_0(x) = 0
\end{gather*}
{% end %}

> **Note:** It is also possible to do this in the *momentum basis* but the calculations become much more hairy. See [this Physics StackExchange answer](https://physics.stackexchange.com/questions/632095/eigenstates-of-qm-harmonic-oscillator-in-momentum-space) if interested.

This gives us a differential equation to solve, albeit a much easier one that can be solved explicitly by the standard methods of solving 1st-order differential equations. The solution is a Gaussian function, and in particular:

{% math() %}
\psi_0(x) = C e^{-m\omega x^2 / (2\hbar)}
{% end %}

And applying the normalization condition, the undetermined constant $C$ can be found to be $C = \left(\frac{m\omega}{\pi \hbar}\right)^{1/4}$, and thus we have:

{% math() %}
\psi_0(x) = \left(\dfrac{m\omega}{\pi \hbar}\right)^{1/4} e^{-m\omega x^2 / (2\hbar)}
{% end %}

> **Note:** Since this is a Gaussian function, it is thus symmetric about $x = 0$, and thus we can infer that the expectation value of $\psi_0(x)$ (the quantum harmonic oscillator in its ground state) is $\langle x\rangle = 0$, which is *also* true for the classical harmonic oscillator.

We can then use the definition of the $\hat a^\dagger$ operator to find all of the wavefunctions for the higher-energy states, since:

{% math() %}
\begin{gather*}
\hat a^\dagger|n\rangle = \sqrt{n + 1}~|n+1\rangle \\
\Rightarrow ~ \hat a^\dagger\langle x|n\rangle = \sqrt{n + 1}\langle x|n+1\rangle \\
\Rightarrow ~ \hat a^\dagger \psi_n(x) = (\sqrt{n + 1} )~\psi_{n + 1}(x)
\end{gather*}
{% end %}

Thus, we have:

{% math() %}
\begin{align*}
\psi_{n + 1}(x) &= \dfrac{1}{\sqrt{n + 1}} \hat a^\dagger \psi_n(x) \\
&= \psi_{n + 1}(x)  \\ &= \ \sqrt{\frac{m\omega}{2(n+1)\hbar}} \left(x - \frac{\hbar}{m\omega} \dfrac{d}{dx}\right) \psi_n(x)
\end{align*}
{% end %}

This allows us to recursively construct all the eigenstates of the system. For instance, we have:

{% math() %}
\begin{align*}
\psi_1(x) &= \dfrac{1}{\sqrt{0 + 1}}\hat a^\dagger \psi_0(x) \\
&= \ \sqrt{\frac{m\omega}{2\hbar}} \left(x - \frac{\hbar}{m\omega} \dfrac{d}{dx}\right) \left[\left(\frac{m\omega}{\pi \hbar}\right)^{1/4} e^{-m\omega x^2 / (2\hbar)}\right] \\
&= \left(\frac{m\omega}{\pi \hbar}\right)^{1/4} \sqrt{\frac{2m\omega}{\hbar}} \, x \, e^{-\frac{m\omega}{2\hbar}x^2} \\
&= \left(\dfrac{4m^3\omega^3}{\pi \hbar^3}\right)^{1/4} x e^{-m\omega x^2 / (2\hbar)}
\end{align*}
{% end %}

In general, we have:

{% math() %}
\begin{gather*}
|n\rangle = \dfrac{(\hat a^\dagger)^n}{\sqrt{n!}}|0\rangle, \\
\psi_n(x) = \langle x|n\rangle = \sqrt{\frac{m\omega}{2\hbar n!}} \left(x - \frac{\hbar}{m\omega} \dfrac{d}{dx}\right)^n \psi_0(x)
\end{gather*}
{% end %}

In the same way, we can get $\psi_2$ from applying the $\hat a^\dagger$ operator on $\psi_1$, then get $\psi_3$ from $\psi_2$, then get $\psi_4$ from $\psi_3$, and so on and so forth. With some clever mathematics (that we won't show here), this recursive formula can be solved in closed-form to yield a *generalized* formula for the _nth_ eigenstate's wavefunction representation:

{% math() %}
\psi_n(x) = \left(\dfrac{m\omega}{\pi \hbar}\right)^{1/4} \dfrac{1}{\sqrt{2^nn!}}H_n\left(\sqrt{\dfrac{m\omega}{\hbar}}x\right)\exp \left(-\dfrac{m\omega x^2}{2\hbar}\right)
{% end %}

Here, $H_n(x)$ is a **Hermite polynomial** of order $n$, defined as:

{% math() %}
H_n(x) = (-1)^n e^{x^2} \frac{d^n}{dx^n} e^{-x^2}
{% end %}

Where the first three Hermite polynomials are given by:

{% math() %}
\begin{align*}
H_0(x) &= 1 \\ H_1(x) &= 2x \\ H_2(x) &= 4x^2 - 2
\end{align*}
{% end %}

Using these definitions, we show a plot of the ground-state wavefunction $\psi_0(x)$ and several excited states' wavefunctions below:

![Plots of the wavefunction of the quantum harmonic oscillator for its first few energy levels](https://upload.wikimedia.org/wikipedia/commons/9/9e/HarmOsziFunktionen.png)

_Source: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:HarmOsziFunktionen.png)_

We can also keep things abstract by noting that we can express any of the wavefunctions of each state $\psi_n(x)$ as $\psi_n(x) = \langle x|n\rangle$, where:

{% math() %}
|n\rangle = \dfrac{(\hat a^\dagger)^n}{\sqrt{n!}}|0\rangle, \quad \psi_0(x) = \langle x|0\rangle
{% end %}

The ladder operator approach to the quantum harmonic oscillator is a powerful technique, one that carries over to relativistic quantum mechanics and allows us to skip solving the Schrödinger equation entirely. In addition, solving problems using operators alone will give us the tools to understand the **Heisenberg picture** of quantum mechanics that we'll soon see.

> **Note for the advanced reader:** The algebraic approach works mathematically because the eigenvalues of $\hat H$ are positive, and that the $\hat p^2$ operator is semi-positive definite. Additionally, the eigenspectrum (energy spectrum) of the system is discrete and **non-degenerate** (that is, all eigenstates have unique eigenvalues).

### Expectation values of the quantum harmonic oscillator

In any quantum system, it is very useful to find their expectation values, and the same is true for the quantum harmonic oscillator. In particular, we are interested in calculating $\langle x\rangle$ and $\langle p\rangle$, the expectation values of the position and momentum. To do so, we will follow [an approach from Brilliant wiki's authors](https://brilliant.org/wiki/quantum-harmonic-oscillator/). We start with the fact that:

{% math() %}
\begin{align*}
\hat x' &= \frac{1}{\sqrt{2}}(\hat a^\dagger + \hat a) \\ 
\hat p' &= \dfrac{i}{\sqrt{2}}(\hat a^\dagger - \hat a) \\
\end{align*}
{% end %}

Now, we can express $\hat x'$ and $\hat p'$ in terms of $\hat x$ and $\hat p$ by simply rearranging the definitions of $\hat x'$ and $\hat p'$ from earlier:

{% math() %}
\begin{align*}
\hat x' &= \sqrt{\dfrac{m\omega}{\hbar}} \hat x \\
\hat p' &= \dfrac{1}{\sqrt{m\hbar \omega}} \hat p \\
\end{align*}
\quad \Rightarrow \quad
\begin{align*}
\hat x &= \sqrt{\dfrac{\hbar}{m\omega}}\hat x' \\
\hat p &= \sqrt{m\hbar \omega}\, \hat p'
\end{align*}
{% end %}

Thus we have:

{% math() %}
\begin{align*}
\hat x &= \sqrt{\frac{\hbar}{2 m \omega}} (a^{\dagger} + a)\\
\hat p &= i \sqrt{\dfrac{m \hbar \omega}{2}} (\hat{a}^{\dagger} - a)
\end{align*}
{% end %}

From here, we can easily calculate the expectation values of $x$ and $p$. We'll start with the expectation value of $x$:

{% math() %}
\begin{align*}
\langle x \rangle &= \langle n|\hat x|n\rangle \\
&= \langle n| \sqrt{\frac{\hbar}{2 m \omega}} (\hat a^{\dagger} + \hat a)|n\rangle \\
&= \sqrt{\frac{\hbar}{2 m \omega}} \big[\langle n|\hat a^\dagger|n\rangle + \langle n|\hat a |n\rangle\big] \\ 
&= \sqrt{\frac{\hbar}{2 m \omega}} \big[\sqrt{n + 1} \langle n|n+1\rangle + \sqrt{n}\langle n|n-1\rangle] \\
& = 0
\end{align*}
{% end %}

Where we used our definitions $\hat a^\dagger = \sqrt{n + 1} |n+1\rangle$, $\hat a = \sqrt{n} |n-1\rangle$ and also utilized the fact that any two eigenstates are orthogonal, that is, $\langle n|m\rangle = \delta_{mn}$, so $\langle n|n+1\rangle$ and $\langle n|n-1\rangle$ are both automatically zero. We can do the same thing with the momentum operator:

{% math() %}
\begin{align*}
\langle p \rangle &= \langle n|\hat p|n\rangle \\
&= \langle n| i \sqrt{\dfrac{m \hbar \omega}{2}} (\hat a^{\dagger} - \hat a)|n\rangle \\
&= i \sqrt{\dfrac{m \hbar \omega}{2}} \big[\langle n|\hat a^\dagger|n\rangle - \langle n|\hat a |n\rangle\big] \\ 
&= i \sqrt{\dfrac{m \hbar \omega}{2}} \big[\sqrt{n + 1} \langle n|n+1\rangle - \sqrt{n}\langle n|n-1\rangle] \\
& = 0
\end{align*}
{% end %}

> **Note:** The result that $\langle x\rangle = \langle p\rangle = 0$ only holds true for *single eigenstates*. It does *not* necessarily hold true in a *superposition* of states.

The same methods of calculation can be used to establish that:

{% math() %}
\begin{align*}
\langle \hat x^2\rangle &= \dfrac{\hbar}{2m\omega}(2n + 1) \\
\langle \hat p^2 \rangle &= \dfrac{\hbar m\omega}{2}(2n + 1)
\end{align*}
{% end %}

From the formula for the uncertainty of an observable $\Delta A = \sqrt{\langle A^2\rangle - \langle A\rangle^2}$ this tells us that:

{% math() %}
\Delta x \Delta p = \dfrac{\hbar}{2}(2n + 1)
{% end %}

Where for the ground state ($n = 0$) we have the **minimum uncertainty**:

{% math() %}
\Delta x \Delta p = \dfrac{\hbar}{2}
{% end %}

### The quantum harmonic oscillator in higher dimensions

It is also possible to solve the quantum harmonic oscillator in higher dimensions. Indeed, consider the quantum harmonic oscillator along a 2D plane or a 3D box, where we can use Cartesian coordinates. Here, we do not actually need to do much more solving at all. The only difference is that rather than a single integer $n$, we need one integer $n$ for each coordinate. That is to say, for 2D we need two integers $n_x, n_y$, and for 3D we need three integers $n_x, n_y, n_z$ to describe all the eigenstates of the system. Therefore, the respective energy eigenvalues are:

{% math() %}
\begin{align*}
E_{n_x, n_y}^{(2D)} &= \hbar \omega \left(n_x + n_y + \dfrac{1}{2}\right) \\
E_{n_x, n_y, n_z}^{(3D)} &= \hbar \omega \left(n_x + n_y + n_z + \dfrac{1}{2}\right)
\end{align*}
{% end %}

Note that this means that we have **degenerate** eigenenergies, losing one of the key distinguishing features of the 1D quantum harmonic oscillator. In addition, the excited-state wavefunctions are unfortunately much more complicated for the 2D and 3D cases; we will restrict our attention to just the ground-state wavefunction. In $K$ dimensions, the ground-state wavefunction is given by:

{% math() %}
\psi_0(\mathbf{r}) = \left(\dfrac{m\omega}{\pi \hbar}\right)^{K/4} \exp\left(-\dfrac{m\omega}{2\hbar}r^2\right), \quad r = |\mathbf{r}|
{% end %}

Note that in 2D and 3D, we also have different cases, such as the quantum harmonic oscillator across a disk or in a spherical region. In these cases, the ground-state wavefunction exhibits polar and spherical symmetry respectively, so the general solutions are quite different from the 1D case. This is very important in nuclear and molecular physics, although we will not discuss it further here.

> **Note for the interested reader:** If you are interested in further applications of the quantum harmonic oscillator, it can be used to model diatomic molecules like $\ce{N2}$ or $\ce{O2}$ and describe atomic nuclei with the [nuclear shell model](https://en.wikipedia.org/wiki/Nuclear_shell_model), as well as serving an important role in *second quantization* of light - something we'll see more of later.

## Time evolution in quantum systems

In all areas of physics, we're often interested in how systems _evolve_. A system that depends on time is usually called a **dynamical system**, and at different points in time, the state of the system changes. Now, if we know that at some initial time $t_0$ a system is in a particular state $A$, and at some arbitrary later time $t$ is in another state $B$, the _time evolution_ of the system describes how the system "gets" from $A$ to $B$.

Consider a very simple example: a particle moving along a line. Its state is described by a single variable - position - which we describe with $x$. In physics, we would describe the motion of this particle with a function $x(t)$, which is a **trajectory**. This trajectory is the time evolution of the system, because from a certain initial time $t_0$, we can calculate the particle's position at any future time $t$ with $x(t)$.

In quantum mechanics, we also see quantum systems exhibit time evolution. For instance, the state-vector may have an initial state $|\psi(t_0)\rangle$ at time $t = t_0$, and at some future time $t$ have the final state $|\psi(t)\rangle$. The question is, how does that initial state become the final state? The answer to that question is the **time-evolution operator** $\hat U(t, t_0)$, which satisfies:

{% math() %}
|\psi(t)\rangle = \hat U(t, t_0)|\psi(t_0)\rangle
{% end %}

That is to say, the time-evolution operator maps the system's state at an initial time $t_0$ to its future state at time $t$. But how does this all work? This is what we'll explore in this section.

### Unitary operators

Before we go more in-depth into the time-evolution operator, we need to introduce the idea of a **unitary operator**. An arbitrary unitary operator $\hat U$ (forget about the time-evolution operator for now) satisfies two *essential* properties:

1. $\hat U^{-1} = U^\dagger$, that is, its inverse is equal to its adjoint.
2. $\hat U \hat U^{-1} = \hat U^{-1} \hat U = 1$, that is, multiplying a unitary operator by its adjoint gives the identity matrix. Together with the first rule, this automatically means that $\hat U \hat U^\dagger = \hat U^\dagger \hat U = 1$.

> **Note on notation:** We will frequently use the shorthand $\hat I = 1$, where $\hat I$ is the identity matrix, when discussing operators, but remember that matrix multiplication always gives another matrix (and not the scalar number 1), so this is just a shorthand!

Note that unitary operator is *not necessarily Hermitian* - in fact, it usually isn't! So why do we care about a non-Hermitian operator when most of the operators we use in quantum mechanics are Hermitian? Well, if we act a unitary operator $\hat U$ on a (normalized) state-vector, we find that:

{% math() %}
(\hat U |\psi\rangle)^\dagger(\hat U |\psi\rangle) = \langle \psi |\hat U^\dagger \hat U|\psi\rangle = \langle \psi|\psi\rangle = 1
{% end %}

This is the most important property of a unitary operator - it preserves the **normalization** of the state-vector! That is to say, acting $\hat U$ on $|\psi\rangle$ does _not_ change its normalization $\langle \psi|\psi\rangle = 1$.

### The unitary time-evolution operator

Now let's return back to the time-evolution operator. It is no accident that we denoted the time-evolution operator as $\hat U(t, t_0)$ and a unitary operator as $\hat U$. This is because the time-evolution operator **_is_ a unitary operator**. It is indeed common to call the time-evolution operator the _unitary time-evolution operator_ for this very reason! So from this point on, anytime you see $\hat U$, that means the time-evolution operator (unless otherwise stated).

Here is where the unitary nature of the time-evolution operator truly makes sense. This is because by knowing $\hat U \hat U^\dagger = \hat U^\dagger \hat U = 1$, and that $|\psi(t)\rangle = \hat U|\psi\rangle$, we also know that:

{% math() %}
\langle \psi(t)|\psi(t)\rangle = \langle \psi(t_0)|\hat U^\dagger\hat U(t, 0)|\psi(t_0)\rangle = \langle \psi(t_0)|\psi(t_0)\rangle = 1
{% end %}

That is, if a state-vector $|\psi\rangle$ is normalized at $t = t_0$, it will *continue* to be normalized for all future times $t$, satisfying the **normalization condition**. This means that the time-evolution operator $\hat U$ automatically guarantees **conservation of probability** in a dynamical quantum system (a system that changes with time). Furthermore, we also add the requirement that the time-evolution operator must satisfy:

{% math() %}
\hat U(t_0, t_0) = 1
{% end %}

This means that:

{% math() %}
\hat U(t_0, t_0)|\psi(t_0)\rangle = |\psi(t_0)\rangle
{% end %}

Therefore operating $\hat U$ on the state-vector returns the system in its initial state at $t = t_0$. This makes sense because at the initial time $t_0$, the system hasn't had any time to evolve, so acting the time-evolution operator on it does nothing but tell you the initial state!

> **Note:** Another name for the unitary time-evolution operator is the **propagator**, which is common in advanced quantum mechanics. Later on in this guide, when we cover the **path integral formulation** of quantum mechanics, we'll speak of $\hat U$ as the propagator. Remember that whether we call $\hat U$ the unitary time-evolution operator or the propagator, we are referring to the same thing!

Now, we've spoken a lot about what the time-evolution operator $\hat U$ _does_, but how do we express it in explicit form? To be able to start, let's write out the Schrödinger equation in a special form. The most general form of the Schrödinger equation - at least, in the form we've generally seen - is given by:

{% math() %}
i\hbar \dfrac{\partial}{\partial t}|\psi(t)\rangle = \hat H|\psi(t)\rangle
{% end %}

But since $|\psi(t)\rangle = \hat U|\psi\rangle$, this can *also* be written as:

{% math() %}
i\hbar \dfrac{\partial}{\partial t}\hat U|\psi(t_0)\rangle = \hat H(\hat U|\psi(t_0)\rangle)
{% end %}

Since $|\psi(t_0)\rangle$ does not depend on time, we can factor it out from both sides, giving us:

{% math() %}
i\hbar \dfrac{\partial}{\partial t} \hat U = \hat H \hat U
{% end %}

Which can be written more explicitly as:

{% math() %}
i\hbar \dfrac{\partial}{\partial t} \hat U(t, t_0) = \hat H \hat U(t, t_0)
{% end %}

This is the **essential equation of motion** for the unitary operator. We'll now do something that may defy intuition but is actually mathematically sound. First, we'll temporarily drop the operator hats and not write out the explicit dependence on $t$ and $t_0$, giving us:

{% math() %}
i\hbar \dfrac{\partial U}{\partial t} = HU
{% end %}

Now, dividing by $i\hbar$ from both sides gives us:

{% math() %}
\dfrac{\partial U}{\partial t} = \frac{1}{i\hbar}HU = -\frac{i}{\hbar} HU
{% end %}

(Here we use the fact that $1/i = -i$, and $\dot U = \frac{\partial U}{\partial t}$). This now looks like a differential equation in the form $\dot U = -\frac{i}{\hbar} H U$! Solving this differential equation (using separation of variables) along with our known property $U(t_0) = 1$ gives us:

{% math() %}
U = e^{-i H (t - t_0)/\hbar}
{% end %}

Now, we can restore the operator hats and we can write the most general form of the time evolution operator:

{% math() %}
\hat U(t, t_0) = \exp\left(-\dfrac{i}{\hbar} \hat H (t - t_0)\right)
{% end %}

If we adopt the convention of choosing $t_0 = 0$, this gives us:

{% math() %}
\hat U(t) = \exp\left(-\dfrac{i}{\hbar} \hat H t\right), \quad \hat U(t) \equiv \hat U(t, 0)
{% end %}

Perhaps you might be inclined to answer with "You're wrong! What in the world is the exponential function of a matrix??" The way of making sense of this is to recognize that the exponential function can be defined in terms of a **power series**:

{% math() %}
e^X = \exp(X) = \sum_{n = 0}^\infty \dfrac{X^n}{n!}
{% end %}

Taking powers of a matrix is a perfectly acceptable operation, and therefore a term like $\hat H^n$ would raise no alarms, since $\hat H^n = \underbrace{\hat H \hat H \dots \hat H}_{n \text{ times}}$. This allows us to write $\hat U(t)$ in the form:

{% math() %}
\begin{align*}
\hat U &= \sum_{n = 0}^\infty \frac{1}{n!}\left(-\dfrac{i}{\hbar} \hat H t\right) \\
&= 1 -\frac{i}{\hbar} \hat H t - \frac{1}{2\hbar^2} \hat H^2 t^2 + \dots
\end{align*}
{% end %}

Usually, applying this definition is quite cumbersome (summing infinite terms is hard!) but if we truncate the series to just a few terms, we can often find a good approximation to the full series. For instance, if we truncate the series to first-order, we have:

{% math() %}
\hat U \approx 1 -\frac{i}{\hbar} \hat H t
{% end %}

Using this approximation can allow us to calculate the future state of a time-dependent quantum system with only knowledge of the Hamiltonian and the initial state. Of course, since we truncated the series, this calculation can yield only an approximate answer, but in some cases an approximate answer is enough. Thus, the time-evolution operator is the starting-point for **perturbative calculations** in quantum mechanics, where we can make successively more accurate approximations to the future state of a quantum system by invoking the time-evolution operator in series form, and taking only the first few terms.

### The Heisenberg picture

Introducing the time-evolution operator has an interesting consequence: it allows us to calculate the future state of any quantum system from a known initial state "frozen" in time. This is because the initial state of a quantum system has not had time to evolve yet, so it is *independent* of time. In fact, it is possible to dispense with time-dependence in calculations almost completely, because it turns out that there is *also* a way to calculate the measurable quantities of quantum systems at any future point in time without needing to explicitly calculate $|\psi(t)\rangle$. This approach is known as the **Heisenberg picture** in quantum mechanics.

Consider the position operator $\hat X$ (we will use an uppercase $X$ here for clarity). Normally, this is a time-independent operator, since we know it is defined by $\hat X|\psi_0\rangle = x|\psi_0\rangle$, where $|\psi_0\rangle$ is a stationary state and $x$ is a position eigenvalue: notice here that time does not appear *at all* as a variable. Taking the inner product of both sides with the bra $\langle \psi_0|$ gives us the *expectation value* of the position:

{% math() %}
\langle \psi_0|\hat X |\psi_0\rangle = \langle \psi_0| x|\psi_0\rangle
{% end %}

Now, we want to find a _time-dependent_ version of the position operator, which we'll call $\hat x_H(t)$, which also satisfies an eigenvalue equation:

{% math() %}
\hat X_H(t)|\psi(t)\rangle = x(t)|\psi(t)\rangle
{% end %}

Notice how our position eigenvalue is now time-dependent, because as the state of the system changes, the positions $x(t)$ also change. Our challenge will be able to write $\hat X_H(t)$ in terms of $\hat X$. How can we do so? Well, recall that $|\psi(t)\rangle = \hat U|\psi(t_0)\rangle$, and $|\psi(t_0)\rangle$ is the same thing as $|\psi_0\rangle$. Thus we can write:

{% math() %}
\hat X_H(t)|\psi(t)\rangle = \hat X\hat U|\psi_0\rangle
{% end %}

Now, let us take its inner product with the bra $\langle \psi(t)|$, which gives us:

{% math() %}
\langle \psi(t)|\hat X_H(t)|\psi(t)\rangle = \langle \psi(t) |x\hat U|\psi_0\rangle
{% end %}

We'll now use the identity that:

{% math() %}
|\psi(t)\rangle = \hat U |\psi_0\rangle \quad \Leftrightarrow \quad |\psi_0\rangle  = \hat U^\dagger |\psi(t)\rangle
{% end %}

You can prove this rigorously, but it can be intuitively understood by recognizing that $\hat U^\dagger = \hat U^{-1}$, meaning that just as $\hat U$ evolves the system _forwards_ in time, $\hat U^\dagger$ evolves the system _backwards_ in time (the "inverse" direction in time). Hence acting $\hat U^\dagger$ on a system at some time $t$ returns it to its original state at some past time $t_0$. With the same result, we note that:

{% math() %}
\langle \psi(t)|\hat X_H(t)|\psi(t)\rangle = \langle \psi(t) |x\hat U|\psi_0\rangle = \langle \psi_0|\hat U^\dagger x \hat U|\psi_0\rangle
{% end %}

Thus by pattern-matching we have:

{% math() %}
\hat X_H(t) = \hat U^\dagger x \hat U = \hat U^\dagger \hat X \hat U
{% end %}

Notice that the latter result holds for all time $t$! We have indeed arrived at our expression for the time-dependent version of the position operator $\hat X_H(t)$:

{% math() %}
\hat X_H(t) = \hat U^\dagger \hat X \hat U
{% end %}

It is also common to say that $\hat X_H$ is the position operator in the **Heisenberg picture**. Unlike the **Schrödinger picture** that we've gotten familiar working with, the Heisenberg picture uses *time-dependent operators* that operate on a constant state-vector $|\psi\rangle = |\psi_{0}\rangle$. It is _completely equivalent_ to the Schrödinger picture, but it is sometimes more useful, since we can dispense with calculating the state-vector's time evolution as long as we know the $\hat U$ operator, which can simplify (some) calculations. In the most general case, for any operator $\hat A$, its equivalent time-dependent version $\hat A_H$ in the Heisenberg picture is given by:

{% math() %}
\hat A_H(t) = \hat U^\dagger \hat A \hat U
{% end %}

If we don't know $\hat U$, it is also possible to calculate $\hat A_H$ via the **Heisenberg equation of motion**, the analogue of the Schrödinger equation in the Heisenberg picture:

{% math() %}
\dfrac{d}{dt} \hat{A}_{H}(t) = \frac{i}{\hbar}[\hat{H}, \hat{A}_{H}(t)]
{% end %}

A particularly powerful consequence of the Heisenberg picture is how easily it maps classical systems into a corresponding quantum system. For instance, the classical harmonic oscillator follows the equation of motion $\dfrac{d^2 x}{dt^2} + \omega^2 x = 0$, which has the (classical) solution:

{% math() %}
\begin{align*}
x(t) &= a e^{-i\omega t} + a^* e^{i\omega t} \\
p(t) &= m \dfrac{dx}{dt} = b^*e^{-i\omega t} + be^{i\omega t}, \quad b =i\omega ma^*
\end{align*}
{% end %}

Where {% inlmath() %}a, a^*{% end %} here are some amplitude constants that can be specified by the initial conditions, and for generality, we assume that they can be complex-valued. Now, the Heisenberg picture tells us that if we want to find the corresponding quantum operators $\hat X_H(t), \hat p(t)$, all we have to do is to change our *constants* {% inlmath() %}a, a^*{% end %} to *operators* {% inlmath() %}\hat a, \hat a^\dagger{% end %} (same with {% inlmath() %}b, b^*{% end %}), giving us:

{% math() %}
\begin{align*}
\hat X_H(t) &= \hat ae^{-i\omega t} + \hat a^\dagger e^{i\omega t} \\
\hat p(t) &= \hat be^{-i\omega t} + \hat b^\dagger e^{i\omega t}, \quad \hat b = i\omega m a^\dagger
\end{align*}
{% end %}

Indeed, we can then identify $\hat a, \hat a^\dagger$ as just the **ladder operators** we're already familiar with from studying the quantum harmonic oscillator! In addition, we can also show that $\hat x$ satisfies a *nearly identical* equation of motion as the classical case ($\frac{d^2 x}{dt^2} + \omega^2 x = 0$), with the exception that the position *function* $x$ is replaced by the *operator* $\hat X_{H}$:

{% math() %}
\dfrac{d^2 \hat X_H(t)}{dt^2} + \omega^2 \hat X_H(t) = 0
{% end %}

Notice the elegance correspondence between the classical and quantum pictures. By doing very little work, we have *quantized* a classical system, taking a classical variable ($x(t)$, representing a particle's position) and turning it ("promoting it") into a quantum operator $\hat X_{H}(t)$, a process formally called **first quantization**. This method will be essential once we discuss **second quantization**, where we take *classical* field theories and use them to construct *quantum* field theories. But we've not gotten to there yet! We'll save a more in-depth discussion of second quantization for later.

> **Note for the advanced reader:** In second quantization, we essentially do the same thing as first quantization, but rather than quantizing the position (by taking the classical variable $x(t)$ and promoting it to an operator $\hat X_{H}$) we are interested in taking a classical field $\phi(x, t)$ and promoting it to an quantum field operator $\hat \phi$. Just as in first quantization, second-quantized fields follow the same equations of motion as their classical field analogues. In particular, the simplest type of quantum field (known as the _free scalar field_) obeys the equation $\partial^2_{t}\hat \phi - \nabla^2 \phi + m^2\phi = 0$, which is very similar to the harmonic oscillator equation of motion.

### The correspondence principle and the classical limit

As we have seen, the Heisenberg picture makes it easy to show the intricate connection between quantum mechanics and classical mechanics, which is also known as the **correspondence principle**. The correspondence principle is essential because it explains why we live in a world that can be so well-described by classical mechanics, even though we know that everything in the Universe is fundamentally quantum at the tiniest scales. A key part of the correspondence principle is **Ehrenfest's theorem**, which is straightforward to prove from the Heisenberg picture. We start by writing down the Heisenberg equation of motion (which we introduced earlier), given by:

{% math() %}
\dfrac{d}{dt} \hat{A}_{H}(t) = \frac{i}{\hbar}[\hat{H}, \hat{A}_{H}(t)]
{% end %}

The Heisenberg equations of motion for the position and momentum operators $\hat X_{H}(t)$, $\hat P_{H}(t)$ are therefore:

{% math() %}
\begin{align*}
\dfrac{d \hat X_H(t)}{dt} = \frac{i}{\hbar}[\hat{H}, \hat X_H(t)] \\
\dfrac{d \hat P_H(t)}{dt} = \frac{i}{\hbar}[\hat{H}, \hat P_H(t)]
\end{align*}
{% end %}

If we take the expectation values for each equation on both sides, we have:

{% math() %}
\begin{align*}
\left\langle\dfrac{d \hat X_H(t)}{dt}\right\rangle = \frac{i}{\hbar}\langle[\hat{H}, \hat X_H(t)]\rangle   \\
\left\langle\dfrac{d \hat P_H(t)}{dt}\right\rangle = \frac{i}{\hbar}\langle[\hat{H}, \hat P_H(t)]\rangle
\end{align*}
{% end %}

Now making use of the fact that {% inlmath() %}[\hat H, \hat X_{H}(t)] = -i\hbar \frac{\hat{P}_{H}}{m}{% end %} and $[\hat H, \hat P_{H}(t)] = i\hbar \nabla V$ (we won't prove this, but you can show this yourself by calculating the commutators with $\hat H = \hat P^2/2m + V$) we have:

{% math() %}
\begin{align*}
\left\langle\dfrac{d \hat X_H(t)}{dt}\right\rangle = \frac{\langle \hat{P}_{H}\rangle}{m}   \\
\left\langle\dfrac{d \hat P_H(t)}{dt}\right\rangle = \langle -\nabla V\rangle
\end{align*}
{% end %}

The first equation tells us that the *expectation value of the position* is equal to the *expectation value of the momentum*, divided by the mass. In the classical limit, this is *exactly* $\dot x = p/m$, which comes directly from the classical definition of the momentum $p = mv = m\dot x$! Meanwhile, the second equation tells us that the *expectation value of the momentum* is equal to $\langle -\nabla V\rangle$. This is (approximately) the same as Newton's second law $F = \frac{dp}{dt} = -\nabla V$. Thus, Ehrenfest's theorem says that at classical scales, quantum mechanics reduces to classical mechanics; this is why we don't observe any quantum phenomena in our everyday lives!

### The interaction picture

Using Heisenberg's approach to quantum mechanics is powerful, but it often comes at the cost of needing to compute a *lot* of operators. The physicist Paul Dirac looked at the Heisenberg picture, and decided that there was a *better way* that would simplify the calculations substantially, while preserving all of the physics of a quantum system. His equivalent approach is known as the **interaction picture**, although it is often also called the **Dirac picture** (obviously after him).

We will quickly go over the interaction picture for the sake of brevity. Essentially, it says that we can split a quantum system into two parts - a non-interacting part and an interacting part. When we say "non-interacting", we mean a hypothetical system that is completely isolated from the outside world and is essentially in a Universe of its own. To do this, we write the Hamiltonian of the system as the sum of a non-interacting Hamiltonian $\hat H_0$ and an interaction Hamiltonian $\hat W$:

{% math() %}
\hat{H} = \hat{H}_{0} + \hat{W}
{% end %}

As with the Schrödinger picture, the state-vector of the system $|\psi(t)\rangle$ will depend on time. But here is where the interaction picture begins to differ from the Schrödinger picture. First, let us consider the time-evolution operator $\hat U_0(t, t_{0}) = e^{-i\hat H_0 (t-t_{0})/\hbar}$. Strictly-speaking, this time-evolution operator is only valid for the non-interacting part of the system, since it comes from $\hat H_0$, the non-interacting Hamiltonian. We will now define a *modified* state-vector $|\psi_I(t)\rangle$, which is related to the original state-vector of the system $|\psi(t)\rangle$ by:

{% math() %}
|\psi_{I}(t)\rangle = \hat U_{0}^{\dagger} |\psi(t)\rangle = e^{i \hat{H}_{0} (t - t_{0})/\hbar} |\psi(t)\rangle
{% end %}

We can of course also invert this relation to write $|\psi(t)\rangle$ in terms of $|\psi_I\rangle$, as follows:

{% math() %}
|\psi(t)\rangle = \hat U_{0} |\psi_{I}(t)\rangle = e^{-i \hat{H}_{0} (t - t_{0})/\hbar} |\psi_{I}(t)\rangle
{% end %}

We can write an arbitrary operator $\hat A$ in its **interaction picture representation**, which we will denote with $\hat A_I$, via:

{% math() %}
\hat{A}_{I}(t) = \hat U_{0}^{\dagger} \hat{A} \hat U_{0} = e^{i \hat{H}_{0} (t - t_{0})/\hbar} \hat{A} e^{-i \hat{H}_{0} (t - t_{0})/\hbar}
{% end %}

In addition, an operator's representation in the interaction picture follows the equation of motion:

{% math() %}
i\hbar\frac{d \hat{A}_{I}}{dt} = [\hat{A}_{I}, \hat{H}_{0}]
{% end %}

Our modified state-vector $|\psi_I(t)\rangle$ then satisfies the following equation of motion:

{% math() %}
i\hbar \frac{d}{dt}|\psi_{I}(t)\rangle = \hat{W}_{I}|\psi_{I}(t)\rangle
{% end %}

Where $\hat W_I = \hat U_{0}^{\dagger} \hat{W} \hat U_{0}$ is the interaction picture representation of the interaction Hamiltonian $\hat W$. What this means is that using the interaction picture, we can *isolate* the interacting parts of the system from the non-interacting parts of the system - something that *isn't possible* to do in the Heisenberg or Schrödinger pictures! The interacting part of the system follow the equation of motion we already presented for $|\psi_I(t)\rangle$, whereas the non-interacting part satisfies the equation of motion for $\hat U_0$:

{% math() %}
i\hbar \dfrac{\partial}{\partial t} \hat U_{0}(t, t_0) = \hat H_{0} \hat U_{0}(t, t_0)
{% end %}

Since these two equations of motion are completely decoupled from each other, we can solve for the interacting and non-interacting parts separately. Once we have successfully solved for $|\psi_I(t)\rangle$ and $\hat U_0$, the state-vector of the full system is just a unitary transformation away, since:

{% math() %}
|\psi(t)\rangle = \hat U_{0} |\psi_{I}(t)\rangle
{% end %}

The interaction picture is powerful because it allows us to describe a quantum system that undergoes very complicated interactions *as if* those interactions were not present, and simply "layer" the interactions on top. This is an idea essential to solving very complicated quantum systems, especially once we get to the topic of **time-dependent perturbation theory** in quantum mechanics. As an added bonus, it turns out that under certain circumstances it is possible to write out an *exact series solution* to solve for the interacting part of a system. As long as we assume that interactions are reasonably "small", we can convert the equation of motion for the interacting part of the system into an integral equation:

{% math() %}
\begin{gather*}
i\hbar \frac{d}{dt}|\psi_{I}(t)\rangle = \hat{W}_{I}|\psi_{I}(t)\rangle \\
\downarrow \\
|\psi_{I}(t) = |\psi_{I}(t_{0})\rangle + \frac{1}{i\hbar} \int_{t_{0}}^t dt' W_{I}(t')|\psi_{I}(t')\rangle
\end{gather*}
{% end %}

One can then write out a series solution that solves the integral equation, which is given by:

{% math() %}
\begin{align*}
|\psi_{I}(t) = \bigg\{1 &+ \frac{1}{i\hbar} \int dt_{1} W_{I}(t_{1}) + \frac{1}{(i\hbar)^2}\int dt_{1} dt_{2}  W_{I}(t_{1})W_{I}(t_{2}) \\ 
&+ \dots + \frac{1}{(i\hbar)^n} \int dt_{1}dt_{2} \dots dt_{n} W_{I}(t_{1})W_{I}(t_{2}) \dots W_{I}(t_{n})\bigg\}|\psi_{I}(t_{0})\rangle
\end{align*}
{% end %}

This is the [Dyson series](https://en.wikipedia.org/wiki/Dyson_series). Right now, the Dyson series is unimportant to us, but it has a great deal of importance in analyzing **scattering**. We have already seen scattering-state solutions to the Schrödinger equation, like the case of the rectangular potential barrier. But quantum-mechanical scattering is far more broad, and the Dyson series provides us with a way to calculate very complex scattering interactions in a solvable way. In fact, this technique is so general that it is even used in quantum field theory!

### Summary of time evolution

We have seen that there are **three equivalent approaches** to understanding the time evolution of the quantum system: the Schrödinger picture, Heisenberg picture, and interaction (or Dirac) picture. In the Schrödinger picture, operators are time-independent but states are time-dependent; in the Heisenberg picture, operators are time-dependent but states are time-independent; and finally, in the interaction picture, both are time-dependent. Each of these approaches has their own strengths and weaknesses, and they are useful in different scenarios. The key idea is that *having* these different approaches to describing quantum systems gives us powerful tools to solve these systems, even if we don't have to use them all the time.

## Angular momentum

In quantum mechanics, we are often interested in **central potentials**, that is, potentials in the form $V = V(r)$. For instance, the hydrogen atom can be modelled by a **Coulomb potential** $V(r) \propto 1/r$, and a basic model of the atomic nucleus uses a **harmonic potential** $V(r) \propto r^2$.

> **Note:** In case it was unclear, in central potential problems, $r = \sqrt{x^2 + y^2 + z^2}$ is the radial coordinate.

Due to the symmetry of such problems, it is often convenient to use a radially-symmetric coordinate system, like polar coordinates (in 2D) or cylindrical/spherical coordinates (in 3D). This leads to an interesting result - the **conservation of angular momentum**. A rigorous explanation of why this is the case requires [Noether's theorem](https://en.wikipedia.org/wiki/Noether's_theorem), which is explained in more detail in the [classical mechanics guide](@/advanced-classical-mech/part-2.md). There are a few differences, however. For instance, while classical central potentials lead to **orbits** around the center-of-mass of a system, the idea of orbits is somewhat vague in quantum mechanics since the idea of probability waves "orbiting" doesn't really make sense. However, for ease of visualization (and also due to some [historical reasons](https://en.wikipedia.org/wiki/Bohr_model)), it is still common to say that central potential problems in quantum mechanics have "orbits", and thus we conventionally call this associated type of angular momentum the **orbital angular momentum**, denoted $\mathbf{L}$.

In addition, a classical spinning object also has angular momentum, and likewise a quantum particle also does - again, this is why we say that electrons (and other spin-1/2 particles) have **spin**, since they do have angular momentum in the form of _spin angular momentum_. Since we know the relationship between the magnetic moment $\boldsymbol{\mu}$ and the spin angular momentum $\mathbf{S}$ (it is proportional to a factor of $\gamma$, the gyromagnetic ratio), we can rearrange to find $\mathbf{S}$:

{% math() %}
\boldsymbol{\mu} = \gamma \mathbf{S} \quad \Rightarrow \quad \mathbf{S} = \frac{\boldsymbol{\mu}}{\gamma}
{% end %}

It is important to recognize that spin angular momentum $\mathbf{S}$ is different from the orbital angular momentum $\mathbf{L}$. They, however, share one important similarity - they are both **conserved quantities**. This means they obey some similar behaviors. Additionally, the study of orbital angular momentum is extremely important for understanding some of the most important problems in quantum mechanics, so we will explore it in detail.

## The hydrogen atom

Hydrogen is the most abundant element in the Universe. In stellar nebulas, it provides the raw material for stars to form. Within stars, the fusion of hydrogen atoms into helium generates immense heat and light, the same energy that ultimately powers all life on Earth. By reacting with oxygen, it forms liquid water, giving us our rivers, lakes, and oceans. In organic compounds, it bonds with oxygen, nitrogen, and carbon to form our proteins, amino acids, and DNA. It is not an exaggeration to say that without hydrogen, humanity could not exist.

Additionally, the hydrogen atom is a classical example of a quantum-mechanical system, well-known because it is one of the few quantum systems with an *exact* analytical solution yet still complex enough to describe a real-world system. In addition, it has great historical importance as one of the first systems successfully described by Schrödinger's wave mechanics, and while it in theory applies only for hydrogen (and a few other types of atoms with similar properties) it continues to form the basis of our modern understanding of atomic physics.

### The Bohr model

Before we solve the hydrogen atom using the Schrödinger equation and quantum mechanics, it is useful to briefly go over the older **Bohr model** of the hydrogen atom. The Bohr model was first derived by the physicist Niels Bohr and was the basis of the theoretical understanding of the hydrogen atom in the early 20th century. Although now outdated, it offers important insights into the hydrogen atom and predicts *some* of its behavior correctly.

![An illustration of a single proton orbited by a single electron in Bohr's model of the hydrogen atom](https://study.com/cimages/multimages/16/hydrogen_bohr_model8259738646372964480.jpg)
_Bohr's model of the hydrogen atom, with a single proton and electron bound by electromagnetic forces. Source: [study.com](https://study.com/academy/lesson/what-is-hydrogen-formula-production-uses.html)_

The Bohr model is known as a *semiclassical model* because it is based primarily off classical mechanics, with the sole exception of one distinctly *quantum* postulate: the **quantization of angular momentum**. Historically, the quantization of angular momentum was derived to fix a major theoretical problem. Physicists initially assumed (incorrectly) that the hydrogen atom was similar to a miniature solar system, with a single negatively-charged electron orbiting a positively-charged atomic radius, held together by electromagnetic forces. However, classical electromagnetism predicts that accelerating charges emit electromagnetic radiation, which carry away energy. Since an orbiting electron would indeed be accelerating (as per Newton's second law), the electron would therefore lose energy due to electromagnetic radiation. However, while the solar system emits so little gravitational radiation that orbits remain stable for millions of years, the classical model of the hydrogen atom predicted that the electron would radiate electromagnetic energy so quickly that the electron would fall into the nucleus! (Clearly, if this was so, then we would all be dead and you would not be reading this guide right now.)

This theoretical inconsistency prompted Bohr to propose that electrons orbited at fixed **orbitals**, which are classical circular orbits with a fixed radius (the name has stuck around to this day despite the fact that we know electrons don't really orbit, at least not in the classical sense anyway). Electrons would be able to "jump" between orbitals if they absorbed (or emitted) energy. However, they could never be found *between* orbitals. Bohr's orbitals meant that electrons would be kept in stable orbits that wouldn't decay, solving the theoretical problem of the electron falling into the radius (and predicting correctly that humans are alive). Mathematically, his proposal required that angular momentum be **quantized** according to the following rule:

{% math() %}
L = n \hbar, \quad n = 1, 2, 3, \dots
{% end %}

Where $L = L_{z}$ is the orbital angular momentum of the electron and $n$ is an integer called the **principal quantum number** (remember this, it will be very important later). As we now know, Bohr's proposal was indeed correct, since we know the eigenvalues of the $\hat L_z$ operator are indeed integer multiples of $\hbar$. However, it defied the classical physics, and there was no explanation for *why* quantization of angular momentum was the case, other than the fact that it offered an (albeit unsatisfying) answer for the stability of atoms, which would not come until Schrödinger's theory of the hydrogen atom in 1926.

On the basis of the quantization of angular momentum, Bohr set to work solving the problem of the hydrogen atom. He knew that the nucleus and electron were held together by electromagnetic forces, so he used the classical **Coulomb potential**:

{% math() %}
V(r) = -\frac{Ze^2}{4\pi\varepsilon_{0}r}
{% end %}

Where $Z$ is the **nuclear charge** of the atom (equal to the atomic number; for the hydrogen atom, $Z = 1$), $e = \pu{1.60218 * 10^{-19} C}$ is the **elementary charge constant**, $\varepsilon_0 = \pu{8.85419 * 10^{-12} C^2 * s^2 * kg^{-1} \cdot m^{-3}}$ is the **permittivity of free space** (also known as the *electric constant*) and $r$ is the radial coordinate. This potential applies both classically and quantum-mechanically (it is the same potential as the one we'll use in the quantum Hamiltonian later), so Bohr was essentially correct on this count, although he did not (and could not) know it at the time.

> **Note:** Technically the Coulomb potential only applies to a nucleus that is completely stationary; we know now that the nucleus does *slightly* move, albeit much less than the electron, so the assumption of a stationary nucleus is indeed sound. Also, the Coulomb potential is no longer valid in the regime of highly-relativistic energies, where we must consider quantum-electrodynamical effects, but these are negligible for the hydrogen atom which can be described quite well without relativity.

The force corresponding to the Coulomb potential is the **Coulomb force**, and since force is the negative derivative of the potential, we have:

{% math() %}
F = -\frac{dV}{dr} = -\frac{Ze^2}{4\pi \varepsilon_{0}r^2}
{% end %}

Since the system had radial symmetry, the Coulomb force must be equal to the centripetal force, which was given by $F_c = mv^2/r$. Thus, equating the two gives us:

{% math() %}
\frac{m_{e} v^2}{r} = \left|-\frac{Ze^2}{4\pi \varepsilon_{0}r^2}\right|
{% end %}

Where $m_e = \pu{9.10938 * 10^{-31} kg}$ is the electron mass. Now, Bohr applied his quantization postulate to solve for the squared velocity $v^2$. Since angular momentum is given classically by $\mathbf{L} = \mathbf{r} \times \mathbf{p} = \mathbf{r} \times m\mathbf{v}$, the *magnitude* of the angular momentum $L = |\mathbf{L}|$ would be equal to $rmv$ (here the cross product is equal to the relative product because the velocity vector $\mathbf{v}$ is tangential to the electron's orbit while the radial position vector $\mathbf{r}$ is pointed towards the nucleus, hence they are perpendicular to each other and thus $|\mathbf{r} \times m\mathbf{v}| = \mathbf{r}m|\mathbf{v}| \sin \theta = rmv$). Combining with $L = n\hbar$ then gives us:

{% math() %}
n \hbar = rmv \implies v^2 = \left(\frac{n\hbar}{mr} \right)^2
{% end %}

Substituting this into the centripetal force (and setting $m = m_e$) gives us:

{% math() %}
\frac{m_{e}}{r} \left(\frac{n\hbar}{m_{e}r} \right)^2 = \frac{Ze^2}{4\pi \varepsilon_{0}r^2}
{% end %}

Thus, solving for $r$ gives us:

{% math() %}
r = \frac{4\pi \varepsilon_{0}}{Ze^2} \frac{n^2 \hbar^2}{m_{e}}
{% end %}

Since the orbital radius depends on integer $n$, we can make this explicitly by writing $r = r_n$, where:

{% math() %}
r_{n} = \frac{4\pi \varepsilon_{0}}{Ze^2} \frac{n^2 \hbar^2}{m_{e}}, \quad n = 1, 2, 3, \dots
{% end %}

Thus, Bohr came up with a result for the orbital radii $r_n$, which indeed matched experimental measurements. For the $n = 1$ orbital in hydrogen (called the **ground state** since it has the smallest orbital), the radius was:

{% math() %}
r_{0} = \frac{4\pi \varepsilon_{0} \hbar^2}{m_{e}e^2} \equiv a_{0}
{% end %}

This quantity, denoted $a_0$ and with a value of approximately $\pu{5.29 * 10^{-11} m}$, is called the **Bohr radius** and is often synonymous with the atomic radius of hydrogen. Written in terms of the Bohr radius, the orbital radii take the form:

{% math() %}
r_{n} = \frac{n^2 a_{0}}{Z}, \quad n = 1, 2, 3, \dots
{% end %}

Recalling that $r m v = n \hbar$, we can now solve for the speed $v$ of the electrons for the $n$-th orbital:

{% math() %}
v_{n} = \frac{n\hbar}{mr_{n}} = \frac{\hbar Z}{n a_{0}m_{e}} = \frac{Z e^2}{4\pi \varepsilon_{0} n \hbar}, \quad m_{e} = 1, 2, 3, \dots
{% end %}

One may also express this in terms of the fine structure constant $\alpha$, defined as $\alpha = \frac{e^2}{4\pi \varepsilon_0 \hbar c}$ (which has a numerical value of around $\frac{1}{137}$), as:

{% math() %}
v_{n} = \frac{Z \alpha c}{n} \approx \frac{Z}{137 n}c
{% end %}

In hydrogen's ground state, where $n = 1$, we have:

{% math() %}
v_{0} \approx \frac{c}{137} \approx 0.007 c \approx 0.01 c
{% end %}

Hence, the electron in a hydrogen atom orbits close to 1% of the speed of light. This is a fortunate fact, because we now know that in certain atoms this is not the case. For example, in gold atoms, the electrons orbit at 58% the speed of light. The Bohr atom does not account for relativity and thus cannot accurately describe these relativistic electrons. Hence, Bohr's theory would not have succeeded to the extent it did if he had been studying gold atoms instead of hydrogen atoms!

Next, Bohr solved for the total energy of the hydrogen atom. As we know, the total mechanical energy is the sum of the kinetic and potential energies. Bohr used the [virial theorem](https://en.wikipedia.org/wiki/Virial_theorem), which states that for any central force potential in the form $V(r) = ar^m$ where $m$ is some power, the average value of the kinetic energy $\langle K\rangle$ and the average potential energy $\langle V\rangle$ are related by:

{% math() %}
V(r) = a r^m \implies 2\langle K\rangle = m \langle V\rangle
{% end %}

By the conservation of energy, the total energy of a system held by a central force must therefore be in the form:

{% math() %}
E = \langle K \rangle + \langle V\rangle = \frac{2}{m}\langle K\rangle + \langle K\rangle
{% end %}

For the Coulomb potential, we have $m = -1$, and hence:

{% math() %}
E = \langle K\rangle + (-2\langle K\rangle) = -\langle K\rangle
{% end %}

Where the energy is negative because the system is in a stable *bound state* (meaning that energy must be *added to* the system to pull the electron and nucleus apart; specifically, around 13.6 electron-volts (abbreviated eV, where $\pu{1 eV} = \pu{1.60218 * 10^{-19} J}$), a number that will be important soon). Now substituting our expression for the speeds $v_n$ of the $n$-th orbital into the classical kinetic energy $K = \frac{1}{2} mv^2$, we obtain:

{% math() %}
E = -\langle K\rangle = -\frac{1}{2}mv^2 = -\frac{Z^2 m_{e} e^4}{32\pi^2 \varepsilon_{0}^2 n^2 \hbar^2} = - \frac{Z^2 m_{e} \alpha^2 c^2}{2n^2}
{% end %}

We have found that the total energy depends on $n$, hence as per our prior conventions we write the energy of the $n$-th orbital as $E_n$, where:

{% math() %}
E_{n} = -\frac{Z^2}{2n^2} m_{e}\alpha^2 c^2 \approx -Z^2\left( \frac{\pu{13.6 eV}}{n^2} \right), \quad n = 1, 2, 3, \dots
{% end %}

In the case of hydrogen, with $Z = 1$, we have:

{% math() %}
E_{n} = -\frac{\pu{13.6 eV}}{n^2}, \quad n = 1, 2, 3, \dots
{% end %}

Bohr had found something extraordinary: each of the orbitals corresponded to *distinct* energy values with fixed $n$. Thus, atomic orbitals were not just specific orbits of fixed radii; they also corresponded to **energy levels** of fixed energy! Therefore, if an atom were to *transition* between higher and lower energy levels (which happens when the electron "falls" from a higher orbital to a lower one), by the conservation of energy, the energy difference must go *somewhere*. Einstein's then-new concept of the *photon*, particles of light, provided the answer to where that missing energy went: a photon is what carries the missing energy away! An atomic transition thus causes the **emission of light**! In fact, nearly all the light we see in the Universe (among which includes light from hydrogen gas clouds in space) comes from transitions between energy levels of atoms (as well as molecules and crystals). Light, previously understood as purely an *electromagnetic* phenomenon, was now inseparable from atomic and quantum physics.

![Diagram of the Bohr model, showing orbitals of fixed radii parametrized by integer n and a photon emitted during an atomic transition](https://upload.wikimedia.org/wikipedia/commons/9/93/Bohr_atom_model.svg)

_A diagram of an atom emitting a photon of energy $\Delta E = h\nu$ in the Bohr model. Source: [Wikipedia](https://commons.wikimedia.org/wiki/File:Bohr_atom_model.svg)_


Using the energy of a single photon $E = h\nu = hc/\lambda$ predicted by Max Planck (where $\nu$ is the frequency, $\lambda$ is the wavelength, and $c$ is the speed of light), Bohr could calculate the wavelength of light emitted by an atom. Specifically, by equating Planck's formula and his calculated energy levels, we have:

{% math() %}
\frac{hc}{\lambda} = E_{f} - E_{i} = -(\pu{13.6 eV}) Z^2\left( \frac{1}{n_{f}^2} - \frac{1}{n_{i}^2} \right), \quad n_{f} < n_{i}
{% end %}

Where $E_f, E_i$ are the energies of the final and initial energy levels, $n_f$ is the final energy level's principal quantum number, and $n_i$ is the initial energy level's principal quantum number. Some straightforward rearrangement yields the famous **Rydberg formula**:

{% math() %}
\frac{1}{\lambda} = -\frac{(\pu{13.6 eV})Z^2}{hc} \left( \frac{1}{n_{f}^2} - \frac{1}{n_{i}^2} \right), \quad n_{f} < n_{i}
{% end %}

Bohr predicted that each of these wavelengths would show up as distinct lines in the hydrogen spectrum, rather than the continuous spectrum, as would be predicted by classical mechanics. Indeed, this formula matched spectroscopic measurements of hydrogen's spectral lines extremely well, making it one of the major triumph's of Bohr's theory, and of early quantum theory in general.

![Image of the hydrogen spectrum](https://upload.wikimedia.org/wikipedia/commons/4/41/Hydrogen_spectrum.svg)

_Hydrogen's spectral lines over different wavelengths. Source: [Wikipedia](https://en.wikipedia.org/wiki/File:Hydrogen_spectrum.svg)_

### The quantum mechanical model of the hydrogen atom

We will now go through the exact, quantum-mechanical model of the hydrogen atom. While our derivation will be primarily focused on hydrogen, the exact solution technically also applies to other types of atoms that have a single electron:

| Atomic species | Chemical symbol | Number of electrons | Number of protons |
| -------------- | --------------- | ------------------- | ----------------- |
| Helium ion     | $\ce{He^+}$     | 1                   | 2                 |
| Lithium ion    | $\ce{Li^{2+}}$  | 1                   | 3                 |
| Beryllium ion  | $\ce{Be^{3+}}$  | 1                   | 4                 |

Moreover, it also applies to all the *isotopes* of hydrogen as well as each of the above atoms (isotopes are atoms with the same number of protons and electrons but different numbers of neutrons); for instance, it applies to deuterium and tritium, which are isotopes with hydrogen with two and three neutrons, respectively. The exact solution also applies to so-called *exotic atoms* with a single electron, including the following:

- **Positronium**, an unstable bound state of an electron and a positron (the antimatter counterpart to an electron). It is of interest in theoretical physics since it uniquely has half the reduced mass of the hydrogen atom and thus its ground-state energy is $E_0 \approx -\pu{6.8 eV}$, half that of the hydrogen atom. It is also used in some particle physics experiments.
- **Muonium**, an unstable bound state of a muon (which behaves very similarly to an electron but with a much greater mass) and an antimuon. It finds uses in [muon spin spectroscopy](https://en.wikipedia.org/wiki/Muon_spin_spectroscopy)
- **Muonic hydrogen**, an unstable bound state of a proton with a muon (effectively a normal hydrogen atom with the electron replaced by a muon). The muon's greater mass means that the atomic radius of muonic hydrogen is $\frac{1}{186}$ that of normal hydrogen atom, allowing nuclear fusion reactions to happen even at room temperature, a phenomenon exploited in [muon-catalyzed fusion](https://en.wikipedia.org/wiki/Muon-catalyzed_fusion).
- **Muonic helium**, an unstable bound state of an alpha particle (helium atom nucleus) with an electron and muon. However, the muon's orbit is so close to the nucleus that, to a good approximation, muonic helium behaves like a single-electron atom

The exact solution for hydrogen-like atom is also an approximate description for atoms with a single *valence electron*, including all the alkaline metals (sodium, potassium, etc.) and ions of other metallic atoms. However, the approximation is imperfect due to the presence of other electrons within the atom (the so-called *quantum defect*).

#### The Hamiltonian of the hydrogen atom

To start, let us write down the Hamiltonian corresponding to the hydrogen atom. As we know from the Bohr model, the hydrogen atom is held together by electromagnetic forces, and in particular the Coulomb force. Thus, our Hamiltonian is given by:

{% math() %}
\hat{H} = \frac{\hat{\mathbf{p}}^2}{2\mu} + V(r) = \frac{\hat{\mathbf{p}}^2}{2\mu} - \frac{Ze^2}{4\pi\varepsilon_{0}r}
{% end %}

Where $\hat{\mathbf{p}}^2$ is the 3-dimensional squared momentum and $\mu$ is the **reduced mass** of hydrogen, which is related to the proton mass $m_p$ and electron mass $m_e$ as:

{% math() %}
\mu = \frac{m_{p}m_{e}}{m_{p} + m_{e}}
{% end %}

To a good approximation $\mu \approx m_e$ (accurate to within 0.5% of the actual value) within the hydrogen atom. We use the reduced mass because the center of mass of the electron-proton system is not technically in the middle of the nucleus; it is slightly offset from it, which is accounted for by the reduced mass.

Owing to the radial symmetry of the hydrogen atom it is most convenient to solve in **spherical coordinates**. There are (at least) two ways to proceed with this. The first way is to expand the Hamiltonian operator, which yields the following extremely-ugly expression:

{% math() %}
\hat{H} =  -{\frac {\hbar ^{2}}{2m}}\left[{\frac {1}{r^{2}}}{\frac {\partial }{\partial r}}\left(r^{2}{\frac {\partial }{\partial r}}\right)+{\frac {1}{r^{2}\sin \theta }}{\frac {\partial }{\partial \theta }}\left(\sin \theta {\frac {\partial }{\partial \theta }}\right)+{\frac {1}{r^{2}\sin ^{2}\theta }}{\frac {\partial ^{2} }{\partial \phi ^{2}}}\right]-{\frac {e^{2}}{4\pi \varepsilon_{0}r}}
{% end %}

One can then treat the eigenvalue equation $\hat H \psi = E \psi$ as a partial differential equation which can be solved using separation of variables. This approach was the one used by Schrödinger and is still commonly-taught today, but it is (in my opinion at least) an inelegant method that makes you think you are learning math instead of quantum mechanics.

Instead, the derivation shown here will use a *different approach* that puts quantum mechanics front-and-center and reveals the intricate quantum theory behind the hydrogen atom. This approach uses an **operator-centric method** that allows us to solve most of the problem using operators that we already know. It is not only *simpler*, but also hopefully provides a *deeper intuition* into the quantum nature of the hydrogen atom.

To begin, we must split the kinetic energy term in the Hamiltonian into a radial part and an angular part. That is to say, we must express $\hat{\mathbf{p}}^2$ in terms of the radial momentum $\hat p_r$ and the angular momentum $\hat{\mathbf{L}}$ (or more precisely, the $\hat{L}^2$ operator). One can derive this by expanding the Laplacian in spherical coordinates and pattern-matching with the expression of the $\hat{L}^2$ (which we have already seen previously), but we will just give the answer here:

{% math() %}
\frac{\hat{\mathbf{p}}^2}{2\mu} = \frac{\hat p_{r}^2}{2\mu} + \frac{\hat{L}^2}{2\mu r^2}
{% end %}

Where $\hat p_r$ and $\hat p_r^2$ are respectively given by:

{% math() %}
\begin{align*}
\hat{p}_{r} &= -i\hbar\left( \frac{\partial}{\partial r} + \frac{1}{r} \right) \\
\hat{p}_{r}^2 &= -\frac{\hbar^2}{r^2} \frac{\partial}{\partial r} \left( r^2 \frac{\partial}{\partial r} \right)
\end{align*}
{% end %}

Thus, our Hamiltonian is given by:

{% math() %}
\hat{H} = \frac{\hat p_{r}^2}{2\mu} + \frac{\hat{L}^2}{2\mu r^2} - \frac{Ze^2}{4\pi \varepsilon_{0}r}
{% end %}

The eigenvalue equation for the Hamiltonian is thus:

{% math() %}
\hat{H}|\psi\rangle = \left( \frac{\hat p_{r}^2}{2\mu} + \frac{\hat{L}^2}{2\mu r^2} - \frac{Ze^2}{4\pi \varepsilon_{0}r} \right)|\psi\rangle = E|\psi \rangle
{% end %}

Now, we will assume that the Hamiltonian is separable, such that we may write the eigenstates of the Hamiltonian as a product of a radial part $|R\rangle$ that only depends on $r$ and an angular part $|\theta, \phi\rangle$ that only depends on $\theta$ and $\phi$. The eigenstates are then a product of the two parts:

{% math() %}
|\psi\rangle = |R\rangle \otimes |\theta, \phi\rangle
{% end %}

(We are using the notation rather loosely here; the product is not technically a tensor product). Similarly, the total energy is a sum of the radial energy $E_{r}$ and angular energy $E_{\theta \phi} = \varepsilon_{\theta \phi} / r^2$ (where the reason we divide by $r^2$ will be evident later):

{% math() %}
E = E_{r} + \frac{\varepsilon_{\theta \phi}}{r^2}
{% end %}

This gives us:

{% math() %}
\left( \frac{\hat p_{r}^2}{2\mu} + \frac{\hat{L}^2}{2\mu r^2} - \frac{Ze^2}{4\pi \varepsilon_{0}r} \right)(|R\rangle \otimes |\theta, \phi\rangle) = \left(E_{r} + \frac{\varepsilon_{\theta \phi}}{r^2}\right)(|R\rangle \otimes |\theta, \phi\rangle)
{% end %}

Now multiplying by $r^2$ on all sides, we have:

{% math() %}
\left( r^2\frac{\hat p_{r}^2}{2\mu} + \frac{\hat{L}^2}{2\mu} - \frac{Ze^2r}{4\pi \varepsilon_{0}} \right)(|R\rangle \otimes |\theta, \phi\rangle) = \left(r^2 E_{r} + \varepsilon_{\theta \phi}\right)(|R\rangle \otimes |\theta, \phi\rangle)
{% end %}

(See why we used the normalized angular energy $\varepsilon_{\theta \phi}/r^2$ rather than just $\varepsilon_{\theta \phi}$ earlier — this allows us to remove the $r^2$ in the $\hat L^2$ term and makes our life easier!) Expanding all the terms and organizing them gives us two eigenvalue equations:

{% math() %}
\begin{align*}
\left( r^2\frac{\hat{p}_{r}^2}{2\mu} - \frac{Ze^2 r}{4\pi\varepsilon_{0}} \right) |R\rangle &= r^2 E_{r}|R\rangle \\
\frac{1}{2\mu} \hat{L}^2 |\theta, \phi\rangle &= \varepsilon_{\theta \phi}|\theta, \phi\rangle
\end{align*}
{% end %}

We will call the top equation the *radial eigenvalue equation* and the bottom equation the *angular eigenvalue equation* and will solve the two separately.

#### Solving the angular eigenvalue equation

The angular eigenvalue equation is straightforward to solve, since we already know the eigenvalues of $\hat L^2$, which are simply $\ell(\ell + 1)\hbar^2$. Thus we have:

{% math() %}
2\mu\varepsilon_{\theta \phi} = \ell(\ell + 1) \hbar^2, \quad -\ell \leq m \leq \ell
{% end %}

We also know that the eigenstates of $\hat L^2$ are simply the spherical harmonics $Y^\ell_m(\theta, \phi)$! Hence, we can write the angular part with the new notation $|\ell, m\rangle$, since we know they depend on the quantum numbers $\ell$ and $m$:

{% math() %}
|\theta, \phi\rangle = |\ell, m\rangle
{% end %}

#### Solving the radial eigenvalue equation

We can now tackle the radial part $|R\rangle$. It is convenient to switch from the operator representation to the functional representation by working in the position basis, where $\langle r|R\rangle = R(r)$ is a function of the radial coordinate. Hence, by multiplying all sides by the position bra-vector $\langle r|$ we have:

{% math() %}
r^2\frac{\hat{p}_{r}^2}{2\mu} R(r) - \frac{Ze^2 r}{4\pi\varepsilon_{0}} R(r) = r^2 E_{r} R(r)
{% end %}

Now, substituting in the explicit form of $\hat{p}_{r}^2 = -\frac{\hbar^2}{r^2} \frac{\partial}{\partial r} \left( r^2 \frac{\partial}{\partial r} \right)$:

{% math() %}
-\frac{\hbar^2}{2\mu} \frac{d}{d r} \left( r^2 \frac{d}{d r} \right) R(r) - \frac{Ze^2 r}{4\pi\varepsilon_{0}} R(r) = r^2 E_{r} R(r)
{% end %}

Where we have switched from partial derivatives to ordinary derivatives ($\frac{\partial}{\partial r} \to \frac{d}{dr}$) since $R(r)$ is only a function of $r$, so the partial derivatives reduce to ordinary derivatives. Now, recall that $E = E_{r} + \frac{\varepsilon_{\theta \phi}}{r^2}$, which we can combine with our previous result (from the angular equation) of $2\mu\varepsilon_{\theta \phi} = \ell(\ell + 1) \hbar^2$. Thus, we may rearrange for $E_r$ as follows:

{% math() %}
E_{r} = E - \frac{\varepsilon_{\theta \phi}}{r^2} = E - \frac{\ell(\ell + 1) \hbar^2}{2\mu r^2}
{% end %}

Substituting this in gives us the following ordinary differential equation:

{% math() %}
-\frac{\hbar^2}{2\mu} \frac{d}{d r} \left( r^2 \frac{d}{d r} \right) R(r) - \frac{Ze^2 r}{4\pi\varepsilon_{0}} R(r) = r^2 \left[E - \frac{\ell(\ell + 1) \hbar^2}{2\mu r^2}\right] R(r)
{% end %}

We'll now use a clever trick for solving differential equations: a change of variables from $R$ to $u$, where $u(r) = rR(r)$. This means that (by the chain rule):

{% math() %}
R = \frac{u}{r}, \quad \frac{dR}{dr} = \frac{1}{r^2}\left( r \frac{du}{dr} - u \right), \quad \frac{d}{dr}\left( r^2 \frac{dR}{dr} \right) = r \frac{d^2 u}{dr^2}
{% end %}

Substituting everything in and simplifying therefore gives us:

{% math() %}
-\frac{\hbar^2}{2\mu} \frac{d^2 u}{dr^2} + \left[ \frac{\hbar^2 \ell(\ell + 1)}{2\mu r^2} - \frac{Ze^2}{4\pi \varepsilon_{0} r} \right] u = Eu
{% end %}

We have therefore obtained the **radial equation** describing the radial part $R(r)$ of the hydrogen atom's wavefunction (which we will just call the *radial wavefunction* for short). Note that the $-\frac{Ze^2}{4\pi \varepsilon_0 r}$ term is specific to the Coulomb potential, but it can be shown (with some tedious math) that the Coulomb potential can be swapped for any central-force potential $V(r)$, giving us a *generalized radial equation*:

{% math() %}
-\frac{\hbar^2}{2\mu} \frac{d^2 u}{dr^2} + \left[ \frac{\hbar^2 \ell(\ell + 1)}{2\mu r^2} + V(r) \right] u = Eu
{% end %}

This generalized radial equation is valid for **all radially-symmetric potentials**. For instance, it can be used for solving the 3D isotropic harmonic oscillator, an infinite spherical well, or a particle quantum-tunneling through a spherical potential barrier (these problems are notably encountered in nuclear physics).

But let's return back to the hydrogen atom with its Coulomb potential. To be able to find $u(r)$, we'll need to solve the radial equation, which is an ordinary differential equation. This is good news and bad news. First, we have reduced a physics problem (of an eigenvalue equation for $\hat p_r^2$) into a math problem. Second, we have reduced a *partial* differential equation into a much simpler *ordinary* differential equation. Third, the radial equation is a *linear* differential equation, which are much easier to solve than nonlinear ODEs frequently encountered in math and physics. Hence, in a meaningful sense, we have greatly reduced the complexity of the problem.

However, the bad news is that we are still left with a differential equation that must be solved, and it isn't particularly clear *how* we would go about solving it. It turns out while the radial equation has an analytical solution, the solution is in terms of *special functions*. This means that instead of elementary functions (like rational, trigonometric, logarithmic, and exponential functions) which are easy to analyze and differentiate, we'll need to use more creativity and more complex mathematics to analyze the solutions of the radial equation.

When we are stuck on solving a differential equation, an excellent technique is to try to cast the differential equation using a change of variables into a well-known ODE with an analytical solution. For instance, we already know that ODEs of the form $u'' = -k^2u$ are simply a variant of the **simple harmonic oscillator ODE** and correspond to analytical solutions of the form $Ae^{-ikr} + Be^{ikr}$. We'll now do the same for the radial equation. It turns out that there *is* a known differential equation that we can transform the radial equation into, called the **associated Laguerre's differential equation**:

{% math() %}
x \frac{d^2 L}{dx^2} + (p + 1 - x) \frac{dL}{dx} + (q-p)L = 0
{% end %}

The solutions to this differential equation are known as the **associated Laguerre polynomials** and are denoted $L^p_{q-p}(x)$, where $p, q$ are nonzero integers (and hence $p - q$ is also an integer). They are given by the [Rodrigues formula](https://en.wikipedia.org/wiki/Rodrigues_formula):

{% math() %}
L^p_{q-p}(x) = (-1)^p \left( \frac{d}{dx} \right)^p L_{q}(x)
{% end %}

Where $L_q$ is a **Laguerre polynomial**, defined as:

{% math() %}
L_{q}(x) = e^x \left( \frac{d}{dx} \right)^q (e^{-x}x^q)
{% end %}

> **Note:** There are several different conventions for the associated Laguerre polynomials; we have chosen the physics convention, which is different from the mathematical convention by a constant factor (and uses some different symbols for the constants).

While the Rodrigues formula may look scary, the associated Laguerre polynomials are ultimately just polynomials. The first few Laguerre polynomials are shown below:

{% math() %}
\begin{align*}
L^0_{0} &= 1 \\
L^0_{1} &= 1 - x \\
L^1_{0} &= 1 \\
L^1_{1} &= 4 - 2x \\
L^2_{0} &= 2 \\
L^2_{1} &= 18 - 6x \\
L^2_{2} &= 12x^2 - 96x + 144 \\
L^3_{0} &= 6 \\
L^3_{1} &= 96 - 24x \\
L^3_{2} &= 60x^2 - 600x + 1200
\end{align*}
{% end %}

To map the radial equation to the associated Laguerre's differential equation, we must perform a series of steps. First, let us define:

{% math() %}
\kappa = \frac{\sqrt{ -2\mu E }}{\hbar}
{% end %}

> **Note:** since $E < 0$ for bound states, $\kappa$ will always be positive, hence the square-root is always well-defined.

Using the substitution for $\kappa$, the radial equation becomes:

{% math() %}
\frac{1}{\kappa^2} \frac{d^2 u}{dr^2} + \left[-\frac{\ell(\ell + 1)}{(\kappa r)^2} + \frac{\mu}{\hbar^2 \kappa^2} \frac{Ze^2}{2\pi \varepsilon_{0} r} \right] u = u
{% end %}

Let us now define:

{% math() %}
\rho_{0} = \frac{Z \mu e^2}{2\pi\varepsilon_{0}\hbar^2 \kappa}
{% end %}

So that we can write the radial equation in the following form (after multiplying all sides by $\kappa^2$ and simplifying):

{% math() %}
\frac{d^2 u}{dr^2} + \left[\frac{\kappa\rho_{0}}{r}-\frac{\ell(\ell + 1)}{r^2} \right] u - \kappa^2 u = 0
{% end %}

Now we can perform a change of coordinates that will turn our equation into an exactly-solvable form. In particular, we will need to use the following change of coordinates to go from $u(r)$ to $L(x)$:

{% math() %}
x = 2 \kappa r, \quad u = x^{\ell + 1} e^{-x / 2} L
{% end %}

Where $x$ is a dimensionless variable. By the chain rule, we have:

{% math() %}
\begin{align*}
\frac{du}{dr} &= \frac{du}{dx} \frac{dx}{dr} = 2\kappa  \frac{du}{dx} \\
\frac{d^2 u}{dr^2} &= \frac{d}{dr}\left( \frac{du}{dr} \right) = \frac{dx}{dr} \frac{d}{dx}\left( 2\kappa \frac{du}{dx} \right) = 4\kappa^2 \frac{d^2 u}{dx^2}
\end{align*}
{% end %}

Substituting these into the simplified radial equation and simplifying gives us:

{% math() %}
4\kappa^2 \frac{d^2 u}{dx^2} + \left[\frac{2\kappa^2 \rho_{0}}{x}-\frac{4\kappa^2\ell(\ell + 1)}{x^2} \right] u - \kappa^2 u = 0
{% end %}

The derivatives $du/dx$ and $d^2u/dx^2$ are rather tedious to compute (since $L$ depends on $x$), but if you compute them (perhaps with the help of a computer algebra system), you will get:

{% math() %}
\begin{align*}
\frac{du}{dx} &= x^\ell e^{-x/2} \left( x \frac{dL}{dx} - \frac{x}{2}L + (\ell + 1)L \right) \\
\frac{d^2 u}{dx^2} &= x^{\ell - 1} e^{-x/2}\left\{ x^2 \frac{d^2 L}{dx^2} - (x^2 -  2x(\ell + 1)) \frac{dL}{dx} + \left[\frac{x^2}{4} - (\ell + 1)x + \ell(\ell + 1) \right] L \right\}
\end{align*}
{% end %}

Substituting these derivatives in and simplifying, we get:

{% math() %}
x \frac{d^2 L}{dx^2} + [2(\ell + 1) - x] \frac{dL}{dx} + \left( \frac{\rho_{0}}{2} - (\ell + 1) \right) L = 0
{% end %}

Now, let's compare with the general form of the associated Laguerre's differential equation that we found earlier:

{% math() %}
x \frac{d^2 L}{dx^2} + (p + 1 - x) \frac{dL}{dx} + (q-p)L = 0
{% end %}

By term-by-term comparison we identify the following:

{% math() %}
p + 1 = 2(\ell + 1), \quad q-p = \frac{\rho_{0}}{2} - (\ell + 1)
{% end %}

From which it is not hard to see that $p = 2\ell + 1$. Also, remember that we mentioned that both $p$ and $q$ *must* be non-negative integers, hence $q-p$ is also an integer.

{% math() %}
q - p = q - [2 \ell + 1] = (q - \ell) - (\ell + 1)
{% end %}

But we *also* know that $q - p = \rho_0 / 2 - (\ell + 1)$. Therefore, by term-by-term comparison:

{% math() %}
\frac{\rho_{0}}{2} - \cancel{ (\ell + 1) } = (q - \ell) - \cancel{ (\ell + 1) } \implies q - \ell = \frac{\rho_{0}}{2} = n
{% end %}

Where we have defined a new integer $n \equiv q - \ell$, called the **principal quantum number**, meaning that:

{% math() %}
q-p = (n + \ell) - (2\ell + 1) = n - \ell - 1
{% end %}

We therefore obtain the following solutions in terms of the associated Laguerre polynomials:

{% math() %}
L^p_{q-p}(x) = L^{2\ell + 1}_{n - \ell - 1}(x), \quad n = 1, 2, 3, \dots, \quad \ell = 0, 1, 2, \dots, (n-1)
{% end %}

Where the condition $n \geq 1$ comes from the fact that $q - p$ (which, as we saw, is equal to $n - \ell - 1$) must be a non-negative integer and the spherical harmonics require that $\ell \geq 0$, meaning that $n - \ell -1 \geq 0$ and thus $n \geq 1$. We can now work backwards to get the radial wavefunction. For this, we use our coordinate transformations $u = rR(r)$, $x = 2\kappa r$, and $u = x^{\ell + 1} e^{-x / 2} L$, giving us:

{% math() %}
\begin{align*}
R(r) &= \frac{u}{r} = 2\kappa x^{-1} u \\
&= 2\kappa x^{-1} x^{\ell + 1} e^{-x / 2} L^{2\ell + 1}_{n - \ell - 1}(x) \\
&= 2\kappa x^{\ell} e^{-x / 2} L^{2\ell + 1}_{n - \ell - 1}(x)
\end{align*}
{% end %}

It is conventional to use the symbol $\rho$ instead of $x$. In addition, it is common to label $R(r)$ with the indices $n$ and $\ell$ to indicate that it is a function parametrized by the constants $n, \ell$. Hence we may write $R(r) = R_{n\ell}(r)$ as:

{% math() %}
R_{n\ell}(r) = 2\kappa e^{-\rho / 2} \rho^\ell L^{2\ell + 1}_{n-\ell - 1}(\rho), \quad \rho = 2\kappa r
{% end %}

After much ado, we have finally found the radial wavefunction! Now, we just need to solve for $\kappa$. We know that $\rho_{0} = \frac{Z \mu e^2}{2\pi\varepsilon_{0}\hbar^2 \kappa}$ and that $\rho_0/2 = n$. Combining these two together, we get:

{% math() %}
2n = \frac{Z \mu e^2}{2\pi\varepsilon_{0}\hbar^2 \kappa} \implies \kappa = \frac{Z \mu e^2}{4\pi\varepsilon_{0}\hbar^2 n}
{% end %}

The above expression for $\kappa$ may not mean anything just yet, but it becomes far more illustrative when we realize that it can *also* be written as:

{% math() %}
\kappa = \frac{Z}{na_{0}^*}
{% end %}

Where $a_0^*$ is the **reduced Bohr radius**, and is related to the regular Bohr radius $a_0$, the reduced mass $\mu$, and electron mass $m_e$ via:

{% math() %}
a_{0}^* = \frac{m_{e}}{\mu} a_{0} \approx a_{0}, \quad a_{0} = \frac{4\pi \varepsilon_{0} \hbar^2}{m_{e}e^2}
{% end %}

(The approximation of $a_0^* \approx a_0$ is correct to within 0.5%). This is the *same Bohr radius* as the one predicted by Bohr's older atomic theory! We can also now give a *physical interpretation* of the Bohr radius. While we will not do the full calculation, it turns out that the *maximum* of the probability density function (which is proportional to the square of $R_{n\ell}$) occurs at $r = a_0^* \approx a_0$. Hence, the Bohr radius (or more accurately, the reduced Bohr radius) is the radius at which an electron is **most likely** to be found in the ground-state of hydrogen. While the idea of electrons going in circular orbits around the nucleus in Bohr's theory is physically-incorrect, its predictions coincide with the predictions of quantum theory!

#### The wavefunctions and energy levels of the hydrogen atom

With both the angular and radial wavefunctions solved for, we can now put everything together. The full wavefunctions are simply a product of the angular and radial parts, that is:

{% math() %}
\psi_{n\ell m} = A_{n \ell m} R_{n\ell}(r) Y^m_\ell(\theta, \phi)
{% end %}

Where $A_{n\ell m}$ is a normalization constant that can be found using the normalization condition:

{% math() %}
\int_{0}^{2\pi} \int_{0}^\pi \int_{0}^\infty |\psi_{n \ell m}(r, \theta, \phi)|^2 r^2 \sin \theta dr d\theta d\phi = 1
{% end %}

(We will not perform the integral here, but curious readers are welcome to do so). Upon completing normalization, we finally get the *glorious* wavefunctions of the hydrogen atom!

{% math() %}
\psi_{n\ell m}(r, \theta, \phi) = \sqrt{ \left( \frac{2}{na_{0}^*} \right)^3 \frac{(n - \ell - 1)!}{2n[(n + \ell)!]^3} } e^{-\rho / 2} \rho^\ell L^{2\ell + 1}_{n-\ell - 1}(\rho) Y^m_{\ell}(\theta, \phi), \quad \rho = \frac{2Zr}{na_{0}^*}
{% end %}

Where $a_0^*$ is the reduced Bohr radius, $\ell = 0, 1, \dots, \pm (n-1)$ and $m = -\ell, \dots, \ell$. This may seem extremely complicated (perhaps even overcomplicated!) but nature has at least given us an *exact solution*; most quantum systems don't have an exact solution, so we should be grateful!

> **Note:** We can also denote the wavefunctions in bra-ket notation as $|n, \ell, m\rangle$. This is a form we will often use in calculations.

Having found the wavefunctions, let's now calculate the energy eigenvalues of the Hamiltonian, which correspond to energy levels of the atom. We can start by finding $E$ in terms of $\kappa$:

{% math() %}
\kappa = \frac{\sqrt{ -2\mu E }}{\hbar} \implies E = - \frac{\hbar^2 \kappa^2}{2\mu}
{% end %}

Now, recall that we found that $\kappa = \frac{Z}{na_{0}^*}$. Substituting this in, we get an expression for the energies of the hydrogen atom:

{% math() %}
E_{n} = -\frac{\hbar^2}{2\mu} \left( \frac{Z}{na_{0}^*} \right)^2 = -\frac{\hbar^2 Z^2}{2\mu (a_{0}^*)^2 n^2} = -\frac{Z^2 \mu e^4}{32\pi^2 \varepsilon_{0}^2 \hbar^2} \approx -(\pu{13.6 eV})\frac{Z^2}{n^2}
{% end %}

This is the same result as in the Bohr atom! Note that the energy levels are *always negative* which is what we expect for a bound state; if the electron were not bound to a nucleus, atoms would no longer be atoms! However, in the limit of very large $n$, the electron becomes close to unbound, and a bit of extra energy is enough to ionize the atom and cause the electron to become a free particle.

> **Note for the advanced reader:** If an electron has $E> 0$ then we have Coulomb scattering (electrons scattering off a nucleus instead of becoming bound to a nucleus and forming an atom). This is a modified form of Rutherford scattering, which is itself a variety of generalized [electron scattering](http://hyperphysics.phy-astr.gsu.edu/hbase/Nuclear/elescat.html). However, to handle these sorts of problems, we will need to wait until we discuss the **Born approximation** much later in this guide.

#### Degeneracy in the hydrogen atom

Most of the eigenstates of the hydrogen atom are degenerate (that is, sharing the same energy as one or more other states). In fact, the **degree of degeneracy** of the hydrogen atom is $n^2$. This means that for the $n$-th energy level, there will be $n^2$ states that share the same energy, as described in the table below:

| $n$ | Number of same-energy states |
| --- | ---------------------------- |
| 1   | 1                            |
| 2   | 4                            |
| 3   | 9                            |
| 4   | 16                           |
| 5   | 25                           |
| 6   | 36                           |

We will now give a short derivation. Since the energy levels $E_n$ only depend upon $n$, we need to count all the possible states $|n, \ell, m\rangle$ that share the same $n$. We know that $\ell$ ranges from zero to $n -1$.

We also know that $-\ell \leq m \leq \ell$, meaning that there are $2\ell + 1$ states with the same value of $\ell$ but different $m$ (the $+1$ is due to $m = 0$ being a possibility as well). Therefore, summing over the states yields us:

{% math() %}
\sum_{\ell} \sum_{m} = \sum_{\ell = 0}^{n - 1} (2\ell + 1) = n^2
{% end %}

> **Note:** Our calculation of the number of degenerate states is not *technically accurate* since it neglects the effect of **spin**. If we include spin (giving us a fourth quantum number) the degrees of degeneracy are $2n^2$ instead of $n^2$.

## Stationary perturbation theory

Perturbation theory exists when we come upon a problem that is too complicated to solve exactly. These problems are often (but not always) variations of existing problems. For instance, we know the solution of the hydrogen atom, since that can be solved exactly, but it turns out that for the _helium atom_, which has just one more electron than the hydrogen atom, there is no analytical solution! In such cases, we typically resort to one of two options:

1. Solve the system on a computer using [numerical methods](https://ui.adsabs.harvard.edu/abs/2013PhDT.......102J/abstract)
2. Find an _approximate_ analytical solution

The second option is what we'll focus on here, since numerical methods in quantum mechanics is a topic broad enough for an entire textbook on its own. This approach - making calculations using approximations - is known as **perturbation theory**, and it allows us to solve many kinds of problems that cannot be solved exactly.

> **Note:** Perturbation theory, despite its association with quantum mechanics, is actually a *far more general* technique for solving complicated differential equations (even those describing classical systems). For more information, see [this excellent article](https://jacopobertolotti.com/PerturbationIntro.html) on a classical application of perturbation theory.

First off, we should mention that there are two general kinds of perturbation theory in quantum mechanics: **stationary perturbation theory**, which (as the name suggests) applies only for stationary (time-independent) problems, and **time-dependent perturbation theory**, which applies for problems that explicitly depend on time. Right now, we'll be focusing on stationary perturbation theory; we'll get to the time-dependent version later. While there are notable differences, both types of perturbation theory use the same general method: a complicated system is approximated as a simpler, more familiar system with some added corrections (called _perturbations_). By computing these correction terms, we are then able to find an *approximate solution* to the system, even if there is no exact analytical solution.

![A comic humorously describing the concept of perturbation theory](https://imgs.xkcd.com/comics/physicists_2x.png)

_A description of perturbation theory from [XKCD](https://xkcd.com/793/)._

### Non-degenerate perturbation theory

We will first review the _simplest_ type of stationary perturbation theory, known as **non-degenerate perturbation theory** (also known as _Rayleigh-Schrödinger perturbation theory_), which applies to quantum systems _without_ degeneracy (meaning that each eigenstate is uniquely associated with a distinct energy eigenvalue of the Hamiltonian). It turns out that this is in many cases an _overly simplified_ assumption, but the methods we will develop here will be extremely useful for our later discussion of **degenerate perturbation theory** that accurately describes a variety of real-world quantum systems.

Mathematically-speaking, non-degenerate perturbation theory assumes that the Hamiltonian of a complicated system can be written as a sum of a Hamiltonian $\hat H_0$ with an _exact_ solution and a small *perturbation* $\Delta \hat{H}$, such that:

{% math() %}
\hat{H} = \hat{H}_{0} + \Delta \hat{H}, \quad \Delta \hat{H} = \lambda\hat{W}
{% end %}

Here $\hat H_0$ is known as the **unperturbed Hamiltonian** or **free Hamiltonian**. For instance, $\hat H_0$ might be the Hamiltonian of a free particle, or of the hydrogen atom, or the quantum harmonic oscillator. The key commonality here is that $\hat H_0$ must be the Hamiltonian of a **simpler system** that can be analytically solved.

> **Note:** It is common to write $\Delta \hat{H}$ without the operator hat, and it is also common to denote it as $V$ (confusingly). Be aware that in all cases, $W$ is an **operator**, not a function!

On top of $\hat H_0$ we add the perturbation $\Delta \hat{H}$, which represents the *deviations* (also called _perturbations_) of the system's Hamiltonian as compared to the simpler system. This perturbation is assumed to be small, so we scale it by a small number $\lambda$ (where $\lambda \ll 1$), giving us a term of $\Delta \hat{H} = \lambda \hat W$ where $\hat W$ is some arbitrary operator representing perturbations to the Hamiltonian. If we write out the Schrödinger equation for the system, we have:

{% math() %}
\hat{H}|\varphi_{n}\rangle = E_{n} |\varphi_{n}\rangle \quad \Rightarrow \quad (\hat{H}_{0} + \lambda\hat{W})\varphi_{n}\rangle = E_{n} |\varphi_{n}\rangle
{% end %}

Note that when we take the limit $\lambda \to 0$, the perturbation vanishes, and the Hamiltonian is exactly the unperturbed Hamiltonian $\hat H_0$. This is why perturbation theory is an *approximation*; it assumes that the simpler system's Hamiltonian $\hat H_{0}$ is already close enough to the more complicate system's Hamiltonian $\hat H$ that $\hat H_0$ can be used to approximate $\hat H$.

The key idea of perturbation theory is that we assume a **series solution** for $\hat{H}|\varphi_{n}\rangle = E_{n}|\varphi_{n}\rangle$. More accurately, we assume that we can write the solution in terms of a *power series* in powers of $\lambda$. Now, this assumption doesn't always work - in fact there are some systems where it doesn't work at all - but using this assumption makes it possible to find an approximate solution using analytical methods, which is "good enough" for most purposes. Remember, in the real world, it is *impossible* to measure anything to infinite precision, so having an approximate answer to a problem that is *close enough* to the exact solution is often more than sufficient to make testable predictions that align closely with experimental data.

#### Derivation of non-degenerate perturbation theory

To begin, remember that we aim to find the approximate wavefunctions and eigenenergies of the Hamiltonian. We also assume that the exact eigenstates $|\psi\rangle$ can be expressed as a power series in $\lambda$:

{% math() %}
\begin{align*}
|\varphi_{n}\rangle &= \sum_{m = 0}^\infty \lambda^m|\varphi_{n}^{(m)}\rangle \\
&=|\varphi_{n}^{(0)}\rangle + \lambda|\varphi_{n}^{(1)}\rangle + \lambda^2|\varphi_{n}^{(2)}\rangle + \dots
\end{align*}
{% end %}

Here, remember that $|\varphi_{n}\rangle$ is the *exact* solution to the system (representing all $n$ *exact* eigenstates of the complicated Hamiltonian $\hat H$), but $|\varphi_{n}^{(0)}\rangle, |\varphi_{n}^{(1)}\rangle, |\varphi_{n}^{(2)}\rangle, \dots$ are *successive states* whose sum *converges* to the exact eigenstates of the system. (For those who need a refreshed on power series please see the [series and sequences guide](@/series-sequences.md)). Be aware that the brackets $(1), (2), \dots$ are **not** exponents; rather they are labels for the successive sets of eigenstates (the first set of eigenstates, the second, the third, and so forth). By summing up infinitely many of these terms in the expansion of the Hamiltonian's eigenstates, we would in principle get the _exact eigenstates_ of the complicated Hamiltonian.

In the same way, we assume that the system's energy eigenvalues $E_n$ can also be written as a power series in $\lambda$, given by:

{% math() %}
\begin{align*}
E_{n} &= \sum_{m=0}^\infty \lambda^m E_{n}^{(m)} \\
&= E_{n}^{(0)} + \lambda E_{n}^{(1)} + \lambda^2 E_{{n}}^{(2)} + \dots
\end{align*}
{% end %}

The first term in the expansion, $E_n^{(0)}$, as we'll see, are simply the energy eigenvalues of the unperturbed Hamiltonian $\hat H_0$. The subsequent terms $E_{n}^{(1)}$, $E_{n}^{(2)}$ are known as the **first-order correction** and **second-order correction** to the energy eigenvalues, since they respectively have coefficients of $\lambda^1$ and $\lambda^2$. By summing up infinitely many of these terms in the expansion of the energy, we would in principle get the _exact energies_.

Now, if we substitute our power series solution into the Hamiltonian's eigenvalue equation $\hat{H}|\varphi_{n}\rangle = E_{n}|\varphi_{n}\rangle$, we have:

{% math() %}
\begin{align*}
(\hat{H}_{0} + \lambda \hat{W})(|\varphi_{n}^{(0)}\rangle &+ \lambda|\varphi_{n}^{(1)}\rangle + \lambda^2|\varphi_{n}^{(2)}\rangle + \dots) \\
&= (E_{n}^{(0)} + \lambda E_{n}^{(1)} + \lambda^2 E_{{n}}^{(2)} + \dots)(|\varphi_{n}^{(0)}\rangle + \lambda|\varphi_{n}^{(1)}\rangle + \lambda^2|\varphi_{n}^{(2)}\rangle + \dots)
\end{align*}
{% end %}

Distributing the left-hand side gives us:

{% math() %}
\begin{align*}
\hat{H}_{0}\bigg(|\varphi_{n}^{(0)}\rangle &+ \lambda|\varphi_{n}^{(1)}\rangle + \lambda^2|\varphi_{n}^{(2)}\rangle + \dots\bigg)
+ \lambda \hat{W}\bigg(|\varphi_{n}^{(0)}\rangle + \lambda|\varphi_{n}^{(1)}\rangle + \lambda^2|\varphi_{n}^{(2)}\rangle + \dots\bigg)
\\
&= E_{n}^{(0)}\left(|\varphi_{n}^{(0)}\rangle + \lambda|\varphi_{n}^{(1)}\rangle + \lambda^2|\varphi_{n}^{(2)}\rangle + \dots\right) \\
&\qquad+ \lambda E_{n}^{(1)}\left(|\varphi_{n}^{(0)}\rangle + \lambda|\varphi_{n}^{(1)}\rangle + \lambda^2|\varphi_{n}^{(2)}\rangle + \dots\right)\\
&\qquad+ \lambda^2 E_{n}^{(2)}\left(|\varphi_{n}^{(0)}\rangle + \lambda|\varphi_{n}^{(1)}\rangle + \lambda^2|\varphi_{n}^{(2)}\rangle + \dots\right)
\end{align*}
{% end %}

If we do some algebraic manipulation to group terms by powers of $\lambda$, we get:

{% math() %}
\begin{align*}
% LHS of equation
\hat{H}_{0}|\varphi_{n}^{(0)}\rangle &+ \lambda \left(\hat{H}_{0}|\varphi_{n}^{(1)}\rangle + \hat{ W}|\varphi_{n}^{(0)}\rangle\right) + \lambda^2\left(\hat{H}_{0}|\varphi_{n}^{(2)}\rangle + \hat{W}|\varphi_{n}^{(1)}\rangle\right) + \dots \\
&= 
% RHS of equation
E_{n}^{(0)}|\varphi_{n}^{(0)}\rangle + \lambda\left(E_{n}^{(0)}|\varphi_{n}^{(1)}\rangle + E_{n}^{(1)}|\varphi_{n}^{(0)}\rangle\right)
+ \lambda^2 \left(E_{n}^{(0)}|\varphi_{n}^{(2)}\rangle + E_{n}^{(1)}|\varphi_{n}^{(1)}\rangle + E_{n}^{(2)}|\varphi_{n}^{(0)}\rangle\right) + \dots
\end{align*}
{% end %}

Notice how each term on the left-hand side of the equation now corresponds to a term on the right-hand side with the same power of $\lambda$. Thus, by equating the quantities in the brackets for every power of $\lambda$, we get a **system of equations** to solve for each order of $\lambda$:

{% math() %}
\begin{align*}
\mathcal{O}(\lambda^0):& \quad E_{n}^{(0)}|\varphi_{n}^{(0)}\rangle \\
\mathcal{O}(\lambda^1):& \quad \lambda \left(\hat{H}_{0}|\varphi_{n}^{(1)}\rangle 
+ \hat{W}|\varphi_{n}^{(0)}\rangle\right) = \lambda\left(E_{n}^{(0)}|\varphi_{n}^{(1)}\rangle + E_{n}^{(1)}|\varphi_{n}^{(0)}\rangle\right) \\ 
\mathcal{O}(\lambda^2):& \quad \lambda^2\left(\hat{H}_{0}|\varphi_{n}^{(2)}\rangle + \hat{W}|\varphi_{n}^{(1)}\rangle\right) = \lambda^2 \left(E_{n}^{(0)}|\varphi_{n}^{(2)}\rangle + E_{n}^{(1)}|\varphi_{n}^{(1)}\rangle + E_{n}^{(2)}|\varphi_{n}^{(0)}\rangle\right) \\
& \qquad\vdots  \\
\mathcal{O}(\lambda^n): &\quad \lambda^n\left(\hat{H}_{0}|\varphi_{n}^{(n)}\rangle 
+ \hat{W}|\varphi_{n}^{(n-1)}\rangle\right) = \lambda^n\left( E_{n}^{(0)}|\varphi_{n}^{(n)}\rangle + \sum_{j = 1}^n E_{n}^{(j)} \left|\varphi_{n}^{(n - j)}\right\rangle\right)
\end{align*}
{% end %}

> **Note:** The final, generalized expression for $\mathcal{O}(\lambda^n)$ comes from [Dr. Moore's Lecture Notes](https://web.pa.msu.edu/people/mmoore/TIPT.pdf) from Michigan State University.

If we solve every single one of these equations and substituted our found values of the energy corrections $E_n^{(1)}, E_n^{(2)}, E_n^{(3)}, \dots$ and the corrections to the eigenstates $|\varphi_{n}^{(1)}\rangle, |\varphi_{n}^{(2)}\rangle, |\varphi_{n}^{(3)}\rangle, \dots$ we would in principle know the **exact eigenstates and energies** of the system.

However, in practice, we obviously wouldn't want to solve infinitely many equations, so we usually truncate the series to just a few terms to get an approximate answer to our desired accuracy. For the lowest-order approximation (also called the **zeroth-order approximation**) we keep only terms of order $\mathcal{O}(\lambda^0)$ - or in simpler terms, drop all terms containing $\lambda$. We are thus left with just the equation for $\mathcal{O}(\lambda^0)$, that is:

{% math() %}
\hat H_0|\varphi_n^{(0)}\rangle = E_n^{(0)}|\varphi_n^{(0)}\rangle
{% end %}

The result is trivial - this is just the eigenvalue equation of the unperturbed Hamiltonian, which we can solve exactly, and tells us nothing new. However, let's keep going, because the **first-order approximation** will be where we'll find a crucial result from perturbation theory. In the first-order approximation we include all terms up to *first-order* in $\lambda$, but no higher-order terms (i.e. ignoring $\lambda^2, \lambda^3, \lambda^4, \dots$ terms). This means that:

{% math() %}
|\varphi_{n}\rangle \approx |\varphi_{n}^{(0)}\rangle + \lambda|\varphi_{n}^{(1)}\rangle, \quad E_n \approx E_{n}^{(0)} + \lambda E_{n}^{(1)}
{% end %}

We will thus also need to solve the second equation in the system of equations we previously derived, given by:

{% math() %}
(\hat{H}_{0} - E_{n}^{(0)})|\varphi_{n}^{(1)}\rangle 
+ \hat{W}|\varphi_{n}^{(0)}\rangle =  E_{n}^{(1)}|\varphi_{n}^{(0)}\rangle
{% end %}

Now, the trick is to take the inner product of the above equation with the bra $\langle \varphi_n^{(0)}|$. This gives us:

{% math() %}
\langle \varphi_n^{(0)}|(\hat{H}_{0} - E_{n}^{(0)})|\varphi_{n}^{(1)}\rangle 
+ \langle \varphi_n^{(0)}|\hat{W}|\varphi_{n}^{(0)}\rangle =  \langle \varphi_n^{(0)}|E_{n}^{(1)}|\varphi_{n}^{(0)}\rangle
{% end %}

Since $\hat H_0$ is a Hermitian operator, we know that for any two states $|\phi\rangle, |\psi\rangle$, it must be the case that $\langle \phi|\hat H_0|\psi\rangle = \big(\langle \phi|\hat H_0\big)\cdot|\psi\rangle$, meaning that:

{% math() %}
\langle \varphi_n^{(0)}|(\hat{H}_{0} - E_{n}^{(0)})|\varphi_{n}^{(1)}\rangle = \underbrace{ \bigg(\langle \varphi_n^{(0)}|\hat{H}_{0} - \langle \varphi_n^{(0)}|E_{n}^{(0)}U\bigg) }_{ \hat H_0|\varphi_n^{(0)}\rangle = E_n^{(0)}|\varphi_n^{(0)}\rangle }|\varphi_{n}^{(1)}\rangle = 0
{% end %}

Thus the entire first term goes to zero, and we are simply left with:

{% math() %}
\langle \varphi_n^{(0)}|\hat{W}|\varphi_{n}^{(0)}\rangle = \langle \varphi_n^{(0)}|E_{n}^{(1)}|\varphi_{n}^{(0)}\rangle
{% end %}

But since our states are normalized, then it must be the case that the right-hand side reduces to:

{% math() %}
\begin{align*}
\langle \varphi_n^{(0)}|E_{n}^{(1)}|\varphi_{n}^{(0)}\rangle &= E_{n}^{(1)} \underbrace{ \langle \varphi_n^{(0)}|\varphi_{n}^{(0)}\rangle }_{ 1 } = E_{n}^{(1)} \\
&\Rightarrow~\langle \varphi_n^{(0)}|\hat{W}|\varphi_{n}^{(0)}\rangle = \langle \varphi_n^{(0)}|E_{n}^{(1)}|\varphi_{n}^{(0)}\rangle = E_{n}^{(1)}
\end{align*}
{% end %}

Finally, after fully simplifying our results, we come to a refreshingly-simple expression for the first-order correction to the eigenenergies:

{% math() %}
E_n^{(1)} = \langle \varphi_n^{(0)}|\hat W |\varphi_{n}^{(0)}\rangle
{% end %}

Note that the result is very general since it applies for _all_ $n$ eigenstates of the system. Adding in the first-order corrections gives us the (approximate) eigenenergies of the system:

{% math() %}
\begin{align*}
E_n &\approx E_{n}^{(0)} + \lambda E_{n}^{(1)} \\
&= E_{n}^{(0)} + \lambda \langle \varphi_n^{(0)}|\hat W |\varphi_{n}^{(0)}\rangle
\end{align*}
{% end %}

Alternatively, if written in terms of the perturbation term $\Delta \hat H$ in the Hamiltonian, we can express the first-order shift in the energy eigenvalues $\Delta E_n^{(1)}$ as:

{% math() %}
\Delta E_{n}^{(1)} = \lambda \langle \varphi_n^{(0)}|\hat W |\varphi_{n}^{(0)}\rangle = \langle \varphi_n^{(0)}| \Delta \hat{H} |\varphi_{n}^{(0)}\rangle
{% end %}

This is one of the **most important** equations in all of quantum mechanics and in most cases gives a good approximation to the exact eigenenergies of the system, at least where $\lambda$ is small. It allows us to solve a variety of quantum systems that would otherwise be impossible to solve exactly, and to a large extent, is responsible for why we can perform quantum-mechanical calculations for complicated real-world systems at all!

We can use a similar process to get the first-order correction $|\varphi_n^{(1)}\rangle$ to the eigenstates of the system. We'll spare the derivation for now and just state the results - the first-order correction to the system's eigenstates are given by:

{% math() %}
\begin{align*}
|\varphi_n^{(1)}\rangle &= \sum_{m\,(m \neq n)} \frac{E_{n}^{(1)}}{\left(\small E_{n}^{(0)} - E_{m}^{(0)}\right)}|\varphi_m^{(0)}\rangle \\
&= \sum_{m\,(m \neq n)} \frac{\langle \varphi_m^{(0)}|\hat W |\varphi_{n}^{(0)}\rangle}{\left(\small E_{n}^{(0)} - E_{m}^{(0)}\right)}|\varphi_m^{(0)}\rangle
\end{align*}
{% end %}

In most cases, the first-order correction is sufficient to get a "good enough" answer. But we can go further to get a more accurate result! We'll now use a **second-order approximation**, where we include all terms up to _second-order_ in $\lambda$, but no higher-order terms (i.e. ignoring $\lambda^3, \lambda^4, \lambda^5, \dots$ terms). This means that:

{% math() %}
\begin{align*}
|\varphi_{n}^{(0)}\rangle &\approx 
|\varphi_{n}^{(0)}\rangle + \lambda|\varphi_{n}^{(1)}\rangle + \lambda^2|\varphi_{n}^{(2)}\rangle \\ E_{n} &\approx E_{n}^{(0)} + \lambda E_{n}^{(1)} + \lambda^2 E_{{n}}^{(2)}
\end{align*}
{% end %}

We'll therefore need the third equation in the system of equations we derived at the start of this section, which is given by:

{% math() %}
\lambda^2\left(\hat{H}_{0}|\varphi_{n}^{(2)}\rangle + \hat{W}|\varphi_{n}^{(1)}\rangle\right) = \lambda^2 \left(E_{n}^{(0)}|\varphi_{n}^{(2)}\rangle + E_{n}^{(1)}|\varphi_{n}^{(1)}\rangle + E_{n}^{(2)}|\varphi_{n}^{(0)}\rangle\right)
{% end %}

Again, making some algebraic simplifications gives us:

{% math() %}
(\hat{H}_{0} - E_{n}^{(0)})|\varphi_{n}^{(2)}\rangle + \hat{W}|\varphi_{n}^{(1)}\rangle =  E_{n}^{(1)}|\varphi_{n}^{(1)}\rangle + E_{n}^{(2)}|\varphi_{n}^{(0)}\rangle
{% end %}

Using our trick from before by taking the inner product with $\langle \varphi_n^{(0)}|$ and exploiting orthogonality, we get:

{% math() %}
\underbrace{ \langle \varphi_n^{(0)}|(\hat{H}_{0} - E_{n}^{(0)}) }_{ 0 }|\varphi_{n}^{(2)}\rangle + \langle \varphi_n^{(0)}|\hat{W}|\varphi_{n}^{(1)}\rangle =  E_{n}^{(1)}\cancel{ \langle \varphi_n^{(0)}|\varphi_{n}^{(1)}\rangle }^0 + E_{n}^{(2)}\cancel{ \langle \varphi_n^{(0)}|\varphi_{n}^{(0)}\rangle }^1
{% end %}

Where the first term again becomes zero since {% inlmath() %}\hat{H}_{0}|\varphi_{n}^{(0)}\rangle = E_{n}^{(0)}|\varphi_{n}^{(0)}\rangle{% end %} and since $\hat H_0$ is Hermitian - this follows the same reasoning we explained for the first-order case. We thus have:

{% math() %}
E_{n}^{(2)} =  \langle \varphi_n^{(0)}|\hat{W}|\varphi_{n}^{(1)}\rangle
{% end %}

But we previously found that $|\varphi_n^{(1)}\rangle$ is given by:

{% math() %}
|\varphi_n^{(1)}\rangle = \sum_{m\,(m \neq n)} \frac{\langle \varphi_m^{(0)}|\hat W |\varphi_{n}^{(0)}\rangle}{\left(\small E_{n}^{(0)} - E_{m}^{(0)}\right)}|\varphi_m^{(0)}\rangle
{% end %}

Thus substituting it into our expression for $E_n^{(2)}$ gives us an explicit expression for the second-order corrections to the eigenenergies of the system:

{% math() %}
\begin{align*}
E_{n}^{(2)} &= \langle \varphi_n^{(0)}|\hat{W}|\varphi_{n}^{(1)}\rangle \\
&= \langle \varphi_{n}^{(0)}|\hat{W} \left(\sum_{m\,(m \neq n)} \frac{\langle \varphi_m^{(0)}|\hat W |\varphi_{n}^{(0)}\rangle}{\left(\small E_{n}^{(0)} - E_{m}^{(0)}\right)}|\varphi_m^{(0)}\rangle\right) \\
&= \sum_{m\,(m \neq n)} \frac{|\langle \varphi_m^{(0)}|\hat W |\varphi_{n}^{(0)}\rangle|^2}{\left(\small E_{n}^{(0)} - E_{m}^{(0)}\right)}
\end{align*}
{% end %}

Equivalently, the second-order shift in the energy eigenvalues $\Delta E_n^{(2)}$ is given by:

{% math() %}
\Delta E_n^{(2)} = \sum_{m\,(m \neq n)} \frac{|\langle \varphi_m^{(0)}|\Delta\hat H |\varphi_{n}^{(0)}\rangle|^2}{\left(\small E_{n}^{(0)} - E_{m}^{(0)}\right)}
{% end %}

While we will not derive it here, one may show that the *third-order corrections* to the eigenenergies of the system are given by:

{% math() %}
E_{n}^{(3)} = \sum_{m~(m \neq n)}\sum_{l} \frac{V_{nl} V_{lm} V_{mn}}{\small (E_{n}^{(0)} - E_{l}^{(0)})(E_{n}^{(0)} - E_{m}^{(0)})} - V_{nn}\sum_{m\,(m \neq n)} \frac{|V_{nm}|^2}{\left(\small E_{n}^{(0)} - E_{m}^{(0)}\right)^2}|\varphi_m^{(0)}\rangle
{% end %}

Where here, $V_{ij} \equiv \langle \varphi_{i}^{(0)}|\hat{W}|\varphi_{j}^{(0)}\rangle$. Therefore, the third-order shift in the energy eigenvalues $\Delta E_n^{(3)}$ is:

{% math() %}
\Delta E_{n}^{(3)} = \sum_{m~(m \neq n)}\sum_{l} \frac{E_{nl} E_{lm} E_{mn}}{\small (E_{n}^{(0)} - E_{l}^{(0)})(E_{n}^{(0)} - E_{m}^{(0)})} - V_{nn}\sum_{m\,(m \neq n)} \frac{|E_{nm}|^2}{\left(\small E_{n}^{(0)} - E_{m}^{(0)}\right)^2}|\varphi_m^{(0)}\rangle
{% end %}

Where $E_{ij} = \langle \varphi_{i}^{(0)}|\Delta\hat{H}|\varphi_{j}^{(0)}\rangle$. Note that in the most general case, we can find the $k$-th order correction to the eigenenergies of the system via:

{% math() %}
E_{n}^{(k)} = \langle \varphi_{n}^{(0)}|\hat{W}|\varphi_{n}^{(k - 1)}\rangle
{% end %}

Equivalently, the $k$-th order energy shift is given by:

{% math() %}
\Delta E_{n}^{(k)} = \langle \varphi_{n}^{(0)}|\Delta \hat{H}|\varphi_{n}^{(k - 1)}\rangle
{% end %}

And the exact energies $E_{n}$ of the system are given by the infinite series:

{% math() %}
E_{n} = E_{n}^{(0)} + \sum_{m = 1}^\infty \Delta E_{n}^{(m)}
{% end %}

In practice, the first few terms of the series are usually enough to yield an exceedingly accurate calculation for the system's energy eigenvalues, and there is no need to calculate beyond the second or third term.

> **Note:** For more in-depth discussion of the formulas for perturbation theory up to arbitrary order, see this [Physics StackExchange post](https://physics.stackexchange.com/questions/717102/higher-order-e-g-nth-order-corrections-to-non-degenerate-time-independent).

### Example: The ramp in an infinite square well

In our first example of using perturbation theory, let us consider a 1-dimensional infinite square well of length $L$, which has the standard "box" potential:

{% math() %}
V_\mathrm{box}(x) = \begin{cases}
0, & 0 \leq x \leq L \\
\infty , & \text{otherwise}
\end{cases}
{% end %}

The Hamiltonian is therefore:

{% math() %}
H = \frac{\hat{p}^2}{2m} + V_\mathrm{box}(x) = \begin{cases}
\frac{\hat{p}^2}{2m}, & 0 \leq x \leq L \\
\infty, & \text{otherwise}
\end{cases}
{% end %}

We have previously calculated energy eigenfunctions and eigenvalues of this potential to be:

{% math() %}
\psi_{n}(x) = \sqrt{ \frac{2}{L} } \sin\left( \frac{n \pi x}{L} \right), \quad 
E_{n} = \frac{n^2 \pi^2 \hbar^2}{2mL^2}
{% end %}

Now, let us consider the modified square well with a linear potential term:

{% math() %}
H = \frac{p^2}{2m} + V_\mathrm{box} + \alpha x
{% end %}

Where $\alpha \ll 1$ is some small constant. We want to find the first-order energy shift caused by this potential (which we may imaginatively call a "ramp potential" since it does look like (and act like) a ramp). Applying the formula for the first-order energy shift, we obtain:

{% math() %}
\begin{align*}
\Delta E_{n}^{(1)} &= \langle \varphi_n^{(0)}| \Delta \hat{H} |\varphi_{n}^{(0)}\rangle \\
&= \int_{0}^L \psi_{n}(x) \alpha x \psi_{n}(x) dx \\
&= \frac{2 \alpha}{L} \int_{0}^L x \sin^2\left( \frac{n\pi x}{L} \right) dx \\
&= \frac{2\alpha}{L}\left[ \int_{0}^L \frac{x}{2} dx - \cancel{ \int_{0}^L \frac{\cos(2n\pi x / L)}{2}dx }^0\right] \\
&= \frac{\alpha L}{2}
\end{align*}
{% end %}

Where we applied the identity $\sin^2 x = \frac{1}{2} - \frac{\cos(2x)}{2}$ to split the integral into two simpler integrals. The result tells us that we would observe a first-order energy shift of $\Delta E = \alpha L/2$ upon applying the ramp potential. This makes sense: if the ramp potential is a positive potential (for $\alpha > 0$) the particle is pushed "up" by the ramp and has increased potential energy, while if the ramp potential is a negative potential (for $\alpha < 0$) the particle falls "down" the ramp and has less potential energy.

### Example 2: The quantum pendulum

The quantum pendulum is a simple model of a nonlinear harmonic oscillator and a classical problem in perturbation theory. Due to its nonlinearity, it behaves differently from the otherwise-similar quantum harmonic oscillator. The quantum pendulum is described by a Hamiltonian of the form:

{% math() %}
\hat{H} = \frac{\hat{L}_{z}^2}{2 m a^2} -\lambda \cos \phi
{% end %}

Where $m$ is the mass of the pendulum, while $a$ and $\lambda$ are two constants (with units of length and energy respectively), and it is assumed that $\lambda$ is small such that we can use perturbation theory. The first part of the Hamiltonian is the free Hamiltonian $H_0 = \frac{\hat{L}_{z}^2}{2ma^2}$, which describes a quantum rigid rotor (a rigid rotor is like a spinning top). The Schrödinger equation for the rigid rotor is:

{% math() %}
\hat{H}_{0}|\psi_{n}\rangle = \frac{\hat{L}_{z}^2}{2ma^2} |\psi_{n}\rangle = E_{n} |\psi_{n}\rangle
{% end %}

It is straightforward to solve for the rigid rotor's eigenstates and energy eigenvalues, since we already know the eigenvalues of $\hat{L}_{z}$, which are simply $n\hbar$ for integer $n$ (we use $n$ instead of the typical $m_l$ for notational clarity). Therefore, the eigenvalues of $\hat L_z^2$ are $n^2\hbar^2$ and:

{% math() %}
\frac{\hat{L}_{z}^2}{2ma^2}|\psi_{n}\rangle = \frac{\hbar^2 n^2}{2ma^2}|\psi_{n}\rangle = E |\psi_{n}\rangle
{% end %}

From which we can easily "read off" the energy eigenvalues as:

{% math() %}
E_{n} = \frac{\hbar^2 n^2}{2ma^2}
{% end %}

Meanwhile, the eigenstates can be obtained if we write $L_z^2 = \hbar^2 \frac{\partial^2}{\partial \phi^2}$ in explicit form and solve the eigenvalue equation $L_z^2 \psi = n^2 \hbar^2 \psi$. This gives us eigenfunctions in the form $\psi = A e^{i n \phi}$, upon which the normalization constant can be straightforwardly calculated:

{% math() %}
\int_{0}^{2\pi} |\psi(\phi)|^2 d\phi = 2\pi A^2 = 1 \implies A = \frac{1}{\sqrt{ 2\pi }}
{% end %}

This gives us the following set of eigenfunctions:

{% math() %}
\psi_{n}(\phi) = \frac{e^{in\phi}}{\sqrt{ 2\pi }}, \quad n = 0, 1, 2, 3, \dots
{% end %}

First, let's find the first-order correction to the energy eigenvalues, so we will use the first-order perturbation theory formula:

{% math() %}
\Delta E_{n}^{(1)} = \langle \varphi_n^{(0)}| \Delta \hat{H} |\varphi_{n}^{(0)}\rangle
{% end %}

Here, the perturbation is $\Delta \hat{H} = - \lambda\cos \phi$. Expanding the inner product (which, for our continuous eigenfunctions becomes an integral) therefore gives us:

{% math() %}
\Delta E_{n}^{(1)} = -\lambda \int_{0}^{2\pi} \frac{e^{-in\phi}}{\sqrt{ 2\pi }} \cos \phi \frac{e^{in\phi}}{\sqrt{ 2\pi }} d\phi = -\frac{\lambda}{2\pi} \int_{0}^{2\pi} \cos \phi d\phi = 0
{% end %}

We thus find that the first-order correction to the energy eigenvalues are zero. The lack of a first-order correction to the energy, however, doesn't mean the perturbation has *no effect*. Rather, it suggests that we need to go to second-order. The second-order corrections to the energy eigenvalues are given by:

{% math() %}
\Delta E_n^{(2)} = \sum_{m\,(m \neq n)} \frac{|\langle \varphi_m^{(0)}|\Delta\hat H |\varphi_{n}^{(0)}\rangle|^2}{\left(\small E_{n}^{(0)} - E_{m}^{(0)}\right)}
{% end %}

Substituting in $\Delta \hat H = -\lambda \cos \phi$ and expanding the inner products, we have:

{% math() %}
\begin{align*}
\Delta E_{n}^{(2)} &= \sum_{m\,(m \neq n)} \frac{1}{\small E_{n}^{(0)} - E_{m}^{(0)}}
\left|(-\lambda)\int_{0}^{2\pi} \psi_{m}(x) \cos \phi \psi_{n}(x) d\phi \right|^2 \\
&= \sum_{m\,(m \neq n)} \frac{\lambda^2}{\small E_{n}^{(0)} - E_{m}^{(0)}} \left| \frac{1}{2\pi} \int_{0}^{2\pi} \cos \phi e^{i(n - m)\phi} d\phi \right|^2
\end{align*}
{% end %}

We will now use the following identity:

{% math() %}
\frac{1}{\pi}\int_{0}^{2\pi} \cos \phi e^{i(n - m)\phi} d\phi = \delta_{n, 1-m} + \delta_{n, -(1+m)}
{% end %}

Where $\delta_{nm}$ is the Kronecker delta, and has a value of zero unless $n = m$ (in which case it equals one). Hence, we have:

{% math() %}
\Delta E_{n}^{(2)} = \frac{\lambda^2}{4}\sum_{m\,(m \neq n)} \frac{\left|\delta_{n, 1-m} + \delta_{n, -(1+m)}\right|^2}{\small E_{n}^{(0)} - E_{m}^{(0)}}
{% end %}

This allows us to collapse the infinite sum over $m$ because all of its terms are zero except for the cases where $\delta_{n, 1-m}$ and/or $\delta_{n, -(1+m)}$ are nonzero, which occur (respectively) when $n = 1 - m$ and when $n = -(1 + m)$. This gives us three possibilities, where we can rule out one of them easily:

1. $n = 1-m$ is individually satisfied.
2. $n = -(1 + m)$ is individually satisfied.
3. *both* of the above are satisfied at the same time (this turns out to be impossible because $1 - m = -(1 + m)$ is an equation with no solutions for $m$).

Hence, we need now only examine the first and second possibilities. In the first case, we can rearrange $n = 1-m$ into $m = 1 - n$. Therefore:

{% math() %}
E_{n}^{(0)} - E_{m}^{(0)} = E_{n} - E_{1-n} = \frac{\hbar^2 n^2}{2ma^2} - \frac{\hbar^2 (1 - n)^2}{2ma^2} = \frac{\hbar^2}{2ma^2}(2n - 1)
{% end %}

In the second case, where $n = -(1 + m)$, we have $n = -1 - m$ hence $m = -1 - n = -(1 + n)$:

{% math() %}
E_{n}^{(0)} - E_{m}^{(0)} = E_{n} - E_{-(1 + n)} = \frac{\hbar^2 n^2}{2ma^2} - \frac{\hbar^2 (1 + n)^2}{2ma^2} = -\frac{\hbar^2}{2ma^2}(2n + 1)
{% end %}

The formerly infinite sum therefore collapses into two terms (with respective values of $E_{n}^{(0)} - E_{m}^{(0)}$ as given above) giving us:

{% math() %}
\begin{align*}
\Delta E_{n}^{(2)} &= \frac{\lambda^2}{4} \left( \frac{1}{\hbar^2(2n - 1) / 2 m a^2} - \frac{1}{\hbar^2(2n + 1) / 2 m a^2} \right) \\
&= \frac{ma^2 \lambda^2}{2\hbar^2} \left( \frac{1}{2n-1} - \frac{1}{2n+1} \right) \\
&= \frac{ma^2 \lambda^2}{\hbar^2(4n^2 - 1)}
\end{align*}
{% end %}

Unlike the first-order correction, the second-order correction is *decidedly nonzero*. In addition, it is always positive *except* for the ground state (where it is negative), meaning that it effectively *decreases* the ground-state energy of the particle and *increases* the energy of all excited states. This has interesting implications, since a lower (as in *more negative*) ground state energy generally means that a particle is more tightly bound to a potential. Indeed, an important application of the quantum pendulum model is to describe the **Josephson effect** in Josephson junctions, a class of superconducting circuits whose operating principle is based on electron tunneling through a gap between two superconductors.

### Example 3: The quartic harmonic oscillator

Lastly, we will consider the quartic harmonic oscillator, which is a nonlinear modification of the quantum harmonic oscillator with the following potential:

{% math() %}
U_\mathrm{quartic} = \frac{1}{2} m \omega^2 x^2 - \frac{\lambda^4}{4!} x^4
{% end %}

Where $4! = 4 \cdot 3 \cdot 2 \cdot 1 = 24$ and $\lambda$ is a constant that is much smaller than 1. It corresponds to the following Hamiltonian:

{% math() %}
\hat{H} = \underbrace{ \frac{\hat{p}^2}{2m} + \frac{1}{2}m \omega^2 x^2 }_{ \hat{H}_{0} } + \underbrace{ \frac{-\lambda}{4!} x^4 }_{ \Delta \hat{H} }
{% end %}

This is a toy model frequently used in quantum field theory; in that context, it is known as the *quartic theory* and is a simple model for interacting particles with no spin (and a precursor to the mathematical description of the [Higgs field](https://en.wikipedia.org/wiki/Higgs_field)). It also has an interesting link to our previous example of the quantum pendulum: the quartic potential is effectively (up to some constants) the pendulum potential Taylor-expanded to 4th-order, since:

{% math() %}
\Delta \hat{H} = -\lambda \cos \phi = -\lambda + \frac{\lambda}{2!} - \frac{\lambda}{4!} + \dots
{% end %}

We want to compute the first-order correction to the energy eigenvalues for the ground state. To start off, the zeroeth-order energy eigenvalues are simply those of the quantum harmonic oscillator:

{% math() %}
E_{n}^{(0)} = \left( n + \frac{1}{2} \right)\hbar \omega
{% end %}

Hence, the ground state energy (with $n = 0$) is simply:

{% math() %}
E_0^{(0)} = \frac{1}{2} \hbar \omega
{% end %}

Now, we will compute the first-order energy shift. Recall that the ground state wavefunction of the quantum harmonic oscillator is given by:

{% math() %}
\psi_0(x) = \left(\dfrac{m\omega}{\pi \hbar}\right)^{1/4} e^{-m\omega x^2 / (2\hbar)}
{% end %}

Therefore, the first-order energy shift is given by:

{% math() %}
\begin{align*}
\Delta E_{0}^{(1)} &= \langle \psi_{0}^{(0)}|\Delta \hat{H} |\psi_{0}^{(0)}\rangle \\
&= \int_{-\infty}^{\infty} \psi_{0}(x) \frac{-\lambda}{4!} x^4 \psi_{0}(x) dx \\
&= \frac{\lambda}{24} \left( \frac{m\omega}{\pi \hbar} \right)^{1/2} \int_{-\infty}^\infty x^4 e^{-m\omega x^2 / \hbar} dx
\end{align*}
{% end %}

Now, we make use of the integral identity:

{% math() %}
\int_{-\infty}^\infty x^{2n} e^{-ax^2} dx = \sqrt{ \frac{\pi}{a} } \frac{(2n - 1)!!}{(2a)^n}
{% end %}

Where $!!$ denotes the double factorial. In our case, letting $n = 2$ and $a = m\omega/\hbar$ we would thus get:

{% math() %}
\Delta E_{0}^{(1)} = \frac{\hbar^2 \lambda}{32 m^2 \omega^2}
{% end %}

This result is particularly interesting because it is a result that depends on the mass $m$ of the particle. In fact, the ground-state energy shift due to the quartic term is actually *inversely-proportional* to the mass! This tells us that lighter particles "feel" the quartic potential more strongly, even though the mass of the particle doesn't appear in the quartic potential itself. Additionally, the correction to the ground-state energy is *positive*, meaning that the particle becomes less tightly bound as a result of the quartic potential. Hence, while a "toy model", the quartic harmonic oscillator is still an important model to study, and even serves as simplified (0+1)-dimensional version of the [Higgs mechanism](https://en.wikipedia.org/wiki/Spontaneous_symmetry_breaking#Sombrero_potential) in particle physics.

Non-degenerate perturbation theory works as long as we are dealing with non-degenerate states. Unfortunately, most quantum systems exhibit some amount of degeneracy. The hydrogen atom, for instance, contains $n^2$ or $2n^2$ (depending on whether you count spin) degenerate states for the $n$-th energy level. In the case of $n = 2$ (the first excited state of hydrogen) this means we have 4 (or 8, if you count spin) degenerate states!

The problem with degenerate eigenstates of the Hamiltonian in perturbation theory arises due to the fact that such eigenstates *by definition* share the same energy. Recall that previously, we noted that the first-order correction to the eigenstates are given by:

{% math() %}
|\varphi_n^{(1)}\rangle = \sum_{m\,(m \neq n)} \frac{\langle \varphi_m^{(0)}|\hat W |\varphi_{n}^{(0)}\rangle}{\left(\small E_{n}^{(0)} - E_{m}^{(0)}\right)}|\varphi_m^{(0)}\rangle
{% end %}

In degenerate systems, $E_n^{(0)} = E_m^{(0)}$, so we have $E_n^{(0)} - E_m^{(0)} = 0$. This gives us an undefined value of $\frac{1}{0}$. Clearly, this is not a physical solution! Hence, we must turn to **degenerate perturbation theory**, a version of stationary perturbation theory that specifically applies to degenerate states.

The trick to making degenerate states work in perturbation theory is to perform a *change of basis* into a new basis. In linear algebra, this process is known as **diagonalization**. To start with, assume that we have a set of $N$ degenerate eigenstates $\{|\varphi_{1}\rangle, |\varphi_{2}\rangle, \dots, |\varphi_{i}\rangle, \dots, |\varphi_{N}\rangle\}$. The fact that they are **all degenerate** is essential here! We now compute the following matrix $H_{ij}$, where:

{% math() %}
H_{ij} = \langle \varphi_{i} | \Delta \hat{H} | \varphi_{j} \rangle
{% end %}

If we were to write it out explicitly in matrix form, we'd have:

{% math() %}
H_{ij} = \begin{pmatrix}
\langle \varphi_{1} | \Delta \hat{H} | \varphi_{1} \rangle & \langle \varphi_{1} | \Delta \hat{H} | \varphi_{2} \rangle & \langle \varphi_{1} | \Delta \hat{H} | \varphi_{3} \rangle & \dots & \langle \varphi_{1} | \Delta \hat{H} | \varphi_{N} \rangle \\
\langle \varphi_{2} | \Delta \hat{H} | \varphi_{1} \rangle & \langle \varphi_{2} | \Delta \hat{H} | \varphi_{2} \rangle & \langle \varphi_{2} | \Delta \hat{H} | \varphi_{3} \rangle & \dots & \langle \varphi_{2} | \Delta \hat{H} | \varphi_{N} \rangle \\
\vdots & \vdots & \vdots & \vdots & \vdots \\
\langle \varphi_{i} | \Delta \hat{H} | \varphi_{1} \rangle & \langle \varphi_{i} | \Delta \hat{H} | \varphi_{2} \rangle & \langle \varphi_{i} | \Delta \hat{H} | \varphi_{3} \rangle & \dots & \langle \varphi_{i} | \Delta \hat{H} | \varphi_{N} \rangle \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
\langle \varphi_{N} | \Delta \hat{H} | \varphi_{1} \rangle & \langle \varphi_{N} | \Delta \hat{H} | \varphi_{2} \rangle & \langle \varphi_{N} | \Delta \hat{H} | \varphi_{3} \rangle & \dots & \langle \varphi_{N} | \Delta \hat{H} | \varphi_{N} \rangle
\end{pmatrix}
{% end %}

While computing all of these inner products may *look* scary, we often don't need to compute all of them due to orthogonality relations between different states. To find the corrections to the eigenenergies, we must diagonalize this matrix. We can do this by solving the following **eigenvalue equation**:

{% math() %}
\det(H_{ij} - \varepsilon \delta_{ij}) = 0
{% end %}

Where $\delta_{ij}$ is the identity matrix. Our aim is to solve for $\varepsilon$, the eigenvalues of $H_{ij}$. Once we do so, we get a new, diagonalized matrix in the form:

{% math() %}
H_{ij}' = \begin{pmatrix}
\varepsilon_{1} &  &  &  &  &  \\
 & \varepsilon_{2} &  &  &  &  \\
 &  & \ddots & & &  \\
 &  &  & \varepsilon_{i} &  &  \\
 & & & & \ddots &  \\
 &  &  &  & & \varepsilon_{N - 1} \\
 &  &  &  & &  & \varepsilon_{N}
\end{pmatrix}, \quad H_{ij}' = 0 \text{ if } i \neq j
{% end %}

(By definition all the components of $H_{ij}'$ are zero except on the diagonal.) Here, $\varepsilon_i$ is the $i$-th eigenvalue of $H_{ij}$ and there are $N$ eigenvalues total. They physically correspond to the energy eigenvalues of the perturbation $\Delta \hat H$.

> **Note:** while there will always be $N$ eigenvalues, some of these may be repeated eigenvalues or zero. If you see these, don't freak out!

The corresponding **eigenvectors** of $H_{ij}$ are the basis vectors for the new basis, and are the solutions of the following equation:

{% math() %}
(H_{ij} - \varepsilon \delta_{ij}) |\phi\rangle = 0
{% end %}

We therefore now have a set of eigenvalues and a set of eigenvectors at our disposal:

{% math() %}
\{\varepsilon_{1}, \varepsilon_{2}, \varepsilon_{3}, \dots, \varepsilon_{N} \}, \quad
\{|\phi_{1}\rangle, |\phi_{2}\rangle, |\phi_{3}\rangle, \dots, |\phi_{N}\rangle \}
{% end %}

Now is the key part: the **energy corrections (shifts)** $\Delta E_i$ to the $i$-th *eigenstate* are **exactly equal** to the $i$-th *eigenvalue* of $H_{ij}$! That is, we have:

{% math() %}
\Delta E_{i} = \varepsilon_{i}
{% end %}

Meanwhile, the **corrections to the eigenstates** $|\tilde{\varphi}_{i}\rangle$ are:

{% math() %}
|\tilde{\varphi}_{i}\rangle = \sum_{j = 1}^N c_{ij} |\varphi_{j}\rangle
{% end %}

Where $c_{ij}$ is the $j$-th component of eigenvector $|\phi_i\rangle$. We therefore observe that the new eigenstates have *mixed* the original degenerate eigenstates into new eigenstates. This "lifts" the degeneracy (a fancy term for essentially saying that the degenerate eigenstates have been made no longer degenerate) and allows the eigenstates of the Hamiltonian to be well-defined, at the cost of requiring the mixing of the original eigenstates.

## Applications of stationary perturbation theory

Having solved a few toy models, we now move on to applications of stationary (time-independent) perturbation theory for real quantum systems. We will develop the techniques to analyze complicated systems — and, in the process, go through some of the most famous calculations in the history of quantum mechanics.

### The Zeeman effect

We will start with a very famous application of perturbation theory: calculating the energy splitting of an atom within a magnetic field. We observe experimentally that when an atom is subjected to a magnetic field, the wavelengths of light it emits change. Quantum mechanics provides an explanation for why.

To analyze the Zeeman effect, we must go beyond the basic Hamiltonian $\hat H = \dfrac{\hat p^2}{2m} + V(\mathbf{r})$, which has been the staple of all our calculations so far. We need to add a new term to the Hamiltonian that incorporates the effect of the magnetic field, which we denote as $\Delta \hat H_\mathrm{Zeeman}$ and which we call the *Zeeman term*, leading to the following Hamiltonian:

{% math() %}
\hat{H} = \frac{\hat{\mathbf{p}}^2}{2\mu} + V_\mathrm{coulomb}(\mathbf{r}) + \Delta \hat H_\mathrm{Zeeman}
{% end %}

Where $\mu$ is the reduced mass. For a uniform magnetic field the Zeeman term $\Delta \hat H_\mathrm{Zeeman}$ is proportional to the magnetic moment operator $\boldsymbol{\mu}_{M}$ and linear in the field, where:

{% math() %}
\Delta \hat H_\mathrm{Zeeman} = -\boldsymbol{\mu}_{M} \cdot \mathbf{B}, \quad \boldsymbol{\mu}_{M} = -g\frac{q}{2m_{q}} \hat{\mathbf{L}}
{% end %}

Where $\hat{\mathbf{L}}$ is the angular momentum operator, and $g$ is a constant known as the **g-factor** that describes the ratio between the quantum magnetic dipole moment and the classical magnetic dipole moment. Here, we use $m_q$ to denote the mass of the charged particle we are studying in question (in atoms, the dominant contribution is from electrons, but the nuclei can also play a part in the Zeeman effect). Therefore, the expanded version of the Zeeman term is given by:

{% math() %}
\Delta \hat H_\mathrm{Zeeman} = g\frac{q}{2m_{q}} \hat{\mathbf{L}} \cdot \mathbf{B}
{% end %}

Up to this point, we have kept our treatment very general and have not assumed a fixed value of the g-factor or the charge of the particle. This is important because an advanced treatment of the Zeeman effect would also take into account the *nuclear spin angular momentum*, which must take into account (among other things) the different charge and mass of protons compared to electrons. However, in the case of electrons, we have, $m_q = m_e$ (where $m_e$ is the electron mass), and $q = -e$ (where $e$ is the elementary charge constant), giving us:

{% math() %}
\Delta \hat H_\mathrm{Zeeman} = -\frac{ge}{2m_{e}} \hat{\mathbf{L}} \cdot \mathbf{B}
{% end %}

It is common to express the above in terms of the so-called **Bohr magneton** $\mu_B$ given by:

{% math() %}
\mu_{B} = \frac{e\hbar}{2m_{e}} \approx \pu{9.274 * 10^{−24} J/T}
{% end %}

Where $m_e$ is the electron mass. Hence, our rewritten Zeeman Hamiltonian (without taking into account spin) is given by:

{% math() %}
\Delta \hat H_\mathrm{Zeeman} = -\frac{g\mu_{B}}{\hbar} \hat{\mathbf{L}} \cdot \mathbf{B}
{% end %}

#### The weak Zeeman effect

If the magnetic field is relatively weak, we may treat the Zeeman term in the Hamiltonian as a perturbation. Therefore, we can use the methods of perturbation theory very straightforwardly. We will first compute the first-order correction with our favorite perturbation theory formula, with our eigenstates being those of the hydrogen atom (that is $|n, \ell, m\rangle$ where we are *not* including spin yet):

{% math() %}
\begin{align*}
\Delta E_{n}^{(1)} &= \langle \varphi_n^{(0)}| \Delta \hat{H}_\mathrm{Zeeman} |\varphi_{n}^{(0)}\rangle \\
&= -\frac{g\mu_{B}}{\hbar}\langle n, \ell, m|(\hat{\mathbf{L}} \cdot \mathbf{B}) |n, \ell, m\rangle
\end{align*}
{% end %}

We will assume a uniform magnetic field $|\mathbf{B}| = B_0 \hat{z}$, hence the component of $\hat{\mathbf{L}}$ that is aligned in the same direction as the field would be $\hat L_z$. As we know eigenvalues of $\hat L_z$ are $m\hbar$, reducing the above to:

{% math() %}
\Delta E_{n}^{(1)} = -\frac{g\mu_{B} B_{0}}{\hbar}(m\hbar) \langle n, \ell, m|n, \ell, m\rangle
{% end %}

Now, since the eigenstates of the hydrogen atom are normalized (that is, $\langle n, \ell, m|n, \ell, m\rangle = 1$), the bra-ket is simply one, giving us:

{% math() %}
\begin{align*}
\Delta E_{n}^{(1)} &= -\frac{g\mu_{B} B_{0}}{\hbar}(m\hbar) = -gm \mu_{B}B_{0} \\ n &= 1, 2, \dots, \\ \ell &= 0, 1, 2, \dots, (n-1), \\ m &= -\ell, -(\ell + 1), \dots, (\ell - 1), \ell
\end{align*}
{% end %}

(Note that $g = 1$ for the weak Zeeman effect as it depends only on orbital angular momentum and not on spin.) Since the energy shift is explicitly dependent on $m$, it is zero for states where $\ell = 0$ and also zero for any states where $m = 0$. However, where $m \neq 0$ the Zeeman effect predicts that the existence of _additional_ energy levels separated by a constant value of $g\mu_B B_0$. These additional energy levels correspond with new eigenstates parametrized by $\ell, m$. The total energy of each state now depends on $n$, $\ell$, and $m$, so instead of $E_n$, we write the energy levels as $E_{n \ell m}$, and they are given by:

{% math() %}
\begin{align*}
E_{n\ell m} &= E_{n}^{(0)} + \Delta E_{n}^{(1)} \\
&= -\pu{13.6 eV} \cdot \frac{Z^2}{n^2} - m \mu_{B} B_{0}
\end{align*}
{% end %}

Hence we say that the Zeeman effect *lifts the degeneracy* of the energy levels, since previously degenerate states have now become non-degenerate. In plainer language, the states that previously shared the same energy now have *distinct energies* that allow us to easily tell them apart. This will be a continuing theme within our exploration of quantum systems: the application of an external electric or magnetic field lifts the degeneracy of the eigenstates and allows new transitions to become possible (which manifest as new spectral lines within the hydrogen spectrum).

> **Note:** The weak Zeeman effect holds for most "everyday" magnetic fields ($B_0 < \pu{1 T}$). In comparison, Earth's magnetic field has an average strength of $\approx \pu{30-60 \mu T}$, which is 100,000 times weaker. Some exceptions include extremely powerful laboratory magnets and astrophysical magnetic fields (e.g. in stars, pulsars, quasars, etc.), where the weak Zeeman effect is replaced by the *strong Zeeman effect*.

#### The anomalous Zeeman effect

It is all well and good using our modified Hamiltonian to describe the Zeeman effect, but if we do out our calculation, we'll find that its predicted energy levels actually deviate a significant amount from experimental values. The discrepancy between experimental observations of Zeeman spectral splitting and our theoretical predictions using our basic formula is known as the **anomalous Zeeman effect**. An explanation of the anomalous Zeeman effect requires us to consider the effects of **electron spin**, which we have previously neglected. This means that we must modify the Zeeman term in the Hamiltonian as follows:

{% math() %}
\Delta \hat H_\mathrm{Zeeman} \to \frac{q}{2m_{e}}(g_{l}\hat{\mathbf{L}} \cdot \mathbf{B} + g_{s}\hat{\mathbf{L}} \cdot \hat{\mathbf{S}})
{% end %}

Here, $g_l = 1$ and $g_s = 2.0023193$ are the electron orbital g-factor and electron spin g-factor respectively (it is common to simply write $g_s = 2$ as an approximation). The $\hat{\mathbf{L}} \cdot \hat{\mathbf{S}}$ term is known as the **LS coupling** or **spin-orbital coupling** term, and comes from the interaction between the electron's spin and the magnetic field of the nucleus in the electron's rest frame. The nucleus is (to a very good approximation) at rest within the atom's rest frame, and hence possesses no magnetic field in that frame; however, in the *electron's* rest frame the nucleus appears to be moving (an effect of relativity) and hence it has a magnetic field. We will later see LS coupling reappear in the explanation of fine structure, which are tiny corrections to the energy levels of the hydrogen atom that cannot be explained within spin or relativity.

But back to calculating the anomalous Zeeman effect. First, note that it is common to write the Zeeman term in the Hamiltonian (including the spin contribution) in an alternate form as:

{% math() %}
\Delta \hat{H}_{Zeeman} = g_{J}\frac{q}{2m_{e}} \hat{\mathbf{J}} \cdot \mathbf{B}
{% end %}

Where $\hat{\mathbf{J}} = \hat{\mathbf{L}} + \hat{\mathbf{S}}$ is the total angular momentum operator, $\mu$ is the reduced mass of the atom, and $g_J$ is the [Landé g-factor](https://en.wikipedia.org/wiki/Land%C3%A9_g-factor), which is defined as:

{% math() %}
\begin{align*}
g_{J} &= g_{l} \frac{j(j+1) + \ell(\ell + 1) - s(s+1)}{2j(j+1)} + g_{s} \frac{j(j+1) + s(s+1) - \ell(\ell +1)}{2j(j+1)} \\
&\approx 1 + \frac{j(j+1) + s(s + 1) - \ell(\ell + 1)}{2j(j+1)}
\end{align*}
{% end %}

Where $\ell$ is the orbital angular momentum quantum number, $s$ is the spin quantum number, $j \equiv \ell + s$ is the total angular momentum quantum number, $g_l = 1$ is the *electron orbital g-factor* and $g_s = 2.0023193 \dots \approx 2$ is the *electron spin g-factor*. If you think the formula looks horrible, early 20th-century physicists had it worse: the Landé g-factor was the painstaking result of essentially guess-and-checking based on empirically-observed data. Imagine needing to try essentially every combination of quantum numbers just to get that formula in the end!

However, given that we *do* know the formula for the g-factor the rest of the derivation is straightforward. Simply apply first-order perturbation theory to the perturbation term $\Delta \hat H_\mathrm{Zeeman}$ (but this time including spin in the hydrogen atom's eigenstates $|n, j, m_{j}, s\rangle$, and recalling that the eigenvalues of $\hat J_z$ are $m_j \hbar$ instead of $m\hbar$), which gives us:

{% math() %}
\begin{align*}
\Delta E_{n}^{(1)} &= \langle \varphi_n^{(0)}| \Delta \hat{H} |\varphi_{n}^{(0)}\rangle \\
&= -\frac{g_{J}\mu_{B}}{\hbar}\langle n, j, m_{j}, s|(\hat{\mathbf{J}} \cdot \mathbf{B}) |n, j, m_{j}, s\rangle \\
&= -\frac{g\mu_{B} B_{0}}{\hbar}(m_{j}\hbar) = -g_{J}m_{j} \mu_{B}B_{0} \\ n &= 1, 2, \dots, \\ \ell &= 0, 1, 2, \dots, (n-1), \\ 
s &= \pm \small \frac{1}{2}, \\
j &= 0, \frac{1}{2}, 1, \frac{3}{2}, \dots, \quad |\ell - s\vert \leq j \leq \ell + s, \\
m_{j} &= -j, (-j + 1), \dots, (j - 1), j
\end{align*}
{% end %}

#### The vector potential approach

Our derivation so far has followed the approach used by most introductory texts, but it turns out that there is another way to derive the Zeeman effect that is more rigorous. To start, we use the *generalized* electromagnetic Hamiltonian for a charged particle of mass $m$ and charge $q$ in an electromagnetic field (called the *Pauli Hamiltonian*, which we'll see again later):

{% math() %}
\begin{align*}
\hat{H} &= \frac{1}{2m}(\hat{\mathbf{p}} - q \hat{\mathbf{A}})^2 + q\phi \\
&= \frac{1}{2m} \left( \hat{\mathbf{p}}^2 - 2q \hat{\mathbf{p}} \cdot \mathbf{A}
 + q^2 \mathbf{A}^2 \right) + q\phi
 \end{align*}
 {% end %}

 > **Note:** Here, $m$ is just the mass of the charged particle, not the magnetic quantum number that we have previously denoted with $m$. We have also **ignored spin** here for simplicity; we'll see the more generalized treatment with spin later.

 Where $\phi$ is the **electric scalar potential** and $\mathbf{A}$ is the **magnetic vector potential** (read more on this in the [electromagnetic theory guide](@/classical-electromagnetism/index.md) if unfamiliar), and $\mathbf{B} = \nabla \times \mathbf{A}$. For reasons that we'll cover more in-depth later, we may arbitrarily chose $\mathbf{A}$ such that it is given by:

 {% math() %}
 \mathbf{A} = \frac{1}{2} \mathbf{B} \times \mathbf{r}
 = \begin{pmatrix}
 -By \\ Bx \\ 0
 \end{pmatrix}, \quad B = \|\mathbf{B}\|
 {% end %}

 > **Note:** If you don't want to wait for the explanation, this is due to a phenomenon called [gauge freedom](https://en.wikipedia.org/wiki/Gauge_freedom). Specifically, we choose the *symmetric gauge* by imposing the aforementioned gauge condition $\mathbf{A} = \frac{1}{2}\mathbf{B} \times \mathbf{r}$, in which $\mathbf{B} = \nabla \times \mathbf{A}$.

 By substituting in our vector potential, using $\hat{\mathbf{L}} = \mathbf{r} \times \hat{\mathbf{p}}$, and expanding terms, we obtain:

 {% math() %}
 \hat{H} = \frac{1}{2m} \left\{ \hat{\mathbf{p}}^2 + q\mathbf{B} \cdot  \hat{\mathbf{L}} + \frac{q^2}{4} (\mathbf{B}^2 \mathbf{r}^2 - (\mathbf{B} \cdot \mathbf{r})^2) \right\}
 {% end %}

 Where the second term is called the **diamagnetic term** and the third is the **paramagnetic term**; each successive term is weaker than the last. If we turn off the magnetic field ($\mathbf{B} = 0$) and use the Coulomb potential $\phi = \dfrac{Q}{4\pi \varepsilon_0 r}$ with $Q = Ze$, we recover the Hamiltonian of the hydrogen atom. However, when $\mathbf{B}$ is nonzero, we observe the splitting of energy levels, which is what we find in the Zeeman effect. Indeed, if we ignore the paramagnetic term we *exactly* reproduce the weak Zeeman effect Hamiltonian that we have been using previously! (As stated previously, it does not cover the anomalous Zeeman effect since we have ignored spin, but a more detailed derivation would also incorporate effect of spin.)

 #### The strong Zeeman effect

 For most cases, our formulas for the Zeeman effect and anomalous Zeeman effect work very well, but they fail in the case of strong magnetic fields. In such cases, the Zeeman term can *no longer* be treated as a small perturbation to the Hamiltonian, and becomes non-perturbative. Instead, we must treat it on equal footing with the rest of the Hamiltonian terms, giving us a Hamiltonian in the form:

 {% math() %}
 \begin{align*}
 \hat{H} &= \frac{\hat{\mathbf{p}}^2}{2\mu} + V_\mathrm{Coulomb} + \hat H_\mathrm{Zeeman} + \dots \\
 &= \frac{\hat{\mathbf{p}}^2}{2\mu} + V_\mathrm{Coulomb} + g_{J}\frac{q}{2m_{e}} \hat{\mathbf{J}} \cdot \mathbf{B} + \dots
 \end{align*}
 {% end %}

 Where the terms after the Zeeman Hamiltonian represent terms that are much smaller than the Zeeman term. This will be significant once we get to the calculation of the **fine structure of hydrogen**, where when the Zeeman energy splitting is comparable to (or greater than) the fine-structure energy splitting, the fine-structure contribution will need to be treated as a *perturbation* "on top of" the Zeeman effect rather than the other way around. Solving this Hamiltonian to find the energy shifts shall be left as an exercise for the reader.

### The Stark effect

If magnetic fields can split energy levels, can an electric field do so too? The answer is yes! This is known as the **Stark effect**. It is weaker than the Zeeman effect, so we will derive both the first and second-order energy corrections using perturbation theory.

The Stark effect is conceptually extremely similar to the Zeeman effect, except we swap the magnetic field with the electric field. To start, we assume a uniform electric field in the form $\vec{\mathcal{E}} = \mathcal{E}_0 \hat z$, where $\mathcal{E}_0$ is the electric field strength. Note that we call the field direction $z$ as a matter of convention, but the choice is technically arbitrary, because we can always rotate our coordinate system such that the electric field aligns with the $z$ axis. The Hamiltonian for the Stark effect can be expressed via the electric dipole moment operator $\boldsymbol{\mu}_E = q\mathbf{r}$ and the electric field as:

{% math() %}
\Delta \hat{H}_\mathrm{Stark} = -\boldsymbol{\mu}_{E} \cdot \vec{\mathcal{E}} = -q\mathbf{r} \cdot \vec{\mathcal{E}}
{% end %}

From trigonometry, $\mathbf{r} \cdot \hat z = r \cos \theta$, hence one obtains:

{% math() %}
\Delta \hat{H}_\mathrm{Stark} = e \mathcal{E}_0 r \cos \theta
{% end %}

Where we have also substituted in $q = -e$ (since the Stark effect affects electrons in an atom). We will now do the calculation of the energy shifts that occur due to the Stark effect.

#### The linear Stark effect

To start, we will calculate the energy shifts to first-order. This is known as the **linear Stark effect** as it is linear in the electric field strength ($\Delta E \sim \mathcal{E}_0$).

To first-order, we obtain:

{% math() %}
\begin{align*}
\Delta E_{n}^{(1)} &= \langle \varphi_n^{(0)}| \Delta \hat{H}_\mathrm{Stark}|\varphi_{n}^{(0)}\rangle \\
&= e \mathcal{E}_0 \langle n, \ell, m|r|n, \ell, m\rangle
\end{align*}
{% end %}

 Now, the hydrogen atom's wavefunctions satisfy:

{% math() %}
\langle n, \ell, m|\mathbf{r}|n, \ell, m\rangle = 0
{% end %}

One can find this via direct calculation, but we will give a physical argument for why this must be the case. An electric dipole moment only exists where one has an asymmetrical configuration of charge. For states with $\ell = 0$, the orbitals are spherical and therefore exhibit spherical symmetry, hence there can be no dipole moment. Meanwhile, for states with $\ell \neq 0$, the probability density of the orbitals is symmetric along the $z$ axis. Since the charge density is proportional to the probability density, there is no dipole moment either. It is only in the case of *mixed orbitals* (that is, superpositions of multiple orbitals) that the electric dipole moment is nonzero, *not* the standard orbitals!

{{ diagram(
desc="Probability density of the pure hydrogen orbitals"
src="hydrogen-orbitals-stark.jpg"
) }}

_Probability density (proportional to charge density) of the "pure" hydrogen atomic orbitals. Original author: [Henning Schomerus from Lancaster University](https://www.lancaster.ac.uk/staff/schomeru/lecturenotes/Quantum%20Mechanics/S17.html)_

Therefore, by direct application of non-degenerate perturbation theory, it would _appear_ that the first-order correction to the energies is also identically zero:

{% math() %}
\Delta E_{n}^{(1)} = 0
{% end %}

But not so fast! It would be more accurate to say that the first-order correction to the energies of **non-degenerate states** is zero. This is because we have not considered the fact that many of the eigenstates of the hydrogen atom are *degenerate*! We know that *non-degenerate perturbation theory* fails for degenerate states, hence we must now use *degenerate perturbation theory instead* (for which, it turns out, that nonzero first-order corrections *are* indeed present).

##### Using first-order degenerate perturbation theory

To start, we need to pick a set of states that we are degenerate. In the hydrogen atom, the energy levels (at least without correction terms due to fine/hyperfine structure, which we'll talk about later) are only depend on the principal quantum number $n$. (The Stark effect is not directly affected by spin.) Hence, any set of degenerate states *must share the same value of $n$*. The converse is *almost true*; states with the same value of $n$ are generally degenerate, with the exception of $n = 1$.

To make our analysis easier, we will only calculate the energy shifts for the *first excited state* (which has $n = 2$). We could in principal calculate the Stark shift for any energy level (that is, for any $n$) we choose, but the number of degenerate states grows $\sim n^2$ meaning that e.g. $n = 3$ splits into at least 9 states, $n = 4$ splits into at least 16, and (for sake of example) $n = 20$ splits into at least 400 states! That is way too many to analyze for an elementary treatment so we will start with the simplest case of $n = 2$, though we will give a general formula at the end.

##### The brute-force way to do degenerate perturbation theory

The first way we can go about solving the problem is what I call the "brute-force" approach. Basically, we proceed as follows:

1. Create a list of degenerate states for the $n$-th energy level; this will be our basis $\{|\varphi_i\rangle\}$
2. Calculate the matrix elements $H_{ij} = \langle \varphi_i|\Delta \hat H|\varphi_j\rangle$ one by one
3. Calculate the eigenvalues and eigenvectors of $H_{ij}$ to get the perturbed energy levels and perturbed eigenstates

Let's start at the first step. In the $n = 2$ energy level, the possible values of $\ell$ are $\ell = 0, 1$ and the possible values of $m$ are $m = 0, \pm 1$. Hence, the 4 states $|2, \ell, m\rangle$ are respectively:

{% math() %}
\{|\varphi_i\rangle\} = \left\{|2, 0, 0\rangle, |2, 1, 0\rangle, |2, 1, 1\rangle, |2, 1, -1\rangle \right\}
{% end %}

One can write these more explicitly as:

{% math() %}
\begin{align*}
|\varphi_{1}\rangle &= |2, 0, 0\rangle \\
|\varphi_{2}\rangle &= |2, 1, 0\rangle  \\
|\varphi_{3}\rangle &= |2, 1, 1\rangle \\
|\varphi_{4}\rangle &= |2, 1, -1\rangle
\end{align*}
{% end %}

Note that the specific ordering here is not important since the basis is orthonormal. For instance, we could've chosen $|\varphi_1\rangle$ to be $|2, 1, 0\rangle$ and $|\varphi_2\rangle$ to be $|2, 1, 1\rangle$. The important thing is to list all the degenerate states for a given energy level and make sure you don't accidentally include non-degenerate states.

Now, we compute the matrix elements $\langle \varphi_i|\Delta \hat H|\varphi_j\rangle$ where $\Delta \hat H$ is the Stark Hamiltonian. This is where things become a bit hairy! After all, if we directly substitute into the matrix we get:

{% math() %}
H_{ij} = \begin{pmatrix}
\langle \varphi_1|\Delta \hat H|\varphi_1\rangle & \langle \varphi_1|\Delta \hat H|\varphi_2\rangle & \langle \varphi_1|\Delta \hat H|\varphi_3\rangle & \langle \varphi_1|\Delta \hat H|\varphi_4\rangle \\
\langle \varphi_2|\Delta \hat H|\varphi_1\rangle & \langle \varphi_2|\Delta \hat H|\varphi_2\rangle & \langle \varphi_2|\Delta \hat H|\varphi_3\rangle & \langle \varphi_2|\Delta \hat H|\varphi_4\rangle \\
\langle \varphi_3|\Delta \hat H|\varphi_1\rangle & \langle \varphi_3|\Delta \hat H|\varphi_2\rangle & \langle \varphi_3|\Delta \hat H|\varphi_3\rangle & \langle \varphi_3|\Delta \hat H|\varphi_4\rangle \\
\langle \varphi_4|\Delta \hat H|\varphi_1\rangle & \langle \varphi_4|\Delta \hat H|\varphi_2\rangle & \langle \varphi_4|\Delta \hat H|\varphi_3\rangle & \langle \varphi_4|\Delta \hat H|\varphi_4\rangle
\end{pmatrix}
{% end %}

Now, with some patience and grit computing all of those inner products (each of which is an integral) you will find that the matrix elements are the following:

{% math() %}
H_{ij} = -3a_{0} e E_{0} \begin{pmatrix}
0 & 1 & 0 & 0 \\
1 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0
\end{pmatrix}
{% end %}

We now need to find the eigenvalues of this matrix. For starters, we don't actually have to find the eigenvalues of the entire $(4 \times 4)$ matrix, since it is zero except for the top-left "corner". This means we ultimately only need to calculate the eigenvalues of this much simpler matrix:

{% math() %}
\begin{pmatrix}
0 & 1 \\
1 & 0
\end{pmatrix}
{% end %}

The eigenvalues are $\pm 1$, which gives the (correct) energy shifts of:

{% math() %}
\Delta E_\mathrm{Stark} = \pm 3 a_{0} e E_{0} \quad (n = 2)
{% end %}

There is nothing specifically wrong with this approach; it *does work*. Unfortunately, it involves a lot of integrals to compute, because there are $n^2$ degenerate states for the $n$-th energy levels. We saw that even for the first excited state ($n = 2$) we have to get all the eigenvalues for a $(4 \times 4)$ matrix; the next excited state ($n = 3$) would involve solving for the eigenvalues of a $(9 \times 9)$ matrix! Now, I don't know about you, but I'd rather not compute that many integrals or eigenvalues! Hence, let us turn to another, more clever approach that saves us time and avoids the need to calculate so many matrix elements.

##### The clever way to do degenerate perturbation theory

The "clever" way to do degenerate perturbation theory is to rule out as many of the matrix elements as possible, until we are left with only the nonzero ones. This is generally a *much quicker method* and involves less work, but does require some reasoning, hence why I call it the "clever" approach.

This approach relies heavily on the *selection rules* of atomic transitions, which dictate which transitions are possible and which are not. We can figure out a lot of these ourselves! First of all, we know that an atomic transition between two energy levels $E_2 \to E_1$ corresponds to the release of a photon carried an energy $\Delta E = E_{2} - E_{1}$ equal to the difference between the energy levels. Unlike electrons, photons are spin-1 particles, meaning that they carry $\pm 1 \hbar$ units of angular momentum (the sign depends on their specific spin state). To conserve angular momentum, we therefore require that the initial and final states' orbital angular momentum changes by a factor of $\Delta \ell = 1$ or $\Delta \ell = -1$. That is, we obtain the selection rule $\Delta \ell = \pm 1$.

In addition, we know that the allowable values of $m$ range from zero to $\pm \ell$. By the restriction $\Delta \ell = \pm 1$, this means that the change in $m$ must therefore be zero, 1, or -1. Hence we obtain the selection rule $\Delta m = 0, \pm 1$.

Finally, since electrons are spin-1/2 particles, their spin quantum number is *always* $s = \frac{1}{2}$. Therefore the spin quantum number cannot change during a transition, so $\Delta s = 0$. (This becomes a bit more complicated once we need to consider nuclear spin, which we'll explore once we talk about hyperfine structure, but we can assume $\Delta s = 0$ to be the case for now.)

Collectively, our selection rules are therefore:

{% math() %}
\begin{cases}
\Delta \ell = \pm 1 \\
\Delta m = 0, \pm 1 \\
\Delta s = 0
\end{cases}
{% end %}

> **Note:** These are known as the *electric dipole transition selection rules* (or E1 selection rules for short) and are not simply the case for the Stark effect, but for all transitions mediated by an electric field!

These selection rules heavily restrict the types of transitions possible in the Stark effect. In our case, it means that each transition between the $n = 2$ states must involve one state with $\ell = 1$ and one state with $\ell = 0$ to satisfy the first selection rule. Hence, we know that the nonzero matrix elements *must* have $|\varphi_{1}\rangle = |2, 0, 0\rangle$ as one of the states since it is the only state with $n = 2$ that also has $\ell = 0$. Therefore, we only need to consider matrix elements of the forms $\langle \varphi_1|\Delta \hat H|\varphi_i\rangle$ or $\langle \varphi_i|\Delta \hat H|\varphi_1\rangle$. Indeed, since these are symmetric we actually only need to explicitly calculate *one* of the two forms (the other matrix element would be equal), leaving us with just 4 matrix elements in total out of the original 16. Quite an improvement!

Now, the second selection rule is less immediately helpful because all transitions to/from $|2, 0, 0\rangle$ for the $n = 2$ states satisfy it. However, the Stark effect Hamiltonian is azimuthally-symmetric. This is clear from the form of the Hamiltonian, which explicitly depends on the $r$ and $\theta$ coordinates, but *doesn't* depend on the $\phi$ coordinate, hence a rotation about the $z$ axis has no effect on the Hamiltonian. Therefore, the $z$-component of the angular component *must be conserved*. Since $L_z = m\hbar$, it is clear that if $\Delta L_z = 0$, then $\Delta m = 0$ must be true as well! Therefore, our selection rules become additionally restricted to the following:

{% math() %}
\begin{cases}
\Delta \ell = \pm 1 \\
\Delta m = 0 \\
\Delta s = 0
\end{cases}
{% end %}

There is only **one** transition involving the $|2, 0, 0\rangle$ state that *also* satisfies $\Delta m = 0$, and it is the transition between the $|2, 0, 0\rangle$ and $|2,1, 0\rangle$ states. Hence, this is the only matrix element we'll need to calculate! By using this "clever" approach, we have drastically cut down the number of matrix elements we need to calculate! Upon doing the calculation, we have:

{% math() %}
\begin{align*}
\langle 2, 0, 0|\Delta \hat{H} |2, 1, 0\rangle &= e\mathcal{E}_{0} \langle \varphi_{1}|r \cos \theta|\varphi_{2}\rangle \\
&= e\mathcal{E}_{0} \int_{0}^\infty R_{20}(r)R_{21}(r) r^2 dr \int_{0}^{2\pi} \int_{0}^\pi Y^0_{0}(\theta, \phi)^* Y^0_{1}(\theta, \phi) \cos \theta(\sin \theta d \theta d\phi) \\
&= -3a_{0}e \mathcal{E}_{0}
\end{align*}
{% end %}

And likewise (due to symmetry):

{% math() %}
\langle 2,1, 0|\Delta \hat{H}|2, 0, 0\rangle = \langle 2, 0, 0|\Delta \hat{H} |2, 1, 0\rangle = -3a_{0}e \mathcal{E}_{0}
{% end %}

The $H_{ij}$ matrix is therefore zero for all terms except for the $H_{12}$ and $H_{21}$ elements, which correspond to the two above transitions. Therefore, we have:

{% math() %}
H_{ij} = -3a_{0} e E_{0} \begin{pmatrix}
0 & 1 & 0 & 0 \\
1 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0
\end{pmatrix}
{% end %}

This is the same matrix that we got earlier, and we've already calculated what its eigenvalues are: they are respectively $\pm 3 a_{0}eE_{0}$, hence the energy shifts due to the linear Stark effect are:

{% math() %}
\Delta E_\mathrm{Stark} = \pm 3 a_{0}eE_{0}
{% end %}

The resulting (normalized) eigenvectors are:

{% math() %}
|\phi_{1}\rangle = \frac{1}{\sqrt{ 2 }} \begin{pmatrix}
-1 \\ 1
\end{pmatrix}, \quad
|\phi_{1}\rangle = \frac{1}{\sqrt{ 2 }} \begin{pmatrix}
1 \\ 1
\end{pmatrix}
{% end %}

(The first corresponds to the eigenvalue of $-3a_0 eE_0$ and the second corresponds to the eigenvalue of $+3 a_0 eE_0$). We can now construct the perturbed eigenstates $|\tilde{\varphi}_{i}\rangle$, which are given by:

{% math() %}
|\tilde{\varphi}_{i}\rangle = \sum_{j = 1}^N \phi_{ij} |\varphi_{j}\rangle
{% end %}

Here, we have $N = 2$ (technically $N = 4$ but there are only two nonzero eigenvectors) and $\phi_{ij}$ denotes the $j$-th component of the eigenvector $|\phi_i\rangle$, which are (respectively):

{% math() %}
\phi_{ij} = \frac{1}{\sqrt{ 2 }} \begin{pmatrix}
-1 & 1 \\
1 & 1
\end{pmatrix}
{% end %}

Therefore, the perturbed eigenstates are:

{% math() %}
\begin{align*}
|\tilde{\varphi}_{1}\rangle &= \frac{1}{\sqrt{ 2 }}(|2, 1, 0\rangle - |2, 0, 0\rangle) \\
|\tilde{\varphi}_{2}\rangle &= \frac{1}{\sqrt{ 2 }}(|2, 0, 0\rangle + |2, 1, 0\rangle)
\end{align*}
{% end %}

Notice how the Stark effect has given us *mixed orbitals*. These orbitals, unlike the regular atomic orbitals, have asymmetric probability densities (and therefore asymmetric charge distributions) which gives rise to a nonzero electric dipole moment, resulting in the splitting of the spectral lines!

##### Summary of degenerate perturbation theory in the Stark effect

In the **general case** for arbitrary $n$, the linear Stark effect predicts that the $n$-th state will split into $2n - 1$ distinct energy levels. A diagram of (some of) the Stark shifts is shown below:

![Image of energy levels splitting due to the Stark effect](https://upload.wikimedia.org/wikipedia/commons/4/44/Stark_splitting.png)

_Source: [Wikipedia](https://en.wikipedia.org/wiki/File:Stark_splitting.png)_

The Stark effect has applications [in spectroscopy](https://en.wikipedia.org/wiki/Stark_spectroscopy) as well as [in semiconductor optics](https://en.wikipedia.org/wiki/Coherent_effects_in_semiconductor_optics#The_excitonic_optical_Stark_effect). The observations of the spectral lines arising from the Stark effect was also historically important in the development of quantum theory, as it could not be explained by classical physics. For those interested in the history of the Stark effect, [this YouTube video](https://youtu.be/CQ1kgzCXDe8) and [this other YouTube video](https://www.youtube.com/watch?v=OvQMIif3ty0) (both by the excellent channel of [Dr. Jorge S. Diaz](https://www.youtube.com/@jkzero)) for more information regarding the history of the Stark effect.

#### The quadratic Stark effect

Now, we will go beyond first-order and examine the energy shifts to *second-order*. This is known as the **quadratic Stark effect** as it is quadratic in the electric field strength ($\Delta E \sim \mathcal{E}_0^2$). Using second-order perturbation theory, it can be shown that the energy shifts are given by:

{% math() %}
\Delta E_{n}^{(2)} = -\frac{1}{2} \sum_{i} \sum_{j} \alpha_{ij} \mathbf{E}_i \mathbf{E}_{j}
{% end %}

Where $\mathbf{E}$ is the $i$-th component of the electric field (in our simplified case, $\mathbf{E} = \mathbf{E} = 0$ except for $i = j = 3$, where $\mathbf{E}_3 = E_0$ Note that if the material is isotropic (which most materials can be assumed to be), the polarizability tensor $\alpha_{ij}$ can be expressed as:

{% math() %}
\alpha_{ij} = \alpha \delta_{ij}, \quad
\alpha_{0} = 4\pi \varepsilon_{0} a_{0}^3 = \text{const.}
{% end %}

Where $\alpha_0$ is known as the **static electric polarizability**. Hence, the expression for the second-order energy shifts for isotropic materials reduces to:

{% math() %}
\Delta E_{n}^{(2)} = -\frac{1}{2} \alpha_{0} E_{0}^2
{% end %}

Unlike the linear Stark effect, the quadratic Stark effect does predict an energy shift for the $n = 1$ state (ground state), albeit a very small energy shift. In fact, it predicts an energy shift for all the energy levels! However, even in an extremely powerful electric field of $E_0 = \pu{10^7 V/cm}$ the quadratic stark shift for the $n = 1$ state is only around $\pu{0.05 meV}$, which is a *tiny shift*. Hence, the Stark effect is generally dominated by the first-order (linear) contribution rather than the second-order (quadratic) contribution.

### The generalized Stark effect

We can use the procedure we performed for the first and second-order energy shifts to come up with energy corrections to any desired order. It is left as a challenge for the reader to derive a *generalized formula* for the Stark energy shifts for arbitrary $n, \ell, m$ (this is an exercise for the adventurous reader because it is not easy to do!) The general solutions for the first, second, and third-order energy shifts are as follows (from section 3.10.2 of [_Elementary Molecular Quantum Mechanics 2nd ed._](https://www.sciencedirect.com/science/chapter/monograph/abs/pii/B9780444626479000038)):

{% math() %}
\begin{align*}
\Delta E^{(1)}_{n} &= -\frac{3}{2} e E_{0} a_{0} n(k_{1} - k_{2}) \\
\Delta E^{(2)}_{n} &= -\frac{1}{16} \alpha_{0} E_{0}^2 n^4(17n^2 - 3n_{e}^2 - 9m^2 + 19), \quad n_{e} \equiv k_{1} - k_{2} \\
\Delta E^{(3)}_{n} &= \frac{3}{32} \frac{(4\pi \varepsilon_{0})^2 a_{0}^5}{e} E_{0}^3 n^7 n_{e}(23 n^2 - n_{e}^2 + 11 m^2 + 39)
\end{align*}
{% end %}

Where $n$ is the principal quantum number, $m$ is the magnetic quantum number, $k_1, k_2$ are known as the *parabolic quantum numbers* that satisfy $n = k_1 + k_2 + m + 1$, and $\alpha_{0} =  4\pi \varepsilon_{0} a_{0}^3$ is the static electric polarizability. In the case of $n = 2$ and $m = 0$ (which we previously analyzed), one has $k_1 + k_2 = 1$; in the case that $k_1 = 2$ and $k_2 = 1$ (or the other way around when $k_1 = 1$ and $k_2 = 2$), we recover the first-order expression for the linear Stark effect for the $n = 2$ state (that is, $\Delta E^{(1)}_{2} = \pm 3 eE_0 a_0$) that we derived earlier!

### The fine structure of hydrogen

We observe that among the spectral lines of the hydrogen atom, there are lines at wavelengths not accounted for by the Rydberg formula. In particular, these lines indicate transitions between eigenstates with different values of $\ell$ but the same value of $n$. But in the basic solution to the hydrogen atom, these states are degenerate, and therefore should have the same energies, making it impossible for a transition to occur between them. So why do they occur?

The answer lies in the **fine structure** of hydrogen. Fine structure is a combination of several different effects that shift the energy levels of the hydrogen atom and lift the degeneracy of the energy levels:

- **Spin-orbit coupling** (_SO coupling_), which comes from considering the interaction of the electron's magnetic moment with the nuclear magnetic field
- The **relativistic energy correction**, which comes from the difference between the relativistic expression and non-relativistic expressions for the kinetic energy operator
- The **Darwin term**, which comes from the interaction of the electron with the quantum fluctuations of the electromagnetic field (called _zitterbewegung_)

The calculation of the fine structure corrections to the energy levels of the hydrogen atom is interesting in that it actually does have an *exact solution*. This involves solving the relativistic [Dirac equation](https://en.wikipedia.org/wiki/Dirac_equation) (which we'll get more to later), and gives the precise energy levels including all relativistic effects as well as spin. However, this solution is complicated, and using perturbation theory, we can arrive at an *approximate solution* that is close enough to the exact solution that it is essentially "correct".

> **Historical note:** Interestingly enough, the fine-structure expression for the energy levels of hydrogen predates (modern) quantum mechanics! In fact, it was first derived in the now-antiquated [Bohr-Sommerfeld model](https://en.wikipedia.org/wiki/Bohr%E2%80%93Sommerfeld_model#Relativistic_orbit) by Arnold Sommerfeld in 1919. It is remarkable that Sommerfeld managed to find the relativistically-correct expression for the energy levels of hydrogen without the use of perturbation theory or even the Schrödinger equation!

> **Note:** In the entire calculation for the fine structure, we will assume that the Bohr radius $a_0$ of the atom is approximately equal to its reduced Bohr radius {% inlmath() %}a_0^*{% end %}. The difference between the two is so small that except for exotic atoms (like positronium and muonium) {% inlmath() %}a_0{% end %} and {% inlmath() %}a_0^*{% end %} are effectively equal.

#### The relativistic energy correction

Let's start with the relativistic energy correction, the first major contribution to the fine-structure constant. This correction is due to the fact that in the Hamiltonian for the hydrogen atom, we started from the non-relativistic expression for the kinetic energy:

{% math() %}
K_\mathrm{nonrelativistic} = \frac{p^2}{2m}
{% end %}

Where $p$ is the momentum and $m$ is the mass of a (classical) particle. But special relativity tells us that the relativistically-correct formula for the kinetic energy is:

{% math() %}
\begin{align*}
K_\mathrm{relativistic} &= \sqrt{ (pc)^2 + (mc^2)^2 } - mc^2 \\
&= mc^2 \sqrt{ 1 + \left( \frac{p}{mc} \right)^2 } - mc^2 \\
&= mc^2 + \left( \frac{p^2}{2m} - \frac{p^4}{8m^3 c^2} + \dots\right) - mc^2 \\
&= \frac{p^2}{2m} - \frac{p^4}{8m^3 c^2}
\end{align*}
{% end %}

Where in the third step, we utilized a Taylor expansion to approximate the square root (where here, $x = p/mc$):

{% math() %}
\sqrt{ 1 + x^2} \approx 1 + \frac{1}{2}x^2 - \frac{1}{8}x^4 + \frac{1}{16}x^6 - \frac{5}{128}x^8 + \dots
{% end %}

> **Note:** Higher-order terms in the Taylor expression for the relativistic kinetic energy are suppressed by powers of $1/c^4 \sim 10^{-34}$ and hence we can safely ignore them in our perturbative calculations.

Hence, the difference between the relativistic and non-relativistic expressions is given (to first-order) by:

{% math() %}
K_\mathrm{nonrelativistic} - K_\mathrm{relativistic} = -\frac{p^4}{8m^3 c^2}
{% end %}

The corresponding perturbation $\Delta \hat H_\mathrm{relativity}$ is obtained by changing the classical momentum $p$ into the quantum momentum operator $\hat p$, giving us:

{% math() %}
\Delta \hat H_\mathrm{relativity} = -\frac{\hat{p}^4}{8m^3 c^2}
{% end %}

Hence, first-order perturbation theory gives us:

{% math() %}
\begin{align*}
\Delta E^{(1)}_\mathrm{relativity} &= \langle \varphi_{n}|\Delta \hat{H}_\mathrm{relativity}|\varphi_{n}\rangle \\
&= -\frac{1}{8m^3 c^2}\langle \varphi_{n}|\hat{p}^4|\varphi_{n}\rangle
\end{align*}
{% end %}

Now, we can use a clever trick to compute the inner product in a simpler way. Recall that the Bohr energies $E_n$ are the solutions to the non-relativistic Hamiltonian $\hat H_0 = \frac{\hat p^2}{2m} + V(r)$, where $V(r)$ is the Coulomb potential. Therefore, we have:

{% math() %}
\hat{H}_{0}|\varphi_{n}\rangle = \left(\frac{\hat p^2}{2m} + V(r)\right)|\varphi_{n}\rangle = E_{n}|\varphi_{n}\rangle
{% end %}

Now, since this is a linear eigenvalue equation, we can rearrange it to:

{% math() %}
E_{n}|\varphi_{n}\rangle - V(r) |\varphi_{n}\rangle = \frac{\hat{p}^2}{2m}|\varphi_{n}\rangle
{% end %}

Therefore, we have:

{% math() %}
\hat{p}^2|\varphi_{n}\rangle = 2m(E_{n} - V(r))|\varphi_{n}\rangle
{% end %}

This tells us that:

{% math() %}
\begin{align*}
\hat{p}^4|\varphi_{n}\rangle &= \hat{p}^2[\hat{p}^2|\varphi_{n}\rangle] \\
&= \big(2m[E_{n} - V(r)]\big)^2|\varphi_{n}\rangle \\
&= 4m^2(E_{n} - 2E_{n}V(r) + V(r)^2)|\varphi_{n}\rangle
\end{align*}
{% end %}

Hence, we have avoided needed to explicitly evaluate $\hat p^4$, which would otherwise involve taking fourth-derivatives of the eigenfunctions — that would not be fun at all! Now, we can expand the terms out and substitute them back into the first-order energy correction equation:

{% math() %}
\begin{align*}
\Delta E_\mathrm{relativity} &= -\frac{1}{8m^3 c^2}\langle \varphi_{n}|\hat{p}^4|\varphi_{n}\rangle \\
&= -\frac{4m^2}{8m^3 c^2} \langle \varphi_{n}|(E_{n} - 2E_{n}V(r) + V(r)^2)|\varphi_{n}\rangle \\
&= -\frac{1}{2m_{e} c^2}(E_{n}^2 - 2 E_{n}\langle V(r)\rangle + \langle V(r)^2\rangle)
\end{align*}
{% end %}

In the last step, we have chosen to explicitly set $m = m_e$, where $m_e$ is the electron mass; this was implied in the previous steps but not written out explicitly. All that is left is computing the expectation values $\langle V(r)\rangle$ and $\langle V(r)^2\rangle$ of the Coulomb potential $V(r) = -\frac{Ze^2}{4\pi \varepsilon_{0}r}$, which are respectively given by:

{% math() %}
\langle V(r)\rangle = -\frac{Ze^2}{4\pi\varepsilon_{0}} \left\langle \frac{1}{r}\right\rangle, \quad \langle V(r)^2\rangle = \left( \frac{Ze^2}{4\pi\varepsilon_{0}} \right)^2\left\langle \frac{1}{r^2}\right\rangle
{% end %}

We may evaluate these with the following identities:

{% math() %}
\left\langle \frac{1}{r}\right\rangle = \frac{Z}{a_{0}n^2}, \quad \left\langle \frac{1}{r^2}\right\rangle = \frac{Z^2}{n^3 a_{0}^2 \left( \ell + \frac{1}{2} \right)}
{% end %}

Where $a_0$ is the Bohr radius and $n, \ell$ are the principal and azimuthal quantum numbers respectively. Substituting these in gives us:

{% math() %}
\langle V(r)\rangle = -\frac{Z^2e^2}{4\pi\varepsilon_{0} a_{0}n^2}, \quad \langle V(r)^2\rangle = \frac{Z^4 e^4}{16\pi^2 \varepsilon_{0}^2} \frac{1}{n^3 a_{0}^2 \left( \ell + \frac{1}{2} \right)}
{% end %}

There is a more elegant way to write these two expressions, using the **fine structure constant** $\alpha$, which is given by:

{% math() %}
\alpha = \frac{e^2}{4\pi\varepsilon_{0}\hbar c} = 0.00729735 \approx \frac{1}{137}
{% end %}

The Bohr radius $a_0$ is itself related to the fine structure constant by $a_0 = \hbar/(m_ec\alpha)$. In fact, nearly every quantum system that has anything to do with an atom can be written in some way in terms of the fine-structure constant! Its ubiquity throughout quantum physics is all the more mysterious considering that it is a *dimensionless number* whose value, to this day, *cannot* be predicted from first principles. Moreover, its reciprocal $\frac{1}{\alpha}$ is *very nearly* 137, a value that has fascinated (and spooked) generations of physicists. Attempting to find an explanation for its value (or trying to find a formula that predicts that value of $\alpha$ from pure numbers) has led some on a path to [numerology](https://en.wikipedia.org/wiki/Numerology#Related_uses), others to begrudging acceptance, and still others to denial. Regardless, the fine structure constant has become an integral part of quantum physics and is here to stay.

But back on topic! In terms of the fine-structure constant, the expectation values we calculated take the following (much more elegant) forms:

{% math() %}
\begin{align*}
\langle V(r)\rangle &= -\frac{Z^2 \alpha \hbar c}{n^2 a_{0}} = -\frac{Z^2}{n^2} \alpha \hbar c \frac{m_{e}c \alpha}{\hbar} \\ &= -\frac{Z^2}{n^2}m_{e}c^2 \alpha^2 \\
\langle V(r)^2\rangle &= \frac{Z^4 (\alpha \hbar c)^2}{n^3\left( \ell + \frac{1}{2} \right)} \frac{1}{a_{0}^2} = \frac{Z^4 (\alpha \hbar c)^2}{n^3\left( \ell + \frac{1}{2} \right)} \frac{1}{a_{0}^2}\frac{(m_{e}c \alpha)^2}{\hbar^2} \\&= \frac{Z^4 \alpha^4}{n^3} \frac{m_{e}^2 c^4}{\left( \ell + \frac{1}{2} \right)}
\end{align*}
{% end %}

Meanwhile, the Bohr energies $E_n$ can also be expressed in terms of the fine structure constant as:

{% math() %}
E_{n} = -\frac{Z^2}{2n^2}m_{e}c^2 \alpha^2 = \frac{1}{2}\langle V(r)\rangle \implies \langle V(r)\rangle = 2E_{n}
{% end %}

(This relation is not coincidental; it is a consequence of the virial theorem, which we discussed when we went over the Bohr model.) Substituting these in gives us our final expression(s) for the relativistic energy correction:

{% math() %}
\begin{align*}
\Delta E_\mathrm{relativity} &= -\frac{1}{2m_{e} c^2}(E_{n}^2 - 2 E_{n}\langle V(r)\rangle + \langle V(r)^2\rangle) \\
&= -\frac{1}{2m_{e}c^2}\left\{ E_{n}^2 - 2E_{n}(2E_{n}) + \frac{Z^4 \alpha^4}{n^3} \frac{m_{e}^2 c^4}{\left( \ell + \frac{1}{2} \right)} \right\} \\
&= -\frac{1}{2m_{e}c^2}\left\{\frac{Z^4 \alpha^4}{n^3} \frac{m_{e}^2 c^4}{\left( \ell + \frac{1}{2} \right)}-3E_{n}^2\right\} \\
&= -\frac{Z^4 \alpha^4}{2n^3} \frac{m_{e}c^2}{\left( \ell + \frac{1}{2} \right)} -\frac{3}{2m_{e}c^2}\left( -\frac{Z^2}{2n^2}m_{e}c^2 \alpha^2 \right)^2 \\
&= -\frac{Z^4 \alpha^4}{2n^3} \frac{m_{e}c^2}{\left( \ell + \frac{1}{2} \right)} - \frac{3Z^4 \alpha^4 m_{e} c^2}{4n^4} \\
&= -\frac{Z^4 \alpha^4 m_{e}c^2}{2n^3}\left( \frac{1}{\ell + \frac{1}{2}} - \frac{3}{4n} \right)
\end{align*}
{% end %}

Where $n$ is the principal quantum number and $\ell$ is the azimuthal quantum number, as before. For the ground state of hydrogen (with $n = 1, \ell = 0$) this gives us an energy shift of:

{% math() %}
\Delta E_\mathrm{relativity} \approx -\pu{9.056 * 10^{-4} eV}
{% end %}

#### Spin-orbit coupling

Let's now analyze the effect of spin-orbit coupling (sometimes abbreviated as "SO coupling"). Spin-orbit coupling comes from the interaction between electron spin and the magnetic field generated by the a moving nucleus. _"But wait! Isn't the nucleus stationary?"_ Indeed that is essentially correct, but only in the *rest frame of the atom*. Einstein's theory of relativity tells us that in the electron's rest frame, the electron is stationary, while the nucleus is moving! And since a moving charge generates a magnetic field, that magnetic field can then interact with the electron's spin, leading to spin-orbit coupling!

First, let's calculate the magnetic field of the nucleus in the rest frame of the electron. We can assume (to a good approximation) that the nucleus is a classical point charge. The magnetic field of a point charge of charge $q$ moving at velocity $\mathbf{v}'$ is given by the Biot-Savart law, which (in its simplified form) is given by:

{% math() %}
\mathbf{B}(\mathbf{r}) = \frac{\mu_{0}}{4\pi} \frac{q\mathbf{v}' \times \mathbf{r}}{r^3}
{% end %}

Where $\mu_0$ is the *permeability of free space*, and is a fundamental constant of electromagnetism. The nucleus is positively-charged, so its charge is $Ze$. Meanwhile, by the principle of relativity, its velocity $\mathbf{v}'$ is equal to $-\mathbf{v}$ (the negative of the electron's velocity in the atom's rest frame). This gives us:

{% math() %}
\mathbf{B}(\mathbf{r}) = -\frac{\mu_{0}}{4\pi} \frac{Ze\mathbf{v} \times \mathbf{r}}{r^3} = \frac{(Ze)\mu_{0}}{4\pi} \frac{\mathbf{r} \times \mathbf{v}}{r^3}
{% end %}

Where we used the fact that cross products are anti-commutative ($\mathbf{A} \times \mathbf{B} = -\mathbf{B} \times \mathbf{A}$). Now, in the atom's rest frame, we know that the velocity $\mathbf{v}$ of the electron is related to its momentum $\mathbf{p}$ by $\mathbf{p} = m_{e}\mathbf{v}$. We can therefore write $\mathbf{v} = \mathbf{p}/m_{e}$, upon which substitution into the expression for the magnetic field gives us:

{% math() %}
\mathbf{B}(\mathbf{r}) = \frac{(Ze)\mu_{0}}{4\pi m_{e}} \frac{\mathbf{r} \times \mathbf{p}}{r^3} = \frac{(Ze)\mu_{0}}{4\pi m_{e}} \frac{\mathbf{L}}{r^3}
{% end %}

Where $\mathbf{L}$ is the classical angular momentum of the electron (we'll soon quantize this). We'll also make another small change by replacing $\mu_0$ with $1/(\varepsilon_0 c^2)$. This comes from the definition of the speed of light, which is given by:

{% math() %}
c = \frac{1}{\sqrt{ \mu_{0}\varepsilon_{0} }}
{% end %}

The reason for this change is to match the standard convention and to make it easier for our simplifications later. With this change, the magnetic field becomes:

{% math() %}
\mathbf{B}(\mathbf{r}) = \frac{Ze}{4\pi m_{e} \varepsilon_{0}c^2} \frac{\mathbf{L}}{r^3}
{% end %}

Now, recall from our calculation of the Zeeman effect that the interaction between an electron and a magnetic field can be expressed with the following perturbation in the Hamiltonian:

{% math() %}
\Delta \hat{H} = -\boldsymbol{\mu}_{M} \cdot \mathbf{B} = -g\frac{q}{2m} (\hat{\mathbf{S}} \cdot \mathbf{B})
{% end %}

Where $\hat{\mathbf{S}}$ is the spin operator, $\boldsymbol{\mu}_{M}$ is the magnetic dipole moment operator, $\mu_B$ is the Bohr magneton, and $g$ is the g-factor, which varies depending on the type of particle and whether the coupling is to orbital or spin angular momentum. In our case, we have an interesting situation, since *both* orbital and spin angular momentum play a role. It turns out that the right g-factor to use is given by:

{% math() %}
g = g_{s} - 1 = 1.0023193
{% end %}

Note that this is *almost* but not *exactly* equal to $g_l$, the electron orbital g-factor, which has a value of exactly one. The reason why $g_s - 1 \neq g_l$ is due to quantum electrodynamics, but that's a topic we'll reserve for later. In any case, we can plug our magnetic field and our not-one-but-almost-one g-factor to construct the following *spin-orbit coupling correction term* to the Hamiltonian:

{% math() %}
\Delta \hat{H}_\mathrm{SO} = -g\frac{q}{2m} (\hat{\mathbf{S}} \cdot \mathbf{B}) = \frac{Ze^2}{4\pi \varepsilon_{0}} \left( \frac{g_{s} - 1}{2m_{e}^2 c^2} \right) \frac{\hat{\mathbf{L}} \cdot \hat{\mathbf{S}}}{r^3}
{% end %}

Where $q = -e$ and $m = m_e$ for an electron, and we exchanged the *classical* angular momentum $\mathbf{L}$ for the *quantum* angular momentum operator $\hat{\mathbf{L}}$. Most of our work is now done, but we still have to apply perturbation theory to find the energy shifts. The spin-orbital energy shift $\Delta E_\mathrm{SO}$ is therefore given by:

{% math() %}
\begin{align*}
\Delta E_\mathrm{SO} &= \langle \varphi_{n}| \Delta \hat{H}_\mathrm{SO} |\varphi_{n}\rangle \\
&= \frac{Ze^2}{4\pi \varepsilon_{0}} \left( \frac{g_{s} - 1}{2m_{e}^2 c^2} \right) \left\langle \frac{\hat{\mathbf{L}} \cdot \hat{\mathbf{S}}}{r^3}\right\rangle
\end{align*}
{% end %}

To evaluate the expectation value without needing to do explicit inner products, we can use a few shortcuts. First, we may use the identity:

{% math() %}
\langle \hat{\mathbf{L}} \cdot \hat{\mathbf{S}}\rangle = \frac{\hbar^2}{2}[j(j + 1) - \ell(\ell + 1) - s(s + 1)]
{% end %}

Where $s$ is the spin quantum number, $\ell$ is the azimuthal quantum number, and $j = \ell + s$ is the total angular momentum quantum number. Since electrons are spin-1/2 particles, we only have $s = \frac{1}{2}$ and thus:

{% math() %}
\langle \hat{\mathbf{L}} \cdot \hat{\mathbf{S}}\rangle = \frac{\hbar^2}{2}\left[ j(j + 1) - \ell(\ell + 1) - \frac{3}{4} \right]
{% end %}

Second, we can use the Kramers-Pasternack relation, which tells us that:

{% math() %}
\left\langle \frac{1}{r^3} \right\rangle = \frac{Z^3}{n^3 a_{0}^3} \frac{1}{\ell\left( \ell + \frac{1}{2} \right) (\ell + 1)}
{% end %}

You are welcome to derive these identities yourself if you so wish; however, we will not attempt to rigorously prove them. With these identities, the energy shift simplifies to:

{% math() %}
\begin{align*}
\Delta E_\mathrm{SO} &= \frac{Ze^2}{4\pi \varepsilon_{0}} \left( \frac{g_{s} - 1}{2m_{e}^2 c^2} \right) \frac{\hbar^2}{2}\left(j(j + 1) - \ell(\ell + 1) - \frac{3}{4}\right) \left\langle \frac{1}{r^3}\right\rangle \\
&= \frac{Ze^2}{4\pi \varepsilon_{0}} \left( \frac{g_{s} - 1}{2m_{e}^2 c^2} \right) \frac{\hbar^2}{2} \frac{Z^3}{n^3 a_{0}^3} \frac{j(j + 1) - \ell(\ell + 1) - \frac{3}{4}}{\ell\left( \ell + \frac{1}{2} \right) (\ell + 1)}
\end{align*}
{% end %}

This can be expressed in terms of the fine-structure constant as:

{% math() %}
\Delta E_\mathrm{SO} = \frac{Z^4}{4n^3}m_{e} c^2 \alpha^4 (g_{s} - 1) \left[ \frac{j(j + 1) - \ell(\ell + 1) - \frac{3}{4}}{\ell\left( \ell + \frac{1}{2} \right) (\ell + 1)} \right]
{% end %}

Unfortunately, our theoretical results have one major error: we assumed $\mathbf{v}' = -\mathbf{v}$ at the beginning of our derivation, which only technically holds true for *inertial reference frames*. By contrast, the electron undergoes acceleration from the Coulomb force, which requires us to modify the relation. This is known as **Thomas precession**, and if we had included Thomas precession in our calculation, we find that the spin-orbital energies would be halved, giving us the corrected energies of:

{% math() %}
\begin{align*}
\Delta E_\mathrm{SO} &= \frac{Z^4}{8n^3}m_{e} c^2 \alpha^4 (g_{s} - 1) \left[ \frac{j(j + 1) - \ell(\ell + 1) - \frac{3}{4}}{\ell\left( \ell + \frac{1}{2} \right) (\ell + 1)} \right] \\
&\approx \frac{Z^4}{8n^3}m_{e} c^2 \alpha^4 \left[ \frac{j(j + 1) - \ell(\ell + 1) - \frac{3}{4}}{\ell\left( \ell + \frac{1}{2} \right) (\ell + 1)} \right]
\end{align*}
{% end %}

> **Note:** in the last line we used the approximation $g_s = 2$, hence $g_s - 1 \approx 1$. This approximation is accurate enough for practically all purposes.

#### The Darwin term

The Darwin term arises from the quantum fluctuations of the electromagnetic field. This is because the electromagnetic field is fundamentally quantum. An oversimplified explanation can be found from the Heisenberg uncertainty principle, which tells us that $\Delta E \Delta t \geq \hbar/2$. This means that over very short time intervals, the total amount of energy in the electromagnetic field is uncertain, leading to *energy fluctuations*. This behavior is captured in the **Darwin Hamiltonian**, which we will not derive, but is given by:

{% math() %}
\Delta \hat{H}_\mathrm{Darwin} = \frac{Ze^2 \hbar^2}{8m_{e}^2 c^2 \varepsilon_{0}} \delta^3(\mathbf{r})
{% end %}

Where $\delta^3(\mathbf{r})$ is the Dirac delta function in three dimensions (here it has units of inverse volume). This is a delta function potential in the form $V = a \delta(x)$, and luckily, we already know how to solve potentials of the form from our exploration of the bound states of the delta function ("spike") potential. The solution, as we found, is:

{% math() %}
E_{n} = a|\psi_{n}(0)|^2
{% end %}

Therefore, substituting this in gives us an energy shift of:

{% math() %}
\Delta E_\mathrm{Darwin} = \frac{Ze^2 \hbar^2}{8m_{e}^2 c^2 \varepsilon_{0}}|\psi(0)|^2 = \frac{Z\alpha\hbar^3 \pi}{2m_{e}^2c} |\psi(0)|^2
{% end %}

Note that this energy shift only affects $s$ orbitals (those with $\ell = 0$) since only $s$ orbitals are nonzero at the origin. Since delta function potentials are zero everywhere except at the origin, they cannot affect states that have $\psi(0) = 0$, which corresponds to all states with $\ell \geq 1$. In the case of the hydrogen ground-state we have:

{% math() %}
|\psi_{100}(0)|^2 = \frac{1}{\pi a_{0}^3} = \frac{1}{\pi}\left( \frac{m_{e}c\alpha}{\hbar} \right)^3 \implies \Delta E_\mathrm{Darwin} = \frac{Z\alpha^4 m_{e}c^2}{2}
{% end %}

(We use the approximation {% inlmath() %}a_0 \approx a_0^*{% end %} here; technically we should use the reduced Bohr radius {% inlmath() %}a_0^*{% end %} in $|\psi(0)|$, but to a good approximation {% inlmath() %}a_0^*{% end %} is equal to the regular Bohr radius of {% inlmath() %}a_0 \approx \pu{52.92 pm}{% end %}). Substituting in numbers, the Darwin energy correction for the hydrogen ground state has a numerical value of:

{% math() %}
\Delta E_\mathrm{Darwin} \approx \pu{7.245 * 10^{-5} eV}
{% end %}

In general, we may express $|\psi(0)|^2$ for arbitrary $n$ (with the approximation $a_0 \approx a_0^*$) as:

{% math() %}
|\psi_{n00}(0)|^2 = \frac{1}{\pi} \left( \frac{Z}{na_{0}} \right)^3
{% end %}

Using the above result, it is a straightforward calculation to calculate the general expression for the Darwin energy shifts for arbitrary $n$:

{% math() %}
\Delta E_\mathrm{Darwin} = \frac{Z\alpha\hbar^3 \pi}{2m_{e}^2c} |\psi(0)|^2
= \frac{Z\alpha\hbar^3}{2m_{e}^2c}  \left( \frac{Z}{na_{0}} \right)^3 = \frac{Z^4\alpha^4 m_{e}c^2}{2n^3}
{% end %}

In numerical form, this can be expressed as:

{% math() %}
\Delta E_\mathrm{Darwin} \approx \frac{Z^4}{n^3} \cdot (\pu{7.245 * 10^{-5} eV})
{% end %}

#### Total effect of fine structure corrections

The total energy shift due to fine-structure corrections is a combination of the three effects we have discussed, and (after tedious algebra that we will not show) they are given by:

{% math() %}
\begin{align*}
\Delta E &= \Delta E_\mathrm{relativity} + \Delta E_\mathrm{SO} + \Delta E_\mathrm{Darwin} \\
&= -\frac{Z^4 \alpha^4}{2n^4}m_{e}c^2 \left[ \frac{n}{j + \frac{1}{2}} - \frac{3}{4} \right]
\end{align*}
{% end %}

Where $n$ is the principal quantum number and $j = \ell + s$ is the angular momentum quantum number. This formula is a non-trivial result because it shows us that states with **different total angular momenta** $j$ are non-degenerate. However, states that share the same $j$ are *still* degenerate. This means that the $2p^{1/2}$ and $2p^{3/2}$ states are non-degenerate but the $2s^{1/2}$ and $2p^{1/2}$ states are still degenerate. Putting together the fine-structure structure and the base energy levels of hydrogen gives us the following expression for the atomic energy levels:

{% math() %}
\begin{align*}
E_{nj} &= -\frac{Z^2 \alpha^2}{2n^2} m_{e}c^2\left[ 1 + \frac{Z^2\alpha^2}{n^2} \left( \frac{n}{j + \frac{1}{2}} - \frac{3}{4} \right) \right] \\
&\approx -\pu{13.6 eV}\cdot \frac{Z^2}{n^2}\left[ 1 + (5.325 \times 10^{-5}) \cdot \frac{Z^2}{n^2} \left( \frac{n}{j + \frac{1}{2}} - \frac{3}{4} \right) \right] 
\end{align*}
{% end %}

> **Note for the advanced reader:** This solution can also be derived non-perturbatively, but we'll need to use relativistic quantum mechanics (in particular, the [Dirac equation](https://en.wikipedia.org/wiki/Dirac_equation)).

In the lowest excited state of the hydrogen atom, the total effect of the fine-structure corrections is an energy shift on the order of $10^{-4} \text{ eV}$. This effect is indeed very small, which is why we can solve the Schrödinger equation for the hydrogen atom while ignoring spin (and relativity) and still have a very accurate result. The two corrections are much more important for heavy atoms (which have highly-relativistic electrons) and in the presence of magnetic or electric fields (as is the case in the Zeeman effect and Stark effect).

![](https://upload.wikimedia.org/wikipedia/commons/6/64/Hydrogen_fine_structure_energy_2.svg)

_From left to right: energy levels of hydrogen with (a) Coulomb potential only, (b) Coulomb potential + relativistic correction, (c) Coulomb potential + all fine-structure corrections, and (d) Coulomb potential + fine structure + Zeeman effect terms._

#### The exact fine-structure energy levels of the hydrogen atom

The fine-structure corrections to the energy levels of hydrogen can also be calculated with the relativistic **Dirac equation**, which yield the *fine-structure energy levels* of the hydrogen atom without needing to invoke approximations. They are given by:

{% math() %}
E_{jn} = -m_{e}c^2 + m_{e}c^2\left( 1 + \left[ \frac{Z\alpha}{n - j - \frac{1}{2} + \sqrt{ \left( j + \frac{1}{2} \right)^2 - (Z\alpha)^2 }} \right]^2 \right)^{-1/2}
{% end %}

(Technically we should use the reduced mass $\mu$ instead of the electron mass $m_e$, though the substitution is straightforward.) Something very interesting happens if we Taylor-expand the exact solution from the Dirac equation, and this is sufficiently important that we will do it step-by-step. First, we use the Taylor series $(1 + x^2)^{-1/2} = 1 - \frac{1}{2}x^2 + \frac{3}{8}x^4 \dots$ to expand out the second term, giving us:

{% math() %}
\begin{align*}
E_{jn} &\approx -m_{e}c^2 + m_{e}c^2\left\{ 1 - \frac{1}{2}\left[ \frac{Z\alpha}{n - j - \frac{1}{2} + \sqrt{ \left( j + \frac{1}{2} \right)^2 - (Z\alpha)^2 }} \right]^2 + \dots\right\} \\
&= \cancel{ -m_{e}c^2 } + \cancel{ m_{e}c^2 } -\frac{m_{e}c^2}{2} \left[ \frac{Z\alpha}{n - j - \frac{1}{2} + \sqrt{ \left( j + \frac{1}{2} \right)^2 - (Z\alpha)^2 }} \right]^2 + \dots \\
&= -\frac{m_{e}c^2(Z\alpha)^2}{2} \left[ \frac{1}{n - j - \frac{1}{2}+ \sqrt{ \left( j + \frac{1}{2} \right)^2 - (Z \alpha)^2 }} \right]^2 \\
&= -\frac{m_{e}c^2 (Z\alpha)^2}{2}\left[ n - \left( j + \frac{1}{2} \right) + \left( j + \frac{1}{2} \right)\sqrt{ 1 - \left(\small \frac{Z\alpha}{j + \frac{1}{2}} \right)^2 } \right]^{-2} \\
&\approx -\frac{m_{e}c^2 (Z\alpha)^2}{2}\left[ n - \left( j + \frac{1}{2} \right) + \left( j + \frac{1}{2} \right)\left( 1 - \frac{1}{2}\left(\small \frac{Z\alpha}{j + \frac{1}{2}} \right)^2 + \dots \right) \right]^{-2} \\
&= -\frac{m_{e}c^2 (Z\alpha)^2}{2} \left[ n - \cancel{ \left( j + \frac{1}{2} \right) } + \cancel{ \left( j + \frac{1}{2} \right) } -\frac{1}{2} \left( j + \frac{1}{2} \right)\left(\small \frac{Z\alpha}{j + \frac{1}{2}} \right)^2 + \dots \right]^{-2} \\
&= -\frac{m_{e}c^2 (Z\alpha)^2}{2n^2}\left[ 1 -\frac{1}{2n} \frac{(Z \alpha)^2}{\left( j + \frac{1}{2} \right)} + \dots \right]^{-2}
\end{align*}
{% end %}

Here, in the first step, we perform our initial Taylor expansion; this naturally allows the $m_ec^2$ dependence to cancel out in the second step. Then, in the third step we factor out $(Z \alpha)^2$ from inside the fraction. In the fifth step, we factor out $\left(j + \frac{1}{2}\right)$ from the square root, which then allows us to use the following Taylor approximation:

{% math() %}
\sqrt{ 1 - \left(\small \frac{Z\alpha}{j + \frac{1}{2}} \right)^2 } = 1 - \frac{1}{2}\left(\small \frac{Z\alpha}{j + \frac{1}{2}} \right)^2 + \mathcal{O}((Z\alpha)^4)
{% end %}

Where $\mathcal{O}(Z^4\alpha^4)$ denotes terms that are fourth-order or higher in $Z\alpha$. This cancels out the first $j + \frac{1}{2}$ term, making the expression far simpler. Finally, in the last step, we factor out $n$ from the fraction. To finish, we use the binomial approximation $(1 - x)^{-2} \approx 1 + 2x$, giving us:

{% math() %}
\left[ 1 -\frac{1}{2n} \frac{(Z \alpha)^2}{\left( j + \frac{1}{2} \right)} + \dots \right]^{-2} \approx 1 + \frac{1}{n} \frac{(Z \alpha)^2}{\left( j + \frac{1}{2} \right)}
{% end %}

Plugging this in, our resulting energies become:

{% math() %}
E_{jn} \approx -\frac{m_{e}c^2 (Z\alpha)^2}{2n^2} \left[1 + \frac{1}{n} \frac{(Z \alpha)^2}{\left( j + \frac{1}{2} \right)} + \dots\right]
{% end %}

Which matches what we got from perturbation theory! Hence, the Dirac equation's solution *reproduces the result from perturbation theory* at low orders of $\alpha$. This is why the fine-structure constant is so important in quantum physics: it is the *natural expansion parameter* for perturbative expansions. Since $\alpha \ll 1$, higher powers of $\alpha$ become increasingly smaller, meaning that higher-power terms in series expansions involving $\alpha$ are much weaker. Hence, we can safely ignore higher-power terms when doing perturbative calculations. In contrast, if $\alpha \gg 1$, then higher-power terms in series expansions would actually grow *increasingly larger*, making perturbation theory useless. This phenomenon remains true even when we go into the world of quantum field theory, where the fine-structure constant occupies a fundamental role as the [coupling constant](https://en.wikipedia.org/wiki/Coupling_constant) of quantum electrodynamics!

> **Note:** While the Dirac equation provides an exact solution for the energy levels due to fine-structure, it does *not* predict smaller effects, including hyperfine structure and the Lamb shift, which (respectively) arise due to nuclear structure and quantum electrodynamics. We will examine these effects shortly.

### The hyperfine structure of hydrogen

Up to this point, we have considered the nucleus as a stationary point-like charge generating an electrostatic (Coulomb) potential, essentially like a classical point charge. However, we know now that this is not the case. Atomic nuclei are composed of protons and neutrons, which are also quantum particles. Crucially, atomic nuclei also have *spin*, and while nuclear spin can be neglected in a lot of problems, it is essential for explaining the **hyperfine transitions** of hydrogen.

The hyperfine transition occurs due to an interaction between the nuclear magnetic dipole moment and the magnetic field (in the nuclear rest frame) generated by the atomic electrons. Therefore, it is similar to spin-orbit coupling, except the spin is now nuclear spin, instead of electron spin. The *nuclear magnetic dipole moment operator* is given by:

{% math() %}
\boldsymbol{\mu}_{N} = g_I\frac{e}{2m_p} \hat{\mathbf{I}} = g_I \frac{\mu_{N}}{\hbar} \hat{\mathbf{I}}
{% end %}

Where $g_I$ is the nuclear spin g-factor, $m_{p}$ is the proton mass, $\mu_N$ is the nuclear magneton (a natural constant), and $\hat{\mathbf{I}}$ is the nuclear spin operator (similar to $\hat{\mathbf{S}}$, the electron spin operator). Since nuclei generally have both protons and neutrons, which have different masses, and may have different numbers of protons from neutrons, the nuclear g-factor does not have a simple formula (it is a constant that you generally have to look up). In the case of hydrogen, which has a nucleus made only of a single proton, $g_N \approx 5.6$.

In any case, the nuclear spin couples to the magnetic field generated by the electron. However, since the electron both has spin and orbital angular momentum, it has a more complicated magnetic field than a classical moving point charge. The orbital part of its magnetic field is straightforward: it is actually the same as what we used in calculating the spin-orbital contribution to fine structure, except we make the replacement $Ze \to -e$ to account for the different charge of the nucleus. This gives us the orbital magnetic field $\mathbf{B}_{\ell}$:

{% math() %}
\mathbf{B}_{\ell} = -\frac{e}{4\pi m_{e} \varepsilon_{0}c^2} \frac{\mathbf{L}}{r^3} = -\mu_{B} \frac{\mu_{0}}{2\pi} \frac{\mathbf{L}}{r^3}
{% end %}

Where $\mu_B = e\hbar/(2m_e)$ is the **Bohr magneton**. So far, so good; unfortunately, getting the contribution from the electron's spin is a much more complicated issue. This is because there is no *classical analogue* for spin. The closest approximation we can use is to model an electron as a magnetic dipole. The magnetic vector potential of a classical magnetic dipole is given by:

{% math() %}
\mathbf{A}(\mathbf{r}) = \frac{\mu_{0}}{4\pi} \frac{\mathbf{m} \times \mathbf{r}}{r^3}
{% end %}

Where $\mathbf{m}$ is the magnetic moment. The magnetic moment of an electron can be expressed as:

{% math() %}
\mathbf{m}_\mathrm{electron} = -\frac{g_{s}\mu_{B}\mathbf{S}}{\hbar}
{% end %}

Where $g_s \approx 2$ is the electron spin g-factor, $\mu_B$ is the Bohr magneton, and $\mathbf{S}$ is the spin angular momentum. The magnetic field is related to the magnetic vector potential by $\mathbf{B} = \nabla \times \mathbf{A}$, so the spin magnetic field $\mathbf{B}_{s}$ is:

{% math() %}
\mathbf{B}_{s} = \nabla \times \left( \frac{\mu_{0}}{4\pi} \frac{\mathbf{m} \times \mathbf{r}}{r^3} \right) = -\frac{g_{s} \mu_{0} \mu_{B}}{4\pi \hbar} \nabla \times \left( \frac{\mathbf{S} \times \mathbf{r}}{r^3} \right)
{% end %}

If we evaluate the curl here, it will expand to three terms:

{% math() %}
\nabla \times \left( \frac{\mathbf{S} \times \mathbf{r}}{r^3} \right) = \frac{3\mathbf{r}(\mathbf{S} \cdot \mathbf{r})}{r^5} - \frac{\mathbf{S}}{r^3} + \frac{8\pi}{3r^3} \delta^3(\mathbf{r}) \mathbf{S}
{% end %}

Where $\delta^3(\mathbf{r})$ is the 3-dimensional delta function. The total magnetic field from the electron is thus given by:

{% math() %}
\mathbf{B} = \mathbf{B}_{\ell} + \mathbf{B}_{s}
{% end %}

Now, we will construct the perturbation of the Hamiltonian describing hyperfine structure. As usual, when we go from a classical to quantum treatment, we replace the classical angular momentum $\mathbf{L}$ with its quantum counterpart, the angular momentum operator $\hat{\mathbf{L}}$. This gives us:

{% math() %}
\begin{align*}
\Delta \hat{H}_\mathrm{hyperfine} &= -\boldsymbol{\mu}_{N} \cdot \mathbf{B} \\
&= -\boldsymbol{\mu}_{N} \cdot (\mathbf{B}_{\ell} + \mathbf{B}_{s}) \\
&= g_I \frac{\mu_{N}}{\hbar} \left\{ \mu_{B} \frac{\mu_{0}}{2\pi} \frac{\hat{\mathbf{L}} \cdot \hat{\mathbf{I}}}{r^3} + \frac{g_{s} \mu_{0} \mu_{B}}{4\pi \hbar} \hat{\mathbf{I}} \cdot \left[ \frac{3\mathbf{r}(\hat{\mathbf{S}} \cdot \mathbf{r})}{r^5} - \frac{\hat{\mathbf{S}}}{r^3} + \frac{8\pi}{3r^3} \delta^3(\mathbf{r}) \hat{\mathbf{S}} \right] \right\} \\
&= g_I \frac{\mu_{N}}{\hbar} \left\{ \mu_{B} \frac{\mu_{0}}{2\pi} \frac{\hat{\mathbf{L}} \cdot \hat{\mathbf{I}}}{r^3} + \frac{g_{s} \mu_{0} \mu_{B}}{4\pi \hbar r^3} \left[ \frac{3(\hat{\mathbf{I}} \cdot\mathbf{r})(\hat{\mathbf{S}} \cdot \mathbf{r})}{r^2} - \hat{\mathbf{I}} \cdot\hat{\mathbf{S}}+ \frac{8\pi}{3} \delta^3(\mathbf{r}) \hat{\mathbf{I}} \cdot\hat{\mathbf{S}} \right] \right\}
\end{align*}
{% end %}

The delta function term is zero for $\ell = 0$, and evaluates to a term proportional to $|\psi(0)|^2$ otherwise. If one only computes the shifts for $\ell \neq 0$, we can can combine the term dependent on $\hat{\mathbf{L}} \cdot \hat{\mathbf{I}}$ and the term dependent on $\hat{\mathbf{I}} \cdot \hat{\mathbf{S}}$ into a single term dependent only on $\hat{\mathbf{J}}$, and apply the following identity:

{% math() %}
\hat{\mathbf{J}} \cdot \hat{\mathbf{I}} = \frac{\hbar^2}{2} [F(F + 1) - I(I + 1) - J(J + 1)]
{% end %}

Where $F = I + J$ is the total atomic angular momentum (as usual, $J = \ell + s$, we have simply written it with uppercase $J$ rather than lowercase $j$ as this is standard convention). We will *not* aim to calculate the general expressions for the energy corrections; that is left as an exercise for the reader, although the techniques are much the same as those we used to calculate the fine-structure corrections. Instead, we will simply give the result for the ground-state hyperfine corrections in hydrogen: it is:

{% math() %}
\Delta E = \frac{2}{3n^3}Z^4 \alpha^4 \left( \frac{m_{e}}{m_{p}} \right) (m_{e}c^2)g_I\left[ F(F + 1) - \frac{3}{2} \right] \quad (n = 1)
{% end %}

Since we are in the ground state ($n = 1, \ell = 0$) and the hydrogen nucleus (which is a single proton) always has a spin of $I = \frac{1}{2}$, the two possible states are $F = 0$ (spin-down) and $F = 1$ (spin-up). The ground-state hyperfine transition ($F = 1 \to F = 0$) is thus a spin-flip transition, where the electron goes from spin-up to spin-down, emitting a photon with an energy of $\Delta E \approx \pu{5.78 \mu eV}$. The hyperfine structure is an example of a so-called *forbidden transition* (the name is a misnomer because a "forbidden transition" really just means a transition is much less probable than a "allowed transition"). This originates from the (electric dipole coupling) selection rules for hydrogen, which mandate that for any transition, one has:

{% math() %}
\Delta \ell = \pm 1, \quad \Delta m = 0,\quad \Delta s = 0
{% end %}

(This comes from the electric dipole transition that we'll calculate later on in time-dependent perturbation theory.) Normally, this means that a spin-flip transition is impossible, since we have a change of the spin quantum number. But in the hyperfine transition this *is possible*. However, it is far more unlikely; in fact a hyperfine transition happens (on average) once every *11 million years*!

We can convert the hyperfine transition energy to frequency to find that a photon emitted (or absorbed) as a result of a hyperfine transition has a frequency of $\pu{1.42 GHz}$ (or more precisely, $1.420405751768(2) \text{{ GHz}}$, a value that has been measured to incredible precision). Converted to wavelength, this results in a wavelength of $\lambda \approx \pu{21 cm}$, which is in the microwave range of the electromagnetic spectrum.

While hyperfine splitting may seem like a tiny quantum correction that barely matters, it actually has tremendous importance in timekeeping and astronomy. The 21-centimeter spectral line of hydrogen is found almost everywhere in outer space, due to the prevalence of hydrogen in the Universe (particularly in hydrogen gas clouds), and observations of the 21 cm line were responsible for revealing the spiral structure of our galaxy. Hydrogen masers (microwave lasers) used for precision interferometry and in atomic clocks rely on the hyperfine transition and are used as some of the most accurate clocks because of the highly-stable frequency of the beams they emit.

### Order of magnitude of fine and hyperfine energy corrections

It is instructive to ask the question: how do fine structure and hyperfine structure compare in the relative magnitudes? First of all, both effects are to the same order in $\alpha$, the fine structure constant. Specifically, they are of order $\mathcal{O}(\alpha^4)$ in magnitude, which tells us that they are *at least* weaker by a factor of $\alpha^2$ than the electronic transitions (unperturbed energy levels) of the hydrogen atom, which are $\mathcal{O}(\alpha^2)$. This explains why we can afford to neglect fine (and hyperfine) structure in the hydrogen atom while still predicting spectral lines to good accuracy. However, this is not the full story: the energies associated with hyperfine transitions are *much smaller* in magnitude than that of fine structure transitions, since they also depend on the ratio $m_e/m_p \approx \frac{1}{1836}$ of the electron mass to the proton mass. Hence, hyperfine transitions are typically suppressed by lower-order effects and are not easily observed. The table below gives an overview of the comparison between electronic, fine-structure, and hyperfine transitions:

| Transition               | Typical energy splitting   | Type of EM radiation emitted     |
| ------------------------ | -------------------------- | -------------------------------- |
| Electronic (unperturbed) | Around $\pu{1 eV - 10 eV}$ | UV, visible light, near-infrared |
| Fine structure           | Around $\pu{1 meV}$        | UV, visible light, near-infrared |
| Hyperfine structure      | Around $\pu{1 \mu eV}$     | Microwaves (GHz range)           |

### The Lamb shift

Although fine (and hyperfine) structure lifts the degeneracy of many of the states of the hydrogen atom, it does not do so for all of them. For instance, the transition $2s^{1/2} \to 2p^{1/2}$ is conventionally impossible since they share the same $n$ and $j$ quantum numbers; hence, the fine-structure formula would tell us that the two states are degenerate (and thus share the same energies). Nevertheless, we physically *do* observe the transition, and it is due to something called the **Lamb shift**.

The Lamb shift originates from the quantum fluctuations of the electromagnetic field, much like the Darwin term in our calculation of the fine structure. Roughly-speaking, the quantum fluctuations have the net effect of "smearing" out the electron's position, which in turn modifies the Coulomb potential:

{% math() %}
V(r) = -\frac{Qe^2}{4\pi \varepsilon_{0}r} \to -\frac{Qe^2}{4\pi \varepsilon_{0}(r + \delta r)}
{% end %}

Where $\delta r$ is the average size of the fluctuations and $Q = Z$.  While a full derivation of the Lamb shift would require relativistic quantum field theory (which is something we'll cover much later), we can use a non-relativistic approximation to calculate the Lamb shift in the context of perturbation theory. The precise details are a bit complex (see [these lecture notes](https://quantummechanics.ucsd.edu/ph130a/130_notes/node476.html) if you want to see the derivation), but the general result is:

{% math() %}
\Delta E_{n} = \frac{2\alpha}{3\pi m_{e}^2 c^2} \frac{\hbar^2 \ln(k_0)}{2} \langle \nabla^2 V_{C}\rangle
{% end %}

Where $V_{C} = -Ze^2/4\pi \varepsilon_0 r$ is the Coulomb potential and $\ln(k_0) \approx \ln(1/8.9 \alpha^2)$ is known as the **Bethe logarithm**. To compute the energy shifts explicitly, we must compute $\langle \nabla^2 V_{C}\rangle$. The following identity is useful:

{% math() %}
\nabla^2\left( \frac{1}{r} \right) = -4\pi \delta^3(\mathbf{r})
{% end %}

Where $\delta^3(r)$ is the 3-dimensional Dirac delta function. Thus we have:

{% math() %}
\langle \nabla^2 V\rangle = -\frac{Z e^2}{4\pi\varepsilon_{0}} \int \psi_{n}^*(\mathbf{r}) \delta(\mathbf{r}) \psi_{n}(\mathbf{r}) dV = -\frac{Z e^2}{\varepsilon_{0}}|\psi_{n}(0)|^2
{% end %}

In the case of hydrogen and similar atoms, we know that the wavefunction at the origin is only nonzero for $\ell = m = 0$, for which it is given by:

{% math() %}
|\psi_{n00}(0)|^2 = \frac{1}{\pi} \left( \frac{Z}{na_{0}} \right)^3 = \frac{1}{\pi} \left( \frac{Z}{n} \frac{\alpha m_{e}c}{\hbar} \right)^3
{% end %}

Substituting this back into our expression for $\Delta E_n$, we have:

{% math() %}
\begin{align*}
\frac{\hbar^2}{2}
\langle \nabla^2 V\rangle &= -\frac{Ze^2 \hbar^2}{2 \varepsilon_{0}} |\psi_{n}(0)|^2 \\
&= -\frac{Z^4e^2 \hbar^2}{2\pi \varepsilon_{0} n^3} \left(\frac{\alpha m_{e}c}{\hbar} \right)^3 \\
&= Z^4 \hbar^2 \left( \frac{2\hbar c \alpha}{n^3} \right) \left( \frac{\alpha m_{e}c}{\hbar} \right)^3 \\
&= \frac{2Z^4 \alpha^4}{n^3} m_{e}^3 c^4
\end{align*}
{% end %}

Where it is useful to note that $\frac{e^2}{2\pi \varepsilon_{0}} = 2\hbar c \alpha$. Hence, the energy shifts are given by:

{% math() %}
\Delta E_{n} = \frac{2\alpha}{3\pi m_{e}^2 c^2} \frac{2Z^4 \alpha^4}{n^3} m_{e}c^4\ln(k_0) = \frac{4Z^4\alpha^5 m_{e}c^2}{3\pi n^3} \ln k_{0} \approx \pu{34.37 \mu eV} \cdot\frac{Z^4}{n^3}
{% end %}

For the transition $2s^{1/2} \to 2p^{1/2}$, this corresponds to a frequency of $\nu \approx \pu{1085.15 MHz}$, which is within 3% of the experimentally measured value of $\pu{1057.864 MHz}$. This is a *tiny energy difference* many orders of magnitude below that of electronic energy levels, which explains why we typically don't notice the Lamb shift. Indeed, since it depends on $\alpha^5$ it is an order of magnitude smaller than fine structure, which depends on $\alpha^4$. However, notice that the Lamb shift also grows with the fourth power of the atomic number. Hence, while the Lamb shift is an extremely tiny correction to the energy levels of the hydrogen atom and is usually negligible, it can become a *much larger* energy shift for super-heavy atoms (e.g. uranium), for which it cannot be ignored.

We will now account for the discrepancy between our theoretically-predicted transition frequency and the experimental data. This discrepancy comes as a result of several factors: first, our treatment is non-relativistic, and second, it includes only the so-called *self-energy correction*. There are two other smaller effects that contribute towards the Lamb shift, as shown below:

| Effect                    | Energy contribution |
| ------------------------- | ------------------- |
| Electron self-energy\*    | +1017 MHz           |
| Anomalous magnetic moment | +68 MHz             |
| Vacuum polarization       | -27 MHz             |
| Total                     | **+1058 MHz**       |

_Source: [LibreTexts](https://phys.libretexts.org/Bookshelves/Quantum_Mechanics/Quantum_Mechanics_(Walet)/12%3A_Quantum_Mechanics_of_the_Hydrogen_Atom/12.05%3A_Smaller_Effects/12.5.02%3A_The_Lamb_Shift)_

<small>*: Also known as "electron mass renormalization" in the quantum electrodynamics</small>

The effect of **vacuum polarization** can be described by replacing the Coulomb potential with a modified potential in the form:

{% math() %}
\begin{align*}
V(r) &= -\frac{Ze^2}{4\pi\varepsilon_{0}}\left( 1 +  \frac{4}{15} \left( \frac{e^2 \hbar^3}{4\pi \varepsilon_{0} m_{e}^2 c} \right) \delta^{(3)}(r) \right) \\
&= -\left( \frac{\alpha \hbar c}{r} + \frac{4\alpha^2 \hbar^3}{15m_{e}^2 c} \delta^{(3)}(r) \right)
\end{align*}
{% end %}

Where $\alpha$ is the fine-structure constant and $\delta^{(3)}(r)$ is the 3-dimensional Dirac delta function (for those curious, see _Quantum Field Theory for the Gifted Amateur Ch. 41.1_ for the derivation from the renormalized photon propagator). The second term in the potential can be treated as a perturbation $\Delta V$ to the potential, that is:

{% math() %}
\Delta V = -\frac{4\alpha^2 \hbar^3}{15m_{e}^2 c} \delta^{(3)}(r)
{% end %}

Using first-order perturbation theory with this as our perturbation gives us an energy shift of:

{% math() %}
\Delta E = \int \psi_{n}^*(\mathbf{r}) \Delta V \psi_{n}(\mathbf{r})dV =  -\frac{4\alpha^2 \hbar^3}{15m_{e}^2 c} |\psi(0)|^2 =-\frac{4\alpha^2 \hbar^3}{15\pi m_{e}^2 c} \left( \frac{Z}{na_{0}} \right)^3
{% end %}

Finally, the effect of the **anomalous magnetic moment** can be incorporated by replacing $g_{s} = 2$ in the spin-orbital coupling terms in the Hamiltonian with the actual value of $g_s = 2 + \frac{\alpha}{\pi} + \dots$ which is approximately $g_{s} = 2.0023193$. For those curious, this effect comes from the non-trivial terms in the QED vertex function, but that is beyond the scope of this guide. Finally, while our computation predicts that the Lamb shift is only nonzero for $s$ orbitals, we do observe a (much smaller) shift for $p$ orbitals as well; this suggests that we have to be more careful with our approximations. A detailed calculation of the Lamb shift using relativistic quantum field theory leads to a result that differs from the experimental value by under $10^{-6}$, making it one of the [most accurate predictions in all of physics](https://en.wikipedia.org/wiki/Precision_tests_of_QED).

## The variational method

Perturbation theory is all well and good for finding approximate solutions to the Schrödinger equation, but it is not perfect. This is because it *requires* an arbitrary Hamiltonian to be able to be written as the sum of a simple, analytically-solvable Hamiltonian plus a small perturbation. It no longer works if the perturbation is large, or if this decomposition is not possible!

However, this does *not* mean we are out of options! Indeed, physicists have developed a variety of other techniques to solve problems that neither perturbation theory nor exact analytical methods can handle. One of these methods is called the **variational method**. This comes from the fact that one can show that the true ground-state energy $E_0$ associated with *any* Hamiltonian $\hat H$ satisfies the following inequality:

{% math() %}
E_{0} \leq \frac{\langle \psi_{0} |\hat{H} | \psi_{0}\rangle}{\langle \psi |\psi\rangle}
{% end %}

If $|\psi_0\rangle$ normalized, that is, $|\langle \psi_0|\hat H|\psi_0\rangle|^2$, this reduces to the simplified form:

{% math() %}
E_{0} \leq \langle \psi_{0} |\hat{H} | \psi_{0}\rangle
{% end %}

If we are working in the position basis, this can be rewritten as:

{% math() %}
E_{0} \leq \frac{\displaystyle \int \psi_{0}^*(\mathbf{r}) \hat{H} \psi_{0}(\mathbf{r}) d\tau}{\displaystyle \int \psi_{0}^*(\mathbf{r}) \psi_{0}(\mathbf{r}) d\tau}
{% end %}

Where $d\tau$ is the integration element (e.g. $dx$ in 1D Cartesian coordinates, $dxdy$ in 2D Cartesian coordinates, $dx dy dz$ in 3D, $r^2 d r d\Omega$ in spherical coordinates, etc.). This reduces to the following if $\psi_0$ is normalized:

{% math() %}
E_{0} \leq \int \psi_{0}^*(\mathbf{r}) \hat{H} \psi_{0}(\mathbf{r}) d\tau
{% end %}

This immediately makes the problem of finding the ground-state wavefunctions (and energies) a *minimization problem* (or, in the language of mathematicians, a *variational problem*). What we can then do is to guess a wavefunction parameterized in terms of one or more constant parameters $\gamma$:

{% math() %}
\psi_{0}(\mathbf{r}) = \psi_{0}(\mathbf{r}; \gamma), \quad \gamma = (a, b, c, \dots, \gamma_{n})
{% end %}

Where the integral is over the entire domain over which the ground-state wavefunction is defined. To find the values of the parameters $a, b, c, \dots$ we can use a classic method from multivariable calculus. Recall that for a function of several variables, its minima are located at its **critical points**, where the first derivatives of the function are all zero. Hence, to minimize the energy of the ground state, we set the first derivatives of the ground-state wavefunctions with respect to the parameters equal to zero:

{% math() %}
\frac{\partial}{\partial (\text{params})} \left(\frac{\langle \psi_{0} |\hat{H} | \psi_{0}\rangle}{\langle \psi |\psi\rangle}\right) = 0
{% end %}

Expanding this, we can rewrite the above as:

{% math() %}
\begin{align*}
\frac{\partial \psi_{0}}{\partial a} &= 0 \\
\frac{\partial \psi_{0}}{\partial b} &= 0 \\
\frac{\partial \psi_{0}}{\partial c} &= 0 \\
\vdots &\quad \vdots \\
\frac{\partial \psi_{0}}{\partial \gamma_{n}} &= 0
\end{align*}
{% end %}

From here, we get a system of equations, which can be solved to find the values of $a, b, c, \dots$ that would *minimize* $\dfrac{\langle\psi_{0} |\hat{H} | \psi_{0}\rangle}{\langle \psi_{0}|\psi_{0}\rangle}$ (which is called the **energy functional** and which we will denote as $\varepsilon$). Once this is done, we can substitute those parameters back into $\psi_0$, which will (hopefully) have a good approximation of the ground-state energy:

{% math() %}
E_{0} \approx \varepsilon = \frac{\langle\psi_{0} |\hat{H} | \psi_{0}\rangle}{\langle \psi_{0}|\psi_{0}\rangle}
{% end %}

This technique is powerful because it does *not* rely on $\hat H$ being able to be separated into a small perturbation on top of a simpler Hamiltonian. However, the accuracy of the approximate ground-state energy obtained from the variational method may greatly vary, depending on how many parameters we put (more parameters generally makes the approximation more accurate) and how close our guess for $\psi_0$ is to the true ground-state wavefunction.

> **Note:** Typically-speaking, the variational method can only compute the ground-state wavefunction and ground-state energy of a system. However, it is possible to find (or at least) *estimate* the higher-energy states (excited states) of a system using the **Gram–Schmidt algorithm**.

### Solving the hydrogen atom by the variational method

Let us return to the hydrogen atom, whose Hamiltonian, as we saw, is given by:

{% math() %}
H = -\frac{\hbar^2}{2\mu} \nabla^2 - \frac{Ze^2}{4\pi \varepsilon_{0} r}
{% end %}

With $\mu$ being the reduced mass and $Z$ being the atomic number, and where we use $q$ for the electron's charge. We will use the variational method to attempt to approximate the ground-state energy and ground-state wavefunction of the hydrogen atom. We will rewrite this as:

{% math() %}
H = b_{1} \nabla^2 + \frac{b_{2}}{r}, \quad b_{1} = -\frac{\hbar^2}{2\mu}, \quad b_{2} = -\frac{Ze^2}{4\pi \varepsilon_{0}}
{% end %}

Next, we choose the following *ansatz* (educated guess) for the ground-state wavefunction:

{% math() %}
\psi_{0}(r) = a e^{-r /\lambda}
{% end %}

Where $a$ and $\lambda$ are unknown constants. We can justify this heuristically: we know that the wavefunction must be normalizable and that it must be well-defined for all real numbers: this suggests a function that smoothly decays to zero at infinity. Moreover, we know that it must be spherically-symmetric due to the spherical symmetry of the hydrogen atom. The above *ansatz* satisfies all the above: the $e^{-r/\lambda}$ decay ensures a smooth decay as $r \to \infty$ and is normalizable, and moreover it is only dependent on $r$, making it spherically-symmetric. In addition — and this is especially important when doing calculations by hand — it is reasonably *simple*, hence calculating the resulting integrals will be less of a nightmare. We can always add more parameters later. It is useful to note the following identities:

{% math() %}
\begin{gather*}
\frac{d}{dr} e^{-r / \lambda} = -\frac{1}{\lambda} e^{-r/\lambda}, \quad \frac{d^2}{dr^2} e^{-r / \lambda} = \frac{1}{\lambda^2} e^{-r / \lambda} \\
\nabla^2 f(r) = \frac{1}{r^2} \frac{d}{dr}\left( r^2 \frac{d f}{dr} \right) = \frac{2}{r} \frac{df}{dr} + \frac{d^2 f}{dr^2}
\end{gather*}
{% end %}

Where $f(r)$ is any spherically-symmetric function of purely the radial coordinate $r$. Substituting into the Hamiltonian, and computing the derivatives, we have:

{% math() %}
\begin{align*}
\hat H \psi_{0} &= \left[b_{1} \nabla^2 + \frac{b_{2}}{r}\right] \psi_{0}(r) \\
&= b_{1}\left( \psi_{0}'' + \frac{2}{r} \psi_{0}' \right) + \frac{b_{2}}{r} \psi_{0} \\
&= \frac{ab_{1}}{\lambda^2} e^{-r / \lambda} - \frac{2ab_{1}}{\lambda} \frac{e^{-r / \lambda}}{r} + \frac{ab_{2}}{r} e^{-r / \lambda} \\
&= a \left\{\frac{b_{1}}{\lambda^2} + \frac{1}{r} \left[ b_{2} - \frac{2b_{1}}{\lambda} \right]
\right\}e^{-r / \lambda}
\end{align*}
{% end %}

Hence, we obtain (upon integrating in spherical coordinates):

{% math() %}
\begin{align*}
\langle \psi_{0} | \hat{H} | \psi_{0} \rangle &= \int_{0}^{2\pi} \int_{0}^\pi \int_{0}^\infty \psi_{0}(r) \hat{H} \psi_{0}(r) r^2 \sin \theta dr d\theta d \phi \\
&= 4\pi \int_{0}^\infty \psi_{0}(r) \hat{H} \psi_{0}(r) r^2  dr \\
&= 4\pi a^2 \int_{0}^\infty \left\{\frac{b_{1}}{\lambda^2} + \frac{1}{r} \left[ b_{2} - \frac{2b_{1}}{\lambda} \right]
\right\}e^{-2r / \lambda} r^2 dr \\
&= \pi a^2 \left( \frac{b_{1}}{\lambda^2} \lambda^3 + \left[ b_{2} - \frac{2b_{1}}{\lambda} \right]\lambda^2 \right) \\
&=\pi a^2 (b_{1}\lambda + b_{2}\lambda^2 -2b_{1}\lambda) \\
&= \pi a^2 (b_{2}\lambda^2 - b_{1}\lambda) \\
\langle \psi_{0} | \psi_{0}\rangle &= \int_{0}^{2\pi} \int_{0}^\pi \int_{0}^\infty |\psi_{0}|^2 r^2 \sin \theta dr d\theta d\phi \\
&= 4\pi \int_{0}^\infty a^2 e^{-2r /\lambda}r^2 dr \\
&= \pi a^2 \lambda^3 \\
&= 1
\end{align*}
{% end %}

Where we used the following identities (both can be derived from integration by parts):

{% math() %}
\int_{0}^\infty re^{-2r/\lambda} dr = \frac{\lambda^2}{4}, \quad \int_{0}^\infty r^2 e^{-2r / \lambda} dr = \frac{\lambda^3}{4}
{% end %}

Thus, the energy functional $\varepsilon$ is given by:

{% math() %}
\varepsilon = \frac{\langle\psi_{0} |\hat{H} | \psi_{0}\rangle}{\langle \psi_{0}|\psi_{0}\rangle} = \frac{\pi a^2 (b_{2}\lambda^2 - b_{1}\lambda)}{\pi a^2 \lambda^3} = \frac{b_{2}}{\lambda} - \frac{b_{1}}{\lambda^2}
{% end %}

In this case, we would conventionally differentiate with respect to *both* $a$ and $\lambda$ to get our system of equations. But we are fortunate that the normalization procedure has already told us that $\pi a^2 \lambda^3 = 1$, hence $a = 1 / \sqrt{\pi \lambda^3}$. Therefore, we only need to minimize with respect to $\lambda$. Taking the derivative with respect to $\lambda$ and setting it equal to zero yields:

{% math() %}
\frac{d\varepsilon}{d\lambda} = -\frac{b_{2}}{\lambda^2} + \frac{2b_{1}}{\lambda^3} = 0
{% end %}

We can now solve for the value of $\lambda$ that satisfies the above equation, which is just a matter of some straightforward algebra. The solution is:

{% math() %}
\lambda = \frac{2 b_{1}}{b_{2}} = \frac{4\pi \varepsilon_{0} \hbar^2}{Z \mu e^2} = \frac{a_{0}^*}{Z}
{% end %}

Where $a_{0}^* = \frac{m_{e}}{\mu} a_{0}$ is the **reduced Bohr radius**, and $a_0 \approx \pu{5.29 * 10^{-11} m}$ is the Bohr radius, as we saw in the derivation of the hydrogen atom. Thus we find that $\lambda = a_0^* / Z$, the Bohr radius, while $a = 1/\sqrt{\pi \lambda^3}$. Substituting back into our ansatz $\psi_{0}(r) = a e^{-r /\lambda}$ gives us a ground-state wavefunction of:

{% math() %}
\psi_{0} = \frac{1}{\sqrt{ \pi }} \left( \frac{Z}{a_{0}^*} \right)^{3/2} e^{-Zr / a_{0}^*}
{% end %}

This is actually the **exact ground-state wavefunction** of hydrogen! Thus, using the variational method, we were able to derive the ground-state wavefunction *without* needing to solve complicated differential equations. In addition, if we substitute our parameters into the energy functional, we get an estimated ground-state energy of:

{% math() %}
\begin{align*}
\varepsilon &= \frac{b_{2}}{\lambda} - \frac{b_{1}}{\lambda^2}
\\
&= -Z^2\left( \frac{e^2}{4\pi \varepsilon_{0} a_{0}^*} + \frac{\hbar^2}{2\mu {a_{0}^*}^2} \right), \quad a_{0}^*= \frac{4\pi \varepsilon_{0} \hbar^2}{\mu e^2} \\
&= -\frac{Z^2 \mu e^4}{32\pi^2 \varepsilon_{0}^2 \hbar^2} \\
& \approx -(\pu{13.6 eV})Z^2
\end{align*}
{% end %}

We know this is indeed the correct ground-state energy of hydrogen! In this particular case, we got lucky, since our *ansatz* happened to exactly match the hydrogen ground-state wavefunction and hence the variational method gave us an exact answer. Usually, we'll end up with an *approximate answer* instead of an exact one, albeit an answer that is "good enough" to approximate the ground-state energy pretty well.

### Solving the helium atom by the variational method

As we mentioned earlier in the guide, the solution for the hydrogen atom is only valid for atoms with a single electron. While it can approximately describe multi-electron atoms, its predicted energy levels are not very accurate. This is because our treatment does not include a variety of effects in multi-electron atoms that affect the total energy:

- **Nuclear screening**, which comes from the inner electrons forming a negatively-charged "cloud" around the nucleus
- **Electron correlation**, which comes from inter-electron interactions within the atom, due to their electrostatic repulsion
- The **exchange interaction**, which comes from the Pauli exclusion principle that forbids electrons from sharing the same quantum state, causing electron-electron repulsion

The next-simplest atom after hydrogen is the **helium atom**, composed of 2 protons, (usually) 2 neutrons, and 2 electrons. The solution for the hydrogen atom can easily be generalized to helium by setting $Z = 2$. This would give us a predicted ground-state energy of:

{% math() %}
E_\mathrm{predicted} = -\pu{54.4228 eV}
{% end %}

Unfortunately, this is quite a bit off from the experimental value, and the reason is because the helium Hamiltonian has a different form from the hydrogen Hamiltonian. In particular, the helium Hamiltonian (disregarding spin and fine/hyperfine-structure corrections) is given by:

{% math() %}
\hat H = \underbrace{-\dfrac{\hbar^2}{2\mu}(\nabla_1^2 + \nabla_2^2)}_\text{electron kinetic energy} -\underbrace{\dfrac{Z}{4\pi \varepsilon_0}\left(\dfrac{e^2}{|\mathbf{r}_1|} + \dfrac{e^2}{|\mathbf{r}_2|}\right)}_\text{nucleus-electron attraction} + \underbrace{\dfrac{1}{4\pi \varepsilon_0}\dfrac{e^2}{|\mathbf{r}_1 - \mathbf{r}_2|}}_\text{electron-electron repulsion}
{% end %}

Where $Z = 2$ (since helium has two protons), $\mathbf{r}_1 = (r_{1}, \theta_{1}, \phi_{1})$ and $\mathbf{r}_2 = (r_{2}, \theta_{2}, \phi_{2})$ are the position coordinates for each of the two electrons and $\nabla_1^2, \nabla_2^2$ are respectively the Laplacians with respect to the coordinates $\mathbf{r}_1$ and $\mathbf{r}_2$. The first 4 terms in the helium Hamiltonian are more or less familiar: they are just the kinetic and potential terms for the first and second electron in helium. However, it is the *last term* that matters to us. This is the **electron correlation term** and it means that *no analytical solution* can be found for helium. Hence, we must tackle the problem using variational techniques.

To start, we choose the following *ansatz* for the ground-state wavefunction with two parameters, $Z_e$ and $\lambda$:

{% math() %}
\psi_{0}(\mathbf{r}_{1}, \mathbf{r}_{2}) = \frac{Z_{e}^3}{\pi \lambda^3} e^{-Z_{e}(r_{1} + r_{2}) / \lambda}
{% end %}

This is similar with our *ansatz* for the hydrogen atom ($\psi_{0}(r) = a e^{-r /\lambda}$, where we found that $a = \sqrt{\pi \lambda^3}$ and $\lambda = a_0^*/Z$). In fact, it is *almost* equal to the product of two hydrogen ground-state wavefunctions, with the exception of replacing $Z$ by $Z_e$, which represents an *effective nuclear charge*. We would expect that the negatively-charged electrons would counter the positive charge of the nucleus, resulting in a lower effective nuclear charge $Z_{e} < Z$ (in the case of helium specifically, this reduces to $Z_e < 2$).

Now, we can begin the variational procedure. First, we need to compute $\hat H \psi_{0}$. This becomes more complicated due to the electron correlation term, which is the magnitude of a difference of vectors; hence we must rewrite it in explicitly terms of coordinates. For this, we can use the well-known identity (which comes from the law of cosines):

{% math() %}
|\mathbf{r}_1 - \mathbf{r}_2| = \sqrt{ r_{1}^2 + r_{2}^2 + 2 r_{1}r_{2} \cos \theta_{2} }
{% end %}

It is also useful to use the following identity when computing the Laplacians $\nabla_1^2, \nabla_2^2$:

{% math() %}
\nabla_{i}^2 \psi(r) = \frac{2}{r} \frac{d\psi}{dr_{i}} + \frac{d^2 \psi}{dr_{i}^2}
{% end %}

Hence we have:

{% math() %}
\nabla_1^2 \psi(r) = \frac{2}{r} \frac{d\psi}{dr_{1}} + \frac{d^2 \psi}{dr_{1}^2}, \quad \nabla_{2}^2 \psi(r) = \frac{2}{r} \frac{d\psi}{dr_{2}} + \frac{d^2 \psi}{dr_{2}^2}
{% end %}

It is recommended to perform the remainder of the calculation with a computer algebra system such as Maple, Mathematica, or SymPy as the calculations get quite involved: we will state just the general steps. However, while tedious, the math is just a combination of differentiation, integration, and algebra. There will be no need to solve differential equations or eigenvalue equations. This is part of the beauty of the variational method: it allows you to find the ground-state wavefunction and energy by performing a series of *explicit steps*, removing the guesswork from the problem (as long as you have already come up with an *ansatz*). Just substitute everything into the helium Hamiltonian, which will give you (after some simplifications and moving terms around) the following:

{% math() %}
\begin{align*}
\hat{H} \psi_{0} &= \underbrace{ \left[-\frac{\hbar^2}{2\mu}(\nabla_{1}^2 + \nabla_{2}^2 ) - \frac{e^2}{4\pi \varepsilon_{0}}\left( \frac{Z_{e}}{r_{1}} + \frac{Z_{e}}{r_{2}} \right)\right] \psi_{0} }_{\hat{H}_{1}} \\
&\qquad + \underbrace{ \frac{e^2}{4\pi\varepsilon_{0}}\left[ \frac{Z_{e} - Z}{r_{1}} + \frac{Z_{e} - Z}{r_{2}}\right] \psi_{0} }_{\hat{H}_{2}} + \underbrace{ \frac{e^2}{4\pi\varepsilon_{0}} \frac{1}{|\mathbf{r}_{1} - \mathbf{r}_{2}|} \psi_{0} }_{\hat{H}_{3}}
\end{align*}
{% end %}

Notice how we have written the Hamiltonian as a sum of three distinct terms: this will be important shortly. Next, we'll compute $\langle \psi_0 |\hat H|\psi_0\rangle$. We could brute-force it by plugging everything into the formula, but there is a clever and faster way. Notice that the Hamiltonian is *linear* in $\psi_{0}$ and has three terms; hence its eigenvalue equation can also be written in the following three-term form:

{% math() %}
\langle \psi_{0}|\hat{H} |\psi_{0}\rangle = (\hat{H}_{1} + \hat{H}_{2} + \hat{H}_{3})|\psi_{0}\rangle = (A E_\mathrm{hydrogen} + E_\mathrm{screening} + E_\mathrm{correlation})|\psi_{0}\rangle
{% end %}

Where $E_\mathrm{hydrogen} = -\pu{13.6 eV}$ is the ground-state energy of hydrogen and $A$ is a to-be-determined constant; the reasoning for the energies will be explained shortly. If we take the inner product with $\langle \psi_{0}|$ we get:

{% math() %}
\begin{align*}
\langle \psi_{0} | \hat{H}_{1} | \psi_{0}\rangle &= A E_\mathrm{hydrogen} \\
\langle \psi_{0} | \hat{H}_{2} | \psi_{0}\rangle &= E_\mathrm{screening} \\
\langle \psi_{0} | \hat{H}_{3} | \psi_{0}\rangle &= E_\mathrm{correlation} \\
\end{align*}
{% end %}

This gives us the three following equations, upon expanding the inner product:

{% math() %}
\begin{align*}
\int \psi_{0}\left[-\frac{\hbar^2}{2\mu}(\nabla_{1}^2 + \nabla_{2}^2 ) - \frac{e^2}{4\pi \varepsilon_{0}}\left( \frac{Z_{e}}{r_{1}} + \frac{Z_{e}}{r_{2}} \right)\right] \psi_{0}\,dV_{1} dV_{2} &= A E_\mathrm{hydrogen} \\
\int \psi_{0}\frac{e^2}{4\pi\varepsilon_{0}}\left[ \frac{Z_{e} - Z}{r_{1}} + \frac{Z_{e} - Z}{r_{2}}\right] \psi_{0}\, dV_{1} dV_{2} &= E_\mathrm{screening}  \\
\int \psi_{0}\frac{e^2}{4\pi \varepsilon_{0}} \frac{1}{|\mathbf{r}_{1} - \mathbf{r}_{2}|} \psi_{0}\, dV_{1} dV_{2} &= E_\mathrm{correlation}
\end{align*}
{% end %}

(Where $dV_i = r_i^2 dr_i d\theta_i d\phi_i$ and we integrate over a 6-dimensional domain for all $r_1, r_2, \theta_1, \theta_2, \phi_1, \phi_2$) We observe that the first equation is effectively two "copies" of the hydrogen Hamiltonian (except with respect to different coordinates, and with $Z$ replaced by $Z_e$). Hence, the energy eigenvalue must be *twice* that predicted by the ground-state energy formula for hydrogen (which is given by $E_0 = -Z^2 \cdot \pu{13.6 eV}$; here we'll have to replace $Z$ with $Z_e$). That is to say:

{% math() %}
AE_\mathrm{hydrogen} = 2 \cdot(-Z_{e}^2 \cdot \pu{13.6 eV}) = 2Z_{e}^2 \cdot E_\mathrm{hydrogen} \implies A = -2Z_{e}^2
{% end %}

Hence, we have:

{% math() %}
\langle \psi_{0} | \hat{H}_{1} | \psi_{0}\rangle = 2Z_{e}^2 E_\mathrm{hydrogen}
{% end %}

For the second term, we will now evaluate the integral:

{% math() %}
\begin{align*}
E_\mathrm{screening} &=
\frac{e^2}{4\pi\varepsilon_{0}}\int \psi_{0}\left[ \frac{Z_{e} - Z}{r_{1}} + \frac{Z_{e} - Z}{r_{2}}\right] \psi_{0}\, dV_{1} dV_{2} \\
&= \frac{e^2}{4\pi\varepsilon_{0}} \left( \frac{Z_{e}^3}{\pi \lambda^3} \right)^2
\int_{0}^{2\pi} \int_{0}^\pi \int_{0}^\infty\int_{0}^{2\pi} \int_{0}^\pi \int_{0}^\infty e^{-2Z_{e}(r_{1} + r_{2}) / \lambda} \\
&\qquad \times \left[ \frac{Z_{e} - Z}{r_{1}} + \frac{Z_{e} - Z}{r_{2}}\right] r_{1}^2 \sin \theta_{1} d\theta_{1} d\phi_{1} ~ r_{2}^2 \sin \theta_{2} d\theta_{2} d\phi_{2}
\end{align*}
{% end %}

What looks like a horrible integral is made immediately-easier by spherical symmetry, meaning that:

{% math() %}
\int_{0}^{2\pi} \int_{0}^\pi \sin \theta_{1} d \theta_{1} d\phi_{1} = \int_{0}^{2\pi} \int_{0}^\pi \sin \theta_{2} d \theta_{2} d\phi_{2} = 4\pi
{% end %}

Hence, four of the six integrals reduce down to a factor of $(4\pi)^2$, giving us:

{% math() %}
\begin{align*}
E_\mathrm{screening} &= \frac{e^2}{4\pi\varepsilon_{0}} \left( \frac{Z_{e}^3}{\pi \lambda^3} \right)^2(4\pi)^2 \int_{0}^\infty \left[ \frac{Z_{e} - Z}{r_{1}} + \frac{Z_{e} - Z}{r_{2}}\right]e^{-2Z_{e}(r_{1} + r_{2}) / \lambda}r_{1}^2 dr_{1} r_{2}^2 dr_{2} \\
&= \frac{e^2}{4\pi\varepsilon_{0}} \left( \frac{Z_{e}^3}{\pi \lambda^3} \right)^2(4\pi)^2 \int_{0}^\infty \left( r_{1}(Z_{e} - Z) r_{2}^2 + r_{2}(Z_{e} - Z) r_{1}^2 \right) e^{-2Z_{e}(r_{1} + r_{2}) / \lambda} dr_{1} dr_{2} \\
&= 2(Z_{e} - Z)\left( \frac{Z_{e}e^2}{4\pi \varepsilon_{0} \lambda} \right), \quad \lambda = a_{0}^*
\end{align*}
{% end %}

Which can be written in terms of $E_\mathrm{hydrogen}$ as:

{% math() %}
E_\mathrm{screening} =-4Z_{e}(Z_{e} - Z) E_\mathrm{hydrogen}
{% end %}

The final (and most challenging) integral to perform is the third term, which, unlike the others, *does* have angular dependence. It is given by:

{% math() %}
\begin{align*}
E_\mathrm{correlation} &= \int \psi_{0}\frac{e^2}{4\pi \varepsilon_{0}} \frac{1}{|\mathbf{r}_{1} - \mathbf{r}_{2}|} \psi_{0}\, dV_{1} dV_{2} \\
&= \frac{e^2}{4\pi \varepsilon_{0}} \left(\frac{Z_{e}^3}{\pi \lambda^3} \right)^2 \int \frac{e^{-Z_{e}(r_{1} + r_{2}) / \lambda}}{\sqrt{ r_{1}^2 + r_{2}^2 + 2 r_{1}r_{2} \cos \theta_{2} }} dV_{1} dV_{2} \\
&= \frac{5Z_{e}}{8a_{0}^*} \left( \frac{e^2}{4\pi \varepsilon_{0}} \right) \\
&= -\frac{5Z_{e}}{4} E_\mathrm{hydrogen}
\end{align*}
{% end %}

Therefore, putting all the terms together, we obtain:

{% math() %}
\begin{align*}
\langle \psi_{0}|\hat{H} |\psi_{0}\rangle  &= A E_\mathrm{hydrogen} + E_\mathrm{screening} + E_\mathrm{correlation} \\
&= \left( 2Z_{e}^2 - 4Z_{e}(Z_{e} - Z) - \frac{5}{4}Z_{e} \right) E_\mathrm{hydrogen} \\
&= \left[ -2Z_{e}^2 +\left( 4Z - \frac{5}{4} \right)Z_{e} \right]E_\mathrm{hydrogen}
\end{align*}
{% end %}

Now, all that's left to do is to minimize this functional! This gives us:

{% math() %}
\frac{d}{dZ_{e}} = -4 Z_{e} + \left( 4Z - \frac{5}{4} \right) = 0
{% end %}

Substituting in $Z = 2$ for helium, we obtain:

{% math() %}
-4Z_{e} + 8 - \frac{5}{4} = 0 \implies Z_{e} = \frac{27}{16} \approx 1.69
{% end %}

Finally, substituting back this value of $Z_e$ into $\langle \psi_0 | \hat H| \psi_0\rangle$, we obtain:

{% math() %}
E_{0} \approx \langle \psi_{0}|\hat{H}|\psi_{0}\rangle \approx 5.7E_\mathrm{hydrogen} \approx -\pu{77.5 eV}
{% end %}

 This value is in extremely good agreement with the experimental value of the helium ground state energy of $\pu{-78.975 eV}$ and illustrates how powerful the variational method can be.

### Solving the screened Coulomb potential by the variational method

While solving the helium atom using the variational approach we mentioned the importance of *nuclear screening*. In particular, nuclear screening has the effect of reducing the nuclear charge $Z$ (the charge of the atomic nucleus). It can be modelled by modifying the Coulomb potential slightly to the following form (called the **screened Coulomb potential**):

{% math() %}
V(r) \to -\frac{Ze^2}{4\pi\varepsilon_{0 }r} e^{-\alpha r}
{% end %}

Where $\alpha$ is a constant and is the inverse of the characteristic length scale at which screening occurs (if there is no screening, $\alpha = \infty$). This is a potential which *cannot* be solved exactly *and* cannot be easily treated with perturbation theory, hence this is a perfect opportunity to make use of the variational method. The reader is encouraged to work this problem out by themselves, but here's a hint: use the following *ansatz* for the screened ground-state wavefunction:

{% math() %}
\psi_{0} = f(r) e^{-r / \lambda}, \quad f(r) = \frac{1 - e^{-a r}}{r}
{% end %}

Where $a, \lambda$ are our two parameters. Why choose this *ansatz*? Well, it is just a guess, but it is an educated guess. First of all, our guess reduces to the $\psi_0 = a$ as $r \to 0$ (you can show this via L'Hôpital's rule), just like the solution for the normal (unscreened) hydrogen ground state. The net effect of the screening, however, is to reduce the effect of the nuclear charge at larger distances from the nucleus, hence $f(r)$ would need to be a smoothly-decaying function, and our chosen form of $f(r)$ also satisfies this criterion.

The detailed solutions are available [on this paper](https://inspirehep.net/files/47754796bfedebbea305a6c09a975ed0), but we will simply state the approximate energy levels for the screened Coulomb potential, which are given by:

{% math() %}
E_{n\ell m}^\mathrm{(screened)} = -\frac{\hbar^2 \alpha^2}{2\mu}\left( \frac{\mu V_{0} / (\hbar^2\alpha) - (n + \ell + 1)^2}{n + \ell + 1} \right)^2
{% end %}

Where $V_0 = Ze^2/(4\pi \varepsilon_{0})$, $\mu$ is the reduced mass, and $\alpha$ is the same as in the screened potential; it has units of inverse length and has a value of $\approx \pu{0.2 fm^{-1}}$ (the paper uses $\hbar = 1$ units; we have converted the formula to SI units). Note that here $n$ is **not** the same as the usual principal quantum number $n$ (which we instead denote as $n'$, where $n' = n + \ell + 1$). From this formula, we obtain the following expression for the approximate ground-state ($n' = 1$) energy, which should be what you got (or close to what you got) by solving via the variational method:

{% math() %}
E_{0} \approx -\frac{\hbar^2 \alpha^2}{2\mu}\left( \frac{\mu V_{0}}{\hbar^2\alpha} - 1 \right)^2
{% end %}

In the limit $\alpha \to \infty$ (that is, in the limit where the nucleus has zero screening) we recover the ground-state energy of the hydrogen atom:

{% math() %}
E_{0} \to -\frac{\mu V_{0}^2}{2\hbar^2} = -\frac{\mu e^4}{32 \pi^2 \varepsilon_{0}^2 \hbar^2} \approx -\pu{13.6 eV}
{% end %}

### Computational techniques using the variational method

Manually calculating using the variational method can be very hit-and-miss and require tedious calculations. This is where it is useful to solve problems using a *numerical* implementation of the variational method to run on a computer, which can be far faster than doing it by hand.

In the computational implementation of the variational method, we write the ground-state wavefunction as a sum of orthonormal basis functions $\phi_i(\mathbf{r})$ multiplied by various coefficients $c_i$:

{% math() %}
\psi_{0}(\mathbf{r}) = \sum_{i} c_{i} \phi_{i} (\mathbf{r})
{% end %}

Since the basis functions are a complete orthonormal basis, the above series can represent an *arbitrary* ground-state wavefunction. A common choice of basis is a **Gaussian basis function** in the form $\phi_{n \ell m} = x^n y^m z^\ell e^{-\alpha r^2}$ though other basis functions can also be used. The energy functional $\varepsilon$ is then given by:

{% math() %}
\varepsilon[\mathbf{r}, c_{i}]  = \frac{\displaystyle \int_{\Omega} \psi_{0} \hat{H} \psi_{0} d\tau}{\displaystyle \int_{\Omega} \psi_{0}^* \psi d\tau}
{% end %}

Where we integrate over a chosen domain $\Omega$ and where (as mentioned) $\psi_0$ is a linear combination of basis functions. These multidimensional integrals are often computed using the **Monte Carlo algorithm**, hence this method is frequently called [Variational Monte Carlo](https://en.wikipedia.org/wiki/Variational_Monte_Carlo). Then, the variational method gives:

{% math() %}
\frac{\partial \varepsilon}{\partial c_{i}} = 0
{% end %}

The Variational Monte-Carlo method can yield extremely accurate estimations of the ground-state wavefunction and energy of complicated quantum systems that cannot be tackled perturbatively. Moreover, it can be more efficient than discretizing the Hamiltonian on a computer and solving it as an eigenvalue problem, which requires exponentially longer time and computing power for quantum systems with many degrees of freedom (a major problem for quantum chemistry). Readers interested in learning more can consult [this blog article](https://adambaskerville.github.io/posts/Variational-Method-Hydrogen/) on computational implementations based on the variational method.

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
