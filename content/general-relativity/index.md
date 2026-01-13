+++
title = "Fundamentals of General Relativity"
date = 2026-01-13
+++

This is a guide to the fundamentals of General Relativity and its applications in astrophysics and cosmology. Topics covered (or will be covered) include the equivalence principle, the concept of a geodesic, the metric tensor, the Einstein Field Equations, and a study of black holes as well as relativistic cosmology.

<!-- more -->

I thank [Professor Giedt](https://faculty.rpi.edu/joel-giedt) at Rensselaer Polytechnic for teaching the GR course that made this guide possible.

## Mathematical prerequisites

This guide presumes strong knowledge of vector calculus, basic linear algebra, differential equations, electromagnetism, and classical mechanics (including Lagrangian and Hamiltonian mechanics). If any of them are unfamiliar to you, consult the below guides to learn/review these topics:

- For a review of calculus (in particular multivariable and vector calculus), see the [calculus series](@/calculus-series.md)
- For a review of basic differential equations, see the [introductory differential equations guide](@/differential-equations/index.md)
- For a review of electromagnetic theory, see the [fundamentals of electromagnetism guide](@/electromagnetism/index.md) as well as the [in-depth electromagnetism guide](@/classical-electromagnetism/index.md)
- For a review of partial differential equations, boundary-value problems, and Fourier series, and see the [PDEs guide](@/intro-pdes/index.md)
- For a review of special relativity and tensors, see the [advanced classical mechanics guide](@/advanced-classical-mech/index.md)
- For an **optional** review of quantum mechanics, see the [introductory quantum mechanics guide](@/intro-quantum-phys.md) as well as the [in-depth quantum mechanics guide](@/quantum-mechanics/index.md). There _might_ be a brief discussion on quantum gravity at the very end of this guide.

## An introduction to General Relativity

General Relativity (GR) is fundamentally a theory about gravity. More precisely it is a *geometric* theory of gravity. Even more precisely it is a *geometric theory of gravity based on the equivalence principle*. Ah, we are getting too far of ourselves here; but the point is that GR is a very complicated theory that *doesn't* make sense.

Which is a shame, because GR predicts fascinating phenomena: black holes, wormholes, the slowing of time by gravity, the beautiful bending of light by galaxies and stars, and so, so much more. And GR describes how our Universe evolves at the largest scales, telling us both about the Universe's past and its present, and even its future. It is mystical, beautiful, and perplexing at the same time. I hope that after reading to the end of this guide, this will be the impression that GR leaves on you.

![A picture taken by the Hubble space telescope, showing the phenomenon of gravitational lensing](https://upload.wikimedia.org/wikipedia/commons/1/11/A_Horseshoe_Einstein_Ring_from_Hubble.JPG)


_Gravitational lensing by the galaxy LRG 3-757, taken by the Hubble Space Telescope. Source: [Wikipedia](https://commons.wikimedia.org/wiki/File:A_Horseshoe_Einstein_Ring_from_Hubble.JPG)_

### The Newtonian and GR regimes

General relativity is the most precise theory of gravity ever created - and indeed, it still is to this day, over a hundred years since it was first proposed. However, the precision of the theory is often not needed. Indeed, we are frequently able to describe gravitational phenomena using the Newtonian theory, which is sufficiently accurate for almost all applications in everyday life, from calculating ballistic trajectories to spacecraft orbits to even simulating the dynamics of galaxies.

It is only in cases of extremely strong gravitational fields and extreme astronomical events, such as around black holes, neutron stars, or binary black-hole/neutron-star mergers that general relativity plays a major role in gravitational interactions. We therefore can distinguish between two physical regimes: the **Newtonian regime**, comprising of all physical systems that can be adequately described by Newtonian gravity, and the **GR regime**, where Newtonian gravity becomes insufficient and general-relativistic effects dominate. Indeed, we may quantify when exactly general-relativistic effects matter by considering the dimensionless quantity $\phi_{GR}$, defined as:

{% math() %}
\phi_{GR} = \frac{2GM}{c^2 R}
{% end %}

When $\phi_{GR} > 1$, the effects of GR become evident and we are in the _GR regime_, whereas for $\phi_{GR} \ll 1$ the effects of GR are negligible and we are in the _Newtonian regime_. But note that since $\phi_{GR} \sim M$, $M$ must be very, very large for $\phi_{GR}$ to be larger than 1. Indeed, even for the Sun, which has a mass on the order of $\pu{10^{30} kg}$, we find that $\phi_{GR} \sim 10^{-8}$, meaning that the GR corrections to the predictions of Newtonian gravity are very, very small. It is only for supermassive black holes and similar ultra-massive (or ultra-dense) astronomical bodies that $\phi_{GR} \gg 1$, and general relativity becomes essential.

> **Note:** Physically, $\phi_{GR}$ is equal to the Newtonian gravitational potential $\Phi$ divided by the speed of light. How this quantity is constructed will be something we'll discuss later.

### Review of relativistic physics and Newtonian gravity

Most theories of physics grew out of a desire to explain phenomena that could not be described (or contradicted) prior theories; general relativity is no different. Indeed, to understand how GR arose, we must first take a look at the two theories that GR supersedes: **special relativity** and **Newtonian gravity**.

To start, special relativity is fundamentally a theory about how our conventional understanding of "space" and "time" is incorrect. This is a result of the fundamental postulate of special relativity: physical interactions **cannot propagate faster** than the speed of light, which we denote as $c$. Even more strangely, no matter how fast you are moving, you will always see light traveling at the *exact same speed* of $c$. For the laws of physics to be consistent (that is, to avoid any paradoxes), the result is that we find that time and space become *relative* concepts. Instead, a new concept of **spacetime** must be devised that supersedes our old notions of space and time. We find that spacetime can mathematically be described using the tools of [differential geometry](https://en.wikipedia.org/wiki/Differential_geometry), and thus special relativity is, in some sense, a geometric theory. However, most special relativistic calculations end up using only algebra (with a sprinkling of some calculus), turning away from a full differential geometry based approach.

Now, let us take a look at Newtonian gravity. Newtonian gravity is the classical (as in non-relativistic) theory of gravity, which is formulated in the laws of **Newtonian mechanics**. The heart of Newtonian gravity is the principle of **universal gravitation**. The principle can be stated as follows:

1. All masses in the Universe attract each other by the **force of gravity**
2. The gravitational force is **instantaneous**, regardless of the distance separating any two masses, and has **infinite range**

To state the first principle more precisely, the gravitational force exerted by mass $m_1$ at position $\mathbf{r}_1$ on some other mass $m_2$ at another position $\mathbf{r}_2$ is given by:

{% math() %}
\mathbf{F}_{12} = -Gm_{1}m_{2} \frac{\mathbf{r}_{2} - \mathbf{r}_{1}}{|\mathbf{r}_{2} - \mathbf{r}_{1}|^3}
{% end %}

In principle, we can use this equation, along with Newton's second law {% inlmath() %}m \ddot{\mathbf{r}}_i = \sum \mathbf{F}_{ij}{% end %}, to precisely calculate the future positions and velocities of $n$ particles interacting gravitationally with each other. (In practice this is actually quite a difficult problem and requires powerful computers to solve adequately). However, the general idea holds: in Newton's theory **gravity is an instantaneous force**, meaning that Newtonian gravity (wrongly) predicts that gravitational interactions can travel faster than the speed of light, breaking special relativity! 

For instance, Newtonian gravity predicts that a star 100 light years away would gravitationally act on Earth just as fast as our Sun, which would act just as fast as the Moon, and so forth. This idea does not hold up to experimental evidence, which can be demonstrated with a very similar thought experiment: in telescope images we have of distant galaxies, the vast majority of stars are long dead, but their light, emitted hundreds or even thousands of years ago, can still be seen. But if their gravitational influence was instant (as Newtonian gravity claims) while their light was not (as special relativity claims), then we would observe gravitational effects from the dead stars while their light had not yet reached us - "ghosts" that invisibly act across astronomical distances without any visible indication they actually exist. Clearly, this does not happen!

> **Note:** Here, I am not discussing dark matter; I am just discussing *regular matter* as an illustrative example of where special relativity and Newtonian gravity contradict each other.

In discussing special relativity and Newtonian gravity, the key takeaway is this: these two theories of physics are **fundamentally incompatible** with each other. Special relativity says that physical interactions can propagate at a *maximum speed* of $c$, but Newtonian relativity says that gravity is an *instantaneous force*. To resolve this conflict, we need **general relativity**.

### The analogue with electromagnetism

To try to have a basic intuitive understanding of how Newtonian gravity must be modified to incorporate the postulates of special relativity, we can consider the theory of **electromagnetism**. Electromagnetism and gravity are remarkably similar in many ways; both are long-range interactions (having theoretically infinite distance) and both follow inverse-square laws (Coulomb's law for electromagnetism and Newton's law for gravity). They are also highly *evident* because unlike the other fundamental interactions of nature (the strong and weak nuclear interactions), we see the effects of gravity and electromagnetism every day, in the forms of falling objects, bright flashes of light, and falling objects that cause bright flashes of light and tend to kill dinosaurs. Okay, maybe not the last one. But the point still stands: both are interactions we can *experience*, and this similarity can be used as an analogy to give us clues about the nature of gravity.

Historically, the development of electromagnetism originated in the study of **electrostatics**. Electrostatics governs the behavior of electric fields and electric charges that are *slow-moving*, and is the origin for **Coulomb's law**. In its original form, Coulomb's law describes the force between two point charges with charges $q_{1}, q_{2}$ and at locations {% inlmath() %}\mathbf{r}_{1}, \mathbf{r}_{2}{% end %} as follows:

{% math() %}
\mathbf{F}_{12} = \frac{q_{1} q_{2}}{4 \pi \varepsilon_{0}} \frac{\mathbf{r}_{2} - \mathbf{r}_{1}}{|\mathbf{r}_{2} - \mathbf{r}_{1}|^3}
{% end %}

Note how similar Coulomb's law is to Newton's law of universal gravitation. In modern physics, it is conventional to write out Coulomb's law not in its force form, but rather in the potential form using the electric scalar potential $V$, that is:

{% math() %}
\ddot{\mathbf{r}} = -\frac{q}{m}\nabla V
{% end %}

Where the electric scalar potential takes the following form:

{% math() %}
V(\mathbf{r}) = \sum_{i} \frac{q_i}{4 \pi \varepsilon_{0}} \frac{1}{|\mathbf{r}_i - \mathbf{r}|}
{% end %}

And the **electric field** takes the form:

{% math() %}
\mathbf{E} = -\nabla  V
{% end %}

Coulomb's law is a good *approximation* for time-independent electric fields and charges moving slowly, but fails to apply once charges are moving close to the speed of light, or if the electric field is time-dependent. One finds that it is actually necessary to define another potential - the **magnetic vector potential** $\mathbf{A}$ - to describe the particle adequately. But wait, that's not all! We also find that for **Lorentz invariance** - that is, for the speed of light to be constant for all observers - we need to "package" the scalar potential and vector potential together into a new 4-dimensional potential, denoted as $A^\mu$ (I'll explain what this notation means soon). This 4-dimensional vector, also called a _4-vector_, looks like this:

{% math() %}
A^{\mu} = \left( \frac{V}{c}, \mathbf{A} \right) = \begin{pmatrix}
V / c \\
A_{x} \\
A_{y} \\
A_{z}
\end{pmatrix}
{% end %}

Indeed, we find that this 4-vector is what is necessary to *accurately* describe the electromagnetic field in the most general (relativistic and time-dependent) case. The evolution of this 4-vector is then given by the **Maxwell equations**, which, when written using Einstein's notation, are given by $\partial^\nu \partial_\nu A^\mu = \mu_0 J^\nu$. This generalization of the laws of non-relativistic electromagnetism is called **relativistic electrodynamics**, and permits classical electromagnetism to be fully consistent with relativity.

In the same idea, general relativity is a theory that takes Newtonian gravity and changes it - radically so - to be consistent with special relativity. Just like in electromagnetism, where the electric scalar potential $V$ had to be replaced by the four-dimensional potential $A^\mu$, in general relativity, the Newtonian gravitational potential $\Phi$ must be replaced by a **tensor potential** in GR, and is written as $g_{\mu \nu}$ (for now, think of a tensor as a "matrix"; more on that later). Since $g_{\mu \nu}$ has 10 independent components, this tensor potential can be thought of as a collection of 10 different potentials that are coupled with each other in a very complicated way. Indeed, if we write out $g_{\mu \nu}$ in matrix form, we have:

{% math() %}
g_{\mu \nu}(\mathbf{r}, t) = \begin{pmatrix}
g_{00} & g_{01} & g_{02} & g_{03} \\
g_{10} & g_{11} & g_{12} & g_{13} \\
g_{20} & g_{21} & g_{22} & g_{23} \\
g_{30} & g_{31} & g_{32} & g_{33}
\end{pmatrix}
{% end %}

In this form, we can see that unlike $A^\mu$ for electromagnetism, which has "only" 4 components, $g_{\mu \nu}$ has 16 components(!) (although only 10 components are independent since $g_{\mu \nu}$ is symmetric). Each component is a sort of "potential" that depends on space and time, and interacts with the other components, which are also "potentials" (roughly-speaking). Crucially, just like $A^\mu$ for electromagnetism, $g_{\mu \nu}$ is **Lorentz invariant**, meaning that it ensures the speed of light is constant. Thus, we have now generalized gravity in a manner that is consistent with the  

We'll see that in the Newtonian limit (weak gravity and slow-moving objects), $g_{00} = -\left( 1 + \dfrac{2\Phi}{c^2} \right)$ becomes the dominant component of the field and most of the other components can be more or less ignored. However, in the ultra-relativistic case, and whenever there is strong gravity, we need to consider *all* the components of $g_{\mu \nu}$ to describe gravity - effectively, we need to consider 10 different potentials!

Indeed, this is where GR and electromagnetism become very different, because unlike Maxwell's equations for EM, which are a system of linear PDEs, the fundamental equations of GR (the Einstein Field Equations) are a system of highly-nonlinear PDEs. Solving them is so difficult that finding an exact solution for [non-trivial cases](https://en.wikipedia.org/wiki/Kerr_metric) can give you [everlasting fame and glory](https://www.nzherald.co.nz/nz/canterbury-professor-first-kiwi-to-receive-einstein-medal/FNPXFRNJD77VSHLMTWI2YNJ4SY/) in the astrophysics community.

### Einstein's dilemma with rotating reference frames

General relativity also fixes another, less-evident issue with Newtonian gravity. Since Newtonian gravity comes from Newtonian mechanics, it comes along with all of its problems as well. In particular, accelerating reference frames are a famously-annoying issue in Newtonian gravity. As a demonstration, imagine you were standing aboard a bus that was moving forwards with some constant speed $v$. That is, until the bus rapidly brakes and comes to a stop. At that moment, you feel a "force" pushing on you (and might embarrassingly fall and drop all your things onto the floor). However, there is *no such force* - you are perfectly stationary with respect to the bus (unless you fall, but that's another thing altogether). So what was pushing on you, then? It was a **fictitious force** caused by the bus's acceleration. While you were stationary with respect to the bus, the bus was accelerating (more precisely, _decelerating_), and thus you feel the effect of that acceleration. To be more precise, you were present within a **accelerating reference frame**, and this led to your unfortunate experience of (possibly) falling.

Indeed, we could go with a much more complicated scenario. Try solving, for instance, the Newtonian equations of motion for a sliding block on rotating platform (DON'T!!! there are more productive uses of your time!!) and you will find terms corresponding to the fictitious **Coriolis force** and equally-fictitious **centrifugal force**, among others. We'll soon see that General relativity, *by its construction*, removes fictitious forces from the picture. Indeed, it tells us that *gravity* itself is a fictitious force, and that we can describe gravitational phenomena without needing to use the concept of forces at all. To summarize, while we are not able to rigorously-define either of these statements at the moment, GR posits that:

- There are **no preferred reference frames**: mathematically, this is governed by the fact that GR is formulated using mathematical objects called **tensors**
- Gravity is not a force, but rather a consequence of **spacetime geometry** which is described by the **Einstein field equations** using the mathematics of differential geometry
