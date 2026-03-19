+++
title = "Fundamentals of General Relativity, Part II"
date = 2026-03-18
+++

We continue our guide to the fundamentals of General Relativity in this second section, where we cover the geodesic equation, black holes, and exact solutions to Einstein's field equations.

<!-- more -->

> ### Chapter guide for General Relativity
> 
> - [Part 1](@/general-relativity/index.md) covers the basic ideas of general relativity, spacetime, and the mathematics of curved spaces.
> - [Part 2](@/general-relativity/part-2.md) covers the geodesic equation, relativistic orbits, and black holes. **You are reading this part right now.**


## The geodesic equation

Let us return to a question that we have asked before, but didn’t answer: is it possible to find the path a particle would take in a particular space (or spacetime), solely with knowledge of the metric? It turns out the answer is **yes**, and we will derive it here.

Consider a particle that travels between two points $A, B$. The particle’s path between the points is given by the parametric equation $x^a = x^a(\tau)$, where $\tau$ is the proper time and parametrizes the path. The total arc length between the points, as we have already seen, is given by:

{% math() %}
s = \int_{A}^B ds =  \int_{A}^B \sqrt{ ds^2 } = \int_{A}^B d\tau \sqrt{ g_{ab} \frac{dx^a}{d\tau} \frac{dx^b}{d\tau} }
{% end %}

In general relativity, the Lagrangian $\mathcal{L}$ of a particle moving in a particular space(time) is closely related to the arc length; it is given by:

{% math() %}
\mathcal{L} = mc\sqrt{ g_{ab} \frac{dx^a}{d\tau} \frac{dx^b}{d\tau} } + \mathcal{L}_I
{% end %}

Where the first term corresponds to the effects of the curved spacetime, and the second term $L_I$ describes the Lagrangian associated with all other forces on the particle (electromagnetic, nuclear, etc.). The associated action $S$ (not to be confused with the arc length) is simply the integral of the Lagrangian with respect to (proper) time, giving us:

{% math() %}
S = \int_{A}^B \mathcal{L} d\tau = \int_{A}^B d\tau \left[mc\sqrt{ g_{ab} \frac{dx^a}{d\tau} \frac{dx^b}{d\tau} } + \mathcal{L}_I\right]
{% end %}

For now, we will consider the particle with no interactions from other forces, that is, $\mathcal{L}_I = 0$. The Lagrangian and action then become:

{% math() %}
\mathcal{L} = mc\sqrt{ g_{ab} \frac{dx^a}{d\tau} \frac{dx^b}{d\tau} }, \quad S = mc \int_{A}^B d\tau \sqrt{ g_{ab} \frac{dx^a}{d\tau} \frac{dx^b}{d\tau} }
{% end %}

This Lagrangian is particularly special because its action is *directly related* to the proper time $\tau$ via:

{% math() %}
S = m c^2 \int d\tau
{% end %}

Which comes from the fact that $ds = c d\tau$ and $ds = \sqrt{ds^2} = \sqrt{g_{ab} dx^a dx^b}$. Recall that the **action principle** tells us that the path taken by a particle is always one that *extremizes* the action. Therefore, up to some constants, the path taken by a particle through spacetime is also the one that *extremizes* (maximizes or minimizes) the proper time $\tau$. Meanwhile, the action $S$ is related to the path length $s$ via:

{% math() %}
S = (mc)s
{% end %}

This tells us that the path travelled by the particle is also one that *extremizes* the path length. Usually in the context of differential geometry and general relativity, the extrenum is a minimum, so it is often said that the path a particle travels in space(time) is the *shortest path* between two points. We have a special name for these paths: they are called **geodesics**. In flat space, we know that the shortest paths between two points is a straight line connecting the two points, so the geodesics associated with a flat space of any dimension are linear curves (that is, the equivalent of a straight line). But in curve space(time), this is not so simple; the shortest possible path may not be straight!

> **Note:** When studying geodesics from a purely mathematical point of view, the factor of $mc^2$ (needed for the units to be correct in physics) is typically dropped. The action is then simply a functional that must be extremized, and is given by the integral of $\sqrt{ds^2} = \sqrt{ g_{ab} \frac{dx^a}{d\lambda} \frac{dx^b}{d\lambda} }$ with respect to an arbitrary parameter $\lambda$.

Now, we know how to get the equations of motion from an arbitrary Lagrangian: just plug it into the Euler-Lagrange equations. Unfortunately, it turns out that our Lagrangian $\mathcal{L} = mc\sqrt{ g_{ab} \frac{dx^a}{d\tau} \frac{dx^b}{d\tau}}$ is quite cumbersome to differentiate. Fortunately, it is possible to choose an alternative form of the Lagrangian that is the square of our original Lagrangian (up to some constants). This Lagrangian is given by:

{% math() %}
\mathcal{L} = g_{ab} \frac{dx^a}{d\tau} \frac{dx^b}{d\tau}
{% end %}

It is natural to ask why we are allowed to do this. The simple answer is that this Lagrangian gives you the same equations of motion as our original Lagrangian. The more complicated answer can be found by reading [this Physics StackExchange post](https://physics.stackexchange.com/a/149087), but we will not go through it here. Another curious fact is that the Lagrangian $\mathcal{L} = -c^2$, which we will not derive right now, but will be very useful later.

### Deriving the equations of motion

We are now ready to find the partial derivatives of our Lagrangian and substitute them into the Euler-Lagrange equation, which (in relativistic form) reads as follows:

{% math() %}
\frac{d}{d\tau}\left( \frac{\partial \mathcal{L}}{\partial \dot{x}^k} \right) = \frac{\partial \mathcal{L}}{\partial x^k}, \quad \dot{x}^k \equiv \frac{dx^k}{d\tau}
{% end %}

Note that from this point forwards, all time derivatives in dot notation (e.g. $\dot x^a, \dot x^b$) will be understood to be derivatives with respect to proper time $\tau$ (unless otherwise stated). First, let us taken the partial derivative of $\mathcal{L}$ with respect to $\dot{x}^k$. This requires us to first write the Lagrangian in terms of $x^k$, which we can do with the Kronecker delta via its index relabelling identities. This gives us:

{% math() %}
\dot{x}^a = \delta^a{}_{k} \dot{x}^k, \quad \dot{x}^b = \delta^b{}_{k} \dot{x}^k
{% end %}

Substituting into the Lagrangian gives us:

{% math() %}
\mathcal{L} = g_{ab} \frac{dx^a}{d\tau} \frac{dx^b}{d\tau} = g_{ab} \delta^a{}_{k} \delta^b{}_{k} \dot{x}^k \dot{x}^k = g_{ab} \delta^a{}_{k} \delta^b{}_{k} (\dot{x}^k)^2
{% end %}

The metric $g_{ab}$ is a function of position $x^k$ and proper time $\tau$, but not of the velocity $\dot{x}^k$. Therefore, the partial derivative of the Lagrangian with respect to $\dot x^k$ is then:

{% math() %}
\frac{\partial \mathcal{L}}{\partial \dot{x}^k} = 2g_{ab} \delta^a{}_{k} \delta^b{}_{k} \dot{x}^k = 2 g_{kb} \dot{x}^b
{% end %}

> **Note:** Here we again used the relabelling via the Kronecker delta, which gives us $g_{ab} \delta^a{}_{k} = g_{kb}$ and $\delta^b{}_k \dot x^k = \dot x^b$.

Now let us differentiate the Lagrangian with respect to $\dot x^k$. Again, remember that the metric is a function of the position $x^k$, that is $g_{ab} = g_{ab}(x^k)$. Therefore, we have:

{% math() %}
\begin{align*}
\frac{\partial \mathcal{L}}{\partial x^k} = \frac{\partial}{\partial x^k}\left[g_{ab} \frac{dx^a}{d\tau} \frac{dx^b}{d\tau}\right] = \frac{\partial g_{ab}}{\partial x^k} \dot{x}^a \dot{x}^b
\end{align*}
{% end %}

Substituting the partial derivatives into the Euler-Lagrange equation and simplifying, we have:

{% math() %}
\begin{align*}
\frac{d}{d\tau} (2 g_{kb} \dot{x}^b) &= \frac{\partial g_{ab}}{\partial x^k} \dot{x}^a \dot{x}^b \\
\frac{d}{d\tau} (g_{kb} \dot{x}^b) &= \frac{1}{2} \frac{\partial g_{ab}}{\partial x^k} \dot{x}^a \dot{x}^b
\end{align*}
{% end %}

Note that we can write this in an alternate form as:

{% math() %}
\frac{d}{d\tau}(g_{kb}\dot{x}^b) - \frac{1}{2} \frac{\partial g_{ab}}{\partial x^k} \dot{x}^a \dot{x}^b = 0
{% end %}

This is the **geodesic equation**, or at least one way to write it. However, to cast it into its canonical (standard) form, we expand the derivative on the left with the product rule, giving us:

{% math() %}
\ddot{x}^b g_{kb} + \frac{d g_{kb}}{d\tau} \dot{x}^b - \frac{1}{2} \frac{\partial g_{ab}}{\partial x^k} \dot{x}^a \dot{x}^b = 0
{% end %}

Now, to find the total derivative of $g_{kb}$ with respect to $\tau$, we need to use the chain rule, giving us:

{% math() %}
\frac{dg_{kb}}{d\tau} = \frac{\partial g_{kb}}{\partial x^a} \frac{dx^a}{d\tau} = \frac{\partial g_{kb}}{\partial x^a} \dot{x}^a
{% end %}

Note that in expanding the partial derivative, the Einstein summation convention tells us that we implicitly sum over $a$. Therefore, $a$ is a dummy index and we can freely change it to whatever we want. For instance, we can make the replacement $a \to j$ or $a \to \sigma$, whatever we want, as long as it is not one of the free indices (which are $k$ and $b$). Plugging this into the geodesic equation gives us:

{% math() %}
\begin{align*}
\ddot{x}^b g_{kb} + \frac{\partial g_{kb}}{\partial x^a} \dot{x}^a \dot{x}^b - \frac{1}{2} \frac{\partial g_{ab}}{\partial x^k} \dot{x}^a \dot{x}^b = 0 \\
\ddot{x}^b g_{kb} + \left[ \frac{\partial g_{kb}}{\partial x^a}  - \frac{1}{2} \frac{\partial g_{ab}}{\partial x^k} \right]\dot{x}^a \dot{x}^b = 0
\end{align*}
{% end %}

This form is technically correct, but to get to the canonical form there is one trick we need to apply. Note that since we can write $X = \frac{1}{2}(X + X)$ where $X$ is an arbitrary quantity, we can do the same for the second term in the expression, giving us:

{% math() %}
\frac{\partial g_{kb}}{\partial x^a} = \frac{1}{2}\left(\frac{\partial g_{kb}}{\partial x^a} + \frac{\partial g_{kb}}{\partial x^a}\right)
{% end %}

Therefore:

{% math() %}
\begin{align*}
\frac{\partial g_{kb}}{\partial x^a}\dot{x}^a \dot{x}^b &= \frac{1}{2}\left(\frac{\partial g_{kb}}{\partial x^a} + \frac{\partial g_{kb}}{\partial x^a}\right) \dot{x}^a \dot{x}^b \\
&= \frac{1}{2}\left( \frac{\partial g_{kb}}{\partial x^a} \dot{x}^a \dot{x}^b + \frac{\partial g_{kb}}{\partial x^a} \dot{x}^a \dot{x}^b \right)
\end{align*}
{% end %}

Since each term has $a, b$ as dummy indices, we can freely exchange them. For the first term, let us perform the transformation $a \to b$ and $b \to a$, giving us:

{% math() %}
\frac{\partial g_{kb}}{\partial x^a} \dot{x}^a \dot{x}^b \rightarrow \frac{\partial g_{ka}}{\partial x^b} \dot{x}^b \dot{x}^a
{% end %}

For the second term, meanwhile, we will leave it alone. This gives us:

{% math() %}
\frac{\partial g_{kb}}{\partial x^a} \dot x^b \dot x^a = \frac{1}{2}\left( \frac{\partial g_{ka}}{\partial x^b} \dot{x}^b \dot{x}^a + \frac{\partial g_{kb}}{\partial x^a} \dot{x}^a \dot{x}^b \right) \dot x^b \dot x^a
{% end %}

 And therefore if we divide by $\dot x^b \dot x^a$ (equivalent to $\dot x^a \dot x^b$), we have:

{% math() %}
\frac{\partial g_{kb}}{\partial x^a} = \frac{1}{2}\left( \frac{\partial g_{ka}}{\partial x^b}  + \frac{\partial g_{kb}}{\partial x^a}  \right)
{% end %}

Which, after substituting back into the geodesic equation we obtained previously, gives us:

{% math() %}
\ddot{x}^b g_{kb} + \frac{1}{2}\left(\frac{\partial g_{ka}}{\partial x^b}  + \frac{\partial g_{kb}}{\partial x^a}   -  \frac{\partial g_{ab}}{\partial x^k} \right)\dot{x}^a \dot{x}^b = 0
{% end %}

In the first term ($\ddot x^b g_{kb}$) we have $b$ as a dummy index, so we can swap it to something else; this is not strictly needed, but is conventional. Here, we will make the replacement $b \to c$ and swap the indices of the metric ($g_{kc} = g_{ck}$), giving us:

{% math() %}
\ddot{x}^c g_{ck} + \frac{1}{2}\left(\frac{\partial g_{ka}}{\partial x^b}  + \frac{\partial g_{kb}}{\partial x^a}   -  \frac{\partial g_{ab}}{\partial x^k} \right)\dot{x}^a \dot{x}^b = 0
{% end %}

Note that the geodesic equation is frequently written using Greek letters since we are working with spacetime. Thus, we perform the substitutions of $a \to \alpha$, $b \to \beta$, $c \to \gamma$, $k \to \kappa$, giving us:

{% math() %}
\ddot{x}^\gamma g_{\gamma \kappa} + \frac{1}{2}\left(\frac{\partial g_{\kappa \alpha}}{\partial x^\beta}  + \frac{\partial g_{\kappa \beta}}{\partial x^\alpha}   -  \frac{\partial g_{\alpha \beta}}{\partial x^\kappa} \right)\dot{x}^\alpha \dot{x}^\beta = 0
{% end %}

Now, contract with the inverse metric by multiplying all sides with $g^{\gamma \kappa}$, giving us:

{% math() %}
\ddot{x}^\gamma = -\frac{1}{2}g^{\gamma \kappa}\left(\frac{\partial g_{\kappa \alpha}}{\partial x^\beta}  + \frac{\partial g_{\kappa \beta}}{\partial x^\alpha}   -  \frac{\partial g_{\alpha \beta}}{\partial x^\kappa} \right)\dot{x}^\alpha \dot{x}^\beta
{% end %}

Finally, if we define the **Christoffel symbols** $\Gamma^\gamma_{\alpha \beta}$ as:

{% math() %}
\Gamma^\gamma_{\alpha \beta} = \frac{1}{2}g^{\gamma \kappa}\left(\frac{\partial g_{\kappa \alpha}}{\partial x^\beta}  + \frac{\partial g_{\kappa \beta}}{\partial x^\alpha}   -  \frac{\partial g_{\alpha \beta}}{\partial x^\kappa} \right)
{% end %}

> **Note:** Formally they are called _Christoffel symbols of the second kind_, which is to be distinguished by the separate but related Christoffel symbols of the first kind. However, we will generally work with only Christoffel symbols of the second kind.

This gives us the **geodesic equation in canonical form**:

{% math() %}
\ddot{x}^\gamma = -\Gamma^\gamma_{\alpha \beta} \dot{x}^\alpha \dot{x}^\beta
{% end %}

Note that we can more explicitly indicate that the derivatives are with respect to (proper) time by writing it as:

{% math() %}
\frac{d^2 x^\gamma}{d\tau^2} = -\Gamma^\gamma_{\alpha \beta} \frac{dx^\alpha}{d\tau} \frac{dx^\beta}{d\tau}
{% end %}

### Symmetries of the Christoffel symbols

The Christoffel symbols have certain symmetries that make them easier to compute. Importantly, they are symmetric about the lower indices, meaning that:

{% math() %}
\Gamma^\gamma_{\alpha \beta} = \Gamma^\gamma_{\beta \alpha}
{% end %}

For this reason, the number of independent Christoffel symbols is far fewer than the *total* number of Christoffel symbols, since the off-diagonal Christoffel symbols are equal to each other. In $N$ dimensions, there are a maximum of $N^2(N+1)/2$ independent Christoffel symbols. For instance, 2D space has 6 independent components, 3D space has 18, and 4D space(time) has 40. This is a result of the symmetries of the Christoffel symbols.

### Calculation of the Christoffel symbols of the 2-sphere

Let us first attempt to compute the Christoffel symbols of the 2-sphere. This is an especially interesting case because the 2-sphere’s Christoffel symbols have a physical importance *even outside of general relativity*. This is because the Earth can be (approximately) modelled as a 2-sphere, which, as we know, is curved! Therefore, precise physics calculations that need to account for the curvature of the Earth - for instance, for long-distance ballistics or rocketry - will implicitly require information about the Christoffel symbols of a 2-sphere. They are also used to determine the most ideal paths for aircraft flights. So these calculations are not just abstract mathematics!

To begin, recall that the metric of a 2-sphere is given by:

{% math() %}
g_{ij} = \begin{pmatrix}
R^2 & 0 \\
0 & R^2 \sin^2 \theta
\end{pmatrix}, \quad
g^{ij} = \begin{pmatrix}
\frac{1}{R^2} & 0 \\
0 & \frac{1}{R^2 \sin^2 \theta}
\end{pmatrix}
{% end %}

Thus, the only two nonzero components of the metric are $g_{11} = g_{\theta \theta} = R^2$ and $g_{22} = g_{\phi \phi} = R^2 \sin^2 \theta$. In addition, the metric is diagonal, so we have:

{% math() %}
\begin{align*}
\Gamma^\gamma_{\alpha \beta} &= \frac{1}{2}g^{\gamma \kappa}\left(\frac{\partial g_{\kappa \alpha}}{\partial x^\beta}  + \frac{\partial g_{\kappa \beta}}{\partial x^\alpha}   -  \frac{\partial g_{\alpha \beta}}{\partial x^\kappa} \right) \\
&= \frac{1}{2}g^{\gamma \gamma}\left(\frac{\partial g_{\gamma \alpha}}{\partial x^\beta}  + \frac{\partial g_{\gamma \beta}}{\partial x^\alpha}   -  \frac{\partial g_{\alpha \beta}}{\partial x^\gamma} \right)
\end{align*}
{% end %}

Where we simply made the replacement $\kappa \to \gamma$ due to the diagonal nature of the metric. Now, since there are only two possibilities for $\gamma$ (either $\gamma = 1$ or $\gamma = 2$, since the metric has only two nonzero components) we have:

{% math() %}
\begin{align*}
\Gamma^1_{\alpha \beta} = \frac{1}{2}g^{1 1}\left(\frac{\partial g_{1 \alpha}}{\partial x^\beta}  + \frac{\partial g_{1 \beta}}{\partial x^\alpha}   -  \frac{\partial g_{\alpha \beta}}{\partial x^1} \right) \\
\Gamma^2_{\alpha \beta} = \frac{1}{2}g^{2 2}\left(\frac{\partial g_{2 \alpha}}{\partial x^\beta}  + \frac{\partial g_{2 \beta}}{\partial x^\alpha}   -  \frac{\partial g_{\alpha \beta}}{\partial x^2} \right)
\end{align*}
{% end %}

For the former case, since $\alpha, \beta$ range from 1 to 2, then we need only compute $\Gamma^1_{11}$, $\Gamma^1_{12}$, and $\Gamma^1_{22}$ (because $\Gamma^1_{21} = \Gamma^1_{12}$ from the symmetries of the Christoffel symbols, so we don’t have to calculate $\Gamma^1_{21}$). Substituting, we have:

{% math() %}
\begin{align*}
\Gamma^1_{1 1} = \frac{1}{2}g^{1 1}\left(\frac{\partial g_{1 1}}{\partial x^1}  + \frac{\partial g_{1 1}}{\partial x^1}   -  \frac{\partial g_{1 1}}{\partial x^1} \right) \\
\Gamma^1_{1 2} = \frac{1}{2}g^{1 1}\left(\frac{\partial g_{1 1}}{\partial x^2}  + \frac{\partial g_{1 2}}{\partial x^1}   -  \frac{\partial g_{1 2}}{\partial x^1} \right) \\
\Gamma^1_{2 2} = \frac{1}{2}g^{1 1}\left(\frac{\partial g_{1 2}}{\partial x^2}  + \frac{\partial g_{1 2}}{\partial x^2}   -  \frac{\partial g_{2 2}}{\partial x^1} \right)
\end{align*}
{% end %}

Since $g_{11} = R^2$ is a constant, its partial derivatives with respect to all coordinates is by definition zero. Therefore, all terms that contain a partial derivative of $g_{11}$ are automatically zero, giving us:

{% math() %}
\begin{align*}
\Gamma^1_{1 1} &= \frac{1}{2}g^{1 1}\left(\cancel{ \frac{\partial g_{1 1}}{\partial x^1} }  + \cancel{ \frac{\partial g_{1 1}}{\partial x^1}  }  -  \cancel{ \frac{\partial g_{1 1}}{\partial x^1} } \right) \\
&= 0 \\
\Gamma^1_{1 2} &= \frac{1}{2}g^{1 1}\left(\cancel{ \frac{\partial g_{1 1}}{\partial x^2} }  + \frac{\partial g_{1 2}}{\partial x^1}   -  \frac{\partial g_{1 2}}{\partial x^1} \right) \\
&= \frac{1}{2}g^{1 1}\left( \frac{\partial g_{1 2}}{\partial x^1}   -  \frac{\partial g_{1 2}}{\partial x^1} \right) \\
\Gamma^1_{2 2} &= \frac{1}{2}g^{1 1}\left(\frac{\partial g_{1 2}}{\partial x^2}  + \frac{\partial g_{1 2}}{\partial x^2}   -  \frac{\partial g_{2 2}}{\partial x^1} \right)
\end{align*}
{% end %}

Meanwhile, since the matrix is diagonal, all of its off-diagonal components are zero, meaning that $g_{12} = g_{21} = 0$. Therefore, all terms that contain a partial derivatives of either of these metric components is by definition zero.

{% math() %}
\begin{align*}
\Gamma^1_{1 2} &= \frac{1}{2}g^{1 1}\left( \cancel{ \frac{\partial g_{1 2}}{\partial x^1} }   -  \cancel{ \frac{\partial g_{1 2}}{\partial x^1}  }\right) \\
&= 0 \\
\Gamma^1_{2 2} &= \frac{1}{2}g^{1 1}\left(\cancel{ \frac{\partial g_{1 2}}{\partial x^2} }  + \cancel{ \frac{\partial g_{1 2}}{\partial x^2} } -  \frac{\partial g_{2 2}}{\partial x^1} \right) \\
&= -\frac{1}{2} g^{11}  \frac{\partial g_{2 2}}{\partial x^1}
\end{align*}
{% end %}

Thus the only Christoffel symbol in $\Gamma^1_{\alpha \beta}$ that survives is $\Gamma^1_{22}$. Let us now do the same for $\Gamma^2_{\alpha \beta}$ (the other set of Christoffel symbols). We have:

{% math() %}
\begin{align*}
\Gamma^2_{1 1} = \frac{1}{2}g^{2 2}\left(\frac{\partial g_{2 1}}{\partial x^1}  + \frac{\partial g_{2 1}}{\partial x^1}   -  \frac{\partial g_{1 1}}{\partial x^2} \right) \\
\Gamma^2_{1 2} = \frac{1}{2}g^{2 2}\left(\frac{\partial g_{2 1}}{\partial x^2}  + \frac{\partial g_{2 2}}{\partial x^1}   -  \frac{\partial g_{1 2}}{\partial x^2} \right) \\
\Gamma^2_{2 2} = \frac{1}{2}g^{2 2}\left(\frac{\partial g_{2 2}}{\partial x^2}  + \frac{\partial g_{2 2}}{\partial x^2}   -  \frac{\partial g_{2 2}}{\partial x^2} \right)
\end{align*}
{% end %}

We can use the same tricks as before to quickly cross out the terms that are zero: specifically, any terms that involve partial derivatives of $g_{11}$, $g_{12}$, or $g_{21}$. This gives us:

{% math() %}
\begin{align*}
\Gamma^2_{1 1} &= 0 \\
\Gamma^2_{1 2} &= \frac{1}{2}g^{2 2} \frac{\partial g_{2 2}}{\partial x^1} \\
\Gamma^2_{2 2} &= \frac{1}{2}g^{2 2}\left(\frac{\partial g_{2 2}}{\partial x^2}  + \cancel{ \frac{\partial g_{2 2}}{\partial x^2} } -  \cancel{ \frac{\partial g_{2 2}}{\partial x^2} } \right) \\
&= \frac{1}{2} g^{22} \frac{\partial g_{22}}{\partial x^2}
\end{align*}
{% end %}

Now, note that $g_{22} = R^2 \sin^2 \theta$, which is only dependent on $\theta$ (the $x^1$ coordinate). Therefore, any partial derivatives of $g_{22}$ with respect to $\phi$ (the $x^2$ coordinate) are zero, giving us:

{% math() %}
\begin{align*}
\Gamma^2_{1 1} &= 0 \\
\Gamma^2_{1 2} &= \frac{1}{2}g^{2 2} \frac{\partial g_{2 2}}{\partial x^1} \\
\Gamma^2_{2 2} &= 0
\end{align*}
{% end %}

All in all, we are left with only two nonzero Christoffels, which are respectively:

{% math() %}
\Gamma^1_{22} = -\frac{1}{2} g^{11}  \frac{\partial g_{2 2}}{\partial x^1}, \quad \Gamma^2_{1 2} = \frac{1}{2}g^{2 2} \frac{\partial g_{2 2}}{\partial x^1}
{% end %}

Writing them out in explicit form, $\Gamma^1_{22} = \Gamma^\theta_{\phi \phi}$ and $\Gamma^2_{12} = \Gamma^\phi_{\theta \phi}$, and they take the form:

{% math() %}
\begin{align*}
\Gamma^\theta_{\phi \phi} &= -\frac{1}{2} g^{\theta \theta} \frac{\partial g_{\phi \phi}}{\partial \theta} \\
&= -\frac{1}{2}\left( \frac{1}{R^2} \right) 2R^2 \sin \theta \cos \theta \\
&= -\sin \theta \cos \theta \\
\Gamma^\phi_{\theta \phi} &= \frac{1}{2}g^{\phi \phi} \frac{\partial g_{\phi \phi}}{\partial \theta} \\
&=\frac{1}{2} \frac{1}{R^2 \sin^2 \theta} (2R^2 \sin \theta \cos \theta) \\
&= \frac{R^2\cos \theta}{R^2 \sin \theta} \\
& = \cot \theta
\end{align*}
{% end %}

The Christoffel symbols can also be written in matrix form as:

{% math() %}
\begin{align*}
\Gamma^\theta_{ij} &= \begin{pmatrix}
0 & 0 \\
0 & -\sin \theta \cos \theta
\end{pmatrix} \\
\Gamma^\phi_{ij} &= \begin{pmatrix}
0 & \cot \theta \\
\cot \theta & 0
\end{pmatrix}
\end{align*}
{% end %}

### Geodesics on a 2-sphere

We now aim to find the geodesics on a sphere, using the geodesic equation $\ddot{x}^\gamma = -\Gamma^\gamma_{\alpha \beta} \dot{x}^\alpha \dot{x}^\beta$ which we previously derived. First, note that $\gamma$ ranges from 1 to 2; meanwhile, since there are only two Christoffel symbols (technically 3, but only 2 are independent), we have:

{% math() %}
\begin{align*}
\ddot{x}^1 &= -\Gamma^1_{\alpha \beta} \dot{x}^\alpha \dot{x}^\beta \\
&= -\Gamma^1_{22} \dot{x}^2 \dot{x}^2 \\
&= -(-\sin \theta \cos \theta) \dot{\phi}^2 \\
&= (\sin \theta \cos \theta) \dot{\phi}^2 \\
\ddot{x}^2 &= -\Gamma^2_{\alpha \beta} \dot{x}^\alpha \dot{x}^\beta \\
&= -(\underbrace{ \Gamma^2_{12} \dot{x}^1 \dot{x}^2 + \Gamma^2_{21} \dot{x}^2 \dot{x}^1 }_\text{these are equal}) \\
&= -2\Gamma^2_{12} \dot{x}^1 \dot{x}^2 \\
&= -(2 \cot \theta) \dot{\phi} \dot{\theta} 
\end{align*}
{% end %}

Expanding them out and writing them in coordinate form gives us:

{% math() %}
\begin{align*}
\frac{d^2 \theta}{d\tau^2} &= \sin \theta \cos \theta \left( \frac{d\phi}{d\tau} \right)^2 \\
\frac{d^2 \phi}{d\tau^2} &= - 2 \cot \theta \frac{d\theta}{d\tau} \frac{d\phi}{d\tau}
\end{align*}
{% end %}

These are highly-nonlinear differential equations that would be very difficult to solve directly. But here is where we can take advantage of the azimuthal symmetry and polar symmetry of a sphere. This means that we are free to reorient our coordinate system such our geodesics always lie on a plane of constant $\theta$. Let us choose $\theta = \pi/2$ for convenience. If we substitute this into the first geodesic equation, it automatically satisfied, since:

{% math() %}
\frac{d^2 \theta}{d\tau^2} = \frac{d^2 (\pi / 2)}{d\tau^2} = 0, \quad \sin \left( \frac{\pi}{2} \right) \cancel{ \cos \left( \frac{\pi}{2} \right) }^0 \dot{\phi}^2 = 0
{% end %}

Therefore the differential equation is satisfied. Let us now look at the second differential equation. Since $\cot(\pi/2) = 0$, the second differential equation reduces to:

{% math() %}
\frac{d^2 \phi}{d\tau^2} = 0
{% end %}

Upon twice-integration we find the solution is simply given by:

{% math() %}
\phi(\tau) = A \tau + B
{% end %}

Where $A, B$ are some constants. If we use the initial conditions $\phi(0) = \phi_0$ and $\dot \phi(0) = \omega$, we have:

{% math() %}
\phi(\tau) = \omega \tau +  \phi_{0}
{% end %}

While this is a linear solution, it is *not* a straight line! This is because if we convert the solution into Cartesian coordinates, we have:

{% math() %}
\phi(\tau) = \cos^{-1}\left( \frac{x}{\sqrt{ x^2 + y^2 }} \right) = \omega \tau + \phi_{0}
{% end %}

Which is clearly a highly-nonlinear (implicit) equation! This is why geodesics on a sphere do not correspond to straight lines in flat space. In fact, if you actually *tried* to follow a path on a sphere that corresponded to a straight line in flat space, it would take you longer to cover the same distance! Hence, we see that geodesics are the paths of shortest (proper) time in a curved space, but they are only straight lines in *flat space*.

### Extra: Calculating the Christoffel symbols with a computer

While our example calculation of the Christoffel symbols was fairly straightforward, in practice it can be be quite a tedious task to do manually. However, it is not a difficult task at all to perform using a computer algebra system (CAS) for those with some programming experience. A very powerful and free CAS is SymPy, which can be programmed using Python. Here, SymPy v1.14.0 is used, but any generally modern version should work.

> **Note:** This section presumes that you are using SymPy in a Jupyter notebook or similar interactive Python environment, which can display SymPy expressions interactively as LaTeX. The quality of the outputs will be degraded if you try to run this code using "plain" Python. Also, it requires a modern version of Python (for instance, it runs on Python 3.13.7).

Finding the Christoffel symbols from the general formula requires us to calculate the inverse metric and to be able to take (partial) derivatives of the metric. SymPy can do all of this automatically for us.

```python
# imports
from sympy import symbols, Symbol, Matrix, simplify, Rational, Eq, diff, Array, Function
from sympy import latex as sympy_to_latex
from sympy import sin, cos, tan, exp
from sympy import csc, sec, cot, asin, acos, atan
from sympy import sinh, cosh, tanh
from sympy import asinh, acosh, atanh
from sympy import log as ln
from sympy.abc import c, G # speed of light and gravity constant
one_half = Rational(1, 2)
from IPython.display import display, Math # for Jupyter notebook/lab only
```

We first define some utility functions:

```python
# calculate christoffel symbols
def metric_to_inverse(g):
    # since only a SymPy `Matrix` has the inv()
    # method we have to do this method
    return Array(Matrix(metric).inv())

def generate_empty_3D_array(dimensions):
    return [[[0 for _ in range(dimensions)] for _ in range(dimensions)] for _ in range(dimensions)]
```

Then, we can transform the tensor formulas into Python code. This is where tensor notation actually helps greatly, because the formulas match naturally onto Python’s indexing syntax; for instance, $T_{ij}$ becomes simply `T[i][j]` in Python code. The first formula we’ll translate is that of the line element $ds^2 = g_{ab} dx^a dx^b$. This can conveniently be written as a dot product between an infinitesimal displacement vector $d\vec x = dx^b$ and its covariant version $dx_{b}$, where $dx_b = g_{ab}dx^a$ is simply the matrix product of the metric with $d\vec x$. Thus, we have:

```python
# calculate the line element ds^2 from the provided metric
def line_element_from_metric(metric, display=True):
    # infinitesimal displacement vector
    dX = Matrix([Symbol("d" + x_i.name) for x_i in coords])
    # here, the "@" operator is shorthand for the matrix product
    line_element = [dX.T @ (Matrix(metric) @ dX)][0]
    if display:
        displayed_line_element = Eq(Symbol("ds")**2, line_element[0])
        return displayed_line_element
    else:
        return line_element
```

To calculate a specific Christoffel symbol $\Gamma^\gamma_{\alpha \beta}$ we need to use the general formula, which is given by:

{% math() %}
\Gamma^\gamma_{\alpha \beta} = \frac{1}{2}g^{\gamma \kappa}\left(\frac{\partial g_{\kappa \alpha}}{\partial x^\beta}  + \frac{\partial g_{\kappa \beta}}{\partial x^\alpha}   -  \frac{\partial g_{\alpha \beta}}{\partial x^\kappa} \right)
{% end %}

We can translate the partial derivatives into python code in an index-like way, where $\frac{\partial g_{ij}}{\partial x^k}$ becomes `diff(metric[i][j], k)` and $i, j, k$ are integers. This gives us the following code:

```python
# calculate a specific christoffel symbol $\Gamma^\gamma_{\alpha \beta}$
# indices is list-like or tuple in the form (gamma, alpha, beta)
# where gamma, alpha, beta are all coordinates
def calculate_symbol(indices, coords, metric, 
                     metric_inv):
    if len(indices) != 3:
        raise Exception(f"Christoffel symbols have 3 indices, but you supplied {len(indices)}!")
        return
    christoffel = 0
    gamma, alpha, beta = indices
    # check that the provided indices are physical coordinates
    for idx in indices:
        if idx not in coords:
            raise Exception(f"Error: provided coordinate {idx} is not in one of your coordinates {coords}")
            return
    # translate symbols into indices, i.e. x^1 -> 1, x^2 -> 2, x^3 -> 3, etc.
    g, a, b = [coords.index(x) for x in indices]
    X = coords
    dimensions = len(coords)
    # note: summation over k (short for kappa)
    for k in range(dimensions):
        d1 = diff(metric[k][a], X[b])
        d2 = diff(metric[k][b], X[a])
        d3 = diff(metric[a][b], X[k])
        christoffel += one_half * metric_inv[g][k] * (d1 + d2 - d3)
    # returns tuple with Christoffel symbol on first
    # and its evaluated value on the second
    backslash = "\\"
    leftbrace = r"{"
    rightbrace = r"}"
    christoffel_pretty = f"\\Gamma^" + gamma.name \
                + "_" + leftbrace + alpha.name + " " \
                + beta.name + rightbrace
    return Symbol(christoffel_pretty), christoffel
```

We can also calculate *all* of the Christoffel symbols at once, which is more involved since we need to loop over all the possible Christoffel symbols. A code implementation could look something like this, where we refer back to the `calculate_symbol()` function we defined for calculating individual Christoffel symbols:

```python
def calculate_all_christoffels(coords, metric, inverse_metric):
    dimensions = len(coords)
    # this array holds the actual christoffel symbols
    christoffels_array = generate_empty_3D_array(dimensions)
    # this array holds the LaTeX symbols for the Christoffel symbols
    christoffels_symbolic_array = generate_empty_3D_array(dimensions)
    for g in range(dimensions):
        for a in range(dimensions):
            for b in range(dimensions):
                gamma = coords[g]
                alpha = coords[a]
                beta = coords[b]
                indices = (gamma, alpha, beta)
                # take advantage of symmetry where possible
                if b == a and christoffels_array[g][b][a] != 0:
                    christoffels_array[g][a][b] = christoffels_array[g][b][a]
                    christoffels_symbolic_array[g][a][b] = christoffels_symbolic_array[g][b][a]
                else:
                    christoffel_gab = calculate_symbol(indices, coords, metric, inverse_metric)
                    # christoffel_gab contains both the LaTeX representation 
                    # and the symbolic expression for the computed christoffel
                    # symbol, which we store in 2 separate arrays
                    christoffels_symbolic_array[g][a][b] = christoffel_gab[0]
                    christoffels_array[g][a][b] = christoffel_gab[1]
    # make both display as a SymPy array
    return Array(christoffels_array), Array(christoffels_symbolic_array)
```

It would be nice to see only the nonzero Christoffel symbols too; after all, we generally only care about the nonzero ones! We can also do this programmically, like so:

```python
# Print all the nonzero christoffel symbols in the form (Gamma^g_ab = ...)
# the "latex" option here allows returning a LaTeX expression
# rather than a list of equations
def find_nonzero_christoffels(coords, metric, inverse_metric, latex=True):
    christoffels, christoffels_tex_symbols = calculate_all_christoffels(coords, metric, inverse_metric)
    dimensions = len(coords)
    nonzero_christoffels = []
    for g in range(dimensions):
        for a in range(dimensions):
            for b in range(dimensions):
                # ignore diagonal entries or vanishing components
                if a > b or christoffels[g][a][b] == 0:
                    continue
                else:
                    ch_symbol = christoffels[g][a][b]
                    tex_symbol = christoffels_tex_symbols[g][a][b]
                    eq = Eq(tex_symbol, ch_symbol)
                    nonzero_christoffels.append(eq)
    if not latex:
        return nonzero_christoffels
    else:
        latex_str = r"\begin{align}"
        for eq in nonzero_christoffels:
            latex_eq = sympy_to_latex(eq).replace("=", r"&=")
            latex_str += "\n" + latex_eq + r" \\"
        latex_str += "\n" + r"\end{align}"
        return latex_str
```

We don’t have to stop there! In fact, we can also find the geodesic equations from the Christoffel symbols that were programmically calculated:

```python
def find_geodesic_equations(coords, christoffels_array, affine_parameter=r"\lambda"):
    # `christoffels_array` should be the first element of the
    # output of the function calculate_all_christoffels()
    dimensions = len(coords)
    parameter = Symbol(affine_parameter)
    # 4-position vector as a function of the affine parameter
    X = [Function(coord.name)(parameter) for coord in coords]
    # initialize equations of motion (setting RHS = 0 to start)
    EoMs_lhs = [diff(x_gamma, parameter, 2) for x_gamma in X]
    EoMs_rhs = [0 for _ in range(dimensions)]
    for gamma in range(dimensions):
        for a in range(dimensions):
            for b in range(dimensions):
                # ignore vanishing components
                # TODO: take advantage of symmetries of christoffel symbols
                if christoffels_array[gamma][a][b] == 0:
                    continue
                else:
                    ch_symbol = christoffels_array[gamma][a][b]
                    EoMs_rhs[gamma] += -ch_symbol*diff(X[a], parameter)*diff(X[b], parameter)
    return Eq(Matrix(EoMs_lhs), Matrix(EoMs_rhs))
```

All of this can be pasted into a single cell in a Jupyter notebook and executed prior to any other computations, since it is very general and doesn’t rely on the metric taking a particular form. Then, to begin a calculation, we use the following code:

```python
# enter your coordinates (in LaTeX, separated by 1 space each)
theta, phi = symbols(r"\theta \phi")
coords = [theta, phi]
# define any constants you need
R = Symbol("R", constant=True, real=True)

# input in your given metric in matrix form
metric = Array([
    [R**2, 0],
    [0,    R**2 * sin(theta)**2]
])

# calculate inverse metric
inverse_metric = Array(Matrix(metric).inv())

# ensure that the variables "coords", "metric", "inverse_metric"
# are available (don't rename them!) since it's used in
# the rest of the code
```

In a Jupyter notebook, we can preview the line element via running the code:

```python
# preview line element (best used in Jupyter notebook)
line_element_from_metric(metric)
```

Aftewards, we can compute the Christoffel symbols as follows:

```python
# pretty-print calculated symbol (best used for Jupyter notebooks)
def calculate_symbol_fmt(*indices, coords=coords, 
		g=metric, g_inv=inverse_metric):
    try:
        christoffel = calculate_symbol(*indices, coords, g, g_inv)
        return Eq(christoffel[0], christoffel[1])
    except:
        raise Exception("Christoffel symbol calculation unsuccessful")

# Now we can compute the Christoffel symbols
# (this is best when used in a Jupyter notebook)
calculate_symbol_fmt((theta, phi, phi)) # returns -sin(theta) cos(theta)
```

If run in a Jupyter notebook, this should return $\Gamma^\theta_{\phi \phi} = -\sin \theta \cos \theta$, the same as we obtained manually. We can also do the same to find the $\Gamma^\phi_{\theta \phi}$ Christoffel symbol:

```python
# Compute another Christoffel symbol
# (this is best when used in a Jupyter notebook)
calculate_symbol_fmt((phi, theta, phi)) # returns cos (theta) / sin(theta)
```

This should return $\Gamma^\phi_{\theta \phi}  = \cos \theta / \sin \theta$, which of course is equal to $\cot \theta$, the same result as we got when we calculated the Christoffel symbols by hand. Finally, we can get the full list of Christoffel symbols with this code:

```python
nonzero_christoffels = find_nonzero_christoffels(coords, metric, inverse_metric)
# Print LaTeX of all nonzero christoffel symbols
print(nonzero_christoffels)
```

In our case for the Christoffel symbols of the 2-sphere, we get this result:

```latex
\begin{align}
\Gamma^\theta_{\phi \phi} &= - \sin{\left(\theta \right)} \cos{\left(\theta \right)} \\
\Gamma^\phi_{\theta \phi} &= \frac{\cos{\left(\theta \right)}}{\sin{\left(\theta \right)}} \\
\end{align}
```

Which, when rendered in any LaTeX editor/viewer (or an online viewer like the one on [this website](https://viereck.ch/latex-to-svg/)) shows up as this:

{% math() %}
\begin{align}
\Gamma^\theta_{\phi \phi} &= - \sin{\left(\theta \right)} \cos{\left(\theta \right)} \\
\Gamma^\phi_{\theta \phi} &= \frac{\cos{\left(\theta \right)}}{\sin{\left(\theta \right)}} \\
\end{align}
{% end %}

If you are using Jupyter notebook, you can also interactively display the printed Christoffel symbols like this, which should show the same rendered result:

```python
# Print rendered version - this works in Jupyter Notebook/JupyterLab only!
display(Math(nonzero_christoffels))
```

Finally, we can find the geodesic equations, as follows:

```python
# In a Jupyter notebook the following code should display
# the equations in matrix form
chrs = calculate_all_christoffels(coords, metric, inverse_metric)[0]
geodesics = find_geodesic_equations(coords, chrs)
geodesics
```

From which we obtain the following result, which is exactly the same as what we got when we hand-calculated the geodesics:

{% math() %}
\left[\begin{matrix}\frac{d^{2}}{d \lambda^{2}} \theta{\left(\lambda \right)}\\\frac{d^{2}}{d \lambda^{2}} \phi{\left(\lambda \right)}\end{matrix}\right] = \left[\begin{matrix}\sin{\left(\theta \right)} \cos{\left(\theta \right)} \left(\frac{d}{d \lambda} \phi{\left(\lambda \right)}\right)^{2}\\- \frac{2 \cos{\left(\theta \right)} \frac{d}{d \lambda} \phi{\left(\lambda \right)} \frac{d}{d \lambda} \theta{\left(\lambda \right)}}{\sin{\left(\theta \right)}}\end{matrix}\right]
{% end %}

The complete code can be found in [`calculate-christoffel-symbols.py`](../calculate-christoffel-symbols.py). Feel free to play around with it and make your own customizations!

> **Note:** There exist Python packages that have far more optimized implementations for performing GR calculations such as [EinsteinPy](https://einsteinpy.org/); this implementation is simply for educational purposes and will be far less optimized compared to true GR packages. In addition, it is possible to perform similar computations in Mathematica and Maple software, but since SymPy is free and open-source, the examples are given using SymPy.

## The Schwarzschild metric

We will now examine the simplest metric of General Relativity: the **Schwarzschild metric**, which describes the spacetime geometry outside a spherically-symmetric mass distribution. The line element for the Schwarzschild metric is given by:

{% math() %}
ds^2 = -\left(1 - \frac{r_s}{r}\right) c^2 dt^2 + \left(1 - \frac{r_s}{r}\right)^{-1} dr^2 + r^2d\Omega^2
{% end %}

Where $d\Omega^2 = d\theta^2 + \sin^2 \theta d\phi^2$ is the familiar metric of the 2-sphere of unit radius, and $r_s$ is known as the **Schwarzschild radius**, given by:

{% math() %}
r_s = \frac{2GM}{c^2}
{% end %}

The Schwarzschild metric has several important characteristics:

- It is a **static metric**, meaning the metric is time-independent (that is, it does not change over time)
- It is a **vacuum metric**, meaning that it describes space with negligible mass-energy; this means it is only applicable for the spacetime *outside* a gravitating body
- It has **spherical symmetry**, allowing us to use spherical coordinates (at least for the spatial components)

### Schwarzschild geodesics

Let us now find the geodesics associated with the Schwarzschild metric, which tells us what trajectories a particle would travel within spacetime. In principle, we could use the geodesic equation in its standard form $\ddot x^\mu = -\Gamma^\mu_{\rho \sigma} \dot x^\rho \dot x^\sigma$, but working out all the Christoffel symbols from the Schwarzschild metric is extremely tedious. Instead, we'll use a convenient shortcut. Recall that the Lagrangian of a particle moving in spacetime with metric $g_{\mu \nu}$ is given by:

{% math() %}
\mathcal{L} = g_{\mu \nu} \frac{dx^\mu}{d\tau} \frac{dx^\nu}{d\tau}
{% end %}

Where we know that the equations of motion are given by the Euler-Lagrange equation:

{% math() %}
\frac{d}{d\tau}\left(\frac{\partial \mathcal{L}}{\partial \dot x^\beta}\right) = \frac{\partial \mathcal{L}}{\partial x^\beta}
{% end %}

Where $\dot x^\beta \equiv \dfrac{dx^\beta}{d\tau}$ (the dot notation represents a derivative with respect to *proper time* unless otherwise specified). In the case of the Schwarzschild metric (which is diagonal), we have:

{% math() %}
\begin{align*}
\mathcal{L} &= g_{00} \frac{dx^0}{d\tau} \frac{dx^0}{d\tau} + g_{11} \frac{dx^1}{d\tau} \frac{dx^1}{d\tau} + g_{22} \frac{dx^2}{d\tau} \frac{dx^2}{d\tau} + g_{33} \frac{dx^3}{d\tau} \frac{dx^3}{d\tau} \\
&= -\left(1 - \frac{r_s}{r}\right) c^2 \dot t^2 + \left(1 - \frac{r_s}{r}\right)^{-1} \dot r^2 + r^2 \dot \theta^2 + r^2 \sin^2 \theta \dot \phi^2
\end{align*}
{% end %}

We can then directly plug in our Lagrangian into the Euler-Lagrange equation, which yields four ODEs in a reasonably straightforward way. However, it turns out we can get the same ODEs with a lot less work, using some clever intuition. This comes as a result of the fact that our Lagrangian has no dependence on $t$ or $\phi$, so we have:

{% math() %}
\frac{\partial \mathcal{L}}{\partial t}, \frac{\partial \mathcal{L}}{\partial \phi} = 0
{% end %}

Thus substituting into the Euler-Lagrange equations for $r$ and $\phi$ gives us:

{% math() %}
\begin{align*}
\frac{d}{d\tau} \left(\frac{\partial \mathcal{L}}{\partial \dot t}\right) = \frac{\partial \mathcal{L}}{\partial t} = 0 \\
\Rightarrow \frac{\partial \mathcal{L}}{\partial \dot t} = \text{const.} \\
\frac{d}{d\tau} \left(\frac{\partial \mathcal{L}}{\partial \dot \phi}\right) = \frac{\partial \mathcal{L}}{\partial \phi} = 0 \\
\Rightarrow \frac{\partial \mathcal{L}}{\partial \dot \phi} = \text{const.} 
\end{align*}
{% end %}

This is because we know that if the (ordinary) derivative of a function is zero, then it must equal a constant, that is:

{% math() %}
\frac{d}{d\tau}(\text{constant}) = 0
{% end %}

Schwarzschild geodesics, like classical Newtonian orbits, always lie in a plane, meaning that $\dot \theta = 0$ (this is not true for other spacetime metrics). Now, since the orbits are in a plane, the value of $\theta$ must be *constant*. We may arbitrary choose any value of $\theta$; we can choose $\theta = \frac{\pi}{2}$ for convenience. We have the freedom to do so because we can arbitrarily redefine our coordinate system using a coordinate transform such that the orbits are *always* within a plane. Remember that in GR, coordinates themselves do not *necessarily* have physical meaning, so one set of coordinates works just as well as another for describing a particular spacetime geometry. This simplifies the Lagrangian to:

{% math() %}
\mathcal{L} = -\left(1 - \frac{r_s}{r}\right) c^2 \dot t^2 + \left(1 - \frac{r_s}{r}\right)^{-1} \dot r^2 + r^2 \dot \phi^2
{% end %}

Taking the partial derivatives of the Lagrangian gives us:

{% math() %}
\begin{align*}
\frac{\partial \mathcal{L}}{\partial \dot t} &= -2\left(1 - \frac{r_s}{r}\right)c^2 \dot t \\
\frac{\partial \mathcal{L}}{\partial \dot \phi} &= 2 r^2 \dot \phi
\end{align*}
{% end %}

We know from earlier that $\frac{\partial \mathcal{L}}{\partial \dot t}$ and $\frac{\partial \mathcal{L}}{\partial \dot \phi}$ are both equal to a constant, so our equations of motion become:

{% math() %}
\begin{gather*}
-2\left(1 - \frac{r_s}{r}\right)c^2 \dot t = A \\
2 r^2 \dot \phi = B
\end{gather*}
{% end %}

Where $A, B$ are some constants. We can write the above equations of motion in a more elegant form by expressing them in terms of two expressions $\kappa$ and $j$, which are respectively given by:

{% math() %}
\kappa = \left( 1 - \frac{r_{s}}{r} \right) c \frac{dt}{d\tau}, \quad j = r^2 \frac{d\phi}{d\tau}
{% end %}

From which we see that $A = -2\kappa c$ and $B = 2j$. By rearranging the above two equations, we find the explicit equations of motion for $\dot t$ and $\dot \phi$:

{% math() %}
\begin{align*}
\frac{dt}{d\tau} &= \frac{\kappa}{c}\left(1 - \frac{r_s}{r}\right)^{-1} \\
\frac{d\phi}{d\tau} &= \frac{j}{r^2}
\end{align*}
{% end %}

> **Note:** It is common to also see $j$ written as $h$ or $\ell$ or $l$ in other texts, but these are just different symbols to describe the *same* thing.

Since $\kappa$ and $j$ are both constants, we call them the **constants of motion**. It turns out that $\kappa$ is dimensionless, while $j$ has units of angular momentum over mass. Thus, we say that $j$ corresponds to the **specific angular momentum** (angular momentum per unit mass; although more precisely it is angular momentum over the [reduced mass](https://en.wikipedia.org/wiki/Reduced_mass) of the system). Meanwhile, $\kappa$ is the ratio of the orbiting particle’s total energy over its rest energy, that is, $\kappa = E/mc^2$. Thus we have found three of the four equations of motion in a very simple and straightforward way! (The equation of motion for $\theta$ is simply $\dot \theta = 0$).

Lastly, we can find the equation of motion for $r$. The reason we have not found it so far from the Euler-Lagrange equations is because differentiating the Lagrangian with respect to $r$ is quite tedious and there is a much simpler and more elegant way to find the equation of motion for $r$. Instead, we can use the identity that:

{% math() %}
\mathcal{L} = g_{\mu \nu} \frac{dx^\mu}{d\tau} \frac{dx^\nu}{d\tau} = -c^2
{% end %}

Which comes from the fact that $g_{\mu \nu} dx^\mu dx^\nu = ds^2$, and since $ds^2 = -c^2 d\tau^2$, we have:

{% math() %}
\mathcal{L} = \frac{ds^2}{d\tau^2} = -c^2
{% end %}

Substituting this result into the Lagrangian gives us:

{% math() %}
-\left(1 - \frac{r_s}{r}\right) c^2 \dot t^2 + \left(1 - \frac{r_s}{r}\right)^{-1} \dot r^2 + r^2 \dot \phi^2 = -c^2
{% end %}

Which we can write in terms of $\kappa$ and $j$ as:

{% math() %}
\begin{gather*}
- \frac{\kappa^2}{c^2} \left(1 - \frac{r_s}{r}\right)^{-1} + 
\left( 1 - \frac{r_{s}}{r} \right)^{-1} \dot{r}^2
+ \frac{j^2}{r^2} = -c^2 \\
\Longrightarrow \left(1 - \frac{r_s}{r}\right)^{-1}\left( \dot{r}^2 - \frac{\kappa^2}{c^2} \right) + \frac{j^2}{r^2} = -c^2
\end{gather*}
{% end %}

We can now rearrange to solve for $\dot r$, as follows:

{% math() %}
\begin{gather*}
\left(1 - \frac{r_s}{r}\right)^{-1}\left( \dot{r}^2 - \frac{\kappa^2}{c^2} \right) = -c^2 - \frac{j^2}{r^2} \\
\left( \dot{r}^2 - \frac{\kappa^2}{c^2} \right) = -\left(1 - \frac{r_s}{r}\right)\left( c^2 + \frac{j^2}{r^2} \right) \\
\dot{r}^2 = \frac{\kappa^2}{c^2} -\left(1 - \frac{r_s}{r}\right)\left( c^2 + \frac{j^2}{r^2} \right)
\end{gather*}
{% end %}

This is the equation of motion for $r$, the last of our four equations of motion! Note that if we wish to write the above equation in terms of the *total energy* of the orbiting particle, by definition of $\kappa = E/mc^2$, we have:

{% math() %}
\left( \frac{dr}{d\tau} \right)^2 = \frac{E^2}{m^2c^2} -\left(1 - \frac{r_s}{r}\right)\left( c^2 + \frac{j^2}{r^2} \right)
{% end %}

Which is the form that is often presented in textbooks, and tells us that the radial motion of the particle is closely related to its energy and angular momentum.


### Extra: numerically plotting Schwarzschild geodesics

(Will be completed later)

### The Schwarzschild effective potential

Let’s take another look at the equation of motion for $\dot r$, which is given by:

{% math() %}
\left( \frac{dr}{d\tau} \right)^2 = \frac{E^2}{m^2c^2} -\left(1 - \frac{r_s}{r}\right)\left( c^2 + \frac{j^2}{r^2} \right)
{% end %}

If we expand the right-hand side, we obtain:

{% math() %}
\left( \frac{dr}{d\tau} \right)^2 = \frac{E^2}{m^2 c^2} - c^2 + \frac{r_{s} c^2}{r} - \frac{j^2}{r^2} + \frac{r_{s}j^2}{r^3}
{% end %}

Meanwhile, if we multiply all sides by $\frac{1}{2}m$, we obtain:

{% math() %}
\frac{1}{2} m\left( \frac{dr}{d\tau} \right)^2 = \left[ \frac{E^2}{2mc^2} - \frac{1}{2} mc^2 \right] + \frac{GMm}{r} - \frac{m j^2}{2r^2} + \frac{GMm j^2}{c^2r^3}
{% end %}

We notice that the first term is exactly the Newtonian (non-relativistic) kinetic energy, whereas the term in square brackets has units of energy. Defining the *effective energy* $\mathcal{E}$, which is equal to the term in square brackets, that is:

{% math() %}
\mathcal{E} = \frac{E^2}{2mc^2} - \frac{1}{2} mc^2
{% end %}

Then we may substitute to find:

{% math() %}
\frac{1}{2} m\left( \frac{dr}{d\tau} \right)^2 = \mathcal{E} - \left[  -\frac{GMm}{r} + \frac{m j^2}{2r^2} - \frac{GMm j^2}{c^2r^3} \right]
{% end %}

Rearranging, we have:

{% math() %}
\underbrace{ \frac{1}{2}m \left( \frac{dr}{d\tau} \right)^2 }_{ K } + \underbrace{ \left[  -\frac{GMm}{r} + \frac{m j^2}{2r^2} - \frac{GMm j^2}{c^2r^3} \right] }_{ U_\text{eff} } = \mathcal{E}
{% end %}

Since the first term is simply the kinetic energy $K$, and $\mathcal{E}$ is an effective energy, this looks exactly like the form of an energy conservation equation $K + U = E$, except with an *effective total energy* $\mathcal{E}$ and an *effective potential energy* $U$, which we denote as $U_\text{eff}$. Thus the above equation is known as the **energy balance equation**. From it, we can see that the effective potential energy is thus given by:

{% math() %}
U_\text{eff} = -\frac{GMm}{r} + \frac{m j^2}{2r^2} - \frac{GMm j^2}{c^2r^3}
{% end %}

Or, if written in terms of the angular momentum $L = m j$ of the particle (not to be confused with the Lagrangian $\mathcal{L}$), we have:

{% math() %}
U_\text{eff} = -\frac{GMm}{r} + \frac{L^2}{2mr^2} - \frac{GM L^2}{c^2mr^3}
{% end %}

> **Note:** It is common to drop the term “effective potential energy” and simply call $U_\text{eff}$ the “effective potential”. While this terminology is not *technically* correct, it is used so frequently that we will also adopt it. Also, we will use the simplified form by assuming that $\mu \approx m$, which is the case for $M \gg m$.

Note that a more careful calculation would use the reduced mass $\mu = \dfrac{Mm}{M + m}$ of the system, for which the effective potential should be written as:

{% math() %}
U_\text{eff} = -\frac{GMm}{r} + \frac{L^2}{2\mu r^2} - \frac{G(M + m) L^2}{c^2\mu r^3}
{% end %}

The effective potential is related to the acceleration of the particle by Newton’s second law, which tells us that (in the one-dimensional case):

{% math() %}
F = m \frac{d^2 r}{dt^2}= -\frac{dU}{dr}
{% end %}

Where $F$ is the force and $U$ is the potential energy. Since we are considering effective potentials in a relativistic setting, however, then $F$ becomes the *effective force* $F_\text{eff}$, giving us:

{% math() %}
F_\text{eff} = m \frac{d^2 r}{dt^2} = -\frac{dU_\text{eff}}{dr}
{% end %}

And thus the particle’s acceleration $\vec{a}$ is given by:

{% math() %}
\vec{a} = \frac{d^2 r}{dt^2}\hat{r} =  -\frac{1}{m} \frac{dU_\text{eff}}{dr}\hat{r}
{% end %}

If we define $V_\text{eff} \equiv U_\text{eff}/m$, we can express the above in an even simpler form:

{% math() %}
\frac{d^2 r}{dt^2} =  -\frac{dV_\text{eff}}{dr}
{% end %}

This is another form of the radial equation of motion, and can be used to find the orbits of particles in Schwarzschild spacetime.

#### Newtonian orbits

It is useful to compare Schwarzschild effective potential with the Newtonian case. In Newtonian mechanics, the potential of a spherically-symmetric body (for instance, of an ideal planet or star) is given by $\Phi = -GM/r$. However, a particle orbiting a central body also experiences a *centrifugal acceleration* due to their rotational motion under a central force (i.e. gravity). The effects of both the static potential of the central body and the centrifugal acceleration can be also be modelled by a **Newtonian effective potential**, which is given by:

{% math() %}
U_\text{eff}(r) = -\frac{GMm}{r} + \frac{L^2}{2mr^2}
{% end %}

(Where again, $L$ is the angular momentum, not the Lagrangian). A plot of this potential is shown below:

![Plot of the Newtonian effective potential](https://i.sstatic.net/slUTn.png)

_Source: [Physics StackExchange](https://physics.stackexchange.com/questions/379708/doubts-about-the-effective-potential-in-newtonian-gravity)_

The behavior of the particle depends on its energy $\varepsilon$. Several possibilities for orbits are the direct result of different energies:

- $\varepsilon > 0$: hyperbolic orbits (orbits in the shape of a hyperbola)
- $\varepsilon = 0$: parabolic orbits (orbits in the shape of a parabola)
- $\varepsilon < 0$: elliptic orbits (orbits in the shape of an ellipse)

In Newtonian gravity, only elliptic orbits are *bound orbits*, meaning that the particle can orbit the central body in a stable orbit. Parabolic orbits “shoot past” the particle after orbiting for some time, while hyperbolic orbits deflect the particle away. Finally, it is notable that the particle **cannot** fall into the central body; it would take an infinite velocity for the particle to even reach the central body.

#### Schwarzschild orbits

Let’s now consider the case of Schwarzschild orbits (i.e. Schwarzschild geodesics), which (as we have seen) has the effective potential:

{% math() %}
U_\text{eff} = -\frac{GMm}{r} + \frac{L^2}{2mr^2} - \frac{GM L^2}{c^2mr^3}
{% end %}

Notice how this effective potential is exactly the same as the Newtonian effective potential, except with one additional term that is proportional to $1/r^3$. The additional $1/r^3$ term (compared to the Newtonian effective potential) is *tiny* since $G/c^2 \sim 10^{-28}$, so this additional term can be ignored in most non-relativistic cases. However, in the case of highly-compact astronomical objects (such as neutron stars and black holes), this *does* have an effect. Unlike the Newtonian case, it means that orbits *can* decay and particles can fall into the central body!

![Plots of Schwarzschild geodesics](https://astronuclphysics.info/Gravit4-6.gif)

_The Schwarzschild effective potential. Source: [Astronuclear Physics](https://astronuclphysics.info/Gravitace4-3.htm)_

This result comes from the fact that the Schwarzschild effective potential has an additional turning point that is not found in the Newtonian case. This means that the Schwarzschild effective potential drops rapidly as $r \to 0$, meaning that particles within the event horizon plunge towards the central body, rather than being deflected as in the Newtonian case. It also means that the orbits are no longer ellipses, rather, they exhibit a rotational motion known as **perihelion precession**, as shown in the graph below:

![Plot of perihelion precession](https://campuscore.ariel.ac.il/wp/gilbert-weinstein/wp-content/uploads/sites/292/2017/12/schw-768x576.jpg)

_Source: [Gilbert Weinstein](https://campuscore.ariel.ac.il/wp/gilbert-weinstein/2017/12/25/the-geodesics-of-the-schwarzschild-metric-6/)_

We therefore say that the orbit *precesses*, meaning that the orbit itself rotates over time. Examining this phenomenon will be what we will discuss next.

### Deriving the perihelion precession

The perihelion precession can be derived by using a perturbative approach. To begin, let us start with the energy balance equation:

{% math() %}
\frac{1}{2}m \left( \frac{dr}{d\tau} \right)^2  + \left[  -\frac{GMm}{r} + \frac{m j^2}{2r^2} - \frac{GMm j^2}{c^2r^3} \right] = \mathcal{E}
{% end %}

Which can also be written in the following form:

{% math() %}
\frac{1}{2} m \dot{r}^2 + \left( 1 - \frac{r_{s}}{r} \right) \frac{mj^2}{2r^2}  - \frac{GMm}{r} = \mathcal{E}
{% end %}

We want to express $r$ in terms of $\phi$, so we must perform a change of variables to go from $r(\tau)$ to $r(\phi)$. This can be done by noting that $j$ is defined by $j = r^2 \dot \phi$, so:

{% math() %}
j = r^2 \left( \frac{d\phi}{d\tau} \right) \quad \Rightarrow \quad d\tau = \frac{r^2}{j} d\phi
{% end %}

It is also useful to make the coordinate transformation $r \to u$, where $u \equiv 1/r$. This will make solving the equations of motion easier. Using the chain rule, we have:

{% math() %}
\frac{dr}{d\phi} = \frac{dr}{du} \frac{du}{d\phi} = -\frac{1}{u^2} \frac{du}{d\phi} = -r^2 \frac{du}{d\phi}
{% end %}

Now using the chain rule again gives us:

{% math() %}
\frac{dr}{d\tau} = \frac{dr}{d\phi} \frac{d\phi}{d\tau} = \dot{\phi} \frac{dr}{d\tau} = \frac{j}{r^2} \frac{dr}{d\phi}
{% end %}

Which comes from rearranging $j = r^2 \dot \phi$ to $\dot \phi = j/r^2$. Combining the previous two equations gives us:

{% math() %}
\begin{align*}
\frac{dr}{d\tau} = \frac{j}{r^2} \frac{dr}{d\phi} &= \frac{j}{r^2}\left( -r^2 \frac{du}{d\phi} \right) \\
&= -j \frac{du}{d\phi}
\end{align*}
{% end %}

Substituting our found expression for $\dot r = \dfrac{dr}{d\tau}$ into the energy balance equation, we obtain:

{% math() %}
\frac{1}{2}mj^2 \left( \frac{du}{d\phi} \right)^2 + \left( 1 - ur_{s} \right) \frac{mj^2}{2}u^2  - (GMm) u = \mathcal{E}
{% end %}

Multiplying all sides by $2/(mj^2)$ gives us a differential equation for $u(\phi)$:

{% math() %}
\left( \frac{du}{d\phi} \right)^2 + \left( 1 - ur_{s} \right) u^2  - \frac{2GM}{j^2} u = \frac{2\mathcal{E}}{mj^2}
{% end %}

Note that this can also be written in terms of the angular momentum $L = mj$ as follows:

{% math() %}
\left( \frac{du}{d\phi} \right)^2 + \left( 1 - ur_{s} \right) u^2  - \frac{2GMm^2}{L^2} u = \frac{2m\mathcal{E}}{L}
{% end %}

We can simplify this expression by defining the following constants:

{% math() %}
\alpha = \frac{L^2}{GMm^2}, \quad C = \frac{2m\mathcal{E}}{L}
{% end %}

For which our differential equation becomes:

{% math() %}
\left( \frac{du}{d\phi} \right)^2 + \left( 1 - ur_{s} \right) u^2  - \frac{2}{\alpha} u = C
{% end %}

Or, fully expanded and written using the shorthand $u' = u'(\phi) = \frac{du}{d\phi}$, we have:

{% math() %}
u'^2 + u^2 - r_{s} u^3 - \frac{2}{\alpha} u = C
{% end %}

This is in the form of a [Binet equation](https://en.wikipedia.org/wiki/Binet_equation), a nonlinear first-order differential equation, albeit one whose exact solution can only be expressed in terms of [elliptic functions](https://en.wikipedia.org/wiki/Jacobi_elliptic_functions). We will instead only seek to find an approximate solution, which we can do via perturbation theory. Let $u = u(\phi)$ be in the form:

{% math() %}
u = u_{0} + u_{1}
{% end %}

Where $u_0$ is the solution to the ODE in the limit $r_s \to 0$, that is:

{% math() %}
u_{0}'^2 + u_{0}^2 - r_{s} u^3 - u_{0} = C
{% end %}

If we differentiate all sides of this equation with respect to $\phi$, we obtain, after some simplification:

{% math() %}
u_{0}'' + u_{0} - \frac{1}{\alpha} = 0
{% end %}

This is in the form of a driven harmonic oscillator, whose solution is given by:

{% math() %}
u_{0} = \frac{1}{\alpha} (1 + e\cos \phi)
{% end %}

Where $e$ is a constant (_not_ Euler’s number!) and is formally known as the **eccentricity** and $e \geq 0$. Thus, in the case $r_s \approx 0$ (non-relativistic approximation), we have $u \approx u_{0}$ and thus:

{% math() %}
r \equiv \frac{1}{u} \approx \frac{1}{u_{0}} \quad \Rightarrow \quad r \approx \frac{\alpha}{1 + e \cos \phi}
{% end %}

This solution is the classical Newtonian solution of the orbit of a particle around a gravitating massive body, and for closed orbits (in which $0 \leq e < 1$) it takes the form of an **ellipse** in polar coordinates.

Now, let us use this solution to find an approximate form of $u_1$. Recall that $u = u_{0} + u_{1}$.

{% math() %}
(u_{0} + u_{1})'^2 + (u_{0} + u_{1})^2 - r_{s} (u_{0} + u_{1})^3 - \frac{2}{\alpha} (u_{0} + u_{1}) = C
{% end %}

If we expand this and substitute in $u_{0} = (1 + e\cos \phi)/\alpha$ and $u_0' = -e \sin(\phi) / \alpha$ we obtain:

{% math() %}
u_{1} e \cos \phi - e \sin \phi \frac{ du_{1}}{d\phi} = \frac{r_{s}}{2\alpha^2}(1 + e \cos \phi)^3
{% end %}

Dividing by $-e \sin \phi$ on all sides gives us:

{% math() %}
\frac{du_{1}}{d\phi} - u_{1}\cot \phi = -\frac{r_{s}}{2e\alpha^2}\left( \frac{(1 + e \cos \phi)^3}{\sin \phi} \right)
{% end %}

This is a linear first-order differential equation that is in the general form $y' + p(\phi) y = q(\phi)$, which can be solved exactly using the **method of integrating factors**. We will dispense with solving it to avoid this derivation growing overly long, but if interested, you can see the [differential equations guide](@/differential-equations/index.md). In any case, the exact solution is:

{% math() %}
u_{1} = \frac{r_{s}}{2\alpha^2} \left[ (3 + 2e^2) +  \left( \frac{1 + 3e^2}{e} \right) \cos \phi - e^2 \cos^2 \phi + 3 e \phi \sin \phi \right]
{% end %}

Substituting this into $u = u_0 + u_1$ and with $u_{0} = (1 + e\cos \phi)/\alpha$, we have:

{% math() %}
\begin{align*}
u = \frac{1}{\alpha}\bigg[   (1 + e\cos \phi) &+ \frac{r_{s}}{2\alpha} \bigg( (3 + 2e^2) +  \left( \frac{1 + 3e^2}{e} \right) \cos \phi \\
&- e^2 \cos^2 \phi + 3 e \phi \sin \phi\bigg) \bigg] \\
= \frac{1}{\alpha}[1 + \overline e \cos \phi &+ \epsilon e\phi \sin \phi + \beta_{1} + \beta_{2} \cos^2 \phi ]
\end{align*}
{% end %}

Where we have:

{% math() %}
\begin{align*}
\beta_{1} &= \frac{r_{s}(3 + 2e^2)}{2\alpha} \\
\beta_{2} &= -\frac{r_{s} e^2}{2\alpha} \\
\epsilon &= \frac{3r_{s}}{2\alpha} \\
\overline e &= e + \frac{r_{s}(1 + 3e^2)}{2e\alpha}
\end{align*}
{% end %}

In our perturbative solution for $u$, the values of $\beta_1$ and $\beta_2$ are of order $\mathcal{O}(e^2)$ and can thus be ignored (to a first approximation). Experimentally, we have measured these parameters to be on the order of $10^{-7}$, which supports this conclusion. Meanwhile, to a good approximation, $\overline e \approx e$. Thus we can write our solution (approximately) as:

{% math() %}
\begin{gather*}
u = \frac{1}{\alpha} [1 + e \cos \phi + \epsilon e\phi \sin \phi] \\
\Rightarrow r = \frac{\alpha}{1 + e [\cos \phi + \epsilon \phi \sin \phi]}
\end{gather*}
{% end %}

Notice that the first two terms are the same as in Newtonian gravity, and if we ignored the third term, we have the standard equation of an ellipse:

{% math() %}
r = \frac{1}{u} = \frac{\alpha}{1 + e \cos \phi}
{% end %}

But the third term is significant since it is proportional to $\phi$, and therefore will grow for each orbit. For orbits over short time intervals, this does not matter much; but over long periods of time (decades or even centuries) the effects become dramatically noticeable. To see why, let us first note that using trigonometric identities, we can (approximately) write our perturbed solution as:

{% math() %}
r = \frac{\alpha}{1 +  e \cos[(1 - \epsilon) \phi]}
{% end %}

Now, the classical Newtonian solution (an ellipse) is periodic over $2\pi$ radians, meaning that one complete orbit causes the particle to return to its initial position. But this is *not* the case with Schwarzschild orbits, since the $\cos \phi$ term is altered to $\cos [(1 - \epsilon)\phi]$. Setting $(1 - \epsilon) \phi = 2\pi$ (since one complete orbit in the Newtonian case would have $\phi = 2\pi$), then we obtain the *actual* value of $\phi$:

{% math() %}
\phi = \frac{2\pi}{1-e} \approx 2\pi (1 - \epsilon)  \implies \delta \phi \equiv 2\pi - \phi =  2\pi \epsilon
{% end %}

This means that over one complete orbit, the Schwarzschild case has $\phi \neq 2\pi$, with the accumulated _additional_ angular displacement $\delta \phi$ being $2\pi \epsilon$. This additional angular displacement is called the **perihelion precession**.

Let us now substitute $\epsilon$ explicitly to find $\delta \phi$ in terms of measurable parameters. First, note that $\alpha = A(1 - e^2)$, where $A$ is the **semi-major axis** (the furthest distance of the orbiting particle to the central body) and $e$ is (once again) the **eccentricity**. This can be found from the conservation of angular momentum, which (after tedious mathematics, [see derivation here](https://physics.stackexchange.com/questions/455066/why-does-angular-momentum-being-constant-prove-keplers-first-law)) tells us that $L^2 = GMm^2 A (1 - e^2)$, where $L$ is the angular momentum, and we can then substitute this into the definition of $\alpha$ with $\alpha = \frac{L^2}{GMm^2}$. Thus, we obtain the following formula for the perihelion precession per orbit:

{% math() %}
\begin{align*}
\delta \phi &= 2\pi \epsilon \\
&= \frac{6\pi r_{s}}{2\alpha} \\
&= \frac{6\pi }{2A(1 - e^2)} \frac{2GM}{c^2} \\
&= \frac{6\pi GM}{c^2 A(1 - e^2)}
\end{align*}
{% end %}

Note that if expressed in terms of the *orbital period* $T$ of the particle, we can use Kepler’s third law $T^2 = \dfrac{4\pi^2 A^3}{GM}$ to obtain the same result, except expressed in terms of the orbital period:

{% math() %}
\delta \phi = \frac{24\pi^3 A^2}{T^2c^2 (1 - e^2)}
{% end %}

This result has units of **radians per revolution**, and is directly proportional to the number of orbits completed by the test particle.

#### Perihelion precession of Mercury

Perihelion precession was infamously observed in the case of the planet Mercury, which has a semi-major axis of $A = 5.791 \times 10^{10} \text{ m}$, an orbital period $T$ of 115.88 days, and an orbital eccentricity of $e = 0.20564$. Since Mercury orbits the Sun, whose mass is $M \approx 2 \times 10^{30} \text{ kg}$, its orbit slowly precesses by $\delta \phi = 6.61 \times 10^{-7}$ arcseconds per orbit. This precession is all but unnoticeable over short times, but over a period of a century, this adds up to an angular precession of around 43 arcseconds - almost _exactly_ the amount found by astronomical observations. The prediction of the perihelion precession of Mercury to such an astounding degree of accuracy was one of the first triumphs of the theory of general relativity!