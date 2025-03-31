+++
title = "In-Depth Classical Electromagnetism"
date = 2025-03-17
draft = false
+++

This is a guide to classical electromagnetism beyond the basics, tackling boundary-value problems in electrostatics and magnetostatics, electric and magnetic fields within materials, and relativistic electrodynamics.

<!-- more -->

I thank [Professor Persans](https://faculty.rpi.edu/peter-persans) at Rensselaer Polytechnic Institute, without whom this guide would not have been possible.

## Introduction to classical electromagnetism

**Classical electromagnetism** concerns the study of electrical and magnetic phenomena. It postulates that electricity and magnetism are phenomena that may be modelled using notions of _charge_, _current_, and _fields_. Charge is a fundamental property of objects that gives rise to electricity and magnetism; current is the flow of charge; and fields are physical quantities that span space and transmit interactions between objects (which, in this case, are _charged_ objects).

In classical electromagnetism, there exists an **electromagnetic field**, with electrical and magnetic components that form one singular field. For mathematical convenience, we may separately analyze the electric components as a _electric field_ and the magnetic components as a _magnetic fields_. We represent the electric field using a vector-valued function $\mathbf{E}(\mathbf{r}, t)$ and the magnetic field using a vector-valued function $\mathbf{B}(\mathbf{r}, t)$.

**Units** are a fundamental part of describing electromagnetic phenomena. The units used in this guide are the **SI units system**, also called MKS(A) units (which stands for _meter-kilogram-second-ampere_). The following SI units are a short list of those commonly used in electromagnetic theory:

| Unit     | Symbol    | Used for                |
| -------- | --------- | ----------------------- |
| Ampere   | $\pu{A}$  | Electric current        |
| Coulomb  | $\pu{C}$  | Electric charge         |
| Tesla    | $\pu{T}$  | Magnetic field strength |
| Weber    | $\pu{Wb}$ | Magnetic flux           |
| Newton   | $\pu{N}$  | Electric/magnetic force |
| Henry    | $\pu{H}$  | Inductance              |
| Kilogram | $\pu{kg}$ | Mass                    |
| Hertz    | $\pu{Hz}$ | Frequency               |
| Ohm      | $\Omega$  | Resistance              |
| Volt     | $\pu{V}$  | Potential difference    |
| Joule    | $\pu{J}$  | Energy                  |
| Watt     | $\pu{W}$  | Power                   |

> **Note:** Alternate units used in theoretical physics are Gaussian units, Lorentz-Heaviside units, and natural units. These simplify many equations in electromagnetic theory, at the cost of being much more unfamiliar and far less used in daily life.

Note that a lot of this guide follows the excellent textbook by David Griffiths, _Introduction to Electrodynamics_ (although this guide is not affiliated with Griffiths). It is highly-recommended to purchase a copy of the book as additional supplementary material to follow along with the course.

### Mathematical prerequisites

The primary mathematics used in electromagnetics is **vector calculus**, the calculus of vectors and vector-valued functions in 3D space. We additionally use some harmonic (Fourier) analysis and infinite series, and also some special functions; we will quickly review all of these. Towards the end, we will encounter special relativity and tensor calculus, but the mathematics of tensors will be explained when we reach that section.

> **Note:** this is _not intended_ to be a complete review of all the mathematics involved (and is extremely fast-paced, which may not be ideal for first-time learners unfamiliar with the material). For a more extensive review on vector calculus, we suggest consulting the [multivariable calculus](@/multivariable-calculus/index.md) or [vector calculus](@/vector-and-advanced-calculus/index.md) guides, or read through the [introductory electromagnetic theory](@/electromagnetism/index.md) notes.

Consider a function of a single variable $f(x)$. Then the ordinary derivative of the function is given by:

{% math() %}
\frac{df}{dx}
{% end %}

Now consider a function of multiple variables $f(x, y, z)$. Since the function has multiple inputs, the function changes at a different rate when each input is varied. Therefore, the function has more than a single derivative. We term each derivative a _partial derivative_, denoted:

{% math() %}
\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}, \frac{\partial f}{\partial z}
{% end %}

To compute the partial derivatives, we imagine that any variable other than the variable that is differentiated with respect to is a constant, and we can factor them out. For example:

{% math() %}
\frac{\partial}{\partial x} (3x^2 y) = 3y \frac{\partial}{\partial x} x^2 = 6xy
{% end %}

Of course, we can take higher derivatives too, such as:

{% math() %}
\frac{\partial^2 f}{\partial x^2} = \frac{\partial}{\partial x} \left(\frac{\partial f}{\partial x}\right)
{% end %}

We can also define other types of derivatives for multivariable functions. For instance, we can collect all the partial derivatives together into a vector, which we call the gradient and we denote with the symbol $\nabla$:

{% math() %}
\nabla f = \left\langle \frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}, \frac{\partial f}{\partial z}\right\rangle = \frac{\partial f}{\partial \mathbf{r}} \hat r
{% end %}

A multivariable function can be one that returns a vector instead of a number. Such a function would be denoted $\mathbf{F}(x, y, z) = \langle F_x, F_y, F_z\rangle$. Then we can define a vector derivative called the _divergence_, represented with the same $\nabla$ symbol with a dot:

{% math() %}
\operatorname{div} \mathbf{F} = \nabla \cdot \mathbf{F} = \frac{\partial F_x}{\partial x} + \frac{\partial F_y}{\partial y} + \frac{\partial F_z}{\partial z}
{% end %}

Similarly, we can define a vector derivative called the _curl_, represented with the $\nabla \times$ symbol:

{% math() %}
\operatorname{curl} \mathbf{F} = \nabla \times \mathbf{F} = \left \langle \frac{\partial F_z}{\partial y} - \frac{\partial F_y}{\partial z}, \frac{\partial F_x}{\partial z} - \frac{\partial F_z}{\partial x}, \frac{\partial F_y}{\partial x} - \frac{\partial F_x}{\partial y}\right \rangle
{% end %}

The notations for the divergence and curl are inspired by the notations for the vector dot and cross products; these become exact when, just like we can represent the differentiation operator with $\displaystyle \frac{d}{dx}$, we can represent the multivariable differentiation operator (also called the nabla operator) with:

{% math() %}
\nabla = \left\langle \frac{\partial}{\partial x}, \frac{\partial}{\partial y}, \frac{\partial}{\partial z} \right\rangle
{% end %}

With this "vector", applying the dot product and cross product formulas using $\nabla$ becomes the divergence and the curl, respectively. Finally, we have the Laplacian ("multivariable second derivative") which is given by the divergence of the curl and denoted $\nabla^2$:

{% math() %}
\nabla^2 f = \nabla \cdot \nabla f = \frac{\partial^2 f}{\partial x^2} + \frac{\partial^2 f}{\partial y^2} + \frac{\partial^2 f}{\partial z^2}
{% end %}

Multivariable integration is very similar to a partial derivative, the idea is that we separate a multivariable integral into partial integrals, where integrate only with respect to one variable at a time for each individual integral. For instance, a 3D integral might be something like:

{% math() %}
\int f(x, y, z)~dV = \iiint f(x, y, z)~dx~dy~dz
{% end %}

Here the way we solved it was to expand the integral as three individual integrals, one each for $x, y, z$. Then we do each of the integrals one by one, integrating just one variable at a time and  treating all the other variables as constant:

{% math() %}
\int \left[\int \left[\int f(x, y, z) dx\right] dy\right] dz
{% end %}

There are several different types of multivariable integrals: line integrals, which are single integrals over a path, surface integrals, which are double integrals over surfaces, and volume integrals, which are triple integrals over space. It sometimes is easiest by rewriting these integrals in terms of an integration element, just like $dV = dx~dy~dz$ for volume integrals or $dA = dx~dy$ for surface integrals or $d\ell = dx \hat i + dy \hat j + dz \hat k$ for line integrals, then expand, then solve via partial integration. While this is mathematically completely non-rigorous, the physics works out just fine. Also, note that sometimes, we add a circular loop around the integral sign - this means whatever is integrated over is closed, such a closed loop for line integrals or a closed surface for surface integrals:

{% math() %}
\begin{align*}
\oint \mathbf{F} \cdot d\mathbf{r} \\
\oint \mathbf{B} \cdot d\mathbf{A}
\end{align*}
{% end %}

#### Curvilinear coordinate systems

We find that when solving some problems in electromagnetism, it is easier to use a non-Cartesian coordinate system, such as polar, cylindrical, and spherical coordinates. This is especially the case if the problem is rotationally symmetric. We illustrate the three most common non-Cartesian coordinate systems below: **polar coordinates**, **cylindrical coordinates**, and **spherical coordinates**.

{{ wideimg(
	desc="An illustration of the polar, cylindrical, and spherical coordinate systems",
	src="cartesian-polar-cylindrical-spherical.excalidraw.svg"
) }}

Polar coordinates use $(r, \theta)$ to describe the location of a point, where $r$ is the radial distance from the origin to the point, and $\theta$ is the angle the point makes with the $x$ axis. Polar coordinates are related to Cartesian coordinates by:

{% math() %}
\begin{align*}
x = r \cos \theta \\
y = r \sin \theta
\end{align*}
{% end %}

Cylindrical coordinates extend the polar coordinate system into 3D space. It uses the coordinates $(\rho, \phi, z)$ to describe the location of a point, where $\rho$ and $\phi$ describe the point's location along the $xy$ plane, and $z$ describes the point's elevation _above_ the $xy$ plane (you may also sometimes see the coordinates written as $(r, \theta, z)$ or $(r, \phi, z)$ but I prefer this form since it allows using the same $\phi$ as in spherical coordinates, as we'll soon see). The conversion from cylindrical coordinates to polar coordinates are given by:

{% math() %}
\begin{align*}
x &= \rho \cos \phi \\
y &= \rho \sin \phi \\
z &= z
\end{align*}
{% end %}

Finally, spherical coordinates describe the location of a point with coordinates $(r, \theta, \phi)$, where $r$ is the absolute distance from the point to the origin, $\theta$ is the angle of elevation the point makes with the $xy$ plane, and $\phi$ is the same (rotational) angle as the $\phi$ in cylindrical coordinates. The conversions from spherical coordinates to Cartesian are given by:

{% math() %}
\begin{align*}
x &= r \sin \theta \cos \phi \\
y &= r \sin \theta \sin \phi \\
z &= r \cos \theta
\end{align*}
{% end %}

#### The Dirac delta and Kronecker delta

In addition to vector calculus, classical electromagnetism also uses two special "functions" - the **Kronecker Delta** and **Dirac Delta**. These are technically speaking _not_ functions, but in many ways they are similar to functions and (specifically in the case of the Dirac delta) can be treated like a function.

The Kronecker delta is written $\delta_{mn}$, where:

{% math() %}
\delta_{mn} = \begin{cases}
0, & m \neq n \\
1, & m = n
\end{cases}
{% end %}

The Kronecker Delta is very useful in expressing _orthogonality_. Orthogonality may be more familiar when discussed using vectors; two unit vectors have a dot product of zero when they are parallel (and thus equal to each other) and one when they are orthogonal (perpendicular to each other). However, we may generalize this principle for _functions_. The orthogonality relations for the sine function, for instance, are given by:

{% math() %}
\begin{align*}
\int_{-\ell}^\ell \sin \left(\dfrac{m\pi x}{\ell}\right)  \sin \left(\dfrac{n\pi x}{\ell}\right)\,dx &= \ell \delta_{mn} =
\begin{cases}
\ell ,& m = n \\
0, & m \neq n
\end{cases} \\
\int_{0}^\ell \sin \left(\dfrac{m\pi x}{\ell}\right)  \sin \left(\dfrac{n\pi x}{\ell}\right)\,dx &= \dfrac{\ell}{2} \delta_{mn} =
\begin{cases}
\ell/2 ,& m = n \\
0, & m \neq n
\end{cases}
\end{align*}
{% end %}

And for the cosine function, we have:

{% math() %}
\int_{0}^\ell \cos \left(\dfrac{m\pi x}{\ell}\right)  \cos \left(\dfrac{n\pi x}{\ell}\right)\,dx = \dfrac{\ell}{2} \delta_{mn} =
\begin{cases}
\ell/2 ,& m = n, & m, n \neq 0 \\
\ell, & m = n = 0 \\
0, & m \neq n
\end{cases}
{% end %}

The Dirac delta is a _generalization_ of the Kronecker delta (which takes a binary discrete input) for continuous inputs. It is defined by:

{% math() %}
\delta(x) = \begin{cases}
0, & x \neq 0 \\
1, & x = 0
\end{cases}
{% end %}

> **Note:** the Dirac delta can be thought of as a function that looks like a "spike" at $x = 0$ and is zero everywhere else.

The Dirac delta's usefulness mostly comes from the fact that it possesses a very special integral:

{% math() %}
\int_a^b \delta(x)\, dx = 1
{% end %}

Which also means that if the Dirac delta were displaced by a certain amount $x'$, then assuming $a < x' < b$:

{% math() %}
\begin{align*}
\int_a^b f(x)\delta(x- x') &= f(x') \\
\int_a^b f(x')\delta(x-x') &= f(x)
\end{align*}
{% end %}

This is incredibly useful (as we'll see) for describing quantities that exist only at one point in space (e.g. a point charge, which has the charge density $\rho(\mathbf{r}) = Q\delta(\mathbf{r}-\mathbf{r}')$).

Note that the Dirac delta can also be generalized to 2D (where it is written $\delta^2(\mathbf{r} - \mathbf{r}')$) and 3D (where it is written $\delta^3(\mathbf{r} - \mathbf{r}')$. The following expressions are for the 2D Dirac delta expressed in Cartesian and polar coordinates:

| Coordinate system   | Expression for Dirac Delta "function"                                                 |
| ------------------- | ------------------------------------------------------------------------------------- |
| Cartesian $(x, y)$  | $\delta^2(\mathbf{r} - \mathbf{r}') = \delta(x - x')\delta(y-y')$                     |
| Polar $(r, \theta)$ | $\delta^2(\mathbf{r} - \mathbf{r}') = \dfrac{1}{r}\delta(r-r')\delta(\theta-\theta')$ |

And the following expressions are for the 3D Dirac delta $\delta^3(\mathbf{r} - \mathbf{r}')$ in Cartesian, cylindrical, and spherical coordinates:

| Coordinate system             | Expression for Dirac Delta "function"                                                                                          |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| Cartesian $(x, y, z)$         | $\delta^3(\mathbf{r} - \mathbf{r}') = \delta(x-x')\delta(y-y')\delta(z-z')$                                                    |
| Cylindrical $(\rho, \phi, z)$ | $\delta^3(\mathbf{r} - \mathbf{r}') = \dfrac{1}{\rho}\delta (\rho - \rho')\delta(\phi-\phi')\delta(z-z')$                      |
| Spherical $(r, \theta, \phi)$ | $\delta^3(\mathbf{r} - \mathbf{r}') = \dfrac{1}{r^2 \sin \theta} \delta(r - r') \delta(\theta - \theta') \delta(\phi - \phi')$ |

We have now completed our short review of the essential mathematics for studying electromagnetism. Again, see the dedicated resources in the [calculus series](@/calculus-series.md) for a slower-paced, more detailed guide to all of these topics. But for the purposes of this guide, we will now move on to the exciting part - the physics of electromagnetism.

### Review of Maxwell's equations

In introductory electromagnetic theory, we have found that the fundamental laws of electromagnetism are **Maxwell's equations**, a series of four coupled partial differential equations that describe the electric and magnetic fields:

| Equation name               | Integral form                                                                                                                                                                      | Differential form                                                                                          |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Gauss's law for electricity | $\displaystyle \oint \mathbf{E} \cdot d\mathbf{A} = \dfrac{1}{\varepsilon_0} \int \rho\, dV$                                                                                       | $\nabla \cdot \mathbf{E} = \rho/\varepsilon_0$                                                             |
| Gauss's law for magnetism   | $\displaystyle \oint \mathbf{B} \cdot d\mathbf{A} = 0$                                                                                                                             | $\nabla \cdot \mathbf{B} = 0$                                                                              |
| Faraday's law               | $\displaystyle \oint \mathbf{E}\cdot d\mathbf{r} = -\dfrac{d}{dt} \displaystyle \iint \mathbf{E} \cdot d\mathbf{A}$                                                                | $\nabla \cdot \mathbf{E} = -\dfrac{\partial \mathbf{B}}{\partial t}$                                       |
| Ampere-Maxwell law          | $\displaystyle \oint \mathbf{B} \cdot d\mathbf{r} = \mu_0 \iint \mathbf{J} \cdot d\mathbf{A} + \mu_0 \varepsilon_0 \dfrac{d}{dt} \displaystyle \iint \mathbf{B} \cdot d\mathbf{A}$ | $\nabla \cdot \mathbf{B} = \mu_0 \mathbf{J} + \mu_0 \varepsilon_0 \dfrac{\partial \mathbf{E}}{\partial t}$ |

We also found that light is an electromagnetic phenomenon, and that the speed of light $c$ in vacuum can be expressed in terms of the electric constant $\varepsilon_0$ and the magnetic constant $\mu_0$ as:

{% math() %}
c = \dfrac{1}{\sqrt{\mu_0 \varepsilon_0}}
{% end %}

> **Note:** the speed of light will be different inside of materials; it is only its speed in vacuum that is constant and takes the value of $c$. For instance, light passes about 33% slower through glass and 58% slower through diamond, and significantly slowly in materials cooled to almost absolute zero. However, the _vacuum_ speed of light is a universal constant and stringent experimental tests have found no difference in the vacuum speed of light in a variety of different conditions.

Finally, we found that the equations of motion of a charged particle in an electromagnetic field follow the Lorentz force law $m\ddot {\mathbf{r}} = q(\mathbf{E} + \mathbf{v} \times \mathbf{B})$, formed by a combination of the electric force $\mathbf{F}_E = q\mathbf{E}$ and the magnetic force $\mathbf{F}_B = q\mathbf{v} \times \mathbf{B}$. In the special case where charged particles are moving at a significant fractional of the speed of light, they follow the relativistic version of the same law:

{% math() %}
\dfrac{d}{dt}\left(\dfrac{mv}{\sqrt{1 - (v/c)^2}}\right) = q(\mathbf{E} + \mathbf{v} \times \mathbf{B})
{% end %}

### Review of electrostatics

Previously in introductory electromagnetic theory, we discussed the concepts of electric force and electric field in **electrostatic scenarios**. Electrostatics governs the behavior of slow-moving and stationary charges. The electric force exerted **by** charge $q_1$ **on** charge $q_2$ (pay attention to the order) is given by **Coulomb's law**:

{% math() %}
\mathbf{F}_\text{1 on 2} = \dfrac{k q_1 q_2}{|\mathbf{r}_2 - \mathbf{r}_1|^3} (\mathbf{r}_2 - \mathbf{r}_1)
{% end %}

Where $\mathbf{r}_2 - \mathbf{r}_1$ is the _displacement vector_ between the positions of the charges, and points from $q_1$ to $q_2$. For $n$ charges, the electric force is the sum of all the individual electric forces:

{% math() %}
\mathbf{F}_\mathrm{total} = \mathbf{F}_\text{1 on 2} + \mathbf{F}_\text{3 on 2} + \mathbf{F}_\text{4 on 2} + \dots + \mathbf{F}_{n\ \text{on 2}}
{% end %}

> **Note:** You may wonder why the denominator of Coulomb's law contains a cubed term when the electric force is known to be an _inverse-square law_. The answer is more apparent if we rewrite Coulomb's law in terms of a _unit vector_ {% inlmath() %}\hat r_{12} = \dfrac{\mathbf{r}_2 - \mathbf{r}_1}{|\mathbf{r}_2 - \mathbf{r}_1|}{% end %}, for which Coulomb's law can be written as {% inlmath() %}\mathbf{F}_\text{1 on 2} = \dfrac{kq_1 q_2}{|\mathbf{r}_2 - \mathbf{r}_1|} \hat r_{12}{% end %} which translates to {% inlmath() %}\mathbf{F}_\text{1 on 2} = \dfrac{kq_1 q_2}{|\mathbf{r}_2 - \mathbf{r}_1|} \dfrac{\mathbf{r}_2 - \mathbf{r}_1}{|\mathbf{r}_2 - \mathbf{r}_1|} = \dfrac{k q_1 q_2}{|\mathbf{r}_2 - \mathbf{r}_1|^3} (\mathbf{r}_2 - \mathbf{r}_1){% end %}.

Calculating electric forces may _seem_ deceptively simple, but for large numbers of charges it becomes very challenging due to the large number of inter-charge forces. It is much easier to instead calculate an _electric field_, and use the electric force law $\mathbf{F}_E = q\mathbf{E}$ to calculate the total electric force on a charge due to all the other charges. The electric field of a single point charge located at the origin is given by:

{% math() %}
\mathbf{E} = \dfrac{kQ}{r^2} \hat r
{% end %}

The more general expression for the electric field $\mathbf{E}(\mathbf{r}) = \mathbf{E}(x, y, z)$ formed by $N$ charges, of which each charge $Q_i$ is situated at position $\mathbf{r}_i$, is given by:

{% math() %}
\mathbf{E}(\mathbf{r}) = \sum \limits_{i = 1}^N \dfrac{kQ_i}{|\mathbf{r} - \mathbf{r}_i|^3}(\mathbf{r} - \mathbf{r}_i)
{% end %}

It may prove useful to explicitly write out the expression in Cartesian coordinates. Then the electric field may be written:

{% math() %}
\mathbf{E}(x, y, z) = \sum \limits_{i = 1}^N \dfrac{kQ_i[(x - x_i)\hat i + (y - y_i)\hat j + (z - z_i)\hat k]}{[(x - x_i)^2 + (y - y_i)^2 + (z - z_i)^2]^\frac{3}{2}}
{% end %}

In the continuous case, where we have a charge distribution such as $\lambda(x)$ (linear charge density), $\sigma(x, y)$ (surface charge density), or $\rho(x, y, z)$ (volume charge density), then:

{% math() %}
\mathbf{E}(\mathbf{r}) = \int \dfrac{k dq'}{|\mathbf{r} - \mathbf{r}'|^3} (\mathbf{r} - \mathbf{r}')
{% end %}

Where $\mathbf{r}'$ is the location of infinitesimal charge element $dq'$, and $\mathbf{r} - \mathbf{r}'$ is the displacement vector. For linear, surface, and volume charge distributions, we have respectively $dq' = \lambda ds' = \sigma dA' = \rho dV'$ so the integral becomes:

{% math() %}
\begin{align*}
\mathbf{E}(\mathbf{r}) &= \int_C k\dfrac{\lambda ds'}{|\mathbf{r} - \mathbf{r}'|^3} (\mathbf{r} - \mathbf{r}'), &\text{(linear charge)} \\
&= \int_S k\dfrac{\sigma dx'dy'}{|\mathbf{r} - \mathbf{r}'|^3} (\mathbf{r} - \mathbf{r}'), &\text{(surface charge)} \\
&= \int_V k\dfrac{\sigma dx'dy'dz'}{|\mathbf{r} - \mathbf{r}'|^3} (\mathbf{r} - \mathbf{r}'), &\text{(volume charge)}
\end{align*}
{% end %}

> **Note:** be careful to remember that the integration is over $x', y', z'$, **not** $x, y, z$! Therefore, the final integral should have the integration variables $dx', dy', dz'$ and bounds in $x', y', z'$. In some cases, it _may be possible_ to express $x', y', z$ _purely in terms of_ $x, y, z$, and similarly express $dx', dy', dz'$ in terms of $dx, dy, dz$; when _all variables_ involving $x', y', z'$ are eliminated and replaced with $x, y, z$, then indeed it is possible to simply integrate over $x, y, z$. This, however, is **not true in the general case**.

## Gauss's law

In the previous section, we covered the discrete and integral forms of **Coulomb's law for electric fields**. This method of computing the electric field is error-prone, difficult to do by hand, and inelegant, which is why it is often termed the _"brute-force method"_. The more elegant alternative is to use **Gauss's law for electric fields**:

{% math() %}
\Phi_E = \oint \mathbf{E} \cdot d\mathbf{A} = \dfrac{Q_\text{total}}{\varepsilon_0}
{% end %}

Gauss's law relates the flux of the electric field $\Phi_E$, which is the surface integral of the electric field over a _closed surface_ (called a Gaussian surface), to the total charge _contained within the surface_. The surface integral is defined as the integral of the field _in the direction normal to the surface_, that is, $\mathbf{E} \cdot d\mathbf{A} = \mathbf{E} \cdot \mathbf{n}\, dA$.

The advantage of using Gauss's law is that many charge configurations exhibit certain symmetries for which the electric field is _uniform across the surface_:

{% math() %}
\oint \mathbf{E} \cdot d\mathbf{A} = E \oint dA
{% end %}

This makes it possible to solve for the electric field rather straightforwardly. In fact, a direct application of Gauss's law allows _deriving_ Coulomb's law giving the electric field of a point charge at the origin. We need only choose our closed surface to be a sphere of radius $r$. As the electric field vectors are directly perpendicular to the surface, it can be factored out of the integral, such that:

{% math() %}
\oint \mathbf{E} \cdot d\mathbf{A} = E \oint dA = E(4\pi r^2) = \dfrac{Q}{\varepsilon_0}
{% end %}

Then rearrangement gives:

{% math() %}
E = \dfrac{1}{4\pi \epsilon_0} \dfrac{Q}{r^2}
{% end %}

Noting that the electric field points radially outwards for $Q > 0$ the vector form is straightforward to find:

{% math() %}
\mathbf{E} = \dfrac{1}{4\pi \epsilon_0} \dfrac{Q}{r^2}\hat r
{% end %}

And thus we have recovered the vector form of Coulomb's law, as would be expected. Note that using $k \equiv \dfrac{1}{4\pi \varepsilon_0}$ is common to be able to simplify the expression.

### Notes on Gaussian surfaces

Gauss's law requires surface integration over a **closed surface** called a _Gaussian surface_. The surface normal is _always chosen_ to be the outward-pointing normal of the surface. In many cases, the normal can be found without explicit calculation by simply analyzing the symmetries of the problem - for instance, in our spherical configuration, which possesses radial symmetry, the surface normals are given by $\hat{\mathbf{n}} = \hat r$. 

In some other cases, we must explicitly find the normal vector from the surface. From multivariable calculus, given a surface implicitly-defined as $F(x, y, z) = 0$, the normal vector is given by:

{% math() %}
\hat{\mathbf{n}} = \dfrac{\nabla F}{|\nabla F|}
{% end %}

A sphere, for instance, is a surface defined by the implicit equation $F(x, y, z) = x^2 + y^2 + z^2 - R^2 = 0$, where $R$ is a constant. Therefore, $\nabla F = \langle 2x, 2y, 2y \rangle = 2 \mathbf{r}$ which has a magnitude of $2\sqrt{x^2 + y^2 + z^2} = 2|\mathbf{r}|$, so:

{% math() %}
\hat{\mathbf{n}} = \dfrac{2\mathbf{r}}{2|\mathbf{r}|} = \dfrac{\mathbf{r}}{|\mathbf{r}|} = \hat r
{% end %}.

### Common solutions for electric fields from Gauss's law

The majority of electric fields cannot be solved analytically by using Gauss's law. However, analytical solutions for the field do exist for some simple geometries. Using Gauss's law, solutions to the field for several common physical scenarios are shown below:

| Physical situation                                                                       | Gaussian surface                                                                                                                    | Result from flux integral                                                                                 | Enclosed charge | Electric field                                                                                                                         |
| ---------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| Anywhere around a point charge                                                           | Sphere of radius $r$ centered at $r = 0$                                                                                            | $\Phi_E = 4\pi r^2 \|\mathbf{E}\|$                                                                        | $Q = Q$         | $\mathbf{E} = \dfrac{1}{4\pi \varepsilon_0} \dfrac{Q}{r^2} \hat{\mathbf{r}}$                                                           |
| Outside uniform sphere of charge with radius $R$                                         | Sphere of radius $r$ centered at $r = 0$                                                                                            | $\Phi_E = 4\pi r^2 \|\mathbf{E}\|$                                                                        | $Q = Q$         | $\mathbf{E} = \dfrac{1}{4\pi \varepsilon_0} \dfrac{Q}{r^2} \hat{\mathbf{r}}, \quad r > R$                                              |
| Above surface of a conductor (of arbitrary thickness/geometry)                           | Box parallel to the surface with rectangular tops/bottoms of area $A$, placed at $z = 0$                                            | $\Phi_E = \|\mathbf{E}\|A$                                                                                | $Q = \sigma A$  | $\mathbf{E} = \dfrac{\sigma}{\varepsilon_0} \hat{\mathbf{n}}$ where $\hat{\mathbf{n}}$ is the normal vector to the conductor's surface |
| Above a single-sided infinite sheet of charge                                            | Box with rectangular tops/bottoms of area $A$, placed at $z = 0$                                                                    | $\Phi_E =  \|\mathbf{E}\|A$                                                                               | $Q = \sigma A$  | $\mathbf{E} = \dfrac{\sigma}{\varepsilon_0} \hat{\mathbf{z}}, \quad z > 0$                                                             |
| Above (or below) a double-sided infinite sheet of charge                                 | Box with  rectangular tops/bottoms of area $A$ centered at $z = 0$ (i.e. it is halfway above and halfway below the sheet of charge) | $\Phi_E = 2\|\mathbf{E}\|A$ (flux contribution from both the top and bottom side of the Gaussian surface) | $Q = \sigma A$  | $\mathbf{E} = \dfrac{\sigma}{2\varepsilon_0} \hat{\mathbf{z}}, \quad \|z\| > 0$                                                        |
| Around infinite line of charge (e.g. infinitely long wire) with charge density $\lambda$ | Coaxial cylinder (aligned along same axis as line of charge) of radius $\rho$ and length $L$                                        | $\Phi_E = 2\pi r L \lambda$                                                                               | $Q = \lambda L$ | $\mathbf{E} = \dfrac{\lambda}{2\pi \rho \varepsilon_0} \hat{\rho}$ (here $\rho$ is distance from wire)                                 |

> **Note:** An interesting consequence of Gauss's law that an infinitely-long uniformly-charged wire would have the _same amount of charge_ regardless of its thickness. In fact, it doesn't even matter if you are inside the wire! The reason why is that their total charge $Q = \lambda L$ is **independent** of the thickness of the wire and also independent of the radial distance. Why? Because any infinite wire would have infinite length, and thus **infinite charge**, no matter its thickness, so the total charge of any infinite wire (regardless of thickness) is $\infty$, so the same! Of course, in actual calculations with real wires, we would set $L$ to a large but non-infinite value, and thus the solution would only be an approximate solution (because the electric field of real wires _does_ depend on their thickness). But in the limit of infinite length, all wires and cylindrical charges with a uniform linear charge density $\lambda$ always have the _same total charge_.

## Electric potential

Previously, we saw that we could express the motion of charged particles within electric fields by using the electric force law $\mathbf{F}_E = q\mathbf{E}$ as well as Coulomb's law for determining the electric field. We also saw that Gauss's law offered an elegant alterative to Coulomb's law for finding the electric field, but analytical solutions could only be found in very specific cases.

We will now look at another elegant but powerful method of solving for the electric field in electrostatics - the electric potential. The electric potential is a function written as $V(\mathbf{r})$; unlike the electric field, it is _scalar-valued_. In electrostatics, the electric potential acquires a very specific physical interpretation:

> **A charge $q$ situated at point $\mathbf{r}$ would gain a potential energy $U_E = qV(\mathbf{r})$ at that point.**

The electric potential is found by solving **Poisson's equation for electrostatics**:

{% math() %}
\nabla^2V(\mathbf{r}) = -\rho/\varepsilon_0
{% end %}

where the force experienced by a charge in a magnetic field becomes:

{% math() %}
\mathbf{F}(\mathbf{r}) = -q \nabla V 
{% end %}

This tells us that _positive charges experience a force towards the minima of the electric potential_. Furthermore, by $\mathbf{E} = qV$, knowledge of the electric potential _determines_ the electric field (as long as the problem is electrostatic, i.e. time-independent). Thus the potential formulation is powerful as it reduces the complicated problem of finding the electric field to a much simpler problem of finding the electric potential. This is further streamlined by a very important result from the mathematical study of partial differential equations: the **uniqueness theorem** of Poisson's equation

>**Uniqueness theorem for Poisson's equation:** A given solution $V(\mathbf{r})$ of Poisson's equation that satisfies given boundary conditions is the **correct and _only_** solution of Poisson's equation.

We will see that this uniqueness theorem has enormous consequences for solving Poisson's equation - in particular, it leads to a powerful method of solving Poisson's equation, known as the **method of images**, which we will cover shortly.

### Electric potential and the properties of conductors

From our previous analysis, we have seen that electric fields both exist in free space as well as inside materials (and other solid objects). However, the nature of electric fields *inside* materials has drastically-different behavior from electric fields outside materials. In particular, electric fields inside materials distinguish between **conducting** and **non-conducting** materials. We will see that an analysis using the electric potential naturally leads to several important results for the characteristics of conductors.

Materials, of course, are composed of atoms; every atom is naturally neutrally-charged and is composed of a postively-charged nucleus and negatively-charged electrons. While physics at an atom scale is quantum-mechanical in nature, we can, to a good approximation, model the nucleus as a classical positive charge and electrons as classical negative charges.

Loosely-speaking, a conductor is any material that allows charges to move. Since protons are bound by electrostatic forces to their innermost electrons, protons usually do not move; it is the electrons that typically move, but this distinction is not that significant because the effects of charge separation (that is, an inbalance of positive and negative charges) are equivalent. **All metals are conductors**, and this is because the outermost (valence) electrons of metals are weakly-bound to their nuclei, allowing them to escape the atom. Thus, metals have free electrons.

Now, consider an external electric field applied on a conductor (for instance, by bringing a charge close to the surface of a conductor). By $\mathbf{F} = -q\mathbf{E}$, the free electrons in the conductor are repelled by the electric field, causing _charge separation_ to occur - the electrons move away from the protons, leading to a region of positive charge and a region of negative charge, as shown:

{{ diagram(
desc="A diagram showing a conductor placed in an external field, which experiences charge separation (polarization), leading to an induced field created that counters the external field"
src="polarized-conductor.excalidraw.svg"
) }}

This separation of positive and negative charges is known as **polarization** and the excess of charge accumulated at each end due to the external field is called the **induced charge**. However, as quickly as polarization occurs, the attractive electrostatic forces between the positive and negative charges leads to an _induced_ electric field {% inlmath() %}\mathbf{E}_\mathrm{induced}{% end %} that pulls the electrons towards the protons. The induced field {% inlmath() %}\mathbf{E}_\mathrm{ext}{% end %} and the external (also called _polarizing_) field $\mathbf{E}_\mathrm{ext}$ are in opposite directions and cancel out, such that the _net electric field_ is zero:

{% math() %}
\mathbf{E}_\mathrm{net} = \mathbf{E}_\mathrm{ext} + \mathbf{E}_\mathrm{induced} = 0
{% end %}

Thus, we arrive at a very important result:

> **In any conductor, regardless of geometry, there is _zero electric field_ inside the conductor.**

Note that this _does not mean_ the conductor cannot produce an electric field; a conductor still can have polarized charge on its _surface_, and thus have an electric field _outside the conductor_. But it has _just the right amount_ of polarized charge on its surface such that the induced field $\mathbf{E}_\mathrm{ext}$ _perfectly cancels out_ the external field, resulting in the electric field is just zero _inside the conductor_. 

Let us also be careful with our terminology here: by "inside the conductor", we mean _in the material of the conductor_. If we have a hollow conductor (such as a metal sphere with a cavity inside), there would still be internal fields inside the cavity. However, **no electric fields outside the conductor** penetrate inside the conductor; the electric field(s) inside the cavity are completely shielded from the external fields as the conductor maintains a zero electric field within its material interior. This is the operating principle behind **Faraday cages**, where sensitive electronic equipment are placed in a metal boxes (or cages) to shield them from outside fields. It is also why an elevator (which a physicist would loudly proclaim as "a conducting spherical shell...erm, I mean, box of length $a$, width $b$, and height $h$") can block Wi-Fi and cellphone signals - a familiar source of annoyance for physicists and non-physicists alike.

Since $\mathbf{E}_\mathrm{inside} = 0$, by $\mathbf{E} = -\nabla V$, this means that $V = V_0 = \text{const.}$ within a conductor. Thus we say that the surface of a conductor is an **equipotential surface** - the potential on the surface of a conductor is constant, and it is the same everywhere else inside the conductor. In addition, since $\mathbf{E} = -\nabla V = 0$ for a conductor and $V = \text{const.}$ on the surace of (and inside) a conductor, the component of the electric field along the surface of a conductor (which we call the _tangential component_ of the field) is always zero (since the derivative of a constant is zero). This leaves only the _normal_ component of the electric field (i.e. the electric field that points in the direction of the normal to the surface). We summarize this result as follows:

> **Electric field lines immediately outside a conductor are always perpendicular to the surface.**

In the special case where a conductor is **grounded**, the conductor is attached by a metal wire to the ground, which acts as an infinite source (and sink) of electrons. Thus, any excess charge on the surface of the conductor is cancelled out by free electrons that enter the conductor from the ground or leave the conductor into the ground, as electrons are free to move. Thus, not only do we have $\mathbf{E}_\mathrm{inside} = 0$, but we *also* have $V = 0$ throughout the conductor. For a more precise and elaborate discussion, see [this Physics StackExchange post](https://physics.stackexchange.com/questions/547488/accumulated-charge-in-a-grounded-conductor).

Using the fact that the electric field lines outside a conductor are always perpendicular to the surface, we can derive an expression for the _induced charge_. We may calculate this induced charge mathematically as follows: recall that the electric field near the surface of a conductor is given by $\mathbf{E} = \dfrac{\sigma}{\varepsilon_0} \hat{\mathbf{n}}$. We illustrate this in the below diagram:

{{ diagram(
desc="A diagram showing how induced charges due to an external field causes positive and negative charges to separate, which we call polarization"
src="induced-charge-conductor.excalidraw.svg"
) }}

Since $\mathbf{E} = -\nabla V$, and since electric field lines outside a conductor are _perpendicular to the surface_ (which means they are also parallel to the normal of the surface), then $\nabla V = \dfrac{\partial V}{\partial n}$. Therefore, by equating the expressions, we obtain:

{% math() %}
\begin{align*}
\mathbf{E} &= -\nabla V \\
\dfrac{\sigma}{\varepsilon_0}\hat{\mathbf{n}} &= -\dfrac{\partial V}{\partial n} \\
\sigma&= -\varepsilon_0 \dfrac{\partial V}{\partial n}
\end{align*}
{% end %}

And thus the induced charge is given by integrating the induced charge density across the surface of the conductor:

{% math() %}
Q_\mathrm{induced} = \iint \sigma \, dA = -\iint \varepsilon_0 \dfrac{\partial V}{\partial n} dA 
{% end %}

This relation has two important consequences, one for finding the field, and one for finding the total induced charge:

- If we know $\sigma$, we can calculate the electric potential $V$ at the surface of the conductor.
	- We can then use this as a _boundary condition_ for Poisson's equation to find the general expression for the electric potential $V(\mathbf{r})$ at any distance from the conductor, and by $\mathbf{E} = -\nabla V$ we can then find the electric field _everywhere in space_ (not just near the conductor)
- If we know the electric potential, we can use it to calculate the charge density, and therefore the induced charge on the surface of the conductor.

## Solving Poisson's equation

We have discussed the *qualitative features* of the electric potential, but what about its *quantitative* (i.e. calculation-based) aspects? To be able to actually _calculate_ potentials, we must solve Poisson's equation $\nabla^2 V = -\rho/\varepsilon_0$, for which we can make use of a variety of methods:

1. Use the *superposition solution* of Poisson's equation $V(\mathbf{r}) = \displaystyle \int \dfrac{k \rho(\mathbf{r}')}{|\mathbf{r} - \mathbf{r}'|} dV'$ , which is based on the superposition principle and the assumption of having one boundary condition of $V(\infty) = 0$ (that is, we require that $V(\mathbf{r}) \to 0$ as $\mathbf{r} \to \infty$)
2. Using separation of variables and then applying the boundary conditions to find a closed-form solution
3. Start from an existing known solution, expanding the solution to incorporate additional terms (this is called _a perturbative solution_, and the particular technique is called the **multipole expansion**)
4. Adapt the problem to reduce it to a simpler problem with the same boundary conditions (called the **method of images**)
5. Using the **mean value theorem** (also called the _method of relaxation_) or some other numerical method to find a numerical solution

Now that we have listed out each method, we will cover each of them in detail.

### The superposition solution of Poisson's equation

Consider a physical situation of a spherically-symmetric potential of a point charge $q$, where the potential $V(\mathbf{r})$ vanishes at infinity. Thus, the work done against the electric force to bring the charge from infinity to a point $r$ (i.e. in spherical coordinates, $(r, \theta, \phi)$) would be given by:

{% math() %}
W = \int_{\infty}^r \mathbf{F}_E \cdot d\mathbf{r}
{% end %}

Recall that the electric force is given by $q \mathbf{E}$, and the electric field of a point charge is given by $\mathbf{E} = k\dfrac{Q}{r}\hat r$. Therefore:

{% math() %}
\begin{align*}
W &= \int_{\infty}^r \dfrac{kQ}{r'} dr' \\
&= -\dfrac{kQ}{r'} \bigg|_{\infty}^r\\
&= \dfrac{kQ}{r'} \bigg|_r^\infty \\
&= \cancel{\dfrac{kQ}{\infty}}^0 - \dfrac{kQ}{r} \\
&= - \dfrac{kQ}{r}
\end{align*}
{% end %}


> **Note:** we switched variables in the integrand from $r \to r'$ and $dr \to dr'$ to avoid confusion

Since we know that $\Delta U = -W$ we would have:

{% math() %}
\Delta U = U(\infty) - U(r) = -\dfrac{kQ}{r}
{% end %}

Again, since we have the boundary condition $U(\infty) = 0$, we have:

{% math() %}
\begin{gather*}
\Delta U = \cancel{U(\infty)}^0 - U(r) = -\dfrac{kQ}{r} \\
-U(r) = -\dfrac{kQ}{r} \\
\Rightarrow U(r) = \dfrac{kQ}{r}
\end{gather*}
{% end %}

Thus the electric potential of a point charge is given by $U(r) = \dfrac{kQ}{r}$. But by the superposition principle, the electric potential of several point charges is just the sum of the superposition of the individual electric potentials of each charge:

{% math() %}
V(\mathbf{r}) = \sum_{i = 1}^{N_\mathrm{charges}}\dfrac{kQ_i}{|\mathbf{r} - \mathbf{r}_i|}
{% end %}

In the limit where the charges form a continuous _charge distribution_ we have:

{% math() %}
V(\mathbf{r}) = \int \dfrac{k\,dq'}{|\mathbf{r} - \mathbf{r}'|} = \int \dfrac{\rho(\mathbf{r}')\, dx'dy'dz'}{((x - x')^2 + (y - y')^2 + (z - z')^2)^{1/2}}
{% end %}

Where, similar to Coulomb's law, we have $dq' = \lambda(x') dx' = \sigma(\mathbf{r}') dA' = \rho(\mathbf{r}') dV'$. This is a **particular solution** to Poisson's equation that applies for $\rho \neq 0$ and under the boundary condition $V(\infty) = 0$. It is _not_ a general solution because it _does not hold_ if $\rho = 0$ or if $V(\infty) \neq 0$, and in addition the singularity of $V(0)$ is unphysical, so $V(\mathbf{r})$ found by this solution is only valid for $|\mathbf{r}| > 0$. However, this solution is general enough for a large class of problems, such as the potential from a finite rod of charge, of a cone of charge, or of a uniform solid sphere of charge. See [this table of solutions](https://en.wikipedia.org/wiki/Electric_potential#Common_formulas) for a number of common potentials, many of which can be solved using this approach.

For cases in which $\rho = 0$ and/or $V(\infty) \neq 0$, we must use the **method of images**, **separation of variables**, or **multipole expansion** to solve, or if we have exhausted all of these methods, to use numerical methods, such as the method of relaxation. We will cover these methods one-by-one.

### The method of images

Consider the problem of a charge $Q$ placed at position $\mathbf{r}_1 = \langle 0, 0, d\rangle$ placed above a (conducting) metal plate that is grounded (that is, $V = 0$). We show a sketch of this physical situation below:

{{ diagram(
desc="A diagram showing a charge placed above a grounded conducting plate"
src="method-of-images.excalidraw.svg"
) }}

Our boundary conditions of $V(0) = V(\infty) = 0$ suggests that we place _another charge_ at $\mathbf{r}_2 = \langle 0, 0, -d\rangle$ that has the opposite charge $\tilde Q = -Q$ (called an **image charge**). Such a physical scenario would have _the same boundary conditions_ as our original problem. We illustrate this _modified_ scenario below:

{{ natural_img(
desc="A diagram showing a fake image charge placed under the aforementioned conducting plate"
src="method-of-images-2.excalidraw.svg"
) }}

Of course, the potential below $z = 0$ is unphysical; there is no real charge at $\langle 0, 0, -d\rangle$, as the image charge is imaginary. But the superposition principle means that the potential of the image charge and the potential of the real charge causes the potential to cancel out at $z = 0$, and since both potentials decay with distance, both vanish at $\pm \infty$. Thus this scenario preserves the boundary conditions $V(0) = 0, V(\infty) = 0$. 

This means that, given the uniqueness theorem of Poisson's equation (_a solution to certain boundary conditions is the one unique solution_), since the two physical scenarios have the **same boundary conditions**, Poisson's equation yields a **unique solution** that is identical for both scenarios.

> **Note:** The requirement of using the method of images is that the image charge _cannot be placed_ in a region where the potential is calculated. This is why we placed the image charge at $z < 0$, since we are *only calculating* $V(\mathbf{r})$ for $z \geq 0$.

Now - with the conceptual basis covered - we are able to get to solving. Recall that by the superposition principle, since the electric potential of a single point charge is given by $V = \dfrac{kQ}{|\mathbf{r} - \mathbf{r}_i|}$, the electric potential of the real and image charges combine such that:

{% math() %}
\begin{align*}
V(\mathbf{r}) &= V_\text{real charge} + V_\text{image charge} \\
&= \dfrac{kq}{|\langle x, y, z\rangle - \langle 0, 0, d\rangle|} + \dfrac{-kq}{|\langle x, y, z\rangle - \langle 0, 0, -d\rangle|} \\
&= \dfrac{kQ}{(x^2 + y^2 + (z - d)^2)^{1/2}} + \dfrac{-kQ}{(x^2 + y^2 + (z - d)^2)^{1/2}}
\end{align*}
{% end %}

And thus we have found the solution for $V(\mathbf{r})$ for all $z \geq 0$! We can substitute our boundary conditions in to check that our solution _does_, indeed, solve Poisson's equation:

{% math() %}
\begin{align*}
V(0, 0, 0) &= \dfrac{kQ}{(\cancel{x^2} + \cancel{y^2} + (\cancel{z} - d)^2)^{1/2}} + \dfrac{-kQ}{(\cancel{x^2} + \cancel{y^2} + (z - d)^2)^{1/2}} \\
&= \dfrac{kQ}{d} + \dfrac{-kQ}{d} \\
&= 0 \quad \checkmark \\
V(x, y, \infty) &=\dfrac{kQ}{(x^2 + y^2 + (\infty - d)^2)^{1/2}} + \dfrac{-kQ}{(x^2 + y^2 + (\infty - d)^2)^{1/2}} \\
&=\dfrac{kQ}{\cancel{(x^2 + y^2 + (\infty - d)^2)^{1/2}}^\infty} + \dfrac{-kQ}{\cancel{(x^2 + y^2 + (\infty - d)^2)^{1/2}}^\infty} \\
&= 0 + 0 \\
&= 0 \quad \checkmark
\end{align*}
{% end %}

And thus we have confirmed that the potential $V(\mathbf{r})$ is indeed:

{% math() %}
\begin{matrix*}
V(\mathbf{r}) = \dfrac{kQ}{(x^2 + y^2 + (z - d)^2)^{1/2}} + \dfrac{-kQ}{(x^2 + y^2 + (z - d)^2)^{1/2}}, &z \geq 0
\end{matrix*}
{% end %}

Which can be written in a slightly nicer way as:

{% math() %}
\begin{matrix*}
V(x, y ,z) = kQ\left[\dfrac{1}{\sqrt{x^2 + y^2 + (z - d)^2}} - \dfrac{1}{\sqrt{x^2 + y^2 + (z - d)^2}}\right], &z \geq 0
\end{matrix*}
{% end %}

From which we may find the electric field $\mathbf{E}(\mathbf{r})$ by simply taking the gradient of $V$, since $\mathbf{E} = -\nabla V$. Thus we have seen that the method of images is a powerful way to solve for not just the electric potential, but also the electric field, especially in case where the electric field is too difficult to solve for directly.

We may also use this expression for the potential to find an expression of the _induced charge_ caused by the real charge upon the conducting plate. For this, recall that the expression for the electric field right outside a conductor is given by:

{% math() %}
\mathbf{E} = \dfrac{\sigma}{\varepsilon_0}\hat{\mathbf{n}}
{% end %}

Where $\sigma$ is the charge density. But since we know that $\mathbf{E} = -\nabla V$, and since the electric field is always perpendicular to the surface of a conductor, the gradient must be along the normal to the conductor, i.e. $\nabla V = \dfrac{\partial V}{\partial n}$, we have:

{% math() %}
\begin{align*}
\mathbf{E} = -\dfrac{\partial V}{\partial n} = \dfrac{\sigma}{\varepsilon_0}\hat{\mathbf{n}} \\
\Rightarrow \sigma = -\varepsilon_0 \dfrac{\partial V}{\partial n}
\end{align*}
{% end %}

The total induced charge is then given by integrating the (induced) charge density across the entirety of the surface of the conductor:

{% math() %}
Q_\text{ind.} = \iint \sigma\, dA
{% end %}

But remember that all the induced charge on a conductor _must_ reside on its surface - this is one of the requirements to ensure that the electric field is always zero inside a conductor! Therefore, the total induced charge must be equal to $-Q$, such that the net charge is zero, causing the electric field to also be zero inside the conductor, as it must.

We may also consider the case of a charge $Q$ placed at a distance $a$ from the center of a grounded conducting sphere of radius $R$. Suppose we wanted to solve for the potential outside of the sphere, that is, for $r \geq R$. Then the boundary conditions would be given by:

{% math() %}
\begin{align*}
V(R, \theta) = 0 \\
V(\infty, \theta) = 0
\end{align*}
{% end %}

The question is, where should we place an image charge so that we can satisfy the boundary conditions? First, the image charge cannot be placed at any point for which $r \geq R$, since that is our region of interest, and we cannot have an imaginary charge be present within the region we are solving for the potential over. Instead, the image charge must be placed somewhere _inside_ the sphere. The idea is to consider an image charge that has a _smaller magnitude_ of charge to counteract for the fact that it is placed a shorter distance away to make it fit inside the sphere. More precisely (we will not prove this), we must let our image charge $\tilde Q$ have a charge of $\tilde Q = -Q R / a$, and be placed at distance $d = R^2/a$ away from the sphere's center, to preserve the boundary conditions. The solution is given by:

{% math() %}
V(r, \theta) = kQ\left[\dfrac{1}{\sqrt{r^2 + a^2 - 2ar \cos \theta}} - \dfrac{1}{\sqrt{R^2 + (\frac{ra}{R})^2-2ra \cos \theta}}\right]
{% end %}

But what about a _non-grounded_ conducting sphere? Suppose our sphere was a charged sphere with constant charge $Q_0$. In this case, in addition to our image charge $\tilde Q = -QR/a$ (which is the same as in the case of the grounded conducting sphere), we must also add *another* image charge $\tilde Q_2$ in the center of our sphere, to ensure we are consistent with our boundary conditions. This image charge would need to have a charge of $\tilde Q_2 = Q_0 + QR/a$. The solution for the electric potential then becomes:

{% math() %}
V(r, \theta) = \left[\dfrac{kQ}{\sqrt{r^2 + a^2 - 2ar \cos \theta}} - \dfrac{kQ}{\sqrt{R^2 + (\frac{ra}{R})^2-2ra \cos \theta}} + \dfrac{k(Q_0 + QR/a)}{r}\right]
{% end %}

> **Note:** the solutions to both problems involving spherical conductors were taken from [this online textbook](https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electro-Optics/Electromagnetic_Field_Theory%3A_A_Problem_Solving_Approach_(Zahn)/02%3A_The_Electric_Field/2.07%3A_The_Method_of_Images_with_Point_Charges_and_Spheres), which additionally offers full-length solutions to both problems.

### The method of relaxation

Before continuing on to more advanced analytical approaches, we will take a brief look at a very common _numerical method_ for solving Laplace's equation. In general, numerical methods are used when we encounter a problem where analytical approaches are insufficient or too time-consuming to tackle the problem. To introduce the topic of numerical methods for Laplace's equation, recall that the derivative is the _limit_ of the difference quotient:

{% math() %}
\begin{align*}
\dfrac{\partial V}{\partial x} = \lim_{h \to 0} \dfrac{V(x + h, y) - V(x, y)}{h} \\
\dfrac{\partial V}{\partial y} = \lim_{h \to 0} \dfrac{V(x, y + h) - V(x, y)}{h} \\
\end{align*}
{% end %}

Of course, this relationship is only exact in the limit where $h \to 0$. But we can _approximate_ partial derivatives by choosing $h = \epsilon$, where $\epsilon$ is a very, very small but nonzero number. Then we have:

{% math() %}
\begin{align*}
\dfrac{\partial V}{\partial x} \approx \dfrac{V(x + \epsilon, y) - V(x, y)}{\epsilon} \\
\dfrac{\partial V}{\partial y } \approx \dfrac{V(x, y + \epsilon) - V(x, y)}{\epsilon} \\
\end{align*}
{% end %}

And we can do something very similar for second-order partial derivatives:

{% math() %}
\begin{align*}
\dfrac{\partial^2 V}{\partial x^2} = \lim_{\epsilon \to 0} \dfrac{V(x + \epsilon, y) - 2V(x, y) + V(x-\epsilon, y)}{\epsilon^2} \\
\dfrac{\partial^2 V}{\partial y^2} = \lim_{\epsilon \to 0} \dfrac{V(x, y + \epsilon) - 2V(x, y) + V(x, y-\epsilon)}{\epsilon^2} \\
\end{align*}
{% end %}

From which we can find:

{% math() %}
\dfrac{\partial^2 V}{\partial x^2} + \dfrac{\partial^2 V}{\partial y^2}
\approx \dfrac{1}{\epsilon^2}(V(x +\epsilon, y) + V(x-\epsilon, y) + V(x, y + \epsilon) + V(x, y-\epsilon) - 4V)
{% end %}

If we substitute this into Laplace's equation $\nabla^2 V = 0$, we have:

{% math() %}
\begin{gather*}
\dfrac{1}{\epsilon^2}(V(x + \epsilon, y) + V(x-\epsilon, y) + V(x, y + \epsilon) + V(x, y-\epsilon) - 4V) = 0 \\
V(x + \epsilon, y) + V(x-\epsilon, y) + V(x, y + \epsilon) + V(x, y-\epsilon) - 4V = 0 \\
4V(x, y) = V(x + \epsilon, y) + V(x-\epsilon, y) + V(x, y + \epsilon) + V(x, y-\epsilon) \\
\end{gather*}
{% end %}

From which we can simplify to get:

{% math() %}
V(x, y) = \dfrac{1}{4}[V(x + \epsilon, y) + V(x-\epsilon, y) + V(x, y + \epsilon) + V(x, y-\epsilon)]
{% end %}

Which tells us that _the potential at one point is equal to the average of the potential at its 4 neighboring points_ - known as the **mean value theorem** for Laplace's equation. This relationship is only exact in the limit as $\epsilon \to 0$, but is _approximately true_ when $\epsilon$ is a very small number, and this is good enough when we want to find an approximate solution to Laplace's equation to find the electric potential of a non-trivial problem. If we discretize a 2D domain as a matrix, which is often done via computer, we can _iterate_ over the entries of the matrix to set the potential as the average of the neighboring points:

{% math() %}
V_{i,j} = \dfrac{1}{4} (V_{i + 1, j} + V_{i-1, j} + V_{i, j+1} + V_{i, j-1})
{% end %}

Thus, if we input the boundary conditions by setting the edges of the matrix (which are the boundary points) to equal the boundary conditions, we can then perform the iterative process until the solution has converged sufficiently. This is known as the **method of relaxation**.

### Boundary-value problems by separation of variables

Consider two grounded metal plates, separated by a dielectric slab of height $a$ and negligible thickness (both shown on the diagram below). We want to find the potential $V(x, y)$ between the two plates. Since the metal plates are conductors and are grounded, they have $V = 0$, while the dielectric slab has a potential distribution given by $V = V_0(y)$.

{{ natural_img(
desc="An illustration of the boundary-value problem, where two metal plates are bridged by a thin dielectric slab"
src="poisson-bvp.excalidraw.svg"
) }}

> **Note:** This problem from Griffiths Example 3.3 from *Introduction to Electrodynamics*.

To solve for the potential between the plates (i.e. $0 < y < a$, $0 < x < \infty$), we use **Poisson's equation**:

{% math() %}
\nabla^2 V = -\rho/\varepsilon_0
{% end %}

Since the space between the two plates is air (or vacuum), it contains zero charge, so $\rho = 0$, and therefore Poisson's equation reduces to **Laplace's equation**:

{% math() %}
\nabla^2 V = \dfrac{\partial^2 V}{\partial x^2} + \dfrac{\partial^2 V}{\partial y^2} = 0
{% end %}

Where we have the boundary conditions:

{% math() %}
\begin{align*}
V(x, 0) &= 0 \\ 
V(x, a ) &= 0 \\
V(0, y) &= V_0(y) \\
V(\infty, y) &= 0
\end{align*}
{% end %}

When using the separation of variables, we presume a solution in the form $V(x, y) = X(x) Y(y)$. Therefore:

{% math() %}
\begin{matrix*}
\dfrac{\partial V}{\partial x} &= X'(x) Y(y) &\Rightarrow  &\dfrac{\partial^2 V}{\partial x^2} = X''(x) Y(y) \\
\dfrac{\partial V}{\partial y} &= X(x) Y'(y) &\Rightarrow &\dfrac{\partial^2 V}{\partial y^2} = X(x) Y''(y)
\end{matrix*}
{% end %}

Substituting into Laplace's equation we have:

{% math() %}
X''(x) Y(y) + X(x) Y''(y) = 0
{% end %}

Which we can alternatively write as:

{% math() %}
X''(x) Y(y) = -X(x) Y''(y) 
{% end %}

If we divide by both sides by $X(x)Y(y)$ we have:

{% math() %}
\begin{align*}
\dfrac{1}{X(x)Y(y)}X''(x) Y(y) &= -\dfrac{1}{X(x)Y(y)}X(x) Y''(y) \\
\dfrac{X''}{X} &= -\dfrac{Y''}{Y}
\end{align*}
{% end %}

Since we have two derivatives with respect to different variables equal to each other, they must be equal to a _constant_ (but it does not matter which constant we choose, or the sign of the constant; the only requirement imposed upon us is that it is a _constant_). We will refer to our _seperation constant_ as $c\beta^2$, where $c = \pm 1$. Therefore, we have:

{% math() %}
\begin{matrix*}
\dfrac{X''}{X} = c\beta^2, & -\dfrac{Y''}{Y} = c\beta^2 
\end{matrix*}
{% end %}

This becomes a system of two _ordinary differential equations_ to solve:

{% math() %}
\begin{matrix*}
X'' = c\beta^2 X,& Y'' = -c\beta^2 Y
\end{matrix*}
{% end %}

Now, we must choose $c = +1$ or $c = -1$. The choice of which sign to use boils down to our boundary conditions:

| If we want...                                                                | We choose... |
| ---------------------------------------------------------------------------- | ------------ |
| $X(x)$ to vanish for $x \to \infty$ or $x \to -\infty$                       | $c=+1$       |
| $X(x)$ to vanish for $x \to L$ or $x \to -L$, where $L$ is a finite constant | $c = -1$     |
| $Y(y)$ to vanish for $y \to \infty$ or $y \to -\infty$                       | $c = -1$     |
| $Y(y)$ to vanish for $y \to L$ or $y \to -L$, where $L$ is a finite constant | $c = +1$     |

> **Note:** If we encounter the case of needing _both_ $X(x)$ and $Y(y)$ to vanish at either infinity or some finite constant, we will need to use more advanced techniques that we will not cover here.

In our case, given our boundary condition $V(\infty, y) = 0$, that is, $V \to 0$ as $x \to \infty$, we choose $c = +1$ and thus we have the differential equations:

{% math() %}
\begin{matrix*}
X'' = \beta^2 X,& Y'' = -\beta^2 Y
\end{matrix*}
{% end %}

We can find the solutions by inspection. For $X'' = \beta^2 X$, then we are looking for a function $X(x)$ which is itself multiplied by $\beta^2$ upon twice differentiating. The exponential function $e^{\beta x}$ satisfies this requirement! But indeed, so does the function $e^{-\beta x}$ (you can check for yourself that this is true). Thus the _general_ solution to the ODE becomes the sum of both solutions, $X(x) = Ae^{\beta x} + B e^{-\beta x}$ (where $A, B$ are undetermined constants that we'll figure out later from the boundary conditions).

Meanwhile, for $Y''(y) = -\beta^2 Y$, then we are looking for a function $Y(y)$ which is itself multiplied by $-\beta^2$ upon twice differentiating. The sine function $\sin(\beta y)$ satisfies this requirement! But indeed, so does the function $\cos(\beta y)$. Thus, once again, the *general* solution to the ODE becomes the sum of both, $Y(y) = C \sin(\beta y) + D\cos(\beta y)$ (where again $C, D$ are undetermined constants that we'll figure out later from the boundary conditions).

Arranging our solutions in a slightly nicer format, we have:

{% math() %}
\begin{align*}
X(x) &= Ae^{\beta x} + B e^{-\beta x} \\
Y(y) &= C \sin(\beta y) + D\cos(\beta y)
\end{align*}
{% end %}

Remember that we assumed a solution in the form $V(x, y) = X(x) Y(y)$? Thus substituting the above solutions for $X(x)$ and $Y(y)$, our general solution is given by:

{% math() %}
V(x, y) = (Ae^{\beta x} + B e^{-\beta x})(C \sin \beta y + D\cos \beta y)
{% end %}

Now is the time for us to find the specific solution for our boundary conditions by determining $A, B, C, D$. Our boundary conditions, remember, are given by:

{% math() %}
\begin{align*}
V(x, 0) &= 0 \tag{1} \\ 
V(x, a ) &= 0 \tag{2} \\
V(0, y) &= V_0(y) \tag{3} \\
V(\infty, y) &= 0 \tag{4}
\end{align*}
{% end %}

Let us start with boundary condition (4), which reads $V(\infty, y) = 0$. Substituting in $x = \infty$, our solution becomes:

{% math() %}
V(\infty, y) = (\underbrace{Ae^{\infty}}_{\infty} + \underbrace{Be^{-\infty}}_0)(C \sin \beta y + D\cos \beta y)
{% end %}

We notice that the first term $Ae^{\beta x} \to \infty$ as $x \to \infty$, which is unphysical behavior!! So to prevent this from happening, the only possible choice for our constant $A$ is $A = 0$. Thus our solution simplifies to:

{% math() %}
V(x, y) = B e^{-\beta x}(C \sin \beta y + D\cos \beta y)
{% end %}

Now let us tackle boundary conditions (1) and (2), namely $V(x, 0) = V(x, a) = 0$. Substituting in our boundary conditions yields:

{% math() %}
\begin{align*}
V(x, 0) &= Be^{-\beta x}(\cancel{C \sin(0)} + \underbrace{D\cos (0)}_D) \\
V(x, a) &= Be^{-\beta x}(C \sin (\beta a) + D \cos(\beta a))
\end{align*}
{% end %}

For the boundary condition $V(x, 0) = 0$ to be true, then since $e^{-\beta x} \neq 0$ except for $x \to \infty$, $D$ must be equal to zero. So our solution becomes:

{% math() %}
V(x, y) = B e^{-\beta x}C \sin \beta y 
{% end %}

We can clean this expression up by defining a new constant $K = BC$ which simplifies our expression to:

{% math() %}
V(x, y) = K e^{-\beta x} \sin \beta y
{% end %}

For the boundary condition $V(x, a) = 0$ to be true, then we must have $Ke^{-\beta x} \sin(\beta a) = 0$. Since, again, $e^{-\beta x} \neq 0$ except for $x \to \infty$, the only possible way to make the equation true is if $\sin(\beta a) = 0$ (okay, unless if we let $K = 0$, but then $V = 0$ as well which does not match our other boundary conditions). 

This means we must solve for $\sin \beta a = 0$. Recall that the sine function $\sin x$ is zero at $x = n\pi = 0, \pi, 2\pi, 3\pi, \dots$ and so if we want $\sin \beta a = 0$, then $\beta a$ must be equal to $n\pi$. Solving for $\beta$ in terms of $a$, we have:

{% math() %}
\beta a = n\pi \quad \Rightarrow \quad \beta = \dfrac{n\pi}{a}
{% end %}

So, after substituting in $\beta = n\pi/a$, our solution becomes:

{% math() %}
V(x, y) = K \exp\left({-\dfrac{n\pi x}{a}}\right) \sin \left(\dfrac{n\pi y}{a}\right)
{% end %}

Our final boundary condition $V(0, y) = V_0(y)$ is somewhat more tricky. If we just directly evaluate $V(0, y)$, we get:

{% math() %}
\begin{align*}
V(0, y) &= K \exp(0) \sin \left(\dfrac{n\pi y}{a}\right) \\
&= K \sin \left(\dfrac{n\pi y}{a}\right) \\
&\neq V_0 (y)
\end{align*}
{% end %}

Which appears to make it impossible to satisfy the boundary condition. But there _is_ a way. Since Laplace's equation is a _linear_ PDE (since it is the sum of two partial derivatives and partial derivatives are _linear operators_), the sum of two solutions of Laplace's equation is _also_ a solution. The same goes for the sum of three solutions, or four, or five, or even _infinitely-many solutions_ - they are all solutions of Laplace's equation! Therefore, we can add up infinitely-many "copies" of our solution to express our solution in terms of a _series_, as shown:

{% math() %}
V(x, y) = \sum_{n = 1}^\infty K_n \exp\left({-\dfrac{n\pi x}{a}}\right) \sin \left(\dfrac{n\pi y}{a}\right)
{% end %}

Thus substituting for $V(0, y) = V_0(y)$, we have:

{% math() %}
\begin{align*}
V(0, y) &= \sum_{n = 1}^\infty K_n \cancel{\exp(0)}^1 \sin \left(\dfrac{n\pi y}{a}\right) \\
&=\sum_{n = 1}^\infty K_n \sin \left(\dfrac{n\pi y}{a}\right) \\
&= V_0(y)
\end{align*}
{% end %}

If we choose the right coefficients $K_n$, then the series can _converge_ such that $V(0, y) = V_0(y)$. But how do we get these coefficients? We can use a trick that Griffiths calls _Fourier's trick_. The trick is based off the orthogonality identity that we stated at the beginning of the guide:

{% math() %}
\int_0^a \sin \left(\dfrac{m\pi y}{a}\right)  \sin \left(\dfrac{n\pi y}{a}\right)\,dy = \dfrac{a}{2} \delta_{mn} =
\begin{cases}
a/2 ,& m = n \\
0, & m \neq n
\end{cases}
{% end %}

This means that if we multiply our respective expressions for $V(0, y)$ by $\sin(m\pi y/a)$, then 
integrate both sides, all the terms in the series become zero except for the term where $m = n$, from which we can find $K_n$. Let us work through what this means, step-by-step. We start with our expression from before, for $V(0, y) = V_0(y)$, which can be expanded as:

{% math() %}
V(0, y)=\sum_{n = 1}^\infty K_n \sin \left(\dfrac{n\pi y}{a}\right) = V_0(y)
{% end %}

Now, we multiply both sides by $\sin(m\pi y/a)$ and integrate both sides to get:

{% math() %}
\begin{align*}
\sum_{n = 1}^\infty K_n \sin \left(\dfrac{n\pi y}{a}\right)\sin \left(\dfrac{m\pi y}{a}\right) &= V_0(y)\sin \left(\dfrac{m\pi y}{a}\right) \\
\int_0^a\sum_{n = 1}^\infty K_n \sin \left(\dfrac{n\pi y}{a}\right)\sin \left(\dfrac{m\pi y}{a}\right)dy &= \int_0^aV_0(y)\sin \left(\dfrac{m\pi y}{a}\right)dy \tag{*}
\end{align*}
{% end %}

But remember our identity - that the integral $\displaystyle \int_0^a \sin \left(\frac{m\pi y}{a}\right)  \sin \left(\frac{n\pi y}{a}\right)\,dy = \dfrac{a}{2} \delta_{mn}$. That is to say, the integral evaluates to zero _except for_ when $m = n$, in which case it evaluates to $a/2$. So the left-hand-side of our previous equation (which we marked with the asterisk) becomes:

{% math() %}
\int_0^a\sum_{n = 1}^\infty K_n \sin \left(\dfrac{n\pi y}{a}\right)\sin \left(\dfrac{m\pi y}{a}\right)dy = \begin{cases}
a K_n/2 ,& m = n \\
0, & m \neq n
\end{cases}
{% end %}

Since the integral is only nonzero if $m = n$, then the _right-hand side_ of our asterisk-marked equation must _also_ have $m = n$, and therefore:

{% math() %}
aK_n/2 = \int_0^aV_0(y)\sin \left(\dfrac{n\pi y}{a}\right)dy
{% end %}

Which we can rearrange to:

{% math() %}
K_n = \dfrac{2}{a}\int_0^aV_0(y)\sin \left(\dfrac{n\pi y}{a}\right)dy
{% end %}

From this, we can evaluate each $K_n$ relatively straightforwardly (assuming a willingness to do a lot of integrals!) Note that this series solution is _exact_, but requires infinitely many terms; in practice we just compute a finite number of terms - as many terms as we need for a reasonably accurate result. This works because the mathematical properties of Laplace's equation (see the [PDE guide for more details](@/intro-pdes/index.md)) guarantee a _smooth_ (what mathematicians would call _well-behaved_) solution across the domain specified by the boundary conditions.

As a demonstrative example, let us take the case where $V_0(y) = V_0$. Then the expression for $K_n$ becomes:

{% math() %}
\begin{align*}
K_n &= \dfrac{2}{a}\int_0^aV_0\sin \left(\dfrac{n\pi y}{a}\right)dy \\
&= \dfrac{2V_0}{a} \int_0^a \sin \left(\dfrac{n\pi y}{a}\right)dy \\
&= \dfrac{2V_0}{a} \left[-\dfrac{a}{n\pi}\cos \left(\dfrac{n\pi y}{a}\right)\right]_0^a \\
&= \dfrac{2V_0}{n\pi} \left[-\cos \left(\dfrac{n\pi y}{a}\right)\right]_0^a\\
&=\dfrac{2V_0}{n\pi} \left[-\cos \left(\dfrac{n\pi \cancel{a}}{\cancel{a}}\right) - (- \cos(0))\right] \\
&=\dfrac{2V_0}{n\pi} \left[1 - \cos n\pi\right] \\
&=\begin{cases}
0, & \text{even } n \\
\frac{4V_0}{n\pi}, &\text{odd } n
\end{cases}
\end{align*}
{% end %}

Where the last line comes from the fact that $\cos(n\pi)$ is equal to zero for even values of $n$ (i.e. for $0, 2\pi, 4\pi, 6\pi, \dots$) and -1 for odd values of $n$ (i.e. for $\pi, 3\pi, 5\pi, \dots$). Thus our complete solution becomes:

{% math() %}
\begin{align*}
V(x, y) &= \sum_{n = 1, 3,5, \dots}^\infty \dfrac{4V_0}{n\pi} \exp\left({-\dfrac{n\pi x}{a}}\right) \sin \left(\dfrac{n\pi y}{a}\right) \\
&= \dfrac{4V_0}{\pi} \left[\sin \left(\dfrac{\pi y}{a}\right)e^{-\pi x/a} + \dfrac{1}{3} \sin \left(\dfrac{3\pi y}{a}\right)e^{-3\pi x/a} + \dfrac{1}{5} \sin \left(\dfrac{5\pi y}{a}\right)e^{-5\pi x/a} + \dots\right]
\end{align*}
{% end %}

An interactive example, using the Desmos 3D calculator, can be found [at this link](https://www.desmos.com/3d/kdij7aiequ).

### Solutions of Laplace's equation in cylindrical and spherical coordinates

We have seen how to solve Laplace's equation for the electric potential $\nabla^2 V = 0$ using the separation of variables in Cartesian coordinates. But let us now consider the problem of solving Laplace's equation in _cylindrical_ and _spherical coordinates_. We will find that this is (alas!) a significantly harder problem, albeit one that still admits analytical solutions in many cases.

#### Solving in polar and cylindrical coordinates

In cylindrical coordinates, where we use the coordinates $\rho, \phi, z$ instead of $x, y, z$, Laplace's equation $\nabla^2 V = 0$ takes the form:

{% math() %}
\nabla^2 V = \dfrac{1}{\rho} \dfrac{\partial}{\partial \rho}\left(\rho \dfrac{\partial V}{\partial \rho}\right) + \dfrac{1}{\rho^2}\dfrac{\partial^2 V}{\partial \phi^2} + \dfrac{\partial^2 V}{\partial z^2}
{% end %}

> **Note:** in polar coordinates, the Laplacian takes essentially the same form, except without the partial derivative with respect to $z$.

Let us begin by assuming a solution in the form:

{% math() %}
V(\rho, \phi, z) = R(\rho)Q(\phi) Z(z)
{% end %}

If we have a problem that is symmetric about the $z$ axis, then we can effectively ignore the $z$ coordinate, leaving us with a polar problem for $V(\rho, \phi)$. Our Laplacian reduces to:

{% math() %}
\nabla^2 V = \dfrac{1}{\rho} \dfrac{\partial}{\partial \rho}\left(\rho \dfrac{\partial V}{\partial \rho}\right) + \dfrac{1}{\rho^2}\dfrac{\partial^2 V}{\partial \phi^2}
{% end %}

Substituting in $V(\rho, \phi) = R(\rho)Q(\phi)$ (we don't need to include $Z(z)$ as again we are ignoring the $z$ coordinate) we have the differential equations:

{% math() %}
\begin{gather*}
\rho \dfrac{d}{d \rho}\left(\rho \dfrac{d R}{d \rho}\right) = k^2 R \\
\dfrac{d^2 Q}{d \phi^2} = -k^2 Q
\end{gather*}
{% end %}

The solution to the second ODE is given by:

{% math() %}
Q(\phi) = \begin{cases}
A\cos k\phi + B\sin k\phi, & n \neq 0 \\
d_0 + d_1 \phi, & n = 0
\end{cases}
{% end %}

Due to the requirement of our assumption of symmetry about the $z$ axis, then $Q(\phi + 2\pi) = Q(\phi)$, which leads to the requirement that $k = n$, such that our solutions take the form:

{% math() %}
Q(\phi) = \begin{cases}
A\cos n\phi + B\sin n\phi, & n \neq 0 \\
d_0 + d_1 \phi, & n = 0
\end{cases}
{% end %}

Meanwhile, the solution to the first ODE is given by:

{% math() %}
R(\rho) = \begin{cases}
a\rho^n+ c\rho^{-n}, & n \neq 0 \\
b_0 + b_1 \ln \rho, & n = 0
\end{cases}
{% end %}

Thus the solution is given by:

{% math() %}
\begin{align*}
V(\rho, \phi) &= [b_0 + b_1 \ln \rho](d_0 + d_1 \phi) \\
&\qquad + \sum_{n,\, n \neq 0}^{\infty} \bigg[(a_n\rho^n + c_n \rho^{-n})(A_n \cos n\phi + B_n \sin n\phi)\bigg]
\end{align*}
{% end %}

> **Note:** If we want the solution to stay physically-valid (i.e. not blow up) for $\rho \to 0$, then we set $b_0 = 1, b_1 = 0, c_n = 0$. Conversely, if we want the solution to stay physically-valid for $r \to \infty$, then we set $b_1, d_1 = 0$ and $a_n = 0$ (as they are coefficients of terms that grow infinite as $\rho \to \infty$). Finally, if we want the solution to be independent of $\phi$, then we set $d_0 = 1$ and $d_1 = A_n = B_n = 0$.

What about cases in which we cannot ignore the $z$ coordinate? The resulting problem becomes more complicated, as the ODEs from the separation of variables become:

{% math() %}
\begin{gather*}
\rho \dfrac{d}{d \rho}\left(\rho \dfrac{d R}{d \rho}\right) + k^2 R = m^2 r^2 R \tag{1} \\
\dfrac{d^2 Q}{d \phi^2} = -m^2 Q \tag{2} \\
\dfrac{d^2 Z}{dz^2} = k^2 Z \tag{3}
\end{gather*}
{% end %}

Equation (1) is called **Bessel's differential equation** and the solutions to the ODE are given by the **Bessel functions** $J_m(\rho)$. We will not go into depth on the details, but the general solution is given by:

{% math() %}
\begin{align*}
V(\rho, \phi, z) = \sum_{m=1}^\infty \sum_{n=1}^\infty J_m(k_n\rho) (A_ne^{k_nz} + Be^{-k_nz})(C_n \sin m \phi + D_n \cos m\phi)
\end{align*}
{% end %}

#### Solving in spherical coordinates

Building on this approach, let us consider an more advanced problem, that of the solution of Laplace's equation in spherical coordinates. We may begin the problem by writing out Laplace's equation in spherical coordinates; unfortunately, it is not a particularly pretty expression:

{% math() %}
\begin{align*}
\nabla^2 V &= \frac{1}{r^2}\frac{\partial}{\partial r}
\left(r^2\frac{\partial V}{\partial r}\right)
+\frac{1}{r^2\sin \theta} \frac{\partial}{\partial \theta}\left(\sin \theta \frac{\partial V}{\partial \theta }\right)+
\frac{1}{r^2\sin^2\theta } \frac{\partial^2 V}{\partial \phi^2} \\
&=\frac{\partial^2 V}{\partial r^2}+\frac{2}{r}\frac{\partial V}{\partial r}+\frac{1}{r^2\sin \theta }\left(\cos \theta \frac{\partial V}{\partial \theta }+\sin \theta \frac{\partial^2 V}{\partial \theta^2}\right)+\frac{1}{r^2\sin^2\theta }\frac{\partial^2 V}{\partial \phi^2}
\end{align*}
{% end %}

> **Note on notation:** This is the most common convention $(r, \theta, \phi)$ used in physics, where $\theta$ is the zenith (up-down) angle and $\phi$ is the azimuthal (left-right) angle. Mathematicians swap $\theta$ and $\phi$ around, and there exist other notations as well. We will stick with the physics convention here and for the rest of this guide.

 We will now perform the separation of variables - that is, we assume a solution in the form:

{% math() %}
V(r, \theta, \phi) = R(r)\Theta(\theta)\Phi(\phi)
{% end %}

For those brave enough to actually substitute in this into the extremely-verbose Laplacian - go right ahead - but we will simply state the ODEs that come as a result of the separation of variables:

{% math() %}
\begin{gather*}
\dfrac{d^2 \Phi}{d\phi^2} = -m^2 \Phi \\
\dfrac{1}{\sin \theta} \dfrac{d}{d\theta} \left(\sin \theta \dfrac{d\Theta}{d\theta}\right) - \dfrac{m^2}{\sin^2 \theta} \Theta = -\ell(\ell + 1) \Theta \\
\dfrac{d}{dr}\left(r^2 \dfrac{dR}{dr}\right) = \ell(\ell + 1) R
\end{gather*}
{% end %}

The solution to the first ODE is given by $\Phi(\phi) = e^{im\phi}$, and the third is given by $R(r) = A_\ell r^\ell + B_\ell r^{-(\ell + 1)}$, where $A, B$ are some constants and $\ell$ is an integer. What about the second ODE, you ask? The solution is given by the regrettably-long expression:

{% math() %}
\Theta_{\ell, m}(\theta) = (-1)^m(1 - \cos^2 \theta)(1 - \cos^2 \theta)^{m/2} \dfrac{d^m}{dx^m} P_\ell(\cos \theta)
{% end %}

Where $P_\ell$ is called a **Legendre polynomial**, and $\ell$ and $m$ are integers. The Legendre polynomials are special functions that solve **Legendre's differential equation**, which is in fact the same as equation (2), with the substitution $x = \cos \theta$. The first few Legendre polynomials are given by:

{% math() %}
\begin{align*}
P_0(x) &= 1 \\
P_1(x) &= x \\
P_2(x) &= \dfrac{3x^2 - 1}{2} \\
P_3(x) &= \dfrac{5x^3 - 3x}{2} \\
P_4(x) &= \dfrac{35 x^4 - 30x^2 +3}{8} \\
P_5(x) &= \dfrac{63x^5 - 70x^3 + 15x}{8}
\end{align*}
{% end %}

It is common to group the solutions in $\theta$ and $\phi$ together to form the **spherical harmonics** $Y_{\ell, m}$ which are given by $Y_{\ell, m}(\theta, \phi) = \Theta(\theta) \Phi(\phi)$. Thus we may write the general solution as:

{% math() %}
V_{\ell, m}(r, \theta, \phi) = (A_\ell r^\ell  + B_\ell r^{-(\ell + 1)})Y_{\ell,m}(\theta, \phi)
{% end %}

Which is a _particular solution_ to Laplace's equation. But due to the linearity of Laplace's equation, this is not the _most_ general solution. The most general solution is found by summing over all possible values of $\ell$, so it is given by:

{% math() %}
V(r, \theta, \phi) = \sum_{\ell = 0}^\infty \sum_{m = -\ell}^\ell (A_\ell r^\ell  + B_\ell r^{-(\ell + 1)})Y_{\ell,m}(\theta, \phi)
{% end %}

For any problem that is symmetric about $\phi$ (possesses **azimuthal symmetry**), then we may set $m = 0$, and we have the "simpler" solution:

{% math() %}
V(r, \theta) = \sum_{\ell = 0}^\infty (A_\ell r^\ell + B_\ell r^{-(\ell + 1)}) P_\ell(\cos \theta)
{% end %}

 This is still a very complicated series, and one might imagine that finding the right coefficients $A_\ell$ and $B_\ell$ would be near-impossible. Luckily, we can again use Fourier's trick, which makes it comparatively straightforward to compute $A_\ell$ and $B_\ell$ by just evaluating some integrals. This works because both the Legendre polynomials and spherical harmonics satisfy orthogonality conditions:

{% math() %}
\begin{gather*}
\int_0^\pi P_\ell(\cos \theta) P_{\ell'}(\cos \theta) \sin \theta\, d\theta = \dfrac{2}{2\ell + 1} \delta_{\ell' \ell} =\begin{cases}
0, & \ell \neq \ell' \\
\dfrac{2}{2\ell + 1}, & \ell = \ell'
\end{cases} \\
\int_0^{2\pi} \int_0^\pi Y_{m, \ell}(\theta, \phi)Y_{m', \ell'}(\theta, \phi) \sin \theta \, d\theta\, d\phi = \delta_{\ell \ell'} \delta_{m m'}
\end{gather*}
{% end %}

Therefore, to solve for some boundary condition $V(R, \theta) = V_0(\theta)$ (boundary condition at $r = R$), if we take our general solution for $V(r, \theta)$, evaluate it at $r = R$ to get $V(R, \theta)$ and multiply both sides by $P_{\ell'} (\cos \theta) \sin \theta$ and integrate, we have:

{% math() %}
\int_0^\pi\sum_{\ell = 0}^\infty (A_\ell R^\ell + B_\ell R^{-(\ell + 1)}) P_\ell(\cos \theta)P_{\ell'}(\cos \theta) \sin \theta\, d\theta =\int_0^\pi V_0(\theta)P_{\ell'} (\cos \theta) \sin \theta d\theta
{% end %}

The left side of the integral, due to orthogonality, becomes:

{% math() %}
(A_\ell R^\ell + B_\ell R^{-(\ell + 1)})\dfrac{2}{2\ell + 1} = \int_0^\pi V_0(\theta)P_{\ell} (\cos \theta) \sin \theta d\theta
{% end %}

If we have a physical situation in which we require the solution to stay valid for $r \to 0$, then we have $B_\ell = 0$, and we need only solve for $A_\ell$. Conversely, if we have a physical situation where we require that the solution stays valid for $r \to \infty$, then we have $A_\ell = 0$, and we need only solve for $B_\ell$. The rest of the problem is simply evaluating the integral (which, although rather annoying, is a doable task). Remember that with just a few terms in the series, the solution to Laplace's equation can be found to good accuracy, so in many cases there is no need to integrate beyond the first few terms.

### Multipole expansions

It is often helpful to describe a complicated charge distribution in terms of a well-known charge distribution. In cases when a complicated charge distribution is _concentrated within a small region_, we can use an approximation method known as the **multipole expansion**.

Consider, for instance, a sphere of radius $R$, centered at the origin, with some complicated charge density $\rho(r', \theta')$. This is a problem that cannot be solved exactly in many cases. However, we can use the multipole expansion to find a solution that is "good enough" at distances (relatively) far away from the sphere.

To start, let us examine the particular solution of the potential in spherical coordinates. The solution is given by:

{% math() %}
V(r, \theta, \phi) = \dfrac{1}{4\pi\varepsilon_0}\iiint \dfrac{\rho(r', \theta', \phi')}{|\mathbf{r}- \mathbf{r}'|} {r'}^2 \sin \theta' \, dr'\, d\theta'\, d\phi'
{% end %}

If we let the magnitudes of the vectors be $r = |\mathbf{r}|$ and $r' = |\mathbf{r}'|$ then using the law of cosines, which says that $|\mathbf{r} - \mathbf{r}'|^2 = r^2 + r'^2 - 2rr' \cos \theta$, we may write:

{% math() %}
V(r, \theta, \phi) = \dfrac{1}{4\pi\varepsilon_0}\iiint \dfrac{\rho(r', \theta', \phi')}{\sqrt{r^2 + r'^2 - 2rr' \cos \theta}} {r'}^2 \sin \theta' \, dr'\, d\theta'\, d\phi'
{% end %}

We will consider the special case of azimuthal symmetry (i.e. $V(\mathbf{r})$ does not depend on $\phi$, for which we have:

{% math() %}
V(r, \theta) = \dfrac{1}{4\pi\varepsilon_0}\iiint \dfrac{\rho(r', \theta'){r'}^2 \sin \theta' }{\sqrt{r^2 + r'^2 - 2rr' \cos \theta}} \, dr'\, d\theta'\, d\phi'
{% end %}

This integral is quite difficult to evaluate! However, we may expand the square root using a series expansion (the [binomial expansion](https://en.wikipedia.org/wiki/Binomial_theorem) for those curious). It turns out (it won't be proven here) that in fact, the series expansion becomes:

{% math() %}
\dfrac{1}{\sqrt{r^2 + r'^2 - 2rr' \cos \theta}} =
\dfrac{1}{r} \sum_{n = 0}^\infty \left(\dfrac{r'}{r}\right)P_n(\cos \theta)
{% end %}

Where $P_n$ are our familiar Legendre polynomials! Thus, we can write out the potential in terms of an infinite series, as follows:

{% math() %}
\begin{gather*}
V(r, \theta, \phi) = \sum_{n = 0}^\infty V_n, \\V_n =\dfrac{1}{4\pi \varepsilon_0} r^{-(n + 1)} \int   (r')^n P_n(\cos \theta')\, \rho(\mathbf{r}') dV'
\end{gather*}
{% end %}

Where $dV' = r'^2 \sin \theta' d\theta' d\phi' dr'$ (the primes are important!), and the integral is evaluated for all (valid regions of) space, i.e. $r' \in [0, r], \theta' \in [0, \pi], \phi' \in [0, 2\pi]$. This series - the **multipole expansion** - is _exact_, but in practice we take only a few terms to our desired accuracy (or use the physics of the problem to argue that all terms outside than a few terms vanish). The first few terms are respectively given by:

{% math() %}
\begin{align*}
V_0 &= \dfrac{1}{4\pi \varepsilon_0} \dfrac{1}{r} \int \rho(r') dV' \\
V_1 &= \dfrac{1}{4\pi \varepsilon_0} \dfrac{1}{r^2} \int \rho(r') r' \cos \theta\, dV' \\
V_2 &= \dfrac{1}{4\pi \varepsilon_0} \dfrac{1}{2r^3} \int \rho(r') (r')^2 (3 \cos^2 \theta - 1)\,dV'
\end{align*}
{% end %}

From which we can begin to have a sense of why we call it the _multipole_ expansion. This is because, if we perform the first integral, we have:

{% math() %}
V_0 = \dfrac{1}{4\pi \varepsilon_0} \dfrac{Q_\text{total}}{r}
{% end %}

Which looks (and is!) the potential of a point charge, that is, an **electric monopole**! Meanwhile, if we perform the second integral, using the definition of the **dipole moment** (which is used to describe a two-charge i.e. _dipole_ system), we have:

{% math() %}
p_r = \int \rho(r') r' \cos \theta\, dV'
{% end %}

Then the integral evaluates to:

{% math() %}
V_1 = \dfrac{1}{4\pi \varepsilon_0} \dfrac{p_r}{r^2}
{% end %}

Which again also looks (and is!) the potential of a **perfect dipole**! We can continue this process as much as we want, leading to the origin of the name _multipole expansion_. Essentially, we assume that the potential very far away "looks" like a monopole, plus a dipole, plus all the other _nth_-poles, and that by summing all of them together, we get the true potential.

## Fields of polarized dielectrics

We recall that in a conductor, the electric field is very simple - $\mathbf{E}_\text{interior} = 0$ is true for _all conductors_. But the field is not so simple in _dielectric materials_ (which can be thought of at this stage as the same thing as insulators, though there _is_ a distinction). Dielectrics have _immobile charges_, meaning that their charges are **not free** to move freely throughout the material, although they can rotate and slightly shift in place. When a neutral dielectric is placed in an external electric field, **polarization** occurs, which, like in conductors, is due to negative charges experiencing a repulsive force and positive charges experiencing an attractive force in the direction of the external field. Unlike in a conductor, however, the negative and positive charges cannot move, so there is no charge separation; rather, they rotate (or in some cases stretch) in place to align with (or against) the field, as we show in the below diagram. 

{{ diagram(
src="dipole-moments-electric.excalidraw.svg"
desc="A diagram showing how dipole moments in a dielectric arise as a result of charges aligning towards (and others against) an applied field"
) }}

This process during polarization leads to a net **dipole moment**, denoted $\mathbf{p}$, where $\mathbf{p} = \alpha \mathbf{E}$ and $\alpha$ is the **polarizability**. The more strongly the dielectric is polarized, the higher the magnitude of its dipole moment.

> **Note:** For materials that consist of a single type of atom, $\alpha$ is a constant that is only dependent on the type of material; for molecular compounds, however, $\alpha$ is a matrix (technically, a _tensor_, and we will see the distinction later).

> **Note for advanced readers:** This is a classical description that does _not_ account for the quantum-mechanical nature of the atom. In reality, the electron _density_ is what is deflected to one side, as opposed to point particles aligning with and against the field, since quantum mechanics tells us that electrons have indeterminate positions and can thus be at *any* point in space around the nucleus - though the probability of finding an electron _is_ determined by the electron (probability) density function, whose density does show a noticeable change on polarization. But that is a much more extensive topic that will not (yet) be covered.

### Polarization field and bound charge

During polarization, the *combined dipole moments* of all the paired positive-negative charges within the dielectric produces a **polarization field**, denoted $\mathbf{P}$ (it is more commonly called the _polarization density_). When there is no applied field, there is no polarization, so $\mathbf{P} = 0$; but when there is an applied field $\mathbf{E}_\text{ext.}$, there _is_ polarization, so $\mathbf{P} \neq 0$, and thus the polarization field _changes_ the total electric field within the dielectric.

> **Note:** In most "normal" (non-extreme-physics) situations, the polarization field $\mathbf{P}$ is linearly-related to the total field $\mathbf{E}$ by $\mathbf{P} = \varepsilon_0 \chi_e \mathbf{E}$, where $\chi_e$ is called the _electric susceptibility_. In cases where this is not true, we have entered the domain of **nonlinear optics**, but that is a very advanced topic for another time.

Since the paired charges within a dielectric are bound in place and can only stretch/rotate during polarization, we call them **bound charges**. We write the bound charge as $Q_\text{bound}$, where $\rho_\text{bound} = \dfrac{dQ_\text{bound}}{dt}$ is the *bound charge density*. When polarization occurs, as we have seen, the paired charges effectively behave as many, many tiny dipoles. Now, the electric potential associated with a single electric dipole at a fixed location $\mathbf{r}$ is given by:

{% math() %}
V(\mathbf{r}) = \dfrac{1}{4\pi \varepsilon_0} \dfrac{\mathbf{p} \cdot (\hat r - \hat r')}{|\mathbf{r} - \mathbf{r}'|^2}
{% end %}

Where again $\mathbf{p}$ is the dipole moment (in this case, of a single dipole). Since the polarization field is formed by the combined contribution of many, many of these tiny dipoles, we can integrate over all of these dipoles in space to obtain the total potential:

{% math() %}
V_\text{polarization} = \dfrac{1}{4\pi \varepsilon_0} \int \limits_\text{dielectric} \dfrac{\mathbf{P} \cdot (\hat r - \hat r')}{|\mathbf{r} - \mathbf{r}'|^2} dV'
{% end %}

We find that upon performing this integral (which requires integration by parts and applying the divergence theorem), the result becomes:

{% math() %}
V_\text{polarization} = \dfrac{1}{4\pi \varepsilon_0} \bigg[\underbrace{\oint\dfrac{\mathbf{P}}{|\mathbf{r}-\mathbf{r}'|} \cdot d\mathbf{A}'}_\text{"surface" charge} - \underbrace{\int \dfrac{\nabla \cdot \mathbf{P}}{|\mathbf{r}-\mathbf{r}'}dV'}_\text{"volume" charge}\bigg]
{% end %}

We find that the two resulting terms - a surface integral and a volume integral - _look_ like the potentials generated by a surface charge and a volume charge! Thus, we can define a surface charge density $\sigma_\text{bound} \equiv \mathbf{P} \cdot \hat{\mathbf{n}}$ (where $\hat{\mathbf{n}}$ is the unit surface normal) and a volume charge density $\rho_{v, \text{bound}} = -\nabla \cdot \mathbf{P}$ to write the above equation in a nicer way:

{% math() %}
V_\text{polarization} = \dfrac{1}{4\pi \varepsilon_0} \left[\oint \dfrac{\sigma_\text{bound}}{|\mathbf{r} - \mathbf{r}'|}\,dA + \int \dfrac{\rho_{v, \text{bound}}}{|\mathbf{r} - \mathbf{r}'|} dV\right]
{% end %}

We should note that there is a slight technical nuance when we describe the bound charge, which we will explain in the same fashion as Griffiths. In theory, *all* charges in a dielectric are bound, since they cannot move out of their places (other than rotating/stretching). As we know, polarization causes the charges to orient themselves like dipoles and thus leads to a nonzero dipole moment. However, the positive end of one dipole will often point in the same direction as the negative end of another dipole, cancelling the polarization out, at least in uniform interior regions of the material. But this "cancelling out" doesn't happen in two places, (1) on the surface of the material, since there aren't any dipoles above the surface to cancel out the outward-facing charged end of the dipoles, and (2) in non-uniform polarized regions inside the material, where the positive end of one dipole does not precisely align with the negative end of another. $\sigma_\text{bound}$ represents the first case: the surface charges that contribute a nonzero dipole moment. $\rho_{v, \text{bound}}$ represents the second case: the charges in non-uniform regions in the interior of the dielectric, which also contribute a nonzero dipole moment. All the other charges' dipole moments cancel out, so while they are certainly bound, they play no discernable role in polarization and we typically exclude them from our definition of bound charge. So it may be better to speak of bound charge as _only_ those charges in a dielectric that contribute a **net** dipole moment, which is separated into those on the surface and those in the interior of the dielectric. To let us recap:

| Physical scenario                               | Bound charges                                               | Why?                                                                                                                                                                                                                                                                                                               |
| ----------------------------------------------- | ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Neutral dielectric                              | $\rho_{v, \text{bound}} = \sigma_\text{bound} = 0$          | Without polarization, charges are randomly aligned and mutually cancel each other out                                                                                                                                                                                                                              |
| Homogeneous (uniform) polarized dielectric      | $\rho_{v, \text{bound}} = 0, \sigma_\text{bound} \neq 0$    | Polarization causes charges to align, so paired charges form dipoles. Since the material is uniform, the oppositely-charged ends of the dipoles are cancelled out by each other in the _interior_ of the material. But there is nothing to cancel out those on the surface, so $\sigma_\text{bound} \neq 0$        |
| Inhomogenous (non-uniform) polarized dielectric | $\rho_{v, \text{bound}} \neq 0, \sigma_\text{bound} \neq 0$ | Polarization (again) causes charges to align, so paired charges form dipoles. While the dipoles cancel each other out in *uniform* interior regions, they don't cancel each other out on the surface or in _non-uniform_ interior regions. Thus $\sigma_\text{bound} \neq 0$ *and* $\rho_{v, \text{bound}} \neq 0$ |

Where the bound charges are respectively calculated with:

{% math() %}
\begin{matrix*}
\sigma_\text{bound} = \mathbf{P} \cdot \hat{\mathbf{n}} = |\mathbf{P}| \cos \theta, \\
\rho_{v, \text{bound}} = -\nabla \cdot \mathbf{P}
\end{matrix*}
{% end %}

Remember that a dielectric is not one-sided, most of the time! For instance, a dielectric shaped into a rectangular block has two surfaces (the top and bottom), _each_ of which has an associated surface bound charge $\sigma_\text{bound}$, so it is necessary to calculate the top surface's bound charge $\sigma_{b, \text{top}}$ and bottom surface's bound charge $\sigma_{b, \text{bottom}}$. Also beware: the top and bottom surfaces have _opposite-pointing_ normal vectors, which must be considered when doing the dot product $\mathbf{P} \cdot \hat{\mathbf{n}}$. With all of this in mind, the total bound charge on the top _and_ bottom surfaces combined is given by integrating over the top and bottom surfaces:

{% math() %}
Q_\text{surface} = \int \limits_\text{bottom}\sigma_{b, \text{ top}} dA + \int \limits_\text{top} \sigma_{b, \text{ bottom}} dA
{% end %}

In addition, if it is a non-uniform dielectric ($\rho_\text{bound} \neq 0$), the bound charge in the interior of the dielectric is given by:

{% math() %}
Q_\text{interior} = \int \rho_\text{bound} dV
{% end %}

And the **total bound charge** would be given by:

{% math() %}
Q_{\text{bound}, T} = Q_\text{surface} + Q_\text{interior}
{% end %}

>**Note:** As a reminder, all of this is a simplified model! The fields within a dielectric are extremely complicated at a microscopic level and our simplifying assumptions (especially the approximation of paired charges in the dielectric as perfect electric dipoles) no longer work at microscopic scales (although Maxwell's equations still apply), so it is best to think of all of this as an **approximate** model that provides reasonably-accurate results _on big length scales_ (big = length scales of micrometers or bigger, which is much larger than atomic scales, but still small compared to observable sizes).

### Free charges and Gauss's law in matter

In any given physical scenario, not all of the charges are going to be bound charges nor can be considered negligible because they cancel out. This is because (1) we need some outside charge to actually *cause* the polarization in the first place, (2) dielectrics can contain "pockets" where charges (e.g. ions) can move, and (3) not all charges are located within the dielectric itself. Such non-bound charges are referred to as **free charges**, denoted $Q_\text{free}$, with the _free charge density_ being $\rho_\text{free}$. As you can see, physicists do not possess much creative flair when it comes to naming things. Free charges are useful because they are usually **known**, and **Gauss's law for free charges** (also called **Gauss's law in matter**) tells us the field generated by those free charges, which is typically written as $\mathbf{D}$ (also called the _electric displacement field_):

{% math() %}
\nabla \cdot \mathbf{D} = \rho_\text{free} \Leftrightarrow \oint \mathbf{D} \cdot d\mathbf{A} = Q_\text{free}
{% end %}

Where, in the above integral version of Gauss's law for free charges, the integral is taken over a surface enclosing _all_ the free charge. We know already know how to solve the standard version of Gauss's law for common geometries, so finding $\mathbf{D}$ is relatively straightforward. When we want to calculate the total electric field outside and inside a polarized dielectric, we can then use the relationship between the total field $\mathbf{E}$ and $\mathbf{D}$ to find:

{% math() %}
\mathbf{D} = \varepsilon_0 \mathbf{E} + \mathbf{P} \Leftrightarrow \mathbf{E} = \dfrac{1}{\varepsilon_0}(\mathbf{D} - \mathbf{P})
{% end %}

> **Note:** This is also called the **constitutive relation**.

In the special case of a conductor, we have $\mathbf{D} = \mathbf{P}$. In physical terms, it means that the field created by all the free charges is _perfectly opposed_ by the polarization field arising from the polarization of the charges inside the conductor, leading to zero total field, that is, $\mathbf{E} = 0$. This is why the electric field in a conductor is _zero_, mathematically-speaking. But this is **not true** in dielectrics. Here, the $\mathbf{P}$ (polarization) field _does not_ cancel out the $\mathbf{D}$ field of the free charges, leading to a nonzero total field, that is, $\mathbf{E} \neq 0$.

> **Note:** What about a _neutral_ material? Regardless of whether the material is a conductor or dielectric, the random alignment of charges in the absence of polarization means that $\mathbf{P} = 0$. Meanwhile, since the positive and negative free charges exactly cancel out, $\mathbf{D} = 0$. Therefore, $\mathbf{E} = \frac{1}{\varepsilon_0}(\mathbf{D} - \mathbf{P})$ predicts that the total field would be zero as well, as we would expect.

### The field of a wire surrounded by a dielectric

Borrowing an example from Griffiths (Example 4.4), consider the case of a long and thin wire of linear charge density $\lambda$, surrounded by some insulating casing made of a dielectric material. In this example, the whole wire (including the casing) has radius $R$. Using Gauss's law for free charges, we can surround the long, thin wire with a cylindrical Gaussian surface of length $L$ and radius $r$, which has surface area $2\pi r L$. Meanwhile, the enclosed free charge within the cylinder would be $Q_\text{free} = \lambda L$. Thus:

{% math() %}
\begin{gather*}
\oint \mathbf{D} \cdot d\mathbf{A} = Q_\text{free} \\
\Rightarrow D(2\pi r L) = \lambda L \\
\Rightarrow D = \dfrac{\lambda}{2\pi r} \\
\Rightarrow \mathbf{D} = \dfrac{\lambda}{2\pi r} \hat r
\end{gather*}
{% end %}

We want to calculate the total electric field, both within the wire ($r \leq R$) and outside of it ($r > R$. Outside the wire, there isn't any other charge, much less any bound charge, so $\mathbf{P} = 0$, and thus the total field is given by:

{% math() %}
\begin{align*}
\mathbf{E} &= \dfrac{1}{\varepsilon_0}(\mathbf{D} - \cancel{\mathbf{P}}^0) \\
&= \dfrac{1}{\varepsilon_0}\mathbf{D} \\
&= \dfrac{\lambda}{2\pi r \varepsilon_0} \hat r, \quad r > R
\end{align*}
{% end %}

Inside the wire (and thus in the dielectric region), the total electric field is given by:

{% math() %}
\begin{align*}
\mathbf{E} &= \dfrac{1}{\varepsilon_0}(\mathbf{D} - \mathbf{P}) \\
&= \dfrac{\lambda}{2\pi r \varepsilon_0} \hat r - \dfrac{1}{\varepsilon_0}\mathbf{P}, \quad r \leq R
\end{align*}
{% end %}

Which we could write as an explicit expression _if_ we knew $\mathbf{P}$. Assuming that the dielectric material was a _linear material_ (this is usually a good approximation for most materials under normal conditions), then the $\mathbf{P}$ field satisfies $\mathbf{P} = \varepsilon_0 \chi_e \mathbf{E}$, where $\chi_e$ is the **electric susceptibility**. So, by rearranging $\mathbf{E} = \dfrac{1}{\varepsilon_0}(\mathbf{D} - \mathbf{P})$ we get:

{% math() %}
\begin{align*}
\mathbf{E} &= \dfrac{1}{\varepsilon_0}(\mathbf{D} - \mathbf{P}) \\
&= \dfrac{1}{\varepsilon_0}\mathbf{D} - \dfrac{1}{\cancel{\varepsilon_0}}\cancel{\varepsilon_0} \chi_e \mathbf{E} \\
&=\dfrac{1}{\varepsilon_0}\mathbf{D} - \chi_e \mathbf{E} \\
\Rightarrow \mathbf{E} &+ \chi_e \mathbf{E} = \dfrac{1}{\varepsilon_0}\mathbf{D} \\
\quad \mathbf{E}&\varepsilon_0 (1 + \chi_e) = \mathbf{D} \\
\quad \mathbf{E}&\varepsilon = \mathbf{D},\quad \mathbf{D} \propto \mathbf{E}
\end{align*}
{% end %}

Where $\varepsilon \equiv \varepsilon_0(1 + \chi_e)$ is known as the **permittivity** (this is why $\varepsilon_0$ is often called the _vacuum permittivity_ or the _permittivity of free space_). Using the relationship we just derived, the electric field *inside* the wire would simply be given by:

{% math() %}
\begin{align*}
\mathbf{E}_\text{interior} &= \dfrac{1}{\varepsilon} \mathbf{D} \\
&=\dfrac{\lambda}{2\pi r \varepsilon} \hat r, \quad r \leq R
\end{align*}
{% end %}

We can write this in a slightly different way by defining $\kappa = \varepsilon/\varepsilon_0$ to be the **dielectric constant** of the material, for which the interior field would then be:

{% math() %}
\begin{align*}
\mathbf{E}_\text{interior} &= \dfrac{\lambda}{2\pi r \kappa \varepsilon_0} \hat r, \quad r \leq R \\
&= \dfrac{1}{\kappa} \mathbf{E}_\text{outside}
\end{align*}
{% end %}

Thus, the total electric field, inside as well as outside the material, would be:

{% math() %}
\mathbf{E}(r) = \begin{cases}
\dfrac{\lambda}{2\pi r \kappa \varepsilon_0} \hat r, &\quad r \leq R \\
\dfrac{\lambda}{2\pi r \varepsilon_0} \hat r, &\quad r > R
\end{cases}
{% end %}

### The field of a uniformly polarized sphere

Let us now consider the case of a uniformly polarized sphere of radius $R$ (Griffiths example 4.2) with _no free charge_. Knowing that it is _uniformly polarized_, then it must be the case that there is no interior bound charge, that is, $\rho_\text{bound} = 0$. But there is still surface bound charge, and the surface bound charge density is given by $\sigma_\text{bound} = \mathbf{P} \cdot \hat{\mathbf{n}}$. In this case, we can solve Laplace's equation with the boundary condition $V \to 0$ for $r \to \infty$. We solved this earlier in our section on the [method of images](#the-method-of-images) for a charged sphere with constant charge $Q_0$ (where here, $Q_0 = 4\pi R^2 \sigma_\text{bound}$); the solution for the potential is:

{% math() %}
V(r, \theta) = \begin{cases}
\dfrac{\sigma_\text{bound} r}{3\varepsilon_0}, & r \leq R \\
\dfrac{\sigma_\text{bound} R^3}{3\varepsilon_0 r^2}, & r > R
\end{cases}
{% end %}

From which, substituting $\sigma_\text{bound} = \mathbf{P} \cdot \hat{\mathbf{n}}$ where $\hat{\mathbf{n}} = \hat r$, and using $\mathbf{E} = -\nabla V$, we find that the electric field is given by:

{% math() %}
\mathbf{E} = \begin{cases}
-\dfrac{1}{3\varepsilon_0} \mathbf{P}, & r \leq R \\[10pt]
\dfrac{2R^3}{3 \varepsilon_0r^3} \mathbf{P}, & r > R
\end{cases}
{% end %}

Unfortunately, this is a case where we cannot (in general) solve for the field using the _constitutive relation_ $\mathbf{E} = \dfrac{1}{\varepsilon_0}(\mathbf{D} + \mathbf{P})$. Let's take a moment to understand why this is the case. Recall that Gauss's law for free charges takes the form:

{% math() %}
\oint \mathbf{D} \cdot d\mathbf{A} = Q_\text{free}
{% end %}

Now, we stated previously that our uniformly-polarized sphere has no free charge, so _in theory_ we would have:

{% math() %}
\oint \mathbf{D} \cdot d\mathbf{A} = 0
{% end %}

The issue arises because while we may think $\displaystyle \oint \mathbf{D} \cdot d\mathbf{A} = 0$ _implies_ $\mathbf{D} = 0$, this is not necessarily the case if the polarization is along a _non-radial axis_. The polarization will still be uniform (a constant value), but because it is _directional_, we lose radial symmetry, and therefore we can no longer make the assumption that just because $\displaystyle \oint \mathbf{D} \cdot d\mathbf{A} = 0$ means $\mathbf{D} = 0$.

### A conclusion on free and bound charges

As we have seen, the free and bound charges give us a way to express the total electric field in a dielectric in a more straightforward way than needing to solve Maxwell's equations for every single charge. By using **Gauss's law for free charges** to find the field's contribution from the free charge, and the constitutive relations to find the bound charge, we can then calculate the total electric field. Since the total field in a polarized dielectric consists of both the $\mathbf{D}$ field from free charges as well as the $\mathbf{P}$ field from the bound charges (due to the effects of polarization), the total charge density can be written as:

{% math() %}
\rho_\text{total} = \rho_\text{free} + \rho_\text{bound}
{% end %}

Gauss's law for free charges is one of the four **Maxwell equations in matter**, which we will soon see more of. Maxwell's equations in matter allow us to describe the fields inside dielectrics (and inside matter in general), something that would be very hard to do with the standard Maxwell equations.

> **Note:** In any problem involving dielectrics, one can also find the _total_ charge by adding up the free charge and bound charge, and then use the conventional form of Gauss's law ($\nabla \cdot \mathbf{E} = \rho/\varepsilon_0$) to calculate the field. However, this presumes that you _know_ the bound charge, which is typically not the case.