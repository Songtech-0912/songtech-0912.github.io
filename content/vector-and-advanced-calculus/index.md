+++
title = "Vector Calculus and Beyond"
date = 2025-01-14
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

One way we can do so is by converting the plane to _parametric form_. To do so, we need to find two vectors that are parallel to the plane.

{{ wideimg(
	src="intersection-of-surfaces.png",
	desc="An illustration of the plane z = 2x as well as two vectors parallel to the plane and lying on the plane"
)
}}

Luckily, this is relatively easy to find (see the above picture for a visualization):

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

{{ natural_img(src="https://upload.wikimedia.org/wikipedia/commons/0/0e/Coord_system_CY_1.svg",
desc="An illustration of the cylindrical coordinate system, with three components, the radial (r) component pointing from the z-axis, the polar (theta) coordinate pointing from the x-axis, and the z coordinate pointing up from the origin"
) }}

_Source: [Wikipedia](https://commons.wikimedia.org/wiki/File:Coord_system_CY_1.svg)_

> **Note on notation:** It is common to use different letters for cylindrical coordinates. We use $(\rho, \phi, z)$ but some authors use $(\rho, \theta, z)$ or $(r, \theta, z)$. In addition, it is also common to write $\phi$ as $\varphi$ (these are the same letter written differently). All of these symbol conventions are all equivalent, but it is important to specify _which_ notation convention is used and what direction each symbol is associated with to avoid confusion.

Cylindrical coordinates are useful in for situations when the mathematics of a problem have _cylindrical symmetry_, such as a tube or a circular loop.

Meanwhile, in spherical coordinates, we describe a point in 3D space also using three coordinates, but with slightly different coordinates. The first coordinate changes from $\rho$ to $r$ (still called radial), the distance from the origin (as opposed to the distance from the z-axis), the second coordinate becomes $\theta$ (azimuthal angle), the angle _above_ the plane of the origin, and the third coordinate is the same $\phi$ as before (polar angle). Therefore, the full set of coordinates describing a point becomes $(r, \theta, \phi)$, as shown in the diagram below:

{{ natural_img(
  src="https://upload.wikimedia.org/wikipedia/commons/f/f9/Kugelkoord-lokb-e.svg",
  desc="A diagram showing spherical coordinates, with a radial (r) coordinate pointing from the origin to the point, a polar angle (theta) pointing up from the plane of the origin, and an azimuthal angle (phi) pointing from the x-axis) pointing up from the plane, and a phi"
) }}

> **Note on notation:** Again, just as with cylindrical coordinates, the notation conventions for spherical coordinates are myriad, and all conventions are equivalent, but it is important to specify which one is used and the meaning of each symbol.

The XY plane in spherical coordinates is often called the **equatorial plane**, and the circle around the equatorial plane is called (unsurprisingly) the _equator_. Spherical coordinates are commonly-used for situations where the mathematics of a problem have _spherical symmetry_, such as a rotating ball or a planet.

### Coordinate conversions and arc length in curvilinear coordinate systems

Recall that previously, we discussed two curvilinear coordinate systems: cylindrical $(\rho, \phi, z)$ coordinates and spherical $(r, \theta, \phi)$ coordinates. We will now explore how we may express points and geometric objects we are familiar with in Cartesian coordinates in these curvilinear coordinate systems.

First, we will go over **cylindrical coordinates**. We may convert $(\rho, \phi, z)$ coordinates to Cartesian $(x, y, z)$ coordinates as follows:

{% math() %}
\begin{align*}
x &= \rho \cos \phi \\
y &= \rho \sin \phi \\
z &= z
\end{align*}
{% end %}

By using this information, we may write out the basis vectors of cylindrical coordinates in terms of Cartesian coordinates:

{% math() %}
\begin{align*}
\hat e_\rho &= \cos \phi\, \mathbf{i} - \sin \phi\, \mathbf{j} \\
\hat e_\phi &= -\sin \phi\, \mathbf{i} + \cos \phi\, \mathbf{j} \\
\hat e_z &= \mathbf{k}
\end{align*}
{% end %}

A parametric curve in cylindrical coordinates can be represented as follows:

{% math() %}
\mathbf{r}(t) = \rho(t) \hat e_\rho + z(t) \hat e_z
{% end %}

There is only one problem here - the unit vectors in cylindrical coordinates (and in general, basically all non-Cartesian coordinate systems) are **non-constant**. Here, $\hat e_\rho = \hat e_\rho(\phi(t))$, that is, the cylindrical radial unit vector depends on the angle $\phi$.

You may be interested in _how_ these formulas are derived. The mathematical justification of these formulas is rather complex and time-consuming and is the domain of a field known as _differential geometry_; see [this wikipedia article](https://en.wikipedia.org/wiki/Metric_tensor#Coordinate_transformations) for those interested. For now, we will accept these formulas as fact to be able to continue our analysis.

Let us take the example of using coordinate-transformed basis vectors to to convert vector-valued equations in Cartesian coordinates to cylindrical and spherical coordinates. An example is the question of how to measure _distances_ and _positions_ in space. Let us consider a parametric curve $\mathbf{r}(s)$ (we use $s$ as a general parameter, it doesn't have to be time). In Cartesian coordinates, we would write out the curve as a vector, in the form:

{% math() %}
\mathbf{r}(s) = x(s) \,\mathbf{i} + y(s)\, \mathbf{j} + z(s)\,\mathbf{k}
{% end %}

Therefore, the **length element** $d\mathbf{r}$, a tiny segment of the curve $\mathbf{r}(s)$ which represents an infinitesimal displacement in space, is given by:

{% math() %}
\mathbf{r}(s) = dx \,\mathbf{i} + dy\, \mathbf{j} + dz\,\mathbf{k}
{% end %}

> **Note:** It is important to remember that $dx = x'(s) ds, dy = y'(s) dy$, and $dz = z'(s) dz$. We have just not written them in fully-expanded form for brevity.

The distance along the infinitesimal displacement vector $d\mathbf{r}$ is given by $\|d\mathbf{r}\|$, from which we can find the familiar expression for the arc length in Cartesian coordinates:

$$
S = \int \|d\mathbf{r}\| = \int_a^b \sqrt{\left(\dfrac{dx}{ds}\right)^2 + \left(\dfrac{dy}{ds}\right)^2 + \left(\dfrac{dz}{ds}\right)^2}\, ds
$$

where $d\mathbf{r}$ is the length element - a tiny segment of the curve $\mathbf{r}(s)$, and $\|d\mathbf{r}\|$ is its magnitude (which, as we stated, represents the distance of a tiny segment of the curve in a physical setting). In physics, a common parameter to use is $t$, so $\mathbf{r} = \mathbf{r}(t)$ and $ds = dt$. However, mathematically-speaking, $s$ can be an arbitrary parameter that parametrizes a path $\mathbf{r}(s)$.

To compute the arc length in cylindrical coordinates we must first write out the length element $d\mathbf{r}$ of a curve in cylindrical form. This is given by:

{% math() %}
d\mathbf{r} = \dfrac{dr}{ds}\hat e_r + r\dfrac{d\theta}{ds} \hat e_\theta + \dfrac{dz}{ds} \hat e_z
{% end %}

> **Note:** here we use the notation $(r, \theta, z)$ rather than $(\rho, \theta, z)$, but both are completely equivalent; it is just a different notational choice.

The arc length is found by _integrating_ over the absolute value (magnitude) line element, the **arc length in cylindrical coordinates** is given by:

{% math() %}
\begin{align*}
S &= \int_a^b \|d\mathbf{r}\| \\
&= \int_a^b \sqrt{\left(\dfrac{dr}{ds}\right)^2 + \left(r \dfrac{d\theta}{ds}\right)^2 + \left(\dfrac{dz}{ds}\right)^2}ds
\end{align*}
{% end %}

We may now consider **spherical coordinates**. However, we must first must mention an important fact. There exist two major coordinate conventions for spherical coordinates. In the **physicists' convention**, $(r, \theta, \phi)$, $\theta$ is the angle of elevation (angle _above_ the XY plane) and $\phi$ is the polar angle (angle _around_ the XY plane). In the **mathematicians' convention** the latter two angles are switched around, where $\theta$ is the polar angle and $\phi$ is the angle of elevation. This can be a matter of immense confusion. Therefore, we will provide each of the following results in both conventions.

In the *mathematicians' convention*, the conversions from spherical to Cartesian coordinates are as follows:

{% math() %}
\begin{align*}
x &= r \sin \phi \cos \theta \\
y &= r \sin \phi \sin \theta \\
z &= r \cos \phi
\end{align*}
{% end %}

While in the *physicist's convention*, the conversions are as follows:

{% math() %}
\begin{align*}
x &= r \sin \theta \cos \phi \\
y &= r \sin \theta \sin \phi \\
z &= r \cos \theta
\end{align*}
{% end %}

A parametric curve in spherical coordinates can be represented as follows:

{% math() %}
\mathbf{r}(t) = r(t) \hat e_r
{% end %}

This parametric equation is deceptively simple: once again, the unit vectors are _non-constant_, which means that $\hat e_r = \hat e_r(\theta(t), \phi(t))$. It must be emphasized: in general, basis vectors **are not constant**. In the case of spherical coordinates, the spherical basis vectors in the _mathematician's convention_ are given by:

{% math() %}
\begin{align*}
\hat e_r &= \cos \theta \sin \phi \hat i + \sin \theta \sin \phi \hat j + \cos \phi \hat k \\
\hat e_\theta &= -\sin \theta \hat i + \cos \theta \hat j \\
\hat e_\phi &= \cos \theta \cos \phi \hat i + \sin \theta \cos \phi \hat j - \sin \phi \hat k
\end{align*}
{% end %}

While in the *physicist's* convention they are given by:

{% math() %}
\begin{align*}
\hat e_r &= \cos \phi \sin \theta \hat i + \sin \phi \sin \theta \hat j + \cos \theta \hat k \\
\hat e_\theta &= \cos \phi \cos \theta \hat i + \sin \phi \cos \theta \hat j - \sin \theta \hat k \\
\hat e_\phi &= -\sin \phi \hat i + \cos \phi \hat j 
\end{align*}
{% end %}

We may therefore write out the line element in the spherical coordinates as:

{% math() %}
\begin{matrix*}
d\mathbf{r} = dr\, \hat r + r d\theta\, \hat \theta + r\sin \theta d\phi\, \hat \phi,
&\text{(physics convention)} \\
d\mathbf{r} = dr\, \hat r + r d\phi\, \hat \phi + r\sin \phi d\theta\, \hat \theta,
&\text{(math convention)}
\end{matrix*}
{% end %}

Therefore, on integrating the line element, the **arc length in spherical coordinates** becomes (in the _mathematician's_ convention):

{% math() %}
S = \int_a^b \sqrt{\left({\dfrac{dr}{ds}}\right)^2 + \left(r \sin \phi\dfrac{d\theta}{ds}\right)^2 + \left(r \dfrac{d\phi}{ds}\right)^2} \, ds
{% end %}

In the _physicist's_ convention we have a very similar formula, just with $\theta$ and $\phi$ switched:

{% math() %}
S = \int_a^b \sqrt{\left({\dfrac{dr}{ds}}\right)^2 + \left(r \sin \theta \dfrac{d\phi}{ds}\right)^2 + \left(r \dfrac{d\theta}{ds}\right)^2} \, ds
{% end %}

### Review of differentiation in several variables

From multivariable calculus, we recall that a partial derivative is defined as _the rate of change of a function in a particular direction_. For instance, consider a function of two variables $f(x, y)$. The partial derivative of $f$ along the $x$-direction (equivalently called _partial derivative with respect to $x$) is written $\dfrac{\partial f}{\partial x}$. It is the limit of the change $\dfrac{\Delta f}{\Delta x}$ as $\Delta x$ approaches zero. We may write this formally as:

{% math() %}
\dfrac{\partial f}{\partial x} = \lim \limits_{\Delta x \to 0}\dfrac{f(x + \Delta x, y) - f(x, y)}{\Delta x}
{% end %}

By the same approach, we may write the partial derivative of $f$ along the $y$-direction (e) as $\dfrac{\partial f}{\partial y}$, where:

{% math() %}
\dfrac{\partial f}{\partial y} = \lim \limits_{\Delta x \to 0}\dfrac{f(x, y + \Delta y) - f(x, y)}{\Delta y}
{% end %}

> It is also common to call these partial derivatives in a slightly different (but mathematically-equivalent) fashion as the _partial derivative with respect to $x$_ and _partial derivative with respect to $y$_. For a more compact name, it is common to use the abbreviation "w.r.t" (short for _with respect to_) such that we may say _partial derivative w.r.t. $x$_ and _partial derivative w.r.t $y$_.

The collection of all partial derivatives of a function in a single vector is known as the **gradient** $\nabla f$, which can be thought of as the partial derivative vector. In our case it is given by:

{% math() %}
\nabla f = \left \langle \dfrac{\partial f}{\partial x}, \dfrac{\partial f}{\partial y}\right\rangle
{% end %}

Partial derivatives follow very similar rules as ordinary derivatives. In particular, the sum, difference, product, and quotient rules are _the same_ for partial derivatives, just with ordinary derivatives replaced by partial derivatives:

| Derivative rule | Expression for partial derivatives                                                                                                                               |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Sum rule        | $\dfrac{\partial}{\partial x}[f(\mathbf{r}) + g(\mathbf{r})] = \dfrac{\partial f}{\partial x} + \dfrac{\partial f}{\partial x}$                                  |
| Difference rule | $\dfrac{\partial}{\partial x}[f(\mathbf{r}) - g(\mathbf{r})] = \dfrac{\partial f}{\partial x} - \dfrac{\partial f}{\partial x}$                                  |
| Product rule    | $\dfrac{\partial}{\partial x}[f(\mathbf{r}) g(\mathbf{r})] = f\dfrac{\partial g}{\partial x} + g\dfrac{\partial f}{\partial x}$                                  |
| Quotient rule   | $\dfrac{\partial}{\partial x}\left[\dfrac{f(\mathbf{r})}{g(\mathbf{r})}\right] = \dfrac{f\dfrac{\partial g}{\partial x} - g\dfrac{\partial f}{\partial x}}{g^2}$ |

Note, however, that the _chain rule_ is not the same for multivariable functions. For a function $f(\mathbf{r(t)}) = f(x(t), y(t), z(t))$, the chain rule for $f$ reads:

{% math() %}
\dfrac{df}{dt} = \dfrac{\partial f}{\partial x} \dfrac{dx}{dt} + \dfrac{\partial f}{\partial y} \dfrac{dy}{dt} + \dfrac{\partial f}{\partial z} \dfrac{dz}{dt}
{% end %}

Which can also be written as $\dfrac{\partial f}{\partial x} = \nabla f \cdot \mathbf{r}'(t)$. Meanwhile, for a function $f(u(\mathbf{r}), v(\mathbf{r}))$ where $u(\mathbf{r}) = u(x, y, z)$ and $v(\mathbf{r}) = v(x, y, z)$ are themselves multivariable functions, the chain rule for $f$ reads:

{% math() %}
\begin{align*}
\dfrac{\partial f}{\partial x} &= \dfrac{\partial f}{\partial u} \dfrac{\partial u}{\partial x} + \dfrac{\partial f}{\partial v} \dfrac{\partial v}{\partial x} \\
\dfrac{\partial f}{\partial y} &= \dfrac{\partial f}{\partial u} \dfrac{\partial u}{\partial y} + \dfrac{\partial f}{\partial v} \dfrac{\partial v}{\partial y} \\
\dfrac{\partial f}{\partial z} &= \dfrac{\partial f}{\partial u} \dfrac{\partial u}{\partial z} + \dfrac{\partial f}{\partial v} \dfrac{\partial v}{\partial z}
\end{align*}
{% end %}

> **Intuition builder:** The multivariable chain rule can thought of as "tree" where one function "branches" into all the functions that depend on it, and you need to "traverse the tree" to collect all the partial derivatives to find the total rate of change.

In the general case for a scalar-valued function $f(u_1, u_2, \dots, u_n)$ that has a dependence on some variables $x_1, x_2, \dots, x_n$, we have:

{% math() %}
\dfrac{\partial f}{\partial x_j} = \sum_i \dfrac{\partial f}{\partial u_i} \dfrac{\partial u_i}{\partial x_j}
{% end %}

The **total derivative** measures the rate of change of a function of several variables with respect to _every direction_ - it is very similar to _implicit differentiation_ in single-variable calculus, but for multivariable calculus instead. Unlike a partial derivative, it is written $\dfrac{df}{ds}$ or $\dfrac{df}{dt}$. It comes from the application of the chain rule to every variable. For instance, consider a function of the form $f(x(t), y(x(t)))$. The total derivative of the function with respect to $t$ would be the equivalent of applying the chain rule to differentiate every variable dependent on $t$:

{% math() %}
\dfrac{df}{dt} = \dfrac{\partial f}{\partial x} \dfrac{dx}{dt} + \dfrac{\partial f}{\partial y} \dfrac{dy}{dx} \dfrac{dx}{dt}
{% end %}

### Tangent planes

Consider a surface defined by the implicit equation $F(x, y, z) = 0$, or alternatively, $f(x, y) - z = 0$. We may _locally approximate_ the surface at a point $(a, b)$ with a **tangent plane**, which is a generalization of a tangent line in single-variable calculus. A tangent plane is the surface defined as:

{% math() %}
z = \dfrac{\partial f}{\partial x}(x - a) + \dfrac{\partial f}{\partial y}(x - b)
{% end %}

Note that a tangent plane does not _always_ exist. First, while it may be somewhat obvious, a tangent plane at a point exists only if that point is actually **on** the surface - otherwise a tangent plane is not defined. Mathematically speaking, this means that the surface must be _continuous_ at $(x_0, y_0, z_0)$.

But continuity is not the only requirement - we also need _differentiability_. Differentiability implies continuity, but continuity is not enough for differentiability. For a surface $z = f(x, y)$, it is a **requirement for the existence of a tangent plane at $(x_0, y_0)$** that $\dfrac{\partial f}{\partial x}$ and $\dfrac{\partial f}{\partial y}$ exist **and** are well-defined (i.e. continuous) at $(x_0, y_0)$. For $f(x, y)$ to be differentiable at $(x_0, y_0)$ is _not_ a sufficient condition.

Tangent planes are one specific case of a far more general class of linear approximations in $n$ dimensions. In $n$ dimensions, the linear approximation to a function $f(\mathbf{r})$ is given by:

{% math() %}
L(\mathbf{r}) = f(\mathbf{r}_0) + \nabla f(\mathbf{r}_0) \cdot (\mathbf{r} - \mathbf{r}_0)
{% end %}

The equivalent expression for the linear approximation for a vector-valued function $\mathbf{F}(\mathbf{r})$ is given as follows:

{% math() %}
\mathbf{L}(\mathbf{r}) = \mathbf{F}(\mathbf{r}_0) + D[\mathbf{F}(\mathbf{r}_0)]\cdot (\mathbf{r} - \mathbf{r}_0)
{% end %}

Where $D$ is the **Jacobian**, given by:

{% math() %}
D = 
\begin{bmatrix}
\nabla F_x \\ \nabla F_y \\ \nabla F_z \\ \vdots \\\nabla F_i
\end{bmatrix}
=
\begin{bmatrix}
\dfrac{\partial F_x}{\partial x} & \dfrac{\partial F_x}{\partial y} & \dfrac{\partial F_x}{\partial z} & \dots & \\
\dfrac{\partial F_y}{\partial x} & \dfrac{\partial F_y}{\partial y} & \dfrac{\partial F_y}{\partial z} & \dots & \\
\dfrac{\partial F_z}{\partial x} & \dfrac{\partial F_z}{\partial y} & \dfrac{\partial F_z}{\partial z} & \dots & \\
\vdots & \vdots & \vdots & \ddots \\
\dfrac{\partial F_i}{\partial x} & \dfrac{\partial F_i}{\partial y} & \dfrac{\partial F_i}{\partial z} &\dots
\end{bmatrix}
{% end %}

The Jacobian can also be used to write out the less-commonly-used  **vector chain rule**. For a given vector-valued function $\mathbf{F}(\mathbf{f}(\mathbf{r}))$ where $\mathbf{F} = \langle F_1(\mathbf{f}), F_2(\mathbf{f}), F_3(\mathbf{f}), \dots, F_p(\mathbf{f}) \rangle$ (i.e. $\mathbf{F}$ has $p$ components) and $\mathbf{f} = \langle f_1(\mathbf{r}), f_2(\mathbf{r}), f_3(\mathbf{r}), \dots, f_m(\mathbf{r})\rangle$ (i.e. $\mathbf{f}$ has $m$ components) and $\mathbf{r} = \langle x_1, x_2, x_3, \dots, x_n\rangle$ (i.e. $\mathbf{r}$ has $n$ components), then the vector chain rule reads:

{% math() %}
D_{\vec{\mathbf{r}}}[\mathbf{F}] = D_{\vec{\mathbf{f}}}[\mathbf{F}] D_{\vec{\mathbf{r}}}[\mathbf{f}]
{% end %}

Or, in full matrix form:

{% math() %}
% 1st matrix
\underbrace{
\begin{bmatrix}
\dfrac{\partial F_1}{\partial x_1} & \dfrac{\partial F_1}{\partial x_2} & \dots \\ 
\dfrac{\partial F_2}{\partial x_1} & \dfrac{\partial F_2}{\partial x_2} & \dots \\
\vdots & \vdots & \ddots
\end{bmatrix}}_{(p \times n) \text{ Jacobian matrix}}
=
% 2nd matrix
\underbrace{
\begin{bmatrix}
\dfrac{\partial F_1}{\partial f_1} & \dfrac{\partial F_1}{\partial f_2} & \dots \\ 
\dfrac{\partial F_2}{\partial f_1} & \dfrac{\partial F_2}{\partial f_2} & \dots \\
\vdots & \vdots & \ddots
\end{bmatrix}}_{(p \times m) \text{ Jacobian matrix}}
% 3rd matrix
\underbrace{
\begin{bmatrix}
\dfrac{\partial f_1}{\partial x_1} & \dfrac{\partial f_1}{\partial x_2} & \dots \\ 
\dfrac{\partial f_2}{\partial x_1} & \dfrac{\partial f_2}{\partial x_2} & \dots \\
\vdots & \vdots & \ddots
\end{bmatrix}}_{(m \times n) \text{ Jacobian matrix}}
{% end %}

### Directional rate of change

We have seen that the _partial derivatives_ of a function of several variables $f(x, y, z)$ measures its rate of change along different directions. But what is the rate of change of $f$ in an _arbitrary_ direction, denoted by $\mathbf{v}$? The answer is given by the **directional derivative**. The directional derivative is written as $\nabla_{\vec{\mathbf{v}}} f$ and is given as follows:

{% math() %}
\nabla_{\vec{\mathbf{v}}} f = \nabla f \cdot \mathbf{v}
{% end %}

But we recall that the dot product is maximized when two vectors are parallel to each other. Thus, the directional deriative - the rate of change of $f$ in direction $\mathbf{v}$ - is in fact _maximized in the direction of the gradient_. That is to say, **the gradient points in the direction of greatest increase** of the function. More precisely, the maximum _rate_ of increase is given by:

{% math() %}
\mathbf{v}_\text{max.} = \dfrac{\nabla f}{|\nabla f|}
{% end %}

And the minimum _rate_ of increase is exactly opposite in direction to the maximum rate of increase (no surprise!) and is given by:

{% math() %}
\mathbf{v}_\text{min.} = -\mathbf{v}_\text{max.} = -\dfrac{\nabla f}{|\nabla f|}
{% end %}

But what about a vector $\mathbf{v} = \mathbf{r}'(t)$ that is _perpendicular_ to the gradient? Well, then, since we know that the dot product is _zero_ when two vectors are perpendicular, then the directional derivative goes to zero:

{% math() %}
\begin{matrix*}
\mathbf{v} \perp \nabla f & \Rightarrow &\nabla_{\vec{\mathbf{v}}} f = \nabla f \cdot \mathbf{v} = 0
\end{matrix*}
{% end %}

By the chain rule, since we have $\mathbf{v} = \mathbf{r}'(t)$, then if we take the _total derivative_ of $f$ with respect to $t$, we can write the same result in a slightly different way:

{% math() %}
\dfrac{df}{dt} = \nabla f \cdot \dfrac{d\mathbf{r}}{dt} = 0
{% end %}

Thus, $f$ takes a _constant value_ along any curve $\mathbf{r}(t)$ which is _perpendicular to the gradient_ (that is, $\mathbf{r}'(t) \perp \nabla f$). These special curves are called **level curves**. Each level curve is defined by the equation $f(\mathbf{r}) = C$ where $C$ is some constant value of $f$. Level curves are a type of **level set**, which we will examine in more depth.

### Level sets

When we are analyzing functions of several variables, we are often interested in points for which the function takes a _constant_ value. If a surface is described by the function $z = f(x, y)$, a level curve is an implicit curve given by $f(x, y) = c$, where $c$ is a constant. Geometrically, i, level curves can be thought of as "slices" to the surface at constant spacings, as shown (in the red solid lines) on the below plot:

{{ natural_img(
src="level-sets-external.png",
desc="A plot of several level curves on a surface, which trace out points along the surface of constant height"
) }}

_Source: [Mathematica Stack Exchange](https://mathematica.stackexchange.com/questions/36837/how-do-you-plot-level-curves-describing-a-3d-surface-on-the-x-y-plane)_

We may use level sets to derive the equations of a tangent plane. To illustrate this process, consider an explicit surface in the form $z = f(x, y)$ - for instance, $f(x, y) = x^2 + y^2$ (this is in fact the equation of a paraboloid). The level curves of $f(x, y)$ are the curves for which $f(x, y)$ takes a constant value, and can be parametrized as $f(x, y) = c$ (equivalently, $f(\mathbf{r}(t)) = c$), where  is a constant. 

We know that since $f(\mathbf{r}(t)) = f(x, y) = c$ is a _level curve_, then $\dfrac{df}{dt} = 0$ (because level curves are where $f(x, y)$ are equal to a constant, and the derivative of a constant is zero). By the chain rule, we may expand $\dfrac{df}{dt}$ as follows:

{% math() %}
\dfrac{df}{dt} = \nabla f \cdot \dfrac{d\mathbf{r}}{dt} = 0
{% end %}

Since $\dfrac{d\mathbf{r}}{dt}$ is _tangent_ to the level curve $\mathbf{r}(t)$, $\nabla f$ must therefore be **normal** to the level curve for the dot product to become zero (since the dot product is only zero for orthogonal vectors). But recall that the linear approximation equation is $\mathbf{n} \cdot (\mathbf{r} - \mathbf{r}_0) = 0$. Since we know that $\nabla f$ is **normal** to the level curves, then at point $\mathbf{r}_0$, the normal vector becomes $\mathbf{n} = \nabla f(\mathbf{r}_0)$ and thus the tangent line is given (in implicit form) by:

{% math() %}
\begin{align*}
\nabla f(\mathbf{r}_0) (\mathbf{r} - \mathbf{r}_0) = 0 \\
\dfrac{\partial f(x_0, y_0)}{\partial x} (x - x_0) - \dfrac{\partial f(x_0, y_0)}{\partial y} (y - y_0) = 0
\end{align*}
{% end %}

We may use the same procedure to find the tangent plane for an _implicitly defined_ surface $F(x, y, z) = g(x, y, z) - c = 0$. In this case, the level sets are not curves but _level surfaces_ in the form $g(x, y, z) = c$. Again, $\nabla F$ is always normal to the level surfaces, and thus the tangent plane is equation is given by $\nabla F (\mathbf{r}_0) \cdot (\mathbf{r} - \mathbf{r}_0) = 0$.

### Taylor expansions in several variables

A tangent plane is the _geometric representation_ of a linear approximation to a function of two or three variables. But higher-dimensional functions beyond three dimensions certainly exist, and while it is hard to make geometric sense of them, the idea of a linear approximation is still mathematically sound. We will now extend this idea to $n$-dimensional approximations to $n$-dimensional functions, using **mutivariable Taylor series**.

We recall that in single-variable calculus, we may approximate complex functions using **Taylor series** (also called _Taylor expansions_). Specifically, at some point $x = x_0$, the function may be approximated by an $n$-th order polynomial called a **Taylor polynomial**:

{% math() %}
\begin{align*}
T_n(x) =& f(x_0) + f'(x_0)(x - x_0) + \dfrac{1}{2!} f''(x_0) (x-x_0)^2 \\
&+ \dfrac{1}{3!} f'''(x_0) (x - x_0)^3 + \dots + \dfrac{1}{n!} f^{(n)}(x_0)(x - x_0)^n
\end{align*}
{% end %}

Where $f^{(n)}(x_0) = \dfrac{d^n f}{dx^n}\bigg|_{\mathbf{r} = \mathbf{r}_0}$ is the $n$-th derivative of $f$, evaluated at point $x_0$. Taylor polynomials also exist for functions of several variables. The **multivariate Taylor polynomial** for a function $f(x, y)$ takes the form:

{% math() %}
\begin{align*}
L(x, y) &= f(\mathbf{r}_0) + \nabla f \cdot (\mathbf{r}- \mathbf{r}_0) \\
&\qquad+ \dfrac{1}{2}\left(\dfrac{\partial^2f(x_0, y_0)}{\partial x^2} (x-x_0)^2 + \dfrac{\partial^2f(x_0, y_0)}{\partial y^2} (y-y_0)^2 + 2\dfrac{\partial^2f(x_0, y_0)}{\partial y \partial x} (x-x_0)(y-y_0)\right) \\
&\qquad+ \dots
\end{align*}
{% end %}

If the point to be approximated happens to be $\mathbf{r} = 0$, then:

{% math() %}
L(x, y) = f_0 + \nabla f \cdot \mathbf{r} +
\dfrac{1}{2} \left(\dfrac{\partial^2f(x_0, y_0)}{\partial x^2} x^2 + \dfrac{\partial^2f(x_0, y_0)}{\partial y^2} y^2 + 2\dfrac{\partial^2f(x_0, y_0)}{\partial y \partial x} xy \right) + \dots
{% end %}

Where $f_0 = f(0, 0, 0)$. Note how there also exist cross terms such as $xy$, which make the expression far more complex than the 1D case. There also exist Taylor approximations for functions of three or more variables, as well as terms beyond quadratic order. Their general form (for $\mathbf{r} = x_1, x_2, x_3, \dots, x_n$) is as follows:

{% math() %}
L(\mathbf{r}) = f_0 + \nabla f \cdot (\mathbf{r} - \mathbf{r}_0) + \dfrac{1}{2} (\mathbf{r} - \mathbf{r}_0)\{D^2[f(r_0)] \cdot (\mathbf{r} - \mathbf{r}_0)\} + \dots
{% end %}

We use the curly braces around the derivatives to indicate that the $(\mathbf{r} - \mathbf{r}_0)^n$ terms are _not to be differentiated_. Here, $D^2$ is a matrix known as the **Hessian** (one we will extensively use later), containing all of a function's second-order partial derivatives, given by:

{% math() %}
D^2 = \begin{bmatrix}
\dfrac{\partial^2 f}{\partial x_1^2} & \dfrac{\partial^2 f}{\partial x_1 \partial x_2} & \dots & \dfrac{\partial^2 f}{\partial x_1 \partial x_n} \\
\dfrac{\partial^2 f}{\partial x_2 x_1} & \dfrac{\partial^2 f}{\partial x_2^2} & \dots & \dfrac{\partial^2 f}{\partial x_2 \partial x_n} \\
\vdots & \vdots & \ddots & \vdots \\
\dfrac{\partial^2 f}{\partial x_n \partial x_1} & \dfrac{\partial^2 f}{\partial x_n \partial x_2} & \dots & \dfrac{\partial^2 f}{\partial x_n^2}
\end{bmatrix}
{% end %}

A useful reminder is that the $(i, j)$ entry of the Hessian matrix is given by $\dfrac{\partial^2 f}{\partial x_i \partial x_j}$. For a function $f(x, y)$, the Hessian takes the (thankfully!) much simpler form:

{% math() %}
D^2_{(x, y)} =
\begin{bmatrix}
\dfrac{\partial^2 f}{\partial x^2} & \dfrac{\partial^2 f}{\partial x \partial y} \\
\dfrac{\partial^2 f}{\partial y \partial x} & \dfrac{\partial^2 f}{\partial y^2}
\end{bmatrix}
{% end %}

> **Note:** The **total degree** of a polynomial of several variables is an easy source of confusion. If a polynomial has a term $x^2 y$, then the term is said to be of _3rd-order_ (or degree 3), because we sum the power of 2 on $x$ and the power of 1 on $y$. Similarly, $x y^3 z^5$ is said to be _9th-order_ (or degree 9), as we have $1 + 3 + 5 = 9$ by summing up the powers on each term. The **total degree** of a polynomial is the order of its highest-order term, so for instance, the polynomial $f(x, y) = 3 + 5xy + 7 x^3 + x^2 y^2$ has a _total degree of 4_, since the highest order term is $x^2 y^2$ which is a _4th-order term_. 

Note that we do not always have to explicitly calculate partial derivatives term-by-term to find the Taylor series of a function of several variables. Consider, for instance, the function $f(x, y) = e^{-(x^2 + y^2)}$. While we could in theory calculate all of its partial derivatives, this would take a long time and be very prone to mistakes. Rather, recall that the Taylor series of $e^t$ is given by:

{% math() %}
e^t =1 + t + \dfrac{1}{2!} t^2 + \dfrac{1}{3!} t^3 + \dfrac{1}{4!} t^4 + \dots + \dfrac{1}{n!} t^n
{% end %}

Thus we can substitute in $-(x^2 + y^2)$ into $t$ for the above Taylor series to find the Taylor series of $f(x, y)$:

{% math() %}
\begin{align*}
  f (x, y) & =  1 + (- (x^2 + y^2)) + \dfrac{(- (x^2 + y^2))^2}{2} +
  \dfrac{(- (x^2 + y^2))^3}{6} + \dots\\
  & =  1 - (x^2 + y^2) + \dfrac{1}{2}  (x^2 + y^2)^2 - \dfrac{1}{6}  (x^2 +
  y^2)^3 + \dots .
\end{align*}
{% end %}

### Optimization in several variables

We are often interested in maximizing or minimizing a function of several variables, just like we do in single-variable calculus. The **extrema** (maxima and minima) of a multivariable function also occur at its _critical points_. The critical points are all points for which:

{% math() %}
\nabla f = 0
{% end %}

Each point $(x_i, y_i)$ that satisfies $\nabla f = 0$ is a critical point. To find these critical points is then just a matter of solving the system of equations from $\nabla f = 0$ for the solutions $(x_i, y_i)$:

{% math() %}
\begin{align*}
\dfrac{\partial f}{\partial x} &= 0 \\
\dfrac{\partial f}{\partial y} &= 0 \\
\dfrac{\partial f}{\partial z} &= 0 \\
\vdots \\
\dfrac{\partial f}{\partial x_i} &= 0
\end{align*}
{% end %}

> **Note:** Typically speaking, this is a system of _nonlinear equations_ - see [this guide here](https://math.libretexts.org/Bookshelves/Algebra/Intermediate_Algebra_1e_(OpenStax)/11%3A_Conics/11.06%3A_Solving_Systems_of_Nonlinear_Equations) for how to be able to solve such systems.

However, not all critical points are extrema. To be able to determine _which_ of the critical points are, indeed, extrema, we must use the **multivariable second derivative test**. Recall how we previously showed that we could write the Taylor polynomial of a function of several variables up to quadratic order:

{% math() %}
L(\mathbf{r}) = f_0 + \nabla f \cdot (\mathbf{r} - \mathbf{r}_0) + \dfrac{1}{2} (\mathbf{r} - \mathbf{r}_0)\{D^2[f(r_0)] \cdot (\mathbf{r} - \mathbf{r}_0)\} + \mathcal{O}((\mathbf{r} - \mathbf{r}_0)^3)
{% end %}

(Note that $\mathcal{O}((\mathbf{r} - \mathbf{r}_0)^3)$ means "all terms involving cubes of $x, y, z$", that is, anything above quadratic order). We know that for a quadratic in one variable in the form $ax^2 + bx + c$, we can find the number of roots via its discrimminant $b^2 - 4ac = \det \begin{pmatrix} b & 2a \\ 2c & b\end{pmatrix}$ and we can find whether it opens upwards (i.e. $\cup$ shaped) or opens downwards (i.e. $\cap$ shaped) based on the sign of $a$. We can do something very similar with the quadratic Taylor polynomial, just with the Hessian (and the other coefficients of the Taylor polynomial). This results in the **multivariable second derivative test**:

> **Multivariable second derivative test:** Let $D^2[f(x_i, y_i)]$ be the Hessian evaluated at the critical point $(x_i, y_i)$. If $D^2[f(x_i, y_i)] > 0$, there exists a **local extrenum** at the critical point. If $D^2[f(x_i, y_i)] < 0$, there exists a **saddle point** at the critical point. If $D^2[f(x_i, y_i)] = 0$, the test is **inconclusive**.

If we find that that the critical point is indeed a local extrenum, we may then determine whether it is a local minimum or a local minimum as follows:

- If $\dfrac{\partial^2 f}{\partial x^2}(x_i, y_i) > 0$, then the point is a **local minimum**
- If $\dfrac{\partial^2 f}{\partial x^2}(x_i, y_i) < 0$, then the point is a **local maximum**

> **Note:** With the second derivative test, we can only determine _local_ minima and maxima. We **cannot guarantee** that they are _global_ minima and maxima without explicitly evaluating the function at all of the boundary points on its domain. With a few exceptions, this is usually not possible to do.

### Optimization with constraints

We saw previously that we may optimize a function of multiple variables by solving for its critical points and using the second partial derivative test to characterize each critical point. Strictly speaking, this type of optimization is called **unconstrained optimization**: we search for critical points (and thus possible minima/maxima) _anywhere_ in the function's domain.

But there is another type of optimization, called **constrained optimization**, in which we only want to find critical points that satisfy a particular condition. Consider the following example problem: find all the minima of $f(x, y)$ at points of unit distance from the origin. We may express this in the following form:

{% math() %}
\begin{align*}
&{\underset {(x, y)}{\operatorname{minimize}}} &&f(x, y)\\
&\operatorname {subject\;to} &&\sqrt{x^2 + y^2} = 1
\end{align*}
{% end %}

Our distance formula $\sqrt{x^2 + y^2} = 1$ can be expressed as $D(x, y) = \sqrt{x^2 + y^2} -1$, where $D(x, y) = 0$. This is known as our **constraint** (in 2D, specifically, a _constraint curve_). Now, notice that $D(x, y) = 0$ is an _implicit equation_. We know from before that the normal vector of an implicit curve/surface $F(x, y, z) = 0$ is given by $\hat{\mathbf{n}} = \nabla F$. In a similar fashion, the normal vector of $D(x, y)$ is given by:

{% math() %}
\hat{\mathbf{n}} = \nabla D(x, y)
{% end %}

Previously, when we were discussing _unconstrained_ optimization, the condition to find the extrema was to solve for the points that satisfy $\nabla f = 0$, i.e. the function _does not change_. The condition to find the extrema in _constrained_ optimization, meanwhile, is to solve for the points _along the constraint curve_ for which $\nabla f$ _does not change_. That is to say, the directional derivative of $f$ must be zero along the tangent $\mathbf{r}'(t)$ to the curve:

{% math() %}
\begin{matrix*}
\nabla_{\vec{\mathbf{r}}'}f = 0 & \Rightarrow & \nabla f \cdot \mathbf{r}'(t) = 0
\end{matrix*}
{% end %}

This can only happen if the _gradient_ of $f$ is _perpendicular_ to the tangent to the curve, that is, $\nabla f \perp \mathbf{r}'(t)$. So the gradient of $f$ must also be parallel to the _normal vector_ of the curve, which is given by $\hat{\mathbf{n}} = \nabla D(x, y)$! This is the key insight behind the idea of Lagrange multipliers. Two vectors that are parallel are scalar multiples of each other, which means that since $\nabla f \parallel \hat{\mathbf{n}}$ and thus $\nabla f \parallel \nabla D$, we have:

{% math() %}
\nabla f \propto \nabla D
{% end %}

Which can also be written as:

{% math() %}
\nabla f = \lambda \nabla D
{% end %}

The proportionality constant is called $\lambda$, also known as a **Lagrange multiplier**. From the above equation we can rearrange to get the **Lagrange system of equations**:

{% math() %}
\begin{align*}
\nabla f - \lambda \nabla D = 0 \\
D(x, y) = 0
\end{align*}
{% end %}

Solving these equations gives the critical points $(x_i, y_i)$ that satisfy the given constraint, and then we can use the second derivative test (as usual) to classify the critical points. Note that it is also possible to have multiple constraints on a system; in that case, the Lagrange system of equations becomes:

{% math() %}
\begin{align*}
&\nabla f - \lambda_1 D_1(x, y) + \lambda_2 D_2 (x, y) + \dots
 +\lambda_n D_n(x, y) = 0 \\[10pt]
&\begin{cases}
 D_1(x, y) &= 0 \\
 D_2(x, y) &= 0 \\
 D_3(x, y) &= 0 \\
 &\vdots \\
 D_n (x, y) &= 0
\end{cases}
\end{align*}
{% end %}

Where $D_1, D_2, D_3, \dots, D_n$ are implicit equations that each describe a particular constraint.

### Implicit function theorem

Consider an implicit function defined by $f(x, y(x)) = 0$. This may be, for instance, the equation of a circle, where $f(x, y(x)) = x^2 + y^2 - R^2$. How would we find the derivative of such a function, expressed as $\dfrac{dy}{dx}$?

We recall that we can use implicit differentiation to be able to solve. But there is a more powerful method from multivariable calculus. If we differentiate $f$ with respect to $x$ we have:

{% math() %}
\dfrac{\partial f}{\partial x} + \dfrac{\partial f}{\partial y} \dfrac{dy}{dx} = 0
{% end %}

Which we may rearrange to:

{% math() %}
\dfrac{\partial f}{\partial y} \dfrac{dy}{dx} = -\dfrac{\partial f}{\partial x}
{% end %}

And thus we find that:

{% math() %}
\dfrac{dy}{dx} = -\dfrac{\partial_x f}{\partial _y f}
{% end %}

> Here we use the notation that $\partial_x f = \frac{\partial f}{\partial x}$ and $\partial_y f = \dfrac{\partial f}{\partial y}$.

### Inverse function theorem

In single-variable calculus, we know that if we had some function $y = y(x)$, whose *inverse* was given by $x = y^{-1}$, then $\dfrac{dx}{dy} = \dfrac{1}{\frac{dy}{dx}}$. This does have some intuitive sense: since $y^{-1}$ (the inverse of $y(x)$) is simply $y(x)$ mirrored across the line $y = x$, the slope of the $y^{-1}$ is the reciprocal of the slope of $y(x)$, hence $(y^{-1})' = 1/y'(x)$. However, this is no longer true in the _multivariable case_, since the inverse of a multivariable function is not a simple reflection about the line $y = x$; indeed, the inverse may be highly nontrivial.

Thankfully, there is a way to find the derivative of the inverse of a multivariable function, called the **implicit function theorem**. We will first state it (although the definition is not necessary particularly helpful):

> **Inverse function theorem:** For given invertible function $f : \mathbb{R}^n \rightarrow \mathbb{R}^m$ given by $f = \langle f_1, f_2, f_3 \ldots f_i \ldots f_{m - 1}, f_m \rangle$ where $f_i = f_i (x_1, x_2, x_3 \ldots x_i \ldots x_{n - 1}, x_n)$ whose inverse  $f^{- 1} : \mathbb{R}^m \rightarrow \mathbb{R}^n$ is given by $f^{-1} = \langle x_1 (f_i), x_2  (f_i), x_3  (f_i) \ldots x_i  (f_i) \ldots x_{n - 1} (f_i), x_n  (f_i) \rangle$ then, given the Jacobian matrix $J [f]$ exists, then $(J [f^{- 1}]) = (J [f])^{- 1}$.

To gain some greater insight, it may be helpful to express it in matrix form, for which we have the following:

{% math() %}
% Jacobian of f^(-1)
\begin{bmatrix}
% row 1
\frac{\partial x_1}{\partial f_1} & \frac{\partial x_1}{\partial f_2}  & \frac{\partial x_1}{\partial f_3} & \dots \frac{\partial x_1}{\partial f_m} \\
% row 2
\frac{\partial x_2}{\partial f_1} & \frac{\partial x_2}{\partial f_2}  & \frac{\partial x_2}{\partial f_3} & \dots \frac{\partial x_2}{\partial f_m} \\
% row 3
\frac{\partial x_3}{\partial f_1} & \frac{\partial x_3}{\partial f_2}  & \frac{\partial x_3}{\partial f_3} & \dots \frac{\partial x_3}{\partial f_m} \\
% row 4
\vdots & \vdots  & \vdots & \ddots & \vdots \\
% row 5 
\frac{\partial x_n}{\partial f_1} & \frac{\partial x_n}{\partial f_2}  & \frac{\partial x_n}{\partial f_3} & \dots \frac{\partial x_n}{\partial f_m} \\
\end{bmatrix} =
% Inverse of the Jacobian of f
\begin{bmatrix}
% row 1
\frac{\partial f_1}{\partial x_1} & \frac{\partial f_1}{\partial x_2} & \frac{\partial f_1}{\partial x_3} & \dots & \frac{\partial f_1}{\partial x_n}
 \\
 % row 2
 \frac{\partial f_2}{\partial x_1} & \frac{\partial f_2}{\partial x_2} & \frac{\partial f_2}{\partial x_3} & \dots & \frac{\partial f_2}{\partial x_n} \\
 % row 3
 \frac{\partial f_3}{\partial x_1} & \frac{\partial f_3}{\partial x_2} & \frac{\partial f_3}{\partial x_3} & \dots & \frac{\partial f_3}{\partial x_n} \\
 % row 4
 \vdots & \vdots  & \vdots & \ddots & \vdots \\
 % row 5
 \frac{\partial f_m}{\partial x_1} & \frac{\partial f_m}{\partial x_2} & \frac{\partial f_m}{\partial x_3} & \dots & \frac{\partial f_m}{\partial x_n}
\end{bmatrix}^{-1}
{% end %}

Neither of these forms, however, are particularly illustrative, so instead let us give a more familiar example - a coordinate transformation. Frequently, we must complete a change of coordinates given only the new coordinates expressed in terms of the old coordinates. Consider a function $z(u, v) = z(u(x, y), u(x, y))$. Presume we want to express the (unknown) partial derivatives of $z$ with respect to $x, y$ in terms of the (known) partial derivatives of $z$ with respect to $u, v$. That is, we want to do the following:

{% math() %}
\begin{align*}
\underbrace{\dfrac{\partial z}{\partial x}, \dfrac{\partial z}{\partial y}}_\text{unknown} \quad \underbrace{\longrightarrow}_\text{transform} \quad \underbrace{\dfrac{\partial z}{\partial u}, \dfrac{\partial z}{\partial v}}_\text{known}
\end{align*}
{% end %}

By the chain rule we have:

{% math() %}
\begin{align*}
\dfrac{\partial z}{\partial x} = \dfrac{\partial z}{\partial u} \dfrac{\partial u}{\partial x} + \dfrac{\partial z}{\partial v} \dfrac{\partial v}{\partial x} \\
\dfrac{\partial z}{\partial y} = \dfrac{\partial z}{\partial u} \dfrac{\partial u}{\partial y} + \dfrac{\partial z}{\partial v} \dfrac{\partial v}{\partial y} \\
\end{align*}
{% end %}

But we only provided with $x = x(u, v)$ and $y = y(u, v)$ - we _don't know_ $\dfrac{\partial u}{\partial x}, \dfrac{\partial u}{\partial y}$ or $\dfrac{\partial v}{\partial x}, \dfrac{\partial v}{\partial y}$. In principle, we can perform some algebra to find $u, v$ in terms of $x, y$ and then differentiate, but suppose that our coordinate transforms are sufficiently complicated that doing so would be very time-consuming and error-prone (sometimes, not even possible!). 

The inverse function theorem speeds this up immensely: we can directly find the partial derivatives as follows. If we define a vector-valued function containing the *known* derivatives $\vec f = \langle x(u, v), y(u, v)\rangle$, where $x = x(u, v), y = y(u, v)$ are our given coordinate transforms, then by the inverse function theorem, we may find the derivatives of the vector-valued function containing the _unknown derivatives_ $\vec g = \vec f^{-1} = \langle u(x, y), v(x, y)\rangle$ as follows:

{% math() %}
J[\vec g(u, v)] = (J[\vec f(x, y)])^{-1}
{% end %}

> **Note:** $f$ and $g$ are just convenient vector-valued functions to "hold" the derivatives to help with expanding the Jacobians. Technically they are not necessary - one can just go directly to the Jacobian with some mental juggling of partial derivatives.

Expanding the Jacobians leads to the following transformation matrix equation:

{% math() %}
\underbrace{
\begin{bmatrix}
\dfrac{\partial u}{\partial x} & \dfrac{\partial u}{\partial y} \\
\dfrac{\partial v}{\partial x} & \dfrac{\partial v}{\partial y}
\end{bmatrix} 
}_{\text{unknown derivatives of }g(u, v)}
= 
\underbrace{
\begin{bmatrix}
\dfrac{\partial x}{\partial u} & \dfrac{\partial x}{\partial v} \\
\dfrac{\partial y}{\partial u} & \dfrac{\partial y}{\partial v} 
\end{bmatrix}^{-1}
}_{\text{known derivatives of }f(x, y)}
{% end %}

Which allows us to compute the derivatives we want from the derivatives we know, completing the coordinate transformation.

### Motion along a path

Let us return to a familiar topic - the description of a path through space. We may describe such a path using a **parametric representation** $\mathbf{r}(t) = \langle x(t), y(t), z(t)\rangle$. We vary our parameter $t$ within $t \in [a, b]$, such that the endpoints of the curve are located at points $\mathbf{r}(a)$ and $\mathbf{r}(b)$. A visualization is shown below:

{{ natural_img(
src="spatial-curve-external.png",
desc="An illustration of a helix-shaped parametric curve in space"
)}}


_Source: [OpenStax](https://math.libretexts.org/Bookshelves/Calculus/Calculus_%28OpenStax%29/13%3A_Vector-Valued_Functions/13.01%3A_Vector-Valued_Functions_and_Space_Curves)_

At every point, there exists also a _tangent vector_ to $\mathbf{r}(t)$, which is denoted $\mathbf{r}'(t) \equiv \dfrac{d\mathbf{r}}{dt}$. In a physical scenario, where $\mathbf{r}(t)$ represents a trajectory through space, $\mathbf{r}'(t)$ represents the _velocity_. Taking another derivative, we have $\mathbf{a}(t) = \mathbf{r}''(t)$, the _acceleration_.

We have already seen some examples of parametric paths. For instance, we saw that a **straight line** is given by:

{% math() %}
\begin{matrix*}
\mathbf{r}(t) = \mathbf{r}_0 + \mathbf{v}t, & t \in [-\infty, \infty]
\end{matrix*}
{% end %}

Meanwhile a semi-circle can be parametrized as:

{% math() %}
\begin{matrix*}
\mathbf{r}(t) = \langle a \cos t, a \sin t\rangle, &t \in [-\pi, \pi]
\end{matrix*}
{% end %}

Note that this parametrization is **non-unique**. It would just be as valid to parametrize a semi-circle as follows:

{% math() %}
\begin{matrix*}
\mathbf{r}(t) = \langle a \cos \tau, a \sin \tau\rangle, &\tau \in \left[-\frac{\pi}{2}, \frac{\pi}{2}\right]
\end{matrix*}
{% end %}

From our tools of calculus and geometry, we may measure the **arc length** (that is, total length) of a parametric curve - physically, this represents the _distance_ travelled along a curve. While the arc length formula may be rather familiar from single-variable calculus, we now want to _derive it_ rather than accept it as proof. To do so, we divide up a path $\mathbf{r}(t)$ into many, many small sections $\Delta \mathbf{r} = \mathbf{r}(t + \Delta t) - \mathbf{r}(t)$. The length of each segment $\Delta L$ is then simply the magnitude of $\Delta \mathbf{r}$, that is:

{% math() %}
\Delta L = |\Delta \mathbf{r}|
{% end %}

Where we use the bar notation to indicate the magnitude. The total length

{% math() %}
\begin{align*}
L &= \sum_{i = 1}^n \Delta L_i \\
&= \sum_{i = 1}^n|\Delta \mathbf{r}_i| \\
&= \sum_{i = 1}^n |\mathbf{r}_i(t + \Delta t) - \mathbf{r}_i|
\end{align*}
{% end %}

Recall that from the theory of _linear approximations_ we have $\mathbf{r}_i (t + \Delta t) \approx \mathbf{r}_i(t) + \mathbf{r}_i'(t)$. Therefore, we have:

{% math() %}
\begin{align*}
L &=\sum_{i = 1}^n |\mathbf{r}_i(t + \Delta t) - \mathbf{r}_i| \\
&\approx \sum_{i = 1}^n \left|\mathbf{r}_i(t) + \mathbf{r}_i'(t) - \mathbf{r}_i\right| \\
&= \sum_{i = 1}^n \left|\cancel{\mathbf{r}_i(t)} + \mathbf{r}_i'(t) - \cancel{\mathbf{r}_i}\right| \\
&= \sum_{i = 1}^n |\mathbf{r}_i'(t)|
\end{align*}
{% end %}

If we take the limit as $n \to \infty$, this relation becomes exact, and the sum becomes an integral: 

{% math() %}
L = \int_a^b |\mathbf{r}'(t)|dt = \int_a^b \sqrt{\left(\dfrac{dx}{dt}\right)^2 + \left(\dfrac{dy}{dt}\right)^2 + \left(\dfrac{dz}{dt}\right)^2}\, dt
{% end %}

For instance, let us calculate the arc length of a circle. Recall that the parametric equations of a circle of radius $R$ are $\mathbf{r}(t) = R\langle \cos t, R\sin t\rangle$, and therefore we have $\mathbf{r}'(t) = \langle -R\sin t, R\cos t\rangle$. Taking the magnitude, we have $|\mathbf{r}'(t)| = \sqrt{(-R\sin t)^2 + (R\cos t)^2} = \sqrt{R^2\left(\sin^2 t + \cos^2 t\right)}$, which, recalling the Pythagorean trigonometric identity $\sin^2 t + \cos^2 t = 1$, becomes $|\mathbf{r}'(t)| = \sqrt{R^2(1)} = R$ and thus $\mathbf{r}'(t) = R$. Since a circle is defined for $t \in [0, 2\pi]$, the integral becomes rather easy to evaluate:

{% math() %}
L = \int_a^b |\mathbf{r}'(t)|dt = \int_0^{2\pi} R\, dt = 2\pi R - 0(R) = 2\pi R
{% end %}

Which reproduces the expected result for the circumference of a circle. Note that the arc length is just one topic in the broad field of **differential geometry** that studies geometry using methods of calculus. We will not go into it, but it is a very fun topic to read about for those interested.

#### Reparametrization of parametric curves

A final topic to mention is that since the parametrization is non-unique, we can choose an arbitrary parametrization. One often-useful parametrization is the **arclength reparametrization**. To do so, we first define the arc length function $s(t)$ as:

{% math() %}
\begin{align*}
s(t) &= \int_a^t |\dot{\mathbf{r}}(t')| dt' \\
&= \int_a^t \small{\sqrt{\left(\frac{dx}{dt'}\right)^2 + \left(\frac{dy}{dt'}\right)^2 + \left(\frac{dz}{dt'}\right)^2}}\, dt'
\end{align*}
{% end %}

Here, since we want the arclength function in terms of $t$, we relabel our integration variable from $t$ to $t'$ (but otherwise the integrand stays identical, this is just a _relabelling_). From $s(t)$, we obtain the inverse function $t(s) = s^{-1}(t)$. Substituting in the parametric path $\mathbf{r}$, we have:

{% math() %}
\mathbf{r}(t) = \mathbf{r}(t(s)) = \mathbf{r}(s)
{% end %}

This allows us to obtain the parametric equations expressed with respect to the distance along the path, which can be very useful.