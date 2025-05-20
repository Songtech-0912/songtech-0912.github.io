+++
title = "Introduction to Quantum Mechanics"
date = 2024-05-07
+++

This a mini-book on quantum mechanics at a beginner's level, with topics covered including wavefunctions, various solutions of the time-dependent and independent Schrödinger equation, the uncertainty principle, and expectation values.

<!-- more -->

## Why quantum theory?

{{ natural_img(src="https://cdn10.picryl.com/photo/2014/12/31/niels-bohr-standing-at-blackboard-principal-investigatorproject-analog-conversion-85f94c-1024.jpg", desc="An image of physicist Niels Bohr, an early proponent of quantum mechanics, standing at a whiteboard") }}

_Niels Bohr doing quantum mechanics - [source](https://nara.getarchive.net/media/niels-bohr-standing-at-blackboard-principal-investigatorproject-analog-conversion-85f94c)_

Quantum theory is our best understanding of how the universe works at its most fundamental level. It is fundamentally paradoxical to human experience, but it is the bedrock of almost all of modern physics and its predictive power has made technological innovations possible. In addition, it is also a very scientifically and philosophically interesting theory to learn. This article forms the basis of an introduction to quantum mechanics.

## Getting started with quantum mechanics

Our understanding of classical physics has served us well for centuries and still makes very accurate predictions about the world. But since the 20th century, we have found that the classical mechanics is actually only part of a much broader theory - quantum mechanics - that applies in many areas that classical theory fails. Quantum theory can explain the same phenomena that classical physics can, but it explains so much more that classical physics can't. It is truly a pillar - and wonder - of modern physics. In fact, it is the most accurate theory of physics ever created, especially with its subdiscipline of quantum field theory - and specifically, quantum electodynamics - that predicts quantities so precisely that they have been confirmed to [ten parts in a billion](https://en.wikipedia.org/wiki/Precision_tests_of_QED).

But quantum theory can be difficult to comprehend, in part because it is founded on very different principles as compared to classical physics:

- The Universe is fundamentally described by probability distributions, as opposed to objects with exact positions and trajectories
- Physical quantities can only take on particular values and exact knowledge about them is often impossible
- Properties of quantum particles include many that don't exist for classical particles, such as the ability to pass through a solid barrier and having a nonzero energy even when stationary in a region of zero potential energy

We **don't** know why we observe the world to behave in this way, and the interpretation of quantum mechanics is a separate philosophical question. Rather, we will simply consider the theory as a model that makes accurate predictions about the world without delving into _why_.

In the first few sections, we'll introduce quantum mechanics without explaining why it works. Consider this as simply a preview of the essential features of quantum mechanics. In the sections after, we'll actually explain why quantum theory works, and derive many of the relations we take for granted in applying quantum mechanics. 

## Mathematical foundations

What follows is a relatively brief mathematical overview of only the fundamentals required for starting quantum physics. However, it would certainly be helpful to have a background in multivariable calculus, differential equations, and some linear algebra (vectors, matrices, and eigenvalues). Don't worry if these are alien topics! There are expanded guides to each in the [calculus series](@/calculus-series.md). In addition, while not required, the [introductory classical dynamics series](@/classical-dynamics.md) can be very helpful as well.

### Eigenvalues and eigenfunctions

To start with understanding quantum theory, we must first start with a concept that may be familiar to those who have studied linear algebra, although knowledge of linear algebra is not required. Consider the function $y(x) = e^{kx}$. If we take its derivative, we find that:

{% math() %}
\dfrac{dy}{dx} = ke^{kx}
{% end %}

Which we notice, can also be written as:

{% math() %}
\frac{dy}{dx} = ky
{% end %}

Notice that the derivative of $y(x)$ is just $y(x)$ multiplied by $k$. We call $y(x)$ an **eigenfunction**, because when we apply the derivative, it just becomes multiplied by a constant, and we call the constant here, $k$, an **eigenvalue**. The exponential function is not the only function that can be an eigenfunction, however. Consider the cosine function $y(x) = \cos kx$. Taking its _second derivative_ results in:

{% math() %}
\frac{d^2 y}{dx^2} = -k^2 \cos kx = -k^2 y
{% end %}

So cosine is _also_ an eigenfunction, except its eigenvalue is $-k^2$ rather than $k$. We can show something very similar with sine - which makes sense because a sine curve is just a shifted cosine curve.

### Complex numbers

In quantum mechanics, we find that real numbers are not enough to fully describe the physics we observe. Rather, we need to use an _expanded number system_, that being the complex numbers.

A complex number can be thought of as a pair of two real numbers. First, we define the _imaginary unit_ $i = \sqrt{-1}$. To start, this seems absurd. We know that no real number can have this property. But the fact that _complex_ numbers do have this properties gives rise to many useful mathematical properties. For instance, it allows for a class of solutions to polynomial equations that can't be expressed in terms of real numbers.

We often write a complex number in the form $z = \alpha + \beta i$, where $\alpha$ is called the _real_ part and $\beta$ is called the _imaginary_ part. For a complex number $z$, we can also define a _conjugate_ given by $\bar z = \alpha - \beta i$ (some texts use $z^*$ as an alternative notation). Uniquely, $z \bar z = (\alpha + \beta i)(\alpha - \beta i) = \alpha^2 + \beta^2$.

Complex numbers also have another essential property. If we define the exponential function $f(x) = e^x$ in a way that allows for complex arguments, i.e. $f(z) = e^{z} = e^{\alpha + \beta i}$, we find that $e^{i\phi} = \cos \phi + i \sin \phi$. This is called **Euler's formula** and means we can use complex exponentials to write complex numbers in the form $z = re^{i\phi}$ where $r = \sqrt{\alpha^2 + \beta^2}$ and $\phi = \tan^{-1} \beta/\alpha$, converting to trigonometric functions whenever more convenient and vice-versa. 

But why do we use - or care - about complex exponentials? Mathematically speaking, complex exponentials satisfy all the properties of exponential functions, such as $e^{iA} e^{iB} = e^{i(A + B)}$ and $e^{iA} e^{-iB} = e^{A-B}$. This greatly simplifies calculations. 

> For a more in-depth review, it may be helpful to see the refresher on [logarithmic and exponential functions here](@/exponential-logs.md).

In addition, Euler's formula results in several identities that are also very helpful in calculations. From $e^{i\phi} = \cos \phi + i\sin \phi$ we can in turn find that $e^{i\phi} + e^{-i\phi} = 2\cos \phi$ and $e^{i\phi} - e^{-i\phi} = 2i \sin \phi$. We will use these extensively later on.

The study of calculus that applies to complex numbers is called _complex analysis_. For most of quantum mechanics, we won't need to do full complex analysis, and can treat $i$ as simply a constant. There are, however, some advanced branches of quantum mechanics that _do_ need complex analysis.

### The wave equation

In classical physics, the laws of physics are described using _differential equations_. Differential equations are a very, very broad topic, and if unfamiliar, feel free to read [the dedicated article on differential equations](@/differential-equations/index.md). Their usefulness comes from the fact that differential equations permit descriptions of large classes of different physical scenarios. Consider, for instance, the wave equation:

{% math() %}
\frac{\partial^2 y}{\partial t^2} = v^2 \frac{\partial^2 y}{\partial x^2} 
{% end %}

This partial differential equation models everything from water ripples in a pond to the vibrations of a drum and even to light - which is an _electromagnetic wave_. The last one, however, is particularly important for quantum mechanics, because light is fundamentally quantum in nature, and the study of light is a crucial part of quantum mechanics.

To solve the wave equation, we may use the _separation of variables_. That is to say, we assume that the solution $y(x, t)$ is a product of two functions $f(x)$ and $g(t)$, such that:

{% math() %}
y(x, t) = f(x) g(t)
{% end %}

This means that we can take the second partial derivatives of $y(x, t)$ as follows.

{% math() %}
\begin{align*}
\dfrac{\partial^2 y}{\partial x^2} &= \dfrac{\partial^2}{\partial x^2} \left(f(x) g(t)\right) = g(t) \dfrac{\partial^2}{\partial x^2} f(x) \\ &= g(t) \dfrac{\partial^2 f}{\partial x^2} \\
\dfrac{\partial^2 y}{\partial t^2} &= \dfrac{\partial^2}{\partial t^2} \left(f(x) g(t)\right) = f(x) \dfrac{\partial^2}{\partial t^2} g(t) \\ &= f(x) \dfrac{\partial^2 g}{\partial t^2} \\
\end{align*}
{% end %}

> Note that we are able to factor out $g(t)$ when taking the second derivative of $y(x, t)$ with respect to $x$ because $g(t)$ _doesn't_ depend on $x$, and therefore we can treat it as a **constant**. The same principle applies when taking the second derivative of $y(x, t)$ with respect to $t$; as $f(x)$ doesn't depend on $t$, we can also treat it as a constant and factor it out of the second derivative.

If we substitute these expressions for the second derivatives back into the wave equation $\partial_{t}{}^2 y = v^2 \partial_{x}{}^2 y$ we have:

{% math() %}
f(x) \dfrac{\partial^2 g}{\partial t^2} = v^2 g(t) \dfrac{\partial^2 f}{\partial x^2}
{% end %}

> **Note on notation:** Here $\partial_{t}{}^2 y$ is a shorthand for $\dfrac{\partial^2 y}{\partial t^2}$ and $\partial_{x}{}^2 y$ is a shorthand for $\dfrac{\partial^2 y}{\partial x^2}$.

From our substituted wave equation, we can now perform some algebraic manipulations by dividing both sides by $f(x) g(t)$ and then multiplying both sides by $\dfrac{1}{v^2}$, as shown:

{% math() %}
\begin{align*}
\dfrac{1}{f(x) g(t)} f(x) \dfrac{\partial^2 g}{\partial t^2} &= \dfrac{1}{f(x) g(t)}v^2 g(t) \dfrac{\partial^2 f}{\partial x^2} \Rightarrow \\
\dfrac{1}{g(t)} \dfrac{\partial^2 g}{\partial t^2} &= v^2 \dfrac{1}{f(x)}\dfrac{\partial^2 f}{\partial x^2} \\
\dfrac{1}{v^2 g(t)} \dfrac{\partial^2 g}{\partial t^2} &= \dfrac{1}{f(x)}\dfrac{\partial^2 f}{\partial x^2}
\end{align*}
{% end %}

However, if two expressions involving different partial derivatives are equal each other, then they must both be equal to a constant. This is called the **separation constant**, which we can set to a generic constant that can be positive or negative in sign (as the sign doesn't change the fact that it is constant), multiplied by any other constant, or raised to any power, as none of these operations change the fact that the end result is a constant. If we let that constant be $-k^2$ (we can choose any other constant or sign but this particular choice makes calculations easier later), we have:

{% math() %}
\dfrac{1}{v^2 g(t)} \dfrac{\partial^2 g}{\partial t^2} = \dfrac{1}{f(x)}\dfrac{\partial^2 f}{\partial x^2} = -k^2
{% end %}

Which means we have _separated_ the wave equation into two differential equations, one only involving $f(x)$, and one only involving $g(t)$:

{% math() %}
\dfrac{1}{v^2 g(t)} \dfrac{\partial^2 g}{\partial t^2} = -k^2 \\
\dfrac{1}{f(x)}\dfrac{\partial^2 f}{\partial x^2} = -k^2
{% end %}

This is the method of **separation of variables**, which is covered in the [differential equations guide](@/differential-equations/index.md) as well as the [solving separable PDEs guide](@/solving-pdes.md). The idea is to reduce a partial differential equation into several ordinary differential equations that are easier to solve.

At this point we should note that since $g(t)$ is purely a function of $t$ and $f(x)$ is purely a function of $x$, neither are multivariable functions and thus the partial derivatives reduce to ordinary derivatives:

{% math() %}
\dfrac{1}{v^2 g(t)} \dfrac{d^2 g}{d t^2} = -k^2 \\
\dfrac{1}{f(x)}\dfrac{d^2 f}{d x^2} = -k^2
{% end %}

We can algebraically rearrange terms in both equations to get them into a slightly nicer and cleaner form:

{% math() %}
\begin{align*}
\dfrac{d^2 g}{d t^2} &= -k^2 v^2 g(t) \\
\dfrac{d^2 f}{d x^2} &= -k^2 f(x) 
\end{align*}
{% end %}

If we define another constant named $\omega$ which is defined as $\omega \equiv kv$ ($\equiv$ is the symbol for "defined as") we can rewrite even more nicely as:

{% math() %}
\begin{align*}
\dfrac{d^2 g}{d t^2} &= -\omega^2 g \\
\dfrac{d^2 f}{d x^2} &= -k^2 f
\end{align*}
{% end %}

Solving these ordinary differential equations involves finding functions $g(t)$ and $f(x)$ whose second derivatives are equal to themselves, multiplied by a constant. We can use the _ansatz_'s (_ansatz_ is a fancy German-derived word for "educated guess") of complex exponential functions as the solutions, and then check that this does indeed work:

{% math() %}
\begin{align*}
g(t) &= e^{-i\omega t} \rightarrow \dfrac{d^2 g}{dt^2} = -\omega^2 e^{-i\omega t} = -\omega^2 g(t) \\
f(x) &= e^{-ik t} \rightarrow \dfrac{d^2 f}{dt^2} = -k^2 e^{-ik t} = -k^2 f(x) \\
\end{align*}
{% end %}

However, we find that $g(t) = e^{i\omega t}$ and $f(x) = e^{ikx}$ _also_ works:

{% math() %}
\begin{align*}
g(t) &= e^{i\omega t} \rightarrow \dfrac{d^2 g}{dt^2} = -\omega^2 e^{i\omega t} = -\omega^2 g(t) \\
f(x) &= e^{ik t} \rightarrow \dfrac{d^2 f}{dt^2} = -k^2 e^{ik t} = -k^2 f(x) \\
\end{align*}
{% end %}

So we write the general solution as a _linear combination_ (i.e. sum with constant coefficients) of the two respective solutions for each:

{% math() %}
g(t) = C_1 e^{i\omega t} + C_2 e^{-i\omega t} \\
f(x) = C_3 e^{ik x} + C_4 e^{-ik x} \\
{% end %}

Now recalling that we set $y(x, t) = f(x) g(t)$ we can substitute our solutions to get the **general solution** for the 1D wave equation:

{% math() %}
y(x, t) = \left(C_1 e^{i\omega t} + C_2 e^{-i\omega t}\right)\left(C_3 e^{ik x} + C_4 e^{-ik x}\right)
{% end %}

> **Note for the mathematical reader:** Technically speaking, this is not the _most_ general solution, as any linear combination of this solution is a solution, given that the wave equation is a linear partial differential equation (PDE). Furthermore, given that one may always add a function to a solution to a PDE that gets differentiated away (as taking a partial derivative of a function with respect to a variable that the function doesn't depend on gives zero), the most general solution is actually $y(x, t) = u(x - vt) + w(x + vt)$ for _any_ two twice-differentiable functions $u, w$.

Expanding the solution we obtained out, we have:

{% math() %}
\begin{align*}
y(x, t) &= C_1 C_3 e^{i\omega t} e^{ikx} + C_1 C_4 e^{i\omega t} e^{-ikx} + C_2 C_3 e^{-i\omega t} e^{ikx} + C_2 C_4 e^{-i\omega t} e^{-ikx} \\
&= (C_2 C_3 e^{ikx - i\omega t} + C_1 C_4 e^{-ikx + i\omega t}) + (C_1 C_3 e^{ikx + i\omega t} + C_2 C_4 e^{-ikx -i\omega t}) \\
& = (C_2 C_3 e^{i(kx - \omega t)} + C_1 C_4 e^{-i(kx - \omega t)}) + (C_1 C_3 e^{i(kx + \omega t)} + C_2 C_4 e^{-i(kx + \omega t)})
\end{align*}
{% end %}

We note that this general solution is actually a sum of **two** wave solutions, one that travels along the $+x$ axis as time progresses, and one that travels along the $-x$ axis as time progresses. Thus we may write $y(x, t)$ as a sum of the rightward-traveling solution $y_1(x, t)$ and the leftward-traveling solution $y_2(x, t)$:

{% math() %}
\begin{align*}
y(x, t) &= y_1(x, t) + y_2(x, t) \\
y_1(x, t) &= C_2 C_3 e^{i(kx - \omega t)} + C_1 C_4 e^{-i(kx - \omega t)} \\
y_2(x, t) &= C_1 C_3 e^{i(kx + \omega t)} + C_2 C_4 e^{-i(kx + \omega t)}
\end{align*}
{% end %}

We can write this in a neater form by defining {% inlmath() %}A \equiv C_2 C_3, B \equiv C_1C_4, C \equiv C_1 C_3, D \equiv C_2 C_4{% end %} and therefore we may write:

{% math() %}
\begin{align*}
y(x, t) &= y_1(x, t) + y_2(x, t) \\
y_1(x, t) &= Ae^{i(kx - \omega t)} + B e^{-i(kx - \omega t)} \\
y_2(x, t) &= C e^{i(kx + \omega t)} + D e^{-i(kx + \omega t)}
\end{align*}
{% end %}

 We call these solutions *wave solutions* (unsurprisingly) and all wave solutions have an associated **wavelength** $\lambda$ and **frequency** $f$ as well as amplitude(s) $A, B, C, D$. From these we can derived more quantities that explicitly appear in the solution: $k = 2\pi/\lambda$ is known as the **wavevector** and $\omega = 2\pi f$ is the **angular frequency** related through $\omega = k v$ (as we saw earlier in the solving process). Here, $v$ is the speed the wave propagates forward.

A pecular feature is that $y(x, t)$ is actually a _standing wave_, meaning that it does actually move, because $y_1, y_2$ move in opposite directions to each other, and thus their effects cancel out when they are added together. 

Now, let us turn our attention to a wave equation that can be considered the classical entryway into quantum theory. The **electromagnetic (EM) wave equation** is a special case of the wave equation given by:

{% math() %}
\dfrac{\partial^2 E}{\partial t^2} = c^2 \dfrac{\partial^2 E}{\partial x^2}
{% end %}

 where $c$ is the speed of light in vacuum and $E(x, t)$ is the magnitude of the **electric field**, whose oscillations produce electromagnetic waves, that is, light. The solutions to the EM wave equation are also a special case of the general solution we have just derived for the wave equation:

 {% math() %}
\begin{align*}
E(x, t) &= E_1(x, t) + E_2(x, t) \\
E_1(x, t) &= Ae^{i(kx - \omega t)} + B e^{-i(kx - \omega t)} \\
E_2(x, t) &= C e^{i(kx + \omega t)} + D e^{-i(kx + \omega t)}
\end{align*}
{% end %}

Where {% inlmath() %}A, B, C, D{% end %} are amplitudes derived from the boundary conditions of a specific problem. The solution characterizes all forms of light and radiation propagations, including all the light we see. The solution is uniquely characterized by two fundamental quantities, the speed of light $c$ and the wavelength of light $\lambda$, as well as its amplitudes (the electric field strength, in physical terms). All other quantities appearing in the solution can be derived from these two:

| Quantity | Expression in terms of $\lambda$ and $c$ |
|-----|------|
| $k$ | $\dfrac{2\pi}{\lambda}$ |
| $f$ | $\dfrac{c}{\lambda}$ |
| $\omega$ | $k c = 2\pi f = \dfrac{2\pi c}{\lambda}$ |

Wave solutions have some particular characteristics: they oscillate in time in predictable ways (which is why we can ascribe a frequency to them), and complete each spatial oscillation over a predictable distance (which is why we can ascribe a wavelength). Despite not being waves, quantum particles behave in ways strikingly similar to solutions of the wave equation, and _also_ have a frequency and wavelength as well as derived quantities such as $k$ and $\omega$. In addition, characterics of waves and how they interact with objects have a big part to play in quantum phenomena, as we will soon see. 

### The Schrödinger equation

In the quantum world, particles no longer follow the laws of classical physics. Instead, they follow the **Schrödinger wave equation**, a famous partial differential equation given by:

{% math() %}
i\hbar \frac{\partial}{\partial t} \Psi(x, t)  = \left(-\frac{\hbar^2}{2m} \frac{\partial^2}{\partial x^2} + V(x, t)\right) \Psi(x, t)
{% end %}

> This is the 1D Schrödinger equation, but we will look at the full 3D Schrödinger equation later.

Here, $\hbar$ is the **reduced Planck constant**, $m$ is the particle's mass, $V(x, t)$ is the particle's potential energy (which is often referred to simply as "the potential"), and the function to be solved for is $\Psi(x, t)$.

The solutions to the Schrödinger equation $\Psi(x, t)$ for given initial and boundary conditions are called **wavefunctions**. The Schrödinger equation tells us that when undisturbed, quantum particles are waves spread out in space, instead of possessing definite positions. We call these waves **matter waves**. A quantum particle (or system) can be analyzed by finding the particular solution of the Schrödinger equation for that particle (or system), although the actual solving process is rather tedious and more of a mathematical exercise than physics. Using **separation of variables** is a common method to solve the Schrödinger equation, and we will work through several examples. However, lots of solutions are very well-known and just looking them up in a textbook, reference book, or online is far faster than actually solving the equation.

As is suggestive of the name, wavefunctions describe the matter wave associated with a particular quantum particle (or system of quantum particles). Just like classical waves, all quantum particles have a wavelength $\lambda$ which is related to the momentum by $\lambda = \dfrac{h}{p}$ and the energy by $\lambda = \dfrac{hc}{E}$. Here, $h = \pu{6.62607E-34 J\cdot s}$ is the **Planck constant**, a fundamental constant of nature, alongside the **reduced Planck constant** $\hbar \equiv \dfrac{h}{2\pi} = \pu{1.05457E-34 J\cdot s}$.

> The equations $\lambda = \dfrac{h}{p}$ and the energy $\lambda = \dfrac{hc}{E}$ can be rewritten as $p = \hbar k$ (the **de Broglie relation**) and $E = \hbar \omega$ (the **Planck-Einstein relation**).

As a bizarre consequence of the Schrödinger equation, wavefunctions - that is, the matter waves - are **complex-valued**. That is to say, matter waves are not physical quantities that are observable in the real world. Furthermore, matter waves are not simply _one wave_, but actually contain all possible *states* that a quantum particle can be in, where each state is a unique wave solution to the Schrödinger equation. At a given moment, a quantum particle's actual state can be _any_ of the states contained in the wavefunction, but _which one_ is impossible to predict in advance.

Thus, rather than physical individual waves in space, wavefunctions are more of a mathematical description of _many_ possible quantum waves of a particle that is non-localized and cannot be predicted exactly. For instance, an electron can be in its _ground state_ (lowest-energy state). But it can also be in a number of other *excited* states (energetic states). Within each state, the particle has specific energies and momenta and has different probabilities to be located at a particular point in space. In fact, squaring the wavefunction and taking its absolute value, which we write as $\rho(x) = |\Psi|^2$, gives the **probability density**, indicating how likely it is to find a quantum particle at a specific point $x$ in space - although theoretically the particle can be almost anywhere. For instance, the following plot showcases the probability density for three wavefunctions:

![A graph of several wavefunctions, which describe how likely a particle is to be at a particular location](https://cdn.kastatic.org/ka-perseus-images/a5e18b829f12622a749e2f131bd029f8783eaf92.jpg)

_Source: [Khan Academy](https://www.khanacademy.org/science/chemistry/atomic-structure-and-properties/orbitals-and-electrons/a/the-quantum-mechanical-model-of-the-atom)_

When we consider quantum problems in 3 dimensions, the associated probability density takes the form $\rho(x, y, z) = |\Psi(x, y, z)|^2$. 3D slices of the probability density for several solutions of the Schrödinger equation are shown below:

![Plots of wavefunctions of the hydrogen atom](https://chem.libretexts.org/@api/deki/files/41592/e74241a7f09f0952511cff1994da750c.jpg?revision=1&size=bestfit&width=749&height=522)

_Source: [LibreTexts](https://chem.libretexts.org/Bookshelves/General_Chemistry/Map%3A_Chemistry_-_The_Central_Science_%28Brown_et_al.%29/06%3A_Electronic_Structure_of_Atoms/6.06%3A_3D_Representation_of_Orbitals)_

To re-emphasize, since quantum particles are described as complex-valued matter waves, they aren't truly point particles, but spread throughout space - hence _wave_ equation, because these solutions carry a wavelike nature. Since these solutions display cyclical (symmetric in space) and oscillatory (repeating in time) behavior, meaning that just like classical waves, we describe them in terms of wave quantities like the wavelength $\lambda$, angular frequency $\omega$, wave propagation speed $v$, and wavevector $k$. However, when we measure a quantum particle, we find that it then behaves particle-like and _occupies_ a particular position. The likelihood of a particle being at a particular position can be calculated from the probability density $\rho = |\Psi|^2$, and we can find which positions the particle is more (or less) likely to be located. But the *precise* position cannot be predicted in advance.

> **Definition:** A **quantum state** $\psi(x)$ is a solution to the Schrödinger equation for a given time $t$ whose physical interpretation is the matter wave of a quantum particle (or system). Taking the squared amplitude $|\psi(x)|^2$ of the quantum state gives a **unique probability distribution function** describing a quantum particle (or system).

### Addenum: the time-independent Schrödinger equation

It is often convenient to write out a wavefunction in terms of separate time-dependent and time-independent components. We denote the full wavefunction as $\Psi(x, t)$, and the time-independent part as $\psi(x)$, where $\Psi(x, t) = \psi(x) e^{-i E/\hbar}$ for some value of the energy $E$. 

This is not simply a matter of convention. The underlying reason is that by the separation of variables technique, the Schrödinger equation can be rewritten as _two_ differential equations in the form:

{% math() %}
\begin{align*}
i\hbar \dfrac{d}{d t} \phi(t) &= E \phi(t) \\
-\dfrac{\hbar^2}{2m} \dfrac{\partial^2 \psi}{\partial x^2} + V(x) \psi &= E \psi(x)
\end{align*}
{% end %}

Where we refer to the bottom differential equation as the _time-independent_ Schrödinger equation, and $\Psi(x, t) = \psi(x) \phi(t)$. Thus we say that $\psi(x)$ is a solution of the _time-independent_ Schrödinger equation and represents the time-independent component of the wavefunction.

> When applying the Schrödinger equation, it is convention (though not a rule) that a lowercase $\psi$ for $\psi(x)$ is used for the spatial component of the wavefunction that is the solution to the time-independent Schrödinger equation, and an uppercase $\Psi$ for $\Psi(x, t) = \psi(x) \phi(t)$ is used for the complete wavefunction in both time and space. This also means that $\psi(x) = \Psi(x, 0)$. 

## Solutions as eigenstates

The solutions to the Schrödinger equation have an important characteristic: they are _linear_ in nature. This means that we can write the general solution in terms of a **superposition** of solutions, each of which is a possible state for a quantum particle (or particles) - see the [differential equation series](@/differential-equations/index.md) for why this works. Taking $\varphi_1, \varphi_2, \varphi_3, \dots$ to be the individual solutions with energies $E_1, E_2, E_3, \dots$, the general time-independent solution would be given by:

{% math() %}
\begin{align*}
\psi(x) &= \sum_n C_n \varphi_n(x)  \\ &= C_1 \varphi_1(x) + C_2 \varphi_2(x) + \dots + C_n \varphi_n(x) 
\end{align*}
{% end %}

And therefore the general (time-dependent) wavefunction $\Psi(x, t)$ would be given by:

{% math() %}
\begin{align*}
\Psi(x, t) &= \sum_n C_n \varphi_n(x) e^{-iE_n t/\hbar} \\ &= C_1 \varphi_1(x)e^{-iE_1t/\hbar} + C_2 \varphi_2(x)e^{-iE_2t/\hbar} + \dots + C_n \varphi_n(x) e^{-iE_nt/\hbar}
\end{align*}
{% end %}

Each individual solution $\varphi_n(x)$ is called an **eigenstate**, a possible state that a quantum particle can take. Eigenstate is just another word for *eigenfunction*, which we've already seen. This is because we note that each eigenstate individually satisfies the Schrödinger equation, which can be recast into the form of an eigenvalue equation:

{% math() %}
\left(-\frac{\hbar^2}{2m} \frac{\partial^2}{\partial x^2} + V(x, t)\right) \varphi_n(x) = E_n \varphi_n(x)
{% end %}

> **Note for the advanced reader:** This is because mathematically speaking, the separation of variables results in a separation constant $E_n$ which results in an eigenvalue problem. We'll later see that $E_n$ acquires a physical interpretation as the energy.

As a demonstration of this principle, the solution to the Schrödinger equation for a particle confined in a region $0 < x < L$ is a series of eigenstates given by:

{% math() %}
\varphi_n(x) = \sqrt{\dfrac{2}{L}} \sin \dfrac{n \pi x}{L},\quad E_n = \dfrac{n^2 \hbar^2 \pi^2}{2mL^2}
{% end %}

> $n$ is often called the **principal quantum number**, it is a good idea to keep this in mind.

Below is a plot of several of these eigenstates:

![A plot of several overlapped eigenstates of the quantum particle confined to a small region of space](https://www.researchgate.net/profile/Susana-Valdez-3/publication/260767966/figure/fig2/AS:669067904036876@1536529627958/Exact-solution-for-the-particle-in-a-one-dimensional-box-Left-Real-part-of-the-wave.ppm)

_Source: [ResearchGate](https://www.researchgate.net/figure/Exact-solution-for-the-particle-in-a-one-dimensional-box-Left-Real-part-of-the-wave_fig2_260767966)_

The general wavefunction of the particle would be given by the superposition:

{% math() %}
\Psi(x, t) = \varphi_1 + \varphi_2 + \dots = \small \sqrt{\dfrac{2}{L}} \normalsize \sum_n C_n \sin \dfrac{n \pi x}{L} e^{-iE_nt / \hbar}
{% end %}

Since the general wavefunction $\Psi(x, t)$ is a superposition of eigenstates, _each eigenstate_ represents one state - and thus **probability distribution** - that a quantum particle can be in. A particle may be more or less likely to take a particular state. Typically, eigenstates are associated with energy, so a particle could have a number of different possible states, from a lowest-energy state to a highest-energy state and everything in between.

However, the actual state the particle takes **cannot be predicted** (as with many things in quantum mechanics). Only the probabilities of a quantum particle being in a particular state are predictable. As an oversimplified example, while an electron could theoretically be in an eigenstate where it has the same amount of energy as a star, the probability of that state is very, very low. Instead, we typically observe electrons with more "normal" energies, as electrons have a much higher probability of being in lower-energy eigenstates.

To quantify this statement in mathematical terms, the _coefficients_ $C_n$ for each eigenstate are directly related to the probability of each eigenstate. In fact, the probability of each eigenstate is given by $P_n = |C_n|^2$. And we may calculate $C_n$ for a particular eigenstate $\varphi_n$ given the initial condition $\Psi(x, 0)$ with:

{% math() %}
C_n = \int_{-\infty}^\infty \bar \varphi_n(x) \Psi(x, 0)\, dx
{% end %}

> The coefficients $C_n$ are referred to by different names; we may call them _probability coefficients_, _probability amplitudes_, or simply _coefficients_. Whichever name is used, it represents the same thing, where $P_n = |C_n|^2$ is the probability of measuring a given eigenstate.

## Quantum operators

We have seen that we can solve for wavefunctions, which are the probability distributions of a quantum particle in space, by solving the Schrödinger equation. But we also want to calculate other physically-relevant quantities. How do we do so? Quantum theory uses the concept of **operators** to describe physical quantities. An operator is something that is _applied_ to a function to get another function. A table of the most important operators is shown below:

| Name | Mathematical form|
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| Position operator| $\hat X = x$ (multiplication by x) |
| Momentum operator| $\hat p = -i\hbar \dfrac{\partial}{\partial x}$ (1D), $\hat p = -i\hbar \nabla$ (general) |
| Angular momentum operator| General $\hat L = \mathbf{r} \times \hat p = \mathbf{r} \times -i\hbar\nabla$, z-component $\hat L_z = -i\hbar \dfrac{\partial}{\partial \phi}$ where $\phi$ is the azimuthal angle $\phi$ in spherical coordinates |
| Kinetic energy operator| $K = -\dfrac{\hbar^2}{2m} \nabla^2$ |
| Potential (energy) operator| $\hat V = V$ (multiplication by the potential $V(x)$) |
| Total energy operator (time-independent) | $\hat H$ often called the **Hamiltonian**, the precise formulation may vary but the most common non-relativistic one is $\hat H = -\dfrac{\hbar^2}{2m} \nabla^2 + \hat V$ |
| Total energy operator (time-dependent) | $\hat E = -i\hbar \dfrac{\partial}{\partial t}$ |

> Note that $\hat H$, the energy operator, is named so due to its correspondence with the [Hamiltonian](https://en.wikipedia.org/wiki/Hamiltonian_mechanics) in classical mechanics

There is a very important _physical_ interpretation of a quantum operator: the **eigenvalues** of each eigenstate of a given quantum operator acting on a state gives the specific _values_ of measurable values. For instance, the energy of one particular state is the eigenvalue of the Hamiltonian operator, and the momentum of one particular state is the eigenvalue of the momentum operator, and so forth.

To find the eigenstates and eigenvalues of physical properties of a quantum particle, we apply each operator to the wavefunction, which results in an eigenvalue equation that we can solve for the eigenvalues. For example, for finding the momentum eigenstates, we can apply $\hat p$ the momentum operator:

{% math() %}
\hat p \varphi = -i\hbar \dfrac{\partial}{\partial x} \varphi(x)
{% end %}

Now, writing $p$ as the eigenvalues of momentum in terms of an eigenvalue equation, we have:

{% math() %}
-i\hbar \dfrac{\partial}{\partial x} \varphi(x) = p\varphi(x)
{% end %}

This is a differential equation that we can in fact solve for $\varphi(x)$ to obtain the solution:

{% math() %}
\varphi(x) = e^{ip x / \hbar}
{% end %}

We have now found a _momentum eigenstate_ which has a momentum $p$. More generally, by the principle of superposition we saw earlier, this would correspond to a wavefunction given by:

{% math() %}
\psi(x) = C_1 e^{ip_1 x / \hbar} + C_2 e^{ip_2 x / \hbar} + \dots + C_n e^{ip_n x / \hbar}
{% end %}

> Remember that $\psi$ is just the time-independent part of the full wavefunction $\Psi$, which is given by $\Psi(x, t) = \psi(x, t) e^{-iE t/ \hbar}$

The fact that operators represent physical properties is very powerful. For instance, by identification of $\hat H = -\dfrac{\hbar^2}{2m} \dfrac{\partial^2}{\partial x^2} + V$ as the left-hand side of the time-independent Schrödinger equation, we have:

{% math() %}
\hat H \psi = E\psi
{% end %}

And we can similarly write the full (time-dependent) Schrödinger equation as:

{% math() %}
i\hbar \dfrac{\partial}{\partial t} = \hat H \psi
{% end %}

That is to say, the Schrödinger equation is the **eigenvalue equation for the energy operator**. This is an incredibly significant statement that we will use extensively going forwards.

### Continuous and discrete eigenvalues

So far, we have restricted a lot of our analysis to purely discrete eigenvalues. Let us explore a bit more in this direction, then change course to continuous eigenvalues.

When a system possesses discrete eigenstates (and this is more easily seen with the fact that eigenstates are notated $\varphi_n(x)$) the system is also **bounded**, meaning that there are (infinite or finite) barriers that confine a particle. The specific feature is that these eigenstates are parametrized by an integer value, so they can be denoted $\varphi_1, \varphi_2, \dots, \varphi_n$. Then the general form of the time-independent wavefunction is given by:

{% math() %}
\psi(x) = \sum_n C_n \varphi_n(x)
{% end %}

One perhaps unexpected result is that since an infinitely many number of eigenstates is in theory possible, a particle's _wavefunction_ at a specific instant $t$ may not itself be an eigenstate - however, it can always be decomposed into a linear superposition of eigenstates. If having knowledge of Fourier series or reading the [differential equation series](@/differential-equations/index.md), this may sound familiar. 

For instance, consider the wavefunction $\psi(x) = \Psi(x, 0) = A\left(x^{3}-x\right)$ for $-1 \leq x \leq 1$. This is not an eigenstate, but we may write it in series form, whose individual terms _are_ eigenstates, and from which we can find the ground state and the other eigenstates:

{% math() %}
\psi(x) = -\dfrac{16A}{\pi^4} (\pi^2 - 12) e^{i(\pi x/ 2 + \pi/2)} - \dfrac{16A}{81\pi^4}(9\pi^2-12) e^{3i(\pi x/ 2 + \pi/2)} + \dots
{% end %}

In the continuous case, which is the case for position and momentum eigenstates, we have an eigenstate for every possible value of the physical quantity, instead of just integers. The position and momentum are examples where we observe continuous eigenstates; they can take a continuous spectrum of values _including_ non-integer values. In addition, instead of discrete probability coefficients $C_n$ whose squares give the probability, we now have a continuous **probability coefficient function** $C(\lambda)$, where $\lambda$ is a continuous eigenvalue, such as $C(x)$ or $C(p)$ for position and momentum respectively. Therefore, we now have an integral for writing down the general wavefunction in terms of the continuous eigenstates; for momentum eigenstates, we have:

{% math() %}
\psi(x) = \int_{-\infty}^\infty C(k) e^{i k x} dk = \int_{-\infty}^\infty C(p) e^{i p x/\hbar} dp
{% end %}

#### Addenum: position eigenstates

Position eigenstates are similar in nature to momentum eigenstates, but they are not discussed as often because position eigenstates run into some complicated technicalities. First, by solving for $\hat x \psi = x \psi$, we can find that the eigenstates are given by $\varphi(x) = \delta(x - x')$ where $\delta$ is the Dirac delta function, which is zero everywhere except for a point $x'$ where the function has a spike. Then the general wavefunction is given by:

{% math() %}
\psi(x) = \int_{-\infty}^\infty C(x)\delta(x - x')\, dx
{% end %}

But the Dirac delta function obeys the identity:

{% math() %}
\int_{-\infty}^\infty f(x)\delta(x - x') dx = f(x)
{% end %}

Which means that:

{% math() %}
\psi(x) = \int_{-\infty}^\infty C(x)\delta(x - x')\, dx = C(x)
{% end %}

We now see that $\psi(x) = C(x)$ - that is to say, the spectrum of probability coefficients for continuous position eigenstates _are_ the wavefunction. This somewhat perplexing result means that there are _infinitely-many position eigenstates_ $\varphi(x) = \delta(x - x')$, one at every point in space, and the wavefunction is just the collection of probability coefficients of all of those eigenstates. 

If this is all too abstract, that is completely understandable. We will re-examine the idea of the wavefunction being a probability coefficient function of eigenstates later, when we discuss the Dirac formulation of quantum mechanics.

### Expectation values

We have seen that operators represent physical properties (such as position or momentum), that eigenstates are solutions to eigenvalue equations, and that eigenvalues are the possible measurable values of the physical property. We have also seen that a superposition of eigenstates of an operator can be used to write out the wavefunction, and that the probability coefficients $C_n$ in the superposition are related to the probability $|P_n|$ associated with each state. 

Recall that the actual properties of a quantum particle are unknown and random, and the best we can do is to predict probabilities. However, just as we can predict the probabilities of the particle being in a particular state through the probability coefficients of each eigenstate, we can predict the _average_ measured value. We call this the **expectation value**.

In the discrete case, for a given operator $\hat A$ with eigenstates $\varphi_n(x)$, the expectation value is notated $\langle \hat A\rangle$ and is given by:

{% math() %}
\langle \hat A\rangle = \sum_n |C_n|^2 A_n
{% end %}

Meanwhile, in the continuous case, for a given operator $\hat A$, the expectation value is given by:

{% math() %}
\langle \hat A\rangle = \int_{-\infty}^\infty \bar \Psi(x, t) \hat A \Psi(x, t)\, dx
{% end %}

In the cases of the position and momentum operators $\hat x = x$ and $\hat p = -i\hbar \dfrac{\partial}{\partial x}$, by substituting into the above formula, the expectation values are given by:

{% math() %}
\begin{align*}
\langle x \rangle &= \int_{-\infty}^\infty \bar \Psi(x, t) x\, \Psi(x, t) dx \\
\langle p \rangle &= \int_{-\infty}^\infty \bar \Psi(x, t) \left(-i\hbar \dfrac{\partial}{\partial x} \Psi(x, t)\right) dx
\end{align*}
{% end %}

It may seem strange at first glance that expectation values are not time-dependent (i.e. that we don't also have to integrate with respect to time). The reason, however, is that when a wavefunction and its conjugate are multiplied, the time-components of the wavefunction combine to form $e^{i E t / \hbar}e^{-i E t / \hbar} = 1$.

We may also take the expectation value of a given operator applied twice, which we denote $\langle \hat A^2\rangle$, where $\hat A^2 \varphi = \hat A(\hat A \varphi)$. This notation means that in the discrete case, we have:

{% math() %}
\langle \hat A^2\rangle = \sum_n |C_n|^2 A_n {}^2
{% end %}

And in the continuous case we have:

{% math() %}
\langle \hat A^2\rangle = \int_{-\infty}^\infty \bar \Psi(x, t) \hat A^2 \Psi(x, t)\, dx
{% end %}

Calculating the expectation values further leads to an incredibly important result. From statistical theory, the **uncertainty** (standard deviation) $\Delta X$ of a given variable $X$ is given by $\Delta X = \sqrt{\langle X^2 \rangle - \langle X \rangle^2}$. This means that in quantum mechanics, for a given physical quantity $A$ which has a corresponding operator $\hat A$, then the uncertainty in measuring $A$ is given by:

{% math() %}
\Delta A = \sqrt{\langle \hat A^2 \rangle - \langle \hat A \rangle^2}
{% end %}

In the case of the momentum $p$ and position $x$, we obtain the famous result of the **Heisenberg uncertainty principle**:

{% math() %}
\Delta x \Delta p \geq \dfrac{\hbar}{2}
{% end %}

The standard deviations $\Delta x$ and $\Delta p$ can be thought of the "spread of measurements", so the Heisenberg uncertainty principle says that the momentum and position eigenvalues cannot both be predicted with certainty. What does this mean in practice? Suppose we had an detector that was purpose-built to measure the momentum and position of a quantum particle. Like any scientific instrument, it has a certain measurement uncertainty, which we will call $\epsilon$. We turn it on, make a position measurement, and then we get a number - perhaps it measures a position of 1.4 nanometers from the measurement device. However, it probably is not _exactly_ at 1.4 nm; since the detector itself has a certain measurement uncertainty, the actual measurement is $\pu{1.4 nm} \pm \epsilon$. We also simultaneously measure the momentum of the particle, and we get another number - perhaps {% inlmath() %}\pu{5.5e-31 kg*ms^{-1}}{% end %}. Conventional wisdom would suggest that the momentum measurement should be {% inlmath() %}\pu{5.5e-31 kg*ms^{-1}} \pm \epsilon{% end %}, just like the position measurement. But the Heisenberg uncertainty principle says that $\Delta x \Delta p \geq \frac{\hbar}{2}$. This means that:

 {% math() %}
 \Delta p \geq \frac{\hbar}{2 \Delta x} \Rightarrow \Delta p \geq \frac{\hbar}{2 \epsilon}
 {% end %}

 So even if the detector's measurement uncertainty $\epsilon$ is made arbitrarily small, the _most accurate_ measurement you can get of the momentum while simultaneously measuring the position is {% inlmath() %}\pu{5.5 kg*ms^{-1}} \pm \hbar/2\epsilon{% end %}. This means that in practice, only one property of a quantum particle can usually be measured to full precision at a time.

### A recap

So, to sum up, the fundamental procedure in introductory quantum mechanics is as follows:

- Solve the Schrödinger equation with the appropriate initial and boundary conditions to determine the solutions, which are eigenstates 
- For each of the eigenstates, find the probability density function with $\rho(x, t) = |\Psi(x, t)|^2 = \Psi(x, t) \bar \Psi(x, t)$, which yields the probability distribution of the particle in space
- Apply all the operators (Hamiltonian, momentum, angular momentum, etc.) to analyze the different properties of the quantum system being studied. The eigenvalues of each operator are the measurable values of the physical quantity (e.g. energy, momentum, etc.)
- Compute the expectation (average) values of each operator, as well as the uncertainties through $\Delta A = \sqrt{\langle \hat A^2\rangle - \langle \hat A\rangle^2}$
- You may also calculate the probabilities of each eigenstate (and of their associated energy, momentum, and other properties) through $P_n = |C_n|^2$ where $C_n$ is the _probability coefficient_ of the eigenstate in the superposition. This becomes a _probability coefficient function_ $C(\lambda)$ for the continuous spectrum case, which includes $C(x)$ for position and $C(p)$ for momentum.

### A brief interlude on spin

For all its predictive power, the simplest form of the Schrödinger equation does not explain one quantum phenomenon: **spin**. Spin is the property that allows quantum particles like electrons to act as tiny magnets and generate magnetic fields. The name is technically a misnomer: in classical mechanics, a spinning charge would create a magnetic field, but subatomic particles don't actually spin, they just behave *as if they did*.

To make this idea more concrete, consider an electron placed in a magnetic field $\mathbf{B}$. It would then experience a torque given by $\vec \tau = \vec \mu \times \mathbf{B}$, where $\vec \mu$ is the magnetic moment given by:

{% math() %}
\vec \mu = -\dfrac{g_e e}{2m} \mathbf{S}
{% end %}

Where $e$ is the electron charge (also called the _elementary charge_), $m$ is the electron mass, $g_e \approx 2.00232$ is the **electron _g-factor_**, and $\|S\| = \hbar \sqrt{s(s + 1)}$ is the spin angular momentum vector. Here, $s = \pm \frac{1}{2}$ is called the _spin quantum number_, which we often shorten to _spin_. Spin explains how some materials are able to act as permanent magnets: the torque caused by their magnetic moments aligns them in the same direction. In this way, they behave just like little (classical) magnets, except their magnetic moments are a consequence of their spin. The alignment of spins amplifies the tiny magnetic fields of each electron strongly enough that we can observe their combined effect as a _macroscopic_ magnetic field.

Spin modifies a quantum state because a quantum state must _additionally_ include information about a quantum particle's spin. For electrons, all spins must either be $+\frac{1}{2}$ (spin-up) or $-\frac{1}{2}$ (spin-down); these are the _only_ two possible spins.


We formulate spin mathematically as an operator, just like energy and momentum. However, unlike the differential operators we've seen, the spin operators $\hat S_x, \hat S_y, \hat S_z$ (there is one for each direction $x, y, z$) are matrices. In the case of elementary fermions (quarks, electrons, and neutrinos) which have spin-1/2 these are specifically expressed as:

{% math() %}
\begin{align*}
\hat \sigma _{x} &=\dfrac{\hbar}{2}{\begin{pmatrix}0 & 1\\1 & 0\end{pmatrix}}\\
\hat \sigma_{y} & =\dfrac{\hbar}{2}{\begin{pmatrix}0 & -i\\i & 0\end{pmatrix}}\\
\hat \sigma_{z} & =\dfrac{\hbar}{2}{\begin{pmatrix}1 & 0\\0 & -1\end{pmatrix}}\\
\end{align*}
{% end %}

The inclusion of spin means that even electrons with otherwise identical eigenstates are not the same; their wavefunctions must also include whether they are spin-up or spin-down. While the Schrödinger equation does not include spin, more advanced formulations of the Schrödinger equation **do include** the effects of spin, and are essential for very accurate calculations. We will return to spin later at the end.

## Solving quantum systems

We will now apply quantum mechanics to solve a variety of quantum systems, to get a feel for how exactly you _do_ quantum mechanics. Note that there are only a few exact solutions to quantum problems, and approximate methods are required for the vast majority of quantum systems, so these should be (with some exceptions) considered _idealized_ systems.

### The free particle

The free particle is among the simplest quantum systems that have an exact solution to the Schrödinger equation. It describes a quantum particle in free space is unconstrained by any potential, and thus has zero potential energy. We start from the one-dimensional Schrödinger equation for $V(x) = 0$, for which we may solve for the wavefunction:

{% math() %}
\begin{align*}
-\dfrac{\hbar^2}{2m} \dfrac{\partial^2 \Psi(x, t)}{\partial x^2} + \cancel{V(x)} &= i \hbar \dfrac{\partial \Psi(x, t)}{\partial t} \Rightarrow \\
-\dfrac{\hbar^2}{2m} \dfrac{\partial^2 \Psi(x, t)}{\partial x^2} &= i \hbar \dfrac{\partial \Psi(x, t)}{\partial t}
\end{align*}
{% end %}

If we assume a solution in the form $\Psi(x) = \psi(x) f(t)$, we may substitute to find that:

{% math() %}
\begin{align*}
\dfrac{\partial^2 \Psi(x, t)}{\partial x^2} &= f(t)\dfrac{d^2 \psi}{dx^2} \\
\dfrac{\partial \Psi(x, t)}{\partial t} &= \psi(x) \dfrac{df}{dt}
\end{align*}
{% end %}

> These are ordinary derivatives because $\psi(x)$ and $f(t)$ are functions of only one variable.

Thus if we substitute these derivatives back into the Schrödinger equation we get:

{% math() %}
-\dfrac{\hbar^2}{2m} f(t)\dfrac{d^2 \psi}{dx^2} = i \hbar \psi(x) \dfrac{df}{dt}
{% end %}

Now dividing both sides by $\psi(x)f(t)$ we have:

{% math() %}
\begin{align*}
-\dfrac{1}{\psi(x) f(t)}\dfrac{\hbar^2}{2m} f(t)\dfrac{d^2 \psi}{dx^2} = \dfrac{1}{\psi(x) f(t)} i \hbar \psi(x) \dfrac{df}{dt} \\
-\dfrac{\hbar^2}{2m} \dfrac{1}{\psi(x)}\dfrac{d^2 \psi}{dx^2} = i \hbar\dfrac{1}{f(t)} \dfrac{df}{dt} = \text{const.}
\end{align*}
{% end %}

If we call the separation constant $E$, we have:

{% math() %}
\begin{align*}
-\dfrac{\hbar^2}{2m} \dfrac{1}{\psi(x)}\dfrac{d^2 \psi}{dx^2} = i \hbar\dfrac{1}{f(t)} \dfrac{df}{dt} = E \Rightarrow \\
-\dfrac{\hbar^2}{2m} \dfrac{1}{\psi(x)}\dfrac{d^2 \psi}{dx^2} = E \\
i \hbar\dfrac{1}{f(t)} \dfrac{df}{dt} = E
\end{align*}
{% end %}

The two ODEs can be rewritten in a more easily-read form as:

{% math() %}
\begin{align*}
-\dfrac{\hbar^2}{2m} \dfrac{d^2 \psi}{dx^2} = E\psi(x) \\
i \hbar\dfrac{df}{dt} = Ef(t)
\end{align*}
{% end %}

> The top differential equation is the **time-independent Schrödinger equation** we saw before, just with $V(x) = 0$.

We can use the traditional methods of solving first- and second-order differential equations (or just make an educated guess, that's called an _ansatz_) to find the solutions are:

{% math() %}
\begin{align*}
\psi(x) &= e^{i k x}, \quad k \equiv \dfrac{\sqrt{2mE}}{\hbar} \\
f(t) &= e^{-i \omega t}, \quad \omega \equiv \dfrac{E}{\hbar} \\
\Psi(x, t) &= \psi(x) f(t) = e^{ikx} e^{-i\omega t} \\ &= e^{ik x - i\omega t}
\end{align*}
{% end %}

> We call this solution a **plane-wave** solution.

We now encounter an issue: the plane-wave solution $\Psi(x, t) = e^{i(kx -\omega t)}$ is non-normalizable; if we try to perform the normalization integral, we'll find that its total probability is infinite and thus is unphysical. However, if we create a superposition of plane waves by adding them together (which, again, are still solutions to the Schrödinger equation because it is a linear combination), we _do_ get a physical solution, which we call a **wave packet**:

![A wave packet, created by summing many plane waves](https://phys.libretexts.org/@api/deki/files/38619/Screen_Shot_2022-01-27_at_2.45.04_PM.png?revision=1&size=bestfit&width=670&height=240)

<em>Source: <a href="https://phys.libretexts.org/Bookshelves/Classical_Mechanics/Essential_Graduate_Physics_-_Classical_Mechanics_(Likharev)/06%3A_From_Oscillations_to_Waves/6.03%3A_1D_Waves">LibreTexts</a></em>

We can create this superposition by adding plane waves of different wavevectors $k$ and frequencies $\omega$, which are related by $\omega = k v_g$ where $v_g$ is the _group velocity_, meaning the velocity at which the wave packet moves over time. This becomes an integral as the number of summed waves approaches infinity:

{% math() %}
\Psi(x, t) = \dfrac{1}{\sqrt{2\pi}} \int_{-\infty}^\infty A(k) e^{i(kx - \omega t)}\, dk
{% end %}

Where $A(k)$ is a function that gives the wavevector $k$ for each summed wave. A common choice of $A(k)$ is the Gaussian, given by:

{% math() %}
A(k) = \sqrt{\sigma}\left(\dfrac{2}{\pi}\right)^{1/4} e^{-\sigma^2 (k - k_0)^2}
{% end %}

And therefore the wavefunction $\Psi(x, t)$ is given by:

{% math() %}
\Psi(x, t) =\left( \dfrac{1}{2 \pi} \right)^{1 / 4} \dfrac{1}{\sqrt{\sigma}} e^{i k_0 x -
\frac{x^2}{4 \sigma^2}} e^{-i \omega t}
{% end %}

We may calculate the expectation values - that is, the average values - of the free particle's position and momentum. Let us begin with that of position. We have:

{% math() %}
\begin{align*}
\langle x \rangle &= \int_{-\infty}^\infty \Psi^*(x, t) \hat x \Psi(x, t)\,dx \\
&= \int_{-\infty}^\infty \Psi^*(x, t) x \Psi(x, t)\,dx \\
&= \left[\left( \dfrac{1}{2 \pi} \right)^{1 / 4} \dfrac{1}{\sqrt{\sigma}}\right]^2 \int_{-\infty}^\infty (e^{-ik_0 x}e^{-\frac{x^2}{4\sigma^2}} e^{i\omega t}) x (e^{ik_0 x}e^{-\frac{x^2}{4\sigma^2}} e^{-i\omega t})\, dx \\
&= \dfrac{1}{\sqrt{2\pi}} \dfrac{1}{\sigma} \int_{-\infty}^\infty e^{-\frac{x^2}{4\sigma^2}} x e^{-\frac{x^2}{4\sigma^2}}\, dx \\
&= \dfrac{1}{\sigma \sqrt{2\pi}} \int_{-\infty}^\infty xe^{-\frac{x^2}{2\sigma^2}}\, dx
\end{align*}
{% end %}

> The squared quantity in brackets $\left( \dfrac{1}{2 \pi} \right)^{1 / 4} \dfrac{1}{\sqrt{\sigma}}$ that is factored out of the integral is the amplitude from the wavefunction. It is squared because $\psi$ and $\psi^*$ both have this amplitude, and therefore multiplying them together gives a squared amplitude. 

However, $xe^{-\frac{x^2}{2\sigma^2}}$ is an _odd_ function. An odd function has $f(-x) = -f(x)$, that is, it flips as you go from $-x$ to $x$, and odd functions satisfy the identity:

{% math() %}
\int_{-\infty}^\infty f(x)\, dx = 0
{% end %}

> This is because odd functions have a positive area for $x > 0$ and a negative area for $x < 0$ that, once added together, cancel each other out.

Therefore we have:

{% math() %}
\langle x \rangle = \dfrac{1}{\sigma \sqrt{2\pi}} \int_{-\infty}^\infty xe^{-\frac{x^2}{2\sigma^2}}\, dx = 0
{% end %}

This means that the particle is most likely to be found at $x = 0$ - which makes sense given that the peak of its wavefunction is located at $x = 0$.

We may also find the expectation value of the momentum. For this, we recall that the momentum expectation value is found by the following equation:

{% math() %}
\begin{align*}
\langle p\rangle &= \int_{-\infty}^\infty \psi^*(x) \hat p \psi(x)\, dx \\
&= \int_{-\infty}^\infty \psi^*(x) \dfrac{\hbar}{i} \dfrac{\partial}{\partial x} \psi(x)\, dx \\
\end{align*}
{% end %}

> Note the identity $-i\hbar = \dfrac{\hbar}{i}$. This is why the momentum operator $\hat p$ is sometimes written $\dfrac{\hbar}{i} \dfrac{\partial}{\partial x}$ and sometimes written $-i\hbar \dfrac{\partial}{\partial x}$. They are **completely equivalent**.

We may find $\hat p \psi$ as follows:

{% math() %}
\begin{align*}
\hat p \psi &= \dfrac{\hbar}{i} \dfrac{\partial}{\partial x} \\
&= \dfrac{\hbar}{i}\dfrac{\partial}{\partial x}\left[\left( \dfrac{1}{2 \pi} \right)^{1 / 4} \dfrac{1}{\sqrt{\sigma}} e^{i k_0 x -
\frac{x^2}{4 \sigma^2}} e^{-i \omega t}\right] \\
&= \dfrac{\hbar}{i} \left( \dfrac{1}{2 \pi} \right)^{1 / 4} \dfrac{1}{\sqrt{\sigma}} e^{-i\omega t} \left[\dfrac{\partial}{\partial x} 
\left(e^{i k_0 x - \frac{x^2}{4 \sigma^2}}\right)\right] \\
&= \dfrac{\hbar}{i} \left( \dfrac{1}{2 \pi} \right)^{1 / 4} \dfrac{1}{\sqrt{\sigma}} e^{-i\omega t} \left[ 
\left(ik_0 - \dfrac{x}{2\sigma^2}\right)e^{i k_0 x - \frac{x^2}{4 \sigma^2}}\right] \\
\end{align*}
{% end %}

Substituting this expression into the equation for $\langle p\rangle$ we have:

{% math() %}
\begin{align*}
\langle p\rangle &= \int_{-\infty}^\infty \psi^*(x) \dfrac{\hbar}{i} \dfrac{\partial}{\partial x} \psi(x)\, dx \\
&= \left[\frac{\hbar}{i} \left[\left( \frac{1}{2 \pi} \right)^{1 / 4} \frac{1}{\sqrt{\sigma}}\right]^2 \cancel{e^{i\omega t}e^{-i\omega t}}^{{}^1} \right]\int_{-\infty}^\infty e^{-i k_0 x - \frac{x^2}{4 \sigma^2}}
\left(ik_0 - \frac{x}{2\sigma^2}\right)e^{i k_0 x - \frac{x^2}{4 \sigma^2}}\,dx \\
&= \frac{\hbar}{i} \left[\left( \frac{1}{2 \pi} \right)^{1 / 4} \frac{1}{\sqrt{\sigma}}\right]^2
\int_{-\infty}^\infty \cancel{e^{i k_0 x} e^{-ik_0x}}^{{}^1} \left(ik_0 - \frac{x}{2\sigma^2}\right) e^{-\frac{x^2}{4 \sigma^2}}e^{-\frac{x^2}{4 \sigma^2}}\,dx \\
&= \frac{\hbar}{i} \left[\left( \frac{1}{2 \pi} \right)^{1 / 4} \frac{1}{\sqrt{\sigma}}\right]^2
\int_{-\infty}^\infty \left(ik_0 - \frac{x}{2\sigma^2}\right) e^{-\frac{2x^2}{4 \sigma^2}} \,dx \\
&= \frac{\hbar}{i} \left[\left( \frac{1}{2 \pi} \right)^{1 / 4} \frac{1}{\sqrt{\sigma}}\right]^2
\int_{-\infty}^\infty \left(ik_0 - \frac{x}{2\sigma^2}\right) e^{-\frac{x^2}{2 \sigma^2}} \,dx \\
&= \frac{\hbar}{i} \left[\left( \frac{1}{2 \pi} \right)^{1 / 4} \frac{1}{\sqrt{\sigma}}\right]^2
\left(\int_{-\infty}^\infty ik_0 e^{-\frac{x^2}{2 \sigma^2}} \,dx - \int_{-\infty}^\infty \frac{x}{2\sigma^2} e^{-\frac{x^2}{2 \sigma^2}} \,dx \right)
\end{align*}
{% end %}

> It is helpful to remember that the conjugate of anything real-valued is itself (e.g. the conjugate of $e^{-\frac{x^2}{2\sigma^2}}$ is itself. Meanwhile, anything complex-valued in the form $e^{\pm i \phi}$ has $e^{\mp i\phi}$ as its conjugate. For instance, $e^{-i\omega t}$ has the conjugate $e^{i\omega t}$, and $e^{-i\omega t} e^{i\omega t} = 1$. 

Note, however, that the second integral in the last line of our expression is an odd function, so the integral goes to zero. Therefore, we have the simplified integral (relief!) as follows:

{% math() %}
\begin{align*}
\langle p \rangle &= \frac{\hbar}{i} \left[\left( \frac{1}{2 \pi} \right)^{1 / 4} \frac{1}{\sqrt{\sigma}}\right]^2
\int_{-\infty}^\infty ik_0 e^{-\frac{x^2}{2 \sigma^2}} \,dx \\
&= \dfrac{\hbar k_0}{\sigma \sqrt{2\pi}} \int_{-\infty}^\infty e^{-\frac{x^2}{2 \sigma^2}} \,dx
\end{align*}
{% end %}

This is a _Gaussian integral_ that we can solve with the following identity:

{% math() %}
\displaystyle \int_{- \infty}^{\infty} e^{- \alpha y^2} d y = \sqrt{\dfrac{\pi}{a}}
{% end %}

If we use the substitution that $a = \dfrac{1}{2\sigma^2}$ then we have:

{% math() %}
\begin{align*}
\langle p \rangle &= \dfrac{\hbar k_0}{\sigma \sqrt{2\pi}} \int_{-\infty}^\infty e^{-\frac{x^2}{2 \sigma^2}} \,dx \\
&= \dfrac{\hbar k_0}{\sigma \sqrt{2\pi}} \sqrt{2\pi \sigma^2} \\
&= \dfrac{\hbar k_0}{\sigma \sqrt{2\pi}} \sigma \sqrt{2\pi} \\
&= \hbar k_0
\end{align*}
{% end %}

This is indeed the momentum we expect of a single particle of wavevector $k_0$. While a free particle's momentum can be any eigenvalue of the momentum operator, and cannot be predicted in advance, the _average_ momentum over several measurements $p = \hbar k_0$ is **equal** to the de Broglie expression for the momentum. Thus, _on average_, quantum mechanics reduces to deterministic laws.

### The infinite square well

Consider a particle that is trapped at a bottom of a well with length $L$ and walls that are infinitely high. We may model this with a potential given by:

{% math() %}
V(x) = \begin{cases}
\infty, & x < 0 \\
0, & 0 \leq x \leq L \\
\infty, & x > L
\end{cases}
{% end %}

The general solution of the time-independent Schrödinger equation is given by:

{% math() %}
\psi(x, t) = A e^{i k x} + B e^{-ik x}
{% end %}

For some yet-to-be determined constants $A$ and $B$. As the particle is confined within the region $0 \leq x \leq L$, the wavefunction must satisfy the boundary conditions that $\psi(0) = \psi(L) = 0$. By substituting $\psi(0) = 0$ into the equation we have:

{% math() %}
\psi(0) = A + B = 0 \Rightarrow B = -A
{% end %}

Thus our solution becomes:

{% math() %}
\psi(x, t) = A e^{i k x} + (-A) e^{-ik x} = A(e^{i k x} - e^{-ikx})
{% end %}

The, we substitute $\psi(L) = 0$. Therefore we have:

{% math() %}
A(e^{i k L} - e^{-ikL}) = 0
{% end %}

We may convert this using Euler's formula to be expressed in terms of trigonometric functions, recalling that $e^{i\theta} - e^{-i\theta} = 2 i\sin \theta$:

{% math() %}
A(e^{i k L} - e^{-ikL}) = 2Ai \sin (kL) = 0
{% end %}

Sine is equal to zero at $\theta = 0, \pi, 2\pi, 3\pi, \dots = n\pi$ so we have:

{% math() %}
kL = n\pi
{% end %}

Which we can rearrange to:

{% math() %}
k = \dfrac{n\pi}{L}
{% end %}

Thus our solution can now be written as:

{% math() %}
\psi(x) = 2A i \sin \left(\dfrac{n\pi x}{L}\right)
{% end %}

With associated probability density:

{% math() %}
\rho(x) = |\psi(x)|^2 = -4A^2 \sin^2 \left(\dfrac{n\pi x}{L}\right)
{% end %}

We may solve for $A$, the normalization factor, by demanding that the integral of the probability density over all space be equal to one:

{% math() %}
\int_{-\infty}^\infty \rho(x)\, dx = 1
{% end %}

From here, we can find that $2Ai = \sqrt{\dfrac{2}{L}}$ and therefore the spatial wavefunction is:

{% math() %}
\psi(x) = \sqrt{\dfrac{2}{L}} \sin \left(\dfrac{n\pi x}{L}\right)
{% end %}

To find the wavefunction in time, we simply apply the Hamiltonian to $\psi$, recalling the $\hat H \psi = E\psi$, where we find that:

{% math() %}
\begin{align*}
\hat H \psi &= -\frac{\hbar^2}{2m} \dfrac{\partial^2}{\partial x^2} \sqrt{\dfrac{2}{L}} \sin \left(\dfrac{n\pi x}{L}\right) \\
& = \dfrac{n^2 \pi^2 \hbar^2}{2 m L^2} \sqrt{\dfrac{2}{L}} \sin \left(\dfrac{n\pi x}{L}\right) \\
&= E \psi
\end{align*}
{% end %}

Thus we identify the energies as given by:

{% math() %}
E_n = \dfrac{n^2 \pi^2 \hbar^2}{2 m L^2}, \quad n = 1, 2, 3, \dots
{% end %}

Note that instead of one energy or a continuous energy spectrum, we have _discrete_ energies $E_1, E_2, E_3, \dots$, one for each integer value of $n$. The $E_1$ state, which is the lowest energy state, is called the **ground state**. Interestingly, this is nonzero; its energy is given by:

{% math() %}
E_1 = \dfrac{\pi^2 \hbar^2}{2 m L^2}
{% end %}

This is due to the fact that the energy and momentum operators commute, so that if $E = 0$, then we know the precise energy of the quantum particle (zero) and the precise momentum (also zero). But if the momentum were known precisely (and thus have zero uncertainty), then the Heisenberg uncertainty principle would be violated:

{% math() %}
\Delta x \Delta p = \Delta x (0) = 0 \ngeq \dfrac{\hbar}{2}
{% end %}

Thus the energy in the ground state cannot be zero; rather, it is a nonzero value we often call the **zero-point energy**. In addition, since energy can only come in steps of integer $n$, we say that the energy is **quantized** - hence _quantum_ mechanics.

> The zero-point energy is the origin of many physical processes, and is explored in-depth in quantum field theory. It is also of interest in cosmology, where the expansion of the Universe is, according to our best understanding at present, driven by zero-point energy.

### The hydrogen atom

A very famous quantum system is that of the hydrogen atom - the simplest atom, with one electron and one proton. We can simplify the system even further by modelling the contribution of the proton with the _classical_ Coloumb charge potential, since the proton is "large enough" compared to the electron (almost a thousand times more massive) that its behavior deviates only slightly from the classical description. Thus, we only need to consider the quantum behavior of the electron for the wavefunction of the entire hydrogen atom system.

> **Note:** In fact, the solution for the hydrogen atom can be generalized to be an exact solution for all _hydrogen-like_ atoms. For instance, it can also be used to solve for the $\ce{He^+}$ atom (helium ion), as well as all the group 1 elements in the periodic table (lithium, sodium, potassium, rubidium, and cesium), ions that have one valence electron (such as $\ce{Ca^+}$ and $\ce{Sr^+}$), and all isotopes of these atoms.

Using the time-independent Schrödinger equation with the Coloumb potential, we have the partial differential equation:

 {% math() %}
 -\frac{\hbar^2}{2m} \nabla^2 \psi - \frac{e^2}{4\pi \varepsilon_0 r} \psi = E \psi
 {% end %}

 This is typically solved in spherical coordinates, where the $\nabla^2$ (Laplacian) operator becomes a mess, resulting in the overwhelmingly long equation (copied from Wikipedia):

 {% math() %}
 -{\frac {\hbar ^{2}}{2m}}\left[{\frac {1}{r^{2}}}{\frac {\partial }{\partial r}}\left(r^{2}{\frac {\partial \psi }{\partial r}}\right)+{\frac {1}{r^{2}\sin \theta }}{\frac {\partial }{\partial \theta }}\left(\sin \theta {\frac {\partial \psi }{\partial \theta }}\right)+{\frac {1}{r^{2}\sin ^{2}\theta }}{\frac {\partial ^{2}\psi }{\partial \varphi ^{2}}}\right]-{\frac {e^{2}}{4\pi \varepsilon _{0}r}}\psi =E\psi
 {% end %}

 The one saving grace is that this PDE happens to be a _separable_ differential equation, and can be solved using separation of variables. But solving this is a matter of mathematics, not physics, and so we will omit the solving steps and just give the general solution:

 {% math() %}
 \psi _{n\ell m}(r,\theta ,\varphi )={\sqrt {{\left({\frac {2}{na_{0}}}\right)}^{3}{\frac {(n-\ell -1)!}{2n(n+\ell )!}}}}e^{-r /2}r^{\ell }L_{n-\ell -1}^{2\ell +1}(r )Y_{\ell }^{m}(\theta ,\varphi )
 {% end %}

 Where:

- $a_0 = \frac{4\pi \epsilon_0 \hbar^2}{me^2}$ is the Bohr radius, where the electron is most likely to be found in the ground-state hydrogen atom
- $\rho = \frac{2r}{na_0^*}$
- $L_{n - \ell - 1}^{2 \ell + 1}(\rho)$ is a Laguerre polynomial
- $Y_\ell^m (\theta, \varphi)$ is a spherical harmonic function
- $n = 1, 2, 3, \dots$ is the principal quantum number that determines the energy level and parametrizes each eigenstate
- $\ell = 0, 1, 2, \dots, n-1$ is the azimuthal quantum number
- $m = -\ell, \dots, \ell$ is the magnetic quantum number

We can visualize the hydrogen wavefunction (or more precisely, the hydrogen eigenstates) by ploting the probability density:

![](https://miro.medium.com/v2/resize:fit:1400/1*kqtDZDdum_mLQLezPlemsA.png)

_Source: [Sebastian Mag, Medium](https://ssebastianmag.medium.com/computational-physics-with-python-hydrogen-wavefunctions-electron-density-plots-8fede44b7b12)_

The energy levels of hydrogen are given by the energy eigenvalues of its Hamiltonian:

{% math() %}
E_n = -\dfrac{\mu e^4}{32\pi^2 \varepsilon_0^2 \hbar^2} \dfrac{1}{n^2} = -\dfrac{\mu c^2 \alpha^2}{2n^2}
{% end %}

Which can be written in even simpler form as $E_n = -\dfrac{\mu R_E}{m_e n^2} \approx -\dfrac{R_E}{n^2}$ where $R_E = \dfrac{m_e c^2 \alpha^2}{2}$, known as the **Rydberg energy** which is approximately $\pu{-13.6 eV}$.
In this expression:

- $c$ is the speed of light
- $n$ is the principal quantum number
- $j$ is the total angular momentum quantum number
- $\mu \equiv \dfrac{m_e m_p}{m_e + m_p}$ (where $m_e, m_p$ are the electron and proton mass) is the reduced mass of the hydrogen atom, which is very close to (but not exactly equal to) $m_e$, the mass of an electron
- $\alpha$ is the fine-structure constant and approximately equal to $1/137$

> **An important note:** Yes, these energy eigenvalues are negative, because the Coulomb potential is negative as well. In fact, we say that the negative energies reflect the fact that the associated eigenstates are _bound states_, and the magnitude of their energy is the energy necessary to overcome the Coulomb potential. As their energies are negative, they do not have enough energy to escape the potential, and thus stay in place - the more negative the energy, the more energy must be put in to "kick" electrons out of place, and the stabler the system.

The historical discovery of the solution to the Schrödinger equation for the hydrogen atom and the calculation of its eigenvalues proved to be one of the first experimental results that confirmed the predictions of quantum mechanics. By using $E_n = \dfrac{hc}{\lambda_n}$ with the value of $E_n = -\dfrac{\mu c^2 \alpha^2}{2n^2}$ predicted by the Schrödinger equation, the calculated wavelengths of light almost exactly matched measurements of those emitted by hydrogen. To read more about this discovery, see the quantum chemistry portion of the [general chemistry series](@/general-chem/index.md). This result revolutionized physics and brought quantum mechanics to its forefront. To this day, quantum mechanics remains the building block of modern physics.

Later on, refinements to quantum theory found that the predicted energy levels, when also including relativistic corrections, are more accurately given by:

{% math() %}
\begin{align*}
E_{j, n} &= -{\mu c^2}\left[{1 - \left(1 + \left(\dfrac{\alpha}{n - j - \frac{1}{2} + \sqrt{\left(j + \frac{1}{2}\right)^2 - \alpha^2}}\right)^2
\right)^{-1/2}}\right] \\
&= -\dfrac{\mu c^2 \alpha^2}{2n^2} \left[1 + \dfrac{\alpha^2}{n^2} \left(\dfrac{n}{j + 1/2} - \dfrac{3}{4}\right) + \dots\right]
\end{align*}
{% end %}

Where again, $\mu$ is the reduced mass, $\alpha \approx 1/137$ is the fine-structure constant, and $j_\pm = |\ell \pm \frac{1}{2}|$. Notice that this more accurate expression depends on _two integers_ $n$ and $j$, unlike the non-relativistic expression, which only depends on $n$. However, when we perform a series expansion (shown above), and take only the first-order term, we obtain (as the first term) the energy levels obtained from the Schrödinger equation. We will not derive this ourselves, but we will touch on relativistic quantum mechanics briefly again at the end of this guide.

### The quantum harmonic oscillator

We'll now take a look at the quantum harmonic oscillator, a quantum system describing a particle that oscillates within a harmonic (i.e. quadratic) potential. But first, why study it? The reason is because all potentials are _approximately_ harmonic potentials close to their local minimums. Let us see how this gives us powerful tools to solve non-trivial quantum systems.

Consider solving the Schrödinger equation with a non-trivial potential $V(x)$ for some given quantum system. We may expand it as a Taylor series. When the system oscillates about a local minimum of the potential - which, in physical terms, corresponds to having a total energy $E$ slightly above the potential minimum $V_0$ - then the first derivative is approximately zero. The second derivative is a constant, and all higher-order terms vanish. Therefore, the potential can be written as:

{% math() %}
V(x) = V(x_0) + \cancel{V'(x_0) x} + \frac{1}{2} V''(x_0) x^2 + \cancel{\frac{1}{6} V'''(x_0) x^3} + \cancel \dots = V_0 + \dfrac{1}{2}kx^2
{% end %}

As the potential energy can be defined against an arbitrarily-chosen reference point, we may add or subtract any constant from the potential without affecting the physics. Thus, we can just as well write the potential as:

{% math() %}
V(x) = \dfrac{1}{2} kx^2
{% end %}

If we set $\omega = \sqrt{\frac{k}{m}}$ to be the _angular frequency_ of the oscillations about the potential, then we may rewrite this as:

{% math() %}
V(x) = \dfrac{1}{2} m \omega^2 x^2
{% end %}

Ultimately, the point of studying the quantum harmonic oscillator is that for _any_ quantum system constrained to evolve under a potential $V(x)$, their behavior close to a local minimum of the potential will be approximately that of the quantum harmonic oscillator, no matter how complicated the potential is. This greatly increases the number of systems we can find (at least) approximate analytical solutions of.

With all that said, we may now begin solving the Schrödinger equation for the quantum harmonic oscillator. Inserting the harmonic potential into the time-independent Schrödinger equation results in the following PDE:

{% math() %}
-\dfrac{\hbar^2}{2m} \dfrac{\partial^2 \psi}{\partial x^2} + \dfrac{1}{2} m \omega^2 x^2 \psi = E\psi
{% end %}

Given that the solution is dependent only on position we may replace the partial derivatives with ordinary derivatives:

{% math() %}
-\dfrac{\hbar^2}{2m} \dfrac{d^2 \psi}{dx^2} + \dfrac{1}{2} m \omega^2 x^2 \psi = E\psi
{% end %}

This is not an easy differential equation to solve, and finding a solution that describes all the possible states of the quantum harmonic oscillator is highly non-trivial. However, we can make the problem tractable by just solving for the ground state of the quantum harmonic oscillator. By making the assumption that the ground state (being the lowest-energy state) has a very small energy, so $E_0 \psi \approx 0$, the differential equation reduces to: 

{% math() %}
-\dfrac{\hbar^2}{2m} \dfrac{d^2 \psi}{dx^2} + \dfrac{1}{2} m \omega^2 x^2 \psi = 0
{% end %}

We may now algebraically rearrange the differential equation into the form:

{% math() %}
\dfrac{d^2 \psi}{dx^2} = \dfrac{m^2 \omega^2}{\hbar^2} x^2 \psi
{% end %}

Now note that this can be rewritten as:

{% math() %}
\dfrac{d^2 \psi}{dx^2} = \left(\dfrac{m \omega}{\hbar}\right)^2 x^2 \psi
{% end %}

If we define a constant $k_s \equiv \dfrac{m \omega}{2\hbar}$ - the physical meaning of this constant will be discussed later - then we can write this as:

{% math() %}
\dfrac{d^2 \psi}{dx^2} = k_s^2 x^2 \psi
{% end %}

To understand why we do this, we can do some dimensional analysis. The units of $\dfrac{m\omega}{\hbar}$ on the right-hand side of the differential equation are those of inverse squared meters, that is, $\pu{m^{-2}}$. We know of a quantity that has units of inverse meters - the wavevector $k$ - so therefore $\dfrac{m\omega}{\hbar}$ must be proportional to the square of the wavevector. Thus we write $k_s \propto k^2$, with some undetermined proportionality constant.

Recalling that $p = \hbar k$ and therefore $p^2 = \hbar^2 k^2$, we may rearrange to $k^2 = \dfrac{p^2}{\hbar^2}$. But also recalling that $E = \dfrac{p^2}{2m}$ we can rearrange this to find that $p^2 = 2mE$ and thus $k^2 = \dfrac{2mE}{\hbar^2}$. However, we also know _another_ expression for the energy - $E = \hbar \omega$, so if we substitute this in, we have 

{% math() %}
k^2 = \dfrac{2m\hbar \omega}{\hbar^2} = \dfrac{2m \omega}{\hbar}
{% end %} 

This is _almost_ there, but not quite - there is the additional factor of two. This is why we include the factor of $1/2$. 

Proceeding from the prior steps, we may consider a solution _ansatz_ in the form: 

{% math() %}
\psi = A e^{-k_s x^2} = Ae^{-\left(\frac{m\omega}{2\hbar}\right) x^2}
{% end %} 

where $A$ is some undetermined normalization factor. All of what we have done so far is just an (educated) guess - that is the essence of the _ansatz_ technique - but it is the right guess, because if we proceed from this assumption, it can be shown that we get the correct results, and had we guessed wrong we could've just chosen another guess. 

If we substitute this _ansatz_ into the Hamiltonian, we find that:

{% math() %}
\begin{align*}
\hat H \psi &=
-\dfrac{\hbar^2}{2m} \dfrac{d^2 \psi}{dx^2} + \dfrac{1}{2} m \omega^2 x^2 \psi \\
&= -\dfrac{\hbar^2}{2m}\dfrac{d^2}{dx^2} \left(Ae^{-k_s x^2}\right) + \dfrac{1}{2} m \omega^2 x^2 \left(Ae^{-k_s x^2}\right) \\
&= -\dfrac{\hbar^2}{2m} (4 k_s^2 x^2 - 2k_s)Ae^{-k_s x^2}  + \dfrac{1}{2} m \omega^2 x^2 \left(Ae^{-k_s x^2}\right) \\
&= \left(-\dfrac{\hbar^2}{2m} (4 k_s^2 x^2 - 2k_s) + \dfrac{1}{2} m \omega^2 x^2\right)Ae^{-k_s x^2} \\
&= \left(-\dfrac{4\hbar^2}{2m}\frac{m^2\omega^2}{4\hbar^2} x^2 + \dfrac{2\hbar^2}{2m} \frac{m\omega}{2\hbar} + \dfrac{1}{2}m\omega^2 x^2\right)Ae^{-k_s x^2} \\
&= \left(-\dfrac{1}{2}m\omega^2 x^2 + \dfrac{2\hbar^2}{2m} \frac{m\omega}{2\hbar} + \dfrac{1}{2}m\omega^2 x^2\right)Ae^{-k_s x^2} \\
&= \dfrac{1}{2} \hbar \omega Ae^{-k_s x^2} \\
&= \dfrac{1}{2}\hbar \omega \psi \\
&= E \psi
\end{align*}
{% end %}

Thus our _ansatz_ does satisfy the Schrödinger equation $\hat H \psi = E\psi$, showing that our solution is indeed valid (even if we had to take some very wild guesses to get there!) We do still need to normalize it, however, to ensure the solution is physical (which also automatically satisfies the boundary conditions of the problem $\psi(-\infty) = \psi(\infty) = 0$). Applying the normalization condition we have:

{% math() %}
\begin{align*}
\int_{-\infty}^\infty \psi^*(x)\psi(x)\, dx
&= \int_{-\infty}^\infty Ae^{-k_s x^2} Ae^{-k_s x^2} dx \\
&= A^2 \int_{-\infty}^\infty e^{-2k_s x^2} dx \\
&= A^2\sqrt{\dfrac{\pi}{2k_s}}
\end{align*}
{% end %}

Where we solved the integral using the Gaussian integral identity:

{% math() %}
\int_{-\infty}^\infty e^{-a x^2} = \sqrt{\dfrac{\pi}{a}}
{% end %}

For probability to be conserved, we must have the $A^2\sqrt{\dfrac{\pi}{2k_s}} = 1$, using which we can solve for $A$:

{% math() %}
\begin{gather*}
A^2\sqrt{\dfrac{\pi}{2k_s}} = 1 \\
A^2 = \sqrt{\dfrac{2k_s}{\pi}} \\
A = \left(\dfrac{2k_s}{\pi}\right)^{1/4}
\end{gather*} \\
A = \left(\dfrac{m\omega}{\pi \hbar}\right)^{1/4}
{% end %}

So the ground state of the quantum harmonic oscillator is given by:

{% math() %}
\psi_0 = \left(\dfrac{m\omega}{\pi \hbar}\right)^{1/4} e^{-\left(\frac{m\omega}{2\hbar}\right) x^2}
{% end %}

Furthermore, we note that this solution for the ground state of the quantum harmonic oscillator has energy eigenvalue $E_0 = \dfrac{1}{2}\hbar\omega$. The _general expression_ for the energy eigenvalues of the quantum harmonic oscillator are given by:

{% math() %}
E_n = \left(n + \dfrac{1}{2}\right)\hbar \omega
{% end %}

For which we can see that with $n = 0$ we have the familiar expression of $E = \dfrac{1}{2} \hbar \omega$. What about the general expression for the wavefunction, you might ask? Well, it is given by:

{% math() %}
\psi_n(x) = \left(\dfrac{m\omega}{\pi \hbar}\right) \dfrac{1}{\sqrt{2^n n!}} H_n\left(\sqrt{\dfrac{m\omega}{\hbar}}x \right) \exp\left(-\dfrac{m\omega x^2}{2\hbar}\right)
{% end %}

Where $n$ is the principal quantum number (as with the hydrogen atom), and $H_n(x)$ is an $n$-th order [Hermite polynomial](https://en.wikipedia.org/wiki/Hermite_polynomials), which are a set of special functions, much like the Laguerre polynomials used in the wavefunction of the hydrogen atom. We show some plots of the quantum harmonic oscillator wavefunction for different  below:

{{ diagram(
src="https://upload.wikimedia.org/wikipedia/commons/9/9e/HarmOsziFunktionen.png"
alt="Plots of the wavefunction of the quantum harmonic oscillator for its first few energy levels"
) }}

_Source: [Wikipedia](https://commons.wikimedia.org/wiki/File:HarmOsziFunktionen.png)_

Understandably, considering the fact that the most general solution can only be expressed in terms of special functions, we started by solving only for the ground state, not the general case for all energy levels!

## The mathematics behind quantum mechanics

The Schrödinger equation is certainly a very useful tool and all problems in non-relativistic quantum theory, with the exception of problems that involve spin, can be solved from the Schrödinger equation. However, simply taking the Schrödinger equation for granted is ignoring _why_ it works the way it does. So we will now take many steps back and build up quantum theory from its mathematical and physical fundamentals.

### Postulate 1: quantization

When a quantitiy is said to be **quantized**, it _cannot take on continuous values_; it can only come in discrete steps. In addition, all possible values of that quantity must be an integer multiple of some base indivisible value. 

For example, consider electrical charge. The base value of electric charge is the elementary charge constant $e$ (not to be confused with Euler's number), associated with a single electron. It is _only_ possible for an object in the universe to have a charge of $1e, 2e, 3e, \dots ne$. It is not possible for an object to have a charge of $3.516e$.

> Note to the advanced reader: yes, indeed, quarks have a different quantum of charge, but since quarks can never be found on their own, and are always grouped together into composite, not elementary particles, we consider $e$ the quantum of charge, associated with an electron.

Similarly, consider electromagnetic radiation. The base value of electromagnetic energy is given by $hf = \dfrac{hc}{\lambda}$, the radiation of a single photon of frequency $f$ and wavelength $\lambda$, where $h = \pu{6.626e-34 J*Hz^{-1}}$ is the Planck constant. All electromagnetic energy of a given frequency $f$ and wavelength $\lambda$ must be composed of multiples of this value.

### Postulate 2: quantum states

In classical mechanics, the future state of any system of particles can be known by knowing its current state and its equations of motion. The equations of motion are Newton's 2nd law:

{% math() %}
m \frac{d^2 \mathbf{r}}{dt^2} = \mathbf{F}(\mathbf{r}, t)
{% end %}

Which can be rewritten as system of 2 coupled first-order ODEs:

{% math() %}
\begin{align*}
\frac{d\mathbf{p}}{dt} = \mathbf{F}(\mathbf{r}, t) \\
m \frac{d\mathbf{r}}{dt} = \mathbf{p}
\end{align*}
{% end %}

The initial condition for this system is the **classical state** of the particle, and is the following 6-component vector, consisting of three components of position and three components of momentum:

{% math() %}
\mathbf{X}_0 = \begin{pmatrix}
x_0 \\
y_0 \\
z_0 \\
p_{x_0} \\
p_{y_0} \\
p_{z_0}
\end{pmatrix}
{% end %}

In quantum mechanics, the current state of a system is described with a **quantum state-vector**. This is typically written abstractly as a complex vector $|\Psi\rangle$ whose components are complex numbers, with the specialized notation (called bra-ket or Dirac notation) used to differentiate quantum states from classical states. 

> **Note on notation:** in bra-ket notation, all vectors are denoted with the right angle-bracket $| V \rangle$, and a scalar multiplication of a vector is written $a | V \rangle$.

Quantum state-vectors can be hard to understand, so it is worth taking some time to get to know them. Recall that ordinary Cartesian vectors in the form $\langle x, y, z \rangle$ can be written in terms of the Cartesian basis vectors $\hat i, \hat j, \hat k$:

{% math() %}
\mathbf{V} = V_x \hat i + V_y \hat j + V_z \hat k
{% end %}

We can alternatively denote the Cartesian basis vectors with $\hat e_x, \hat e_y, \hat e_z$, in which notation the same vector can be written as:

{% math() %}
\mathbf{V} = V_x \hat e_x + V_y \hat e_y + V_z \hat e_z
{% end %}

We can also write the same using index notation. Let $i = 1, 2, 3$ equal the coordinates $x, y, z$, and let $\hat e_1, \hat e_2, \hat e_3 = \hat e_x, \hat e_y, \hat e_z$. Then we may write:

{% math() %}
\mathbf{V} = V_1 \hat e_1 + V_2 \hat e_2 + V_3 \hat e_3 = \sum_{i = 1}^3 V_i e_i
{% end %}

Thus we can write ordinary vectors as a **superposition** (sum of constant multiple terms) of the Cartesian basis vectors and their components. Quantum state-vectors can also be written as a superposition of basis vectors and components, but unlike ordinary Cartesian vectors in Euclidean 3D space $\mathbb{R^3}$, they reside in a complex Hilbert space $\mathcal{H}$, and can have infinitely many components. Expressed as a superposition, they take the form:

{% math() %}
| \Psi \rangle = 
\begin{pmatrix}
\Psi_1 \\ 
\Psi_2 \\ 
\Psi_3 \\ 
\vdots \\ 
\Psi_n
\end{pmatrix} =
\Psi_1 | \phi_1 \rangle + \Psi_2 | \phi_2 \rangle + \Psi_3 | \phi_3 \rangle + \dots
{% end %}

where $\Psi_1, \Psi_2, \dots \Psi_n$ are the components (which are in general complex-valued) and $| \phi_1 \rangle, | \phi_2 \rangle, \dots | \phi_n \rangle$ are the basis vectors. What these basis vectors and components represent, we'll see in a moment. Using the index notation introduced earlier, the superposition form of a quantum state-vector can be compactly written as:

{% math() %}
|\Psi\rangle = \sum_{i = 1}^n \Psi_i | \phi_i \rangle
{% end %}

Consider, for instance, a quantum coin. A real coin, of course, is technically not truly random; if you could measure the exact position and velocity of the coin at the moment it was flipped, you could determine if it would land heads or tails. However, imagine a quantum coin that was fully probabilistic - not even full knowledge of its state $|\Psi \rangle$ could be enough to predict its future outcome. The only thing we _do_ know about this quantum coin is that, just like a regular coin, it has a 50% probability of landing heads, and a 50% probability of landing tails, and those are the _only two possible states_ it could be in. Then we could write its quantum state as:

{% math() %}
|\Psi \rangle = \frac{1}{\sqrt{2}} | \Psi_H \rangle + \frac{1}{\sqrt{2}} | \Psi_T \rangle
{% end %}

Where $| \Psi_H \rangle$ is the "heads" state, $| \Psi_T \rangle$ is the "tails" state, and the coefficients are both $\frac{1}{\sqrt{2}}$ because the square of $\frac{1}{\sqrt{2}} = \frac{1}{2} = 50\\%$ which was the probability we know the coin can be in either one of its states. So now we can give a _physical_ interpretation of the coefficients and basis vectors that make up the superposition of $| \Psi \rangle$:

> For any given quantum state-vector $| \Psi \rangle = \Psi_1 | \phi_1 \rangle + \Psi_2 | \phi_2 \rangle + \Psi_3 | \phi_3 \rangle + \dots$ the basis vectors are to be interpreted as _possible states_ (such as possible locations, possible momenta, possible energies, etc.) and the squares of coefficients are to be interpreted as _probabilities_ of being in a particular state.

To get out of over-abstractness it is helpful to explicitly write down these superpositions. For instance, a wave-vector of a one-dimensional particle can be written using basis vectors of position, where each basis vector $| x \rangle$ represents the state where the particle is at point $x$:

{% math() %}
| \Psi \rangle = \Psi_1 | x_1 \rangle + \Psi_2 | x_2 \rangle + \Psi_3 | x_3 \rangle + \dots
{% end %}

Or perhaps more concretely:

{% math() %}
| \Psi \rangle = 0.1~| \text{ at 1 cm } \rangle + 0.2~| \text{ at 1.5 cm } \rangle + 0.7~| \text{ at 2 cm } \rangle + \dots
{% end %}

Here, each squared coefficient becomes the _probability_ of the particle being at point $x$. For instance, the square of the $\Psi_1$ coefficient is the probability of the particle being at the point $x_1 = \pu{1cm}$. 

The same wave-vector can be written using basis vectors of momentum, where each basis vector $| p \rangle$ represents the state of the particle having momentum $p$:

{% math() %}
| \Psi \rangle = \Psi_1 | p_1 \rangle + \Psi_2 | p_2 \rangle + \Psi_3 | p_3 \rangle + \dots
{% end %}

Each squared coefficient now becomes the probability of the particle having that momentum $p$. For instance, the square of $\Psi_1$ will be the probability of the particle of having momentum $p_1$.

We can do the same with energy basis vectors, with each basis vector $|E \rangle$ representing the state where the particle has energy $E$, and each squared coefficient is the associated probability:

{% math() %}
| \Psi \rangle = \Psi_1 | E_1 \rangle + \Psi_2 | E_2 \rangle + \Psi_3 | E_3 \rangle + \dots
{% end %}

All vectors, quantum state-vectors included, exist independently of their basis vectors. For instance, a regular 3D vector can be equivalently written in Cartesian coordinates, polar coordinates, cylindrical coordinates, or any other coordinate system, each of which uses different basis vectors. A quantum state-vector can similarly be written in any chosen set of basis vectors, although only a few, like the position, momentum, and energy basis vectors shown, are physically meaningful. The square of the coefficients associated with the choice of basis vectors returns the probabilities of being in a particular state, such as the probabilities of a particle being in a state of a certain position, or energy, as we just showed.

Be aware, however that saying "the square of the coefficients" is a loose way of describing the process of actually computing the probability, as the coefficients of $| \Psi \rangle$ are, in general, complex-valued. So in actuality, we typically mean the **squared norm** of the components of $| \Psi \rangle$, that is:

{% math() %}
P = | \Psi_i |^2
{% end %}

And we can use the complex identity $|z|^2 = z z^*$ to rewrite as:

{% math() %}
P = \Psi_i \Psi_i^*
{% end %}

For instance, the probability a particle is in its $|E_1 \rangle$ state corresponding to having an energy of $E_1$ is given by;

{% math() %}
P = \Psi_1 \Psi_1^*
{% end %}

But you may ask, isn't it absurd that a particle's position, momentum, energy, and so forth all come from writing down the same state-vector using different basis vectors? This is a good question to ask, but recall that in classical mechanics, position, momentum, and energy can _also_ all be found from the same classical state of $(\mathbf{x}_0, \mathbf{p}_0)$ packaged together as one vector.

And remember Newton's 2nd law as the key equation governing how a classical state can evolve? Quantum states evolve too, but under a partial differential equation called the **Schrödinger equation**:

{% math() %}
i \hbar \frac{\partial}{\partial t} | \Psi \rangle = \hat H | \psi \rangle
{% end %}

Where $\hat H$ can be thought of as a type of matrix that acts on the state-vector $| \Psi \rangle$. What is its physical interpretation? That is what we'll see in the next section.

### Postulate 3: observables

The rules of linear algebra apply when working with quantum state-vectors, as they do for regular vectors. For instance, matrices, which encode linear transformations, act on vectors in linear algebra. Similarly, linear operators act on state-vectors in quantum mechanics.

First, what is a linear operator? Put simply, a linear operator does some sort of operation on a state-vector, be it multiplication, differentiation, or even exponentiation (more on that later). Linear operators are commonly either denoted with hats like $\hat M$, or with boldface like $\mathbf{M}$, of which the hat notation will be predominantly used. What makes linear operators _linear_ is the fact that it doesn't matter whether you scalar-multiply and sum a state-vector _before_ or _after_ you apply the linear operator, the result is the same. Mathematically speaking, we can represent this fact with:

{% math() %}
a \hat M | \Psi \rangle_A + b \hat M | \Psi \rangle_B = \hat M (a | \Psi \rangle_A + b | \Psi \rangle_B)
{% end %}

This looks _very_ similar to the constant and sum rules for derivatives:

{% math() %}
a \frac{d}{dx} f(x) + b \frac{d}{dx} g(x) = \frac{d}{dx} (a f(x) + b g(x))
{% end %}

In fact, the differentiation operator $\frac{d}{dx}$ **is** a linear operator. So is the integration operator, the partial differentiation operator, and the gradient operator from vector calculus. In addition, so is an operator that does multiplication by a scalarvalue, or of a function; one could define an operator $\hat C$ that simply multiplies the state-vector by a certain constant, or a certain function. You can check by substitution that such an operator is linear.

But that is mathematics, we want to do physics, and so we will only use the operators that are physically meaningful, of which there are just a few, with some examples being the position, momentum, and energy (Hamiltonian) operators. These can be derived from taking the classical limit and finding out what the operators must be to reproduce classical mechanics. Recall that the Schrödinger equation is given by:

{% math() %}
i \hbar \frac{\partial}{\partial t} | \Psi \rangle = \hat H | \psi \rangle
{% end %}

The interpretation of this equation now is clearer: it specifies that the change through time of the state-vector (left-hand side of the equation) is proportional to the energy operator acting on the state-vector (right-hand side of the equation). That is, energy drives the evolution of a quantum system. The proportionality constant $i \hbar$ is simply there for 1) dimensional consistency and 2) to ensure both sides of the equation are complex-valued. Operators also allow us to write the time-independent form of the Schrödinger equation:

{% math() %}
E | \Psi \rangle = \hat H | \psi \rangle
{% end %}

Where $E$ is a constant associated with, understandably, the energy. This form is easier to solve, and can be used to find explicit analytical solutions for a variety of quantum systems.

#### Interlude: concrete representations of state-vectors

Up to this point we have been working with state-vectors abstractly as a linear superposition of basis vectors:

{% math() %}
| \Psi \rangle = \Psi_1 | \phi_1 \rangle + \Psi_2 | \phi_2 \rangle + \Psi_3 | \phi_3 \rangle + \dots
{% end %}

This form works out nicely when the possible states of a quantum system are small - such as the quantum coin we saw earlier, which can only be in two states, heads or tails. However, it is not as helpful when considering many possible states, where the superposition has so many terms that writing it all out becomes ridiculous. We want a more concrete, more familiar representation of state-vectors for actual calculations. And for this, we turn to the **inner product**.

The inner product is a generalization of the dot product, familiar from physics formulas such as the definition of work $W = \mathbf{F} \cdot \Delta \mathbf{x}$. Recall that you can take the dot product by writing out a regular vector in column vector form, and their associated row vector, which is just the same vector but written out in row form. Then the respective elements are multiplied together, like this:

{% math() %}
\mathbf{A} \cdot \mathbf{B} =
\begin{pmatrix}
A_x & A_y & A_z
\end{pmatrix}
\begin{pmatrix}
B_x \\ B_y \\ B_z
\end{pmatrix} = A_x B_x + A_y B_y + A_z B_z
{% end %}

In quantum mechanics, the analogue of column and row vectors are **bra-vectors** and **ket-vectors**, or bras and kets for short. For a bra-vector, such as the quantum state-vector $| \Psi \rangle$, the associated ket-vector $\langle \Psi |$ is found by taking the complex conjugate of each of its components $z \to z^*$, and then transposing (converting all columns to rows, and vice-versa). The ket-vector version of a given bra-vector is also called the **adjoint**. We can write this in the specialized notation (Dirac notation) as:

{% math() %}
\langle \Psi | = (| \Psi \rangle^*)^T
{% end %}

Taking the inner product of a ket-vector and its adjoint (associated bra-vector) is then just a modified version of the regular dot product:

{% math() %}
\langle \Psi | \cdot | \Psi \rangle = \langle \Psi | \Psi \rangle = 
\begin{pmatrix}
\Psi_1 \\ \Psi_2 \\ \Psi_3 \\ \vdots \\ \Psi_n
\end{pmatrix}
\begin{pmatrix}
\Psi_1^* \quad \Psi_2^* \quad \Psi_3^* ~ \dots ~ \Psi_n^*
\end{pmatrix}
{% end %}

> Just like regular dot products, inner products in quantum mechanics are associative - $\langle A | B \rangle = \langle B | A \rangle$

Quantum state-vectors are also _normalized_, which means that their magnitude is equal to one. This means that the dot product of a quantum state-vector with its respective ket-vector is equal to one (from the dot product property $A \cdot A = \|A\|^2$):

{% math() %}
\langle \Psi | \Psi \rangle = 1
{% end %}

Since we end up with a bra next to a ket, we now have a "bra-ket" - a _bracket_, a physics pun by Dirac. And yes, that is why we call them bra-vectors and ket-vectors!

There is one other important property of inner products to mention, which carries over from dot products in classical mechanics. Recall how the Cartesian basis vectors $\hat i, \hat j, \hat k$ used in normal 3D space are _mutually orthogonal_ (perpendicular to each other). That means taking the dot product of any basis vector with another basis vector returns zero:

{% math() %}
\hat i \cdot \hat j = \hat j \cdot \hat k = \hat i \cdot \hat k = 0
{% end %}

In addition, the Cartesian basis vectors are _normalized_, which means that they each have unit magnitude, so:

{% math() %}
\hat i \cdot \hat i = \hat j \cdot \hat j = \hat k \cdot \hat k = 1
{% end %}

In quantum mechanics, any set of basis vectors must also be mutually orthogonal and normalized. The combination of basis vectors that have unit magnitude and orthogonality has a technical name: an **orthonormal basis**.

Now we are ready to proceed to find a useful representation of state-vectors. We start by taking the dot product of a quantum state-vector with a position basis bra-vector $\langle x |$. In Dirac notation, we write this as:

{% math() %}
\langle x | \Psi \rangle
{% end %}

We expand out $| \Psi \rangle$ using its superposition form, using position basis vectors:

{% math() %}
\langle x | \Psi \rangle = \langle x | \sum_{i = 1}^n \Psi_i | x_i \rangle
{% end %}

Which, if we write component-by-component, becomes:

{% math() %}
\langle x | \Psi \rangle = \langle x | \Psi_1 | x_1 \rangle + \langle x | \Psi_2 | x_2 \rangle + \langle x | \Psi_3 | x_3 \rangle + \dots + \langle x | \Psi_i | x_i \rangle
{% end %}

This is where you get to blame Paul Dirac for inventing a notation so terse as to be incredibly confusing. Remember that the $\Psi_i$'s are the components, whereas $\langle x|$ and the $| x_i \rangle$'s are the position basis bras and kets. Inner products, like dot products, are linear: you can factor any constant coefficients out, and it won't affect the calculation. So let's do that now:

{% math() %}
\langle x | \Psi \rangle = \Psi_1 \langle x | x_1 \rangle + \Psi_2 \langle x | x_2 \rangle + \Psi_3 \langle x | x_3 \rangle + \dots + \Psi_i \langle x | x_i \rangle
{% end %}

Remember that basis vectors in quantum mechanics are **orthonormal**. This means that $\langle x | x_i \rangle = 0$, unless $x_i = x$, in which case the dot product returns one. This is a very abstract mathematical argument, so let me rephrase this with plainer language: given any random position basis bra-vector, say $\langle x | = \langle x_3 |$, taking its inner product with itself $\langle x_3 | x_3 \rangle = 1$, while taking its inner product with **any other position basis ket-vector** will equal zero. In practical terms, we can satisfyingly cancel out nearly every term in the superposition, giving:

{% math() %}
\langle x | \Psi \rangle = \cancel{\Psi_1 \langle x | x_1 \rangle} + \cancel{\Psi_2 \langle x | x_2 \rangle} + \cancel{\Psi_3 \langle x | x_3 \rangle + \dots} + \Psi_i \cancel{\langle x | x_i} \rangle^1 = \Psi_i
{% end %}

So we have found a way to extract the components of the state-vector!

{% math() %}
\langle x | \Psi \rangle = \Psi_i
{% end %}

The collection of components of the state-vector we've found here is in the position basis, because we used position basis vectors. Index notation is quite compact; $\Psi_i$ is actually a collection of _infinitely_ many complex numbers, each of which is a complex-valued coefficient for a given position state at every position in space $x$. That is:

{% math() %}
\Psi_i = \begin{pmatrix}
\Psi_1 \\ \Psi_2 \\ \Psi_3 \\ \Psi_4 \\ \vdots \\ \Psi_n
\end{pmatrix}
{% end %}

What else assigns a complex number to every position in space? A function! We can interpret $\Psi_i$ as a complex-valued function of $x$, which we will call $\psi(x)$:

{% math() %}
\Psi_i = \langle x | \Psi \rangle = \psi(x)
{% end %}

We call $\psi(x)$ by a special name - a **wavefunction**. In general, the wavefunction also depends on time, so $\psi = \psi(x, t)$. Just like the relation $P = \Psi_i \Psi_i^*$ we found before, we can write:

{% math() %}
\rho = \psi(x, t) \psi^*(x, t)
{% end %}

Note that $\rho$ here is the probability _density_, that is, the probability per unit volume, not the probability itself. This is to ensure that the probability of a particle to be somewhere over all space is 100% (because the particle must exist and be _somewhere_). Put mathematically:

{% math() %}
P = \int_{-\infty}^\infty \rho(x)~dx = \int_{-\infty}^\infty \psi(x, t) \psi^*(x, t)~dx = 1
{% end %}

Or, if we are analyzing a system in 3 dimensions rather than just 1, we would have:

{% math() %}
P = \int_{-\infty}^\infty \int_{-\infty}^\infty \int_{-\infty}^\infty \rho(x)dx,dy,dz = \int_{-\infty}^\infty \psi(x, t) \psi^*(x, t)~dx\,dy\,dz = 1
{% end %}

In addition, the complex-valued outputs of $\psi(x, t)$ are more correctly called **probability amplitudes** - we referred to these equivalently as _probability coefficients_ earlier. Thus the Schrödinger wave equation simplifies to something far more familiar, a partial differential equation:

{% math() %}
i\hbar \frac{\partial}{\partial t} \psi(x, t) = \left(-\frac{\hbar^2}{2m} \frac{\partial^2}{\partial x^2} + V(x, t)\right) \psi(x, t) 
{% end %}

 The physical interpretation of the Schrödinger equation is that all quantum particles (such as electrons, quarks, etc.) have wave-like properties as well as particle-like properties, and their wave nature is associated with the wavefunction $\psi(x, t)$. This allows them to exhibit effects such as wave interference and diffraction, as well as to have an associated wavelength and frequency. However, quantum particles are localized on measurement, like classical particles, and this is due to the fact that the wavefunction is associated with particle probability distributions. This fact is known as **wave-particle duality**.

But in addition to its physical significance, the Schrödinger equation expressed in terms of wavefunctions also provides a systematic process of actually doing calculations. Rather than working with Hilbert spaces and abstract vectors represented as superpositions, we simply need to solve a PDE for the wavefunction, or at worst, plug it into a computer to solve. From the wavefunction, we can calculate the probability density $\rho(x, t) = \psi(x, t) \psi^*(x, t)$ to find the probability of the quantum system taking a particular position state. In other words, we will be able to predict, with perfect certainty, the likelihood a quantum particle is present at a particular location.

And it is not only the probabilities of positions that we are able to calculate. Recall that while we chose the position basis for the wavefunction, there is no reason why we are restricted to just the position basis. We can define a wavefunction in any orthonormal basis we would like in quantum mechanics, so wavefunctions that are a function of momentum (or any other continuous basis) are also perfectly valid:

{% math() %}
\psi(x) = \langle x | \Psi \rangle \Rightarrow \psi(p) = \langle p | \Psi \rangle 
{% end %}

### Postulate 4: measurements and eigenvalues

 Up to this point, we have learned what quantum state-vectors are, how they can be represented in a particular basis as a wavefunction, and how operators act on state-vectors. Now is the time to finally begin to understand what happens when we take a measurement.

 First, recall that physical observables such as momentum and position take the form of operators that act on a quantum state-vector $| \Psi \rangle$. Usually, an operator applied to a state-vector results in a new state-vector completely different from the first. But sometimes, that operator outputs a new state-vector that is a constant multiple of the first. In this case we can write:

 {% math() %}
 \hat M | \Psi \rangle = a | \Psi \rangle
 {% end %}

 This is called an **eigenvalue equation**, where $a$, the constant multiple, is called the **eigenvalue**, and the state-vector $| \Psi \rangle$ that satisfies the equation is called the **eigenvector**. Eigenvectors that are infinite and continuous are also called _eigenfunctions_, because (as we learned earlier) functions are essentially just vectors with an infinite number of components. 

 As a more concrete example, consider the differentiation operator $\frac{d}{dx}$ applied to the function $f(x) = e^{kx}$. Then we end up with an eigenvalue equation where $k$ is the eigenvalue and $f(x)$ is the eigenfunction:

 {% math() %}
 \frac{d}{dx} f(x) = \frac{d}{dx} (e^{kx}) = ke^{kx} = k \cdot f(x) \Rightarrow \frac{d}{dx} f(x) = k f(x)
 {% end %}

 Now, this is the key: in quantum mechanics, the eigenvectors of any operator **must** form a set of orthonormal basis vectors for the state-vector $| \Psi \rangle$. That's a lot to unpack, so let's take it bit by bit. Consider the $\hat p$ momentum operator. Its eigenvectors $|p_1 \rangle, |p_2 \rangle, |p_3 \rangle, \dots |p_i \rangle$ correspond to states of having momenta $p_1, p_2, p_3$, and so on, and thus are often called momentum _eigenstates_. These momentum eigenstates are the basis vectors that we can use to express the superposition form of the state-vector $|\Psi \rangle$:

 {% math() %}
 | \Psi \rangle = \Psi_1 | p_1 \rangle + \Psi_2 | p_2 \rangle + \dots + \Psi_i | p_i \rangle
 {% end %}

 The possible measured values of the momentum are the eigenvalues $p_1, p_2, p_3$ and so on, and the momentum can _only_ be one of these eigenvalues. This satisfies the requirement that physical quantities be _quantized_. While the exact value of the momentum can jump randomly between the momentum eigenvalues, the average value (denoted $\langle p \rangle$) found after many measurements follows the rule:

 {% math() %}
 \langle p \rangle = \langle \Psi | \hat p | \Psi \rangle
 {% end %}

 Where this notation means that we _apply_ $\hat p$ to the state-vector ket, then take the result's inner product with the state-vector bra. Using the (position basis) wavefunction representation for clarity, we can rewrite this as:

 {% math() %}
 \langle p \rangle = \int_{-\infty}^\infty \psi^*(x, t) \hat p\, \psi(x, t)~dx
 {% end %}

 Where from the operator table earlier, we know that:

 {% math() %}
 \hat p = -i\hbar \frac{\partial}{\partial x}
 {% end %}

 This is called the **expectation value of the momentum**, and is one case of the more general formula for the expectation values of an operator $\hat A$ in quantum mechanics:

 {% math() %}
 \langle A \rangle = \langle \Psi | \hat A | \Psi \rangle = \int_{-\infty}^\infty \psi^*(x, t) \hat A \psi(x, t)~dx
 {% end %}

### Postulate 5: the Born rule and probabilities

 We have gone in-depth about quantum state-vectors and their representations as wavefunctions. But for all their fundamental relevance in quantum mechanics, state-vectors are complex-valued and can never be directly measured, because measurements are always real numbers. How do we get a real-valued measurement out of a complex-valued state-vector? This is where the **Born rule** applies.

 Consider a quantum particle with state-vector $|\Psi\rangle$. Recall that expressing its state-vector in the position basis gives the position wavefunction $\psi(x) = \langle x | \Psi \rangle$.

 Before we measure the particle, the wavefunction evolves naturally by the Schrödinger equation, which we can solve with the help of a math wizard or unwillingly-recruited professor. But now we want to measure the particle. This is a bit of a problem, because to measure a quantum particle involves causing it to interact with _something_, such as a photon that encounters it or the electron of an atom in our detector. So all quantum measurements are indirect; essentially, using one quantum system to learn information about another system. This also means that all quantum measurements are _disruptive_: on quantum scales, anything you use to measure with will disturb the system you measure.

> How do particles know they are being observed? Because the act of observation involves detecting changes in another particle that interacts with (and disturbs) the particle being measured.

 So it's not actually that unintuitive that we don't know where a particle is or what its properties are until we observe it. Taking a measurement, even in very careful conditions with very sensitive equipment, will alter the system in some way - a change that will make it impossible to reconstruct the previous state of the particle from its current state. Even light disturbs a system, "seeing" a quantum particle like an electron is only possible through bouncing a photon at that electron, and that interaction fundamentally changes the state of the electron. Naturally, we can't know everything with perfect detail when all the information we can find about any quantum particle will require doing something that also affects their properties.

 But let's say that with some apparatus, we have managed to make a measurement of some physical quantity. What happens now? We know from the previous section on eigenvalues and measurement that the measurement must result in some value that is an eigenvalue of the operator associated with that physical quantity. For instance, if we take a measurement of the momentum $\hat p$, then the result is going to be an eigenvalue of the momentum operator $\hat p$. But which exact eigenvalue? **We can't know.** As far as we understand, quantum mechanics is probabilistic and no certain measurements can be made, only statistical likelihoods of a particular measurement. And the probability of measuring an eigenvalue $\alpha$ associated with the eigenstate $\langle \alpha |$ of an operator is given by the **Born rule**:

 {% math() %}
P = |\langle \alpha | \Psi \rangle|^2
 {% end %}

> And yes, we are using an abuse of terminology, technically it is the inner product of the adjoint of the eigenvector (remember: complex conjugate transpose) and the state-vector.

 For any operator that has _continuous_ eigenstates, such as position and momentum, we can equivalently rewrite the Born rule in terms of the probability density $P$ and wavefunction $\psi(x)$:

 {% math() %}
 P = |\psi(\alpha)|^2 = \psi(\alpha) \psi^*(\alpha)
 {% end %}

 And this is the physical interpretation of what seemed like a math trick to represent the quantum state as a wavefunction - a wavefunction is actually a collection of infinitely-many eigenvalues of an operator with continuous eigenstates, such as the eigenvalues of the position and momentum operators. _This_ is why it makes sense that you can extract the probability of a certain measurement from the wavefunction. More accurately, you can extract the probability _density_ from the wavefunction, and then integrate to find the probability of a certain range of measurements:

 {% math() %}
 \text{Prob} = \int_{\alpha_1}^{\alpha_2} |\psi(\alpha)|^2 d\alpha = \int_{\alpha_1}^{\alpha_2} \psi(\alpha) \psi^*(\alpha) d\alpha 
 {% end %}

 At the moment where that measurement is performed, the wavefunction jumps to a single spike at one of its eigenvalues, which gives us the measured value; after the measurement is done, the wavefunction continues to evolve by the Schrödinger equation. However, if we take measurements in quick succession, the wavefunction does not have much time to evolve before another measurement is taken, so the result of the measurement will be the same. If we give more time to let the wavefunction evolve, then the measurements no longer yield the same results and return to being random, although they will always follow the Born rule of probabilities. Together with the rule of expectation values, the Born rule requires that quantum mechanics reproduce the results of classical mechanics at the classical limit, in which probabilities of measurements become certain measurements.

 In other words, the Born rule allows a physicist making theoretical predictions about a quantum particle to say "the particle is _most likely_ at $x$" or "the particle is relatively likely (or unlikely) to be somewhere between $x_1$ or $x_2$" or "the particle has a 60% likelihood of having energy $E$", but _not_ "the particle is definitely at $x$". Only after measurement can a definite value be found for an observable.

 However - if only it were so simple! There is an additional issue when considering certain operators that places a restriction on how accurately we can even make probability predictions. To understand it, consider the example of the position and momentum operators. From the table of operators (or Wikipedia) we know that they are respectively:

 {% math() %}
 \hat x = x, \quad \hat p = -i\hbar \frac{\partial}{\partial x}
 {% end %}

 Something interesting happens when we apply the operators in different orders to a wavefunction. Applying the momentum operator first, and then the position operator, gives:

 {% math() %}
 \hat x \hat p \psi(x) = -i\hbar x \frac{\partial \psi}{\partial x}
 {% end %}

 But if we apply the operators in the opposite order, such that we apply the position operator first, and then the momentum operator, we have:

 {% math() %}
 \hat p \hat x \psi(x) = -i\hbar \frac{\partial}{\partial x} (x \psi(x)) = -i\hbar \left(\psi(x) + x\frac{\partial \psi}{\partial x}\right) 
 {% end %}

 These are not the same, and the difference between them is given by:

 {% math() %}
 \hat x \hat p \psi(x) - \hat p \hat x \psi(x) = i\hbar \psi(x)
 {% end %}

 We can express that difference as a new operator, the **commutator**, applied to the wavefunction, which we denote with square brackets $[\hat x, \hat p]$:

 {% math() %}
 [\hat x, \hat p] = \hat x \hat p - \hat p \hat x = i\hbar \Rightarrow [\hat x, \hat p] \psi(x) = i\hbar \psi(x)
 {% end %}

 This is the famous **canonical commutation relation** $[\hat x, \hat p] = i\hbar$. There are other commutation relations but this is the most important one to encounter in studying quantum physics.

 What is the relevance of commutation? From the requirements of probability theory (read about the Cauchy-Schwarz inequality if interested), commuting operators must obey the general uncertainty principle:

> Given two commutating operators $\hat A$ and $\hat B$, the values of their eigenvalues cannot both be precisely measured. The more precise you want to measure an eigenvalue of $\hat A$, the less precise you can measure an eigenvalue of $\hat B$.

 A famous example is the uncertainty relation between $\hat x$ and $\hat p$, one that we have already seen earlier - the Heisenberg uncertainty principle:

 {% math() %}
 \Delta x \Delta p \geq \frac{\hbar}{2}
 {% end %}

## The fundamental postulates of quantum mechanics

To summarize what we've covered, we can distill the theory of quantum mechanics into these fundamental _mathematical_ postulates:

1. A quantum system is completely described by a **quantum state** $|\Psi\rangle$, also represented by $\psi(x) \equiv \Psi(x, 0)$, which is a complex-valued vector in a Hilbert space.
	- A state describes a quantum particle at a particular instant in terms of its probability distribution. 
	- Further, a state also evolves through time by the Schrödinger equation $i\hbar \dfrac{\partial}{\partial t} |\Psi(t)\rangle = \hat H |\Psi(t)\rangle$, which we may represent by $|\Psi(t)\rangle$ or $\Psi(x, t)$.
2. A quantum state is a superposition of all possible eigenstates of the system, that is, $|\Psi \rangle = \displaystyle \sum_i C_i |\varphi_i \rangle$.
3. Physical quantities are known as **observables**, and are represented by linear operators acting on the quantum state. For instance, $\hat x = x, \hat p = -i\hbar \nabla, \hat H = -\frac{\hbar^2}{2m} \nabla^2 + V$.
4. Applying an observable results in an eigenvalue equation to solve in the form $\hat A |\varphi_i\rangle = A |\varphi_i\rangle$, where $A$ is the eigenvalue and $|\varphi_i\rangle$ is the eigenstate. The *eigenvalues* of each observable correspond to *possible values* of the associated physical quantity (e.g. position, momentum, energy). The eigenvalues can be quantized or continuous. Each eigenvalue is associated with an eigenstate of the system.
6. It is **not possible** to predict in advance the measured value a physical quantity may take. However, it is possible to predict the *probability* $P$ of a particular eigenstate $|\varphi_i\rangle$ through the Born rule $P= |\langle \varphi_i| \Psi\rangle |^2 = |C_i|^2$
7. We may use the _wave formulation_ or _matrix formulation_ to obtain the same results, and the two are completely equivalnet:
	- In the **wave formulation**, we have $\psi(x)$ as a quantum state, represented as a time-indepedent wavefunction, $\varphi_i(x)$ as a component eigenstate, and $\Psi(x, t) = \psi(x) e^{-iE t/\hbar}$ as the general wavefunction
	- In the **matrix-vector formulation**, we have $|\Psi\rangle$ as a quantum state, $|\varphi_i\rangle$ as a component eigenstate, and $|\Psi(t)\rangle$ as the general time-evolving state

## The classical limit of quantum mechanics

Quantum mechanics is the most comprehensive theory of physics ever devised, because it governs the mechanics of everything in the universe. In practice, however, quantum calculations are often so involved that we only apply quantum mechanics to systems where quantum effects deviate significantly from classical behavior. In fact, any calculations with macroscopic objects that treat them as larger versions of idealized quantum systems quickly become intractable. This is because they are composed of many billions of subatomic particles, and a combination of advanced methods in quantum mechanics and statistical physics is often necessary to sufficiently describe them. See [this Physics SE post](https://physics.stackexchange.com/questions/567596/is-quantum-mechanics-applicable-to-only-small-things) for more details.

To understand where quantum mechanics can be sufficiently well-approximated by quantum mechanics, we turn to the _correspondence principle_. This says that quantum mechanics reproduces the results of classical mechanics _on average_.

So as a takeaway, quantum mechanics is conventionally only _required_ for analyzing systems smaller than an atom, but below that limit, many things simply cannot be explained classically. We can (and should) use the classical theory for all scales above the atomic scale; we must use quantum for anything below.

### Ehrenfest's theorem

How quantum mechanics reduces to classical mechanics is given by **Ehrenfest's theorem**. To understand the theorem, let us start with the standard quantum Hamiltonian:

{% math() %}
\hat H = \dfrac{\hat p^2}{2m} + V(x)
{% end %}

Ehrenfest's theorem relies on the fact that physical time-independent operators obey what's known as the **Heisenberg equation of motion** (which comes from their mathematical properties), given by:

{% math() %}
\dfrac{d\hat A}{dt} = \dfrac{i}{\hbar} [\hat H, \hat A]
{% end %}

This also means that the _expectation values_ of the Heisenberg equations of motion satisfy:

{% math() %}
\dfrac{d\langle A\rangle}{dt} = \dfrac{i}{\hbar} \langle[\hat H, \hat A]\rangle
{% end %}

One particularly interesting case is when $\hat A = \hat p$, the momentum operator. Then, its commutator with the Hamiltonian becomes:

{% math() %}
\begin{align*}
[\hat H, \hat p]\psi &= (\hat H \hat p - \hat p \hat H)\psi \\
&= \left[-\dfrac{\hbar^2}{2m} \hat p^2 + V(x)\hat p - \hat p\left(-\dfrac{\hbar^2}{2m} \hat p^2 + V(x)\right)\right]\psi \\
&= -\dfrac{\hbar^2}{2m}\hat p^2 \hat p \psi + V (x)\hat p \psi +\dfrac{\hbar^2}{2m}\hat p \hat p^2 \psi - \hat p (V(x) \psi) \\
&= -\dfrac{\hbar^2}{2m}\hat p^2 \hat p \psi + V (x)\hat p \psi +\dfrac{\hbar^2}{2m}\hat p \hat p^2 \psi - \hat p (V(x) \psi) \\
&= -\dfrac{\hbar^2}{2m}\hat p^3 \psi + V (x)\hat p \psi +\dfrac{\hbar^2}{2m}\hat p^3 \psi - \underbrace{(\hat p V(x) \psi + V(x)\hat p \psi)}_\text{product rule}) \\
&= \cancel{-\dfrac{\hbar^2}{2m}\hat p^3 \psi} + \cancel{V (x)\hat p \psi} + \cancel{\dfrac{\hbar^2}{2m}\hat p^3 \psi} - (\hat p V(x) \psi - \cancel{V(x)\hat p \psi)}) \\
&= -\hat p V(x) \psi \\
&= i\hbar \dfrac{\partial V}{\partial x} \psi
\end{align*}
{% end %}

Thus we see that:

{% math() %}
\begin{gather*}
[\hat H, \hat p]\psi = i\hbar \dfrac{\partial V}{\partial x} \psi \\
\Rightarrow [\hat H, \hat p] = i\hbar \dfrac{\partial V}{\partial x}
\end{gather*}
{% end %}

Now, if we substitute this result into the Heisenberg equation of motion, we have:

{% math() %}
\begin{align*}
\dfrac{d\langle p\rangle}{dt} &= \dfrac{i}{\hbar} \langle[\hat H, \hat p]\rangle \\
&= \dfrac{i}{\hbar} \left\langle i\hbar \dfrac{\partial V}{\partial x} \right\rangle \\
&= -\left\langle \dfrac{\partial V}{\partial x} \right\rangle
\end{align*}
{% end %}

But remember, in classical mechanics, $\dfrac{dp}{dt}$ is the force, and Newton's second law is simply $F = \dfrac{dp}{dt} = -V'(x)$! So we have reproduced something that looks very _similar_ (though not identical) to Newton's second law:

{% math() %}
\dfrac{d\langle p\rangle}{dt} = -\left\langle \dfrac{\partial V}{\partial x} \right\rangle
{% end %}

We can follow the same process with the position operator $\hat x$ to see that its Heisenberg equation of motion is given by:

{% math() %}
\dfrac{d\langle x\rangle}{dt} = \dfrac{\langle p\rangle}{m}
{% end %}

Which looks very similar to the classical $\dot x = v = p/m$! The two above equations comprise **Ehrenfest's theorem** goes to show that quantum mechanics ultimately reproduces classical mechanics, although its predictions are much more significant at small scales, where classical mechanics fails.

### The general ideas of the classical limit

To go through a full treatment of the classical limit of quantum mechanics would take quite a lot of time and involve a lot of advanced mathematics. However, to get an intuitive idea of how quantum mechanics reproduces classical mechanics, there are a few key ideas:

- The **expectation values** of quantum operators reproduce their respective classical expressions (for instance, $\langle \hat x \rangle \approx x(t)$, $\langle \hat p \rangle \approx p(t), \langle \hat H \rangle \approx E$ and so forth)
- In the limits of large quantum numbers, **quantized values become continuous values**. For instance, consider the $z$-angular momentum operator $\hat L_z$, which has eigenvalues $L_z = m \hbar$, where $m$ is an integer. Since $L_z$ can only come in integer multiples $m \hbar$, the angular momentum of a quantum particle is quantized. However, in the limit as $m$ grows very large (after all, macroscopic objects have huge amounts of angular momenta compared to tiny subatomic particles!), the difference between angular momenta of different integer $m$ become almost negligible. For a rolling marble, which might have $L_z = \pu{1 g m^2/s} \approx \pu{9.48E30}\hbar$, no one would notice the difference between the angular momentum for $L_z = m\hbar = 9.48 \times 10^{30} \hbar$ versus $\tilde L_z = (m + 1)\hbar = 9.480000\dots01 \times 10^{30}\hbar$. This is to say, any macroscopic object has such a huge amount of angular momentum (and thereby such a big value of $m$) that its angular momentum **_appears_ to be continuous**
- **Probability amplitudes for large objects** are such that the state that matches classical behavior is _overwhelmingly_ the most likely state, and such that the time-evolution of a system follows classical laws. (This is especially evident in the [path integral formulation of quantum mechanics](https://www.quantamagazine.org/how-our-reality-may-be-a-sum-of-all-possible-realities-20230206/) but we won't go into that here)
- The **de Broglie wavelength** grows _extremely small_ for large objects, meaning that the wavelike properties of quantum particle vanish, and objects become well-approximated by discrete point particles (or systems of infinitely many point particles for continuum objects)

## A brief peek at more advanced quantum mechanics

Up to this point, we have considered quantum mechanics primarily using the Schrödinger equation as well as working with pure quantum states. There are more advanced derivatives of the Schrödinger equation that incorporate the effects of relativity and spin in their description of quantum particles. First, we have the Klein-Gordon equation:

{% math() %}
\left(\partial_\mu \partial^\mu \psi + \dfrac{m^2 c^2}{\hbar^2}\right) \psi = 0
{% end %}

The Klein-Gordon equation describes spinless elementary particles, like the Higgs boson, and certain spinless composite particles, such as mesons and pions. But for fermions - including quarks, electrons, and muons - we use the **Dirac equation**, which is a four-component PDE often written in condensed form as:

{% math() %}
(i\hbar \gamma^\mu \partial_\mu - m c) \psi = 0
{% end %}

We can expand it to show it as a system of equations for a four-component wavefunction $\psi$, where:

{% math() %}
\psi = \begin{pmatrix} \psi_1 \\ \psi_2 \\ \psi_3 \\ \psi_4 \end{pmatrix}, \quad
\begin{align*}
i\hbar \frac{\partial}{\partial t} \psi_1 - \frac{\partial}{\partial x} \psi_3 + \frac{\partial}{\partial y} \psi_4 - \frac{\partial}{\partial z} \psi_3 - mc \psi_1 &= 0, \\
i\hbar \frac{\partial}{\partial t} \psi_2 - \frac{\partial}{\partial x} \psi_4 - \frac{\partial}{\partial y} \psi_3 + \frac{\partial}{\partial z} \psi_4 - mc \psi_2 &= 0, \\
i\hbar \frac{\partial}{\partial t} \psi_3 + \frac{\partial}{\partial x} \psi_1 + \frac{\partial}{\partial y} \psi_2 + \frac{\partial}{\partial z} \psi_1 - mc \psi_3 &= 0, \\
i\hbar \frac{\partial}{\partial t} \psi_4 + \frac{\partial}{\partial x} \psi_2 - \frac{\partial}{\partial y} \psi_1 + \frac{\partial}{\partial z} \psi_2 - mc \psi_4 &= 0.
\end{align*}
{% end %}

> **Note:** in gauge field theory and specifically quantum electrodynamics, which is discussed at the end of the [electromagnetic theory article](@/electromagnetism/index.md), we find that the Dirac equation describing fermions coupled to an electromagnetic field (i.e. electrons) must be modified to $(i\hbar \gamma^\mu D_\mu - m c) \psi$, where $D_\mu = \partial_\mu + \dfrac{ie}{\hbar c} A_\mu$ is the **gauge covariant derivative**.

The most precise theory of quantum mechanics is the **Standard Model**, which extends the Dirac equation into describing **quantum fields**. The Standard Model makes highly-accurate predictions that are even more precise than the Schrödinger equation, including tiny corrections to the energy levels of the hydrogen atom. However, it is a theory that is far too complex to cover here and best left to an in-depth textbook treatment. For those interested, feel free to see my [quantum field theory book](https://www.learntheoreticalphysics.com/quantum-field-theory/) to learn more.

### An epistemological remark

Quantum mechanics is perhaps one of the most profoundly impactful and _useful_ theories of physics ever devised. Its uses are numerous and essentially anything to do with microscopic processes - for instance, semiconductors, diodes, superconductors, atomic spectroscopy, nuclear technologies, quantum optics, lasers, scanning electron microscopy, quantum chemistry, and advanced materials research - all involve quantum mechanics in some way. That is to say, quantum mechanics has many _practical applications_.

However, these are essentially all applications of non-relativistic quantum mechanics. Going beyond and into relativistic quantum mechanics becomes more and more the realm of purely precision science (except for some applications in condensed matter physics). Elementary particle physics, in particular, does not (yet) have many day-to-day applications, other than simply advancing our understanding of physics and science. It is motivated purely by human curiosity and the pursuit of pushing the frontiers of science ever further. One day, our civilization may reach the levels of technological development that require relativistic quantum field theory on a regular basis, but this has not come yet. Bearing that in mind, it is nonetheless a fascinating intellectual pursuit, providing us with valuable scientific knowledge to advance our current understanding of science, and worth doing simply by virtue of itself.

## Further reading

Introductory quantum mechanics covers only a tiny part of the much larger landscape of quantum theory. There are _so_ many more things to learn, enough to study for an entire career:

- Applied quantum mechanics to more systems, including many-body systems
- Relativistic quantum mechanics such as the Dirac equation
- Quantum field theory and the standard model
- Quantum cosmology, quantum thermodynamics, and other advanced topics
- Quantum gravity and a possible quantum theory of everything

Some very useful resources are the free courses at MIT OpenCourseWare, the _Theoretical Minimum_ series (and associated YouTube lectures) of Leonard Susskind, the _In a Nutshell_ books by A. Zee, and of course, the standard texts by David Griffiths, namely _Introduction to Quantum Mechanics_ and _Introduction to Elementary Particles_. The quantum world is mysterious - but at the same time, endlessly fascinating, and richly rewarding to learn. 
