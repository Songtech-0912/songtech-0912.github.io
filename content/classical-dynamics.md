+++
title = "Notes on introductory classical dynamics"
date = 2024-01-08
+++

These are notes taken in RPI's Physics 1150 class, relating to introductory classical dynamics. Make sure to read the [calculus series](@/calculus-series.md) first as these notes are calculus-heavy.

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
F(x, \dot x, t) = m \frac{d^2 x}{dt^2}
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
m \frac{d^2 \vec s}{dt^2} = m\frac{d \vec v}{dt} = \vec F \left(\vec r, \frac{d\vec s}{dt}, t\right)
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

If a force depends only on position, it is called a **conservative force**. Conservative forces are associated with a potential energy function $U(x)$ in 1D via:

$$
F(x) = -\frac{dU}{dx}
$$

Using the same method as prior to obtain the work-energy theorem, we can:

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
The force is applied along a path in 3D space, which we call $C$ (for "curve"). The total work is given by the integral of this quantity along the curve, which we call a **line integral**:

$$
W = \int_C \vec F \cdot d\vec s
$$
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
\int_C \vec F(\vec r) \cdot d\vec s = \int_{C(a)}^{C(b)} (F_x(t) x'(t)+ F_y(t) y'(t) + F_z(t) z'(t) )dt = \int_{C(a)}^{C(b)} \vec F(t) \cdot \vec r'(t) dt
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
W = \int_C \vec F \cdot d\vec s = \int_C m\frac{d\vec v}{dt} \cdot \frac{d\vec s}{dt} dt = \int_C m \vec v \cdot d\vec v = \frac{1}{2} m(\vec v \cdot \vec v) \bigg |_a^b = \frac{1}{2} m \Delta v^2 = \Delta K
$$

## Conservation of energy in higher dimensions

A force $\vec F$ is called **conservative** if there is a scalar function $U(x, y, z)$ such that:

$$
\vec F = -\nabla U = -\left(\frac{\partial U}{\partial x}, \frac{\partial U}{\partial y}, \frac{\partial U}{\partial z}\right)
$$

This function $U(x, y, z)$ is known as the potential function, and particles naturally flow from a region of higher potential to a region of lower potential. For conservative forces, there are several important properties:

- The line integral of the force is independent of path
- The line integral of the force vanishes for any closed path
- $\nabla \times \vec F(\vec r) = 0$

Therefore the work (in the case of conservative forces only!) can be rewritten as:

$$
W = \int_C \vec F \cdot d\vec s = -\int_C \nabla U \cdot d\vec s = -\int_a^b dU = U(a) - U(b) = -\Delta  U
$$

Here we use the expression of the total differential to arrive at the prior result:

$$
\nabla U \cdot d\vec s = \left(\frac{\partial U}{\partial x}, \frac{\partial U}{\partial y}, \frac{\partial U}{\partial z}\right) \cdot (dx, dy, dz) = \frac{\partial U}{\partial x} dx + \frac{\partial U}{\partial y} dy + \frac{\partial U}{\partial z} dx = dU
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
