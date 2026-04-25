+++
title = "Thermodynamics and Statistical Mechanics, Part II"
date = 2026-04-23
+++

This is a guide to statistical mechanics - a fascinating branch of physics that explains, among other things, what entropy is, how objects emit radiation, and why fermions (like electrons) act so differently than bosons (like photons). It is the second part of a two-part guide to thermodynamics and statistical mechanics

<!-- more -->

> ### Chapter guide for Thermodynamics and Statistical Mechanics
> 
> - [Part 1](@/thermo-stat-mech/index.md) covers classical thermodynamics, mostly focusing on the ideal gas and its behavior according to the laws of thermodynamics.
> - [Part 2](@/thermo-stat-mech/part-2.md) covers introductory statistical mechanics and quantum systems, including the Bose-Einstein and Fermi-Dirac statistics, the Einstein and Debye theories of solids, blackbody radiation, and boson condensates. **You are reading this part right now.**

## Introduction to statistical mechanics

Classical thermodynamics is the classical limit of a more fundamental theory: that being **statistical mechanics**. Statistical mechanics not only explains everything that classical thermodynamics could — remarkably, it also allows us to *derive* classical thermodynamics as the classical limit of a more fundamental theory.

In statistical mechanics, we consider **assemblies**, which are roughly a certain number of identical entities (such as atoms, electrons, phonons, photons, etc.). Here, whenever we consider an assembly, it will generally be synonymous with the number of particles. For the $j$-th energy level of the system, we will denote the number of particles as $N_j$.

A system, particularly a quantum system, has different energy levels. **Macrostates** are then the number of particles in each energy level (in practice, they are more complicated, but we will stick to this interpretation for now). Meanwhile, **microstates** are the number of particles in each energy state (quantum state). Microstates and macrostates are *not* the same thing due to the fact that there may be more than one energy state per energy level; there may be *multiple* microstates in each macrostate. As in quantum mechanics, this is known as **degeneracy**.

When applied to thermodynamics, statistical mechanics tells us that **all possible microstates** of an isolated assembly are **equally probable**. That is, while which *exact* microstate the system is in at a particular time is not known, we know that the system is *equally likely* to be in each of its microstate (for a given macrostate).

The **thermodynamic probability** is the number of microstates that can be found for a given macrostate. For the $k$-th macrostate, the thermodynamic probability is denoted as $\omega_k$. It important to note that this is an *unnormalized* and can be anything from zero to infinity; in fact, the thermodynamic probability is not really a probability at all! In mathematical terms, it is more accurately considered a *multiplicity*; the association with probability is due to the fact that a higher thermodynamic probability means that a macrostate is more likely to be observed.

The **true probability** $p_k$, meanwhile, is an actual probability, which is properly normalized (constrained to be between zero and one). It can be found from the thermodynamic probability $\omega_k$ by dividing by the *total* number of microstates $\Omega$. That is, $p_{k} = \omega_{k} / \Omega$.

### A toy statistical model of a coin toss

To understand how our fundamental statistical quantities (microstates, macrostates, and the thermodynamic probability) work, it is instructive to start with the simplest model possible: the coin toss. For instance, consider four distinguishable coins. The coils are tossed and the results are measured. Since each coin can either be heads ($H$) or tails ($T$), there are **five macrostates** depending on the number of heads and the number of tails that are measured after the coil flip, as given below:

| Macrostate | Macrostate     |
| ---------- | -------------- |
| $k = 1$    | $H = 0, T = 4$ |
| $k = 2$    | $H = 1, T = 3$ |
| $k = 3$    | $H = 2, T =2$  |
| $k = 4$    | $H = 3, T= 1$  |
| $k = 5$    | $H = 4, T = 0$ |

Meanwhile, for each of the macrostates, there are a certain number of microstates. In the $k =1$ macrostate, the only possible microstate is $T,T,T,T$ (4 tails); similarly, in the $k = 5$ macrostate, the only possible microstate is $H, H, H, H$ (4 heads). In all other macrostates, there are 4 possible microstates for each macrostate, which are each some combination of heads and tails. The **average occupation number** $\overline N_j$ for the $j$-th macrostate is defined as:

{% math() %}
\overline N_{j} = \frac{\sum_{k}N_{jk}\omega_{k}}{\sum_{k}\omega_{k}} = \frac{\sum_{k}N_{jk}\omega_{k}}{\Omega} = \sum_{k} N_{jk} p_{k}
{% end %}

Where here, we sum over macrostate label $k$. The thermodynamic probability is the highest for $k = 3$: that is, rolling 2 heads and 2 tails is the *most* probable result.

This is well and good for cases in which we can count the possible combinations, but in many cases the number of permutations becomes impossible to count. If we increase the number of (distinguishable) coins to $N$, how many ways are there to select the number of heads or tails?

> **Note:** the requirement of distinguishability is important here. For a coin, it is clearly possible to distinguish between heads and tails (by just looking at the coin); but we will see cases where it is not so simple.

It turns out that if we have $N$ coins, the number of possible heads $N_1$ is given by the **binomial coefficient** for $N_1$ according to the formula:

{% math() %}
\omega_{1} = \begin{pmatrix}
N \\ N_{1}
\end{pmatrix} = 
\frac{N_{1}!}{N_{1}!(N-N_{1})!}
{% end %}

Where $\omega_1$ is the thermodynamic probability of selecting $N_1$ heads. The same is true for the number of possible tails $N_2$, which is given by the binomial coefficient for $N_2$:

{% math() %}
\omega_{2}
=\begin{pmatrix}
N \\ N_{2}
\end{pmatrix} = 
\frac{N_{2}!}{N_{2}!(N-N_{2})!}
{% end %}

And as before, $\omega_2$ is the thermodynamic probability of selecting $N_2$ tails, and by definition:

{% math() %}
N = N_{1} + N_{2}
{% end %}

From this, we can calculate that the most probable macrostate for $N = 1000$ is to have $N_1 = N_2 = 500$ (that is, 500 heads and 500 tails). This tells us what we already intuitively know: that the most likely result of a coin toss is half heads and half tails.

#### The Stiring approximation

Calculating factorials for large numbers is tedious and extremely slow, both manually and even on a computer. However, it turns out that there is a way to approximate factorials for large numbers, called the **Stirling approximation**. This tells us that for large values of $n$, we have:

{% math() %}
\ln n! \approx (n \ln n) - n
{% end %}

This means that we can simply take the natural log of the factorial we want to compute, which is much simpler because calculators can easily calculate logarithms (and we can reasonably approximate them by hands as well).

#### Generalizing the coin toss

Now, let us generalize our two-level system (in which the coins can only be either heads or tails) to an $n$-level system. You can think of this as having a magical coin with $n$ different sides. In that case, we have:

{% math() %}
\omega_{n} = \frac{N!}{N_{1}! N_{2}! N_{3}! \dots N_{n}!} = \frac{N!}{\prod_{j = 1}^n N_{n}!}
{% end %}

Where $\omega_n$ is the thermodynamic probability of selecting the $n$-th macrostate of the system.

### A statistical model of distinguishable particles

Now, let us switch from our toy model of a coin toss to a more realistic model of particles. The **macrostates** of a system of particles confined in a box can be labelled with $(N, V, U)$, where $U$ is the internal energy of the system, $N$ is the number of distinguishable particles, and $V$ is the volume of the box. Here, we use “box” as a generic term; the system does not necessarily need to be in a physical box, it simply has to be an isolated system.

> **Note:** We assume that the particles are non-interacting or weakly-interacting and are in equilibrium states.

We know that the system has $n$ total energy levels; we denote the energy of the $j$-th energy level as $\varepsilon_j$. We want to find the expected number of particles in each macrostate of the system. To start, we can constrain the problem by imposing conservation of particle number and conservation of energy:

{% math() %}
\sum_{j = 1}^n N_{j} = N, \quad \sum_{j = 1}^n N_{j} \varepsilon_{j} = U
{% end %}

These two requirements restrict the possible microstates of the system, and once again (through some tedious calculation) we can find the probabilities of the system being in each macrostate.

### Statistical interpretation of entropy

We have already introduced the classical concept of entropy in thermodynamics, which we may variously interpret as quantifying the useful work that the system can perform or as a measure of the fundamental irreversibility (and thus, imperfect efficiency) of all real-world thermal systems. But we can also interpret entropy from a statistical perspective: a far more powerful perspective that allows us to *derive* the form of entropy we encounter in classical thermodynamics.

Let the entropy $S$ be a function of the thermodynamic probability $\omega$ (we will drop the indices for the states for simplicity). That is to say, $S = f(\omega)$. Now, entropy itself is an extensive property, since it changes depending on the number of particles. Therefore, the total entropy of the system $S$ is a sum of the individual entropies of each of the subsystems in the system. If we denote these subsystems as $A, B, C, \dots$ then we can express this mathematically as:

{% math() %}
\begin{align*}
S &= S_{A} + S_{B} + S_{C} + \dots + S_{N} \\
&= f(\omega_{A})  + f(\omega_{B}) + f(\omega_{C}) + \dots + f(\omega_{N})
\end{align*}
{% end %}

The thermodynamic probabilities $\omega_A, \omega_B, \dots$ are independent, and we know that we can combine independent probabilities via multiplication. Thus $\omega$ is given by:

{% math() %}
\omega = \omega_{A} \omega_{B} \omega_{C} \dots \omega_{N} = \prod_{j} \omega_{j}
{% end %}

But we know that $S = f(\omega)$. Therefore we have:

{% math() %}
S = f(\omega) = f(\omega_{A} \omega_{B} \omega_{C} \dots \omega_{N})
{% end %}

Now, if we equate this with our other expression for $S$:

{% math() %}
S = f(\omega_{A})  + f(\omega_{B}) + f(\omega_{C}) + \dots + f(\omega_{N}) 
{% end %}

We thus have:

{% math() %}
f(\omega_{A} \omega_{B} \omega_{C} \dots \omega_{N}) = f(\omega_{A})  + f(\omega_{B}) + f(\omega_{C}) + \dots + f(\omega_{N}) 
{% end %}

There is only one real-valued function that satisfies this property: the logarithm, which satisfies $\ln(a b) = \ln a + \ln b$. Therefore, the function $f(\omega)$ must be in the form $k \ln(\omega)$, where $k$ is some constant, giving us the famous **Boltzmann entropy formula**:

{% math() %}
S = k \ln \omega 
{% end %}

Where $k$ is the Boltzmann constant (sometimes also denoted $k_{B}$), and $\omega$ (sometimes denoted $\Omega$) is the total number of microstates of the system. This equation allows us to relate the *microscopic* properties of a system (that is, its microstates) 

### Quantum systems

Up to this point, we have mostly stayed within classical physics and simply applied statistical methods to analyze them. But the true power of statistical mechanics is when describing *quantum systems*. Quantum systems frequently have quantized energy levels, that is, energy levels with discrete energies. These energy levels may be non-degenerate (only one quantum state per energy level) or degenerate (more than one quantum state per energy level). The **degeneracy** of the $n$-th energy state is denoted $g_n$ where $n \geq 1$.

For instance, consider the quantum particle of mass $m$ trapped in a 1D box of width $L$. Assume that the box has infinite height. The energies of the particle are then quantized, and are given by:

{% math() %}
\varepsilon_{n} = \frac{n^2 \pi^2 \hbar^2}{2mL^2}, \quad n = 1, 2, 3, \dots
{% end %}

Where $\hbar = h/2\pi$ is the reduced Planck constant, $h = 6.62 \times 10^{-34}\ \mathrm{J \cdot s}$ is the Planck constant, and $n$ is an integer. We can extend this to three dimensions with a box of dimensions $(L_x, L_y, L_z)$, giving us:

{% math() %}
\varepsilon_{q, \ell, k} = \frac{\pi^2 \hbar^2}{2m} \left[ \left( \frac{q}{L_{x}} \right)^2 + \left( \frac{\ell}{L_{y}} \right)^2 + \left( \frac{k}{L_{z}} \right)^2 \right], \quad q, \ell, k \in 1, 2, 3, \dots
{% end %}

Where $q = n_x$, $\ell = n_y$, $k = n_z$ are the quantum numbers in each direction. The **principal quantum number** $n_j$ for the $j$-th energy level is given by:

{% math() %}
n_{j}^2 = q^2 + \ell^2 + k^2 = n_{x}^2 + n_{y}^2 + n_{z}^2
{% end %}

Meanwhile, the degeneracy of the $j$-th energy level is always greater than 1 for anything except the ground state (where $n = \ell = k = 1$). Assuming that the box has volume $V = L_{x}L_{y} L_{z}$, we can then write the energy levels with:

{% math() %}
\varepsilon_{j} = \frac{n_{j}^2 \pi^2 \hbar^2 }{2m}V^{-2/3}
{% end %}

### Density of states

If the quantum numbers are large and that the energy levels are closely spaced-together, then we may consider an infinitesimal energy $d\varepsilon$. We may then define a function $g(\varepsilon)$, called the **density of states**. This relates an infinitesimal number of quantum states $dn$ in the energy levels $\varepsilon$ to that of $\varepsilon + d\varepsilon$ as given by:

{% math() %}
dn = g(\varepsilon) d\varepsilon \quad \Leftrightarrow \quad \frac{dn}{d\varepsilon} = g(\varepsilon)
{% end %}

This is a *linear approximation* for the difference between the number of quantum states at energy level $\varepsilon$ and the number of quantum states at energy level $\varepsilon + d\varepsilon$. That is to say:

{% math() %}
d n \approx  n(\varepsilon + d\varepsilon) - n(\varepsilon), \quad n = n(\varepsilon)
{% end %}

Where $n(\varepsilon)$ gives the number of states at an energy (level) of $\varepsilon$. First, note that $n_j^2$ can be written in terms of the energy as:

{% math() %}
n^2_{j} = n_{x}^2 + n_{y}^2 + n_{z}^2 = \frac{8mV^{2/3}}{h^2} \varepsilon_{j}
{% end %}

Notice how this is very similar to the equation of a sphere, $x^2 + y^2 + z^2 = R^2$, where in this case, the “radius” $R$ becomes:

{% math() %}
R^2 = \left[ \varepsilon_{j}\left( \frac{8mV^{2/3}}{h^2} \right) \right]
{% end %}

Here, we will drop the indices and simply write $n, \varepsilon$ instead of $n_j, \varepsilon_j$ for notational convenience; the indices are now implied. Thus, we have:

{% math() %}
R^2 = \varepsilon \left( \frac{8mV^{2/3}}{h^2} \right)
{% end %}

Assuming that the energy levels are spaced closely together, we can let $n = n(\varepsilon)$ be a continuous function of energy. Now, let $g(\varepsilon) d\varepsilon = n(\varepsilon + d\varepsilon) - n(\varepsilon)$ be the number of energy levels between $n(\varepsilon)$ and $n(\varepsilon + d\varepsilon)$. In our analogy of a sphere, this would be thin shell on an octant of a sphere of radius $R$.  Since the volume of a sphere is given by $V = \frac{4}{3} \pi R^3$ we simply divide this by 8 for the volume of a quadrant. Therefore, we may solve for $n(\varepsilon)$ as follows:

{% math() %}
n(\varepsilon) = \frac{1}{8}\left( \frac{4}{3} \pi R^3 \right) = \frac{\pi}{6} \left[ \varepsilon \left( \frac{8mV^{2/3}}{h^2} \right) \right]^{3/2} = \frac{\pi}{6} V \left( \frac{8m \varepsilon}{h^2} \right)^{3/2}
{% end %}

So the density of states $g(\varepsilon)$ is then given by:

{% math() %}
dn = g(\varepsilon) d\varepsilon
 \quad \Rightarrow \quad g(\varepsilon) = \frac{dn}{d\varepsilon} = \frac{4\pi\sqrt{2}(V m^{3/2} \varepsilon^{1/2})}{h^3}
{% end %}

A more careful calculation would yield the solution of:

{% math() %}
g(\varepsilon) = \gamma_{s} \frac{4\pi\sqrt{2}(V m^{3/2} \varepsilon^{1/2})}{h^3}
{% end %}

Where $\gamma_s = 1$ for **bosons** (particles with integer spin, like photons) and $\gamma_s = 2$ for **fermions** (particles with half-integer spin, like electrons).

### Constrained systems in statistical mechanics

In statistical mechanics, we aim to find the *most probable* state of the system. We already know how to find the macrostates of a system; to find the most probable state, we must use optimization methods from multivariable calculus. However, it is important to note that for the physics to be consistent, we need to perform **constrained optimization**, since we have two physical constraints, corresponding to the conservation of particle number and conservation of energy:

{% math() %}
\sum_{j = 1}^n N_{j} = N, \quad \sum_{j = 1}^n N_{j} \varepsilon_{j} = U
{% end %}

For this, we use the **method of Lagrange multipliers**. This tells us that if we have two equations $f(x_1, x_2, \dots, x_n) = 0$ and $g(x_1, x_2, \dots, x_n) = 0$ that impose constraints on the system, we must solve the following equation to find the maxima (or minima) of the system

{% math() %}
\frac{\partial f}{\partial x_{j}} + \alpha \frac{\partial g}{\partial x_{j}} + \beta \frac{\partial g}{\partial x_{j}} = 0
{% end %}

where $\alpha, \beta$ are the **Lagrange multipliers**. Now, consider a system of $N$ particles The number of ways to put $N_1$ particles into the first energy level containing $g_1$ distinct options is:

{% math() %}
\frac{N!(g_{1})^{N_{1}}}{N_{1}!(N - N_{1})!}
{% end %}

This gives us the thermodynamic probability $\omega_B$ of Boltzmann statistics, given by:

{% math() %}
\omega_{B} = N! \prod_{j = 1}^n \frac{(g_{j})^{N_{j}}}{N_{j}!}
{% end %}

Where $g_j$ is the degeneracy of the $j$-th state. This is the **Boltzmann statistics equation**. Taking the logarithm of the aforementioned equation and switching indices from $j \to i$ gives us:

{% math() %}
\ln \omega_{B} = \ln N! + \sum_{i = 1}^n N_{i} \ln g_{i} - \sum_{i = 1}^n \ln (N_{i}!)
{% end %}

> **Note:** Here, the notation $\ln N!$ is equivalent to $\ln (N!)$ in case that was unclear.

Applying Stirling’s approximation $\ln (N_{i}!) \approx (N_{i} \ln N_{i}) - N_{i}$ to the last term, we have:

{% math() %}
\ln \omega_{B} \approx \ln N! + \sum_{i = 1}^n N_{i} \ln g_{i}
- \sum_{i = 1}^nN_{i} \ln N_{i} + \sum_{i = 1}^n N_{i}
{% end %}

To calculate the maximum of $\omega_B$ under our two constraints (conservation of particle number and conservation of energy), we can combine our two constraint equations and the Lagrange multipliers equation to give us:

{% math() %}
\frac{N_{j}}{g_{j}} = \exp(\alpha + \beta \varepsilon_{j}) =  f (\varepsilon_{j})
{% end %}

Where $\alpha, \beta$ are our Lagrange multipliers. This us the number of particles per quantum state for the equilibrium configuration of the $j$-th energy level.

## Classical statistical distributions

We will now consider four of the most common statistical distributions in statisical mechanics. With some derivations, we will arrive at the **distribution functions** of these four distributions. These tell us the probable number of particles in each state (the *occupancy number*), divided by the degrees of degeneracy, and as we will soon see, it will be the crucial link between statistical and classical thermodynamics.

### The Boltzmann distribution

The Boltzmann distribution (not to be confused with the similarly-named _Maxwell-Boltzmann distribution_) is an idealized statistical model of a gas composed of distinguishable particles. As mentioned before, it is described by the following equation:

{% math() %}
\frac{N_{j}}{g_{j}} = f(\varepsilon_{j}), \quad f(t_{j}) = \exp(\alpha + \beta \varepsilon_{j})
{% end %}

Where $N_j$ are the number of particles in the $j$-th energy level, which has energy $\varepsilon_j$ and degeneracy $g_j$, while $\alpha, \beta$ are Lagrange multipliers. Note that if we take the natural log of both sides and rearrange, we obtain:

{% math() %}
\ln g_{j} - \ln N_{j} + \alpha + \beta \varepsilon_{j} = 0
{% end %}

If we sum over all energy levels, we obtain:

{% math() %}
\sum_{j} N_{j} \ln g_{j} - \sum_{j} N_{j} \ln N_{j} + \alpha \sum_{j}N_{j} + \beta \sum_{j} N_{j} \varepsilon_{j} = 0
{% end %}

Now, $\sum_j N_j$ is the same thing as $N$, the total number of particles, and $\sum_j N_j \varepsilon_j$ is simply the internal energy $U$ of the system. We can therefore rearrange and simplify the above expression as:

{% math() %}
\sum_{j} N_{j} \ln g_{j} - \sum_{j} N_{j} \ln N_{j} = -\alpha N - \beta U
{% end %}

We can now combine the above equation with the Boltzmann statistics equation (given below):

{% math() %}
\ln \omega = \ln N! + \sum_{i = 1}^n N_{i} \ln g_{i}
- \sum_{i = 1}^nN_{i} \ln N_{i} + \sum_{i = 1}^n N_{i}
{% end %}

By substitution, we therefore obtain:

{% math() %}
\begin{align*}
\ln \omega &= \ln N!  - \alpha N - \beta U + N \\
&= c - \beta U
\end{align*}
{% end %}

Where $c \equiv  \ln N! - \alpha N + N$ is a constant. This allows us to use the Boltzmann entropy formula to obtain:

{% math() %}
\begin{align*}
S &= k \ln w \\
&= k(c - \beta U) \\
&= S_{0} - \beta k U, \quad S_{0} = kc = \text{const.}
\end{align*}
{% end %}

We have now cast a statistical distribution in a form that can be analyzed with classical thermodynamics. Physically, we have related the number of particles in each energy level to the entropy of the system. Now, in classical thermodynamics, if we write out the entropy $S = S(U, V)$ in (total) differential form, we have:

{% math() %}
dS = \left( \frac{\partial S}{\partial U} \right)_{V}dU + \left( \frac{\partial S}{\partial V} \right)_{U} dV
{% end %}

Meanwhile, via the Clausius definition of entropy, we equivalently may arrive at another differential expression for the entropy:

{% math() %}
dS = \frac{dQ}{T} =  \frac{dU}{T} + \frac{P dV}{T}
{% end %}

Via term-by-term comparison, we thus have:

{% math() %}
\left( \frac{\partial S}{\partial U} \right)_{V} = \frac{1}{T}, 
\quad \left( \frac{\partial S}{\partial V} \right)_{U} = \frac{P}{T}
{% end %}

Now, by combining this result with $S = S_0 - \beta kU$, if we take the partial derivative of $S$ with respect to $U$, we have:

{% math() %}
\left( \frac{\partial S}{\partial U} \right) = -k \beta = \frac{1}{T}
\quad \Rightarrow \quad \beta = -\frac{1}{kT}
{% end %}

Therefore we have derived the value of our Lagrange multiplier $\beta$! If we substitute this back into the Boltzmann distribution equation, we have:

{% math() %}
\frac{N_{j}}{g_{j}} = \exp(\alpha + \beta \varepsilon_{j}) \quad \Rightarrow \quad N_{j} = g_{j} \exp(\alpha) \exp\left( -\frac{\varepsilon_{j}}{k T} \right)
{% end %}

Summing again over all energy levels, and noting that $\sum_j N_j = N$, we have:

{% math() %}
\begin{gather*}
\sum_{j} N_{j} = \sum_{j} g_{j} \exp(\alpha) \exp\left( -\frac{\varepsilon_{j}}{kT} \right) \\
\Rightarrow \quad \exp(\alpha) = \frac{N}{\sum_{j} g_{j} e^{- \varepsilon_{j} / k T}}
\end{gather*}
{% end %}

Substituting this value of $\exp(\alpha)$ into the original Boltzmann distribution equation, we have:

{% math() %}
\begin{align*}
N_{j} &= g_{j} \exp(\alpha) \exp\left( -\frac{\varepsilon_{j}}{k T} \right) \\
\frac{N_{j}}{g_{j}} &= \exp(\alpha) \exp\left( -\frac{\varepsilon_{j}}{k T} \right) \\
&= \frac{N}{\sum_{j} g_{j} e^{- \varepsilon_{j} / k T} } \exp\left( -\frac{\varepsilon_{j}}{k T} \right) \\
&= \frac{N}{Z} \exp\left( -\frac{\varepsilon_{j}}{kT} \right)
\end{align*}
{% end %}

Here, $Z \equiv  \sum_{j} g_{j} e^{- \varepsilon_{j} / k T}$ is known as the **partition function** and is an essential quantity in statistical mechanics, because it contains **all of the statistical information** about the system. The Boltzmann distribution is fundamentally dependent on the partition function. Now, an important note that if the energy levels are spaced close, then the discrete energies $\varepsilon_j$ becomes continuous energies $\varepsilon$, the occupancy number $N_{j}$ becomes a function of energy $N(\varepsilon)$, and the partition function becomes an integral over all energies:

{% math() %}
\frac{N(\varepsilon)}{g(\varepsilon)} = \frac{N}{Z} \exp\left( -\frac{\varepsilon}{kT} \right), \quad Z = \int g(\varepsilon) e^{-\varepsilon / kT} d\varepsilon
{% end %}

### The Fermi-Dirac distribution

In the Boltzmann statistics, we considered *distinguishable* particles. But what if the particles are identical and *indistinguishable*? Then, we must use one of two distributions, depending on what type of particles make up the system. If these particles are **fermions**, then the distribution to use is the **Fermi-Dirac distribution**.

Fermions obey the **Pauli exclusion principle**, meaning that a given state can either be occupied by *one* particle or *zero* particles, but never more than one. This can be equivalently stated as the requirement that $g_j \geq N_j$. Thus, for each energy level, the thermodynamic probability for each of the $j$-th energy levels is given by:

{% math() %}
\omega_{j} = \frac{g_{j}!}{N_{j}!(g_{j} - N_{j})!}
{% end %}

This gives us the **Fermi-Dirac statistics equation**:

{% math() %}
\omega_{FD} = \prod_{j = 1}^n \frac{g_{j}!}{N_{j}!(g_{j} - N_{j})!}
{% end %}

We can solve for the corresponding distribution for fermions again by taking the natural logarithm of both sides and using the method of Lagrange multipliers.

{% math() %}
\frac{N_{j}}{g_{j}} = \frac{1}{\exp(-\alpha - \beta \varepsilon_{j}) + 1}
{% end %}

Setting $\beta = -1/KT$ and $\alpha = \mu/kT$ (where $\mu$ is the chemical potential), we obtain the famous **Fermi-Dirac distribution**:

{% math() %}
\frac{N_{j}}{g_{j}} = \frac{1}{e^{(\varepsilon_{j} - \mu_{j})/ kT} + 1}
{% end %}

Which, in the continuous case (that is, when we can consider the energy spectrum to be approximately continuous), is given by:

{% math() %}
\frac{N(\varepsilon)}{g(\varepsilon)} = \frac{1}{e^{(\varepsilon - \mu) / kT} + 1}
{% end %}

### The Bose-Einstein Distribution

Lastly, we will consider the case where we have identical and *indistinguishable* particles that are **bosons**, which *do not* follow the Pauli exclusion principle. This means that we cannot use the Fermi-Dirac distribution; instead, we must use the **Bose-Einstein distribution**. This means that there is no limitation on how many particles are allowed in each state, meaning that $N_j$ can be arbitrary, regardless of what $g_j$ is. It turns out that the thermodynamic probability for the $j$-th state is then given by:

{% math() %}
\omega_{j} = \frac{(N_{j} + (g_{j} - 1))!}{N_{j}!(g_{j} - 1)!}
{% end %}

And thus the **Bose-Einstein statistics equation** is given by:.

{% math() %}
\omega_{BE} = \prod_{j = 1}^n  \frac{(N_{j} + (g_{j} - 1))!}{N_{j}!(g_{j} - 1)!}
{% end %}

Using the same Lagrange multiplier approach, we obtain:

{% math() %}
\frac{N_{j}}{g_{j}} = \frac{1}{\exp(-\alpha - \beta \varepsilon_{j}) - 1}
{% end %}

We then find that $\alpha = \frac{\mu}{kT}$ and $\beta = -\frac{1}{kT}$, which, upon substitution, gives us:

{% math() %}
\frac{N_{j}}{g_{j}} = \frac{1}{e^{(\varepsilon_{j} - \mu_{j})/ kT} - 1}
{% end %}

This is the **Bose-Einstein distribution**. In the continuous case, it reduces to:

{% math() %}
\frac{N(\varepsilon)}{g(\varepsilon)} = \frac{1}{e^{(\varepsilon - \mu)/kT} - 1}
{% end %}

### The Maxwell-Boltzmann distribution

Finally, in the limiting case of indistinguishable particles with large degeneracies ($g_j \gg N_j$), it turns out that the Fermi-Dirac statistics and Bose-Einstein statistics both reduce to a new statistics equation, given by:

{% math() %}
\omega_{MB} = \prod_{j = 1}^n \frac{(g_{j})^{N_{j}}}{N_{j}!}
{% end %}

This is the **Maxwell-Boltzmann statistics equation**, which is closely related to the Boltzmann statistics equation. Indeed, the thermodynamic probability $\omega_B$ for Boltzmann statistics is related to that of Maxwell-Boltzmann statistics via $\omega_B = (N!) \omega_{MB}$. It turns out that their distribution functions are also the same; that is:

{% math() %}
\frac{N_{j}}{g_{j}} = \frac{N}{Z} \exp\left( -\frac{\varepsilon_{j}}{kT} \right), \quad Z = \sum_{j} g_{j} e^{-\varepsilon_{j} / kT}
{% end %}

Likewise, the continuous energy spectrum case is also the same:

{% math() %}
\frac{N(\varepsilon)}{g(\varepsilon)} = \frac{N}{Z} \exp\left( -\frac{\varepsilon}{kT} \right), \quad Z = \int g(\varepsilon) e^{-\varepsilon / kT} d\varepsilon
{% end %}

> **Note:** It is important to understand that the Maxwell-Boltzmann distribution *fails at low temperatures*. It is only an approximate model that can describe the statistical behavior of particles at high temperatures.

#### The Helmholtz function for the Maxwell-Boltzmann distribution

There is another link between classical and statistical thermodynamics, using the Helmholtz function $F$. To see why, recall that in classical thermodynamics, we can write out the Helmholtz function in differential form as:

{% math() %}
\begin{align*}
dF &= dU - TdS - SdT \\
&= -S dT - P dV + \mu dN
\end{align*}
{% end %}

Where {% inlmath() %}\mu^*{% end %} is the chemical potential per kilomole, that is, {% inlmath() %}\mu^* = \mu N_A{% end %}. Now, if we take $T, V = \text{const.}$ we find that:

{% math() %}
\mu = \left( \frac{\partial F}{\partial N} \right)_{T, V}
{% end %}

Let us try to obtain the Helmholtz function for the Maxwell-Boltzmann distribution. Using Stirling’s approximation and taking the natural logarithm of the Maxwell-Boltzmann statistics equation, we have:

{% math() %}
\begin{align*}
\ln \omega_{MB} &= N - \sum_{j = 1}^n N_{j} \ln N + \sum_{j = 1}^n N_{j} \frac{\varepsilon_{j}}{k T} + \sum_{j = 1}^n N_{j} \ln Z \\
&= N - N \ln N + \frac{U}{kT} + N \ln Z
\end{align*}
{% end %}

Where we have omitted the intermediate steps for brevity. From which substituting into Boltzmann’s entropy equation yields:

{% math() %}
\begin{align*}
S &= k \ln \omega_{MB} \\
&= \frac{U}{T} + N k [\ln Z - \ln N + 1]
\end{align*}
{% end %}

### The chemical potential from a statistical perspective

Recall that previously, we have seen that the chemical potential satisfies:

{% math() %}
\mu = \left( \frac{\partial F}{\partial N} \right)_{T, V}
{% end %}

If we combine Boltzmann’s entropy equation $S = k \ln \omega$ with $\omega = \omega_B$, where $\omega_B$ is the thermodynamic probability of the Maxwell-Boltzmann distribution, we obtain:

{% math() %}
S = \frac{U}{T} + Nk(\ln Z - \ln N + 1)
{% end %}

Therefore, the **Helmholtz function** $F = U - TS$ gives us:

{% math() %}
F = -N k T (\ln Z - \ln N + 1)
{% end %}

> **Note:** This the case for a **Maxwell-Boltzmann distribution**. For a Boltzmann distribution, the Helmholtz function can be shown to be given by $F = -Nk T \ln Z$.

Therefore we may obtain an expression for the chemical potential as follows:

{% math() %}
\mu = \left( \frac{\partial F}{\partial N} \right)_{{T, V}} =  k T \ln \frac{N}{Z}
{% end %}

We notice that $\mu$ is directly proportional to the number of particles per unit volume and the temperature. Physically, this reflects the fact that particles flow from higher to lower chemical potential and higher to lower concentration. Moreover, we may rearrange to express $N/A$ in terms of the chemical potential:

{% math() %}
\frac{N}{Z} = e^{\mu / k T}
{% end %}

If we substitute this into the Boltzmann distribution, we obtain:

{% math() %}
\frac{N_{j}}{g_{j}} = \frac{Ne^{- \varepsilon / k T}}{Z} = e^{\mu / k T} e^{- \varepsilon / k T} = \frac{1}{e^{(\varepsilon_{j}- \mu)/kT}}
{% end %}

(Note that this is the same for the Maxwell-Boltzmann distribution). In the most general case, we can write a generalized distribution in the form:

{% math() %}
\frac{N_{j}}{g_{j}} = \frac{1}{e^{(\varepsilon_{j} - \mu)/ k T} + a}
{% end %}

Where $a$ can take one of three dimensionless values:

- $a = +1$ for the Fermi-Dirac distribution
- $a = -1$ for the Bose-Einstein statistics
- $a = 0$ for the Boltzmann/Maxwell-Boltzmann statistics

## Statistical ensembles

In more advanced statistical mechanics, it is frequent to consider three different *ensembles* to model statistical systems:

- Microcanonical ensemble
- Canonical ensemble
- Grand canonical ensemble

However, we will not go into these for now in our elementary discussion.

## Classical statistics of the ideal gas

Let us now take the classical limit of statistical thermodynamics. That is, we consider the following assumptions:

- Temperatures much higher than absolute zero
- Gas is composed entirely of non-interacting molecules, and thus the effects of spin are unimportant (since molecules have negligible net spin)
- No phase changes

We can show that in this limit, statistical thermodynamics agrees exactly with classical thermodynamics.

### Derivation of the ideal gas equation

To start, let us recall the Maxwell-Boltzmann distribution:

{% math() %}
\frac{N_{j}}{g_{j}} = \frac{Ne^{- \varepsilon_{j}/k T}}{Z} \quad \Rightarrow \quad N_{j} = \frac{g_{j} Ne^{-\varepsilon_{j}/ kT}}{Z}
{% end %}

Previously, we have also found that:

{% math() %}
F = -NkT(\ln Z - \ln N + 1)
{% end %}

Therefore, the internal energy $U$ can be expressed as follows:

{% math() %}
U = \sum_{j} N_{j} \varepsilon_{j} = \sum_{j} \frac{g_{j} \varepsilon_{j} Ne^{-\varepsilon_{j}/ kT}}{Z}
{% end %}

Meanwhile, recall that we have defined the partition function $Z$ as:

{% math() %}
Z = \sum_{j} g_{j} e^{-\varepsilon_{j} / k T}
{% end %}

With some mathematical rewriting, we can express $Z$ in the following form:

{% math() %}
\left( \frac{\partial Z}{\partial T} \right)_{V} = \frac{1}{k T^2} \sum_{j} g_{j} e^{-\varepsilon_{j}/ kT} = \frac{Z}{kT^2}\quad \Rightarrow \quad Z = k T^2 \left( \frac{\partial Z}{\partial T} \right)_{V}
{% end %}


Substituting this expression for $Z$ into $U$, we obtain an expression for the **total internal energy** of a classical gas:

{% math() %}
U = NkT^2 \left( \frac{\partial \ln Z}{\partial T} \right)_{V}
{% end %}

> **Note:** It so happens that this is the same result for the *Boltzmann distribution*, as well as for the *Maxwell-Boltzmann* distribution.

From the Helmholtz function, internal energy, and chemical potential, we can now derive classical thermodynamic quantities straight from statistical mechanics. For instance, the classical Gibbs function $G$ can be expressed as:

{% math() %}
G = \mu N = -NkT(\ln Z - \ln N)
{% end %}

Thus, the enthalpy of a classical ideal gas is given by:

{% math() %}
\begin{align*}
H &= U + PV \\
&= (U + PV - T S ) + TS \\
&= G + TS \\
&= N kT^2 \left( \frac{\partial \ln Z}{\partial T} \right)_{V} + NkT
\end{align*}
{% end %}

Differentiating the Helmholtz function $F = -NkT(\ln Z - \ln N + 1)$ and holding temperature constant, we can then obtain the pressure:

{% math() %}
P = -\left( \frac{\partial F}{\partial V} \right)_{T} =NkT\left( \frac{\partial \ln Z}{\partial V} \right)_{T}
{% end %}

What about the partition function for a classical ideal gas? Well, first, we can make the reasonable approximation that the gas has a continuous energy spectrum, and therefore we can use the integral expression for the partition function:

{% math() %}
Z = \int g(\varepsilon) e^{-\varepsilon / k T} d \varepsilon
{% end %}

We also recall that the expression for the density of states we calculated before was given by:

{% math() %}
g(\varepsilon) d\varepsilon = \frac{4\pi\sqrt{ 2 } V m^{3/2}\varepsilon^{1/2}}{h^3} d\varepsilon
{% end %}

Therefore, if we substitute $g(\varepsilon)$ into the integral expression for $Z$, we obtain:

{% math() %}
Z = \int_{0}^\infty g(\varepsilon) e^{-\varepsilon/kT} d\varepsilon = \frac{4\pi \sqrt{ 2 }V m^{3/2}}{h^3} \int_{0}^\infty \varepsilon^{1/2} e^{-\varepsilon / k T} d \varepsilon
{% end %}

This integral is non-trivial (it is a very hard integral to evaluate), but it can be shown that:

{% math() %}
\int_{0}^\infty \varepsilon^{1/2} e^{-\varepsilon / k T} d \varepsilon = \frac{\sqrt{ \pi }}{2} (kT)^{3/2}
{% end %}

This gives us the partition function for a classical ideal gas with a continuous energy spectrum:

{% math() %}
Z = V\left( \frac{2\pi m k T}{h^2} \right)^{3/2}
{% end %}

Let’s see what happens when we take the logarithm of the partition function. We find:

{% math() %}
\ln Z = \ln V + \frac{3}{2} \ln T + \frac{3}{2} \ln\left( \frac{2\pi m k}{h^2} \right)
{% end %}

Therefore:

{% math() %}
\left( \frac{\partial \ln Z}{\partial V} \right)_{T} = \frac{1}{V},
\quad \Rightarrow \quad \left( \frac{\partial \ln Z}{\partial T} \right)_{V} = \frac{3}{2T}
{% end %}

Now recall that we previously derived that:

{% math() %}
P = NkT\left( \frac{\partial \ln Z}{\partial V} \right)_{T}
{% end %}

Therefore, substituting our obtained value of $\left( \frac{\partial \ln Z}{\partial V} \right)_{V}$ in our formula for $P$, we have:

{% math() %}
P = Nk T \left( \frac{1}{V} \right) = \frac{N kT}{V}
{% end %}

Defining $n = N/N_A$ and $R = k N_A$, we obtain the famous **ideal gas law** upon rearrangement:

{% math() %}
PV = n R T
{% end %}

Meanwhile, if we substitue in our obtained value of $\left( \frac{\partial \ln Z}{\partial T} \right)_{V}$ into our formula for $U$, we have the famous **temperature-energy relation**, which can also be derived from the classical kinetic theory of molecules:

{% math() %}
U = NkT^2 \left( \frac{\partial \ln Z}{\partial T} \right)_{V} = \frac{3}{2} N kT
{% end %}

Finally, we can also compute the entropy of a classical ideal gas:

{% math() %}
\begin{align*}
S &= \frac{U}{T} + Nk(\ln Z - \ln N + 1) \\
&= \frac{3}{2} Nk + Nk\left(\ln \left[ V \left( \frac{2\pi mkT}{h^2} \right)^{3/2} \right]- \ln N + 1 \right) \\
&= \frac{3}{2} Nk + Nk\left( \ln\left[ \frac{V}{N} \left( \frac{2\pi m k T}{h^2} \right)^{3/2} \right] + 1 \right)
\end{align*}
{% end %}

Rearrangement yields the famous **Sackur-Tetrode equation**:

{% math() %}
S = Nk\left[ \ln\left[ \frac{V}{N}\left( \frac{4\pi mU}{3h^2N} \right)^{3/2} \right] + \frac{5}{2}\right]
{% end %}

This may be well and good, but a question we might want to ask, is: how good is this model for real gases? Well, let us define $n_Q$ as:

{% math() %}
n_{Q} \equiv \left( \frac{2\pi m kT}{h^2} \right)^{3/2}, \quad Z = n_{Q} V
{% end %}

Therefore, we have:

{% math() %}
\frac{N_{j}}{g_{j}} = \frac{Ne^{-\varepsilon_{j}/kT}}{Z} = \left( \frac{N}{V} \right) \frac{e^{-\varepsilon_{j}/kT}}{n_{Q}}
{% end %}

For low temperatures, we can make the approximation that $e^{-\varepsilon_j/kT} \approx e^{-1} \approx 1$. With these approximations, we have:

{% math() %}
\frac{N_{j}}{g_{j}} \approx \frac{N}{n_{Q}V}
{% end %}

Under standard conditions for most gases, $N_j \ll g_j$. The gas is then said to be in the **classical regime**, and the ideal gas law is highly-accurate.

### The equipartition theorem

Lastly, we can calculate the average energy of a molecule in a classical ideal gas. To start, we can combining the three equations we’ve used extensively:

{% math() %}
\begin{gather*}
\frac{N(\varepsilon)}{g(\varepsilon)} = \frac{Ne^{-\varepsilon / kT}}{Z} \\
Z = V\left( \frac{2\pi m k T}{h^2} \right)^{3/2} \\
g(\varepsilon) d\varepsilon = \frac{4\pi\sqrt{ 2 } V m^{3/2}\varepsilon^{1/2}}{h^3} d\varepsilon
\end{gather*}
{% end %}

This allows us to obtain:

{% math() %}
N(\varepsilon) d\varepsilon = \frac{2\pi N\varepsilon^{1/2}e^{-\varepsilon / k T}}{(n k T)^{3/2}}
{% end %}

Combining all three together and using the classical kinetic velocity relation $\varepsilon(v) = \frac{1}{2} mv^2$, and thus $d\varepsilon = mvdv$, then we have:

{% math() %}
N(v) dv = 4\pi N e^{- m v^2 / 2 kT} v^2 \left( \frac{m}{2\pi k T} \right)^{3/2} dv
{% end %}

To find the average energy $\overline \varepsilon$, we have:

{% math() %}
\overline \varepsilon(v) = \frac{U_{\text{total}}}{N_\text{total}} = \frac{\displaystyle \int_{0}^\infty \varepsilon(v) N(v)dv}{\displaystyle \int_{0}^\infty N(v) dv}
{% end %}

The integrals are very difficult to solve, but they do have an analytical solution, and it is given by:

{% math() %}
\overline \varepsilon(v) = \frac{3}{2} kT
{% end %}

This is *exactly* the same as the formula we saw before for the classical theory of gases, where $U = \frac{3}{2}N k T$ and thus $\overline \varepsilon = U/N = \frac{3}{2}kT$ (we divide by $N$, since here we are interested in the average energy per molecule). Indeed, the more generalized case of this formula is given by:

{% math() %}
\overline \varepsilon = \frac{d}{2} kT
{% end %}

Where $d$ is the number of degrees of freedom; in the case of velocity, $d = 3$ since the velocity vector has three components. This is called the **equipartition of energy states** or the **equipartition theorem**.

## Molecular degrees of freedom and heat capacity

Previously, we saw that monatomic and diatomic gases have *different* heat capacities. We did not previously explain the reasons behind these different heat capacities, and simply took it as a fact. With statistical thermodynamics, we can finally answer *why*.

It turns out that different heat capacities have all to do with *molecular degrees of freedom*. A monatomic gas has a single atom, so it has only *translational* degrees of freedom. But a diatomic gas has two atoms, so in addition to its translational degrees of freedom, it also has *vibrational* and *rotational* degrees of freedom. These vibrations and rotations are fundamentally quantized, which has a tangible macroscopic effect.

In a more mathematical form, we can say that the partition function of a monatomic gas satisfies $Z_\text{monatomic} = Z_\text{trans}$, while the partition function of a diatomic gas satisfies $Z_\text{diatomic} = Z_\text{trans} + Z_\text{rot} + Z_\text{vib}$, where $Z_\text{trans}, Z_\text{rot},Z_\text{vib}$ are the contributions to the partition function from the translational, rotational, and vibrational degrees of freedom, respectively.

We have already considered the case of a monatomic gas, whose internal energy (more specifically, the internal energy due to the translational degrees of freedom) was given by:

{% math() %}
U_\text{trans} = N k T^2 \left( \frac{\partial \ln Z_\text{trans}}{\partial T} \right)_{V} = \frac{3}{2} NkT
{% end %}

However, for a diatomic gas, we must also consider the vibrational and rotational degrees of freedom. In the case of a monatomic gas, a single molecule has no rotational or vibrational degree of freedom, so $Z_\text{rot} = Z_\text{vib} = 0$.

### Vibrational degrees of freedom

We will calculate the former first. To start, let us recall the Maxwell-Boltzmann distribution:

{% math() %}
\frac{N_{j}}{g_{j}} = \frac{N}{Z} e^{-\varepsilon_{j}/kT}
{% end %}

The vibrational degrees of freedom of a diatomic molecule can be modelled as a quantum harmonic oscillator, which has quantized energy levels $\varepsilon_j$ given by:

{% math() %}
\varepsilon_{j} = \left( j + \frac{1}{2} \right) h \nu
{% end %}

Here, $\nu$ is the *natural frequency* of oscillation, and the ground-state energy (for the $j = 0$ state) is given by $\varepsilon_0 = \frac{1}{2} h \nu$, and is also called the **zero-point energy**. It is important to note that the energy levels of the quantum harmonic oscillator are **non-degenerate**; thus, $g_j = 1$.

From this information, we can then calculate the partition function. Substituting in the above expression for the energy for $\varepsilon_j$ in the partition function formula, we obtain:

{% math() %}
\begin{align*}
Z &= \sum_{j} g_{j} \exp\left( -\frac{\varepsilon_{j}}{kT} \right) \\
&= \sum_{j} \exp\left( -\frac{\left( j + \frac{1}{2}\right) h \nu}{k T} \right)
\end{align*}
{% end %}

Let us define $\theta \equiv h\nu/k$ as the **characteristic temperature**. This allows us to simplify the partition function:

{% math() %}
\begin{align*}
Z &= \sum_{j} \exp\left( -\frac{\left( j + \frac{1}{2} \right)\theta}{T} \right) \\
&= e^{- \theta/2T} \sum_{j} e^{-j \theta / T} \\
&= e^{- \theta/2T}(1 + e^{-\theta/T} + e^{-2\theta / T} + \dots) \\
&= \frac{e^{-\theta / 2 T}}{1 - e^{- \theta / T}}
\end{align*}
{% end %}

Where the last step comes from the fact that the sum is in the form of a convergent **geometric series**, which has an exact analytical expression. Substituting this into the Maxwell-Boltzmann distribution (with $g_j = 1$), we obtain:

{% math() %}
\begin{align*}
\frac{N_{j}}{\cancel{ g_{j} }^1} &= \frac{N}{Z} e^{-\varepsilon_{j}/kT} \\
&= Ne^{-\varepsilon_{j}/kT} \left( \frac{1 - e^{- \theta / T}}{e^{-\theta / 2 T}} \right) \\
N_{j} &= N(1 - e^{-\theta/T}) e^{-j \theta/T} \\
\frac{N_{j}}{N} &= (1 - e^{-\theta/T}) e^{-j \theta/T}
\end{align*}
{% end %}

We can also find the internal energy contribution from vibrations, $U_\text{vib}$, through our known formula:

{% math() %}
\begin{align*}
U_\text{vib} &= N kT^2 \left( \frac{\partial \ln Z}{\partial T} \right)_{V} \\
&= N k T^2 \frac{\partial}{\partial T} [\ln e^{-\theta / 2 T} - \ln (1 - e^{-\theta/T})] \\
&= Nk \theta\left[ \frac{1}{2} + \frac{1}{e^{\theta / T} - 1} \right]
\end{align*}
{% end %}

In the limit as $T \to 0$, then $U_\text{vib} \to \frac{N k \theta}{2} = \frac{N h \nu}{2}$, which is simply the zero-point energy $\varepsilon_0$ multiplied by $N$. This tells us that at very low temperatures, the molecules all condense into the ground state. Conversely, in the opposite limit $T/\theta \gg 1$ (that is, for high temperatures), we can use the approximation $e^{\theta/T} - 1 \approx \theta/T$. This gives us:

{% math() %}
U_\text{vib} \approx N k \theta \left( \frac{1}{2} + \frac{T}{\theta} \right) \approx N k T
{% end %}

Where we have dropped the $N k \theta/2$ term (which represents the zero-point energy) since it is negligible at high temperatures. Now, from $C_{V} = \left( \frac{\partial U}{\partial T} \right)_{V}$, we obtain:

{% math() %}
C_{V} = \left( \frac{\partial U_\text{vib}}{\partial T} \right)_{V} = N k \left( \frac{\theta}{T} \right)^2 \frac{e^{\theta / T}}{(e^{\theta / T} - 1)}
{% end %}

In the low and high temperature limits respectively, we have:

{% math() %}
C_{V} \approx \begin{cases}
N k, & T / \theta \gg 1 \\
N k \left( \frac{\theta}{T} \right)^2 e^{-\theta/T},  & T / \theta \ll 1
\end{cases}
{% end %}

As $T \to 0$, we notice that $C_V \to 0$. This is consistent with the third law of thermodynamics, which says that all thermodynamical properties of a system go to zero as $T \to 0$.

### Rotational degrees of freedom

Let us now consider the rotational degrees of freedom for a diatomic molecule. In 3D space, there are 3 rotation axes for any object. This means that a diatomic molecule would have *two* rotational degrees of freedom ($d = 2$), since it is symmetric about one axis, but can rotate among the other two axes. Therefore, by the equipartition theorem $U = d NkT/2$, we can directly arrive at the following expression for the internal energy contribution due to rotations:

{% math() %}
U_\text{rot} = \frac{d}{2} NkT = N k T, \quad T \gg \theta_\text{rot}
{% end %}

Where $\theta_\text{rot}$ is the characteristic temperature for rotations (we’ll show the exact expression for this later). This result applies for **high temperatures**, but is a generally reasonable assumption, and is certainly one for a classical gas.

> **Note:** In theory, there is also a contribution from electron excitations to the total internal energy. In practice, the temperatures at which this applies is so high that it does not matter for a classical gas.

#### Quantum calculation of rotations

We will also show a first-principles derivation of the rotational degrees of freedom. To start, the (squared) quantum angular momentum operator $\hat L$ has eigenvalues given by:

{% math() %}
L^2 = l (l + 1) \hbar^2, \quad l = 0, 1, 2, \dots
{% end %}

From classical mechanics, the rotational energy is given by:

{% math() %}
\varepsilon = \frac{1}{2} I \omega^2, \quad L = I \omega
{% end %}

Therefore, equating the two expressions, we have the following expression for the energy levels due to rotations:

{% math() %}
\varepsilon_{l} = \frac{l(l + 1)}{2I} \hbar^2
{% end %}

Defining $\theta_\text{rot} = \frac{\hbar^2}{2Ik}$ as the **characteristic temperature for rotations**, we therefore obtain:

{% math() %}
\varepsilon_{l} = l(l + 1) k \theta_\text{rot}
{% end %}

Thus, the partition function becomes:

{% math() %}
\begin{align*}
Z &= \sum_{l} g_{l} e^{-\varepsilon_{l} / k T} \\
&= \sum_{l} (2 l + 1) \exp\left( -\frac{l(l + 1)\theta_\text{rot}}{T} \right) \\
&= 1 + 3 e^{-2 \theta_\text{rot} / T} + 5 e^{-6 \theta_\text{rot} / T} + \dots
\end{align*}
{% end %}

Where $g_l$ is the rotational degrees of degeneracy, and $g_l = 2l + 1$ (this can be determined by solving the Schrödinger equation). For diatomic gases (*except hydrogen*, where the characteristic temperature is 85.4 K), $\theta_\text{rot} \leq 10K$. Therefore, we can truncate the series to the first two terms. This gives us:

{% math() %}
\ln Z \approx \ln(1 + 3e^{- 2 \theta_\text{rot} / T})
{% end %}

Now with the approximation $\ln(1 + x) \approx x$ (valid for small $x$) we thus have:

{% math() %}
\ln Z \approx 3e^{-2 \theta_\text{rot} / T}
{% end %}

From which we obtain:

{% math() %}
\begin{align*}
U &= N k T^2 \left( \frac{\partial \ln Z}{\partial T} \right)_{V} = 6 N k \theta_\text{rot} e^{-2 \theta_\text{rot} / T}, \quad \theta_\text{rot} \gg T \\
C_{V, \text{rot}} &= \left( \frac{\partial U}{\partial T} \right)_{V} 
= 3Nk \left( \frac{2\theta_\text{rot}}{T} \right)^2 e^{-2 \theta_\text{rot} / T} , \quad \theta_\text{rot} \gg T
\end{align*}
{% end %}

### Combined degrees of freedom

Recall the expression for the total internal energy of a classical (Maxwell-Boltzmann) gas is given by:

{% math() %}
U = N k T^2 \left( \frac{\partial \ln Z}{\partial T} \right)_{V}
{% end %}

The total internal energy of the diatomic molecule gives us:

{% math() %}
\begin{align*}
U_\text{total} &= U_\text{trans} + U_\text{rot} + U_\text{vib} \\
&= NkT^2\left[ \frac{\partial}{\partial T} (Z_\text{trans} + Z_\text{rot} + Z_\text{vib}) \right] \\
\end{align*}
{% end %}

For a monatomic gas, $U_\text{total}$ is simply equal to $U_\text{trans}$. However, for diatomic gases, the incorporation of rotational and vibrational degrees of free adds additional terms that change the internal energy, and thus naturally, the heat capacity. To summarize:

| Regime                | Typical value (for molecular hydrogen) | Situation               |
| --------------------- | -------------------------------------- | ----------------------- |
| Low temperature       | ~10 K to 85 K                          | $C_V = \frac{3}{2} kNT$ |
| High temperature      | 85 K to 6140 K                         | $C_V = \frac{5}{2} NkT$ |
| Very high temperature | > 6140 K                               | $C_V = \frac{7}{2} NkT$ |

## Introduction to solid-state physics

Having primarily studied fluids (gases and liquids), we will now take a look at the study of solids. This is the branch of physics known as **solid-state physics**. In solid-state physics, we study different types of solids:

- Crystals, which are **ordered**
- Amorphous solids, which are **disordered**
- Quasi-crystals, which are **quasi-ordered**

At the beginning of the 20th century, major efforts were taken to try to describe and explain the properties of solids, and particularly crystals. The **electronic properties** of a crystal can be studied in a reasonably straightforward manner, due to their symmetries. This allows a crystal to be understood as a periodic lattice, essentially a repeating series of a basic building block (called a **unit cell**) extending in all directions in space. Thus, it is possible to simply study the properties of just one unit cell and apply periodic boundary conditions to generalize these properties to those of the entire crystal. But the **thermodynamic properties** of a crystal are less easy to study. Here, we will focus on the *heat capacity* of a crystal.

### Einstein’s theory of crystalline solids

Einstein modelled a crystal as a lattice composed of $N$ atoms, each of which was fixed in place but allowed to vibrate. Since the atoms in a 3D crystal can vibrate in any of the 3 $x, y, z$ directions, there will be 3 degrees of freedom, and thus could be described as $3N$ quantum harmonic oscillators. Recall we previously derived the following expression for the internal energy of $N$ harmonic oscillators, corresponding to the degrees of freedom for a gas:

{% math() %}
U_\text{vib} = Nk \theta\left[ \frac{1}{2} + \frac{1}{e^{\theta / T} - 1} \right]
{% end %}

In Einstein’s model, we simply multiply this by three to obtain the internal energy of $3N$ harmonic oscillators:

{% math() %}
U_\text{vib} = 3Nk \theta_{E}\left[ \frac{1}{2} + \frac{1}{e^{\theta / T} - 1} \right]
{% end %}

Where we have the **Einstein characteristic temperature** $\theta_E = h\nu/k$. Thus, we find that:

{% math() %}
C_{V} = \left( \frac{\partial U}{\partial T} \right)_{V} 
= 3 Nk\left( \frac{\theta_{E}}{T} \right)^2 \frac{e^{\theta_{E}/T}}{(e^{\theta_{E}/T} - 1)^2}
{% end %}

This can be approximated in the higher and low temperature regimes as follows:

{% math() %}
C_{V} \approx \begin{cases}
3 Nk, & T \gg \theta_{E} \\
3 Nk \left( \frac{\theta_{E}}{T} \right)^2 e^{-\theta_{E} / T}, & T \ll \theta_{E}
\end{cases}
{% end %}

(Note that $3 Nk = 3 nR$, where $R$ is the ideal gas constant, and $n$ is the number of kilomoles). At high temperature, $C_V$ approaches a constant temperature, reproducing the **Dulong-Petit law**, which we previously showed:

{{ diagram(
	src="../specific-heat-capacity-comparison.excalidraw.svg"
	desc="A plot of the specific heat capacity for a solid across different temperatures"
	width=400
) }}

It turns out that while the Einstein model works well for the high-temperature regime, it fails at low temperatures. The search for a low-temperature theory to improve on Einstein’s theory resulted in **Debye’s theory**.

### Debye’s theory of crystalline solids

Debye’s model associates the internal energy with quasi-particles called **phonons** (lattice vibrations). Phonons have no mass, but they can vibrate at different (quantized) frequencies; that is to say, they are essentially waves. Thus they can be described by a wavefunction. Due to the boundary conditions of a single unit cell, the solutions for the wavefunctions are given by the same wavefunctions for the particle in a box/infinite square well. In one dimension, these are given by:

{% math() %}
\psi_{n}(x) = A \sin \frac{n\pi x}{L}, \quad n = \frac{2L}{\lambda}, \quad n = 1, 2, 3, \dots
{% end %}

The vibrational frequency $\nu$ is related to the wavelength $\lambda$ of the phonon waves with $v = \lambda \nu$, where $v$ is the velocity of the wave. This gives us the following relation for a 1D phonon:

{% math() %}
n = \frac{2L \nu}{v}
{% end %}

If we work in 3 dimensions, considering a solid crystal of volume $V = L^3$ with side lengths $L$ (we assume the crystal is a square), then we have:

{% math() %}
n = \frac{2V^{1/3} \nu}{v}, \quad n^2 = n_{x}^2 + n_{y}^2 + n_{z}^2
{% end %}

Then, we may deduce the following expression for the density of states $g(\nu)$ for a given frequency $\nu$:

{% math() %}
g(\nu) = \frac{dn}{d\nu} \quad \Rightarrow \quad g(\nu) d\nu = \frac{n^2 \pi}{2} dn = \frac{4 \pi V \nu^2}{v^3} d \nu
{% end %}

In a vibrating solid, we encounter the three types of waves: longitudinal modes (with velocity $v_l$) and two kinds of transverse modes (with velocity $v_t$). Thus, we may write the density of states as:

{% math() %}
g(\nu) d\nu = 4\pi V \nu^2 \left( \frac{1}{v_{l}^3} + \frac{2}{v_{t}^3} \right) d\nu
{% end %}

The phonons in a solid may have different vibrational frequencies $\nu$, up to a maximum allowable frequency $\nu_m$. It can be shown (we won’t do the calculation here) that the density of states can be expressed in the equivalent form in terms of $\nu_m$:

{% math() %}
g(\nu) d\nu = \frac{9N}{\nu_{m}^3} \nu^2 d\nu
{% end %}

Despite being quasiparticles, phonons can be regarded as bosons. Therefore, their individual energies are given by $\varepsilon = h\nu$ (just like photons), and they can be modelled by the Bose-Einstein distribution:

{% math() %}
\frac{N(\varepsilon)}{g(\varepsilon)} = \frac{1}{e^{(\varepsilon - \mu)/kT} - 1}
{% end %}

The number of phonons is *not constant*; as temperature increases, the number of phonons increases, and as the temperature decreases, the number of phonons decreases. But we want to find the number of phonons (which we denote as $N$) in an *equilibrium state*. This can be found by minimizing the Helmholtz function $F$:

{% math() %}
\mu = \left( \frac{\partial F}{\partial N} \right)_{T, V} = 0
{% end %}

From which we can show that $N(\nu)$, the number of phonons are a given frequency $\nu$, is given by:

{% math() %}
N(\nu)dn = \frac{g(\nu) d\nu}{e^{h\nu / kT} - 1}
{% end %}

If we substitute in the value of $g(\nu)d\nu$ into the above expression, we may express $N(\nu)$ in explicit form:

{% math() %}
N(\nu) = \begin{cases}
\dfrac{9N\nu^2}{\nu_{m}^3(e^{h\nu / k T} - 1)}, & \nu \leq \nu_{m} \\
0, & \nu > \nu_{m}
\end{cases}
{% end %}

Where we see that the frequency $\nu$ of a phonon is physically limited to $\nu \leq \nu_m$. Thus, the total internal energy due to the phonons is given by:

{% math() %}
\begin{align*}
U &= \int_{0}^{\nu_{m}} N(\nu) \varepsilon(\nu) d\nu \\
&= \int_{0}^{\nu_{m}} h\nu N(\nu) d\nu \\
&= \frac{9 Nh}{\nu_{m}^3} \int_{0}^{\nu_{m}} h\nu \frac{\nu^3 d\nu}{e^{h\nu / k T} - 1}
\end{align*}
{% end %}

Where $\varepsilon(\nu)$ is the energy of a phonon of frequency $\nu$, which we know is given by $\varepsilon = h\nu$. It is useful to define $\theta_D$, the **characteristic Debye temperature**, given by:

{% math() %}
\theta_{D} = \frac{h\nu_{m}}{k}
{% end %}

Therefore, with a couple of transformation of variables, we find that:

{% math() %}
C_{V} =  \left( \frac{\partial U}{\partial T} \right)_{V} =  \frac{9NkT^3}{(\theta_{D}^3)} \int_{0}^{\theta_{D}/T} \frac{x^4 e^x dx}{(e^x - 1)^2}
{% end %}

This integral is highly-nontrivial to evaluate; however, if we simply consider the low-temperature regime (at temperatures at or below the Debye temperature), we have:

{% math() %}
C_{V} \approx \frac{12 \pi^4 Nk}{5} \left( \frac{T}{\theta_{D}} \right)^3, \quad T \leq \theta_{D}
{% end %}

#### Partition function of a Debye solid

The partition function of a Debye solid can be written as:

{% math() %}
\ln Z = -9 \left( \frac{T}{\theta_{D}} \right)^3 \int_{0}^{\theta_{D} / T} x^2 \ln(1 - e^{-x}) dx
{% end %}

The Helmholtz function $F = -Nk T \ln Z$ can then be written as:

{% math() %}
F = 3 N k T \ln (1 - e^{- \theta_{D} / T}) - N k T D\left( \frac{\theta_{D}}{T} \right)
{% end %}

Where:

{% math() %}
D(\theta_{D} / T) = \frac{3}{(\theta_{D} / T)^3} \int_{0}^{\theta_{D} / T} \frac{x^3 dx}{e^x - 1}
{% end %}

This integral is non-trivial, but can be evaluated in the limit $\theta_D/T \gg 1$ and $\theta_D/T \ll 1$. We can then use this to calculate other characteristics of a Debye solid, although we will not do so here.

## Statistical mechanics of bosons

We will now take a look at two of the most famous predictions of statistical mechanics, both of which involve boson statistics:

- Blackbody radiation
- Bose-Einstein condensation

We will cover the former first. **Blackbody radiation** refers to the phenomenon that we observe the emission of electromagnetic radiation from all objects in the Universe, even those that are not actively producing light. A so-called *blackbody* is an idealized model of an object that has no color, since it absorbs all light across the electromagnetic spectrum, but emits *only* thermal radiation, making them black. It is important to keep in mind that a blackbody is an idealization; real objects usually have *some* amount of reflection (there are exceptions, such as black holes). However, with the idealized blackbody, we can apply the methods of statistical mechanics to analyze the electromagnetic radiation emitted. Importantly, blackbody radiation is *independent* of the type of atoms the object is composed of. This means we can use it to deduce an (effective) temperature of a body by just observing its color, which is very useful in astronomical studies.

To start, we know that electromagnetic radiation is technically composed of photons, so we must use a Bose-Einstein distribution for a “photon gas”. (Technically, there are other ways to derive the blackbody radiation formula, but this is the most straightforward method). Recall that the Bose-Einstein distribution is given by:

{% math() %}
\frac{N(\varepsilon)}{g(\varepsilon)} = \frac{1}{e^{\varepsilon / k T} - 1}
{% end %}

Using $\varepsilon = h\nu$, we can rewrite this as:

{% math() %}
\frac{N(\nu)}{g(\nu)} = \frac{1}{e^{h \nu / k T} - 1}
{% end %}

Where the density of states is similar to that for phonons, except with $v = c$ (since photons travel at the speed of light):

{% math() %}
g(\nu) d\nu = \frac{8\pi V \nu^2 d \nu}{c^3}
{% end %}

Meanwhile, the internal energy $U(\nu)$, expressed as a function of frequency, satisfies:

{% math() %}
U(\nu) d\nu = N (\nu) \varepsilon(\nu) d\nu = N(\nu) h \nu d \nu
{% end %}

Therefore, substituting this into $g(\nu) d\nu$ into $N(\nu)$, we obtain:

{% math() %}
\begin{align*}
N(\nu) &= \frac{g(\nu)}{e^{h \nu / k T}} - 1 \\
U(\nu) d \nu&= \frac{8\pi h V}{c^3}\left[ \frac{\nu^3 d\nu}{e^{h \nu / k T} - 1} \right]
\end{align*}
{% end %}

If we perform a change of variables to express $U(\nu)$ in terms of wavelength $\lambda$, we have:

{% math() %}
U(\lambda) = \frac{8\pi h c V}{\lambda^5(e^{hc / k T \lambda} - 1)}
{% end %}

The *energy density* $u$ is simply this value divided by the volume, that is, $u = U/V$, giving us the famous **Planck’s law** (also called the *Planck radiation distribution*):

{% math() %}
u(\lambda) = \frac{8\pi h c}{\lambda^5} \frac{1}{e^{hc / k T \lambda} - 1}
{% end %}

Or in terms of frequency:

{% math() %}
u(\nu) = \frac{8\pi h }{c^3} \frac{\nu^3}{e^{h \nu / k T} - 1}
{% end %}

![A plot of Planck’s law, showing different radiation curves at different temperatures](https://upload.wikimedia.org/wikipedia/commons/1/19/Black_body.svg)

_A plot of the Planck radiation distribution. Source: [Wikipedia](https://commons.wikimedia.org/wiki/File:Black_body.svg)_

The *total radiated energy density* can be found by integrating across all wavelengths, giving us:

{% math() %}
\begin{align*}
u_{total} &= \int_{0}^\infty u(\lambda) d\lambda \\
&= \frac{8\pi (kT)^4}{(hc)^3} \underbrace{ \int_{0}^\infty \frac{x^3 dx}{e^x - 1} dx }_{ \pi^4 / 15 }, \quad x \equiv \frac{hc}{k T \lambda} \\
&= \frac{8\pi (kT)^4}{h^3 c^3} \left( \frac{\pi^4}{15} \right)
\end{align*}
{% end %}

This gives us the **Stefan-Boltzmann law** $u_{total} = a T^4$, which gives a quadratic dependence of the radiated energy density on the temperature, with the proportionality constant given by:

{% math() %}
a = \frac{8\pi^5 k^4}{15 h^3 c^3} \approx 7.55 \times 10^{-16} \pu{ J*m^{-3} K^{-4} }
{% end %}

The Stefan-Boltzmann law is also often expressed in the form $e = \sigma T^4$, where $e$ is the **energy flux**, and $\sigma$ is the **Stefan-Boltzmann constant**, given by:

{% math() %}
\sigma = \frac{c a}{4}= 5.67 \times 10^{-8} \pu{ W*m^3 K^{-4} }
{% end %}

The maximum of the Planck radiation distribution, $\lambda_{max}$, is found at:

{% math() %}
\lambda_{max} = \frac{hc}{4.96 kT} \approx \frac{\pu{2.9E-3 m\cdot K }}{T}
{% end %}

If the wavelength is large such that $hc/\lambda k T \ll 1$, we may use the approximation $e^{hc / k T \lambda} \approx 1 + \frac{hc}{k T \lambda}$ (which comes from the first two terms in the Taylor series for the exponential function). This gives us:

{% math() %}
u(\lambda) = \frac{8\pi k T}{\lambda^4}, \quad \frac{hc}{\lambda k T} \ll 1
{% end %}

This is known as the **Rayleigh-Jeans law**, which is a good approximation to Planck’s law at long wavelengths (visible light and infrared), but fails in the UV spectrum, leading to the famous **ultraviolet catastrophe** that is now widely regarded as a failure of classical physics. Meanwhile, for short wavelengths such that $e^{hc / k T \lambda} \ll 1$, we can use the approximation $e^{hc / k T \lambda} -1 \approx e^{hc / k T \lambda}$. This gives us **Wien’s law**, a good approximation to Planck’s law at short wavelengths:

{% math() %}
u(\lambda) = \frac{8\pi h c}{\lambda^5} e^{-hc / k T \lambda}, \quad e^{hc / k T \lambda} \ll 1
{% end %}

We can also consider the heat capacity of the photon gas. Using the Stefan-Boltzmann relation $u_{total} \equiv \frac{U}{V} = a T^4$, we have:

{% math() %}
U = V a T^4
{% end %}

From which we may calculate the heat capacity at constant volume:

{% math() %}
C_{V} = \left( \frac{\partial U}{\partial T} \right)_{V} = 4 V a T^3
{% end %}

This allows us to calculate the entropy:

{% math() %}
S = \int \frac{dQ}{T} = \int \frac{C_{V}}{T} d T = \frac{4}{3} V a T^3
{% end %}

It can also be shown that the Helmholtz function $F$ of a photon gas is given by:

{% math() %}
F = U - TS =  -\frac{1}{3} V aT^4
{% end %}

And the pressure $P$ is given by:

{% math() %}
P = -\left( \frac{\partial F}{\partial V} \right)_{T, N} = \frac{1}{3} a T^4
{% end %}

### Bose-Einstein condensation

Bosons are uniquely distinguished from fermions by the fact that they do not obey the Pauli exclusion principle. This means that it is possible for a system of bosons to all occupy the ground state, forming what is known as a **Bose-Einstein condensate** (BEC). Moreover, it applies not only for *elementary particles* that are bosons, but also *composite particles*, including all atoms with integer spin. Bose-Einstein condensation has been observed in, among other elements, rubidium and helium atoms at very low temperatures.

To begin, recall that the Bose-Einstein distribution is given by:

{% math() %}
\frac{\mathcal{N}(\varepsilon)}{g(\varepsilon)} = \frac{1}{e^{(\varepsilon - \mu)/k T} - 1}
{% end %}

Where here we use the script $\mathcal{N}$ to represent the occupancy number (number of particles per energy level) because we will be using $N$ as the *total number* of particles in every energy level. Assuming a system of bosons (a “boson gas”) is in its ground state, where $\varepsilon = 0$, then the chemical potential $\mu$ *must* be a negative value for the units to make sense. Therefore, $\mu$ must switch sign at some temperature, meaning that is has to be a *function* of temperature.

To make the problem more tractable, it is useful to express the total number of particles $N$ as a sum of particles in the ground state, $N_0$, and the number of particles in the excited state, $N_{ex}$, as follows:

{% math() %}
N = N_{0} + N_{ex}
{% end %}

Then, we can integrate the Bose-Einstein distribution to find the total number of particles  in the excited and ground states. We will denote this as $N$:

{% math() %}
\begin{align*}
\int_{0}^\infty \mathcal{N}(\varepsilon) d\varepsilon
&= \int_{0}^\infty \frac{\mathcal{N}(\varepsilon)}{g(\varepsilon)} g(\varepsilon) d\varepsilon, \quad g(\varepsilon) 
= \frac{4\pi\sqrt{2}(V m^{3/2} \varepsilon^{1/2})}{h^2} \\
&= 2\pi V \left( \frac{2m}{h^2} \right)^{3/2} \int_{0}^\infty \frac{\varepsilon^{1/2} d\varepsilon}{e^{(\varepsilon - \mu) / k T} - 1}
\end{align*}
{% end %}

At low temperatures where $\varepsilon \approx 0$ and where $x = \mu/kT$, this integral can be simplified and evaluated (numerically) to find a value of:

{% math() %}
N \approx 2.612 V \left( \frac{2\pi m k T}{h^2} \right)^{3/2}
{% end %}

One then defines the **Bose temperature** $T_B$ to delineate between the high-temperature regime (where a Bose-Einstein condensate does not form) and the low-temperature regime (where a Bose-Einstein condense *can* form), where:

{% math() %}
T_{B} = \frac{h^2}{2\pi m k} \left( \frac{N}{2.612 V} \right)^{2/3}
{% end %}

Such that we may express the ratios of the ground state and excited state particle numbers to the total particle number as follows:

{% math() %}
\frac{N_{0}}{N} = 1 - \left( \frac{T}{T_{B}} \right)^{3/2}, \quad \frac{N_{ex}}{N} = \left( \frac{T}{T_{B}} \right)^{3/2}
{% end %}

We can understand these ratios as per the plot below:

{{ diagram(
	desc="A plot of the normalized excited vs ground state occupancy numbers of a boson gas"
	src="../bose-temp.excalidraw.svg"
	width=400
) }}

### Thermodynamic properties of a boson gas

We can also consider other properties of a boson gas, such as the internal energy:

{% math() %}
\begin{align*}
U &= \int_{0}^\infty \varepsilon N(\varepsilon) d\varepsilon \\
&= \frac{2V}{\sqrt{ \pi }} k T \left( \frac{2\pi m k T}{h^2} \right)^{3/2} \int_{0}^\infty \frac{x^{3/2} dx}{e^x - 1} , \quad x = \frac{\varepsilon}{kT} \\
&\approx 0.77 N k T \left( \frac{T}{T_{B}} \right)^{3/2}, \quad T < T_{B}
\end{align*}
{% end %}

Notice how the internal energy of an ideal gas, $U = (3/2) N k T$, is more than twice this value, meaning that this is a *very small* amount of energy. Meanwhile, the heat capacity is given by:

{% math() %}
C_{V} = \left( \frac{\partial U}{\partial T} \right)_{V} \approx 1.92 Nk \left( \frac{T}{T_{B}} \right)^{3/2}, \quad T < T_{B}
{% end %}

Which we can also express (approximately) as follows:

{% math() %}
C_{V} \approx \frac{5}{2} \left( \frac{U}{T} \right)
{% end %}

Meanwhile, the absolute entropy is:

{% math() %}
S = \int_{0}^T \frac{C_{V}}{T'} dT' = 1.28 N k \left( \frac{T}{T_{B}} \right)^{3/2}, \quad T < T_{B}
{% end %}

Which can also be written as:

{% math() %}
S \approx \frac{5}{3} \left( \frac{U}{T} \right)
{% end %}

Finally, the Helmholtz function and pressure are respectively given by:

{% math() %}
\begin{align*}
F &= U - TS \\ 
& \approx -0.51 N k T\left( \frac{T}{T_{B}} \right)^{3/2}, \quad T < T_{B} \\
& \approx -\frac{2}{3}U , \quad T < T_{B} \\
P &= -\left( \frac{\partial F}{\partial V} \right)_{T, N} \\
&\approx 1.33 k T\left( \frac{2\pi m k T}{h^2} \right)^{3/2}, \quad T < T_{B} \\
&\approx \frac{2}{3}\left( \frac{U}{V} \right),\quad T < T_{B} \\
\end{align*}
{% end %}
