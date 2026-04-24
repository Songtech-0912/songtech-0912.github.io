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
\varepsilon_{q, \ell, k} = \frac{\pi^2 \hbar^2}{2m} \left( \left( \frac{q}{L_{x}} \right)^2 + \left( \frac{\ell}{L_{y}} \right)^2 + \left( \frac{k}{L_{z}} \right)^2 \right), \quad q, \ell, k \in 1, 2, 3, \dots
{% end %}

Where $q = n_x$, $\ell = n_y$, $k = n_z$ are the quantum numbers in each direction. The **principal quantum number** $n_j$ for the $j$-th energy level is given by:

{% math() %}
n_{j}^2 = q^2 + \ell^2 + k^2 = n_{x}^2 + n_{y}^2 + n_{z}^2
{% end %}

Meanwhile, the degeneracy of the $j$-th energy level is always greater than 1 for anything except the ground state (where $n = \ell = k = 1$). Assuming that the box has volume $V = L_{x}L_{y} L_{z}$, we can then write the energy levels with:

{% math() %}
\varepsilon_{j} = \frac{n_{j}^2 \pi^2 \hbar^2 }{2m}V^{-2/3}
{% end %}