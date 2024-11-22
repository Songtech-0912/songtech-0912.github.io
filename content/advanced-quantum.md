+++
title = "A practical guide to quantum field theory"
date = 2024-07-19
draft = true
+++

Quantum field theory (QFT) is the our most accurate description of the universe. The standard model, a comprehensive quantum field theory, is the backbone of modern physics, and has been tested to [extreme precision](https://en.wikipedia.org/wiki/Precision_tests_of_QED). Despite this, quantum field theory has a reputation for not being very accessible, in part due to its [scary-long Lagrangians](https://www.symmetrymagazine.org/article/the-deconstructed-standard-model-equation) and [incredibly formidable integrals](https://arxiv.org/pdf/1307.4337). So this is an informal guide to QFT in plainer language, targetted for advanced physics students.

<!-- more -->

## What you should know

We'll be working with natural units where $c = \hbar = 1$ simply out of convenience. As this is an informal guide I won't be going through everything in detail. Also, everything will be in tensors, see the [tensors guide](@/tensors-guide.md) if you're not familiar with those. We will be working in the formalism of Lagrangian and Hamiltonian field theory as is standard in physics.

## A few things to clear up

Quantum field theory has a lot of confusing parts, and so it's best to understand these before going too far into it:

- Quantum field theory is **not** string theory, they are distinct theories that share some similarities but are not extensions of each other
- Even though it is mostly used in very specific cases due to its complexity, quantum field theory is a **more fundamental theory** than classical field theory and classical field theory is its limiting case
- The interpretations of PDEs (equations of motion) is **different** in quantum field theory as compared to quantum mechanics; quantum field theory PDEs, even complex-valued ones, have none of the probability interpretation of the Schrödinger equation

## Canonical quantization

Start with your Lagrangian. If you don't know one and can't copy one from a book or ask someone, then just propose one (i.e. make an educated guess). For instance, if you were studying the electron field, then maybe you would want to use this Lagrangian:

{% math() %}
\mathscr{L} = \overline \psi (i \gamma^\mu \partial_\mu - m) \psi
{% end %}

Plug that Lagrangian into Euler-Lagrange equations, here with $\varphi = \psi(x^\nu)$:

{% math() %}
\frac{\partial \mathscr{L}}{\partial \varphi} - \partial_\mu \left(\frac{\partial \mathscr{L}}{\partial (\partial_\mu \varphi)}\right) = 0
{% end %}

Then you get the equations of motion of the field (PDEs). E.g. for Higgs field this is the complex-valued Klein-Gordon equation, for quarks & electrons this is the Dirac equation, for photons this is Maxwell's equations. In our case this is the Dirac equation, which describes all matter fields (i.e. those of electrons and quarks, which make up all atoms):

{% math() %}
(i \gamma^\mu \partial_\mu - m) \psi = 0
{% end %}

The associated quantum fields obey the operator equations of motion, which are the **same** as the PDE equations of motion but operator-valued. For the electron field this is:

{% math() %}
(i \gamma^\mu \partial_\mu - m) \hat \psi = 0
{% end %}

Where we just made the change $\psi \to \hat \psi$ to get an operator-valued equation of motion. You solve for those operator equations of motion by first solving the PDE equation of motion for the field. Then from there you can promote the field to an operator. I mean, you could solve the operator equation of motion directly but that's annoying, like what does a partial derivative of an operator mean??? so it's easier to just solve the PDE equation of motion and then promote the solution to an operator rather than directly trying to solve the operator equation of motion.

## Path integrals

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

A similar procedure works in QFT!

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

Up to this point, we have been operating within the realm of known physics. We know the right-hand side of this equation: it is simply the combined stress-energy operator of the standard model. And we know that the left-hand side must hold true, due to the correspondence principle. But we _don't_ know what form the left-hand side must take, that is, what the operators have to be to satisfy this operator equation.

## Referenced sources

- https://www.quora.com/What-is-the-most-complex-Feynman-Diagram