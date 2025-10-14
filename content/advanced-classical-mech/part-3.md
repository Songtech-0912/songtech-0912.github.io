+++
title = "Advanced Classical Mechanics, Part III"
date = 2025-01-26
draft = false
+++

In this third (and final) part of the classical mechanics series, we delve into the physics of rotational motion and interacting systems of particles. We learn about the harmonic oscillator and its many generalizations. And we conclude our journey on classical mechanics by discussing oscillating systems, eventually taking us to continuous oscillations and waves.

<!-- more -->

Again, remember that this is part of the **advanced classical mechanics series**, which I have split into several parts to not be overly long. A complete catalogue of the entire three-part guide is shown below:

> ### Chapter guide for classical mechanics
>
> - [Go to part 1 of the series](@/advanced-classical-mech/index.md) for Newtonian mechanics and special relativity
> - [Go to part 2 of the series](@/advanced-classical-mech/part-2.md) for Lagrangian and Hamiltonian formulations of classical mechanics
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

> **Note:** The inertia tensor $I_{ak}$ is the collective description of the moment of inertia of a _system_ of $N$ particles, where $N$ can be arbitrarily-large. This means that in our definition of the inertia tensor $I_{ak} = \displaystyle \sum_i m_i \left[\left(\delta_{ak} \sum_{a=1}^3 {r_a^{(i)}}^2 \right) - r_a^{(i)} r_k^{(i)}\right]$, we must remember to sum over every particle; that is, the index $i$ sums from the first particle to the last ($N$-th) particle.

### The physical meaning of the inertia tensor

We have seen that the inertial tensor takes the mathematical form:

{% math() %}
I_{ak} = \sum_i^{N_\text{particles}} m_i \left[\delta_{ak} \sum_{a=1}^3 r_a^{(i)} - r_a^{(i)} r_k^{(i)}\right]
{% end %}

If we wanted to expand the inertia tensor into its respective components, we have:

{% math() %}
I_{ak}
= \begin{bmatrix}
I_{11} & I_{12} & I_{13} \\
I_{21} & I_{22} & I_{23} \\
I_{31} & I_{32} & I_{33}
\end{bmatrix}
= \begin{bmatrix}
\sum_i m_i (y_i^2 + z_i^2) & - \sum_i m_i x_i y_i & -\sum_i m_i x_i z_i \\
-\sum_i m_i y_i x_i & \sum_i m_i(x_i^2 + z_i^2) & - \sum_i m_i y_i z_i \\
-\sum_i m_i z_i x_i & -\sum_i m_i z_i y_i & \sum_i m_i(x_i^2 + y_i^2)
\end{bmatrix}
{% end %}

> **Note:** Notice how $I$ is symmetric about the diagonal: $I_{12} = I_{21}, I_{31} = I_{13}, I_{23} = I_{32}$, and so forth. In general, $I_{ak} = I_{ka}$. This is very nice for calculation purposes: it means that instead of calculating all 9 components in the inertia tensor, we may just calculate the 3 components along the diagonal and the three components ($I_{12}$, $I_{13}$, and $I_{23}$) above the diagonal (so just 6 components in total), and by symmetry we know the remaining 3 components, saving us quite a bit of work.

Now let us discuss the _physical interpretation of the inertia tensor_: it describes how a rigid object's distribution of mass is related to _how it spins_ in each direction. Just as mass measures the resistance of an object to be *moved* (remember Newton's first law), moment of inertia measures the resistance of an object to be _spun_. A large mass requires a large force to accelerate it to a certain speed; similarly, a rotating object with a large moment of inertia requires a large _torque_ to accelerate it to a certain angular velocity. The same principle applies to a small mass, and to a small moment of inertia: a small moment of inertia means that an object requires only a small torque to begin spinning. This is why Newton's second law for the force, $\mathbf{F} = m\mathbf{a} = m \dot{\mathbf{v}}$, has a rotational equivalent $\vec \tau = I \dot{ \vec \omega}$.

#### Addennum: the inertia tensor as a tensor

While the name of the inertia tensor may seem like an unimportant detail, we call the inertia tensor a _tensor_ for a very important reason - the name is not arbitrary! It is a _tensor_, not just a matrix, because while its _components_ depend on the coordinate system chosen (which also determines the position and orientation of the axis of rotation), the _inertia_ of the object is a physical quantity that stays the same. This is just like how a force on an object, which is a vector, may be expressed in different coordinates, but of course the object feels the same force, which means that forces, and in general **all vectors**, are _tensors_. This property of invariance under transformation is what makes it a **tensor**, because tensors are _defined_ as objects that stay the same under transformation of coordinates.

### Moment of inertia in many-body systems

While the rigid object may be considered a single object, it should be considered a collection of many, many individual particles, summed over all particles $i_1, i_2, \dots, i_{N}$ where $N$ is the total number of particles (which can be a lot!). And since the kinetic energy is based on an object's kinetic mass, then the total kinetic energy of the collection of particles (and thus of the rigid body) would be given by:

{% math() %}
\begin{align*}
K_\text{rot} &= \dfrac{1}{2} \sum_{a = 1}^3 \sum_{k = 1}^3 I_{ak} \omega_a \omega_k \\
&= \begin{pmatrix} \omega_1 & \omega_2 & \omega_3 \end{pmatrix}
\dfrac{1}{2}
\begin{bmatrix}
I_{11} & I_{12} & I_{13} \\
I_{21} & I_{22} & I_{23} \\
I_{31} & I_{32} & I_{33} \\
\end{bmatrix}
\begin{pmatrix} \omega_1 \\ \omega_2 \\ \omega_3 \end{pmatrix}
\end{align*}
{% end %}

### The continuum form of the inertia tensor

Let us now consider what happens as we go from a _discrete_ collection of particles to a _continuous distribution_. In such a case, instead of summing over distinct particles, we have an integral over a _mass density_ $\rho(\mathbf{r})$ across the volume the object occupies $V$, such that:

{% math() %}
I_{ak} = \int_V \rho(\mathbf{r}) \left[\delta_{ak} \sum_{a=1}^3 r_a^2 - r_a r_k\right]\, dV
{% end %}

> **An intuitive look at the inertia tensor for continuous objects:** One way to think of it is that as the number of particles grows to be very, very large, then the individual masses of each particle $m_i$ grows very small, so we have $m_i \to dm$, where $dm$ is an infinitesimal amount of mass. Since the mass density $\rho$ is given by $\rho(\mathbf{r}) = \dfrac{dm}{dV}$, we can rearrange it to find that $dm = \rho dV$, and replace the sum with an integral, from which the inertia tensor for continuous object naturally emerges.

As an example, consider a rectangular plate of uniform density $\rho$, of dimensions length $a$, width $b$, and height $c$, with total mass $M$, as shown:

{{ diagram(
	src="../momentum-of-inertia-box.excalidraw.svg"
	desc="A diagram of a box of length a, width b, and height c, with a Cartesian coordinate system with the axes x1, x2, x3."
) }}

Let us calculate the $I_{11}$ component, that is, the moment of inertia with respect to the $x_1$ axis of rotation. By our previous expression for the moment of inertia in the continuous case, we have:

{% math() %}
\begin{align*}
I_{11} &= \int_V \rho \left[\delta_{11} \sum_{a=1}^3 r_a - r_a r_1\right]\, dV \\
&= \int_V \rho (x_2^2 + x_3^2)\, dV \\
&= \int_V \rho x_2^2\, dV + \int_V \rho x_3^2\, dV \\
&= \rho\int_V (\mathbf{r}) x_2^2\, dV + \rho\int_V (\mathbf{r})x_3^2\, d \\ 
&= \rho \int_{-a/2}^{a/2} dx_1 \int_{-b/2}^{b/2} x_2^2 dx_2 \int_{-c/2}^{c/2} dx_3 + \\
&\qquad \rho \int_{-a/2}^{a/2} dx_1 \int_{-b/2}^{b/2} dx_2 \int_{-c/2}^{c/2} x_3^2 dx_3 \\
&= \rho \left[ac \dfrac{1}{3}x_2^2\right]_{-b/2}^{b/2} + \left[ab \dfrac{1}{3} x_3^2\right]_{-c/2}^{c/2} \\
&= \dfrac{1}{2} \dfrac{M}{abc} [ab^3 c + abc^3] \\
&= \dfrac{1}{12} M(b^2 + c^2)
\end{align*}
{% end %}

We may apply the same procedure to be able to calculate the rest of the components:

{% math() %}
\begin{align*}
I_{22} &= \dfrac{1}{12} M(a^2 + c^2) \\
I_{33} &= \dfrac{1}{12} M(a^2 + b^2) \\
I_{12} &= I_{13} = I_{23} = 0
\end{align*}
{% end %}

Recall that since the moment of inertia tensor is symmetric across the diagonal, we also know that $I_{21} = I_{31} = I_{32} = 0$. Thus our moment of inertia tensor becomes:

{% math() %}
I_{ak} = \dfrac{1}{12}M\begin{bmatrix*}
b^2 + c^2 & 0 & 0 \\ 0 & a^2 + c^2 & 0 \\ 0 & 0 & a^2 + b^2
\end{bmatrix*}
{% end %}

Which gives the moment of inertia for rectangular plate rotating in any direction in 3D space. Note that if we let $c \ll b, c \ll a$ (that is, if the rectangular plate is very thin), then its inertia tensor becomes:

{% math() %}
I_{ak} = \dfrac{1}{12}M\begin{bmatrix*}
b^2 & 0 & 0 \\ 0 & a^2 & 0 \\ 0 & 0 & a^2 + b^2
\end{bmatrix*}
{% end %}

> **Note:** for the inertia tensors of other common physical configurations, [the Wikipedia article on moments of inertia](https://en.wikipedia.org/wiki/List_of_moments_of_inertia) provides many, many examples.

### Principal axes and moments of inertia

As we have seen in our examples, the inertia tensor frequently has off-diagonal components. This is because the inertia tensor is axis-dependent, and the moment of inertia for a sphere for instance, along an axis oriented at 45 degrees from the vertical versus an axis oriented directly vertically is going to be different. This is an issue if we want to calculate the rotational kinetic energy or the angular momentum, which are given by:

{% math() %}
\begin{align*}
K_\text{rot.} = \dfrac{1}{2} \sum_i \sum_j I_{ij} \omega_i \omega_j, \quad
L_i = \sum_j I_{ij} \omega_j
\end{align*}
{% end %}

The off-diagonal components of the inertia tensor makes using these formulas for calculations much more complicated, because you need to sum over all of the terms on the off-diagonals as well as the diagonal terms. Luckily, there is a way to determine the most preferable choice of axes, for which the inertia tensor _is_ diagonal. These preferred axes are known as the **principal axes**.

To calculate the principal axes, we must first calculate the **eigenvectors** of the inertia tensor $I_{ij}$ by solving the eigenvalue equation $I_{ij} \mathbf{v} = \lambda \mathbf{v}$ for all possible solutions $\mathbf{v}_n$. If you haven't solved eigenvalue equations before, you can consult [this online textbook](https://math.libretexts.org/Bookshelves/Linear_Algebra/A_First_Course_in_Linear_Algebra_(Kuttler)/07%3A_Spectral_Theory/7.01%3A_Eigenvalues_and_Eigenvectors_of_a_Matrix) for a guide. The eigenvectors {% inlmath() %}\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_n{% end %} are known as the **principal axes**.

From there, we may construct a matrix $P$ with the principal axes (eigenvectors) $\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_n$ as its columns, as shown below:

{{ diagram(
	src="../matrix-column-space.excalidraw.svg"
	desc="The matrix P composed of eigenvectors v1, v2, ... as its rows"
) }}

> **Note:** in case this was not clear, each of the columns of $P$ are formed by one of the eigenvectors $\mathbf{v}_n$. For instance, column 1 is the first eigenvector, column 2 is the second eigenvector, and so forth.

Finally, we can **diagonalize** the inertia tensor to transform it to our new set of axes, giving us a new inertia tensor $I_{ij, \mathbf{p}}$ ("p" for _principal_) given by:

{% math() %}
I_{ij, \mathbf{p}} = P^{-1} I_{ij} P
{% end %}

Where $P^{-1}$ is the matrix inverse of $P$. This new inertia tensor $I_{ij, \mathbf{p}}$ is a purely diagonal matrix, and has the form:

{% math() %}
I_{ij, \mathbf{p}} = \begin{pmatrix}
I_{11}' & 0 & 0 \\
0 & I_{22}' & 0 \\
0 & 0 & I_{33}'
\end{pmatrix}
{% end %}

The diagonal elements $I_{11}', I_{22}', I_{33}'$ are the *only* nonzero elements, and they are called the **principal moments of inertia**. They are the moments of inertia of the object *when* it rotates along its principal axes, and they come naturally from finding the diagonalized inertia tensor.

### Parallel- and perpendicular-axis theorems

In some cases, calculating all components of the inertia tensor for a continuous body can be exceptionally difficult. It is then advantageous to use either the **parallel-axis theorem** or **perpendicular-axis theorem**. Both theorems allow calculating an unknown inertia tensor using a known inertia tensor at a different location.

The **parallel-axis theorem** (also called _Steiner's theorem_) is used when we know (or can more easily calculate) the inertia tensor from a coordinate system centered a distance $\mathbf{r}$ from the center-of-mass of a continuous body. We refer to this known inertia tensor as $I_{ij}'$. As long as our coordinate systems have **parallel axes**, we can then find the center-of-mass inertia tensor $I_{ij}$ with:

{% math() %}
I_{ij} = I_{ij}' - M(r^2 \delta_{ij}  - r_i r_j)
{% end %}

> **Note:** You may recognize this in the more familiar form $I_{CM} = I - Mh^2$ from the [classical dynamics](@/classical-dynamics.md) guide, which is the one-dimensional special case of the parallel-axis theorem.

The **perpendicular-axis theorem** is less-used, as it only applies to objects that lie on a 2D Cartesian plane (and thus satisfies $z = 0$). However, _if_ this is the case, then we have:

{% math() %}
I_{zz} = I_{xx} + I_{yy}
{% end %}

This allows us to determine the moment of inertia along the $z$ axis by just knowing the two moments of inertia along the $x$ and $y$ axes.

## Harmonic oscillators and oscillatory systems

Oscillators are a fundamental part of physics, and arise from all branches in physics, including acoustics, optics, the study of springs and pendulums, waves, and even in quantum physics. We will dedicate this section to exploring the physics of oscillators in classical mechanics.

### The simple harmonic oscillator

We will first examine the _simple harmonic oscillator_. While this is often introduced in terms of oscillating springs, we will discuss its more generalized case. Let us consider an object whose potential energy is given by $U(x)$. Now, assume that the object is _very near_ a stable equilibrium (and therefore local minimum) of $U(x)$. This means that we may expand the potential energy as a Taylor expansion. If we define our coordinate system such that the object's position

{% math() %}
U(x) = U_0 + U'(0) x + \dfrac{1}{2} U''(0)x^2 + \dfrac{1}{6} U'''(0) x^3 + \dots
{% end %}

Since the object is near a local minimum of $U(x)$, by definition, $U'(0) = 0$ (since at minima, $U'(x) = 0$). Therefore, we have:

{% math() %}
U(x) = U_0 + \dfrac{1}{2}U''(0) x^2
{% end %}

Let $U''(0) = k$ as a constant value. Remember that we can shift the potential by an arbitrary constant without changing it, so we can subtract the constant $U_0$ such that our potential is simply:

{% math() %}
U(x) = \dfrac{1}{2} kx^2 = \dfrac{1}{2} m \omega_0^2 x^2
{% end %}

> **Note:** It is common to denote the **angular frequency** with $\omega$ where $k = m \omega_0^2$, which also means that $\omega_0 = \sqrt{\dfrac{k}{m}}$.

Thus, substituting our approximate potential into Newton's second law yields:

{% math() %}
m\ddot x = F = -\dfrac{dU}{dx} = -k x
{% end %}

This is the differential equation for the **simple harmonic oscillator**. Solving for this differential equation - $\ddot x = -(k/m) x$ - yields the general solution given by:

{% math() %}
x(t) = A \cos (\omega_0 t + \phi)
{% end %}

This is the solution for the **simple harmonic oscillator**. It describes an oscillating system with _amplitude_ $A$, *angular frequency* $\omega_0$, and *phase shift* $\phi$. The amplitude and phase shift are determined by the initial conditions imposed on the system - for now, it is important to just recognize they are constants. From $x(t)$ we may calculate the kinetic energies:

{% math() %}
K = \dfrac{1}{2} m \omega_0^2 A^2 \sin^2(\omega_0 - \phi) = \dfrac{1}{2} kA^2 \sin^2(\omega_0 t - \phi)
{% end %}

Since the oscillations are the result of work done by conservative force across a displacement (remember, work is done whenever a force is applied that moves the object or system _out of equilibrium_), the potential energy can be found through the work done by the force:

{% math() %}
\begin{gather*}
W = \int k x d x = \dfrac{1}{2} kx^2 = U(x) \\
\Rightarrow U(x) = \dfrac{1}{2} kA^2 \cos^2(\omega_0 t - \phi)
\end{gather*}
{% end %}

Thus we find that the sum of the kinetic and potential energies gives:

{% math() %}
\begin{align*}
E &= K + U \\
&= \dfrac{1}{2} kA^2 \sin^2(\omega_0 t - \phi) +\dfrac{1}{2} kA^2 \cos^2(\omega_0 t - \phi) \\
&= \dfrac{1}{2} kA^2 [\sin^2(\omega_0 t - \phi) + \cos^2(\omega_0 t - \phi)] \\
&= \dfrac{1}{2} kA^2 = \text{const.}
\end{align*}
{% end %}

Thus we see that the energy is actually a _constant_, which is what we would expect of a conservative force (which would therefore satisfy the conservation of energy). Note that the period of oscillations (the time it takes to complete one oscillation cycle and return to its starting point) is _independent_ of the amplitude. This means that the period is also a constant, and thus thes system always oscillates between $[-A, A]$. This period $T$ (and associated frequency $f$) is given by:

{% math() %}
\begin{matrix*}
T = \dfrac{1}{f} =\dfrac{2\pi}{\omega_0} = 2\pi \sqrt{\dfrac{m}{k}},
& f = \dfrac{1}{2\pi} \sqrt{\dfrac{k}{m}}
\end{matrix*}
{% end %}

### The dampened harmonic oscillator

Unfortunately, the simple harmonic oscillator is a very basic model. In fact, a simple harmonic oscillator would (in theory) oscillate forever, which is clearly not very realistic. We will now consider a more _realistic case_, the **dampened harmonic oscillator**, where dampening forces are present that slow the oscillations over time.

Consider a one-dimension oscillating object that experiences a dampening force given by $F = b \dot x$ (this could model drag, friction, or some other dampening force). By applying Newton's second law, we have:

{% math() %}
m \ddot x + b \dot x = - \dfrac{dU}{dx} = -kx
{% end %}

Rearranging, we have a cleaner differential equation form given by:

{% math() %}
\ddot x + \dfrac{b}{m} \dot x + \dfrac{k}{m} x = 0
{% end %}

If we define $\omega_0^2 \equiv k/m$ and $\beta = b/2m$, where $\beta$ is the **dampening parameter** proportional to the dampening force(s), our differential equation takes the form:

{% math() %}
\dfrac{d^2 x}{dt^2} + 2\beta \dfrac{dx}{dt} + \omega_0^2 x = 0
{% end %}

This equation is a second-order linear differential equation with constant coefficients, something that can be solved using the standard methods of differential equations (which you can read about in the [differential equations guide](@/differential-equations/index.md)). Here we won't solve it - we will just state its general solution:

{% math() %}
x(t) = e^{-\beta t} \left(A_1 \exp \left(\sqrt{\beta^2 - \omega_0^2}t\right) + A_2 \exp \left(-\sqrt{\beta^2 - \omega_0^2}t\right)\right)
{% end %}

Here, $A_1, A_2$ are undetermined amplitudes (that we'd need to find for a specific system based on initial conditions), $\beta$ is the dampening parameter, and we have

- If $\omega_0^2 > \beta^2$, the system is called **underdamped**
- If $\omega_0^2 = \beta^2$, the system is called **critically-damped**
- If $\omega_0^2 < \beta^2$, the system is said to be **over-damped**

A plot of the three scenarios is shown below:

![A mathematica-generated plot of the three dampening scenarios. The under-damped curve shows a decaying sinusoid, the critically-damped curve shows a rapid exponential decay, and the over-damped scenario shows a slow exponential decay](../dampened-oscillators-plots.png)

#### Under-damping

Let us first explore the first case of under-damping. If we have $\omega_0^2 > \beta^2$, then $\pm \sqrt{\beta^2 - \omega_0^2}t$ would be _imaginary_. If we define $\tilde \omega \equiv \sqrt{\beta^2 - \omega_0^2}$, then we can write:

{% math() %}
x(t) = e^{-\beta t}\left(A_1 e^{i \tilde \omega t} + A_2 e^{-i \tilde \omega t}\right)
{% end %}

If we have $A_1 = A_2 = A$, it is possible to rewrite this expression as:

{% math() %}
x(t) = Ae^{-\beta t} \cos(\tilde \omega t - \delta)
{% end %}

We say that $Ae^{-\beta t}$ is the **damping envelope** - it represents the amplitude as a function of time. The amplitude $A_\text{osc.}(t) = Ae^{-\beta t}$ therefore decays over time, and since $\tilde \omega \neq \omega_0$ (except for $\beta = 0$), we also find that **the period of oscillations is non-constant**, and in fact would grow longer over time.

#### Critical damping

When we have a critically-damped system, where $\beta^2 = \omega_0^2$, the general solution for $x(t)$ reduces to:

{% math() %}
x(t) = A_1e^{-\beta t}
{% end %}

The oscillations of $x(t)$ approach zero more quickly than for either of the two other types of damping, regardless of the initial conditions. This is important for galvanometers, which must be critically-damped to ensure they operate correctly.

#### Over-damping

When we have $\beta^2 > \omega_0^2$, then $\tilde \omega = \sqrt{\beta^2 - \omega_0^2}$ would always be real. Thus the solution becomes:

{% math() %}
x(t) = e^{-\beta t} \left(A_1 e^{\tilde \omega t} + A_2 e^{-\tilde \omega t}\right) = A_3\cosh(\tilde \omega t) e^{-\beta t}
{% end %}

Where $A_1, A_2, A_3$ are undetermined coefficients that require initial conditions to be set to be solved for. In this case, the solution is completely real; instead of complex exponentials (whose real parts are sinusoidal in nature), we simply have regular exponentials, so in fact we observe _no oscillations_ at all. Instead, the system slowly decays from its initial position $x_0$ to zero.

### The driven damped oscillator

We can now examine a more sophisticated version of the dampened harmonic oscillator: the **driven damped oscillator**. The driven damped oscillator adds an _external force_ to the oscillating system, called the **driving force**. This may be, for instance, a force in the form $\tilde F = F_0 \cos \omega t$ - physical models described by driven damped oscillators include [RLC circuits](https://en.wikipedia.org/wiki/RLC_circuit) in electromagnetism. In the case of a driven damped oscillator, Newton's 2nd law in one dimension ($F = m\ddot x$) then reads:

{% math() %}
F = m \ddot x = -kx - b \dot x + \underbrace{F_0 \cos \omega t}_\text{driving force}
{% end %}

Following our previous example, we can rearrange this to:

{% math() %}
\ddot x + 2\beta \dot x + \omega_0^2 x = A \cos \omega t, \quad A \equiv F_0/m
{% end %}

We may recognize this as the **inhomogenous** version of the differential equation for the dampened harmonic oscillator - in simpler terms, it is the same as the differential equation for the dampened harmonic oscillator, but with a nonzero right-hand side. The solution to the differential equation can be found by using any of the methods of solving inhomogeneous 2nd-order differential equations, including the [method of undetermined coefficients](@/differential-equations/index.md#the-method-of-undetermined-coefficients). But in the interest of avoiding showing a lot of math, we will simply state the general solution here:

{% math() %}
\begin{align*}
x(t) &= \bigg(A- D\left[(\omega_0^2 - \omega^2) \cos \delta + 2\omega \beta \sin \delta\right]\bigg) \cos \omega t \\
&\qquad \qquad- \bigg(D\left[(\omega_0^2 - \omega^2) \sin \delta - 2\omega \beta \cos \delta \right]\bigg) \sin \omega t = 0
\end{align*}
{% end %}

Where $D$ is a yet-undetermined coefficient $\tan \delta = \dfrac{2\omega \beta}{\omega_0^2 - \omega^2}$ and $A = F_0/m$, as with before. Note that this solution has an interesting quirk: the _only_ valid solutions must be those for which $D = 0$, because $C_1 \sin(\omega t) + C_2\cos(\omega t) = 0$ is an equation that can only be true when $C_1 = C_2 = 0$. The intuitive reason why is that sine and cosine are basically the same curve shifted by $\pi/2$. Thus, their sum $\cos \omega t + \sin \omega t$ is always nonzero, unless we multiply both sinusoids by zero. Using this fact - and with a long mathematical derivation we will not show here - we can express the general solution as a sum of the solution we previously figured out for the (undriven) *damped harmonic oscillator*, $x_\text{damp.}(t)$, and an extra driving term $x_D(t)$:

{% math() %}
x(t) = x_\text{damp.}(t) + x_D(t), \quad x_D(t) \equiv \dfrac{A \cos (\omega t - \delta)}{\sqrt{(\omega_0^2 - \omega^2)^2 + 4\omega^2 \beta^2}}
{% end %}

> **Note:** You will also see $x_D(t)$ denoted as $x_P(t)$ and for it to be called the **particular solution**. This name comes from the language of differential equations, but it is physically equivalent to the name we use of "driving term".

For $t \gg 1/\beta$, the solution reaches a **steady state**, since $x_\text{damp.}(t) \to 0$, meaning that $x_P(t)$ becomes the only nonzero term. The system then oscillates at (angular) frequency $\omega$, the same as the driving force $\tilde F = F_0 \cos \omega t$.

### Two-body systems of coupled oscillators

A yet more sophisticated version of the oscillator is the **coupled harmonic oscillator**, where several bodies, connected to each other, are oscillating in motion. The motion of many bodies is quite complicated and very difficult to analyze separately. However, there is a way to make the problem tractable: we can choose a system of coordinates, called **normal coordinates**, such that the motion of each individual oscillating body can be considered _relative_ to the system of normal coordinates. This allows the motion to be constrained so that _only one_ normal coordinate varies with time.

Let's go through what we mean. Consider a system of $n$ oscillators. The system would have $n$ normal modes (although they are not necessarily distinct; if they are repeated, we call them **degenerate modes**, and yes, physicists are _horrible_ at naming things). In the case that $n = 2$, where we have two bodies of masses $m_1 = m_2$ and positions $x_1(t), x_2(t)$ (using a coordinate systems centered at their equilibrium position), we have two normal modes.

{{ diagram(
	src="../coupled-harmonic-oscillator.excalidraw.svg"
	desc="A diagram showing two masses that are attached to springs and are also connected to each other by a spring. Their positions are denoted x1, x2 and their masses are equal and of magnitude m."
) }}

Let us make the simplifying assumption that $m_1 = m_2 = M$. We can write down a Lagrangianfor the system, as given by:

{% math() %}
\begin{align*}
K &= \dfrac{1}{2} M \dot x_1^2 + \dfrac{1}{2} M\dot x_2^2 \\
U &= \dfrac{1}{2} \kappa x_1^2 + \dfrac{1}{2}\kappa x_2^2 + \dfrac{1}{2} \kappa_{12}(x_1 - x_2)^2 \\
\mathcal{L} &= K - U \\
&= \dfrac{1}{2} M \dot x_1^2 + \dfrac{1}{2} M\dot x_2^2 - \dfrac{1}{2} \kappa x_1^2 - \dfrac{1}{2}\kappa x_2^2 - \dfrac{1}{2} \kappa_{12}(x_1 - x_2)^2
\end{align*}
{% end %}

Using the Euler-Lagrange equations for $x_1, x_2$, we obtain the equations of motion:

{% math() %}
\begin{align*}
\dfrac{d}{dt} \left(\dfrac{\partial \mathcal{L}}{\partial \dot x_1}\right) - \dfrac{\partial \mathcal{L}}{\partial x_1} = 0 
\Rightarrow M \ddot x_1 + \kappa x_1 + \kappa_{12} (x_1 - x_2) \\
\dfrac{d}{dt} \left(\dfrac{\partial \mathcal{L}}{\partial \dot x_2}\right) - \dfrac{\partial \mathcal{L}}{\partial x_2} = 0 \Rightarrow M \ddot x_2 + \kappa x_2 + \kappa_{12} (x_1 - x_2)
\end{align*}
{% end %}

By a slight rearrangement, we obtain the system of second-order ODEs, given by:

{% math() %}
\begin{align*}
M\ddot x_1 + (\kappa + \kappa_{12}) x_1 - \kappa_{12} x_2 = 0 \\
M\ddot x_2 + (\kappa + \kappa_{12}) x_2 - \kappa_{12} x_1 = 0
\end{align*}
{% end %}

We can solve the system by assuming solutions in the form $x_1(t) = B_1 e^{i\omega t}$ and $x_2 = B_2 e^{i\omega t}$ (where $B_1, B_2$ are undetermined coefficients that may be complex). This is a good guess because such solutions would have oscillatory behavior, and we extract purely their real part at the end to get the real-valued expression for $x_1(t), x_2(t)$. By substitution, we have:

{% math() %}
\begin{align*}
\ddot x_1 &= -B_1 \omega^2 e^{i\omega t} \\
& \quad \Rightarrow M B_1 \omega^2 + (\kappa + \kappa_{12})B_1 - \kappa_{12} B_2 = 0 \\
\ddot x_2 &= - B_2 \omega^2 e^{i\omega t} \\
& \quad \Rightarrow M B_2 \omega^2 + (\kappa + \kappa_{12})B_2 - \kappa_{12} B_1 = 0
\end{align*}
{% end %}

The system of equations can then be written in the form:

{% math() %}
\begin{bmatrix}
\kappa + \kappa_{12} - M\omega^2 & -\kappa_{12} \\
-\kappa_{12} & \kappa + \kappa_{12} - M\omega^2
\end{bmatrix}
\begin{bmatrix}
B_1 \\ B_2
\end{bmatrix}
= \begin{bmatrix}
0 \\ 0
\end{bmatrix}
{% end %}

For nontrivial solutions, the left matrix must in general be a **singular matrix**, meaning that its determinant must be zero, and we can treat this as an **eigenvalue problem** and solve for the eigenvalues. Thus, taking the determinant, we can rewrite it as:

{% math() %}
\det \begin{vmatrix}
\kappa + \kappa_{12} - M\omega^2 & -\kappa_{12} \\
-\kappa_{12} & \kappa + \kappa_{12} - M\omega^2
\end{vmatrix} = 0
{% end %}

Solving the characteristic equation results in:

{% math() %}
\begin{align*}
(\kappa + \kappa_{12} - M \omega^2)^2 - \kappa_{12}^2 = 0 \\
\kappa + \kappa_{12} - M \omega^2 = \pm \kappa_{12} \\
\Rightarrow \omega = \pm \sqrt{\dfrac{\kappa + \kappa_{12} \pm \kappa_{12}}{M}}, \\
\omega_1 = \pm \sqrt{\dfrac{\kappa + 2\kappa_{12}}{M}}, \, \omega_2 = \pm \sqrt{\dfrac{k}{m}}
\end{align*}
{% end %}

We have therefore found the eigenvalues - which we call **eigenfrequencies** (or _characteristic frequencies_) $\omega_1, \omega_2$. Now, if we define the coordinates:

{% math() %}
\begin{align*}
\eta_1 = x_1 - x_2  \\
\eta_2 = x_1 + x_2
\end{align*}
{% end %}

Which leads to the following identities:

{% math() %}
\begin{align*}
x_1 = \dfrac{1}{2}(\eta_2 + \eta_1) \\
x_2 = \dfrac{1}{2}(\eta_2 - \eta_1)
\end{align*}
{% end %}

We can therefore take the time derivatives and substitute them into the coupled differential equations that we have before, which gives:

{% math() %}
\begin{gather*}
M\ddot x_1 + (\kappa + \kappa_{12}) x_1 - \kappa_{12} x_2 = 0 \\
\Rightarrow M(\ddot \eta_2 + \ddot \eta_1) + (\kappa + \kappa_{12})(\eta_2 + \eta_1) - \kappa_{12}(\eta_2 - \eta_1) = 0 \\
M\ddot x_2 + (\kappa + \kappa_{12}) x_2 - \kappa_{12} x_1 = 0 \\
\Rightarrow M(\ddot \eta_2 - \ddot \eta_1) + (\kappa + \kappa_{12})(\eta_2 - \eta_1) - \kappa_{12}(\eta_2 + \eta_1) = 0
\end{gather*}
{% end %}

By distributing and rearranging, we can rewrite as:

{% math() %}
\begin{align*}
M(\ddot \eta_2 + \ddot \eta_1) + (\kappa + 2\kappa_{12}) \eta_1 + \kappa \eta_2 = 0 \\
M(\ddot \eta_2 - \ddot \eta_1) - (\kappa + 2\kappa_{12}) \eta_1 + \kappa \eta_2 = 0
\end{align*}
{% end %}

Now here comes a very elegant result. If we subtract the bottom differential equation from the top differential equation, and divide by $1/2$, we get:

{% math() %}
M \ddot \eta_1 + (\kappa + 2\kappa_{12}) \eta_1 = 0
{% end %}

Meanwhile, if we add the bottom differential equation to the top differential equation and divide by $1/2$, we get:

{% math() %}
M \ddot \eta_2 + \kappa \eta_2 = 0
{% end %}

So we have uncoupled the system of equations! Thus we can solve the system for $\eta_1, \eta_2$, with the solutions being:

{% math() %}
\begin{align*}
\eta_1(t) &= C_1^+ e^{i\omega_1 t} + C_1^- e^{-i\omega_1 t},\, \omega_1 = \sqrt{\dfrac{\kappa + 2\kappa_{12}}{m}} \\
\eta_2(t) &= C_2^+ e^{i\omega_2 t} + C_2^- e^{-i\omega_2 t},\, \omega_2 = \sqrt{\dfrac{k}{m}}
\end{align*}
{% end %}

Where $C_1^\pm, C_2^\pm$ represent undetermined coefficients. We have therefore arrived at the **normal modes** of the system. The coordinates $\eta_1, \eta_2$ allow us to describe the motion of the system in a much simpler way, constraining the system to reduce the complicated variables $x_1, x_2$ into the more natural coordinates $\eta_1, \eta_2$.

### Generalized problem of $N$ coupled oscillators

We are now ready to tackle the general case of an arbitrary number of coupled harmonic oscillators. Consider a system with $N$ oscillators, indexed by $k = 1, 2, 3, \dots N$. Using the generalized coordinates $q_k(t)$, we would have $k$ Euler-Lagrange equations in the form:

{% math() %}
\dfrac{\partial \mathcal{L}}{\partial q_k} - \dfrac{d}{dt} \left(\dfrac{\partial \mathcal{L}}{\partial \dot q_k}\right) = 0
{% end %}

For a problem with a large number of harmonic oscillators, solving $k$ Euler-Lagrange equations becomes non-trivial. Instead, we may choose to Taylor-expand the system around a stable equilibrium $q_{k0}$ where $\dot q_k = 0$, and center our coordinate system such that $q_{k0} = 0$. The expansion of the potential would then take the form:

{% math() %}
U(q_1, q_2, \dots, q_n) = U_0 + \sum_{k = 1}^N \dfrac{\partial U}{\partial q_k} \bigg|_0 q_k + \dfrac{1}{2} \sum_{j = 1}^N \sum_{k = 1}^N \dfrac{\partial^2 U}{\partial q_j \partial q_k} \bigg|_0 q_j q_k + \dots
{% end %}

For small oscillations about our equilibrium point (which is by definition a minimum of the potential), we have $\dfrac{\partial U}{\partial q_k} = 0$. In addition, we can define our potential energy such that $U_0 = 0$ (since we can always add or subtract a constant energy term from the potential energy). Taking terms only up to quadratic (second-order) with our given definitions, the first and second terms of the Taylor expansion disappear, so only the third term remains:

{% math() %}
U(q_1, q_2, \dots , q_n) = \dfrac{1}{2} \sum_{j = 1}^N \sum_{k = 1}^N \underbrace{\dfrac{\partial^2 U}{\partial q_j \partial q_k} \bigg|_0}_{A_{jk}} q_j q_k = \dfrac{1}{2} \sum_{j = 1}^N \sum_{k = 1}^N A_{jk} q_j q_k
{% end %}

Where $A_{jk}$ is a matrix that captures the potential energies of all the oscillators in a single matrix, which takes the form:

{% math() %}
A_{jk} = \dfrac{\partial^2 U}{\partial q_j \partial q_k} \bigg|_{q_{k0} =0}
=
\begin{pmatrix}
\frac{\partial^2 U}{\partial q_1^2} & \frac{\partial^2 U}{\partial q_1 \partial q_2}
& \dots & \frac{\partial^2 U}{\partial q_1 \partial q_n} \\
\frac{\partial^2 U}{\partial q_2 \partial q_1} & \frac{\partial^2 U}{\partial q_2^2}
& \dots & \frac{\partial^2 U}{\partial q_2 \partial q_n} \\
\vdots & \vdots & \ddots & \vdots \\
\frac{\partial^2 U}{\partial q_n \partial q_1} & \frac{\partial^2 U}{\partial q_n \partial q_2} & \dots & \frac{\partial^2 U}{\partial q_n^2}
\end{pmatrix}
{% end %}

> **Note:** This is a symmetric matrix (that is, $A_{jk} = A_{kj}$) as second partial derivatives commute, so in principle we only need to calculate the diagonal terms and the terms above the diagonal.

Meanwhile, the kinetic energy of the system of $N$ oscillators would be given by:

{% math() %}
K = \dfrac{1}{2} \sum_{j = 1}^N \sum_{k = 1}^N m_{jk} \dot q_j \dot q_k
{% end %}

Where $m_{jk}$ is a matrix of all the masses of the individual harmonic oscillators, as given by:

{% math() %}
m_{jk} = \begin{pmatrix}
  m_1 & 0 & 0 & 0\\
  0 & m_2 & \ldots & 0\\
  \vdots & \vdots & \ddots & \vdots\\
  0 & 0 & \ldots & m_n
\end{pmatrix}
{% end %}

Currently, we have our kinetic energy in terms of a coordinate-independent tensor; to explicitly specify its form in Cartesian coordinates (where we have three components $x, y, z$, and thus we sum from 1 to 3), we have:

{% math() %}
T = \dfrac{1}{2} \sum_{\alpha = 1}^N \sum_{i = 1}^3 m_\alpha \dot x_{i^{(\alpha)}}^2
{% end %}

Where $x_{i^{(\alpha)}}^2$ denotes the $i$th coordinate $x_i = (x, y, z)$ of the $\alpha$-th oscillator. To convert this Cartesian form back to generalized coordinates, we would need to perform a coordinate transformation using:

{% math() %}
\begin{align*}
x_{i, \alpha} &= x_{i^{(\alpha)}}(q_1, q_2, \dots, q_n) \\
\dot x_{i, \alpha} &= \sum_{k = 1}^N \dfrac{\partial x_{i^{(\alpha)}}}{\partial q_k} \dot q_k \\
\end{align*}
{% end %}

After substituting into the form of the kinetic energy we previously wrote, the kinetic energy thus becomes:

{% math() %}
\begin{align*}
T = \dfrac{1}{2} \sum_{\alpha = 1}^N \sum_{j, k}^N \sum_{i = 1}^3 m_\alpha \dfrac{\partial x_{i^{(\alpha)}}}{\partial q_j} \dfrac{\partial x_{i^{(\alpha)}}}{\partial q_k} \dot q_j \dot q_k
\end{align*}
{% end %}

Upon which we may make the identification that the matrix $m_{jk}$ transforms into our coordinates $x_{i^{(a)}}$ according to:

{% math() %}
m_{jk} = \sum_{\alpha = 1}^N \sum_{i = 1}^3 m_\alpha \dfrac{\partial x_{i^{(\alpha)}}}{\partial q_j} \dfrac{\partial x_{i^{(\alpha)}}}{\partial q_k}
{% end %}

Substituting both results for the kinetic and potential energies, we may be able to write a system Lagrangian for the $n$-body system:

{% math() %}
\begin{align*}
\mathcal{L} &= K - U  \\
&=  \dfrac{1}{2} \sum_{j = 1}^N \sum_{k = 1}^N m_{jk} \dot q_j \dot q_k -  \dfrac{1}{2} \sum_{j = 1}^N \sum_{k = 1}^N A_{jk} q_j q_k \\
&=  \dfrac{1}{2} \sum_{j = 1}^N \sum_{k = 1}^N \bigg(m_{jk} \dot q_j \dot q_k-A_{jk} q_j q_k\bigg)
\end{align*}
{% end %}

Taking the partial derivatives of the Lagrangian, we have:

{% math() %}
\begin{align*}
\dfrac{\partial \mathcal{L}}{\partial q_k} &= -\dfrac{1}{2} \sum_{j = 1}^N A_{jk} q_j \\
\dfrac{\partial \mathcal{L}}{\partial \dot q_k} &=\dfrac{1}{2} \sum_{j = 1}^N m_{jk} \dot q_j \\
\dfrac{d}{dt} \left(\dfrac{\partial \mathcal{L}}{\partial \dot q_k}\right) &= \dfrac{1}{2} \sum_{j = 1}^N m_{jk} \ddot q_j
\end{align*}
{% end %}

Therefore, the Euler-Lagrange equation for the _generalized coordinates_ $q_k$ would be:

{% math() %}
\sum_{j = 1}^N (m_{jk} \ddot q_j + A_{jk} q_j) = 0
{% end %}

Or if we wanted to, we could fully write it out in matrix form:

{% math() %}
\begin{bmatrix*}
m_{11} \ddot q_1 + A_{11}q_1 & m_{21} \ddot q_2 + A_{21} q_2 & m_{31} \ddot q_3 + A_{31} q_3 &+ \dots & + m_{N1} \ddot q_N  + A_{N1} q_N \\
m_{12} \ddot q_1 + A_{12}q_1 & m_{22} \ddot q_2 + A_{22} q_2 & m_{32} \ddot q_3 + A_{32} q_3 &+ \dots & + m_{N2} \ddot q_N + A_{N2} q_N \\
m_{13} \ddot q_1 + A_{13}q_1 & m_{23} \ddot q_2 + A_{23} q_2 & m_{33} \ddot q_3 + A_{33} q_3 &+ \dots & + m_{N3} \ddot q_N + A_{N3} q_N \\
\vdots & \vdots & \vdots &\ddots &\vdots \\
m_{1N} \ddot q_1 + A_{1N}q_1 & m_{2N} \ddot q_2 + A_{2N} q_2 & m_{3N} \ddot q_3 + A_{3N} q_3 &+ \dots & + m_{NN} \ddot q_N + A_{NN} q_N \\
\end{bmatrix*}
\begin{bmatrix*}
1 \\ 1\\ 1 \\ \vdots \\ 1
\end{bmatrix*} = 0
{% end %}

And yes - that is a lot of harmonic oscillators!! At first glance, such a complicated system of ODEs may appear to be unsolvable, but there is a way we can solve it rather straightforwardly. Since we would expect sinusoidal solutions of the form $q_j(t) = a_j e^{i\omega t}$ (alternatively, with a phase shift, $q_j(t) = a_j e^{i(\omega t + \delta)}$, we find that its second derivative yields $\ddot q_j = -\omega^2 q_j$. We may now substitute this reference solution into the above equation of motion, from which we obtain:

{% math() %}
\ddot q_j = -\omega^2 q_j \Rightarrow \sum_{j = 1}^N (A_{jk} -\omega^2 m_{jk})a_j = 0
{% end %}

While it may be hard to see it, $(A_{jk} -\omega^2 m_{jk})a_j = 0$ is actually an **eigenvalue equation** whose solution(s) are the **eigenvector(s)** $a_{j^{(n)}}$ (again, remember, a single-index Cartesian tensor like $a_j$ is a vector, $n$ is just a label for which of the oscillators we're talking about). Typically speaking, there will be more than one eigenvector, so we use the index $n$ here to denote which specific eigenvector we're talking about. The nontrivial solutions (i.e. eigenvectors) of the eigenvalue equation can be found by solving its **characteristic equation**:

{% math() %}
\det(A_{jk} - \omega^2 m_{jk}) = 0
{% end %}

Where the determinant in 2D is given by:

{% math() %}
\det(A_{jk} - \omega^2 m_{jk})_{\text{(2D)}} = (A_{11}- \omega^2 m_{11})(A_{22}- \omega^2 m_{22}) - A_{12}A_{21}
{% end %}

The formula for the 3D determinant is quite long (hint: it's the same as the cross product formula) but one can find it online, for instance, in the [interactive linear algebra textbook](https://textbooks.math.gatech.edu/ila/determinants-cofactors.html). In the general case, there will be $N$ roots to the characteristic equation, where for each root $n = 1, 2, 3, \dots$, the _eigenfrequency_ $\omega_n$ would be the **eigenvalue**, and $a_{j^{(n)}}$ would be the **eigenvectors** . If we substitute this result into our reference solution, we have the _general solution_ of the system's motion, as given by:

{% math() %}
q_j(t) = \sum_n \underbrace{a_{j^{(n)}} e^{i(\omega_n t - \delta_n)}}_{q_{j^{(n)}}} = \sum_n q_{j^{(n)}}(t)
{% end %}

Where each term in the sum is known as a **normal mode**, given by:

{% math() %}
q_{j^{(n)}}(t) = a_{j^{(n)}} e^{i(\omega_nt - \delta_n)}
{% end %}

Or, if we were to write out the general solution in (perhaps more familiar) vector notation (omitting the phase shifts $\delta_n$ here for clarity):

{% math() %}
\mathbf{q}(t) = \underbrace{\mathbf{a}_1 e^{i\omega_1 t}}_\text{1st normal mode} + \underbrace{\mathbf{a}_2 e^{i\omega_2 t}}_\text{2nd normal mode} + \underbrace{\mathbf{a}_3 e^{i\omega_3 t}}_\text{3rd normal mode} + \dots + \mathbf{a}_n e^{i\omega_n t}
{% end %}

Where $\mathbf{a}_1, \mathbf{a}_2, \dots, \mathbf{a}_n$ are the eigenvectors of the system, and again, $\omega_n$ are the **eigenfrequencies** and $\mathbf{q}_n(t) = \mathbf{a}_n e^{i\omega_n t}$ are the **normal modes**. We see that the solution to the system's equation of motion in its generalized coordinates $q_j(t)$ (or in vector notation $\mathbf{q}(t)$) is simply _a sum of its normal modes_!

> **Note:** while everything we have written is mathematically sound, since the position of physical objects are always real-valued, we only take the real part of $q_j$, which yields $\operatorname{Re}(q_j) = \displaystyle \sum_n a_{j^{(n)}} \cos(\omega_n t- \delta_n)$, and the normal modes would be given by $q_{j^{(n)}}(t) = a_{j^{(n)}} \cos(\omega_n t - \delta_n)$, or alternatively, $\mathbf{q}_n(t) = \mathbf{a}_n \cos(\omega_n t - \delta_n)$.

#### Normal modes and coordinates of two coupled oscillators

Let us consider the system of two coupled harmonic oscillators and use our newfound methods to solve it in a more elegant way. Consider our system of two masses from before, each attached to a spring that is joined to a wall, and joined together by a third spring, as shown:

{{ diagram(
	src="../coupled-harmonic-oscillator.excalidraw.svg"
	desc="A diagram showing two masses that are attached to springs and are also connected to each other by a spring. Their positions are denoted x1, x2 and their masses are equal and of magnitude m."
) }}

For simplicity, let $m_1 = m_2 = M$, and let $x_1, x_2$ be the position of mass 1 and mass 2 respectively. We may then write out the kinetic and potential energies of the system, as follows:

{% math() %}
\begin{align*}
K &= \dfrac{1}{2}M \dot x_1^2 + \dfrac{1}{2} M \dot x_2^2 \\
U &= \dfrac{1}{2} \kappa x_1^2 + \dfrac{1}{2} \kappa x_2^2 + \dfrac{1}{2} \kappa_{12} (x_1 - x_2)^2
\end{align*}
{% end %}

Thus our mass matrix $m_{ij}$ is given by:

{% math() %}
m_{ij} = \begin{pmatrix} m_1 & 0 \\ 0 & m_2 \end{pmatrix} = \begin{pmatrix} M & 0 \\ 0 & M \end{pmatrix}
{% end %}

Meanwhile, our $A_{ij}$ matrix, where $A_{ij} = \dfrac{\partial^2 U}{\partial q_i \partial q_j}$, has the components:

{% math() %}
\begin{align*}
A_{11} &= \dfrac{\partial^2 U}{\partial q_1^2} = \kappa + \kappa_{12} \\
A_{12} &= \dfrac{\partial^2 U}{\partial q_1 \partial q_2} =A_{21} = -\kappa_{12} \\
A_{22} &= \dfrac{\partial^2 U}{\partial q_2^2} = \kappa + \kappa_{12}
\end{align*}
{% end %}

> **Note:** Here, $q_1 = x_1$ and $q_2 = x_2$ are our two generalized coordinates, so that's why they are the variables to which we take derivatives with respect to. Also, the reason why $A_{12} = A_{21}$ is because second partial derivatives commute, so $\dfrac{\partial^2 U}{\partial q_1 \partial q_2} = \dfrac{\partial^2 U}{\partial q_2 \partial q_1}$.

Therefore, our $A_{ij}$ matrix becomes:

{% math() %}
A_{ij} = \begin{pmatrix}
\kappa + \kappa_{12} & -\kappa_{12} \\
-\kappa_{12} & \kappa + \kappa_{12}
\end{pmatrix}
{% end %}

Solving the characteristic equation $\det(A_{ij} - \omega^2 m_{ij}) = 0$ for the eigenvalues $\omega^2$, we obtain the solutions:

{% math() %}
\omega_1 = \sqrt{\dfrac{\kappa + 2\kappa_{12}}{M}}, \quad \omega_2 = \sqrt{\dfrac{\kappa}{M}}
{% end %}

We may substitute this into $(A_{ij} - \omega^2 m_{ij})a_j = 0$ to find the eigenvectors $a_{j^{(n)}}$, which then determine the *normal modes* $q_j(t) = a_{j^{(n)}} e^{i\omega_n t}$. We will not do the full calculations here (they are quite long!) but that is the general method. We will simply state the results - the eigenvectors are:

{% math() %}
\mathbf{a}_1 = \begin{pmatrix} 1 \\ -1 \end{pmatrix}, \quad
\mathbf{a}_2 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}
{% end %}

Being eigenvectors, they will be orthogonal to each other (this comes from a result in linear algebra, but you can also check by confirming that $\mathbf{a}_1 \cdot \mathbf{a}_2 = 0$). Also, it is possible to go one step further to normalize the set of eigenvectors to form an _orthonormal set_ (where each eigenvector has magnitude 1). In that case, we have:

{% math() %}
\mathbf{a}_1 = \dfrac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ -1 \end{pmatrix}, \quad
\mathbf{a}_2 = \dfrac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ 1 \end{pmatrix}
{% end %}

Since each normal mode is defined by $q_j(t) = a_{j^{(n)}} e^{i\omega_n t}$ (or in vector notation $\mathbf{q}_n(t) = \mathbf{a}_n e^{i\omega_n t}$) the normal modes for $\mathbf{q}_1, \mathbf{q}_2$ are therefore:

{% math() %}
\begin{align*}
\mathbf{q}_1(t) &= \mathbf{a}_1 e^{i\omega_1 t} \\
\mathbf{q}_2(t) &= \mathbf{a}_2 e^{i\omega_2 t} \\
\mathbf{q}(t) &= \mathbf{q}_1(t) + \mathbf{q}_2(t) \\
&= \dfrac{1}{\sqrt{2}}
\left[\begin{pmatrix} 1 \\ -1 \end{pmatrix}e^{i\omega_1 t}+ 
\begin{pmatrix} 1 \\ 1 \end{pmatrix}e^{i\omega_2t}\right]
 \end{align*}
{% end %}

Let's see how we can now use this information to derive a set of normal coordinates, where we can describe the system oscillating in terms of just _one_ frequency. This is possible if we write out the system as a superposition of its normal coordinates $\eta_1, \eta_2, \dots, \eta_r$, that is, in the form:

{% math() %}
\mathbf{q}(t) = \sum_r \mathbf{a}_r \eta_r(t)
{% end %}

Which, assuming a two-body system described with two coordinates $(x, y)$, we can expand out in component form with:

{% math() %}
\begin{align*}
q_x &= a_{x1} \eta_1 + a_{x2}\eta_2 \\
q_y &= a_{y1} \eta_1 + a_{y2} \eta_2
\end{align*}
{% end %}

Note that we may not always be using $x, y, z$ as our coordinates, so instead we use the generalized coordinates {% inlmath() %}\mathbf{q} = \langle q_1, q_2, \dots, q_n\rangle{% end %} and {% inlmath() %}\mathbf{a}_r = \langle a_{r1}, a_{r2}, \dots, a_{rn}\rangle{% end %} instead. Then, for a two-body system, we will have the following **normal coordinates equations**:

{% math() %}
\begin{align*}
q_1 &= a_{11} \eta_1 + a_{12}\eta_2 \\
q_2 &= a_{21} \eta_1 + a_{22} \eta_2
\end{align*}
{% end %}

Now is the time we can do some pattern-matching. Remember that our system's solution that we found previously (which we temporarily write without the normalization factor $1/\sqrt{2}$ here for mathematical clarity) is given by:

{% math() %}
\mathbf{q}(t)=
\begin{pmatrix} 1 \\ -1 \end{pmatrix}e^{i\omega_1 t}+ 
\begin{pmatrix} 1 \\ 1 \end{pmatrix}e^{i\omega_2t}
{% end %}

From here, with some pattern-matching with the normal coordinates equations we just derived for a two-body system, we find that:

{% math() %}
\begin{matrix*}
a_{11} = 1, & a_{12} = 1 \\
a_{21} = -1, & a_{22} = 1
\end{matrix*}
{% end %}

So this means that $a_{21} = -a_{aa}$, $a_{12} = a_{22}$. Now if we use these identities, along with the normal coordinates equations (which we repeat below):

{% math() %}
\begin{align*}
q_1 &= a_{11} \eta_1 + a_{12}\eta_2 \\
q_2 &= a_{21} \eta_1 + a_{22} \eta_2
\end{align*}
{% end %}

We can then find that:

{% math() %}
\begin{align*}
q_1 + q_2 = 2 a_{22} \eta_2 \\\Rightarrow \eta_2 = \dfrac{1}{2a_{22}}(q_1 + q_2) \\
q_1 - q_2 = 2 a_{11} \eta_1 \\
\Rightarrow \eta_1 = \dfrac{1}{2 a_{11}} (a_q - q_2)
\end{align*}
{% end %}

This means that $\eta_1 = 0$ if $q_1 = q_2$, while $\eta_2 = 0$ if $q_1 = -q_2$. This exactly behaves as two sinusoidal oscillations separated by a varying phase $\phi$, where when $q_1 = q_2$, the two oscillations are _in-phase_ (so $\phi = 0$), and when $q_1 = -q_2$, the two oscillations are _out-of phase_ (so $\phi = \frac{\pi}{2}$)! Furthermore, it means that one coordinate is sufficient to determine the other, because these relations mean that if we know one, we will know the other. Physically speaking, it means that each mass's oscillation drives each other's oscillation, which is exactly what we would expect for _coupled_ harmonic oscillator. Therefore, we know that these are definitely **normal coordinates**, where the system oscillates at just one frequency, and only 1 coordinate is sufficient to determine the motion of both masses in the system.

Let's now take a recap:

> **Normal coordinates** are the coordinates in which the system has a well-defined (eigen-)frequency; that is, when the entire system oscillates with one frequency (and thus fixed phase).
> **Normal modes** are the specific excitations (eigenvectors) of the system that match the eigenfrequencies of the system. By finding the **normal modes**, we can isolate the system's complicated motion into independent transverse and longitudinal components, both of which are associated with a specific frequency of vibration.

### An application of coupled oscillations for molecular vibrations

An excellent usage for coupled oscillations is to describe **molecular vibrations**. Since molecules are very small, and therefore they oscillate rather close to the equilibria of their potential, making this a good theoretical model.

In 3 dimensions, a molecule with $n$ atoms will have $3n$ degrees of freedom. We have 3 degrees of freedom each for **translation** and **rotation**, as well as $3n - 6$ degrees of freedom for **vibration** (this becomes $3n-5$ if the atoms are aligned linearly, that is, one one axis). 

> **Note:** "Degrees of freedom" is just a fancy way to say "number of coordinates required to fully describe the state of a system at a given time". A good way to think of this is the **number of initial conditions for the system, if we let it evolve from some starting time $t = 0$**.

The oscillatory behavior of molecules in 3 dimensions, however, is rather complex, so we can apply the simplifying assumption that the motion of the atoms in a molecule all occur **with respect to the same plane**, that is, either at $z = 0$ or with $z \perp \hat{\mathbf{n}}$, where $\hat{\mathbf{n}}$ is the normal vector of the plane. Thus, we are left with only $2n$ degrees of freedom: 2 degrees for translation (one each for $x, y$), 1 degree of freedom for rotation, and $2n - 3$ degrees of freedom for vibration. But *if* the molecule oscillates **with respect to the same plane**, this means that there is only one axis of rotation left (the $z$ axis). Thus its **longitudinal oscillations** (oscillations in-plane, that is, either along $x$ or $y$) reduce to $n - 1$ longitudinal degrees of freedom, whereas its **transverse oscillations** (oscillations out-of plane, that is, along $\hat{\mathbf{n}}$) have $n-2$ degrees of freedom (due to symmetry). Adding those two together gives $2n-3$ **total vibrational degrees of freedom** for such molecules. 

At first, you may think that assuming that molecules can be effectively thought of little connected springs and that they can only vibrate in a plane or parallel to its normal is an *absurd* set of assumptions. However, there are real molecules that satisfy this condition, such as the carbon dioxide molecule $\ce{CO2}$, so this is _actually_ a reasonable assumption to make. Carbon dioxide has three atoms (two oxygens and a single carbon), joined by a double bond. Thus it has $2n - 3 = 3$ total vibrational degrees of freedom, where there are *two longitudinal modes* and *one transverse mode*. We show this in the diagram below:

{{ diagram(
	src="../co2-vibrational-modes.excalidraw.svg"
	desc="A diagram showing a simplified model of the carbon dioxide atom, composed of two oxygen atoms, each joined by a bond (represented as a line) to the main carbon atom."
) }}

> **Note:** Here $\kappa_1, \kappa_2$ are the spring constants of the longitudinal and transverse vibrations, respectively.

#### Longitudinal modes

Let us begin by solving for the longitudinal modes of the $\ce{CO2}$ molecule. Unfortunately, we immediately encounter a problem: since we have three atoms, we would need three coordinates $x_1, x_2, x_3$ to describe the longitudinal oscillations, but _only two longitudinal modes_. So the system is **over-determined** - there are too many variables. To solve this issue, we switch to the CoM (center-of mass) frame, which is _stationary during vibrations_. If we let $m$ be the mass of the oxygen atom, and $M$ be the mass of the carbon atom, then in the CoM frame, this means we have:

{% math() %}
m x_1 + M x_2 + m x_3 = 0
{% end %}

Thus we have:

{% math() %}
x_2 = -\dfrac{m}{M}(x_1 + x_3)
{% end %}

So we have eliminated the $x_2$ coordinate, and only have two coordinates $(x_1, x_3)$ left, thus solving the issue of over-determination! From here, we can write the kinetic energy of the system, as follows:

{% math() %}
\begin{align*}
K &= \dfrac{1}{2} m \dot x_1^2 + \dfrac{1}{2} M \dot x_2^2 + \dfrac{1}{2} m \dot x_3^2 \\
&= \dfrac{1}{2} m (\dot x_1^2 + \dot x_3^2) + \dfrac{1}{2} M\left(\dfrac{m}{M}\right)^2 (\dot x_1 + \dot x_3)^2 \\
&= \dfrac{1}{2} m (\dot x_1^2 + \dot x_3^2) + \dfrac{1}{2} M\left(\dfrac{m^2}{M}\right) (\dot x_1 + \dot x_3)^2 \\
&= \dfrac{1}{2} m (\dot x_1^2 + \dot x_3^2) + \dfrac{1}{2} \dfrac{m^2}{M}(\dot x_1^2 + \dot x_3^2 + \underbrace{2 \dot x_1 \dot x_3}_\text{cross-term}) \\
U &= \dfrac{1}{2} \kappa_1 (x_2 - x_1)^2 + \dfrac{1}{2} (x_3 - x_1)^2
\end{align*}
{% end %}

Unfortunately, we now have a _coupled system_ due to the cross term (we say that the system is _dynamically-coupled_); we would prefer to choose a system of generalized coordinates that can eliminate the dynamic coupling. This is possible if we switch to the coordinates $(q_1, q_2)$, where:

{% math() %}
\begin{align*}
q_1 &= x_3 + x_1 \\
q_2 &= x_3 - x_1
\end{align*}
{% end %}

Thus, upon substitution we have:

{% math() %}
\begin{align*}
x_1 &= \dfrac{1}{2} (q_1 - q_2) \\
x_2 &= \dfrac{1}{2} (q_1 + q_2)
\end{align*}
{% end %}

And substituting back into our kinetic energy expression, we get:

{% math() %}
K = \dfrac{1}{4} m \dot q_2^2 + \dfrac{m(2m + M)}{4m} \dot q_1^2
{% end %}

The potential energy then becomes:

{% math() %}
U = \left(\dfrac{2m + M}{2m}\right)^2 \kappa_1 q_1^2
{% end %}

Now substituting into our generalized equation of motion of coupled oscillatory systems, we have:

{% math() %}
\sum_{i = 1}^N (m_{ij} \ddot q_i + A_{ij} q_i) = 0
{% end %}

Thus we have:
 
{% math() %}
\begin{gather*}
A_{ij} = \dfrac{\partial^2 U}{\partial q_i \partial q_j}, \\
A_{11} = 2 \left(\dfrac{2m + M}{2m}\right)^2 \kappa_1,
\quad A_{12} = A_{21} = 0,
\quad A_{22} = \dfrac{1}{2} \kappa_1
\end{gather*}
{% end %}

If we solve for $\det(A_{ij} - \omega^2 m_{ij}) = 0$, we find that the eigenvalues $\omega^2$ are given by:

{% math() %}
\begin{align*}
\omega_1^2 &= \dfrac{2m + M}{mM} \kappa_1 \\
\omega_2^2 &= \dfrac{\kappa_1}{m}
\end{align*}
{% end %}

So the eigenfrequencies $\omega_1, \omega_2$ of the two normal modes are, respectively:

{% math() %}
\begin{align*}
\omega_1 &= \sqrt{\dfrac{2m + M}{mM} \kappa_1} \\
\omega_2 &= \sqrt{\dfrac{\kappa_1}{m}}
\end{align*}
{% end %}

We can then find the eigenvectors to write out the normal modes, and from there, do pattern-matching with the normal coordinates equations to find the normal coordinates. We'll not show the math here. If you try this on your own, you'll find that interestingly, the generalized coordinates $q_1, q_2$ **are the normal coordinates**.

#### Transverse normal modes

Now, we switch to analyzing purely the _transverse_ vibrations of the molecule (that is, vibrations along the vertical axis). Since these are up-and-down vibrations, we will be interested in the $z$ coordinates of the atoms, that is, $z_1, z_2, z_3$. We show this in the diagram below (here $\alpha$ is an angle):

{{ diagram(
	src="../molecule-transverse-vibration.excalidraw.svg"
	desc="A diagram showing the carbon dioxide molecule from earlier, again composed of a single carbon and two oxygen atoms, but now showing the transverse (up-down) motion of the atoms."
) }}

We previously saw before that by choosing the center-of-mass coordinates, we can fix the problem of overdetermination. We can do the same here:

{% math() %}
m z_1 + m z_3 + M z_2 = 0 
\quad \Rightarrow z_2 = -\dfrac{2m}{M} y_1
{% end %}

As the molecule vibrates, $y_3$ makes the angle $\alpha$ with the line connecting the two edge atoms, as shown in the previous diagram. Assuming small oscillations, that is, $\alpha$ is small, then we can express $\alpha$ as:

{% math() %}
\alpha = \dfrac{\Delta z}{b} = \dfrac{(z_1 - z_2) + (z_3 - z_2)}{b}
{% end %}

But using our center-of-mass coordinates, we have $z_1 = z_3$, and therefore:

{% math() %}
\begin{matrix*}
\alpha = \dfrac{2z_1}{bM}(2m + M), & z_1 = \dfrac{bm\alpha}{2(M + 2m)}
\end{matrix*}
{% end %}

From here, we can write the kinetic energy directly as:

{% math() %}
\begin{align*}
K &= \dfrac{1}{2} m(\dot z_1^2 + \dot z_3^2) + \dfrac{1}{2} M \dot z_2^2 \\
&= \dfrac{m}{M} (M + 2m) \dot z_1^2 \\
&= \dfrac{mM b^2}{4(M + 2m)} \dot \alpha^2
\end{align*}
{% end %}

The potential energy would be given by:

{% math() %}
U = \dfrac{1}{2} \kappa_2 \Delta y^2 = \dfrac{1}{2} \kappa_2 (\alpha b)^2, \quad \omega_3^2 = \dfrac{2(M + m)}{mM} \kappa_2
{% end %}

Now, we have obtained all the normal modes of the system: the transverse mode, and two longitudinal modes. From the perspective of classical electromagnetic theory, the symmetric longitudinal mode (where the two atoms on the sides are being drawn with equal strength) has no **electrical dipole moment**, but both of the other normal modes have _differing dipole moments_. In both of these two other cases, there is an asymmetry in the vibrations of the two side atoms, leading to a net **electrical dipole moment** of the molecule, which causes the production of electromagnetic radiation (i.e. light). This is, indeed, why the vibrational modes of carbon dioxide (which is well-described using our model of coupled oscillators) emit infrared light (which is electromagnetic radiation). For those interested, see this [nice online visualization](https://www.chem.purdue.edu/jmol/vibs/co2.html) of the vibrational modes of $\ce{CO2}$.

## Infinite coupled oscillators and waves

Up to this point we have examined a finite number of $N$ coupled oscillators. But what happens when we take the limit as $N \to \infty$? When this occurs, we have a _continuous_ oscillating system. Familiar examples include the vibrations of a violin string or waves on the ocean - these are all continuous oscillating systems, which we can imagine as a set of infinite coupled harmonic oscillators. Let us now examine the dynamics of such systems.

### The loaded string, part 1

We have found the equations of motion for $n$ coupled harmonic oscillator, and analyzed specific cases for $n = 2$ as well as $n = 3$. This gives us a ready-to-use model for a string, which we can think of as a system of $n$ oscillating masses that are separated by a very small distance $d$. We assume the string is fixed on both ends, and thus the total length of the string is $L = (n + 1)d$ (since we have $n+1$ separations for $n$ masses). We illustrate this physical scenario below:

{{ diagram(
	src="../loaded-spring.excalidraw.svg"
	desc="A diagram of a loaded string, which is visualized as a set of oscillating masses adjacent to each other."
) }}

Note that the masses are constrained to oscillate only vertically, which is automatically a transverse mode. If we just use Newton's second law, the interactions between $m_j$ with its two neighbors $m_{j - 1}$ and $m_{j + 1}$ lead to the forces given by:

{% math() %}
\begin{align*}
F_{j - 1} &= -\tau \sin \alpha \\
F_{j + 1} &= -\tau \sin \beta
\end{align*}
{% end %}

Where $\tau$ is the force of tension (not torque). Since each mass is very *very* close to its neighbors, each oscillates by only a small angle relative to its neighbors; the collective vibration of the string comes from the accumulated small-angle oscillations of each of the adjacent oscillating masses. Thus, with the small-angle approximation, we have $\sin \phi \approx \tan \phi$. Thus, we can say that:

{% math() %}
\begin{align*}
\tan \alpha = \dfrac{q_j - q_{j-1}}{d} \\
\tan \beta = \dfrac{q_j - q_{j + 1}}{d}
\end{align*}
{% end %}

Where the total force on mass $j$ becomes:

{% math() %}
F_j = -\dfrac{\tau}{d} (q_j - q_{j - 1}) - \dfrac{\tau}{d}(q_j - q_{j + 1})
{% end %}

Now, we may choose **generalized coordinates** $q_j$ for which $F_j = m \ddot q_j$. Then we have:

{% math() %}
\begin{gather*}
m \ddot q_j = \dfrac{\tau}{d} (q_{j - 1} - 2q_j + q_{j+1}) \\
\Rightarrow \ddot q_j = \dfrac{\tau}{md} (q_{j - 1} - 2q_j + q_{j+1})
\end{gather*}
{% end %}

Using our generalized coordinates, we have:

{% math() %}
F_j = -\dfrac{\partial U}{\partial q_j} \quad \Rightarrow  U = \dfrac{\tau}{2d} \sum_{j = 1}^{n + 1}(q_{j - 1} - q_j)^2
{% end %}

Where here, $q_0 = q_{n + 1}$ (the ends of the spring) are both zero, since the string is fixed in place. The kinetic energy is just our regular sum of the kinetic energies of each:

{% math() %}
K = \dfrac{1}{2} m \sum_{j = 1}^n \dot q_j^2
{% end %}

We can substituted our quantities into the Lagrangian:

{% math() %}
\mathcal{L} = \dfrac{1}{2} \sum_{j = 1}^{n + 1}\left[m \dot q_j - \dfrac{\tau}{d}(q_{j - 1} - q_j)^2\right]
{% end %}

Which gives, by the Euler-Lagrange equation, the ODE for $\ddot q_j$:

{% math() %}
m \ddot q_j - \dfrac{\tau}{d} \left(q_{j -1} - 2q_j + q_{j + 1}\right) = 0
{% end %}

Since we would expect oscillating behavior, let our trial solution be $q_j(t) = a_j e^{i\omega t}$. And since the string is fixed, we know that $y(0) = y(L) = 0$. Long story short, after substituting $q_j(t)$ into the ODE for $\ddot q_j$, we arrive at an eigenvalue problem, whose eigenvalues $\lambda$ are given by:

{% math() %}
\lambda =\dfrac{2\tau}{d} - m \omega^2
{% end %}

Thus, we get $\omega^2 = \dfrac{\tau z}{md}$ as the longitudinal eigenfrequency of the system.

### The loaded string, part 2

We've found the eigenfrequencies of the loaded string, but how does the string as a whole move? Or in more technical terms, what is $q_j(t)$? This is a classic problem in **Fourier analysis**. The solution, it turns out, is to start with the general form for $q_j(t)$, and decompose it in terms of its normal modes $\eta_j^{(r)}(t)$:

{% math() %}
q_j(t) = \sum_r a_j^{(r)}\eta_j^{(r)}(t)
{% end %}

We expect the normal modes to oscillate, so we let $\eta_j^{(r)}$ to take the form $\eta_j^{(r)}(t) = B_r e^{i\omega_r t}$, where $B_r$ is the mode's amplitude and $\omega_r$ is its vibrational frequency. As we've seen many times, using normal modes means that we can decompose the motion of the string into individual vibrational modes of fixed frequency $\omega_r$:

{% math() %}
\begin{align*}
q_j(t) &= \sum_r a_j^{(r)} \underbrace{\eta_j^{(r)}(t)}_{B_r e^{i\omega_r t}} \\
&= \sum_r a_j^{(r)} B_r e^{i\omega_r t} \\
\end{align*}
{% end %}

Adding all of those modes together with the right coefficients $a_j^{(r)}$ gets you the solution $q_j(t)$ that describes the motion of the string as a whole. We will not derive how to get this here (it depends on the _orthogonality_ of sinusoidal functions, if you're curious), but it turns out the correct coefficients are given by:

{% math() %}
a_j^{(r)} = \sin \left(j \dfrac{r\pi}{n + 1}\right), \quad n = 1, 2, 3, \dots
{% end %}

> **Note:** This notation may be confusing - remember that $j$ is index of the $j$-th mass in the string, and $r$ is the sum index in the sum of normal modes

As a bonus of this approach, we get the eigenfrequencies of the modes basically "for free"! If we substitute in our results, it is possible to find (no proof shown here) that:

{% math() %}
\begin{align*}
q_j(t)
&= \sum_r B_r \sin \left(j \dfrac{r\pi}{n + 1}\right) e^{i\omega_r t} \\
&\Rightarrow \omega_r = 2 \sqrt{\dfrac{\tau}{md}} \sin \left(\dfrac{r\pi}{2(n + 1)}\right)
\end{align*}
{% end %}

However, we are not done yet - we haven't yet found what $B_r$ (the amplitude of the normal modes) needs to be. Since we're working with complex exponentials, $B_r$ is in general complex-valued, that is, $B_r = u_r + i \nu_r$ (where $u_r, \nu_r$ are two constants), and expanding $B_r e^{i\omega t}$, we have:

{% math() %}
\begin{align*}
B_r e^{i\omega_r t} &= (u_r + i \nu_r)(\cos \omega_r t + i \sin \omega_r t) \\
\operatorname{Re}(B_r e^{i\omega_r t}) &= u_r \cos \omega_r t - \nu_r \sin \omega_r t
\end{align*}
{% end %}

In the last step we take only the real part for a physically-meaningful solution. Using this information, we can substitute to rewrite $q_j$ as follows:

{% math() %}
q_j(t) = \sum_r \big [u_r \cos \omega_r t - \nu_r \sin \omega_r t\big] \sin \left(j \dfrac{r\pi}{n + 1}\right)
{% end %}

Okay, but how can we find $u_r$ and $\nu_r$? The answer is that we can derive them from specified **initial conditions** - that is, the value of $q_j(t)$ at $t = 0$. This derivation will require some Fourier analysis so skip to the end if you're not familiar with it (or review Fourier series in the [PDEs guide](@/intro-pdes/chapter-2.md#fourier-series)). To start, we multiply both sides of the previous expression by $\sin\left(j \dfrac{s \pi}{n + 1}\right)$. Then summing over $j$ on both sides, we get:

{% math() %}
\begin{align*}
\sum_j \sin\left(j \dfrac{s \pi}{n + 1}\right) q_j(0) &= \sum_j \sum_r \underbrace{\sin\left(j \dfrac{r \pi}{n + 1}\right) \sin\left(j \dfrac{s \pi}{n + 1}\right)}_{(n + 1)/2 \delta_{rs}} \\
&=\dfrac{n + 1}{2} u_s
\end{align*}
{% end %}

Which comes from the orthogonality of sines, and where $\delta_{rs}$ is shorthand for:

{% math() %}
\eta_{rs} = \begin{cases}
1, & r = s \\
0, & \text{otherwise}
\end{cases}
{% end %}

This collapses all terms in the sums to a single term, so we find that:

{% math() %}
\begin{align*}
u_s = \dfrac{2}{n + 1} \sum_j q_j(0)  &\sin \left(j \dfrac{s\pi}{n + 1}\right),\\
\nu_s = -\dfrac{2}{\omega_s(n + 1)} \sum_j &\dot q_j(0)  \sin \left(j \dfrac{s\pi}{n + 1}\right)
\end{align*}
{% end %}

At this point, since we have just a single index in both expressions anyways, we might as well switch the index back to $r$, so we have the (completely equivalent) form:

{% math() %}
\begin{align*}
u_r = \dfrac{2}{n + 1} \sum_j q_j(0)  &\sin \left(j \dfrac{r\pi}{n + 1}\right),\\
\nu_r = -\dfrac{2}{\omega_r(n + 1)} \sum_j &\dot q_j(0)  \sin \left(j \dfrac{r\pi}{n + 1}\right)
\end{align*}
{% end %}

Now is the beautiful part. Up to this point, we've thought of each mass $m_j$ on the string as discrete entities, with a finite number of masses in total. But if we take the continuous limit (that is, taking the limit as $j \to \infty$) we get _infinite harmonic oscillators_, where there is a mass located at every point $x$ along the string. So $q_j(t)$ - which describes the motion of a specific mass $j$ - becomes $q(x, t)$, the motion of the _collective system_ of an infinite number of masses that forms the spring. We make further replacements of $j \to x$ as necessary to turn our discrete variables into continuous functions (and also switch discrete sums to continuous integrals), giving us a function $q(x, t)$ which describes the motion of the _entire string_:

{% math() %}
\begin{gather*}
q(x, t) = \sum_r \big [u_r \cos \omega_r t - \nu_r \sin \omega_r t\big] \sin \left( \dfrac{r\pi x}{n + 1}\right), \\
u_r = \dfrac{2}{n + 1}\int q(x, 0)  \sin \left(\dfrac{r\pi x}{n + 1}\right) dx,\\
\nu_r = -\dfrac{2}{\omega_s(n + 1)} \int \dot q(x, 0)  \sin \left(\dfrac{r\pi x}{n + 1}\right)dx
\end{gather*}
{% end %}

### Applications of continuous oscillations

We've spent the better part of a third of this series on classical mechanics discussing harmonic oscillators and coupled oscillations. But _why_ learn all of this, when most physical systems aren't (literal) strings or springs? The reason is because it introduces us a powerful idea used extensively through physics:

> We can represent arbitrarily-complex functions by decomposing them as a sum over the _harmonic modes_ $e^{-i\omega_r t}$ of a system.

This idea is tremendously powerful, and allows us to analyze many systems as if they were strings or springs, including:

- Electromagnetic waves in classical electromagnetism
- Classical fields in classical field theories (e.g. Newtonian gravity)
- Quantum fields in quantum field theories

Indeed, as the theoretical physicist Sidney Coleman put so aptly:

> "The career of a young theoretical physicist consists of treating the harmonic oscillator in ever-increasing levels of abstraction."

Learn to solve the harmonic oscillator in its many forms, and it will take you far.

## Further reading

We've now reached the end of our series on special relativity and classical mechanics. But there is much more to learn! An understanding of classical mechanics would be incomplete without also learning electromagnetic theory, for which you can see the [fundamentals of  electromagnetism](@/electromagnetism/index.md) and [in-depth electromagnetism](@/classical-electromagnetism/index.md) guides. For more resources to learn classical mechanics, the famous (and free!) [Feynman lectures on physics, vol. 1](https://www.feynmanlectures.caltech.edu/) are a wonderful learning resource, as our [Michael Fowler's lecture notes](https://galileoandeinstein.phys.virginia.edu/7010/home.html) on classical mechanics (though the latter is at a graduate level and may be more suited for advanced students).

Last but not least, classical mechanics is not the end of physics! For more on relativity, you might like my (free) online book [Special & General Relativity](https://learntheoreticalphysics.com/relativity/). And once you're ready to tackle quantum mechanics, feel free to check out the [introductory quantum mechanics](@/intro-quantum-phys.md) and [in-depth quantum mechanics](@/quantum-mechanics/index.md) guides. I'd like to end with a quote by the great physicist [Richard Feynman](https://en.wikipedia.org/wiki/Richard_Feynman), which captures the spirit of learning physics (as well as anything else!) brilliantly:

> "Nobody ever figures out what life is all about, and it doesn't matter. Explore the world. Nearly everything is really interesting if you go into it deeply enough."
> **Richard Feynman**