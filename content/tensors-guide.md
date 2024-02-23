+++
title = "A guide to Tensors"
date = 2024-02-12
+++

Tensors are some of the most elegant ways to write the laws of physics, used extensively in relativistic mechanics and relativistic quantum theory. However, their use goes beyond advanced theoretical physics. So here is a guide to tensors that hopefully is more accessible and appeals to a broader audience.

<!-- more -->

## What is a tensor?

A tensor is a coordinate-independent object typically associated with a physical quantity. A scalar is a tensor, so is a vector, a matrix, and anything made of a combination of these. Whether we use spherical or cylindrical or cartesian coordinates, after all, the air temperature (a scalar field) doesn't change, the wind current velocity (a vector field) doesn't change, and the moment of inertia of a baseball hurtling towards me (a matrix) also doesn't change. These are all examples of a general principle:

> The universe just doesn't care what coordinates we use to measure it.

However, when we impose a coordinate system to write out the equations of physics, we fix the values of the components. So a vector might be the same physical thing regardless of coordinate system, but its _components_ are different in different coordinates. This can be an annoying issue: equations that might look simple in cartesian coordinates can grow monstrously annoying to read in, for instance, spherical coordinates. For example, this is Laplace's equation, often used for modelling gravity in a vacuum, in cartesian coordinates:

$$
\nabla^2 f = 0
$$

And this is its equivalent in spherical coordinates:


$$
{\frac {1}{r^{2}}}{\frac {\partial }{\partial r}}\left(r^{2}{\frac {\partial f}{\partial r}}\right)+{\frac {1}{r^{2}\sin \theta }}{\frac {\partial }{\partial \theta }}\left(\sin \theta {\frac {\partial f}{\partial \theta }}\right)+{\frac {1}{r^{2}\sin ^{2}\theta }}{\frac {\partial ^{2}f}{\partial \varphi ^{2}}} = 0
$$

With a change of coordinates, equations that looked elegant and easy to work with become clunky and untractable. What if there were a way to formulate physics in a way that doesn't depend on coordinates, and where we could use whichever coordinates we wished? This is why we use tensors.

## Tensor algebra and calculus

Vector: 

$$V^i e_i$$

Co-vector: 

$$V_j e^j$$

Euclidean metric/kronecker delta: 

$$\delta_{ij}$$

Dot product (euclidean, for all non-euclidean spaces replace $\delta_{ij}$ with the metric tensor):

$$
S = A^i e_i B^j e_j = \delta_{ij} A^i B^j = A^i B_i
$$

(where for the last term we used the kronecker delta to lower an index, that is $\delta_{ij} B^j = B_i$)

Cross product:

$$
C^k = A_i B_j - A_j B_i
$$
Gradient:

$$
\nabla F = \partial_\mu F
$$

Curl:

$$
\nabla \times F = \partial_\nu V_\mu - \partial_\mu V_\nu
$$
Relabelling ($j \to i$):
$$
\delta^i_j T^j = T^i
$$
Where we use the fact that $\delta^i_j = \delta^{ik} \delta_{kj}$.

Matmul:

$$
C_{ij} = A_{ik} B_{kj}
$$

https://www.physicsforums.com/threads/what-is-einstein-notation-for-curl-and-divergence.511811/

## Maxwell's equations with tensors 

Let $A^\mu = (\phi, \mathbf{A})$ in units where $c = 1$, where $\phi$ is the electrical potential and $\mathbf{A}$ is the magnetic potential. Then:

$$
F^{\mu \nu} = \eta^{\mu a} \eta^{\nu b} F_{ab} = \eta^{\mu a} \eta^{\nu b} (\partial_a A_b - \partial_b A_a) = \partial^\mu A^\nu - \partial^\nu A^\mu
$$

But since $\partial_\mu F^{\mu \nu} = \mu_0 J^\nu$, and given that second derivatives commute:

$$
\partial_\mu \partial^\mu A^\nu - \partial^\nu \partial_\mu A^\mu = \mu_0 J^\nu
$$

If there are no sources, then we have **Maxwell's equations** written in one equation:

$$
\partial_\mu \partial^\mu A^\nu - \partial^\nu \partial_\mu A^\mu = 0
$$

Here $\nu$ is the free index. Now note that $\partial_\mu \partial^\mu = -\partial_t^2 + \nabla^2$, $\partial^\nu = -\partial_t + \nabla$, and $\partial_\mu A^\mu = \partial_t \phi + \nabla \cdot \mathbf{A}$. If we substitute these in, we have:

$$
(-\partial^2_t \phi + \nabla^2 \phi) - (-\partial_t^2 \mathbf{A} + \nabla^2 \mathbf{A}) = 0
$$

Or, if we use standard units instead of setting $c = 1$, we find we get the Maxwell equations written in potential form:

$$
\nabla^2 \phi - \frac{1}{c^2} \frac{\partial^2 \phi}{\partial t^2} = 0
$$

$$
\nabla^2 \mathbf{A} - \frac{1}{c^2} \frac{\partial^2 \mathbf{A}}{\partial t^2} = 0
$$

## Tensors and differential geometry

Differential geometry is primarily concerned with studying the characteristics of differentiable manifolds - non-Euclidean geometries that locally resemble flat Euclidean space. Tensors naturally lend themselves to differential geometry, because they are coordinate-invariant objects, which are very useful when describing coordinate systems on manifolds, where the basis vectors are non-constant.
