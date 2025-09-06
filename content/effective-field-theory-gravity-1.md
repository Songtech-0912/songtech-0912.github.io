+++
title = "Gravity as an effective field theory, part 1"
date = 2025-09-06

[extra]
non_note = true
+++

**Abstract.** Effective field theory is an idea that comes from [quantum field theory](https://learntheoreticalphysics.com/quantum-field-theory/), and forms the backbone of the Standard Model. The core idea of effective field theory is that it gives us an "entry point" to new physics we don't know by assuming that the new physics is hidden behind suppressed high-energy terms; these terms reduce to physics we do know in the low-energy limit. By finding approximate forms for these high-energy terms, we can often successfully make predictions with an incomplete theory. With that in mind, effective field theory is very often discussed purely in the context of quantum field theory, even though it is a far more general idea. In this article, I'll discuss the interesting examples of treating Newtonian gravity and General Relativity as effective field theories, and how it fits in with our currently incomplete _quantum_ theory of gravity.

<!-- more -->

## Newtonian gravity as an effective field theory

I will begin with this claim: _Newtonian gravity is an effective field theory in disguise_. However, before we proceed to show that this is the case, let's first forget most of the things we typically associate with Newtonian gravity: no inverse-square law, no vectors, no free-fall or projectile motion. Instead, we'll start with the fundamental building block of all field theories: a **field**. To treat gravity as a field theory, we must define some field (let's denote it $\Phi$) associated with gravity. Since fields are functions of position, it must be the case that $\Phi = \Phi(\mathbf{r})$ (though here we'll use the shorthand $\Phi(r)$ for simplicity). Let's also call $\Phi$ the **gravitational potential** - again, let's forget about potential energy and just treat "gravitational potential" as a convenient name for our field for gravity.

I will now make the claim that by starting with only three primary assumptions, which can all be derived from observation, we can reconstruct the theory of Newtonian gravity from scratch. These assumptions are:

1. Gravity is characterized by the gravitational constant $G$, which controls the strength of gravitational interactions.
2. The strength of the gravitational force decreases with distance. In mathematical terms, this means that the gravitational potential $\Phi$ must be constructed from terms proportional to $r^{-n}$, where $n$ is a positive nonzero integer. This should be trivial, since if gravity was constant or increased with distance, orbiting bodies would spontaneously accelerate away from each other, which of course doesn't happen.
3. The effects of gravity are only apparent for massive astronomical bodies like planets and stars, meaning that $G$ must be very small in magnitude. We know from experiments that $G \sim 10^{-11}$, but this is actually not necessary to know; the only requirement for this assumption is that $G \ll 1$.

> **Note:** Assumption (1) can be justified by noting that all the fundamental interactions of nature have characteristic constants (the fine-structure constant $\alpha$ for electromagnetism, the strong coupling constant $g_s$ for the strong force, and so forth). Also, we do assume Newton's second law (and other basic physics) applies to gravity, which technically counts as a fourth (implicit) assumption.

With these assumptions, we can already write down the general form of the gravitational potential as a series expansion involving $G$:

{% math() %}
\Phi(r) = -\left[\dfrac{a_1 G}{r} + \dfrac{a_2 G}{r^2} + \dfrac{a_3 G}{r^3} + \dots\right]
{% end %}

Where $a_1, a_2, a_3$ are constants, and where we pick an overall negative sign because we observe that gravity is an attractive force (after all, apples don't exactly fall towards the sky!). Since gravity depends on mass, it is also easy to define constants $b_1, b_2, b_3$, where $a_n = b_n M$ to include the effect of mass. Thus we have:

{% math() %}
\Phi(r) = -\left[\dfrac{b_1 GM}{r} + \dfrac{b_2 GM}{r^2} + \dfrac{b_3 GM}{r^3} + \dots\right]
{% end %}

To ensure that the potential reduces to Newtonian gravity, we pick $b_1 = 1$, so that the zeroeth-order term of the potential becomes the familiar potential $\Phi(r) = -\dfrac{GM}{r}$. But what about the higher-order terms? The answer comes from the observation that $G$ is already a very small number, and the $r^{-n}$ dependence of the terms means that gravity rapidly decreases with distance. This means that the $r^{-3}$ term is suppressed (near-zero) for all but very strong gravitational fields. This is important because we'd expect General Relativity to be the correct theory of gravity in the strong-field regime, and thus the $b_3$ term is suppressed in weak fields (as in Newtonian gravity) and only becomes relevant in GR. Thus, Newtonian gravity is the _effective field theory_ of gravity, since whenever we have $b_3 \ll 1$ (corresponding to weak gravitational fields) all terms above first-order vanish, reducing to:

{% math() %}
\Phi_\text{Newtonian}(r) = -\left[\dfrac{ GM}{r} + \dfrac{b_2 GM}{r^2}\right]
{% end %}

If we consider the case of approximately-circular orbits, with a smaller body of mass $m$ orbiting the central body of mass $M$, the correct expression for the (effective) potential in Newtonian gravity is given by:

{% math() %}
\begin{align*}
\Phi_\text{Newtonian}(r) &= -\left[\dfrac{GM}{r} - \dfrac{L^2}{2m^2r^2}\right], \quad L^2 \approx GMm^2 R \\
&\approx -\left[\dfrac{GM}{r} - \dfrac{GMR}{2r^2}\right]
\end{align*}
{% end %}

From which we may conclude that $b_2 \approx -\dfrac{R}{2}$, where $R$ is the radius of the central body. This proves that indeed, our expansion is justified. Furthermore, we can derive it with some basic heuristic arguments. First, since the zeroeth-order term of the potential $-GM/r$ is strictly negative and inversely-proportional to distance, a purely $-1/r$ potential would lead to orbital decay and eventually impact for _all orbiting bodies_, meaning that the Moon would crash into the Earth and the Earth would crash into the Sun (you can show this if you work out the equations of motion using Newton's 2nd law $F \equiv m \ddot r = -m\frac{d\Phi}{dr}$). Thus, the first-order term must have a positive sign to counteract orbital decay so that stable orbits are possible (which thankfully they are!). Second, dimensional analysis tells us that we need a factor with units of length so that the units match up. Our relevant constants are $G, M, R, m$, but since $GM$ is already taken in the expansion and we observe that the gravitational force is independent of the mass of the orbiting body (at least when $m \ll M$), the only constant left is $R$. Thus we have now found that $b_2 \propto +R$; the factor of 1/2 can then be determined by finding the equilibrium points of the potential, and demanding that the (only) stable equilibrium be located at the distance that matches observations (for instance, the distance of the Moon from Earth). While this may sound extremely tedious, notice how our results came from _minimal knowledge_ of Newton's theory of gravity and came primarily from heuristics, yet reproduced the same exact formula. This is the power of effective field theory!

In fact, you may already be using an effective field theory without knowing! Consider the well-known linear approximation for Newtonian gravity, which is given by $F_g = -m|g|$. It comes as a result of $1/r \approx 1/(R+y) - 1/R$, where $R$ is the radius of the central body and $y$ is a small displacement off the surface of the body. Using the approximation $y \ll R$, the potential becomes approximately linear, as shown:

{% math() %}
\begin{align*}
\Phi(r) &\approx -\dfrac{b_1 GM}{r} \\
&\approx - b_1 GM\left[\dfrac{1}{R+y} - \dfrac{1}{R}\right] \\
&= -b_1 GM\left[\dfrac{R - (R + y)}{R(R + y)}\right] \\
&\approx (-b_1 GM)\dfrac{-y}{R^2} \\
&= b_1 |g|y, \quad g \equiv \dfrac{GM}{R^2}
\end{align*}
{% end %}

Thus, using $F = -mV'(r) = -m\dfrac{dV}{dy}$ we recover the expression $F_g = -b_1 m|g|$, where a simple tabletop experiment like those done by Mr. Galilei can trivially determine that $b_1 = 1$. It is natural to conclude that a linear potential is a good short-distance approximation to the Newtonian potential, which itself is a weak-field approximation to the GR potential. As a summary:

| Domain of validity               | Form of $\Phi$                                                                 |
| -------------------------------- | ------------------------------------------------------------------------------ |
| Weak-field, short-distance       | $\Phi \propto gy$ (linear)                                                     |
| Weak-field, long-distance        | $\Phi \propto b_1 r^{-1} + b_2 r^{-2}$ (inverse quadratic correction)          |
| Fully relativistic, strong-field | $\Phi \propto b_1 r^{-1} + b_2 r^{-2} + b_3 r^{-3}$ (inverse cubic correction) |

Again, _all of this_ came without nearly any information about Newtonian celestial mechanics or General Relativity; our results required purely a clever use of effective field theory. What's more, the effective field theory approach allows us to make predictions _without_ needing knowledge of either theory! In fact, even without knowing the explicit form of $b_3$ it is possible to derive the anomalous perihelion precession of Mercury (up to some constant factors). To do so, we assume that the effective potential correctly captures the GR corrections, such that the orbiting body (in this case, Mercury) overall follows the same equation of motion as given by Newton's second law:

{% math() %}
m \ddot r = -m \dfrac{\partial \Phi}{\partial r} \Rightarrow \ddot r = -\dfrac{\partial \Phi}{\partial r}
{% end %}

Now, we assume that the trajectory $r(\theta)$ can be written in the form $r(\theta) = r_0(\theta) + r_p(\theta)$, where $r_p(\theta)$ is a small correction term that modifies the Newtonian orbit to account for the effects of general relativity. Note here that using polar coordinates is justified by the fact that the conservation of angular momentum implies that orbits lie in a 2D plane, so we only need two coordinates ($r$ and $\theta$) to parameterize the orbit. Substituting into our equation of motion, we have:

{% math() %}
\begin{align*}
\ddot r &= \ddot r_0(\theta) + \ddot r_p(\theta) \\
&= -\dfrac{\partial}{\partial r} \left[-\dfrac{GM}{r} + \dfrac{GMR}{2r^2} + \dfrac{b_3 GM}{r^3}\right] \\
&= -\dfrac{\partial}{\partial r} \left[\underbrace{-\dfrac{GM}{(r_0 + r_p)} + \dfrac{GMR}{2(r_0 + r_p)^2}}_\text{Newtonian potential} + \underbrace{\dfrac{b_3 GM}{(r_0 + r_p)^3}}_\text{GR correction}\right]
\end{align*}
{% end %}

Let $r_0(\theta)$ be the solution to the equation of motion according to the **Newtonian potential** (the first two terms in our above potential), for which there is a well-known solution (spoilers: an ellipse in the form $r(\theta) \sim (1 + \cos \theta)^{-1}$). Now, since $r_p(\theta)$ is a small correction term that slightly modifies $r_0(\theta)$, we can assume that it makes a negligible contribution for the zeroeth-order and first-order terms; that is, $(r_0 + r_p)^2 \approx (r_0 + r_p) \approx r_0$. Thus, we have:

{% math() %}
\ddot r_0(\theta) = -\dfrac{\partial}{\partial r} \left[-\dfrac{GM}{r_0(\theta)} + \dfrac{GMR}{2r_0(\theta)^2}\right] \approx -\dfrac{\partial}{\partial r} \left[-\dfrac{GM}{(r_0 + r_p)} + \dfrac{GMR}{2(r_0 + r_p)^2} \right]
{% end %}

Therefore, making the suitable identifications, we can write our equation of motion as:

{% math() %}
\begin{align*}
\ddot r_0(\theta) + \ddot r_p(\theta) &= -\dfrac{\partial}{\partial r} \left[-\dfrac{GM}{(r_0 + r_p)} + \dfrac{GMR}{2(r_0 + r_p)^2} \right] -\dfrac{\partial}{\partial r}\left[\dfrac{b_3 GM}{(r_0 + r_p)^3}\right] \\
&= \ddot r_0(\theta) + \dfrac{b_3(3 GM)}{(r_0 + r_p)^3}
\end{align*}
{% end %}

This gives us a separate equation of motion for $\ddot r_p(\theta)$:

{% math() %}
\ddot r_p(\theta) = \dfrac{b_3(3 GM)}{(r_0 + r_p)^3}
{% end %}

We can simplify this highly-nonlinear differential equation by first using the binomial expansion, which tells us that $(a + b)^3 = a^3 + 3ab(a + b) + b^3$. In this case, since $r_0 \gg r_p$, then $\dfrac{1}{r_0} \ll \dfrac{1}{r_p}$, which we can use to simplify this equation greatly:

{% math() %}
\dfrac{1}{(r_0 + r_p)^3} \approx \dfrac{1}{r_p^3} \quad \Rightarrow \quad \ddot r_p(\theta) \approx \dfrac{b_3(3 GM)}{r_p^3}
{% end %}

We may solve this differential equation with an _ansatz_ (a clever guess). For instance, an appropriate guess could be $r_p(\theta) = C \theta^{-1}$ where $C$ is some constant. Indeed, substitution of this _ansatz_ into the differential equation verifies that this guess is correct:

{% math() %}
\ddot r_p = \dfrac{d^2}{dr^2} \left(\dfrac{C}{\theta}\right) = \dfrac{2C}{\theta^3} \sim \dfrac{1}{r_p^3}
{% end %}

Thus, if we take $2C = b_3(3GM)$, we find that $C = \dfrac{3}{2} b_3 GM$, and that:

{% math() %}
r_p(\theta) = \dfrac{3b_3 GM}{2\theta}
{% end %}

By inverting, we can get $\theta$ as a function of $r_p$:

{% math() %}
\theta = \dfrac{3b_3 GM}{2r_p}
{% end %}

If we assume that the unperturbed orbit is approximately circular of radius $a$ (that is, we let $r_p \approx a$), the total magnitude of the radial displacement is:

{% math() %}
\Delta \theta = \dfrac{3b_3 GM}{2a}
{% end %}

By dimensional analysis, $b_3$ must have factors of inverse speed squared, and since we expect this to be a result that only appears in general relativity (where $c$, the speed of light, is a fundamental quantity) the obvious choice is that $b_3 = k c^{-2}$, where $k$ is some dimensionless constant. Thus, we have:

{% math() %}
\Delta \theta = \dfrac{3k GM}{2c^2a}
{% end %}

Meanwhile, the correct answer for the perihelion precession from General Relativity, assuming that the unperturbed orbits are approximately circular, is given by:

{% math() %}
\Delta \theta = \dfrac{6\pi GM}{c^2 a}
{% end %}

Thus, we find that by identification of $b_3 = 4\pi /c^2$ (or alternately, $k = 4\pi$) we (approximately) reproduce the result of general relativity! Indeed, the true GR effective potential is not that far off - assuming spherical symmetry and the static regime (i.e. Schwarzschild spacetime), it is given by:

{% math() %}
\begin{align*}
\Phi(r) &= -\dfrac{GM}{r} + \dfrac{\ell^2}{2r^2} - \dfrac{GM \ell^2}{c^2 r^3} \\
&= -\dfrac{GM}{r} \left[\left(1 - \dfrac{\ell^2}{2GMr}\right) + \frac{\ell^2}{c^2r^2}\right]
\end{align*}
{% end %}

Where $\ell$ is the angular momentum per unit mass of the orbiting particle (in the non-relativistic limit, $\ell^2 \approx GMR$, where $R$ is the radius of the central body). This means that the true value of $b_3$ is given by $b_3 = \ell^2/c^2$, meaning that while we did correctly calculate the $1/c^2$ dependence, our results are not exact - though it is already quite impressive that our calculation already matches quite closely! Using the same ideas, Poisson's equation in Newtonian gravity $\nabla^2 \Phi = -4\pi G\sigma$ can be modified with nonlinear terms up to quadratic order to serve an approximation to the relativistic Einstein field equations, although the process for doing so is much more complicated. As a heuristic treatment, we would expect the modified Poisson equation to take the form:

{% math() %}
c_1 \nabla^2 \Phi + c_2(\vec r \cdot \nabla \Phi) + c_3(\nabla \Phi)^2 + \dots = -4\pi G\sigma
{% end %}

> **Why quadratic order?** The simple answer is that any terms above quadratic-order are themselves suppressed, as GR is expected to itself be a low-energy limit to a theory of quantum gravity, which we'll explore next.

Of course, our results fall short of actually giving us the _complete_ theory of general relativity. It doesn't tell us that spacetime is curved, that particles follow geodesics, or that the Einstein field equations are the correct equations of motion for gravity (indeed, the best it could tell us is that Poisson's equation for gravity becomes modified with nonlinear terms). Rather than being formulated in tensors and differential geometry, which are foundational to GR, our results come from basic calculus in Euclidean space. But the power of this approach shows: with a bare minimum amount of information about gravity, we were not only able to reconstruct Newtonian gravity from scratch, but even make predictions that align with those of General Relativity!

> **Note:** It is also possible to start with special relativity and first construct a linear theory of gravity much like (linear) electrodynamics; indeed, this gives you a linearized field equation given by $\square h_{\mu \nu} = -2\kappa T_{\mu \nu}$ where $h_{\mu \nu} = g_{\mu \nu} - \eta_{\mu \nu}$ and where $\square = \partial_\nu \partial^\nu$ is the [D'Alembertian operator](https://en.wikipedia.org/wiki/D'Alembertian). Then, nonlinear terms of order $\mathcal{O}((\nabla h)^2)$ (where $h = \eta^{\mu \nu} h_{\mu \nu}$) can be added to reproduce, to an extent, the results of general relativity. This comes with the advantage that the theory is naturally relativistic and thus naturally predicts phenomena like gravitational waves, just like the relativistic Maxwell equations in electrodynamics predict electromagnetic waves. However, the drawback is that it still assumes relatively weak gravitational fields cannot accurately describe strong-field phenomena like black holes.

## A path to quantum gravity?

Having discussed effective field theory applied to gravity, one might think that while the approach shown is quite elegant, it has little use today, given that General Relativity is well-established by this point and we have yet to find any better theory of gravity. However, this is anything but the case, because physicists are still eagerly working on finding a _quantum_ theory of gravity. While we do not have the complete theory yet, we can use the same tricks as prior to obtain an *approximate* theory and perform useful calculations.

As we will now be working in the realm of quantum field theory, we start with an action for gravity. This can again be written in the form of a power series, except this time in powers of the **Ricci scalar** $R$:

{% math() %}
S = \dfrac{1}{2\kappa} \int d^4 x \sqrt{-g} (c_1 R + c_2 R^2 + c_3 R^3 + \dots), \quad \kappa \equiv \dfrac{8\pi G}{c^4}
{% end %}

Where we take $c_1 = 1$ so that the action reduces to general relativity (the Einstein-Hilbert action) in the limit of low energies, where $c_2$, $c_3$, and all higher-order terms vanish. If one chooses to ignore all terms beyond second-order, then we have a quadratic action in $R$ for an effective field theory of quantum gravity:

{% math() %}
S = \dfrac{1}{2\kappa} \int d^4x \sqrt{-g} (R + c_2 R^2)
{% end %}

Using the standard framework of quantum field theory, one can then derive an effective potential in the form:

{% math() %}
\begin{align*}
\Phi(r) &= -\left[\dfrac{k_1 GM}{r} + \dfrac{k_2 GM}{r^2} + \dfrac{k_3 GM}{r^3}\right] \\
&= -\dfrac{GM}{r}\left[k_1 + \dfrac{k_2}{r} + \dfrac{k_{31} + k_{32}}{r^2}\right]
\end{align*}
{% end %}

Where $k_1, k_2, k_3$ are constants, just as we saw previously. We know $k_1$ and $k_2$ from Newtonian gravity: $k_1 = 1$ and $k_2 = -\ell^2/2GM$, as we saw previously. However, the $k_3 = k_{31} + k_{32}$ term differs from both the Newtonian expression and the GR expression, because it modifies the GR corrective term $k_{31} = GM\ell^2/c^2$ with an additional term $k_{32}$ that is purely quantum in nature. More precisely, we expect $k_{32}$ to take the form ([_Donoghue, 1994_](https://arxiv.org/abs/gr-qc/9405057)):

{% math() %}
k_{32} \sim \dfrac{G\hbar}{c^3}
{% end %}

So the effective potential is therefore modified to:

{% math() %}
\Phi(r) =-\dfrac{GM}{r} \left[\left(1 - \dfrac{\ell^2}{2GMr}\right) + \dfrac{1}{r^2}\left(\frac{\ell^2}{c^2} + \beta\dfrac{G\hbar}{c^3}\right) + \dots\right]
{% end %}

Where $R_M$ is the radius of the central body, and $\beta$ is a dimensionless constant; calculations put the value of $\beta$ at around $-\dfrac{127}{30\pi^2}$ ([_Donoghue, 1994_](https://arxiv.org/abs/gr-qc/9405057)). If indeed correct (and we have good reason to believe it is), this result would modify geodesics around black holes and neutron stars, leading to what could potentially be observable (but tiny) effects such as gravitational lensing behavior beyond that predicted by GR. However, given that $G \hbar/c^3 \sim 10^{-70}$ such effects would be extremely weak, and would likely require observations of supermassive black holes or similarly-massive objects to detect, though detection is _not impossible_. More powerful gravitational wave detectors and more observations of ultra-compact astronomical objects might make it possible for us to detect quantum gravity effects and compare them to theory, allowing us to take our next steps in developing a comprehensive theory of quantum gravity.

As an interesting aside, if we take the nonrelativistic, classical limit of our action describing an effective theory of quantum gravity, the action for **Newtonian gravity** emerges:

{% math() %}
S = -\dfrac{1}{8\pi G}\int d^4x (\nabla \Phi)^2
{% end %}

This can be derived by linearizing the Einstein-Hilbert action; in this case, $\sqrt{-g}$ is replaced by $\sqrt{-\eta}$ (where $\eta = \det(\eta_{\mu \nu}) = -1$ is the determinant of the Minkowski metric) and where the Ricci scalar is now given by $R = \eta_{\mu \nu}R^{\mu \nu}$ instead of $R = g_{\mu \nu}R^{\mu \nu}$. After linearization the dominant contribution to the action takes the form:

{% math() %}
S \approx \dfrac{c^4}{8\pi G} \int d^4 x \left[-\dfrac{1}{4}\partial_\sigma h_{\mu \nu}\partial^\sigma h^{\mu \nu}\right], \quad g_{\mu \nu} = \eta_{\mu \nu} + h_{\mu \nu}
{% end %}

Note that this is the first term in the **Fierz-Pauli Action** that describes the hypothetical **graviton** in some theories of quantum gravity ([_Tong, 2019_](https://www.damtp.cam.ac.uk/user/tong/gr/five.pdf)), although in its un-quantized form it is a purely classical action that serves as the first term in the linearized Einstein-Hilbert action. In the nonrelativistic (Newtonian) limit, the dominant component of $h_{\mu \nu}$ is $h_{00} \approx -2\Phi/c^2$ (with associated inverse $h^{00} = 2\Phi/c^2$). In addition, the spatial component in the four-gradient $\partial_\sigma = (\frac{1}{c} \partial_t, \nabla)$ also dominates over the temporal component, so $\partial_\sigma \approx \nabla$. Thus making the replacements $h_{\mu \nu} \to h_{00}$, $h^{\mu \nu} \to h^{00}$, as well as $\partial_\sigma \to \nabla$ and $\partial^\sigma \to -\nabla$ we are left with:

{% math() %}
\begin{align*}
S &\approx \dfrac{c^4}{8\pi G} \int d^4 x \left[-\dfrac{1}{4}\partial_i h_{00} \partial^i h^{00}\right] \\
&= -\dfrac{c^4}{32\pi G} \int d^4 x\, \nabla(-2 \Phi/c^2) \cdot \nabla(-2 \Phi/c^2) \\
&= -\dfrac{1}{8\pi G} \int d^4x (\nabla \Phi \cdot \nabla \Phi) \\
&= -\dfrac{1}{8\pi G} \int d^4x (\nabla \Phi)^2
\end{align*}
{% end %}

Thus, for a weak gravitational field in the non-relativistic and classical regime, the effective action for quantum gravity reduces to the familiar action of Newtonian gravity. Using the least-action principle, it is not hard to see that the equation of motion associated with this action is given by $\nabla^2 \Phi = 0$, which is Poisson's equation for gravity in vacuum. Solving it via a series expansion in inverse powers of $r$ allows us to write down an expression for $\Phi(r)$, which is where we started our discussion. We've now come full-circle!

## Concluding thoughts

In many physical systems, we have an incomplete understanding of their behavior. This is especially the case in both classical and quantum field theory. But effective field theory is at our disposal to make sense of what we _don't_ know based on what we do know. Far from being arbitrary mathematical tricks, the power of the effective field theory approach is that they are firmly grounded in the **correspondence principle**, which says that _whenever we develop a new theory, it must reduce to pre-existing theories in the appropriate limits_. Effective field theory is our best way of understanding the world using the _knowledge we have_, rather than the knowledge that we don't have. It is a powerful approach that lets us bravely march into the wild frontiers of physics, knowing that we have the map of effective field theory to guide us on our way.