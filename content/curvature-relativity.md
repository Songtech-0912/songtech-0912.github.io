+++
title = "Visualizing curvature in General Relativity"
date = 2023-11-17
+++

General Relativity is a theory of gravity that is formulated in a 4-dimensional spacetime. So how do we visualize spacetimes, if they're 4D? This article will hopefully explain the mathematics of how one type of visualization, embedding diagrams, work.

<!-- more -->

Take the Schwarzschild metric:

{% math() %}
ds^2 = -\left(1 - \frac{R_s}{r}\right) c^2 dt^2 + \frac{1}{\left(1 - \frac{R_s}{r}\right)} dr^2 + r^2 (d\theta^2 + \sin^2 d\phi^2)
{% end %}

Where:

{% math() %}
R_s = \frac{2GM}{c^2}
{% end %}

Note that we have a problem: spacetime is 4D, but we can only visualize curvature of a function of two variables embedded in 3D space. So we need to reduce 4D spacetime down 2 dimensions to visualize it effectively. Typically, to do so, we take a 2D slice of 4D spacetime by setting $t = 0$ and $\phi = 0$ (the $\phi$ coordinate because the metric is spherically symmetric, so it'll look the same whichever $\phi$ we choose, which is why we can take any arbitrary slice of it). So the metric becomes:

{% math() %}
ds^2 = \frac{1}{\left(1 - \frac{R_s}{r}\right)} dr^2 + r^2 d\theta^2
{% end %}

Now, we want to compare this to the metric of our embedding space, which in our case is 3D Euclidean metric in cylindrical coordinates (we chose cylindrical because it was the only coordinate system that contained a $z$ coordinate that we'll need in embedding but also $r$ and $\theta$ that the Schwarzschild metric uses):

{% math() %}
ds^2 = dr^2 + r^2 d\theta^2 + dz^2 
{% end %}

If we rearrange the terms of the Euclidean metric, we get:

{% math() %}
ds^2 = dz^2 + dr^2 + r^2 d\theta^2
{% end %}

Comparing the similar terms in these two metrics, we can find that:

{% math() %}
dz^2 + dr^2 = \frac{1}{\left(1 - \frac{R_s}{r}\right)} dr^2
{% end %}

This is a differential equation we can solve for $z$. First, note that:

{% math() %}
dz^2 = \frac{1}{\left(1 - \frac{R_s}{r}\right)} dr^2 - dr^2
{% end %}

If we factor out $dr^2$, we get:

{% math() %}
dz^2 = dr^2 \left[\frac{1}{1 - \frac{R_s}{r}} -1\right]
{% end %}

Which means that:

{% math() %}
\left(\frac{dz}{dr}\right)^2 = \left[\frac{1}{1 - \frac{R_s}{r}} -1\right]
{% end %}

This simplifies to:

{% math() %}
\left(\frac{dz}{dr}\right)^2 = \frac{R_s}{r - R_s}
{% end %}

So:

{% math() %}
z(r, \theta) = \sqrt{R_s} \int \frac{1}{\sqrt{r - R_s}} dr = 2\sqrt{R_s} \sqrt{r - R_s}
{% end %}

An interactive 3D plot of this embedding diagram can be found at <https://demonstrations.wolfram.com/SchwarzschildSpaceTimeEmbeddingDiagram/>.

Note that the $z$ coordinate in the final embedding diagram has no physical meaning! It is only used as a convenient way for us to grasp the curvature of the space by embedding the 2D curvature into a higher dimension (in our case, 3D). Only the $r$ coordinate (which corresponds to $\sqrt{x^2 + y^2}$) and $\theta$ coordinate have a physical meaning.
