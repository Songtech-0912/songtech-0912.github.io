+++
title = "Advanced Classical Mechanics, Part III"
date = 2025-01-26
draft = false
+++

In this third (and final) part of the classical mechanics series, we delve into the physics of rotational motion and interacting systems of particles. We learn about the harmonic oscillator and its many generalizations. And we conclude our journey on classical mechanics by discussing oscillating systems, eventually taking us to continuous oscillations and waves.

<!-- more -->

Again, remember that this is part of the **advanced classical mechanics series**, which I have split into several parts to not be overly long. A complete catalogue of the entire three-part guide is shown below:

> ### The advanced classical mechanics series
>
> - [Go to part 1 of the series](@/advanced-classical-mech/index.md) for Newtonian mechanics and special relativity
> - [Go to part 2 of the series](@/advanced-classical-mech/part-2.md) for Lagrangian and Hamiltonian formulations of classicial mechanics
> - [Go to part 3 of the series](@/advanced-classical-mech/part-3.md) for rigid-body dynamics, many-body systems, the harmonic oscillator, and systems of coupled oscillators (**this is the part you're reading right now**)

## Dynamics of systems of particles

In previous examples, we discussed the motion of a few-body system. But for systems of many bodies, it is helpful to split the problem into two parts: the motion of the **center of mass** of the system, and the motion of each body _with respect_ to the center of mass.

For a system of $N$ interacting particles with masses $m_1, m_2, \dots, m_N$, the position of the center of mass $\mathbf{R}_{CM}$ can be found through:

{% math() %}
\mathbf{R}_{CM} = \dfrac{1}{\sum_{i=1}^N m_i} \sum_{i=1}^N m_i \mathbf{r}_i
{% end %}

This can be written more simply in terms of the _total mass_ of the system, $M_\text{total}$, which we may find through: 

{% math() %}
M_\text{total} = \sum_{i = 1}^N m_i
{% end %}

Thus our expression for the position of the center of mass reduces to:

{% math() %}
\mathbf{R}_{CM} = \dfrac{1}{M_\text{total}}\sum_{i=1}^N m_i \mathbf{r}_i
{% end %}

If we have a _continuous mass density_ described by a mass density function $\rho(\mathbf{r})$, the equivalent formulas are:

{% math() %}
\begin{align*}
M_\text{total} = \int \rho dV \\
\mathbf{R}_{CM} = \dfrac{1}{M_\text{total}}\int \rho\, \mathbf{r}\, dV
\end{align*}
{% end %}

The total **linear momentum** of the system of $N$ (discrete, not continous) masses is given by:

{% math() %}
\mathbf{P}_\text{total} = \sum_{i = 1}^N \mathbf{p}_i = \sum_{i = 1}^N m_i\mathbf{v}_i
{% end %}

Where $\mathbf{p}_i$ is the momentum associated with each of the individual particles. A system of particles obeys the **conservation of total momentum** if no external force is applied on the entire system. That is, we have:

{% math() %}
\dfrac{d\mathbf{P}_\text{total}}{dt} = 0
{% end %}

The *velocity* of the center of mass is given by:

{% math() %}
\mathbf{v}_{CM} =\dfrac{d\mathbf{R}_{CM}}{dt} = \dfrac{1}{M_\text{total}} \underbrace{\sum_{i = 1}^N m_i \mathbf{v}_i}_{ \mathbf{P}_\text{total}} =\dfrac{\mathbf{P}_\text{total}}{M_\text{total}}
{% end %}

The system of particles can also possess _angular momentum_ if the system is rotating (for instance, individual stars moving within a stellar cluster, which itself rotates about the galactic plane). The **total angular momentum** of the system can be written as:

{% math() %}
\mathbf{L}_\text{total} = \underbrace{\mathbf{R}_{CM} \times \mathbf{P}_\text{total}}_\text{angular momentum of CoM} + \underbrace{\sum_{i = 1}^N \mathbf{r}_i \times \mathbf{p}_i}_\text{angular momenta of particles}
{% end %}

Note that here, $\text{CoM}$ is an abbreviation for "center of mass". To simplify the problem, it is easier to choose a special coordinate system known as the **center of mass frame** with the coordinate transformations:

{% math() %}
\begin{align*}
\mathbf{r}_i' &= \mathbf{R}_{CM} + \mathbf{r}_i \\
\dot{\mathbf{r}}_i' &= \mathbf{v}_{CM} + \dot{\mathbf{r}}_i \\
\mathbf{p}_i' &= m_i \dot{\mathbf{r}}_i' = m_i(\mathbf{v}_{CM} + \dot{\mathbf{r}}_i)
\end{align*}
{% end %}

Which allows us to write the total angular momentum of the system in a much-simplified form:

{% math() %}
\mathbf{L}_\text{total} = \sum_{i = 1}^N \mathbf{r}_i' \times \mathbf{p}_i'
{% end %}

This form is also useful because expressing the conservation of angular momentum, that is, $\dfrac{d \mathbf{L}_\text{total}}{dt} = 0$, becomes much easier. This is because while the inter-particle interactions may not conserve angular momentum, the _system_ as a whole does indeed conserve angular momentum.

Now, recall that we saw earlier that the total angular momentum of an $N$-body system can be found from:

{% math() %}
\mathbf{L}_\text{total} = \mathbf{R}_{CM} \times \mathbf{P}_\text{total} + \sum_{i = 1}^N \mathbf{r}_i \times \mathbf{p}_i
{% end %}

If we differentiate this result, we have:

{% math() %}
\begin{align*}
\dfrac{d\mathbf{L}_\text{total}}{dt} &= \mathbf{R}_{CM} \times \dfrac{d\mathbf{P}_\text{total}}{dt} + \sum_{i = 1}^N \mathbf{r}_i \times \dfrac{d\mathbf{p}_i}{dt} \\
&= \underbrace{\mathbf{R}_{CM} \times \mathbf{F}_\text{ext.}}_\text{net torque} + \sum_{i = 1}^N \mathbf{r}_i \times \dfrac{d\mathbf{p}_i}{dt} \\
&= \tau_\text{net} + \sum_{i = 1}^N \left(\mathbf{r}_i \times \dfrac{d\mathbf{p}_i}{dt}\right) \\
&= \tau_\text{net} + \sum_{i = 1}^N \left(\mathbf{r}_i \times \mathbf{F}_i\right)
\end{align*}
{% end %}

This is because the rate of change of the system's total momentum is equal to the _external forces_ on the system (we know this from Newton's second law $\mathbf{F} = \dfrac{d\mathbf{p}}{dt}$), and thus we have {% inlmath() %}\dfrac{d\mathbf{P}_\text{total}}{dt}{% end %}, and the cross product of position and force is the torque. Meanwhile, the rate of the change of each _particle_'s momentum {% inlmath() %}\dot{\mathbf{p}}_i{% end %} is equal to the force {% inlmath() %}\mathbf{F}_i{% end %} experienced by the particle, which comes from the inter-particle interactions _within_ the system. But if the inter-particle forces in the system are _only_ dependent on the separation vector {% inlmath() %}\mathbf{r}_{ij}{% end %} between any two particles $i, j$, that is, {% inlmath() %}\mathbf{F}_{ij} = \mathbf{F}(\mathbf{r}_{ij}){% end %}, then {% inlmath() %}\mathbf{F}_{ij} = -\mathbf{F}_{ji}{% end %}, so the inter-particle forces cancel _as a whole_, meaning the second term vanishes in the expression of the total angular momentum of the system. Thus we have:

{% math() %}
\dfrac{d\mathbf{L}_\text{total}}{dt} = \tau_\text{net}
{% end %}

 We can also examine other characteristics of an $N$-body system. For instance, the total kinetic energy of the system is given by:

{% math() %}
K = \dfrac{1}{2} m_\text{total} \mathbf{v}_{CM}^2 + \dfrac{1}{2} \sum_{i = 1}^N m_i \mathbf{v}_i^2
{% end %}

Where {% inlmath() %}\mathbf{v}_i{% end %} is the velocity of a particle with respect to the center-of-mass frame and {% inlmath() %}\mathbf{v}_{CM}{% end %} is the velocity of the center-of-mass frame. We may also define the total _potential energy_ as:

{% math() %}
U = \underbrace{\sum_i U_{i,\ \text{ext.}}}_\text{external forces} + \underbrace{\sum_{i < j} U_{ij}}_\text{inter-particle forces}
{% end %}

The first term in the potential describes the potential arising from the _external forces_ acting on the system. The second term, meanwhile, describes the potential arising from the _internal inter-particle forces_ within the system. Thus, we may write the total force on the system as:

{% math() %}
\mathbf{F} = -\sum_i\nabla U_i - \sum_{i < j}\nabla U_{ij}
{% end %}

## Collisions and scattering

From our discussion of many-body systems, it is natural to ask how particles interact when they collide with each other, as is bound to happen when we have a many-body system of particles held together by attractive forces (such as gravity). Thankfully, collisions satisfy the **conservation of momentum**. Let us see why. By Newton's third law, when two particles collide, the contact force of the first particle against the second must be equal and opposite to the contract force of the second particle against the first. That is, we have:

{% math() %}
\mathbf{F}_{12} = -\mathbf{F}_{21}
{% end %}

Recalling that force is the time derivative of momentum, we thus have:

{% math() %}
\dfrac{d\mathbf{p}_2}{dt} = -\dfrac{d\mathbf{p}_1}{dt}
{% end %}

We can integrate both sides to get:

{% math() %}
\mathbf{p}_2 = -\mathbf{p}_1
{% end %}

But let us now consider a frame where we observe the collision between the two particles. The total momentum within the frame would then be the sum of the momenta of the two particles:

{% math() %}
\begin{align*}
\mathbf{p}_\text{total} &= \mathbf{p}_1 + \mathbf{p}_2 \\
&= \underbrace{\mathbf{p}_1 + (-\mathbf{p}_1)}_{\text{from }  \mathbf{p}_2 = -\mathbf{p}_1} \\
&= 0
\end{align*}
{% end %}

So indeed, we find that momentum is conserved for two colliding particles. The same is true for any number of colliding particles, but for simplicity, we will only consider the two-particle case here, rather than the more general $N$-body case.

### Analysis of elastic and inelastic collisions

In general, two-particle collisions can be classified as either **elastic** or **inelastic**. The names give a hint as to what they refer to: when we have an elastic collision, the two particles "bounce off" each other after colliding, while when we have a (perfectly) inelastic collision, the two particles "stick together" afterwards. Perfectly elastic collisions are very, very rare in nature, as they essentially require both colliding objects to be 100% imprenetrable or with zero volume; thus (roughly speaking) only collisions between subatomic particles are truly perfectly elastic. What about inelastic collisions? "Inelastic" means that the two colliding objects will be deformed in some way, radiating energy in the form of light, heat, and/or sound. Any collision between two macroscopic objects is bound to be inelastic, which is why kicking a soccer ball makes a (pretty obvious!) sound and why the collisions between tectonic plates in the Earth's crust causes earthquakes. But macroscopic collisions can fall into a wide range between *perfectly* elastic and *perfectly* inelastic - thus, it is possible to *model* some collisions as perfectly elastic (a good approximation when we have near-rigid objects) and model some other collisions as perfectly inelastic (a good approximation when we don't).

Elastic collisions are characterized by the fact that they _leave no trace_ of the collision. There is no sound, no heat, no light, no indication after the collision that the collision occured _at all_. This means they **perfectly conserve energy**. By contrast, inelastic collisions can leave plenty of traces of the collision, including things we typically associate with colliding objects - a loud "bang", a burst of light, and so forth. All of these come from energy that cascades away when the collision occurs, so inelastic collisions **do not conserve energy**.

Let us first consider an _elastic collision_ between two objects of masses $m_1, m_2$, whose initial velocities are $\mathbf{v}_1, \mathbf{v}_2$, and whose post-collision velocities (which we want to solve for) are $\mathbf{v}_1', \mathbf{v}_2'$. By the conservation of energy, we have $K_1 + K_2 = K_1' + K_2'$, and therefore:

{% math() %}
\dfrac{1}{2} m_1 \mathbf{v}_1^2 + \dfrac{1}{2} m_2 \mathbf{v}_2^2 = \dfrac{1}{2} m_1 \mathbf{v}_1'^2 + \dfrac{1}{2} m_2 \mathbf{v}_2'^2
{% end %}

This is rather long and unyieldy equation, so it is helpful to switch to the _center of momentum frame_. First, we write out the _total momentum_ of the system (which is _always_ conserved) as:

{% math() %}
\begin{gather*}
\mathbf{P}_\text{total} = m_1 \mathbf{v}_1 + m_2 \mathbf{v}_2 = M_\text{total} \mathbf{v}_{CM} \\
\Rightarrow \mathbf{v}_{CM} = \dfrac{m_1 \mathbf{v}_1 + m_2 \mathbf{v}_2}{m_1 + m_2}
\end{gather*}
{% end %}

Where {% inlmath() %}\mathbf{v}_{CM}{% end %} is the velocity of the center of momentum frame, and {% inlmath() %}M_\text{total} = m_1 + m_2{% end %}. This allows us to make a transformation to a set of new velocity coordinates {% inlmath() %}\mathbf{v}_1^*, \mathbf{v}_2^*{% end %}, which give the velocities of each of the two objects in the center of momentum frame, given by:

{% math() %}
\begin{align*}
\mathbf{v}_1^* = \mathbf{v}_1 - \mathbf{v}_{CM} \\
\mathbf{v}_2^* = \mathbf{v}_2 - \mathbf{v}_{CM} \\
\end{align*}
{% end %}

By substituting these definitions into our previous equation for the total momentum, we find that:

{% math() %}
\underbrace{m_1 \mathbf{v}_1^* + m_2 \mathbf{v}_2^*}_\text{initial} = \underbrace{m_1 \mathbf{v}_1'^* + m_2 \mathbf{v}_2'^*}_\text{post-collision} =0
{% end %}

Which is a much simpler result, and allows us to also derive the relationships between the sets of velocities:

{% math() %}
\begin{matrix*}
\underbrace{\mathbf{v}_2^* = -\dfrac{m_1}{m_2} \mathbf{v}_1^*}_\text{initial velocities}, &\underbrace{\mathbf{v}_2'^* = -\dfrac{m_1}{m_2} \mathbf{v}_1'^*}_\text{post-collision velocities}
\end{matrix*}
{% end %}

> **Note:** another special property is that the angles of deflection (the angle between {% inlmath() %}\mathbf{v}_1^*, \mathbf{v}_1'^*{% end %}, as well as the angle between {% inlmath() %}\mathbf{v}_2^*, \mathbf{v}_2'^*{% end %}) are the _same_ when measured in the center of momentum frame, which is _not true_ in general within the regular (untransformed) frame.

Now, if we substitute the above relations for {% inlmath() %}\mathbf{v}_2^*{% end %} and {% inlmath() %}\mathbf{v}_2'^*{% end %}, we can write out the conservation of energy equation as:

{% math() %}
\begin{gather*}
\dfrac{1}{2} m_1 {\mathbf{v}_1^*}^2 + \dfrac{1}{2} m_2 {\mathbf{v}_2^*}^2 = \dfrac{1}{2} m_1 {\mathbf{v}_1'^*}^2 + \dfrac{1}{2} {m_2 \mathbf{v}_2'^*}^2 \\
\dfrac{1}{2} m_1 {\mathbf{v}_1^*}^2 + \dfrac{1}{2} m_2 \left(\dfrac{m_1}{m_2}\right)^2 {\mathbf{v}_1^*}^2 = \dfrac{1}{2} m_1 {\mathbf{v}_1'^*}^2 + \dfrac{1}{2} m_2\left(\dfrac{m_1}{m_2}\right)^2 {\mathbf{v}_1'^*}^2 \\
\dfrac{1}{2} \left[m_1 + \left(\dfrac{m_1}{m_2}\right)^2\right] {\mathbf{v}_1^*}^2 = \dfrac{1}{2} \left[m_1 + \left(\dfrac{m_1}{m_2}\right)^2\right] {\mathbf{v}_1'^*}^2 \\
\cancel{\dfrac{1}{2} \left[m_1 + \left(\dfrac{m_1}{m_2}\right)^2\right]} {\mathbf{v}_1^*}^2 = \cancel{\dfrac{1}{2} \left[m_1 + \left(\dfrac{m_1}{m_2}\right)^2\right]} {\mathbf{v}_1'^*}^2 \\
\Rightarrow  {\mathbf{v}_1^*}^2 = {\mathbf{v}_1'^*}^2
\end{gather*}
{% end %}

So we find that {% inlmath() %}|\mathbf{v}_1^*| = |\mathbf{v}_1'^*|{% end %}, which also implies that {% inlmath() %}|\mathbf{v}_2^*| = |\mathbf{v}_2'^*|{% end %}. We would expect this: the conservation of energy would require that this be the case.

We will now examine a classic problem to be able to showcase using the center-of-momentum frame to solve problems. Consider a mass $m_1$ moving at velocity $\mathbf{v}_1$ that collides with another mass $m_2$ that istationary, so $\mathbf{v}_2 = 0$ (this is a classic billiard-ball style situation). The masses are rigid, so we may assume that the collision is close to perfectly elastic. The collision sends the two massses flying in opposite directions; the first mass is deflected by an angle $\psi$, and the second mass is deflected by an angle $\xi$. We show this scenario in the below diagram:

{{ natural_img(
src="elastic-collision-demo.excalidraw.svg"
desc="My description"
) }}

Writing out the conservation of momentum yields the following equation:

{% math() %}
m_1 \mathbf{v}_1 = m_1 \mathbf{v}_1' + m_2 \mathbf{v}_2' = M_\text{total} \dot{\mathbf{R}}
{% end %}

Where $\dot{\mathbf{R}} = \mathbf{v}_{CM}$ is the center-of-mass velocity. If we define $v_1 = |\mathbf{v}_1$ as the _speed_ of the first mass pre-collision, and $v_1' = |\mathbf{v}_1'|$ and $v_2' = |\mathbf{v}_2'|$ as the _speeds_ of the objects, post-collision, then we can write the above in component form as:

{% math() %}
\begin{bmatrix} m_1 v_1 \\ 0 \end{bmatrix} =
\begin{bmatrix} m_1 v_1' \cos \psi \\ m_1 v_1' \sin \psi \end{bmatrix} +
\begin{bmatrix} m_2 v_2' \cos \xi \\ m_2 v_2' \sin \xi \end{bmatrix}
{% end %}

Let us now switch over to the center of momentum frame. We use the transformations:

{% math() %}
\begin{matrix*}
\mathbf{v}_1^* = \mathbf{v}_1 - \dot{\mathbf{R}},
&\mathbf{v}_2^* = \mathbf{v}_2 - \dot{\mathbf{R}} \\
\mathbf{v}_1'^* = \mathbf{v}_1' - \dot{\mathbf{R}}, &\mathbf{v}_2'^* = \mathbf{v}_2' - \dot{\mathbf{R}} \\
\end{matrix*}
{% end %}

Where again, $\dot{\mathbf{R}}$ is the center-of-mass velocity, given by:

{% math() %}
\begin{align*}
\dot{\mathbf{R}} &= \dfrac{m_1 \dot{\mathbf{r}}_1 + \cancel{m_2 \dot{\mathbf{r}}_2}}{m_1 + m_2} \\
&= \dfrac{m_1}{m_1 + m_2} \mathbf{v}_1 \\
&= \dfrac{m_1}{m_1 + m_2} \begin{bmatrix} v_1 \\ 0 \end{bmatrix}
\end{align*}
{% end %}

Now, if we perform our coordinate transformations to our center-of-momentum frame coordinates, where our angle of deflection for both masses would be the transformed angle $\theta$, we have:

{% math() %}
\begin{align*}
v_1^* \cos \theta &= v_1' \cos \psi - \dfrac{m_1}{m_1 + m_2} v_1 \\
\Rightarrow v_1' &\cos \psi = v_1'^* \cos \theta + \dfrac{m_1}{m_1 + m_2} v_1 \\
v_1^* \sin \theta &= v_1' \sin \psi - 0 \\
&= v_1' \sin \psi \\
\dfrac{v_1' \sin \psi}{v_1' \cos \psi} &= \tan \psi \\ &= \dfrac{v_1'^* \sin \theta}{v_1'^* \cos \theta + \frac{m_1 v_1}{m_1 + m_2}}
\end{align*}
{% end %}

But recall that $v_1^* = v_1'^*$, as we derived before from the conservation of energy, and using the coordinate transformation equations and our definition of $\dot{\mathbf{R}}$, we find that:

{% math() %}
\begin{align*}
v_1^* &= v_1 - \dot R_x \\
&= v_1 - \dfrac{m_1}{m_1 + m_2} v_1 \\
&= \dfrac{m_1 + m_2}{m_1 + m_2}v_1 - \dfrac{m_1}{m_1 + m_2} v_1 \\
&= \dfrac{m_2}{m_1 + m_2} v_1
\end{align*}
{% end %}

And since $v_1^* = v_1'^*$, we can substitute this into our expression for $\tan \psi$ to get:

{% math() %}
\begin{align*}
\tan \psi &= \dfrac{v_1'^* \sin \theta}{v_1'^* \cos \theta + \frac{m_1 v_1}{m_1 + m_2}} \\
&= \dfrac{\sin \theta}{\cos \theta + \frac{m_1}{m_1 + m_2}\frac{m_1 + m_2}{m_2}} \\
&= \dfrac{\sin \theta}{\cos \theta + m_1/m_2} \\
\end{align*}
{% end %}

We note that if $m_1 \ll m_2$, then $\tan \psi \approx \tan \theta$ and $\psi \approx \theta$. Meanwhile, if $m_1 = m_2$, then $\tan \psi = \dfrac{\sin \theta}{\cos \theta + 1} = \tan \left(\dfrac{\theta}{2}\right)$. We will not do the derivations but we note that in the case $m_1 = m_2$, we additionally have $\tan \xi = \tan \left(\dfrac{\pi}{2} - \dfrac{\theta}{2}\right)$ and therefore we have $\xi = \dfrac{\pi}{2} - \psi$. And we can now see the significance of center-of-momentum frames: while the math to solve this problem was intense, it would have been much, much harder had we not used a center-of momentum frame to solve the problem.

### Scattering problems

Using the conservation of momentum, we can solve for collisions between two (or perhaps three or four) particles - anything beyond that is intractable. But what if we have a large number of particles, all of them colliding at some surface? That is to say, if we were to shoot a number of particles on some surface, what would be the distribution of the particle impacts on the surface (if the collision is inelastic) or where would the particles be deflected (if the collision is elastic)? This is the problem known as **scattering**.

{{ diagram(
src="https://upload.wikimedia.org/wikipedia/commons/d/dc/Differential_cross_section.svg"
desc="An illustration of scattering. A particle incident on some object at a height b above the collision axis incident on cross-sectional area sigma is deflected at solid angle d omega."
) }}

_Source: [Wikipedia](https://en.wikipedia.org/wiki/File:Differential_cross_section.svg)_

To describe scattering, we begin by defining the collision object (that the particle(s) hit and scatter off of), and draw an axis through its center - we refer to this axis as the **centerline** or **collision axis**. The particle(s)' distance _above_ the centerline is known as the **impact parameter**, which we denote as $b$. If the particle does indeed deflect, then the angle at which it deflects is called the **scattering angle**, and is denoted by $\theta$.

Now, to analyze scattering, we use something called the _scattering cross-section_. This describes the ratio of $d\sigma$, an infinitesimal cross-sectional area the particle(s) pass through, to $d\Omega$, an infinitesimal scattering angle (the $\Omega$ is due to the fact that the angle is called a **solid angle**). Using the notation in Griffiths, _Introduction to Elementary Particles_, the scattering cross-section $D(\theta)$ is therefore defined as:

{% math() %}
\begin{matrix*}
D(\theta) = \dfrac{d\sigma}{d\Omega}, &d\sigma = |b\,db\, d\phi|, & d\Omega = |\sin \theta\, d\theta\, d\phi|
\end{matrix*}
{% end %}

> **Note:** Funnily enough, while it _looks_ like a derivative, the scattering cross-section $\dfrac{d\sigma}{d\Omega}$ is not a derivative at all! It is truly just a fraction (albeit between two infinitesimal quantities), so we manipulate it like a fraction, no calculus or limit trickery needed.

Thus, by some rearrangement of $D(\theta)$ we find that we may also express the scattering cross-section as:

{% math() %}
\dfrac{d\sigma}{d\Omega} = \left|\dfrac{b}{\sin \theta} \left(\dfrac{db}{d\theta}\right)\right|
{% end %}

To find the *total* cross-section from the differential cross-section, we integrate over the total solid angle:

{% math() %}
\begin{align*}
\sigma_t &= \int \dfrac{d\sigma}{d\Omega} d\Omega \\
&= \int_0^{2\pi} \int_0^\pi \dfrac{d\sigma}{d\Omega} \sin \theta d\theta d\phi \\
&= \int_0^{2\pi} \int_0^\pi D(\theta) \sin \theta d\theta d\phi
\end{align*}
{% end %}

The scattering cross-section has rather unusual units: it is expressed in terms of $\pu{m^2/sr}$, that is, _meters squared over steradians_ (steradians are the standard unit for solid angle and are very similar to radians for regular angles). However, since steradians are dimensionless, the scattering cross-section can equivalently just be expressed in units of $\pu{m^2}$. In (quantum) particle physics, it is common to use the (funnily-named) unit of the _barn_ ($\pu{b}$), where $\pu{1b} = \pu{100 fm^2} = \pu{10^{-28} m^2}$. But for classical physics, we can just use regular meters and centimeters.

### Scattering over a hard sphere

Let us consider a particle (or stream of particles) bouncing off a hard sphere of radius $R$ (this problem is also in Griffiths, _Introduction to Elementary Particles_, example 6.1). By "hard", we mean a completely rigid, impenetrable sphere, which is of course impossible in reality, so this is an idealization. For this problem, it is always helpful to draw a diagram, so we show one below:

{{ wideimg(
src="./hard-sphere-scattering.excalidraw.svg"
desc="A diagram showing a particle of height b passing through cross-section d sigma that hits a solid impenetrable sphere and is deflected at angle theta (measured from the +x axis). The scattering solid angle is d Omega."
) }}

Recall that $\dfrac{d\sigma}{d\Omega} = \left|\dfrac{b}{\sin \theta} \left(\dfrac{db}{d\theta}\right)\right|$ is the general result that we found before (one that generalizes to other problems, it is not just true for this particular problem). Unfortunately, to be able to compute the formula explicitly, we need to know $b(\theta)$. This is where our diagram comes in. By defining the angle $\phi$ for which $\theta = \pi - 2\phi$, we have:

{% math() %}
\begin{gather*}
\sin \phi = \dfrac{b}{R} \Rightarrow b = R \sin \phi \\
\theta = \pi - 2\phi \Rightarrow \phi = \dfrac{\pi}{2} - \dfrac{\theta}{2} \\
b = R \sin \phi = R \sin \left(\dfrac{\pi}{2} - \dfrac{\theta}{2}\right)
\end{gather*}
{% end %}

Using the result that $\cos \alpha = \sin \left(\dfrac{\pi}{2} - \alpha \right)$ we have:

{% math() %}
\begin{align*}
b &= R \cos \left(\dfrac{\theta}{2}\right) \\
b'(\theta) &= -\dfrac{R}{2} \sin \left(\dfrac{\theta}{2}\right) \\
|b'(\theta)| &= \dfrac{R}{2} \sin \left(\dfrac{\theta}{2}\right)
\end{align*}
{% end %}

So our differential cross section would be:

{% math() %}
\dfrac{d\sigma}{d\Omega} = \left|\dfrac{b}{\sin \theta} \left(\dfrac{db}{d\theta}\right)\right| = \dfrac{1}{\sin \theta} R \cos \left(\dfrac{\theta}{2}\right) \dfrac{R}{2} \sin \left(\dfrac{\theta}{2}\right) = \dfrac{R^2}{2} \dfrac{\sin(2\theta/2)}{2 \sin \theta} = \dfrac{R^2}{4}
{% end %}

Where here we used the identity that $\sin \beta \cos \beta = \dfrac{1}{2} \sin(2\beta)$. Thus, we have solved the problem of scattering over a hard sphere, and we have found that the distribution of the scattered particle(s) in terms of cross-sectional area per solid angle is $\dfrac{d\sigma}{d\Omega} = \dfrac{R^2}{4}$.

> **Note:** This scattering problem may seem like it is for a very specific case. However, hard-sphere scattering is in fact more general, because it also models any scattering off any spherically-symmetric potential barrier $V_0$ that a classical particle with energy $E < V_0$ cannot pass through.

### Scattering over a force field

Scattering does not necessarily have to involve two objects hitting each other. A particle (or set of particles) could just as easily scatter off a central force field, such as an electrostatic field, in which it doesn't "hit" anything, but its direction and speed still changes. For instance, in spacecraft navigation (especially NASA space probes heading into deep space), it is common for a spacecraft to receive a _gravity assist_ from a planet (usually Jupiter). This means it essentially scatters off the gravitational field of the planet, which gives it a big velocity boost, necessary to overcome the strong gravitational pull of the Sun and travel into the furthest reaches of the Solar System (and beyond!).

In the case of a particle of mass $m$ (such as a small spacecraft) scattering over the gravitational planet caused by a much larger mass $M$ (such as a planet), we use essentially the same approach, just with some more sophisticated mathematics. The derivation is a bit difficult, but the essentials are the same. We once again define an angle $\phi$ for which $\theta = \pi - 2\phi$, where $\phi$ is given by:

{% math() %}
\phi(r) = -\int_{r_0}^{r_\text{min}} \dfrac{\ell}{r^2} \dfrac{dr}{\sqrt{2\mu(E - U(r)- \ell^2/2\mu r^2)}}
{% end %}

Where $U(r) = -\dfrac{GMm}{r}$ is the gravitational potential energy of the particle, $\mu = \dfrac{mM}{m+M}$ is the reduced mass of the two-body system, where $r_0$ is the distance from the center of the solid sphere that the particle starts off at $t  = 0$, and $r_\text{min}$ is the _point of closest approach_. Remember that since the particle is scattering off a gravitational field, there is no solid object that the particle actually "bounces off" of; rather, the particle approaches from some distance $r_0$ until it reaches the closest point $r = r_\text{min}$, before it is deflected away and goes the opposite direction. We can often get away by setting $r_0 = \infty$, meaning that the particle approaches from sufficiently far away that it can be considered to initially infinitely distant. From here, we "just" need to compute the integral, and then use $\dfrac{d\sigma}{d\Omega} = \left|\dfrac{b}{\sin \theta} \left(\dfrac{db}{d\theta}\right)\right|$ to find the differential cross-section.

> **Note:** This expression is more general than just for gravitational fields; in fact, it applies for _any_ central force field with potential $U = U(r)$, so it equally applies for harmonic potentials and electrostatic force fields!

### Non-inertial reference frames

We have seen in our study of moving reference frames that due to the constraints in a rotating coordinate system, fictitious "forces" arise when attempting to apply Newton's second law $\mathbf{F} = m \mathbf{a}$. While these are not real forces, they can be _mathematically treated_ as parts of an **effective force** to allow us to treat the problem in the same way as we would treat a problem that used a stationary (inertial) reference frame. In a rotating frame, the effective force $\mathbf{F}_\text{eff.}$ experienced by an observer is given by:

{% math() %}
\mathbf{F}_\text{eff.} = \underbrace{\mathbf{F}_\text{fixed} - m \ddot{\mathbf{R}}_F}_\text{inertial terms} - \underbrace{m \vec{\dot \omega} \times \mathbf{r}  - m \vec \omega \times(\vec \omega \times \mathbf{r}) - 2m\vec \omega \times \mathbf{v}_r}_\text{non-inertial terms}
{% end %}

Where {% inlmath() %}\mathbf{F}_\text{fixed}{% end %} describes all physical (real) forces in the _fixed reference frame_, {% inlmath() %}m \ddot{\mathbf{R}}_F{% end %} describes the acceleration due to translation of the rotating system, {% inlmath() %}m \vec{\dot \omega} \times \mathbf{r}{% end %} describes the angular acceleration, {% inlmath() %}m \vec \omega \times(\vec \omega \times \mathbf{r}){% end %} is the acceleration due to the centrifugal "force", and {% inlmath() %}2m\vec \omega \times \mathbf{v}_r{% end %} is due to the Coriolis force. Note that all terms after {% inlmath() %}\mathbf{F}_\text{fixed} - m\ddot{\mathbf{R}}_F{% end %} are terms unique to the non-inertial frame; these _non-inertial terms_ come as a result of the coordinate system. The only _real_ forces (e.g. gravity, electric force, etc.) are contained within {% inlmath() %}\mathbf{F}_\text{fixed}{% end %}; all other "force" terms arise due to the motion (translational and rotational) of the rotating frame and should be considered as **fictitious forces**.

To solve for the equations of motion, we must set {% inlmath() %}\mathbf{F}_\text{eff.} = m\mathbf{a}_r{% end %}, where we solve for {% inlmath() %}\mathbf{a}_r{% end %}, the effective force on some moving body inside the rotating reference frame. Consider, for instance, a fixed reference frame located at the center of the Earth. We are interested in what is happening within a reference frame at the Earth's surface. The surface reference frame rotates as the Earth rotates, so it is a _rotating reference frame_. We want to describe the motion of an object on the Earth's surface (which means that it is in our surface reference frame) by finding the equations of motion.

To be able to solve for the equations of motion, we begin by isolating the forces in the fixed frame. The forces in the fixed frame are:

{% math() %}
\mathbf{F}_\text{fixed} = m\ddot{\mathbf{R}}_F = \mathbf{S} + m\mathbf{g}_0
{% end %}

Where $\mathbf{g}_0 = -\dfrac{GM}{r^2} \hat r$ and $\mathbf{S}$ includes all other physical forces (e.g. geothermal pressure). These are forces that _do not arise_ as a result of the rotating coordinate system, hence why we say that they are _physical_ forces, rather than fictitious forces that are the result of a rotating reference frame.

Let us now consider the terms that *are* dependent on the rotating coordinate system. First, the Earth's rotation has an approximately constant angular velocity, which we may denote $\omega_0$, such that:

{% math() %}
\vec \omega = \omega_0 \hat z
{% end %}

We have:

{% math() %}
\ddot{\mathbf{R}}_F = \vec \omega \times (\vec \omega \times \mathbf{R}_F)
{% end %}

Such that the effective force takes the form:

{% math() %}
\begin{align*}
\mathbf{F}_\text{eff} &= \mathbf{F}_\text{fixed} - m\ddot{\mathbf{R}}_F - m \vec \omega \times(\vec \omega \times \mathbf{r}) - 2m\vec \omega \times \mathbf{v}_r \\
&= \mathbf{S} + m\mathbf{g}_0 - m\vec \omega \times (\vec \omega \times (\mathbf{R} + \mathbf{r})) - 2m\vec \omega \times \mathbf{v}_r
\end{align*}
{% end %}

We note that the gravitational acceleration interestingly does not point _directly_ towards the center of the Earth. This is because of the contribution of the centrifugal "force", which _modifies_ the direction of the gravitational acceleration away from the direction of the gravitational field $\mathbf{g}_0$. Thus, it is convenient to define the _effective_ gravitational acceleration as measured on the Earth's surface, given by:

{% math() %}
\mathbf{g} = \mathbf{g}_0 - \vec \omega \times (\vec \omega \times (\mathbf{R} + \mathbf{r}))
{% end %}

> **Note:** In general, $\mathbf{g} - \mathbf{g}_0 \approx \pu{0.034 m/s}$ (while the precise value depends on your latitude, this is the approximate maximum value). This discrepancy is the contribution due to centrifugal effects (what we call the centrifugal "force").

Using the effective gravitational acceleration, we can rewrite our expression for the effective force as:

{% math() %}
\mathbf{F}_\text{eff.} = \mathbf{S} + m\mathbf{g} - \underbrace{2m \vec \omega \times \mathbf{v}_r}_\text{coriolis "force"}
{% end %}

Let us now consider the case of a particle falling to Earth's surface from some height $h$. We will use $z$ as our radial coordinate, $x$ as the horizontal coordinate, and $\theta$ as the angle made with respect to the center of the Earth, as we show in the below diagram:

{{ diagram(
src="coriolis-earth.excalidraw.svg"
desc="A diagram of the problem's coordinate system, showing z as the distance above earth's surface, theta as the angle with respect to the center of the earth, and y as the direction tangent to the Earth's surface"
) }}

The angular velocity of the Earth about its rotational axis is given by:

{% math() %}
\vec \omega = -\omega_0 \cos \theta \hat x + \omega_0 \sin \theta \hat z
{% end %}

From here, substituting our result for the effective force on the surface of the Earth, we find that:

{% math() %}
\begin{align*}
\mathbf{F}_\text{eff.} &= m \mathbf{g} - 2m \vec \omega \times \vec{\mathbf{v}}_r \\
m\mathbf{a}_r &= m \mathbf{g} - 2m \vec \omega \times \vec{\mathbf{v}}_r \\
\mathbf{a}_r &= \mathbf{g} - 2\vec \omega \times \vec{\mathbf{v}}_r \\
\end{align*}
{% end %}

The velocity $\mathbf{v}_r$ is given, in this configuration by:

{% math() %}
\mathbf{v}_r = \begin{pmatrix} 0 \\ 0 \\ -gt \end{pmatrix}
{% end %}

From which we can calculate the cross product of the angular velocity vector with:

{% math() %}
\begin{align*}
\vec \omega \times \mathbf{v}_r &= \begin{vmatrix}
 \hat x & \hat y & \hat z \\
 -\omega_0 \cos \theta & 0 & \omega_0 \sin \theta \\
 0 & 0 & -gt
\end{vmatrix} \\
&= -g \omega_0 t \cos \theta \hat y
\end{align*}
{% end %}

Thus, expanding out $\mathbf{a}_r = \mathbf{g} - 2\vec \omega \times \vec{\mathbf{v}}_r$ in vector form, we have:

{% math() %}
\mathbf{a}_r =
\begin{pmatrix}
a_{rx} \\
a_{ry} \\
a_{rz}
\end{pmatrix} =
\begin{pmatrix}
\ddot x_r \\
\ddot y_r \\
\ddot z_r
\end{pmatrix}
=
\begin{pmatrix}
0 \\
2g\omega t \cos \theta \\
-g
\end{pmatrix}
{% end %}

These can be solved as a system of 2nd-order differential equations, with the initial conditions $\mathbf{r}(0) = \langle 0, 0, h\rangle$, $\mathbf{r}'(0) = 0$ to yield the solutions:

{% math() %}
\begin{align*}
x(t) &= 0 \\
y(t) &= \dfrac{1}{3} \omega_0 g t^3 \cos \theta \\
z(t) &= h - \dfrac{1}{2} gt^2
\end{align*}
{% end %}

Thus, the amount of deflection from a straight-line path caused by the Coriolis "force" is given by:

{% math() %}
\Delta y = \dfrac{1}{3} \omega_0 g \left(\dfrac{2h}{g}\right)^{3/2}\cos \theta
{% end %}

## Dynamics of rigid bodies

It is common to consider purely point-like particles in physics, and up to this point, we have had considered objects to be located at a definite location. However, we know that _real_ (macroscopic) objects have internal volume and size, so point particles are only an approximation to describe them. A better description uses the model of a **rigid body**, which more accurately accounts for the internal volume and nonzero size of real objects.

Rigid bodies can be thought of as a system of $n$ particles of masses $m_1, m_2, m_3, \dots$ which allows them to be modelled as such a system. Each particle would then have velocity $\mathbf{v}_i$, given by:

{% math() %}
\mathbf{v}_i = \mathbf{v}_{CM} + \vec \omega \times \mathbf{r}_i
{% end %}

where as with before, $\mathbf{v}_{CM}$ is the velocity of the center-of-mass of the system, and $\omega \times \mathbf{r}_i$ describe the particle's velocity about the center-of-mass (equivalently, the rate of rotation of the particle with respect to the rotating reference frame):

{% math() %}
\underbrace{\mathbf{r}_i = \begin{pmatrix} x_i \\ y_i \\ z_i \end{pmatrix},}_{\text{position of particle } i} \quad
\underbrace{\vec \omega = \begin{pmatrix}
\omega_x \\ \omega_y \\ \omega_z
\end{pmatrix}}_\text{angular velocity of particle w.r.t CoM}
{% end %}

For a rigid body, the distance of every point on its surface from the center of mass will remain constant in time as we assume the object cannot stretch or shrink. Rigid bodies can be analyzed by positioning our coordinate system such that the origin of our coordinate system is exactly positioned at the center of Earth's.

Let us consider the total kinetic energy of a rigid body. Using our definition of $\mathbf{v}_i$, we have:

{% math() %}
\begin{align*}
K_\text{total} &= \sum \dfrac{1}{2} m_i \mathbf{v}_i^2 \\
&= \dfrac{1}{2} \sum_i m_i (\mathbf{v}_{CM} + \vec \omega \times \mathbf{r}_i)^2 \\
&= \dfrac{1}{2} \sum_i m_i (\mathbf{v}_{CM}^2 + 2 \mathbf{v}_{CM}\cdot (\vec \omega \times \mathbf{r}) + (\vec \omega + \mathbf{r}_i)^2) \\
&= \underbrace{\dfrac{1}{2} \sum_i m_i \mathbf{v}_{CM}^2}_\text{translational KE} + \underbrace{\dfrac{1}{2} \sum_i m_i (\vec \omega \times \mathbf{r}_i)^2}_\text{rotational KE}
\end{align*}
{% end %}

Where we note that the total kinetic energy $K_\text{total} = K_\text{transl.} + K_\text{rot.}$ which is the sum of the translational and rotational kinetic energies. Note that if we use the identity $(\mathbf{A} \times \mathbf{B})^2 = \mathbf{A}^2 \mathbf{B}^2 - (\mathbf{A} \cdot \mathbf{B})^2$, we can rewrite the above expression as:

{% math() %}
\begin{align*}
K_\text{rot.} &= \dfrac{1}{2} \sum_i m_i (\vec \omega \times \mathbf{r}_i)^2 \\
&= \dfrac{1}{2} \sum_i m_i \left[\omega^2 \mathbf{r}_i^2 - (\vec \omega \cdot \mathbf{r}_i)^2\right]
\end{align*}
{% end %}

Where here, $\omega^2 = \vec \omega \cdot \vec \omega$ and {% inlmath() %}\mathbf{r}_i^2 = \mathbf{r}_i \cdot \mathbf{r}_i{% end %}. But the angular velocity is a _vector_ (technically, pseudovector, but that distinction can be ignored here), which can be written in tensor form as {% inlmath() %}\omega_j = \sum_{k=1}^3 \omega_k \delta_{jk}{% end %}, where {% inlmath() %}\delta_{jk}{% end %} is the identity matrix, given by:

{% math() %}
\delta_{ij} = \begin{pmatrix*}
\delta_{11} & \delta_{12} & \delta_{13} \\
\delta_{21} & \delta_{22} & \delta_{23} \\
\delta_{31} & \delta_{32} & \delta_{33}
\end{pmatrix*} =\begin{pmatrix*}
1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1
\end{pmatrix*}
{% end %}

If this tensor notation is unfamiliar, the idea is that when we want to compute the $j$-th component of the angular velocity (for instance, $\omega_1$, the $x$-component of $\vec \omega$), we substitute in $j = x$ and plug that into the sum, which gives:

{% math() %}
\begin{align*}
\omega_1 &= \sum_{k=1}^3 \omega_k \delta_{1k} \\
&= \omega_1 \delta_{11} + \omega_2{\delta}_{12} + \omega_3 \delta_{13} \\
&= \omega_1 (1) + 0 + 0 \\
&= \omega_1
\end{align*}
{% end %}

Similarly, notice that the position of each particle, which we referred to as {% inlmath() %}\mathbf{r}_i{% end %}, may be written as {% inlmath() %}r_b = \sum_{a = 1}^3 r_a^{(i)}\delta_{ab}{% end %}, such that {% inlmath() %}\mathbf{r}_i \cdot \mathbf{r}_i{% end %} becomes:

{% math() %}
\begin{align*}
\mathbf{r}_i \cdot \mathbf{r}_i &= r_b\, r_b \\
&= \sum_{a = 1}^3 r_a^{(i)}\delta_{ab} \sum_{a = 1}^3 r_a^{(i)}\delta_{ab} \\
&= \sum_{a = 1}^3 {r_a^{(i)}}^2
\end{align*}
{% end %}

Since $\delta_{ab} \delta_{ab} = \delta_{ab}$ (the matrix product of the identity matrix with an identity matrix is still an identity matrix) - note that this is true for the identity matrix regardless of which indices you use, so we find that:

{% math() %}
\begin{align*}
\omega^2 &= \vec \omega \cdot \vec \omega \\
&= \omega_j \,\omega_j \\
&= \sum_{k=1}^3 \omega_k \delta_{jk} \sum_{k=1}^3 \omega_k \delta_{jk} \\
&= \sum_{k=1}^3 \omega_k^2 \cancel{\delta_{jk} \delta_{jk}}^1 \\
&= \sum_{k=1}^3 \omega_k^2
\end{align*}
{% end %}

On substituting our new definitions for $\omega^2$ and $\mathbf{r}_i^2$, we have:

{% math() %}
\begin{align*}
K_\text{rot.} &= \dfrac{1}{2} \sum_i m_i \left[\omega^2 \mathbf{r}_i^2 - (\vec \omega \cdot \mathbf{r}_i)^2\right] \\
&=\dfrac{1}{2} \sum_i m_i \left[\left(\sum_{k=1}^3 \omega_k^2\right)^2 \left(\sum_{a = 1}^3 {r_a^{(i)}}^2\right) - \left(\sum_{a = 1}^3 r_a^{(i)}\omega_a\right)\left(\sum_{k = 1}^3 r_k^{(i)}\omega_k\right)\right] \\
&= \dfrac{1}{2} \sum_i m_i \sum_{a= 1}^3 \sum_{k = 1}^3\left[\omega_a \omega_k \delta_{ak} \sum_{a=1}^3 {r_a^{(i)}}^2 - \omega_a \omega_k r_a^{(i)} r_k^{(i)}\right] \\
&= \dfrac{1}{2} \sum_{a= 1}^3 \sum_{k = 1}^3 \omega_a \omega_k\underbrace{\sum_i m_i \left[\left(\delta_{ak} \sum_{a=1}^3 {r_a^{(i)}}^2\right) - r_a^{(i)} r_k^{(i)}\right]}_{I_{ak}} \\
&= \sum_{a= 1}^3 \sum_{k = 1}^3 \dfrac{1}{2} I_{ak} \omega_a \omega_k
\end{align*}
{% end %}

Note how in the second-last line, we defined a special matrix $I_{ak}$, given by:

{% math() %}
I_{ak} = \sum_i m_i \left[\left(\delta_{ak} \sum_{a=1}^3 {r_a^{(i)}}^2\right) - r_a^{(i)} r_k^{(i)}\right]
{% end %}

This is the **moment of inertia** in its _most general form_, called the _moment of inertia tensor_, or just **inertia tensor** for short. In 3D, it is written as a $(3 \times 3)$ matrix. Note that along the diagonals of the inertia tensor, since $\delta_{ak} = 1$ when $a = k$, we have:

{% math() %}
I_{aa} = \sum_i m_i \left[\left(x_a^{{(i)}^2} + y_a^{{(i)}^2} + z_a^{{(i)}^2}\right) - \left(r_a^{(i)}\right)^2\right]
{% end %}

Where $r_a = (r_1, r_2, r_3) = (x, y, z)$ is the tensor expression for the $a$-th component of the position, and $r_a^{(i)} = (r_1^{(i)}, r_2^{(i)}, r_3^{(i)}) = (x^{(i)}, y^{(i)}, z^{(i)})$ is the position of the $i$-th particle. Meanwhile, for the non-diagonals (cross terms) of the inertia tensor, since $\delta_{ak} = 0$ when $a \neq k$, we have:

{% math() %}
I_{{ak},\, \text{cross}} = -\sum_i m_i r_a^{(i)} r_k^{(i)}
{% end %}

We notice that in the limiting case, as the number of particles grows very large, this expression reduces to the familiar expression of the rotational kinetic energy:

{% math() %}
K = \dfrac{1}{2} I \omega^2
{% end %}

> **Note:** The inertia tensor $I_{ak}$ is the collective description of the moment of inertia of a _system_ of $N$ particles, where $N$ can be arbitrarily-large. This means that in our definition of the inertia tensor $I_{ak} = \displaystyle \left[\sum_i m_i \left(\delta_{ak} \sum_{a=1}^3 {r_a^{(i)}}^2 \right) - r_a^{(i)} r_k^{(i)}\right]$, we must remember to sum over every particle; that is, the index $i$ sums from the first particle to the last ($N$-th) particle.