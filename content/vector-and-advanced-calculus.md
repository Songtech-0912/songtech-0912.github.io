+++
title = "Vector Calculus And Beyond"
date = 2026-01-14
+++

This guide covers the methods of calculus that go beyond multivariable calculus, including vector calculus, tensor calculus, the calculus of variations, and applications for each. In addition, derivations and more advanced treatments of topics in single- and multivariable calculus are also included.

<!-- more -->

I thank [Professor Jeffrey Banks](https://faculty.rpi.edu/jeffrey-banks) of RPI for giving his permission to share these notes.

## Overview of multivariable calculus

Vector calculus is based off analytic geometry (a fancy name for the mathematics of points, lines, surfaces, and vectors) and multivariable calculus - the calculus of functions of several variables. Such functions can be scalar-valued, meaning that they output a quantity that is a number (scalar), or vector-valued, meaning that they output a quantity that is a vector. We will start by going over the fundamentals of multivariable calculus. Note that a more beginner-friendly introductory treatment of multivariable calculus can be found in the dedicated [intro to multivariable calculus guide](@/multivariable-calculus/index.md).

### Vectors

A vector describes a directional quantity in space. For instance, the position vector $\mathbf{r} = \langle x, y, z\rangle$ describes, unsurprisingly, the position of a point from a chosen reference point, known as the origin. Vectors can be written in several forms. For instance, the position vector can be written with the bracket notation shown previously:

{% math() %}
\mathbf{r} = \langle x, y, z\rangle
{% end %}

It can also be written in row (horizontal) or column vector (vertical) form:

{% math() %}
\mathbf{r} = \begin{bmatrix}x & y & z\end{bmatrix}^T = \begin{bmatrix} x \\ y \\ z \end{bmatrix}
{% end %}

> $T$ here means "transpose", that is, flipping the row vector around to form a column vector.

Finally, vectors can be written in _linear combination form_, in which they are written in terms of a sum of special _basis vectors_:

{% math() %}
\mathbf{r} = x\begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix} + y\begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix} + z\begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}
{% end %}

In this expression, $\langle 1, 0, 0\rangle, \langle 0, 1, 0\rangle, \langle 0, 0, 1\rangle$ are the _basis vectors_, often alternatively written as $\mathbf{i}, \mathbf{j}, \mathbf{k}$. They allow us to _decompose_ the vector into a sum of its components, multiplied by each one of the basis vectors:

{% math() %}
\mathbf{r} = x \mathbf{i} + y \mathbf{j} + z \mathbf{k}
{% end %}

Here $x, y, z$ are called the _components_ of the position vector, and each represents a component of the position vector along each direction in 3D space. As another example, for the velocity vector $\mathbf{v} = \langle v_x, v_y, v_z\rangle$, we can write it as $\mathbf{v} = v_x \mathbf{i} + v_y \mathbf{j} + v_z \mathbf{k}$, and $v_x, v_y, v_z$ are the components of the velocity vector in each direction (for instance, $v_x$ is the x-component of the velocity vector).

> The Cartesian basis vectors $\mathbf{i}, \mathbf{j}, \mathbf{k}$ are often also written as $\hat x, \hat y, \hat z$ or $\hat e_x, \hat e_y, \hat e_z$. We will use these notations interchangeably.

The "length" of a vector is called its _magnitude_, written $\| \mathbf{v} \|$ or $|\mathbf{v}|$, and is found using the Pythagorean formula:

{% math() %}
\| \mathbf{v}\| = \sqrt{v_x^2 + v_y ^2 + v_z^2}
{% end %}

For a more general vector $\langle a, b, c \rangle$, the magnitude is found by summing the squared components of the vector:

{% math() %}
\|\langle a, b, c\rangle\| = \sqrt{a^2 + b^2 + c^2}
{% end %}

#### Vector arithmetic

Vectors are added and subtracted _component-wise_, which means you add or subtract each of their components:

{% math() %}
\begin{bmatrix} a_1\\ b_1\\ c_1 \end{bmatrix} + 
\begin{bmatrix} a_2\\ b_2\\ c_2 \end{bmatrix} =
\begin{bmatrix} a_1 + a_2\\ b_1 + b_2\\ c_1+c_2 \end{bmatrix} 
{% end %}

Vector multiplication is more complex. There are three different types of "vector multiplication" to speak of. The first type is **scalar multiplication**, when a vector is multiplied by a scalar. The resulting vector is formed by multiplying each of the vector's components:

{% math() %}
k \begin{bmatrix} a\\ b\\ c \end{bmatrix} =
\begin{bmatrix} k \cdot a\\ k \cdot b\\ k \cdot c \end{bmatrix}
{% end %}

#### Dot product of vectors

The **dot product**, or scalar product, is a product of two vectors (rather than a scalar and a vector). To take the dot product, we multiply the corresponding components of each of the two vectors, then add them together:

{% math() %}
\begin{bmatrix} a_1\\ b_1\\ c_1 \end{bmatrix} \cdot 
\begin{bmatrix} a_2\\ b_2\\ c_2 \end{bmatrix} =
a_1 a_2 + b_1b_2 + c_1 c_2
{% end %}

As the result is a scalar, we often call the dot product the _scalar product_. The dot product can also be expressed _geometrically_ in terms of the _angle_ between two vectors: for two vectors $\mathbf{u}$ and $\mathbf{v}$ that make an angle $\theta$, the dot product is given by:

{% math() %}
\mathbf{u} \cdot \mathbf{v} = |\mathbf{u}| |\mathbf{v}| \cos \theta
{% end %}

As a consequence, $\mathbf{u} \cdot \mathbf{v} = |\mathbf{u}| |\mathbf{v}|$ when $\theta = 0$, and $\mathbf{u} \cdot \mathbf{v} = 0$ when $\theta = 90 \degree$. In the latter case, we say that $\mathbf{u}$ and $\mathbf{v}$ are _orthogonal_ (perpendicular, i.e. 90 degrees apart). 

The dot product also has some useful mathematical properties. First, it is _commutative_ - {%  inlmath() %}\mathbf{u} \cdot \mathbf{v} = \mathbf{v} \cdot \mathbf{u}{% end %}. Second, it is _linear_ under scalar multiplication: {% inlmath() %}k (\mathbf{u} \cdot \mathbf{v}) = (k\mathbf{u}) \cdot \mathbf{v} = \mathbf{u} \cdot (k\mathbf{v}){% end %}. Third, the component of $\mathbf{u}$ in the direction of $\mathbf{v}$ can be expressed as {% inlmath() %}\mathbf{u} \cdot \mathbf{e}_v{% end %}, where {% inlmath() %}\mathbf{e}_v{% end %} is the unit vector in the direction of $\mathbf{v}$. Using this fact, we can define an operation known as the **vector projection** of $\mathbf{u}$ in the direction of $\mathbf{v}$, written {% inlmath() %}\operatorname{proj} \limits_{\mathbf{v}} \mathbf{u}{% end %}, which can be expressed as {% inlmath() %}\operatorname{proj} \limits_{\mathbf{v}} \mathbf{u} = (\mathbf{u} \cdot \mathbf{e}_v)\mathbf{e}_v{% end %}. The vector projection produces a vector parallel to $\mathbf{v}$ whose length is the component of $\mathbf{u}$ along $\mathbf{v}$.

#### Cross product of vectors

Similar to the dot product, we can define another type of vector-vector multiplication called the _cross product_. The cross product, written $\mathbf{u} \times \mathbf{v}$, results in a vector that is _perpendicular_ to both $\mathbf{u}$ and $\mathbf{v}$. In Cartesian coordinates ($xyz$ components) it can be computed using the formula:

{% math() %}
\mathbf{u}\times \mathbf{v} = (u_y v_z - u_z v_y) \mathbf{i} + (u_z v_x - u_x v_z)\mathbf{j} + (u_x v_y - u_y v_x) \mathbf{j}
{% end %}

The magnitude of the cross product between two vectors can be computed based on the angle between the two vectors, using the formula:

{% math() %}
| \mathbf{u} \times \mathbf{v} | = |\mathbf{u}||\mathbf{v}| \sin \theta
{% end %}

The cross product obeys the _anticommutative property_: $\mathbf{v} \times \mathbf{u} = -\mathbf{u} \times \mathbf{v}$. In addition, due to the angular formula, when $\theta = 0$, the cross product $|\mathbf{u} \times \mathbf{v}| = 0$, and when $\theta = 90 \degree$, the cross product $|\mathbf{u} \times \mathbf{v}| = |\mathbf{u}||\mathbf{v}|$.

### Multivariable functions

A **multivariable function** is a function that depends on several (i.e. more than one) variables. For instance, we may have a function that depends on the $(x, y)$ position in space, which we write $f(x, y)$. We may also have a function that depends on position and time, which we write $f(x, t)$. Notice how each of these functions depends on _more than one variable_. We may also have vector-valued multivariable functions in the form $\mathbf{F}(x, y, z)$. Such functions are the objects of study of multivariable calculus.

> Note: in the rest of this guide, for avoiding overly difficult-to-read equations, we will use the shorthand $f(\mathbf{r}) = f(x, y, z)$ and $\mathbf{F}(\mathbf{r}) = F_x(x, y, z) \mathbf{i} + F_y(x, y, z) \mathbf{j} + F_z(x, y, z) \mathbf{k}$. Note the boldface $\mathbf{r}$ represents $x, y, z$, and it is a shorthand, so please do not get this confused with $f(r)$ or $\mathbf{F}(r)$ which are single-variable functions.

### Parametric equations

We describe a wide variety of geometric objects in space with a _parametric equation_. There are many examples of parametric equations. The simplest types of parametric equations describe a curve in space, such as the trajectory of a particle. These are called **parametric curves** and follow the basic form:

{% math() %}
\begin{matrix}
x = x(t),& y= y(t),& z=z(t)
\end{matrix}
{% end %}

> We note that these equations are functions of $t$, called the _parameter_. $t$ does not have to be time - it can stand for any real number.

We may write parametric equations in this form in a more compact way as $\mathbf{r} = \mathbf{r}(t)$, which expands to the form shown above. The simplest example of a parametric curve is a **line**. A line takes the parametric form:

{% math() %}
\mathbf{r} = \mathbf{r}_0 + \mathbf{v} t
{% end %}

Where $\mathbf{r}_0$ is the starting point of the line, and $\mathbf{v}$ is the vector specifying the direction of the line. A line through two points $\mathbf{r}_0, \mathbf{r}_1$ takes the form:

{% math() %}
\mathbf{r} = \mathbf{r}_0 + (\mathbf{r}_1 - \mathbf{r}_0)t
{% end %}

More complex parametric curves can be arbitrary functions of $t$. The _length_ $S$ of a parametric curve defined by $\mathbf{r}(t) = \langle x(t), y(t), z(t)\rangle$ is found by the integral for the **arc length**:

{% math() %}
S = \int_a^b \sqrt{\left(\dfrac{dx}{dt}\right)^2 + \left(\dfrac{dy}{dt}\right)^2 + \left(\dfrac{dz}{dt}\right)^2} dt
{% end %}

Which can also be written as:

{% math() %}
S = \int_a^b \| \mathbf{r}'(t)\| dt
{% end %}

Where $\mathbf{r}'(t) = \left \langle \dfrac{dx}{dt}, \dfrac{dy}{dt}, \dfrac{dz}{dt}\right \rangle$ is the derivative along the path, and is always _tangent_ to the path. As a physical example, when we let $t$ be time, then $\mathbf{r}'(t)$ is the velocity vector. The velocity vector always points in the direction of motion, as it is tangent to the position vector.

### Planes and surfaces

In addition to lines and (parametric) curves, we may also define _planes_ in 3D space. A plane takes the form of an _implicit_ equation of $x$, $y$, and $z$:

{% math() %}
a(x - x_0) + b(y - y_0) + c(z - z_0) = 0
{% end %}

We may also write this in more compact form $\mathbf{n} \cdot (\mathbf{r} - \mathbf{r}_0) = 0$, where $\mathbf{r}_0$ is the point at the center of the plane, and $\mathbf{n} = \langle a, b, c\rangle$ is the normal vector - the vector that points out of the surface of the plane. Alternatively, we can write a plane in _parametric form_ with $\mathbf{r} = \mathbf{r}_0 + s \mathbf{v} + t\mathbf{w}$, where $\mathbf{v}, \mathbf{w}$ are two vectors spanning the surface of the plane and $s, t$ are two parameters, which are required to define the plane.

![A diagram showing the mathematical description of a plane, defined by a point where the plane is centered and a normal vector that points out of the surface of the plane](https://upload.wikimedia.org/wikipedia/commons/f/f9/Plane_equation_qtl3.svg)

_Source: [Wikipedia](https://commons.wikimedia.org/wiki/File:Plane_equation_qtl3.svg#/media/File:Plane_equation_qtl3.svg)_

We can also define other common geometric shapes. For instance, a sphere in 3D space of radius $R$ is defined by the implicit equation:

{% math() %}
x^2 + y^2 + z^2 = R^2
{% end %}

We can analyze more complex shapes in 3D space with _surfaces_. A _surface_ in 3D space is described by a function of $x$ and $y$ with the general form $z = f(x, y)$, which can also be written implicitly as $F(x, y, z) = 0$, where $F(x, y, z) = f(x, y) - z$. For instance, the equation of a paraboloid is:

{% math() %}
z = x^2 + y^2
{% end %}

> Note that implicit surfaces, which are in the form $F(x, y, z) = 0$, can also take more complex forms, where $F(x, y, z) = f(x, y) - g(z)$.

#### Intersections of surfaces

Just as we have _points_ of intersection in 2D space, we have _curves_ of intersection in 3D space. The **intersection of two surfaces** given by $F(x, y, z) = 0$ and $G(x, y, z) = 0$ is a parametric curve $\mathbf{r}(t)$. The precise form of this parametric curve may vary. But we will look at a simple case.

Consider the intersection between the unit sphere, given by $x^2 + y^2 + z^2 = 1$, and the plane $z = 2x$ (see [an interactive visualization here](https://www.math3d.org/K51UuVpjP4)). How would we solve this?

One way we can do so is by converting the plane to _parametric form_. To do so, we need to find two vectors that are parallel to the plane. Luckily, by using the visualization, this is relatively easy to find:

{% math() %}
\begin{matrix*}
\mathbf{u} = \begin{bmatrix} 1 \\ 0 \\ 2 \end{bmatrix}, 
& \mathbf{v} = \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix}
\end{matrix*}
{% end %}

From which can define the plane in parametric form as $\mathbf{r} = s\mathbf{u} + t\mathbf{v}$, which expands to:

{% math() %}
\begin{bmatrix} x \\ y \\ z\end{bmatrix} =
s\begin{bmatrix} 1 \\ 0 \\ 2 \end{bmatrix} + 
t\begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix}
{% end %}

Thus we have $x = s, y = t, z = 2s$. Now note that if we substitute these into the equation for the sphere, we have:

{% math() %}
\begin{align*}
x^2 + y^2 + z^2 &= s^2 + t^2 + (2s)^2 \\
&= s^2 + t^2 + 4s^2 \\
&= 5s^2 + t^2 \\
&= 1
\end{align*}
{% end %}

Thus, we may rearrange to find that:

{% math() %}
\begin{align*}
5s^2 + t^2 &= 1 \\
5s^2 &= 1 - t^2 \\
\end{align*}
{% end %}

It may seem that we have gotten nowhere. However, the appearance of an expression in the form $a^2 = 1 - b^2$ suggests a Pythagorean trigonometric substitution. For instance, if we were to try to define a new parameter $\lambda$ such that:

{% math() %}
s = \frac{1}{\sqrt{5}} \cos \lambda \\
t = \sin \lambda
{% end %}

Then indeed we have:

{% math() %}
\begin{align*}
5s^2 &= 5 \left(\frac{1}{\sqrt{5}} \cos \lambda\right)^2 \\
&= \cos^2 \lambda \\
&= 1 - \sin^2 \lambda \\
&= 1 - t^2
\end{align*}
{% end %}

Since we have $x = s, y = t, z = 2s$, we can now rewrite each in terms of $\lambda$:

{% math() %}
\begin{matrix*}
x=s & \Rightarrow & x = \dfrac{1}{\sqrt{5}} \cos \lambda \\
y=t & \Rightarrow & y = \sin \lambda \\
z=2s & \Rightarrow & z = \dfrac{2}{\sqrt{5}} \cos \lambda
\end{matrix*}
{% end %}

Thus the intersection between the unit sphere and the plane $z = 2x$ is given by the following parametric curve:

{% math() %}
\begin{matrix*}
\begin{align*}
x(t) &= \dfrac{1}{\sqrt{5}} \cos \lambda \\
y(t) &= \sin \lambda \\
z(t) &= \dfrac{2}{\sqrt{5}} \cos \lambda
\end{align*}
& \lambda \in [0, 2\pi]
\end{matrix*}
{% end %}

Which is a specific type of curve known as an **ellipse** that will frequently appear in multivariable and vector calculus.

### Curvilinear coordinate systems

Until this point, we have only discussed lines, curves, and surfaces in Cartesian 3D coordinates. Such coordinates are relatively simple to use and are well-suited for introducing the topics of multivariable calculus. However, we often want to use other coordinate systems, which are more suited to a particular mathematical problem. The two most common are **spherical coordinates** and **cylindrical coordinates**.

In cylindral coordinates, we describe a point 3D space using three coordinates - $\rho$ (radial distance), the distance from the z-axis, $\phi$ (polar angle), the angle between the point and the x-axis, and $z$ (elevation), the height of the point above the origin. Thus, the full set of coordinates describing a point takes the form $(\rho, \phi, z)$, as shown:

![An illustration of the cylindrical coordinate system, with three components, the radial (r) component pointing from the z-axis, the polar (theta) coordinate pointing from the x-axis, and the z coordinate pointing up from the origin](https://upload.wikimedia.org/wikipedia/commons/0/0e/Coord_system_CY_1.svg)

_Source: [Wikipedia](https://commons.wikimedia.org/wiki/File:Coord_system_CY_1.svg)_

> **Note on notation:** It is common to use different letters for cylindrical coordinates. We use $(\rho, \phi, z)$ but some authors use $(\rho, \theta, z)$ or $(r, \theta, z)$. In addition, it is also common to write $\phi$ as $\varphi$ (these are the same letter written differently). All of these symbol conventions are all equivalent, but it is important to specify _which_ notation convention is used and what direction each symbol is associated with to avoid confusion.

Cylindrical coordinates are useful in for situations when the mathematics of a problem have _cylindrical symmetry_, such as a tube or a circular loop.

Meanwhile, in spherical coordinates, we describe a point in 3D space also using three coordinates, but with slightly different coordinates. The first coordinate changes from $\rho$ to $r$ (still called radial), the distance from the origin (as opposed to the distance from the z-axis), the second coordinate becomes $\theta$ (azimuthal angle), the angle _above_ the plane of the origin, and the third coordinate is the same $\phi$ as before (polar angle). Therefore, the full set of coordinates describing a point becomes $(r, \theta, \phi)$, as shown in the diagram below:

![A diagram showing spherical coordinates, with a radial (r) coordinate pointing from the origin to the point, a polar angle (theta) pointing up from the plane of the origin, and an azimuthal angle (phi) pointing from the x-axis) pointing up from the plane, and a phi](https://upload.wikimedia.org/wikipedia/commons/f/f9/Kugelkoord-lokb-e.svg)

> **Note on notation:** Again, just as with cylindrical coordinates, the notation conventions for spherical coordinates are myriad, and all conventions are equivalent, but it is important to specify which one is used and the meaning of each symbol.

The XY plane in spherical coordinates is often called the **equatorial plane**, and the circle around the equatorial plane is called (unsurprisingly) the _equator_. Spherical coordinates are commonly-used for situations where the mathematics of a problem have _spherical symmetry_, such as a rotating ball or a planet.