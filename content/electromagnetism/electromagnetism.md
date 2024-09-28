+++
title = "Electromagnetism"
date = 2024-05-15
+++

These notes consist of a comprehensive guide to electromagnetism from the classical theory all the way to quantum electrodynamics. Topics covered include Coulomb's law, electromagnetic fields, Maxwell's equations, the wave nature of light, second quantization, and the quantum description of electromagnetism.

<!-- more -->

## Introduction

All that we can see, feel, and touch is the product of one fundamental interaction in physics - the electromagnetic interaction. It is due to electromagnetism that contact forces exist, that photons can interact             with electrons, and that radio, satellite, and internet communications are possible at all. The relativistic nature of electromagnetism also has a key role in relativity and the theories of spacetime.

## Electric forces

Objects are **charged** due to an imbalance in their number of protons and electrons. As protons are immobile, the *movement of electrons* causes changes in charge. Objects gaining electrons become negatively-charged, objects losing electrons become positively charged.

As is well-known, like charges attract, and opposing charges repel, causing a force between any two charges $Q$ and $q$ placed together. The magnitude of this attraction (or repulsion) can be found from Coulomb's law:

{% math() %}
F_e = \frac{kQq}{r^2}
{% end %}

The **vector form** of Coulomb's law is found by taking the scalar form and adding a unit vector:

{% math() %}
\vec F_e = \frac{kQq}{r^2} \hat r
{% end %}

Charges are discrete, but when there are enough of them distributed throughout a volume, we may consider *continuous* charges. That is, we may define a charge density function $\rho(\vec x, t)$ such that:

{% math() %}
Q = \int_V \rho(\vec x, t)~d^3 x
{% end %}

> Interlude for the advanced reader: the charge density function for a single charge $q$ can be written using the Dirac delta function $\rho(\vec x, t) = q\delta(\vec x - \vec x_0)$

## Electric potential energy

Electrical forces do work, and therefore, systems of charges store energy. The stored energy is equivalently called the **electrical potential energy**, and for a system of two charges $Q$ and $q$, it is given by:

{% math() %}
U_e = -\frac{kQq}{r}
{% end %}

This may be derived through the definition of electrical work as the work done against the electrical force. Work - that is, a _transfer of enegy_ - must be put in to assemble a system of charges, because the electrical force would otherwise prevent the system from. That energy of assembly is stored in the system, and is the electrical potential energy. Therefore, from using the integral definition of work:

{% math() %}
U_e = -W_e = -\int_{r_0}^r \frac{kQq}{\tilde r^2}~d\tilde r = -\int_{\infty}^r \frac{kQq}{\tilde r^2}~d\tilde r = -\frac{kQq}{r}
{% end %}

> Note: the tildes (~) are used to prevent confusion with the integration bound variables.

## Electric fields and potentials

The **electric field** is vector field produced by charges and extends throughout space, exerting a force on charges. The electric field created by a single charge $q$ given by:

{% math() %}
\vec E = \frac{kq}{r^2} \hat r
{% end %}

Or, equivalently:

{% math() %}
\vec F_e = m \frac{d^2 x}{dt^2} = q \vec E
{% end %}

When the electric field is created by a dipole or any case with more than one charge, we must sum the individual electric fields from each charge:

{% math() %}
\vec E = \sum_i \frac{kq_i}{r_i} \hat r
{% end %}

Electrical fields also have an associated quantity known as the **electric potential**, which is a scalar field that accompanies the vector electric field. When charges are placed in an electrical field, their potential energy is equal to the energy stored at that point in the field. The electrical potential, typically denoted $V$, formalizes this concept; it assigns a potential energy to a given charge in an electrical field, based on its location in space. The electrical potential energy of a charge $q$ placed into an electric field with electric potential $V$ is given by:

{% math() %}
U = qV
{% end %}

And the electric field itself can be written in terms of the electrical potential via the **gradient theorem**:

{% math() %}
\vec E = -\nabla V
{% end %}
