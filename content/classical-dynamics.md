+++
title = "Notes on introductory classical dynamics"
date = 2024-01-08
+++

These are notes taken in RPI's Physics 1150 class, relating to introductory classical dynamics - essentially, Newtonian mechanics. Make sure to read the [calculus series](@/calculus-series.md) first as these notes are calculus-heavy.

<!-- more -->

## Dimensional analysis

Dimensional analysis is a method of doing a "sanity check" for _numerical computations_ with units. That is, an equation only makes sense if the units check out.

For instance, consider:

$$
x(t) = \frac{1}{2} at^2
$$
Does this make sense with dimensional analysis? Well, acceleration is in units of $ms^{-2}$ and time is in units of $s^2$, so multiplying them together and by 1/2 (a dimensionless value) gives units of $m$ (meters). And meters are a reasonable unit for a position $x(t)$.

To keep track of dimensions, it is often more useful to use general dimensions for each term - $M$ for the mass dimension, $L$ for the length dimension, $T$ for the time dimension. So, plugging in this:

$$
L = \frac{1}{2} \times LT^{-2} \times T^2 = L
$$

So it's correct!

## Newton's 2nd Law

In 1 dimension, Newton's second law relates the net force $F$ with position and time:

$$
F(x(t), \dot x(t), t) = m \frac{d^2 x}{dt^2}
$$

This is a **2nd-order ordinary differential equation of motion** that describes how an object moves.

### Special cases of Newton's 2nd Law

In a **constant-force problems**, then we assume $F$ is a constant. Therefore:

$$
F = m \frac{d^2 x}{dt^2}
$$
Which we can rewrite as:

$$
F = m \frac{dv}{dt}
$$

Using integration, we can solve:

$$
v(t) = \int \frac{F}{m} dt = v_0 + \frac{F}{m}t
$$

Then, we solve for:

$$
v = \frac{dx}{dt}
$$
We integrate again to find:

$$
x(t) = \int v(t) dt = x_0 + v_0 t + \frac{1}{2} \frac{F}{m} t^2
$$

In a **time-dependent force problem**, then:

$$
v(t) = \int \frac{F(t)}{m} dt
$$
$$
x(t) = \int v(t) dt
$$

### Drag force application

For an object falling through atmosphere, the drag force is given by $F_D = -bv$, and the gravitational force is given by $F_G = mg$.

Using the principle of superposition of forces, we can add all the individual forces acting on a falling object to obtain:

$$
m \frac{dv}{dt} = mg - bv, \quad v(0) = 0
$$

This is a **separable** first-order ordinary differential equation, which we can solve by the method of separation of variables.

Therefore, we have:

$$
\frac{dv}{dt} = g - \frac{b}{m} v
$$
$$
\frac{dv}{g - (b/m) v} = dt
$$
Now, we can integrate both sides to solve (the left-hand side uses a u-substitution):

$$
\int \frac{dv}{g - (b/m) v} = \int dt
$$

$$
-\frac{b}{m} \ln \left( g - \frac{b}{m} v \right) = t + C
$$

Solving for the initial condition $v(0) = 0$, we have:

$$
-\frac{m}{b} \ln |g| = C
$$
Using algebraic manipulation, we can solve for $v$ in terms of $t$:

$$
v(t) = \frac{mg}{b} \left(1 - e^{-\frac{b}{m}t} \right)
$$
Note that if we take the limit of $v(t)$ as $t \to \infty$, then we reach a terminal (constant) velocity:

$$
\lim_{t \to \infty} v(t) = \frac{mg}{b}
$$

## Approximation techniques

To first-order (when a point is close to $x_0$), the derivative is approximately a finite difference:

$$
\frac{df}{dx} \bigg|_{x = x_0} \approx \frac{\Delta f}{\Delta x}
$$

So a linear approximation to a function at an arbitrary point $x_0$ is:

$$
f(x) \approx f(x_0) + f'(x_0)(x - x_0)
$$

For example, $e^x \approx 1 + x$, and $\sin(x) \approx x$.

## Kinematics with calculus

Recall the derivative relationships between velocity and acceleration:

$$
v(t) = \frac{dx}{dt}
$$
$$
a(t) = \frac{dv}{dt} = \frac{d^2 x}{dt^2}
$$
And recall the inverse integral relationships:
$$
\Delta x = \int_{t_0}^{t_1} v(t) dt
$$
$$
\Delta v = \int_{t_0}^{t_1} a(t) dt
$$
In addition, to solve differential equations (such as those that result from applying Newton's 2nd law), use the method of **separation of variables**.

## Vectors and their representations

A vector is a mathematical object with special properties that is often used to model physical phenomena.

A **coordinate system** is a measurement grid centered at a particular origin. Vectors can be written in any coordinate system. To do so, they are written in terms of unit (basis) vectors, which are the vectors of length 1 that align with each of the axes of the given coordinate system.

For instance, vectors in Cartesian space can be written in terms of the $\hat i, \hat j, \hat k$ vectors that correspond to the x, y, z Cartesian axes. They are notationally written as follows:
$$
\vec a = a_x \hat i + a_y \hat j = \langle a_x, a_y\rangle
$$
There are other coordinate systems that can be used, including polar, spherical, and cylindrical. For example, polar vectors are written with:

$$
\hat a = a_r \hat r + a_\phi \hat \phi = \langle a_r, a_\phi \rangle
$$
Coordinate systems can be converted - for example, these are conversions of polar to cartesian:

$$
x = r \cos \phi, \quad
y = r \sin \phi
$$

And these are the conversions from cartesian to polar:

$$
r = \sqrt{x^2 + y^2}, \quad \phi = \tan^{-1} \left(\frac{y}{x}\right)
$$
The length of a vector, also called the magnitude or norm, is found by taking the square root of the sum of the squares of each component:

$$
\| \vec s \| = \sqrt{s_x^2 + s_y^2}
$$

Vectors sum and subtract elementwise. To do so, just add/subtract each of the vector's components:

$$
\vec s = \vec a + \vec b = \langle a_x + b_x, a_y + b_y \rangle
$$

Vectors can also be multiplied by scalars, which are simply numbers. Scalar multiplication is performed by multiplying the scalar by each of their components:

$$
\vec s = c \vec a = \langle c \cdot a_x, c \cdot a_y \rangle
$$

The dot product of two vectors results in a scalar, and is given by:

$$
\vec a \cdot \vec b = \|a \| \|b \| \cos \phi = a_x b_x + a_y b_y
$$
The cross product of two vectors results in a new vector, and is given by:

$$
\vec a \times \vec b = \| a \| \| b \|  \sin \phi = \langle a_y b_z - a_z b_y, a_z b_x - a_x b_z, a_x b_y - a_y b_x \rangle
$$
To remember this formula:

- Remember that the components' subscripts are in the order $yz$, $zx$, $yx$ (e.g. $yz$ expands into $a_y b_z - a_z b_y$)
- Follow the cycle $yzx$, the first component is the $y \to z$, the second is $z \to x$, the third is $y \to x$

(to remember this, just remember the $yz, zx, yx$ pattern)

The cross product is defined only for 3D space, and is anticommutative: $\vec a \times \vec b = - (\vec b \times \vec a)$. Taking the cross product of 2D vectors requires making them 3D vectors with a z-component of zero.

The area of a parallelogram is given by the _magnitude_ of the cross product of the two vectors:

$$
A = ab \sin \theta = \| \vec a \times \vec b \|
$$

## Vector kinematics

The position vector is given by $\vec s = \langle x(t), y(t), z(t) \rangle$ in Cartesian coordinates. The velocity vector is given by the derivative of position vector with respect to time. That is:

$$
\vec v = \frac{d \vec s}{dt} = \left\langle \frac{dx}{dt}, \frac{dy}{dt}, \frac{dz}{dt} \right\rangle
$$

And similarly, the acceleration vector is defined by the time derivative of the velocity vector:

$$
\vec a = \frac{d \vec v}{dt} = \frac{d^2 \vec s}{dt^2} = \left \langle \frac{d^2 x}{dt^2}, \frac{d^2 y}{dt^2}, \frac{d^2 z}{dt^2} \right \rangle
$$

Note that Newton's second law in vector form (for 2D or 3D) is given by a vector differential equation that expand to 4 (in 2D) or 6 (in 3D) coupled ordinary differential equations:

$$
m \frac{d^2 \vec s}{dt^2} = m\frac{d \vec v}{dt} = \vec F \left(\vec s, \frac{d\vec s}{dt}, t\right)
$$

Luckily, a shift of coordinates is typically sufficient to be able to treat most 2D and 3D problems as 2D or 1D problems, reducing the need to solve such a complex vector differential equation.

**Projectile motion** (motion under constant downward acceleration) in 2D is a special case of this vector differential equation that is able to be solved analytically:

$$
m \frac{dv_x}{dt} = 0, \quad m \frac{dv_y}{dt} = -mg
$$
$$
v_x (0) = v_0 \cos \theta, \quad v_y(0) = v_0 \sin (\theta)
$$

The analytical solution is given by:

$$
\vec s(t) = \langle x(t), y(t) \rangle
$$
$$
x(t) = x_0 + v_0 \cos (\theta) t, \quad y(t) = y_0 + v_0 \sin (\theta) t - \frac{1}{2} gt^2
$$
We can find the range of a projectile (how far it travels horizontally) by solving for the value of $t$ where $y(t) = 0$ and then substituting that value of $t$ into $x(t)$. That is:

$$
y(t) = 0 \Rightarrow t = 0, t=\frac{2v_0 \sin \theta}{g}
$$

The first solution is trivial (not useful) but the second is nontrivial. Substituting into $x(t)$, we have:

$$
R = x_0 + v_0 \cos \theta \left(\frac{2 v_0 \sin \theta}{g}\right) = x_0 + \frac{v_0^2 \sin (2 \theta)}{g}
$$

To maximize the range $R$ given the angle $\theta$, we simply set $\frac{dR}{d\theta} = 0$ as with typical methods of optimization in calculus. From there, it can be found that the optimal angle is at $\theta = \frac{\pi}{4}$.

Lastly, it can be shown that this traces out the trajectory of a parabola. To do so, we take the two parametric equations $x(t)$ and $y(t)$ and eliminate the parameter. From this we get:


$$
y = -\frac{g}{2v_{0x}^2 } x^2 + \frac{v_{0y}}{v_{0x}}x
$$
Which can be written as:

$$
y = -\frac{g}{2 v_0^2 \cos^2 \theta} x^2 + v_0 \tan (\theta) x
$$

## Energy

Energy can be understood as a measure of the ability to make things move. It comes in two primary types: kinetic energy, which is associated with moving, and potential energy, which is associated with being able to move.

## Work

Work is the transfer of energy by a force applied along a displacement. It is a scalar quantity defined by:

$$
W = \int_{x_0}^{x_1} F(x) dx
$$
Note that force can be defined by:

$$
F = m \frac{dv}{dt}
$$

We can use this alternate definition of force to obtain the work-energy theorem:

$$
W = \int_{x_0}^{x_1} m\frac{dv}{dt} dx = \int_{x_0}^{x_1} m\frac{dv}{dt} \frac{dx}{dt} dt = \int_{x_0}^{x_1} m \frac{dv}{dt} v dt = \int_{v_0}^{v_1} mvdv = \frac{1}{2} m(v_2^2 - v_1^2) = \frac{1}{2} m \Delta v^2 = \Delta K
$$

## Conservation of energy

If a force depends only on position, it is called a **conservative force**. A conservative force stores energy in the form of potential energy, and releases energy in the form of kinetic energy. Conservative forces are associated with a potential energy function $U(x)$ in 1D via:

$$
F(x) = -\frac{dU}{dx}
$$

Using the same method as prior to obtain the work-energy theorem, we find that:

$$
W = \int_{x_0}^{x_1} -\frac{dU}{dx} dx = -\int_{x_0}^{x_1} dU = -U(x) \bigg |_{x_0}^{x_1} = -\Delta U
$$

Therefore:

$$
W = -\Delta U = \Delta K
$$
$$
K_1 + U_1 = K_2 + U_2
$$

The total mechanical energy $E$ is conserved for conservative forces (this means it's a constant):

$$
E = K + U, \quad \frac{dE}{dt} = 0
$$
Recall that while force can be perfectly defined from potential energy, the potential energy cannot be perfectly defined by the force. This is because:

$$
U(x) = -\int F(x) dx + C
$$
And therefore any $C$ could possibly be chosen. So, one often choses the constant such that the potential energy is zero at a conveniently specified location $x_0$, which we can call the "ground level":

$$
U(x) = -\int_{x_0}^x F(x') dx'
$$
For instance, consider the example of 1D constant gravity, where $F(x) = -mg$ and $U(0) = 0$, we have:

$$
U(x) = -\int_0^h F(x) dx = mgh
$$
Given that $x(0) = h, v(0) = 0$, and using conservation of energy, we have:

$$
E_1 = E_2
$$
$$
mgh = \frac{1}{2} mv^2 \Rightarrow v = \sqrt{2gh}
$$
For the more general 1D case, we can write the conservation of energy as a differential equation, where $E$ is constant:

$$
\frac{1}{2} m \left(\frac{dx}{dt}\right)^2 + U(x) = E
$$
Rearranging, we get the **separable 1st-order ODE**:

$$
\frac{dx}{dt} = \pm \sqrt{\frac{2}{m}(E - U(x))}
$$

## Potential energy landscapes

By plotting the graph of $U(x)$, the potential energy function, we can determine the characteristics of the motion of an object. The following features of $U(x)$ are especially important:

- Local minimum of $U(x)$ - stable equilibrium position
- Local maximum $U(x)$ - unstable equilibrium position
- Lower potential energy regions - the object has more kinetic energy and so moves faster
- Higher potential energy regions - the object has less kinetic energy and so moves slower

## Multivariable functions and partial derivatives

Consider a multivariable function $f(x, y, z)$. How would the derivative of this function be defined? Since the function depends on multiple variables, you can differentiate with respect to each individual variable. Each derivative is known as a _partial derivative_, and is denoted as follows:

$$
\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}, \frac{\partial f}{\partial z}
$$
When differentiating with respect to one variable, all the other variables are kept constant. That is, if $f(x, y) = x^2 y^3$, then when taking the partial derivative with respect to $x$, we factor out all terms in $y$ and consider them a constant:

$$
\frac{\partial f}{\partial x} = \frac{\partial}{\partial x} x^2 y^3 = y^3 \frac{\partial}{\partial x} x^2 = 2xy^3
$$
Similarly, if taking the partial derivative with respect to $y$, we factor out all terms in $x$ and consider them a constant:

$$
\frac{\partial f}{\partial y} = \frac{\partial}{\partial y} x^2 y^3 = x^2 \frac{\partial}{\partial y} y^3 = 3x^2 y^2
$$
The total differential of a multivariable function is given by:

$$
df = \frac{\partial f}{\partial x} dx + \frac{\partial f}{\partial y} dy + \frac{\partial f}{\partial z} dz
$$

## Vector calculus

We say that the gradient of a multivariable function $f(x, y, z)$ is given by:

$$
\left(\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}, \frac{\partial f}{\partial z}\right)
$$
This is often notated $\nabla f$ for "gradient of $f$", where $\nabla$ is a vector operator defined by:

$$
\nabla = \left(\frac{\partial}{\partial x}, \frac{\partial}{\partial y}, \frac{\partial}{\partial z} \right)
$$
Similarly an infinitesimal displacement can be written as:
$$
d \vec s = (dx, dy, dz)
$$
Using this notation:

$$
df = \nabla f \cdot d\vec s
$$
There are two other vector operations of relevance in vector calculus. These operate on vector-valued multivariable functions, which are typically in the form:

$$
\vec F = \vec F(x, y, z) = \begin{bmatrix}
F_x(x, y, z) \\\\
F_y(x, y, z) \\\\
F_z(x, y, z)
\end{bmatrix} =
F_x(x, y, z) \hat i + F_y(x, y, z) \hat j + F_z (x, y, z) \hat k
$$

First, the divergence operation measures flow rate, and is given by:

$$
\nabla \cdot \vec F = \left(\frac{\partial}{\partial x}, \frac{\partial}{\partial y}, \frac{\partial}{\partial z} \right) \cdot (F_x, F_y. F_z) =\frac{\partial F_x}{\partial x} + \frac{\partial F_y}{\partial y} + \frac{\partial F_z}{\partial z}
$$
Second, the curl operation measures rotation, and is given by:

$$
\nabla \cdot \vec F = \left(\frac{\partial}{\partial x}, \frac{\partial}{\partial y}, \frac{\partial}{\partial z} \right) \times (F_x, F_y. F_z)  = \left(
\frac{\partial F_z}{\partial y} - \frac{\partial F_y}{\partial z},
\frac{\partial F_x}{\partial z} - \frac{\partial F_z}{\partial x},
\frac{\partial F_{y}}{\partial x}- \frac {\partial F_x}{\partial y}
\right)
$$
## Work in higher dimensions

In higher dimensions, force is a vector-valued function of the position $\vec r(t)$, which itself has three components $x(t)$, $y(t)$, and $z(t)$. So force depends on position, which depends on $x$, $y$, and $z$, which themselves depend on time. That's a mouthful! We can mathematically express this relationship as:

$$
\vec F = \vec F(\vec r) = \vec F(x, y, z) = \vec F(x(t), y(t), z(t))
$$

Extending the definition of 1D work, the differential of the work in higher dimensions would be given by:

$$
dW = \vec F \cdot d\vec s
$$
The force is applied along a path from $a = (x_0, y_0, z_0)$ to $b = (x_1, y_1, z_1)$ in 3D space, which we denote with $C$ (for "curve"). The total work is given by the integral of this quantity along the path, which we call a **line integral**:

$$
W = \int_{C[a \to b]} \vec F \cdot d\vec s
$$

Note that the subscript under the integral is optional and not required.

Line integrals can be evaluated by expanding them component-by-component:

$$
\int_C \vec F \cdot d\vec s = \int_{C(a)}^{C(b)} \vec F(x(t), y(t), z(t)) \cdot (dx, dy, dz)
$$
Using the fact that:

$$
d\vec s = \frac{d\vec s}{dt} dt = (x'(t) dt, y'(t) dt, z'(t) dt) = \vec r'(t) dt
$$
where $r'(t) = (x', y', z')$, line integrals can be rewritten as:

$$
\begin{align}
& \int_C \vec F(\vec r) \cdot d\vec s \\\\ &= \int_{C(a)}^{C(b)} (F_x(t) x'(t)+ F_y(t) y'(t) + F_z(t) z'(t) )dt \\\\ &= \int_{C(a)}^{C(b)} \vec F(t) \cdot \vec r'(t) dt
\end{align}
$$

In higher dimensions, Newton's 2nd Law can be written as:

$$
m \frac{d^2 \vec r}{dt^2} = m \frac{d \vec v}{dt} = \vec F
$$

The work-energy theorem can also be expressed in higher dimensions. Using the fact that:

$$
d\vec s = \frac{d\vec s}{dt} dt = \vec v dt
$$
We obtain:

$$
\begin{align}
W &= \int_C \vec F \cdot d\vec s \\\\ & = \int_C m\frac{d\vec v}{dt} \cdot \frac{d\vec s}{dt} dt \\\\ &= \int_C m \vec v \cdot d\vec v \\\\ &= \frac{1}{2} m(\vec v \cdot \vec v) \bigg |_a^b \\\\ &= \frac{1}{2} m \Delta v^2 = \Delta K
\end{align}
$$

## Conservation of energy in higher dimensions

In higher dimensions, kinetic energy is still a scalar function, but involves derivatives in more than one dimension:

$$
K = \frac{1}{2} mv^2 = \frac{1}{2} m \left[\left( \frac{dx}{dt} \right)^2 + \left( \frac{dy}{dt} \right)^2 + \left( \frac{dz}{dt} \right)^2 \right]
$$

Potential energy is also still a scalar function, but becomes multivariable:

$$
U = U(x, y, z)
$$

A force $\vec F$ is called **conservative** if there is a potential energy function $U(x, y, z)$ such that:

$$
\vec F = -\nabla U = -\left(\frac{\partial U}{\partial x}, \frac{\partial U}{\partial y}, \frac{\partial U}{\partial z}\right)
$$

This means that particles naturally flow from a region of higher potential energy to a region of lower potential energy. We can also write this in (line) integral form; in this form, the potential energy at $r = (x, y, z)$ defined with respect to a reference point $r_0 = (x_0, y_0, z_0)$ is given by:

$$
U(x, y, z) = -\int_{C[r_0 \to r]} \vec F \cdot d\vec s
$$

For conservative forces, there are several important properties:

- The line integral of the force is independent of path
- The line integral of the force vanishes for any closed path
- $\nabla \times \vec F = 0$

Therefore the work (in the case of conservative forces only!) can be rewritten as:

$$
\begin{align}
W &= \int_{C[a \to b]} \vec F \cdot d\vec s \\\\ &= -\int_{C[a \to b]} \nabla U \cdot d\vec s \\\\ &= -\int_a^b dU = U(a) - U(b) = -\Delta  U
\end{align}
$$

Here we use the expression of the total differential to arrive at the prior result:

$$
\begin{align}
\nabla U \cdot d\vec s &= \left(\frac{\partial U}{\partial x}, \frac{\partial U}{\partial y}, \frac{\partial U}{\partial z}\right) \cdot (dx, dy, dz)
\\\\ &= \frac{\partial U}{\partial x} dx + \frac{\partial U}{\partial y} dy + \frac{\partial U}{\partial z} dx \\\\ &= dU
\end{align}
$$

Equating the two equivalent definitions of work (for kinetic and potential energy respectively), we find that the work-energy theorem still holds true:

$$
\Delta K = -\Delta U
$$
Or:

$$
K(b) - K(a) = U(a) - U(b)
$$

Rearranging, we find that:

$$
K(a) + U(a) = K(b) + U(b)
$$

Therefore, total energy is conserved in the case of conservative forces, even in higher dimensions:

$$
\frac{d}{dt} (K + U) = 0
$$

## Uniform circular motion

Uniform circular motion describes motion in which an object moves with constant velocity in a circular path of fixed radius. In this situation, the object does not have any tangential acceleration (acceleration along its velocity vector) but it does have **centripetal acceleration** towards the center, with a magnitude given by:
$$
a = \frac{v^2}{R}
$$
Or in vector form:
$$
\vec a = -\frac{v^2}{R} \hat r
$$
The object moving along the circular path would trace out a distance $ds = Rd\theta$ when it advances along an angle $d\theta$. Therefore

$$
\frac{ds}{dt} = R \frac{d\theta}{dt} \Rightarrow v =R \omega
$$
The angular velocity $\omega$ can be found from differentiation of $\theta(t)$, but in the special case of uniform circular motion it can be more easily found from the period (the time it takes for the object to complete a full revolution):
$$
\omega = \frac{2\pi}{T}
$$
Note that:
$$
f = \frac{1}{T}
$$
In the case of non-uniform circular motion, there is both tangential and centripetal acceleration present. The tangential acceleration in this case is given by:

$$
\vec a_t = \frac{d\vec v}{dt}
$$
The centripetal acceleration, however, remains the same:
$$
\vec a_c = -\frac{v^2}{R} \hat r
$$
The overall acceleration $\vec a$ is given by:
$$
\vec a = \vec a_t + \vec a_c
$$
When considering problems of circular motion, instead of using $\sum F_i = ma$, instead use $\sum F_i = \frac{mv^2}{R}$. The centripetal force is not an isolated force, but is rather the net force in the radial direction, and the forces that provide it are other forces, such as gravitational force and normal force.

### Example cases of circular motion

Consider a bead of mass $m$ attached to a string and is revolving in a circular fashion. We can decompose the forces into vertical and horizontal components. Using Newton's second law, the horizontal net force is given only by the radial tension force $\vec T$. Therefore, considering the magnitudes of the forces only:

$$
m a_c = m\frac{v^2}{R}=  T
$$
Meanwhile, the vertical net force depends on the location of the bead. At the very top of the circle, then:

$$
m a_c = m\frac{v^2}{R} = T + mg
$$
At the very bottom of the circle, then:

$$
m a_c = m\frac{v^2}{R} = T - mg
$$
At the leftmost and rightmost edges of the circle, then:

$$
m a_c = m\frac{v^2}{R} = T
$$
## Newton's theory of gravity

In Newtonian mechanics, the gravitational force is given by:

$$
\vec F_g = -\frac{Gm_1 m_2}{r^2} \hat r
$$
### Perfectly circular orbits

The simplest case of planetary motion can be modeled with uniform circular motion, that is, equating centripetal force and the gravitational force:

$$
m\frac{v^2}{R} = G \frac{Mm}{r^2}
$$
Solving for $v$, we have:
$$
v = \sqrt{\frac{GM}{r}}
$$

And the orbital period $T$ is given by:

$$
T = 2\pi \sqrt{\frac{r^3}{GM}}
$$

This is often rewritten as:

$$
T^2 = \frac{4\pi^2 r^3}{GM}
$$

### Newton's shell theorem

Newton found that a uniformly dense thin spherical shell attracts an external particle identically to a point mass. In addition, a particle _inside_ such a shell would feel no gravitational force. This is often called **Newton's shell theorem**.

Using the shell theorem, we can divide a solid sphere of radius $R$ and mass $M$ into infinitely many infinitesimally-thin shells, and apply the shell theorem additively for each. Therefore we find again that the sphere attracts an external particle identically to a point mass. A particle inside such a sphere at a radius $r$ would feel a gravitational force that comes only from the amount of mass underneath the particle (that is, within $r$). 

To compute the value of this force, we want to first find the amount of mass inside a radius $r$. Given $dm = \rho dV$, and $dV = 4\pi r^2 dr$, we can say that:

$$
M(r) = \int_0^r dm = \int_0^r 4\pi (r')^2\rho(r') dV
$$

where we relabel from $r \to r'$ in the integrand to avoid confusing integration bounds and variables. This results in a linear force inside the spherical mass given by:
$$
F = \frac{GMm}{R^3} r
$$
Therefore given the spherical mass $M$ of radius $R$, the magnitude of the gravitational force $F$ is a piecewise function:

$$
F = 
\begin{cases}
\frac{GMm}{r^2}, & r > R \\\\
\frac{GMm}{R^3}r, & r < R \\\\
\end{cases}
$$

### Gravitational potential energy

The gravitational potential energy, like any potential energy for a conservative force, is given by the negative work (work done against the force of gravity) to bring a mass to its position $r$:

$$
U = -\int_{C[r_0 \to r]} \vec F \cdot d\vec s
$$

More precisely, this negative work is done along a path from a reference point $r_0$ to the object's current position $r$, where we choose the reference point such that $U(r_0) = 0$. Previously, this reference point was often assumed to be the ground - that is, $U = 0$ when $y = 0$. In the case of generalized gravitation, we choose a point infinitely far away as the reference point for the gravitational potential energy (that is, $U = 0$ at $r = \infty$). Therefore, the line integral simplifies to:

$$
U(r) = -\int_\infty^r -\frac{GMm}{{r'}^2} dr' = -\frac{GMm}{r}
$$

This can be approximated for objects near the Earth as:

$$
U(y) \approx mgy
$$

### Gravitational total energy

The total energy in gravitation is given by:

$$
E = K + U = \frac{1}{2} mv^2 -\frac{GMm}{r}
$$

$E$ must be less than zero for an object to remain in orbit. Solving for $v$ in the case $E \geq 0$, we find that the **escape velocity** of an object in orbit is given by:

$$
v_{\mathrm{esc}} = \sqrt{\frac{2GM}{r}}
$$

## Angular momentum

Newton's second law can be formulated in terms of momentum $\vec p$:

$$
F = \frac{d\vec p}{dt}
$$
However, for radial problems, it is often more helpful to formulate Newton's second law in terms of _angular momentum_ $\vec L$, defined:
$$
\vec L = \vec r \times \vec p
$$
In this case, Newton's second law becomes the equation for **torque** $\vec \tau$, the radial equivalent of force:

$$
\vec \tau = \frac{d\vec L}{dt} = \vec r \times \vec F
$$

## Kepler's laws

1. Each planet moves in an elliptical orbit described by the parameters $a$ and $b$
2. A line from the Sun to a given planet sweeps out equal areas in equal times
3. The square of the period of the orbit is proportional to the cube of $a$

Kepler's first law means that the orbits of planets follow the equation of an ellipse:

$$
\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1
$$

Here, $a$ is the semi-major axis, which is half the distance across the longer diameter of the ellipse. $b$ is the semi-minor axis, which is half the distance across the shorter diameter of the ellipse. 

![Image of an ellipse, showing the semi-major and semi-minor axes](https://upload.wikimedia.org/wikipedia/commons/9/96/Ellipse-def0.svg)

(Credit: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Ellipse-def0.svg))

For gravitational orbits, the values of $a$ and $b$ are given by:

$$
a = \frac{GMm}{2|E|}
$$
$$
b = \frac{L}{\sqrt{2m|E|}}
$$

Kepler's second law is due to the fact that as the gravitational force and angular momentum are parallel vectors, their cross product is zero, and thus angular momentum is conserved.

Kepler's third law was proven earlier in the case of perfectly circular orbits. For an improved generalization that extends to elliptical orbits, the relationship is given by:

$$
T^2 = \sqrt{\frac{4\pi^2 a^3}{GM}}
$$

## Mathematical interlude: Taylor series

A function can be approximated near a point $x_0$ via:

$$
f(x) \approx f(x_0) + f'(x_0)(x - x_0) + \frac{1}{2} (x - x_0)^2 + \dots
$$

If infinite terms are used, then the function can be _exactly_ represented by its approximation:
$$
f(x) = \sum_{n = 0}^\infty \frac{f^{(n)}(x_0)}{n!}(x - x_0)^n
$$
In practice, however, only a few terms (typically up to 2nd-order or 3rd-order) are necessary, and we usually set $x_0 = 0$. For instance:

| Function | Approximation about $x = 0$ (up to 2nd or 3rd order) |
| ---- | ---- |
| $(1 + x)^\alpha$ | $1 + \alpha x + \frac{1}{2}\alpha (\alpha - 1)x^2$ |
| $e^x$ | $1 + x + \frac{x^2}{2}$ |
| $\sin x$ | $x - \frac{x^3}{6}$ |
| $\cos x$ | $1 - \frac{x^2}{2}$ |
| $\ln (1 + x)$ | $x - \frac{x^2}{2}$ |
| $\tan x$ | $x + \frac{x^3}{3}$ |
| $1/(x + \alpha)^n$ | $\frac{1}{\alpha^{n}}-\frac{nx}{\alpha^{n+1}}+\frac{n(n+1)x^{2}}{2\alpha^{n+2}}$ |

This means, for instance, that for an object a small distance $\alpha$ above the surface of the Earth, where the radius of the Earth is given by $r_E$, then the magnitude of the gravitational force can be reasonably approximated by a Taylor expansion about $r = r_E$:

$$
F_g = \frac{GMm}{r_E^2} -\frac{GMm}{r_E^3} (r - r_E) + \frac{GMm}{2r_E^4} (r-r_E)^2 + \dots
$$
If we define $g = \frac{GM}{r_E^2}$, then to the first term of the Taylor expansion, we have:

$$
F_g = mg
$$

## Complex numbers

The **imaginary unit** is defined by $i = \sqrt{-1}$. Complex numbers are made of a real part and an imaginary part, and are written with $z = a + bi$. Complex numbers can also be represented in polar coordinates, where the magnitude $\|z\| = \sqrt{a^2 + b^2}$ and they can be written as $z = \|z\| \cos \phi + \|z\| i \sin \phi$. The complex conjugation is given by $z^\*$ where if $z = a + bi$, then $z^\* = a - bi$, and there is the special property $z \cdot z^* = a^2 + b^2$.

Using Euler's formula, we can extend the exponential function to the complex plane:
$$
e^z = e^a(\cos b + i \sin b)
$$
If we let $a = 0$ and $b = i\phi$, then it simplifies to:

$$
e^{i\phi} = \cos \phi + i \sin \phi
$$

Therefore, any complex number can be written in the form:

$$
z = \|z\| e^{i\phi}
$$
And the trigonometric functions can be written in terms of exponentials:

$$
\cos \phi = \frac{e^{i\phi} + e^{-i\phi}}{2}, \quad \sin \phi = \frac{e^{i\phi} - e^{-i\phi}}{2i}
$$
## Small oscillators and the simple harmonic oscillators

Newton's second law can be written in the form:
$$
m\frac{d^2 x}{dt^2} =-\frac{dU}{dx}
$$
Around a certain point $x_0$, the Taylor expansion of the potential energy around that point is given by:

$$
U(x) = U_0 + U'(x_0)(x - x_0) + \frac{1}{2} U''(x_0)(x - x_0)^2 + \frac{1}{6} U'''(x_0) (x - x_0)^3 + \dots
$$
When a system only slightly deviates from equilibrium (that is, it is at a point close to a local minimum of the potential energy), the Taylor expansion to first-order is given by:

$$
U(x) \approx U_0 + U'(x_0) (x - x_0) + \frac{1}{2} U''(x_0)(x - x_0)^2
$$
Therefore:

$$
\frac{dU}{dx} = U'(x_0) + U''(x_0) (x-x_0)
$$
Given that the system is very close to its local minimum, the first derivative $U'$ at $x_0$ vanishes as well, so:

$$
\frac{dU}{dx} = U''(x_0) (x - x_0)
$$

If we set $k = U''(x_0)$ and perform the change of variables $y = x - x_0$ then Newton's second law is approximately:

$$
m\frac{d^2 y}{dt^2} = -ky
$$
Which can be written as:

$$
\frac{d^2 y}{dt^2} + \frac{k}{m}y = 0
$$
Or, with $\omega = \sqrt{\frac{k}{m}}$, we have:

$$
\frac{d^2 y}{dt^2} + \omega^2 y = 0
$$

Which has the exact general solution:

$$
y = A e^{i \omega t} + Be^{-i\omega t}
$$
Using Euler's formula we can rewrite as:

$$
y = C_1 \cos \omega t + C_2 \sin \omega t
$$
Examples of systems described in this form include the simple pendulum equation:
$$
\frac{d^2 \theta}{dt^2} + \frac{g}{L} \theta = 0
$$

## Oscillators

Oscillators are a very important system in physics because, as mentioned previously, many systems from classical and even quantum mechanics can be approximated as a (oftentimes coupled) system of oscillators. In regions close to a potential well, a particle typically oscillates back and forth about the potential well, 

### The damped oscillator

A dampening force (such as drag) can be added to more realistically model an oscillator. A good approximation for the dampening force is a force proportional to velocity, such as $F_d = -bv$. Then Newton's second law becomes:

$$
m\frac{d^2 x}{dt^2} = -kx - bv
$$
Since $v = dx/dt$, we can rewrite this equation as:

$$
\frac{d^2 x}{dt^2} + \frac{b}{m} \frac{dx}{dt} + \frac{k}{m} x = 0
$$
If we let $\omega_0^2 = k / m$ and $\beta = b / 2m$, then the differential equation becomes:

$$
\frac{d^2 x}{dt^2} + 2\beta \frac{dx}{dt} + \omega_0^2 x = 0
$$
This equation is a 2nd-order homogeneous differential equation. The solution of this differential equation is given by three cases:

- $\beta > \omega_0$ is the case of over-dampening, which tends to an exponential decay with a general solution of $x(t) = Ae^{-\beta t + \sqrt{\beta^2 - \omega_0^2} t} + Be^{-\beta t - \sqrt{\beta^2 - \omega_0^2}t}$
- $\beta = \omega_0$ is the case of critical-dampening, which also tends to an exponential decay with a general solution $x(t) = (At + B)e^{-\beta t}$
- $\beta < \omega_0$ is the case of under-dampening (or weak dampening), which leads to a slow decay with the general solution of $x(t) = Ae^{-\beta t} \cos (\sqrt{\omega_0^2 - \beta^2} t + \phi)$

### Driven damped harmonic oscillators

A driven harmonic oscillator adds a a driving force in addition to a dampening force to the model of an oscillator. Such a driving force could be in the form $F = F_0 \cos \omega t$ (here note that $\omega$ is not the same as $\omega_0$). Therefore, the differential equation becomes:

$$
m\frac{d^2 x}{dt^2} = -kx - bv + F_0 \cos (\omega t)
$$

Which we can rearrange to obtain:

$$
\frac{d^2 x}{dt^2} + 2\beta \frac{dx}{dt} + \omega_0^2 x = \frac{F_0}{m} \cos (\omega t)
$$
This equation is still a 2nd-order differential equation, but it is now _inhomogeneous_. The solution to this equation is given by:

$$
x(t) = x_H(t) + D(\omega) \cos(\omega t - \delta(\omega))
$$
Where:
$$
D(\omega) = \frac{F_0}{m} \frac{1}{\sqrt{(\omega_0^2 - \omega^2)^2 + 4\beta^2 \omega^2}}
$$
$$
\delta(\omega) = \tan^{-1} \left(\frac{2\beta \omega}{\omega_0^2 - \omega^2}\right)
$$
And $x_H(t)$ is the general solution of the dampened harmonic oscillator for the given $\beta$ and $\omega_0$. For instance, for a weak-dampening driven harmonic oscillator, then the general solution is:

$$
x(t) = Ae^{-\beta t} \cos (\sqrt{\omega_0^2 - \beta^2} t + \phi) + D(\omega) \cos(\omega t - \delta(\omega))
$$
Typically, as $t \to \infty$, $x_H(t)$ decays exponentially, so $x_H(t) \approx 0$ and only the driving force (also called "transient") part of the solution remains.

Unlike purely dampened or simple harmonic oscillators, driven damped oscillators have the phenomena of **resonance**. This is the idea that $D(\omega)$ can be _tuned_ to maximize its value and thereby maximize the amplitude. As a paraphrased example from _Waves: An Interactive Tutorial_ by Forinash and Christian, an example is a sound wave tuned with a value of $\omega$ that maximizes its amplitude sufficient break a wine glass.

### Applied harmonic oscillators

A LRC circuit is an oscillating system which is described by a very similar differential equation:

$$
L \frac{d^2 Q}{dt^2} + R \frac{dQ}{dt} + \frac{Q(t)}{C} = \mathcal{E}_0 \cos \omega t
$$
Here, we can cast the differential equation into the general form of a harmonic oscillator by using $\beta = R / 2L$ and $\omega_0^2 = \frac{1}{LC}$. This can be readily solved using the same method as the harmonic oscillator.
