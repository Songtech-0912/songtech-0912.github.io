+++
title = "A guide to tensors"
date = 2024-02-12
draft = true
+++

Tensors are some of the most elegant ways to write the laws of physics, used extensively in relativistic mechanics and relativistic quantum theory. However, their use goes beyond advanced theoretical physics. So here is a guide to tensors that hopefully is more accessible and appeals to a broader audience.

<!-- more -->

## What is a tensor?

A tensor is a general name for a class of coordinate-independent objects. A scalar is a tensor, so is a vector, a matrix, and anything made of a combination of these. Whether we use spherical or cylindrical or cartesian coordinates, after all, the air temperature (a scalar field) doesn't change, the wind current velocity (a vector field) doesn't change, and the rotation of baseball hurtling towards me (a transformation matrix) also doesn't change. These are all examples of a general principle:

> The universe just doesn't care what coordinates we use to measure it. Coordinates are human constructs, not a fundamental fact of nature.

However, when we impose a coordinate system to write out the equations of physics, we fix the values of the components. So a vector might be the same physical thing regardless of coordinate system, but its _components_ are different in different coordinates. This can be an annoying issue: equations that might look simple in cartesian coordinates can grow monstrously annoying to read in, for instance, spherical coordinates. For example, this is Laplace's equation, often used for modelling gravity in a vacuum, in cartesian coordinates:

{% math() %}
\nabla^2 f = 0
{% end %}

And this is its equivalent in spherical coordinates:


{% math() %}
{\frac {1}{r^{2}}}{\frac {\partial }{\partial r}}\left(r^{2}{\frac {\partial f}{\partial r}}\right)+{\frac {1}{r^{2}\sin \theta }}{\frac {\partial }{\partial \theta }}\left(\sin \theta {\frac {\partial f}{\partial \theta }}\right)+{\frac {1}{r^{2}\sin ^{2}\theta }}{\frac {\partial ^{2}f}{\partial \varphi ^{2}}} = 0
{% end %}

With a change of coordinates, equations that looked elegant and easy to work with become clunky and untractable. What if there were a way to formulate physics in a way that doesn't depend on coordinates, and where we could use whichever coordinates we wished? This is where tensors come in. The tensor formulation of the same equation is given by:

{% math() %}
\delta^{ij} \partial_j \partial_i f = 0
{% end %}

How amazingly simple and graceful! _This_ is why we use tensors.

## Tensor algebra and calculus

To use tensors, it's helpful to start from our familiar vector and matrix formulas and build up from there.

For instance, consider a vector in Euclidean 3D space. Written in terms of a Cartesian basis, it is given by:

{% math() %}
\vec V = V_x \hat e_x + V_y \hat e_y + V_z \hat e_z
{% end %}

It is common convention when writing tensors to write the components of vectors with superscript (upstairs) indices and their basis vectors with subscript (downstairs) indices. The reason will become apparent later, consider this just a convention for now. So we can rewrite as:

{% math() %}
\vec V = V^x \hat e_x + V^y \hat e_y + V^z \hat e_z
{% end %}

If we set $x = 1, y = 2, z = 3$ we can equivalently write using _index_ notation:

{% math() %}
\vec V = V^1 \hat e_1 + V^2 \hat e_2 + V^3 \hat e_3 = \sum_{i = 1}^3 V^i \hat e_i
{% end %}

So a vector can be written in tensor form with:

{% math() %}
\hat V = \sum_{i = 1}^3 V^i \hat e_i
{% end %}

When writing tensors, it is common practice to omit the summation sign; as long as the reader is aware that you are using tensors and that the summation is there even if it's not written out, the conveyed meaning remains the same, but the notation becomes much more compact:

{% math() %}
\hat V = V^i \hat e_i
{% end %}

In a similar fashion, the dot product formula expressed using tensors can be written as:

{% math() %}
S = A^i B_i
{% end %}

And the matrix multiplication formula becomes:

{% math() %}
C_{ij} = A_{ik} B^k {}_j
{% end %}

To be able to discuss tensors further, however, we must introduce two concepts: that of a co-vector, and of the metric: 

{% math() %}V_j e^j{% end %}

Euclidean metric/kronecker delta: 

{% math() %}\delta_{ij}{% end %}

Dot product (euclidean, for all non-euclidean spaces replace $\delta_{ij}$ with the metric tensor):

{% math() %}
S = A^i e_i B^j e_j = \delta_{ij} A^i B^j = A^i B_i
{% end %}

(where for the last term we used the kronecker delta to lower an index, that is $\delta_{ij} B^j = B_i$)

Cross product:

{% math() %}
C^k = A_i B_j - A_j B_i
{% end %}

Gradient:

{% math() %}
\nabla F = \partial_\mu F
{% end %}

Curl:

{% math() %}
\nabla \times F = \partial_\nu V_\mu - \partial_\mu V_\nu
{% end %}

Relabelling ($j \to i$):
{% math() %}
\delta^i_j T^j = T^i
{% end %}

Where we use the fact that $\delta^i_j = \delta^{ik} \delta_{kj}$.

https://www.physicsforums.com/threads/what-is-einstein-notation-for-curl-and-divergence.511811/

## Maxwell's equations with tensors 

Let $A^\mu = (\phi, \mathbf{A})$ in units where $c = 1$, where $\phi$ is the electrical potential and $\mathbf{A}$ is the magnetic potential. Then:

{% math() %}
F^{\mu \nu} = \eta^{\mu a} \eta^{\nu b} F_{ab} = \eta^{\mu a} \eta^{\nu b} (\partial_a A_b - \partial_b A_a) = \partial^\mu A^\nu - \partial^\nu A^\mu
{% end %}

But since $\partial_\mu F^{\mu \nu} = \mu_0 J^\nu$, and given that second derivatives commute:

{% math() %}
\partial_\mu \partial^\mu A^\nu - \partial^\nu \partial_\mu A^\mu = \mu_0 J^\nu
{% end %}

If there are no sources, then we have **Maxwell's equations** written in one equation:

{% math() %}
\partial_\mu \partial^\mu A^\nu - \partial^\nu \partial_\mu A^\mu = 0
{% end %}

Here $\nu$ is the free index. Now note that $\partial_\mu \partial^\mu = -\partial_t^2 + \nabla^2$, $\partial^\nu = -\partial_t + \nabla$, and $\partial_\mu A^\mu = \partial_t \phi + \nabla \cdot \mathbf{A}$. If we substitute these in, we have:

{% math() %}
(-\partial^2_t \phi + \nabla^2 \phi) - (-\partial_t^2 \mathbf{A} + \nabla^2 \mathbf{A}) = 0
{% end %}

Or, if we use standard units instead of setting $c = 1$, we find we get the Maxwell equations written in potential form:

{% math() %}
\nabla^2 \phi - \frac{1}{c^2} \frac{\partial^2 \phi}{\partial t^2} = 0
{% end %}

{% math() %}
\nabla^2 \mathbf{A} - \frac{1}{c^2} \frac{\partial^2 \mathbf{A}}{\partial t^2} = 0
{% end %}

## Tensors and differential geometry

Differential geometry is primarily concerned with studying the characteristics of differentiable manifolds - non-Euclidean geometries that locally resemble flat Euclidean space. Tensors naturally lend themselves to differential geometry, because they are coordinate-invariant objects, which are very useful when describing coordinate systems on manifolds, where the basis vectors are non-constant.

## General relativity

In general relativity, the metric tensor also acquires a physical interpretation: it is a description of a spacetime in terms of how distances are measured within it.

### A final awesome and ridiculous example

We know that the Einstein Field Equations with zero cosmological constant is:

{% math() %}
R_{\mu \nu} - \frac{1}{2} R g_{\mu \nu} = \frac{8\pi G}{c^4} T_{\mu \nu}
{% end %}

Which can be rewritten as:

{% math() %}
R_{\mu \nu}\left(1 - \frac{1}{2} \delta^\mu {}_\lambda \delta^\nu {}_\gamma g^{\lambda \gamma} g_{\mu \nu}\right) = \frac{8\pi G}{c^4} T_{\mu \nu}
{% end %}

The goal is to express the Einstein Field Equations purely in terms of the metric and inverse metric. Note that this is equivalent to just the metric as:

{% math() %}
g^{\mu \nu} g_{\nu \lambda} = \delta^\mu {}_\lambda
{% end %}

The Ricci tensor is defined as:

{% math() %}
R_{\mu\nu}=\partial_\nu \Gamma_{\mu\lambda}^\lambda - \partial_\lambda \Gamma_{\mu\nu}^\lambda +\Gamma_{\mu\lambda}^\beta\Gamma_{\nu\beta}^\lambda-\Gamma_{\mu\nu}^\beta\Gamma_{\beta\lambda}^\lambda 
{% end %}

Using the Kronecker delta to relabel indices, we instead have:

{% math() %}
\Gamma_{\mu\lambda}^\beta\Gamma_{\nu\beta}^\lambda-\Gamma_{\mu\nu}^\beta\Gamma_{\beta\lambda}^\lambda 
{% end %}

{% math() %}
A_{\nu \beta \lambda} = A_{\lambda \nu \beta} \delta^\nu {}_m \delta^m {}_\lambda \delta^\beta {}_m \delta^m {}_\nu \delta^\lambda {}_m \delta^m {}_\beta
{% end %}

Resulting in:

{% math() %}
R_{\mu\nu}=\partial_\nu \Gamma_{\mu\lambda}^\lambda - \partial_\lambda \Gamma_{\mu\nu}^\lambda + \Gamma_{\mu\lambda}^\beta\Gamma_{\nu\beta}^\lambda (1 - \delta^\nu {}_m \delta^m {}_\lambda \delta^\beta {}_m \delta^m {}_\nu \delta^\lambda {}_m \delta^m {}_\beta)
{% end %}

Which reduces the terms to just three (technically). To go even more compact would sacrifice a bit of clarity, but it is technically possible to write:

{% math() %}
B_{\lambda \nu} = B_{\nu \lambda} \delta^\nu {}_m \delta^m {}_\lambda \delta^\lambda {}_m \delta^m {}_\nu
{% end %}

So one can write:

{% math() %}
R_{\mu\nu}=\partial_\nu \Gamma^\lambda_{\mu\lambda} (1 - \delta^\nu {}_m \delta^m {}_\lambda \delta^\lambda {}_m \delta^m {}_\nu) + \Gamma_{\mu\lambda}^\beta\Gamma_{\nu\beta}^\lambda (1 - \delta^\nu {}_m \delta^m {}_\lambda \delta^\beta {}_m \delta^m {}_\nu \delta^\lambda {}_m \delta^m {}_\beta)
{% end %}

And the connection coefficients (Christoffel symbols) are defined as:

{% math() %}
\Gamma^i_{jk} = \frac{1}{2} g^{i \lambda} \left(\partial_k g_{\lambda j} + \partial_j g_{\lambda k} - \partial_\lambda g_{j k} \right)
{% end %}

Resulting in:

{% math() %}
\begin{aligned}
R_{\mu\nu} = \frac{1}{2}\partial_\nu g^{\lambda m} &\left(\partial_\lambda g_{m \mu} + \partial_\mu g_{m \lambda} - \partial_m g_{\mu \lambda} \right) (1 - \delta^\nu {}_m \delta^m {}_\lambda \delta^\lambda {}_m \delta^m {}_\nu) \\
&+ \frac{1}{4} g^{\beta m} g^{\lambda m} \left(\partial_\lambda g_{m \mu} + \partial_\mu g_{m \lambda} - \partial_m g_{\mu \lambda} \right) \left(\partial_\beta g_{m \nu} + \partial_\nu g_{m \beta} - \partial_m g_{\nu \beta} \right) (1 - \delta^\nu {}_m \delta^m {}_\lambda \delta^\beta {}_m \delta^m {}_\nu \delta^\lambda {}_m \delta^m {}_\beta)
\end{aligned}
{% end %}

So it is _technically_ possible to write the EFEs relatively compactly using the power of Einstein  summation notation and tensor magic, using just 9 terms rather than the usual 18 or even 30+:

{% math() %}
\begin{aligned}
\left(1 - \frac{1}{2} \delta^\mu {}_\lambda \delta^\nu {}_\gamma g^{\lambda \gamma} g_{\mu \nu}\right)
&\Big(\frac{1}{2}\partial_\nu g^{\lambda m}
\left(\partial_\lambda g_{m \mu} + \partial_\mu g_{m \lambda} - \partial_m g_{\mu \lambda} \right) 
(1 - \delta^\nu {}_m \delta^m {}_\lambda \delta^\lambda {}_m \delta^m {}_\nu) \\ &+ 
\frac{1}{4} g^{\beta m} g^{\lambda m} 
\left(\partial_\lambda g_{m \mu} + \partial_\mu g_{m \lambda} - \partial_m g_{\mu \lambda} \right) 
\left(\partial_\beta g_{m \nu} + \partial_\nu g_{m \beta} - \partial_m g_{\nu \beta}\right) 
\left(1 - \delta^\nu {}_m \delta^m {}_\lambda \delta^\beta {}_m \delta^m {}_\nu \delta^\lambda {}_m \delta^m {}_\beta \right)\Big) = \frac{8\pi G}{c^4} T_{\mu \nu}
\end{aligned} 
{% end %}

This is even easier for the vacuum EFEs which reduce to just $R_{\mu \nu} = 0$, or:

{% math() %}
\begin{aligned}
\frac{1}{2}\partial_\nu g^{\lambda m} &\left(\partial_\lambda g_{m \mu} + \partial_\mu g_{m \lambda} - \partial_m g_{\mu \lambda} \right) (1 - \delta^\nu {}_m \delta^m {}_\lambda \delta^\lambda {}_m \delta^m {}_\nu) \\
&+ \frac{1}{4} g^{\beta m} g^{\lambda m} \left(\partial_\lambda g_{m \mu} + \partial_\mu g_{m \lambda} - \partial_m g_{\mu \lambda} \right) \left(\partial_\beta g_{m \nu} + \partial_\nu g_{m \beta} - \partial_m g_{\nu \beta} \right) (1 - \delta^\nu {}_m \delta^m {}_\lambda \delta^\beta {}_m \delta^m {}_\nu \delta^\lambda {}_m \delta^m {}_\beta) = 0
\end{aligned}
{% end %}

(note to self: change the kronecker delta to the metric tensor, the euclidean metric $\Delta_{ij}$ is no longer valid in curved spacetime)

However, that is not mentioning the _ungodly_ number of summation signs required to make it actually usable, or mention how technically it is 10 PDEs packaged into one using tensors...that is, as every physics textbook author would say, "an exercise left for the reader".