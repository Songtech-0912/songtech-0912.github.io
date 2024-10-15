+++
title = "Fundamentals of Chemistry"
date = 2024-09-26
+++

This is a mini-book on chemistry, including atomic structure, general chemistry and the theory of reactions, using chemical equations, stoichiometry, Lewis theory, and a brief introduction to quantum chemistry. Topics to be added with time include valence bonding theory, VSEPR theory, and energy changes within reactions.

<!-- more -->

I owe a debt of gratitude to Professor [Steven Tysoe](https://faculty.rpi.edu/steven-tysoe) of Rensselaer Polytechnic Institute for his instruction and permission to share this with everyone, and I have tried to ensure there are as few sentences copied verbatim from his lecture materials as possible. There is no need for attribution for redistributing this mini-book in part of in whole, or permission to use them for commercial purposes. In fact, I release it to the public domain (dual licensed with Creative Commons CC0, whichever is more permissive in the given jurisdiction) so that **it belongs to everyone**. Copy from it, study from it, and give it to others freely and without limits - I would welcome that!

In these notes, there is general information as well as optional asides for more advanced/interested readers that are _not important_ for studying general chemistry. Read the asides only if interested, otherwise, just read the main content.

## A high-level introduction to chemistry

Chemistry is the empirical (evidence and experimentally-based) study of the matter and the interactions of matter that analyzes the **microscopic properties** of matter to describe its **macroscopic** behavior.

While physics is usually on the scale of generally big life-sized things (projectiles, rockets, trains), very big things (black holes, galaxies, the entire universe even) or very very small things (elementary particles like electrons and quarks), chemistry analyzes things on the scale of atoms and molecules, and up to compounds and materials, that generally form a bigger whole.

Stability (that is, descent to a lower energy state that is more stable) and conservation (quantities that do not change) are essential to chemistry. In addition, the behavior of electrons is essential to understanding chemical interactions. This is because electrons are the mediators of the electromagnetic interaction and therefore responsible for **all** chemistry (other than nuclear chemistry). Armed with this knowledge, we can explain the rich and diverse landscape of chemistry.

## The quantum origins of chemistry

Fundamental chemistry comes from the quantum world that governs matter on the atomic and subatomic scales. Atoms constitute the fundamental building blocks of ordinary matter. Therefore, atoms and the structures they form are the main objects of study in chemistry.

Atoms are not the only important factor in the chemical properties of matter. For instance, graphite and diamond are both composed of carbon atoms, but their differing *arrangement* of electrons results in greatly different macroscopic properties.

As a high-level overview, matter is anything that *occupies space* (more technically, a cross-sectional area in which it interacts) and has *mass*. The **structure and composition** of matter determines its **properties**. In addition, the energy present in matter determines its state and structure. Energy is divided into two general types, kinetic energy and potential energy (energy that is stored in some thing and capable of being released). In chemistry, kinetic energy measured macroscopically typically takes the form of **thermal energy** (heat) and potential energy measured macroscopically typically takes the form of **chemical energy**.

> **Note for the advanced reader:** Chemical energy, which we can broadly speak of as energy stored in chemical bonds, is actually the sum of the individual electromagnetic potential energies associated with each of the electrons in matter. The results of quantum electrodynamics (a type of quantum field theory) is necessary for a complete description of chemical energy in terms of the energy of the individual electrons that form the total chemical energy we consider in chemistry. Nuclear chemistry in addition extends this to the theories of quantum chromodynamics. This will be explained in an optional section further down but is **not** necessary for general chemistry or even conventional treatments of the quantum chemistry which simply use the Schrödinger equation and non-relativistic quantum mechanics.

## The chemistry lexicon

An **intensive property** is a characteristic that is intrinsic to a substance, but an **extensive property** can vary based on how much of the substance there is. 

**Significant figures** are the proper way to record scientific measurement, which involves writing a value in terms of a value and an uncertainty in the form of limited precision, such as $3.57 \pm 0.005\ \pu{kg}$. Significant figures ignore leading zeroes and round after a certain number of digits, truncating the rest and (often) writing an uncertainty to represent the fact that values were omitted.

**Accuracy** and **precision** are not identical in chemistry and have specific meanings. **Accuracy** is how well a measurement can be made to ensure that it is as close as possible to the real value. **Precision** is a measure of the spread of a measurement.

**Units** are a prerequisite for doing chemistry. The SI system of measurement is the predominant unit system used in science, but regardless of what unit is used, you should **never** report a measurement without units (unless if the quantity is dimensionless).

## Modern atomic theory

Modern atomic theory regards substances according to three key observations of nature:

- The **conservation of mass** - no mass is created or destroyed within a chemical reaction
- The **law of definite proportions** - the reactants participating in a chemical reaction are *proportional* to their products and furthermore these ratios must be *whole positive numbers*
- The **law of multiple proportions** - the ratios of reactants to products in chemical reactions are _fixed ratios_ no matter the quantities involved in the reaction; this means you can scale up the amounts of reactants but the formulas and laws describing the reaction will stay the same

> Note: the law of the conservation of mass takes a different form in relativistic quantum chemistry, in which case mass and energy may be converted into each other, and mass posseses intrinsic energy.

The chemist **John Dalton** was one of the originators of atomic theory. He recognized that elements do not magically turn into each other; rather they participate in chemical reactions that change the compounds they form. Chemist **J. J. Thomson** proved the existence of electrons as particles that are inside of atoms. Rutherford's **gold foil experiment** found that electrons are negatively charged, and that the nucleus is positively charged. Eventually, it was found that neutral **neutrons** as well as positively-charged **protons** made up of the nucleus. 

Elements are identified by the atomic number $Z$ which is the number of **protons** within the atom, as well as the atomic mass $A$ which is the sum of the number of protons and number of neutrons as given in atomic mass units $\pu{amu}$. We therefore notate an element with $\ce{^A_Z S}$ where $S$ is the element name. For instance, $\ce{^4_2 He}$ denotes the helium atom, with an atomic mass of 4 (2 protons and 2 neutrons) and an atomic number of 2 (because of its two protons).

Due to the equal and opposite charges of electrons as compared to protons, there are *equal* numbers of electrons and protons in a neutral atom, so that atoms are generally electrically neutral and thus stable. However, the same element can have different numbers of neutrons; variations of the same element are called **isotopes** and are important for nuclear chemistry and nuclear physics. One common example is uranium, which has several well-known isotopes, uranium-238 denoted {% inlmath() %}\ce{^{238}_{92} U}{% end %}, and uranium-235 denoted {% inlmath() %}\ce{^{235}_{92} U}{% end %}.

## Periodic table

The **periodic table** categorizes the properties of all known elements. All elements are represented by a specific *chemical symbol*, such as $\ce{Cu}$ for copper, $\ce{Fe}$ for iron, and $\ce{C}$ for carbon. The original periodic table was able to predict the properties of 2 then-unknown elements, affirming its success as a theory of the elements. The phenomena that allows the periodic table to exist is called **periodicity**, where repeating groups of elements share the same chemical properties. This is caused by the arrangement of valence (outermost) electrons, which are the same in elements of the same group. For example, the alkali metals (sodium, potassium, cesium, etc. referred together as group I) all have one valence electron. The underlying reasons behind periodicity, however, must be explained in the quantum behavior of electrons, which will be covered further down.

