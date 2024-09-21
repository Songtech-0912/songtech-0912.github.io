+++
title = "Notes on introductory classical dynamics"
date = 2024-01-08
+++

These are notes taken in RPI's Physics 1150 class, relating to introductory classical dynamics - essentially, Newtonian mechanics. Make sure to read the [calculus series](@/calculus-series.md) first as these notes are calculus-heavy.

<!-- more -->

## Dimensional analysis

Dimensional analysis is a method of doing a "sanity check" for _numerical computations_ with units. That is, an equation only makes sense if the units check out.

For instance, consider:

{% math() %}
x(t) = \frac{1}{2} at^2
{% end %}

Does this make sense with dimensional analysis? Well, acceleration is in units of $ms^{-2}$ and time is in units of $s^2$, so multiplying them together and by 1/2 (a dimensionless value) gives units of $m$ (meters). And meters are a reasonable unit for a position $x(t)$.

To keep track of dimensions, it is often more useful to use general dimensions for each term - $M$ for the mass dimension, $L$ for the length dimension, $T$ for the time dimension. So, plugging in this:

{% math() %}
L = \frac{1}{2} \times LT^{-2} \times T^2 = L
{% end %}

we have the correct units, so we have verified it is correct!

## Kinematics with calculus

Position, velocity, and acceleration are fundamental quantities in physics whose collective study is known as **kinematics**. The quantities are related through differential and integral calculus. For instance, they can be written as derivatives of each other:

{% math() %}
v(t) = \frac{dx}{dt}
{% end %}
{% math() %}
a(t) = \frac{dv}{dt} = \frac{d^2 x}{dt^2}
{% end %}

And accumulated changes in position and velocity are given by integrals of velocity and acceleration, respectively:

{% math() %}
\Delta x = \int_{t_0}^{t_1} v(t) dt
{% end %}
{% math() %}
\Delta v = \int_{t_0}^{t_1} a(t) dt
{% end %}

## Introduction to Newtonian mechanics

Newtonian mechanics are a formulation of physics developed primarily by Isaac Newton and his contemporaries. In Newtonian mechanics, _forces_ are the cause of motion. When there are no forces acting on an object, or when all the forces are balanced, the object stays in constant motion. When the forces are not balanced, then the object experiences a change in its motion. Both of these observations, and more, are described by **Newton's second law**:

{% math() %}
F_\mathrm{net}(x(t), \dot x(t), t) = m \frac{d^2 x}{dt^2}
{% end %}

where the net force $F_\mathrm{net}$ is given by the sum of all forces:

{% math() %}
F_\mathrm{net} = \sum_i F_i(x, \dot x, t) = F_1 (x, \dot x, t) + F_2 (x, \dot x, t) + \dots + F_n (x, \dot x, t)
{% end %}

This is a **2nd-order ordinary differential equation** that describes how an object moves, which is also why it's called an _equation of motion_. In fact, it's one of the most important equations of motion in physics. It describes the physics of many different systems, from planetary orbits to springs to projectiles to charged particles moving through electromagnetic fields.

However, to actually apply Newton's 2nd Law can be quite difficult. Other than a few special cases with known general solutions, the differential equation often cannot be solved exactly, and even when exact solutions exist, there is no general formula for them. Luckily, the special cases of Newton's 2nd law are still sufficient to describe the physics of many systems, and a brief overview of these special cases is given in the following section. 

### Special cases of Newton's 2nd Law

The following special cases of Newton's 2nd law are cases in which the differential equation can be solved with the method of **separation of variables**. This is a technique used widely throughout physics to solve differential equations.

In a **constant-force problems**, we assume $F$ is a constant. Therefore:

{% math() %}
F = m \frac{d^2 x}{dt^2}
{% end %}

Which we can rewrite as:

{% math() %}
F = m \frac{dv}{dt}
{% end %}

Using integration, we can solve:

{% math() %}
v(t) = \int \frac{F}{m} dt = v_0 + \frac{F}{m}t
{% end %}

Then, we solve for:

{% math() %}
v = \frac{dx}{dt}
{% end %}

We integrate again to find:

{% math() %}
x(t) = \int v(t) dt = x_0 + v_0 t + \frac{1}{2} \frac{F}{m} t^2
{% end %}

In a **time-dependent force problem**, then:

{% math() %}
v(t) = \int \frac{F(t)}{m} dt
{% end %}
{% math() %}
x(t) = \int v(t) dt
{% end %}

which can be rewritten as one integral:

{% math() %}
x(t) = \frac{1}{m} \int_0^t \int_0^t F(s) ~ds~ds
{% end %}

> Note here we are replacing $F(t)$ with $F(s)$ to avoid mixing the integration bounds with integration variable.

Finally, in a **position-dependent force problem**, then the general solution is an implicit solution given by:

{% math() %}
\int \left(\frac{2}{m} \int F(x)~dx + C \right)^{-{1 \over 2}} dx - t = 0
{% end %}

### Drag force application

An example of the time-dependent case of Newton's 2nd law is an object experiencing drag. For an object falling through atmosphere, the drag force is given by $F_D = -bv$, and the gravitational force is given by $F_G = mg$.

Using the principle of superposition of forces, we can add all the individual forces acting on a falling object to obtain:

{% math() %}
m \frac{dv}{dt} = mg - bv, \quad v(0) = 0
{% end %}

This is a **separable** first-order ordinary differential equation, which we can solve by the method of separation of variables.

Therefore, we have:

{% math() %}
\frac{dv}{dt} = g - \frac{b}{m} v
{% end %}
{% math() %}
\frac{dv}{g - (b/m) v} = dt
{% end %}

Now, we can integrate both sides to solve (the left-hand side uses a u-substitution):

{% math() %}
\int \frac{dv}{g - (b/m) v} = \int dt
{% end %}

{% math() %}
-\frac{b}{m} \ln \left( g - \frac{b}{m} v \right) = t + C
{% end %}

Solving for the initial condition $v(0) = 0$, we have:

{% math() %}
-\frac{m}{b} \ln |g| = C
{% end %}

Using algebraic manipulation, we can solve for $v$ in terms of $t$:

{% math() %}
v(t) = \frac{mg}{b} \left(1 - e^{-\frac{b}{m}t} \right)
{% end %}

Note that if we take the limit of $v(t)$ as $t \to \infty$, then we reach a terminal (constant) velocity:

{% math() %}
\lim_{t \to \infty} v(t) = \frac{mg}{b}
{% end %}

## Approximation techniques

To first-order (when a point is close to $x_0$), the derivative is approximately a finite difference:

{% math() %}
\frac{df}{dx} \bigg|_{x = x_0} \approx \frac{\Delta f}{\Delta x}
{% end %}

So a linear approximation to a function at an arbitrary point $x_0$ is:

{% math() %}
f(x) \approx f(x_0) + f'(x_0)(x - x_0)
{% end %}

For example, $e^x \approx 1 + x$, and $\sin(x) \approx x$.

## Vectors and their representations

A vector is a mathematical object with special properties that is often used to model physical phenomena.

A **coordinate system** is a measurement grid centered at a particular origin. Vectors can be written in any coordinate system. To do so, they are written in terms of unit (basis) vectors, which are the vectors of length 1 that align with each of the axes of the given coordinate system.

For instance, vectors in Cartesian space can be written in terms of the $\hat i, \hat j, \hat k$ vectors that correspond to the x, y, z Cartesian axes. They are notationally written as follows:
{% math() %}
\vec a = a_x \hat i + a_y \hat j = \langle a_x, a_y\rangle
{% end %}

There are other coordinate systems that can be used, including polar, spherical, and cylindrical. For example, polar vectors are written with:

{% math() %}
\hat a = a_r \hat r + a_\phi \hat \phi = \langle a_r, a_\phi \rangle
{% end %}

Coordinate systems can be converted - for example, these are conversions of polar to cartesian:

{% math() %}
x = r \cos \phi, \quad
y = r \sin \phi
{% end %}

And these are the conversions from cartesian to polar:

{% math() %}
r = \sqrt{x^2 + y^2}, \quad \phi = \tan^{-1} \left(\frac{y}{x}\right)
{% end %}

The length of a vector, also called the magnitude or norm, is found by taking the square root of the sum of the squares of each component:

{% math() %}
\| \vec s \| = \sqrt{s_x^2 + s_y^2}
{% end %}

Vectors sum and subtract elementwise. To do so, just add/subtract each of the vector's components:

{% math() %}
\vec s = \vec a + \vec b = \langle a_x + b_x, a_y + b_y \rangle
{% end %}

Vectors can also be multiplied by scalars, which are simply numbers. Scalar multiplication is performed by multiplying the scalar by each of their components:

{% math() %}
\vec s = c \vec a = \langle c \cdot a_x, c \cdot a_y \rangle
{% end %}

The dot product of two vectors results in a scalar, and is given by:

{% math() %}
\vec a \cdot \vec b = \|a \| \|b \| \cos \phi = a_x b_x + a_y b_y
{% end %}

The cross product of two vectors results in a new vector, and is given by:

{% math() %}
\vec a \times \vec b = \| a \| \| b \|  \sin \phi = \langle a_y b_z - a_z b_y, a_z b_x - a_x b_z, a_x b_y - a_y b_x \rangle
{% end %}

To remember this formula:

- Remember that the components' subscripts are in the order $yz$, $zx$, $yx$ (e.g. $yz$ expands into $a_y b_z - a_z b_y$)
- Follow the cycle $yzx$, the first component is the $y \to z$, the second is $z \to x$, the third is $y \to x$

(to remember this, just remember the $yz, zx, yx$ pattern)

The cross product is defined only for 3D space, and is anticommutative: $\vec a \times \vec b = - (\vec b \times \vec a)$. Taking the cross product of 2D vectors requires making them 3D vectors with a z-component of zero.

The area of a parallelogram is given by the _magnitude_ of the cross product of the two vectors:

{% math() %}
A = ab \sin \theta = \| \vec a \times \vec b \|
{% end %}

## Vector kinematics

The position vector is given by $\vec s = \langle x(t), y(t), z(t) \rangle$ in Cartesian coordinates. The velocity vector is given by the derivative of position vector with respect to time. That is:

{% math() %}
\vec v = \frac{d \vec s}{dt} = \left\langle \frac{dx}{dt}, \frac{dy}{dt}, \frac{dz}{dt} \right\rangle
{% end %}

And similarly, the acceleration vector is defined by the time derivative of the velocity vector:

{% math() %}
\vec a = \frac{d \vec v}{dt} = \frac{d^2 \vec s}{dt^2} = \left \langle \frac{d^2 x}{dt^2}, \frac{d^2 y}{dt^2}, \frac{d^2 z}{dt^2} \right \rangle
{% end %}

Note that Newton's second law in vector form (for 2D or 3D) is given by a vector differential equation that expand to 4 (in 2D) or 6 (in 3D) coupled ordinary differential equations:

{% math() %}
m \frac{d^2 \vec s}{dt^2} = m\frac{d \vec v}{dt} = \vec F \left(\vec s, \frac{d\vec s}{dt}, t\right)
{% end %}

Luckily, a shift of coordinates is typically sufficient to be able to treat most 2D and 3D problems as 2D or 1D problems, reducing the need to solve such a complex vector differential equation.

**Projectile motion** (motion under constant downward acceleration) in 2D is a special case of this vector differential equation that is able to be solved analytically:

{% math() %}
m \frac{dv_x}{dt} = 0, \quad m \frac{dv_y}{dt} = -mg
{% end %}
{% math() %}
v_x (0) = v_0 \cos \theta, \quad v_y(0) = v_0 \sin (\theta)
{% end %}

The analytical solution is given by:

{% math() %}
\vec s(t) = \langle x(t), y(t) \rangle
{% end %}
{% math() %}
x(t) = x_0 + v_0 \cos (\theta) t, \quad y(t) = y_0 + v_0 \sin (\theta) t - \frac{1}{2} gt^2
{% end %}

We can find the range of a projectile (how far it travels horizontally) by solving for the value of $t$ where $y(t) = 0$ and then substituting that value of $t$ into $x(t)$. That is:

{% math() %}
y(t) = 0 \Rightarrow t = 0, t=\frac{2v_0 \sin \theta}{g}
{% end %}

The first solution is trivial (not useful) but the second is nontrivial. Substituting into $x(t)$, we have:

{% math() %}
R = x_0 + v_0 \cos \theta \left(\frac{2 v_0 \sin \theta}{g}\right) = x_0 + \frac{v_0^2 \sin (2 \theta)}{g}
{% end %}

To maximize the range $R$ given the angle $\theta$, we simply set $\frac{dR}{d\theta} = 0$ as with typical methods of optimization in calculus. From there, it can be found that the optimal angle is at $\theta = \frac{\pi}{4}$.

Lastly, it can be shown that this traces out the trajectory of a parabola. To do so, we take the two parametric equations $x(t)$ and $y(t)$ and eliminate the parameter. From this we get:


{% math() %}
y = -\frac{g}{2v_{0x}^2 } x^2 + \frac{v_{0y}}{v_{0x}}x
{% end %}

Which can be written as:

{% math() %}
y = -\frac{g}{2 v_0^2 \cos^2 \theta} x^2 + v_0 \tan (\theta) x
{% end %}

## Energy

Energy can be understood as a measure of the ability to make things happen - causing a ball to move, a plane to fly, or a star to shine. Without energy, the universe would be boring and nothing interesting would happen.

Energy (at least in non-quantum physics) comes in two main types: **kinetic energy**, which is energy that causes things to move, and **potential energy**, which is stored energy that _can_ be released to cause things to move. The total energy in a closed system is always constant.

## Work and conservation of energy

Energy can never be created nor destroyed, only transferred. Work is the transfer of energy by a force applied along a path between two points. It is a scalar quantity, and in one dimension it is defined by:

{% math() %}
W = \int_{x_0}^{x_1} F(x) dx
{% end %}

A force can release potential energy - that is, the stored energy - and transfer the released energy to objects in the form of kinetic energy. The kinetic energy gained by an object acted on by a force is equal to the work done by the force and equal to the negative of the potential energy released:

{% math() %}
W = \Delta K = -\Delta U
{% end %}

To prove this, note that force can be defined by:

{% math() %}
F = m \frac{dv}{dt}
{% end %}

We can use this alternate definition of force to obtain the work-energy theorem:

{% math() %}
\begin{align*}
W &= \int_{x_0}^{x_1} m\frac{dv}{dt} dx \\
&= \int_{x_0}^{x_1} m\frac{dv}{dt} \frac{dx}{dt} dt \\
&= \int_{x_0}^{x_1} m \frac{dv}{dt} v dt \\
&= \int_{v_0}^{v_1} mvdv \\
&= \frac{1}{2} m(v_2^2 - v_1^2) \\
&= \frac{1}{2} m \Delta v^2 \\
&= \Delta K
\end{align*}
{% end %}

If a force depends only on position, it is called a **conservative force**. Conservative forces can be written in terms of a potential energy function $U(x)$ in 1D via:

{% math() %}
F(x) = -\frac{dU}{dx}
{% end %}

Using the same method as prior to obtain the work-energy theorem, we find that:

{% math() %}
W = \int_{x_0}^{x_1} -\frac{dU}{dx} dx = -\int_{x_0}^{x_1} dU = -U(x) \bigg |_{x_0}^{x_1} = -\Delta U
{% end %}

Therefore:

{% math() %}
W = -\Delta U = \Delta K
{% end %}

Or written differently:

{% math() %}
K_1 + U_1 = K_2 + U_2
{% end %}

The total mechanical energy $E$ is conserved for conservative forces (this means it's a constant):

{% math() %}
E = K + U, \quad \frac{dE}{dt} = 0
{% end %}

> Note: for non-conservative forces such as friction, the total energy is conserved, but the total energy is not equal to the total mechanical energy.

Recall that while a conservative force can be perfectly defined by the associated potential energy, the potential energy cannot be perfectly defined by the force. This is because:

{% math() %}
U(x) = -\int F(x) dx + C
{% end %}

And therefore any $C$ could possibly be chosen. So, one often choses the constant such that the potential energy is zero at a conveniently specified location $x_0$, which we can call the "ground level" or "reference point" of the potential energy:

{% math() %}
U(x) = -\int_{x_0}^x F(x') dx'
{% end %}

For instance, consider the example of 1D constant gravity, where $F(x) = -mg$ and $U(0) = 0$, we have:

{% math() %}
U(x) = -\int_0^h F(x) dx = mgh
{% end %}

Given that $x(0) = h, v(0) = 0$, and using conservation of energy, we have:

{% math() %}
E_1 = E_2
{% end %}
{% math() %}
mgh = \frac{1}{2} mv^2 \Rightarrow v = \sqrt{2gh}
{% end %}

For the more general 1D case, we can write the conservation of energy as a differential equation, where $E$ is constant:

{% math() %}
\frac{1}{2} m \left(\frac{dx}{dt}\right)^2 + U(x) = E
{% end %}

Rearranging, we get the **separable 1st-order ODE**:

{% math() %}
\frac{dx}{dt} = \pm \sqrt{\frac{2}{m}(E - U(x))}
{% end %}

## Potential energy landscapes

By plotting the graph of $U(x)$, the potential energy function, we can determine the characteristics of the motion of an object. The following features of $U(x)$ are especially important:

- Local minimum of $U(x)$ - stable equilibrium position
- Local maximum $U(x)$ - unstable equilibrium position
- Lower potential energy regions - the object has more kinetic energy and so moves faster
- Higher potential energy regions - the object has less kinetic energy and so moves slower

## Multivariable functions and partial derivatives

Consider a multivariable function $f(x, y, z)$. How would the derivative of this function be defined? Since the function depends on multiple variables, you can differentiate with respect to each individual variable. Each derivative is known as a _partial derivative_, and is denoted as follows:

{% math() %}
\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}, \frac{\partial f}{\partial z}
{% end %}

When differentiating with respect to one variable, all the other variables are kept constant. That is, if $f(x, y) = x^2 y^3$, then when taking the partial derivative with respect to $x$, we factor out all terms in $y$ and consider them a constant:

{% math() %}
\frac{\partial f}{\partial x} = \frac{\partial}{\partial x} x^2 y^3 = y^3 \frac{\partial}{\partial x} x^2 = 2xy^3
{% end %}

Similarly, if taking the partial derivative with respect to $y$, we factor out all terms in $x$ and consider them a constant:

{% math() %}
\frac{\partial f}{\partial y} = \frac{\partial}{\partial y} x^2 y^3 = x^2 \frac{\partial}{\partial y} y^3 = 3x^2 y^2
{% end %}

The total differential of a multivariable function is given by:

{% math() %}
df = \frac{\partial f}{\partial x} dx + \frac{\partial f}{\partial y} dy + \frac{\partial f}{\partial z} dz
{% end %}

## Vector calculus

We say that the gradient of a multivariable function $f(x, y, z)$ is given by:

{% math() %}
\left(\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}, \frac{\partial f}{\partial z}\right)
{% end %}

This is often notated $\nabla f$ for "gradient of $f$", where $\nabla$ is a vector operator defined by:

{% math() %}
\nabla = \left(\frac{\partial}{\partial x}, \frac{\partial}{\partial y}, \frac{\partial}{\partial z} \right)
{% end %}

Similarly an infinitesimal displacement can be written as:
{% math() %}
d \vec s = (dx, dy, dz)
{% end %}

Using this notation:

{% math() %}
df = \nabla f \cdot d\vec s
{% end %}

There are two other vector operations of relevance in vector calculus. These operate on vector-valued multivariable functions, which are typically in the form:

{% math() %}
\vec F = \vec F(x, y, z) = \begin{bmatrix}
F_x(x, y, z) \\
F_y(x, y, z) \\
F_z(x, y, z)
\end{bmatrix} =
F_x(x, y, z) \hat i + F_y(x, y, z) \hat j + F_z (x, y, z) \hat k
{% end %}

First, the divergence operation measures flow rate, and is given by:

{% math() %}
\nabla \cdot \vec F = \left(\frac{\partial}{\partial x}, \frac{\partial}{\partial y}, \frac{\partial}{\partial z} \right) \cdot (F_x, F_y. F_z) =\frac{\partial F_x}{\partial x} + \frac{\partial F_y}{\partial y} + \frac{\partial F_z}{\partial z}
{% end %}

Second, the curl operation measures rotation, and is given by:

{% math() %}
\nabla \cdot \vec F = \left(\frac{\partial}{\partial x}, \frac{\partial}{\partial y}, \frac{\partial}{\partial z} \right) \times (F_x, F_y. F_z)  = \left(
\frac{\partial F_z}{\partial y} - \frac{\partial F_y}{\partial z},
\frac{\partial F_x}{\partial z} - \frac{\partial F_z}{\partial x},
\frac{\partial F_{y}}{\partial x}- \frac {\partial F_x}{\partial y}
\right)
{% end %}
## Work in higher dimensions

In higher dimensions, force is a vector-valued function of the position $\vec r(t)$, given as follows:

{% math() %}
\vec r(t) = x(t) \hat i + y(t) \hat j + z(t) \hat k
{% end %}

Therefore the force can generally be written in component form as:

{% math() %}
\vec F = F_x \hat i + F_y \hat j + F_z \hat k
{% end %}

Do remember that $F_x, F_y, F_z$ are each functions of $x(t), y(t), z(t)$, so this expands to:

{% math() %}
\vec F = F_x(x(t), y(t), z(t)) \hat i + F_y(x(t), y(t), z(t)) \hat j + F_z(x(t), y(t), z(t)) \hat k
{% end %}

Extending the definition of 1D work, the differential of the work in higher dimensions would be given by:

{% math() %}
dW = \vec F \cdot d\vec s
{% end %}

The force is applied along a path from $a = (x_0, y_0, z_0)$ to $b = (x_1, y_1, z_1)$ in 3D space, which we denote with $C$ (for "curve"). The total work is given by the integral of this quantity along the path, which we call a **line integral**:

{% math() %}
W = \int_{C[a \to b]} \vec F \cdot d\vec s = \int_C F_x~dx + F_y~dy + F_z~dz
{% end %}

> Note that the subscript $C[a \to b]$ under the integral is for illustrative purposes; it is optional and not required.

Line integrals can be evaluated by expanding them component-by-component:

{% math() %}
\int_C \vec F \cdot d\vec s = \int_{C(a)}^{C(b)} \vec F(x(t), y(t), z(t)) \cdot (dx, dy, dz)
{% end %}

Using the fact that:

{% math() %}
d\vec s = \frac{d\vec s}{dt} dt = (x'(t) dt, y'(t) dt, z'(t) dt) = \vec r'(t) dt
{% end %}

where $r'(t) = (x', y', z')$, line integrals can be rewritten as:

{% math() %}
\begin{align*}
& \int_C \vec F(\vec r) \cdot d\vec s \\ &= \int_{C(a)}^{C(b)} (F_x(t) x'(t)+ F_y(t) y'(t) + F_z(t) z'(t) )dt \\ &= \int_{C(a)}^{C(b)} \vec F(t) \cdot \vec r'(t) dt
\end{align*}
{% end %}

The line integral of a force (or component of a force) that is _perpendicular_ to the path along which the force is applied is zero. For instance, given a force dependent on $y$, applied on a path along the $x$ axis, the line integral - and therefore the work done - is zero.

In higher dimensions, Newton's 2nd Law can be written as:

{% math() %}
m \frac{d^2 \vec r}{dt^2} = m \frac{d \vec v}{dt} = \vec F
{% end %}

The work-energy theorem can also be expressed in higher dimensions. Using the fact that:

{% math() %}
d\vec s = \frac{d\vec s}{dt} dt = \vec v dt
{% end %}

We obtain:

{% math() %}
\begin{align*}
W &= \int_C \vec F \cdot d\vec s \\ & = \int_C m\frac{d\vec v}{dt} \cdot \frac{d\vec s}{dt} dt \\ &= \int_C m \vec v \cdot d\vec v \\ &= \frac{1}{2} m(\vec v \cdot \vec v) \bigg |_a^b \\ &= \frac{1}{2} m \Delta v^2 = \Delta K
\end{align*}
{% end %}

## Conservation of energy in higher dimensions

In higher dimensions, kinetic energy is still a scalar function, but involves derivatives in more than one dimension:

{% math() %}
K = \frac{1}{2} mv^2 = \frac{1}{2} m \left[\left( \frac{dx}{dt} \right)^2 + \left( \frac{dy}{dt} \right)^2 + \left( \frac{dz}{dt} \right)^2 \right]
{% end %}

Potential energy is also still a scalar function, but becomes multivariable:

{% math() %}
U = U(x, y, z)
{% end %}

A force $\vec F$ is called **conservative** if there is a potential energy function $U(x, y, z)$ such that:

{% math() %}
\vec F = -\nabla U = -\left(\frac{\partial U}{\partial x}, \frac{\partial U}{\partial y}, \frac{\partial U}{\partial z}\right)
{% end %}

This means that particles naturally flow from a region of higher potential energy to a region of lower potential energy. We can also write this in (line) integral form; in this form, the potential energy at $r = (x, y, z)$ defined with respect to a reference point $r_0 = (x_0, y_0, z_0)$ is given by:

{% math() %}
U(x, y, z) = -\int_{C[r_0 \to r]} \vec F \cdot d\vec s
{% end %}

For conservative forces, there are several important properties:

- The line integral of the force is independent of path
- The line integral of the force vanishes for any closed path
- $\nabla \times \vec F = 0$
- The force is uniquely determined through $\vec F = -\nabla U$

Therefore the work (in the case of conservative forces only!) can be rewritten as:

{% math() %}
\begin{align*}
W &= \int_{C[a \to b]} \vec F \cdot d\vec s \\ &= -\int_{C[a \to b]} \nabla U \cdot d\vec s \\ &= -\int_a^b dU = U(a) - U(b) = -\Delta  U
\end{align*}
{% end %}

Here we use the expression of the total differential to arrive at the prior result:

{% math() %}
\begin{align*}
\nabla U \cdot d\vec s &= \left(\frac{\partial U}{\partial x}, \frac{\partial U}{\partial y}, \frac{\partial U}{\partial z}\right) \cdot (dx, dy, dz)
\\ &= \frac{\partial U}{\partial x} dx + \frac{\partial U}{\partial y} dy + \frac{\partial U}{\partial z} dx \\ &= dU
\end{align*}
{% end %}

Equating the two equivalent definitions of work (for kinetic and potential energy respectively), we find that the work-energy theorem still holds true:

{% math() %}
\Delta K = -\Delta U
{% end %}

Or:

{% math() %}
K(b) - K(a) = U(a) - U(b)
{% end %}

Rearranging, we find that:

{% math() %}
K(a) + U(a) = K(b) + U(b)
{% end %}

Or, to generalize to the $n$-body case:

{% math() %}
\sum_i K_i(a) + \sum_i U_i (a) = \sum_i K_i(b) + \sum_i U_i (b) 
{% end %}

Therefore, total energy is conserved in the case of conservative forces, even in higher dimensions:

{% math() %}
\frac{d}{dt} (K + U) = 0
{% end %}

### Addendum: non-conservative forces

In nature, essentially all forces can be considered conservative if analyzed on the microscopic level. That is, the total energy of an object is actually an approximation for the sum of the kinetic energies and potential energies of all of its individual atoms interacting with each other (we won't go into subatomic particles because the effects of quantum mechanics make notions of energy blurry). However, it is impractical to analyze systems on the microscopic level and perform detailed calculations of millions of atoms. Therefore, we consider certain forces, such as friction, non-conservative, meaning that while total energy is conserved, total _mechanical_ energy is not. Through Helmholtz's theorem, a non-conservative force can still be written in terms of the potential energy $U$, but also must include a vector potential $\vec A$:

{% math() %}
\vec F = -\nabla U + \nabla \times \vec A
{% end %}

## Uniform circular motion

Uniform circular motion describes motion in which an object moves with constant velocity in a circular path of fixed radius. In this situation, the object does not have any tangential acceleration (acceleration along its velocity vector) but it does have **centripetal acceleration** towards the center, with a magnitude given by:
{% math() %}
a = \frac{v^2}{R}
{% end %}

Or in vector form:
{% math() %}
\vec a = -\frac{v^2}{R} \hat r
{% end %}

The object moving along the circular path would trace out a distance $ds = Rd\theta$ when it advances along an angle $d\theta$. Therefore

{% math() %}
\frac{ds}{dt} = R \frac{d\theta}{dt} \Rightarrow v =R \omega
{% end %}

The angular velocity $\omega$ can be found from differentiation of $\theta(t)$, but in the special case of uniform circular motion it can be more easily found from the period (the time it takes for the object to complete a full revolution):
{% math() %}
\omega = \frac{2\pi}{T}
{% end %}

Note that:
{% math() %}
f = \frac{1}{T}
{% end %}

In the case of non-uniform circular motion, there is both tangential and centripetal acceleration present. The tangential acceleration in this case is given by:

{% math() %}
\vec a_t = \frac{d\vec v}{dt}
{% end %}

The centripetal acceleration, however, remains the same:
{% math() %}
a_c = \frac{v^2}{R}
{% end %}

The overall acceleration $\vec a$ is given by:
{% math() %}
\vec a = \vec a_t + \vec a_c
{% end %}

When considering problems of circular motion, instead of using $\sum F_i = ma$, instead use $\sum F_i = \frac{mv^2}{R}$. The centripetal force is not an isolated force, but is rather the net force in the radial direction, and the forces that provide it are other forces, such as gravitational force and normal force.

### Example cases of circular motion

Consider a bead of mass $m$ attached to a string and is revolving in a circular fashion. We can decompose the forces into vertical and horizontal components. Using Newton's second law, the horizontal net force is given only by the radial tension force $\vec T$. Therefore, considering the magnitudes of the forces only:

{% math() %}
m a_c = m\frac{v^2}{R}=  T
{% end %}

Meanwhile, the vertical net force depends on the location of the bead. At the very top of the circle, then:

{% math() %}
m a_c = m\frac{v^2}{R} = T + mg
{% end %}

At the very bottom of the circle, then:

{% math() %}
m a_c = m\frac{v^2}{R} = T - mg
{% end %}

At the leftmost and rightmost edges of the circle, then:

{% math() %}
m a_c = m\frac{v^2}{R} = T
{% end %}
## Newton's theory of gravity

In Newtonian mechanics, the gravitational force between two masses $M$ and $m$ is given by:

{% math() %}
\vec F_g = -\frac{GMm}{r^2} \hat r
{% end %}

The magnitude of the gravitational force is given by:

{% math() %}
F_g = \|F_g\| = \frac{GMm}{r^2}
{% end %}

### Perfectly circular orbits

The simplest case of planetary motion can be modeled with uniform circular motion, that is, equating centripetal force and the gravitational force:

{% math() %}
m\frac{v^2}{R} = G \frac{Mm}{r^2}
{% end %}

Solving for $v$, we have:
{% math() %}
v = \sqrt{\frac{GM}{r}}
{% end %}

And the orbital period $T$ is given by:

{% math() %}
T = 2\pi \sqrt{\frac{r^3}{GM}}
{% end %}

This is often rewritten as:

{% math() %}
T^2 = \frac{4\pi^2 r^3}{GM}
{% end %}

### Newton's shell theorem

Newton found that a uniformly dense thin spherical shell attracts an external particle identically to a point mass. In addition, a particle _inside_ such a shell would feel no gravitational force. This is often called **Newton's shell theorem**.

Using the shell theorem, we can divide a solid sphere of radius $R$ and mass $M$ into infinitely many infinitesimally-thin shells, and apply the shell theorem additively for each. Therefore we find again that the sphere attracts an external particle identically to a point mass. A particle inside such a sphere at a radius $r$ would feel a gravitational force that comes only from the amount of mass underneath the particle (that is, within $r$). 

To compute the value of this force, we want to first find the amount of mass inside a radius $r$. Given $dm = \rho dV$, and $dV = 4\pi r^2 dr$, we can say that:

{% math() %}
M(r) = \int_0^r dm = \int_0^r 4\pi (r')^2\rho(r') dr
{% end %}

where we relabel from $r \to r'$ in the integrand to avoid confusing integration bounds and variables. This results in a linear force inside the spherical mass given by:
{% math() %}
F = \frac{GMm}{R^3} r
{% end %}

Therefore given the spherical mass $M$ of radius $R$, the magnitude of the gravitational force $F$ is a piecewise function:

{% math() %}
F = 
\begin{cases}
\frac{GMm}{r^2}, & r > R \\
\frac{GMm}{R^3}r, & r < R \\
\end{cases}
{% end %}

### Gravitational potential energy

The gravitational potential energy, like any potential energy for a conservative force, is given by the negative work (work done against the force of gravity) to bring a mass to its position $r$:

{% math() %}
U = -\int_{C[r_0 \to r]} \vec F \cdot d\vec s
{% end %}

More precisely, this negative work is done along a path from a reference point $r_0$ to the object's current position $r$, where we choose the reference point such that $U(r_0) = 0$. Previously, this reference point was often assumed to be the ground - that is, $U = 0$ when $y = 0$. In the case of generalized gravitation, we choose a point infinitely far away as the reference point for the gravitational potential energy (that is, $U = 0$ at $r = \infty$). Therefore, the line integral simplifies to:

{% math() %}
U(r) = -\int_\infty^r -\frac{GMm}{{r'}^2} dr' = -\frac{GMm}{r}
{% end %}

This can be approximated for objects near the Earth as:

{% math() %}
U(y) \approx mgy
{% end %}

### Gravitational total energy

The total energy in gravitation is given by:

{% math() %}
E = K + U = \frac{1}{2} mv^2 -\frac{GMm}{r}
{% end %}

$E$ must be less than zero for an object to remain in orbit. Solving for $v$ in the case $E \geq 0$, we find that the **escape velocity** of an object in orbit is given by:

{% math() %}
v_{\mathrm{esc}} = \sqrt{\frac{2GM}{r}}
{% end %}

## Angular momentum

Newton's second law can be formulated in terms of momentum $\vec p$:

{% math() %}
F = \frac{d\vec p}{dt}
{% end %}

However, for radial problems, it is often more helpful to formulate Newton's second law in terms of _angular momentum_ $\vec L$, defined:
{% math() %}
\vec L = \vec r \times \vec p
{% end %}

In this case, Newton's second law becomes the equation for **torque** $\vec \tau$, the radial equivalent of force:

{% math() %}
\vec \tau = \frac{d\vec L}{dt} = \vec r \times \vec F
{% end %}

> Note that torque is covered more in-depth in the section on rotational motion.

## Kepler's laws

1. Each planet moves in an elliptical orbit described by the parameters $a$ and $b$
2. A line from the Sun to a given planet sweeps out equal areas in equal times
3. The square of the period of the orbit is proportional to the cube of $a$

Kepler's first law means that the orbits of planets follow the equation of an ellipse:

{% math() %}
\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1
{% end %}

Here, $a$ is the semi-major axis, which is half the distance across the longer diameter of the ellipse. $b$ is the semi-minor axis, which is half the distance across the shorter diameter of the ellipse. 

![Image of an ellipse, showing the semi-major and semi-minor axes](https://upload.wikimedia.org/wikipedia/commons/9/96/Ellipse-def0.svg)

(Credit: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Ellipse-def0.svg))

For gravitational orbits, the values of $a$ and $b$ are given by:

{% math() %}
a = \frac{GMm}{2|E|}
{% end %}
{% math() %}
b = \frac{L}{\sqrt{2m|E|}}
{% end %}

Kepler's second law is due to the fact that as the gravitational force and angular momentum are parallel vectors, their cross product is zero, and thus angular momentum is conserved.

Kepler's third law was proven earlier in the case of perfectly circular orbits. For an improved generalization that extends to elliptical orbits, the relationship is given by:

{% math() %}
T^2 = \sqrt{\frac{4\pi^2 a^3}{GM}}
{% end %}

## Mathematical interlude: Taylor series

A function can be approximated near a point $x_0$ via:

{% math() %}
f(x) \approx f(x_0) + f'(x_0)(x - x_0) + \frac{1}{2} (x - x_0)^2 + \dots
{% end %}

If infinite terms are used, then the function can be _exactly_ represented by its approximation:
{% math() %}
f(x) = \sum_{n = 0}^\infty \frac{f^{(n)}(x_0)}{n!}(x - x_0)^n
{% end %}

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

{% math() %}
F_g = \frac{GMm}{r_E^2} -\frac{GMm}{r_E^3} (r - r_E) + \frac{GMm}{2r_E^4} (r-r_E)^2 + \dots
{% end %}

If we define $g = \frac{GM}{r_E^2}$, then to the first term of the Taylor expansion, we have:

{% math() %}
F_g = mg
{% end %}

## Complex numbers

The **imaginary unit** is defined by $i = \sqrt{-1}$. Complex numbers are made of a real part and an imaginary part, and are written with $z = a + bi$. Complex numbers can also be represented in polar coordinates, where the magnitude $\|z\| = \sqrt{a^2 + b^2}$ and they can be written as $z = \|z\| \cos \phi + \|z\| i \sin \phi$. The complex conjugation is given by $z^\*$ where if $z = a + bi$, then $z^\* = a - bi$, and there is the special property $z \cdot z^* = a^2 + b^2$.

Using Euler's formula, we can extend the exponential function to the complex plane:
{% math() %}
e^z = e^a(\cos b + i \sin b)
{% end %}

If we let $a = 0$ and $b = i\phi$, then it simplifies to:

{% math() %}
e^{i\phi} = \cos \phi + i \sin \phi
{% end %}

Therefore, any complex number can be written in the form:

{% math() %}
z = \|z\| e^{i\phi}
{% end %}

And the trigonometric functions can be written in terms of exponentials:

{% math() %}
\cos \phi = \frac{e^{i\phi} + e^{-i\phi}}{2}, \quad \sin \phi = \frac{e^{i\phi} - e^{-i\phi}}{2i}
{% end %}
## Small oscillators and the simple harmonic oscillators

Newton's second law can be written in the form:
{% math() %}
m\frac{d^2 x}{dt^2} =-\frac{dU}{dx}
{% end %}

Around a certain point $x_0$, the Taylor expansion of the potential energy around that point is given by:

{% math() %}
U(x) = U_0 + U'(x_0)(x - x_0) + \frac{1}{2} U''(x_0)(x - x_0)^2 + \frac{1}{6} U'''(x_0) (x - x_0)^3 + \dots
{% end %}

When a system only slightly deviates from equilibrium (that is, it is at a point close to a local minimum of the potential energy), the Taylor expansion to first-order is given by:

{% math() %}
U(x) \approx U_0 + U'(x_0) (x - x_0) + \frac{1}{2} U''(x_0)(x - x_0)^2
{% end %}

Therefore:

{% math() %}
\frac{dU}{dx} = U'(x_0) + U''(x_0) (x-x_0)
{% end %}

Given that the system is very close to its local minimum, the first derivative $U'$ at $x_0$ vanishes as well, so:

{% math() %}
\frac{dU}{dx} = U''(x_0) (x - x_0)
{% end %}

If we set $k = U''(x_0)$ and perform the change of variables $y = x - x_0$ then Newton's second law is approximately:

{% math() %}
m\frac{d^2 y}{dt^2} = -ky
{% end %}

Which can be written as:

{% math() %}
\frac{d^2 y}{dt^2} + \frac{k}{m}y = 0
{% end %}

Or, with $\omega = \sqrt{\frac{k}{m}}$, we have:

{% math() %}
\frac{d^2 y}{dt^2} + \omega^2 y = 0
{% end %}

Which has the exact general solution:

{% math() %}
y = A e^{i \omega t} + Be^{-i\omega t}
{% end %}

Using Euler's formula we can rewrite as:

{% math() %}
y = C_1 \cos \omega t + C_2 \sin \omega t
{% end %}

Examples of systems described in this form include the simple pendulum equation:
{% math() %}
\frac{d^2 \theta}{dt^2} + \frac{g}{L} \theta = 0
{% end %}

## Oscillators

Oscillators are a very important system in physics because, as mentioned previously, many systems from classical and even quantum mechanics can be approximated as a (oftentimes coupled) system of oscillators. In regions close to a potential well, a particle typically oscillates back and forth about the potential well, 

### The damped oscillator

A dampening force (such as drag) can be added to more realistically model an oscillator. A good approximation for the dampening force is a force proportional to velocity, such as $F_d = -bv$. Then Newton's second law becomes:

{% math() %}
m\frac{d^2 x}{dt^2} = -kx - bv
{% end %}

Since $v = dx/dt$, we can rewrite this equation as:

{% math() %}
\frac{d^2 x}{dt^2} + \frac{b}{m} \frac{dx}{dt} + \frac{k}{m} x = 0
{% end %}

If we let $\omega_0^2 = k / m$ and $\beta = b / 2m$, then the differential equation becomes:

{% math() %}
\frac{d^2 x}{dt^2} + 2\beta \frac{dx}{dt} + \omega_0^2 x = 0
{% end %}

This equation is a 2nd-order homogeneous differential equation. The solution of this differential equation is given by three cases:

- $\beta > \omega_0$ is the case of over-dampening, which tends to an exponential decay with a general solution of $x(t) = Ae^{-\beta t + \sqrt{\beta^2 - \omega_0^2} t} + Be^{-\beta t - \sqrt{\beta^2 - \omega_0^2}t}$
- $\beta = \omega_0$ is the case of critical-dampening, which also tends to an exponential decay with a general solution $x(t) = (At + B)e^{-\beta t}$
- $\beta < \omega_0$ is the case of under-dampening (or weak dampening), which leads to a slow decay with the general solution of $x(t) = Ae^{-\beta t} \cos (\sqrt{\omega_0^2 - \beta^2} t + \phi)$

### Driven damped harmonic oscillators

A driven harmonic oscillator adds a a driving force in addition to a dampening force to the model of an oscillator. Such a driving force could be in the form $F = F_0 \cos \omega t$ (here note that $\omega$ is not the same as $\omega_0$). Therefore, the differential equation becomes:

{% math() %}
m\frac{d^2 x}{dt^2} = -kx - bv + F_0 \cos (\omega t)
{% end %}

Which we can rearrange to obtain:

{% math() %}
\frac{d^2 x}{dt^2} + 2\beta \frac{dx}{dt} + \omega_0^2 x = \frac{F_0}{m} \cos (\omega t)
{% end %}

This equation is still a 2nd-order differential equation, but it is now _inhomogeneous_. The solution to this equation is given by:

{% math() %}
x(t) = x_H(t) + D(\omega) \cos(\omega t - \delta(\omega))
{% end %}

Where:
{% math() %}
D(\omega) = \frac{F_0}{m} \frac{1}{\sqrt{(\omega_0^2 - \omega^2)^2 + 4\beta^2 \omega^2}}
{% end %}
{% math() %}
\delta(\omega) = \tan^{-1} \left(\frac{2\beta \omega}{\omega_0^2 - \omega^2}\right)
{% end %}

And $x_H(t)$ is the general solution of the dampened harmonic oscillator for the given $\beta$ and $\omega_0$. For instance, for a weak-dampening driven harmonic oscillator, then the general solution is:

{% math() %}
x(t) = Ae^{-\beta t} \cos (\sqrt{\omega_0^2 - \beta^2} t + \phi) + D(\omega) \cos(\omega t - \delta(\omega))
{% end %}

Typically, as $t \to \infty$, $x_H(t)$ decays exponentially, so $x_H(t) \approx 0$ and only the driving force (also called "transient") part of the solution remains.

Unlike purely dampened or simple harmonic oscillators, driven damped oscillators have the phenomena of **resonance**. This is the idea that $D(\omega)$ can be _tuned_ to maximize its value and thereby maximize the amplitude. As a paraphrased example from _Waves: An Interactive Tutorial_ by Forinash and Christian, an example is a sound wave tuned with a value of $\omega$ that maximizes its amplitude sufficient break a wine glass.

### Applied harmonic oscillators

A LRC circuit is an oscillating system which is described by a very similar differential equation:

{% math() %}
L \frac{d^2 Q}{dt^2} + R \frac{dQ}{dt} + \frac{Q(t)}{C} = \mathcal{E}_0 \cos \omega t
{% end %}

Here, we can cast the differential equation into the general form of a harmonic oscillator by using $\beta = R / 2L$ and $\omega_0^2 = \frac{1}{LC}$. This can be readily solved using the same method as the harmonic oscillator.

## Momentum and Impulse

**Momentum** is a measure of how much an object is moving. More massive and faster objects have a greater momentum, whereas less massive and slower objects have a lesser momentum. We define an object's momentum along the object's trajectory by $\vec p = m\vec v$. Newton's 2nd law can be formulated (and indeed, was originally formulated) in terms of momentum:

{% math() %}
\vec F_\mathrm{net} = \frac{d\vec p}{dt}
{% end %}

**Impulse** is the change in an object's motion produced by a net force acting over a time interval. In mathematical terms, it is the time integral of force. Given that $dp = \vec F dt$, we can integrate over time to get the **impulse**:

{% math() %}
J = \int_{t_0}^{t_1} \vec F~dt = \Delta p
{% end %}

Newton's 3rd law states that:

{% math() %}
\vec F_{12} = -\vec F_{21}
{% end %}

If we combine the definitions of impulse and Newton's 3rd law:

{% math() %}
\Delta \vec p_1 = \int_{t_0}^{t_1} \vec F_{12}~dt = \int_{t_0}^{t_1} (-\vec F_{21})~dt = -\int_{t_0}^{t_1} \vec F_{21}~dt = -\Delta \vec p_2
{% end %}

We arrive at the **conservation of momentum**, which states that momentum is conserved in a closed system (with no external forces):

{% math() %}
\Delta \vec p_1 = -\Delta \vec p_2
{% end %}

If there are external forces present in a system, then the total momentum evolves as:

{% math() %}
\frac{d \vec P}{dt} = \sum_i \vec F_\mathrm{ext}
{% end %}

Where the total momentum can be determined by:

{% math() %}
\vec P = \sum_i m_i \vec v_i = m_1 \vec v_1 + m_2 \vec v_2 + \dots + m_n \vec v_n
{% end %}

## Collisions

The conservation of momentum is readily applied to _collision_ problems in physics, whether that be a billiard ball shot toward another, a neutron colliding into an atomic nucleus, or even a close gravitational encounter. Collisions typically take one of the following forms:

- Elastic collisions are collisions where momentum and energy are conserved, or informally where the two colliding objects are deflected from each other and move apart from each other with different velocities after the collision
- Inelastic collisions are collisions where only momentum is conserved, or informally, where there is loss in total mechanical energy to heat, light, or sound
- Perfectly inealstic collisions are collisions where the total mechanical energy is entirely dissipated after the collision, or informally when the two colliding objects stick together and move together with the same velocity after the collision

> Note: when two objects are said to have different _velocities_, that doesn't mean they have the same speed, as two different velocities with the same magnitude can have opposite directions.

Most collisions, at least on a non-atomic level, are inelastic, dissipating some but not all of their initial total mechanical energy during the collision. However, when the loss is small enough to be considered negligible, collisions can be modelled as elastic, and when the loss is sufficiently large as to be considered total, collisions can be modelled as perfectly inelastic.

### Elastic case

In an elastic collision, the final velocities of the colliding objects are **completely determined** by the initial velocities and masses of the two colliding objects. That is, given initial velocities $v_1(a)$ and $v_2(a)$ and initial masses $m_1$ and $m_2$, we can find the final velocities $v_1(b)$ and $v_2(b)$. 

Both energy and momentum are conserved in elastic collisions. Conservation of energy and momentum together give:

{% math() %}
\sum_i K_i(a) + \sum_i U_i(a) = \sum_i K_i(b) + \sum_i U_i(b)
{% end %}
{% math() %}
\sum_i p_i(a) = \sum_i p_i(b)
{% end %}

> **A note about conservation of total mechanical energy:** elastic collisions are idealizations, because most collisions do end up generating heat, light, sound, or radiate away some of their total mechanical energy otherwise. Thus, while total _energy_ is conserved in all collisions, total _mechanical energy_ - that is, the sum of the kinetic and potential energies of all objects in a system - typically is not. 

The higher dimensional generalization can be written in vector form:

{% math() %}
\sum_i \mathbf{P}_i(a) = \sum_i \mathbf{P}_i(b)
{% end %}

Which yields three separate equations for each component:

{% math() %}
\begin{align*}
\sum_i P_{i, x}(a) = \sum_i P_{i, x}(b) \\
\sum_i P_{i, y}(a) = \sum_i P_{i, y}(b) \\
\sum_i P_{i, z}(a) = \sum_i P_{i, z}(b)
\end{align*}
{% end %}

A general form can be found in the case of a two-body system of two masses $m_1$ and $m_2$. When the collision between the two bodies results in a negligible change in their respective potential energies, or where any increase in potential energy during the collision is immediately released back as kinetic energy afterwards, we can ignore the potential energy terms in the conservation of energy equation. Therefore, the resulting system of conservation equations becomes:

{% math() %}
\frac{1}{2} m_1 v_1(a)^2 + \frac{1}{2} m_2 v_2(a)^2 = \frac{1}{2} m_1 v_1(b)^2 + \frac{1}{2} m_2 v_2(b)^2 
{% end %}
{% math() %}
m_1 v_1(a) + m_2 v_2(a) = m_1 v_1(b) + m_2 v_2(b)
{% end %}

The solution to this system of equations is given by:

{% math() %}
v_1(b) = \frac{2m_2 v_2(a)}{m_1 + m_2} + v_1(a) \frac{m_1 - m_2}{m_1 + m_2}
{% end %}
{% math() %}
v_2(b) = \frac{2m_1 v_1(a)}{m_1 + m_2} + v_2(a) \frac{m_2 - m_1}{m_1 + m_2}
{% end %}

A full derivation is given [here](@/collision-derivations.md).

### Perfectly inelastic case

In a perfectly inelastic collision, the final velocities of the two colliding objects are the same, and is also **completely determined** by the initial velocities and masses. For two bodies of masses $m_1$ and $m_2$, conservation of momentum takes the form of the following equation, where $v_\mathrm{after}$ is the final velocity of both bodies after the collision:

{% math() %}
m_1 v_1(a) + m_2 v_2(a) = (m_1 + m_2)v_\mathrm{after}
{% end %}

### Ballistic pendulum

A ballistic pendulum is a device consisting of a wooden block of mass $M$ hanging from two sets of strings. When a projectile (for instance, a bullet) of mass $m$ and velocity $v_1$ is shot into the wooden block, the collision between the projectile and the block is a _perfectly inelastic_ collision where only conservation of momentum applies:

{% math() %}
mv_1 + M(0) = (m + M)v
{% end %}

Afterwards, the project and block move upwards together, causing the pendulum swings up by distance $h$. As this is separate from the prior collision, energy conservation can be applied in this case:

{% math() %}
\frac{1}{2} (m + M)v^2 = (m + M)gh
{% end %}

Solving the system of equations, we can obtain the speed $v_1$ of the projectile from only knowing the masses $M$ and $m$ (of the block and bullet respectively) and the height $h$ by which the pendulum swung upwards:

{% math() %}
v_1 = \frac{m + M}{m} \sqrt{2gh} 
{% end %}

## Center of mass

A system of many bodies can often be analyzed more simply as an equivalent single body whose mass $M$ is equal to the sum of the masses of the constituent bodies $m_1, m_2, \dots, m_n$, and whose position is at the center of mass of the body $\vec r_{CM}$. The expressions for the total mass $M$ and the center of mass $\vec r_{CM}$ are given by:

{% math() %}
M = \sum_i m_i
{% end %}

{% math() %}
\vec r_{CM} = \frac{\displaystyle \sum \nolimits_i m_i \vec r_i}{\displaystyle \sum \nolimits_i m_i} = \frac{1}{M} \sum_i m_i \vec r_i
{% end %}

An extended body can be considered a system of all its individual atoms, and therefore a many-body system as well. For the case of extended bodies, however, we compute the total mass and center of mass over a continuum of values, and therefore the expression for the center of mass becomes an integral. The general expressions of a single extended body's mass $M$ and center of mass $r_{CM}$ are:

{% math() %}
M = \int dm
{% end %}

{% math() %}
r_{CM} = \frac{1}{M} \int rdm
{% end %}

As $dm$ can be written in terms of density functions, the general expressions expand to specific integrals in different dimensions:

| Dimension | Expression for density function | Expression for total mass $M$ | Expression for center of mass $\vec r_{CM}$ |
|-----|-----|-----|----|
| 1D | Linear density $\lambda(x)$ | $\displaystyle \int_{L_1}^{L_2} \lambda(x)~dx$ | $\displaystyle \frac{1}{M} \int_{L_1}^{L_2} x\lambda(x)~dx$ |
| 2D | Surface density $\sigma(\vec r)$ | $\displaystyle \iint_\Sigma \sigma(\vec r)~dA$ | $\displaystyle \frac{1}{M} \iint_\Sigma \vec r \sigma(\vec r)~dA$ |
| 3D | Volume density $\rho(\vec r)$ | $\displaystyle \iiint_\Omega \rho(\vec r)~dV$ | $\displaystyle \frac{1}{M} \iiint_\Omega \vec r \rho(\vec r)~dV$ |

Symmetries can be used to rewrite higher-dimensional integrals in terms of one-dimension integrals. For instance, for a sphere, $dV = 4\pi r^2~dr$, so the multivariable integral becomes just a single-variable integral.

## Rigid body motion

Rigid body motion occurs for bodies that move in rotational as well as translational (straight-line) motion. Consider a rotating rigid body a distance $r$ from its axis of rotation. Then its tangential velocity is given by:

{% math() %}
ds = rd\phi \Rightarrow v = \frac{ds}{dt} = r\frac{d\phi}{dt} = r \omega
{% end %}

Therefore, rotational motion can be entirely characterized by the object's angle as a function of time $\phi(t)$. The angle can be used to derive both angular velocity $\omega$ and angular acceleration $\alpha$:

{% math() %}
\omega(t) = \frac{d\phi}{dt}
{% end %}

{% math() %}
\alpha(t) = \frac{d\omega}{dt} = \frac{d^2 \phi}{dt^2}
{% end %}

Note that $\alpha(t)$ can also be written as:

{% math() %}
\alpha(t) = \omega v = \omega^2 r = \frac{v^2}{r}
{% end %}

In cases of constant angular acceleration, then the following kinematic equations result from straightforward integration:

{% math() %}
\omega(t) = \omega_0 + \alpha t
{% end %}

{% math() %}
\phi(t) = \phi_0 + \omega_0 t + \frac{1}{2} \alpha t^2
{% end %}

### Vector representations of rotations

Rotations in higher dimensions can be represented with vectors. That is, a rotation about the $x$, $y$, and $z$ axes respectively can be represented as:

{% math() %}
\vec \phi = (\phi_x, \phi_y, \phi_z)
{% end %}

Therefore, the angular velocity $\vec \omega$ and angular acceleration $\alpha$ are also both vector quantities in higher dimensions. The expression for the tangential velocity $\vec v$ also becomes a cross product:

{% math() %}
\vec v = \omega \times \vec r
{% end %}

The direction of the angular velocity can be found through the right-hand rule. Aligning the fingers to point along the direction of the object's rotation (clockwise or counterclockwise), the thumb would point in the direction of $\vec \omega$.

The tangential acceleration in vector form is given by:

{% math() %}
\vec a_\mathrm{tan} = \frac{d\vec v}{dt} = \vec \alpha \times \vec r
{% end %}

And the radial acceleration in vector form is given by:

{% math() %}
\vec \alpha_\mathrm{rad} = \frac{d\vec \omega}{dt} = \vec \omega \times \vec v = \vec \omega \times (\omega \times \vec r)
{% end %}

The total acceleration of a rigid body is the combination of its tangential and radial acceleration:

{% math() %}
\vec a = \vec a_\mathrm{tan} + \vec \alpha_\mathrm{rad} = \vec a \times \vec r + \vec \omega \times \vec r
{% end %}

## Torque

The **torque** is the rotational equivalent of linear force, akin to a measure of twisting of a rotating body, and is given by:

{% math() %}
\tau = \vec r \times \vec F
{% end %}

The magnitude of the torque is given by:

{% math() %}
\\| \tau \\| = rF\sin \theta
{% end %}

Here, $\theta$ is measured counter-clockwise. An angle measured clockwise between $\vec r$ and $\vec F$ would be equivalent to an angle of $-\theta$.

For a rigid body of total mass $m$, the total external gravitational torque for uniform $\vec g$ is given by:

{% math() %}
\vec \tau = \vec r_{CM} \times m \vec g
{% end %}

where $\vec r_{CM}$ is its center of mass.

### 1D rotational equations of motion

For a particle undergoing a net force $\vec F_\perp$ perpendicular to its radial vector $\vec r$, then Newton's 2nd law gives:

{% math() %}
m \vec a_\mathrm{tan} = \vec F_\perp
{% end %}

This can also be rewritten as:

{% math() %}
\tau_\mathrm{net} = \sum_i \tau_i = I\alpha
{% end %}

Where $I$ is the moment of inertia, the rotational equivalent of mass, given by:

{% math() %}
I = \sum_i m_i r_i^2
{% end %}

Often, the axis of rotation (which runs through the center of mass) is not always The moment of inertia of the body can be found through any arbitrary coordinate system with its origin $\vec h$ from the center of mass of the body by the **parallel-axis theorem**:

{% math() %}
I = I_{CM} + mh^2
{% end %}

For a continuous rigid body of non-uniform density, then the moment of inertia is given by:

{% math() %}
I = \int m r^2~dm = \iiint r^2 \rho~dV
{% end %}

As an example, for a rod of length $L$, mass $M$, and linear mass density $\lambda = \frac{M}{L}$, then $dm = \lambda dx$ and the moment of inertia about an axis that runs through its left end (that is, where $x = 0$) is given by:

{% math() %}
I = \int m r^2 dm = \int_0^L x^2 \lambda dx = \int_0^L x^2 \frac{M}{L} dx = \frac{1}{3} ML^2
{% end %}

The parallel-axis theorem can be used to derive its moment of inertia at its center of mass (where $x = L/2$):

{% math() %}
I_{CM} = I - Mh^2 = I - M\left(\frac{L}{2}\right)^2 = \frac{1}{12} ML^2
{% end %}

## Rigid body dynamics

A rigid body is a body that does not deform under motion; while rigid bodies are an idealization, many objects that do not deform much under motion can be approximately modelled by rigid bodies. Motion can always be decomposed into the translational motion of the center of mass and rotational motion about the center of mass:

{% math() %}
M\vec a_{CM} = M \frac{d \vec v_{CM}}{dt} = \sum_i \vec F_i
{% end %}

{% math() %}
I \vec \alpha_{CM} = I_{CM} \frac{d \vec \omega}{dt} = \sum_i \tau_i
{% end %}

Rigid body dynamics may have the condition of slipping. An object is formally said to be slipping if its motion follows the property:

{% math() %}
v_{CM} - R\omega = 0
{% end %}

### Kinetic dynamics

{% math() %}
K = \frac{1}{2} I \omega^2
{% end %}

> More will be added soon.


## Fluid mechanics

Fluids are any substances that can flow and change shape. They include both liquids and gases (but also include other substances, such as plasmas). Fluids are not characterized by their mass, but rather by their **density**. A fluid's density $\rho$ is defined by:
{% math() %}
\rho(x, y, z) = \frac{dm}{dV}
{% end %}

The density of many fluids can vary. However, liquids in particular are typically _incompressible_, that is, $\rho = \text{const.}$

### Fluid pressure

Like solids, fluids can be acted on by forces. However, unlike solids, fluids distribute force across a continuum, and thus the fluid equivalent of force is **pressure**. The pressure $P$ of a fluid is defined as:

{% math() %}
P = \frac{dF}{dA}
{% end %}
> Note that one **pascal** is equal to $\pu{1 N/m^2}$ and is the standard unit for pressure.

Fluid pressure in a single dimension is described by the differential equation:
{% math() %}
\frac{dP}{dy} = -\rho(y) g
{% end %}

For incompressible fluids, $\rho = C$ and thus:

{% math() %}
P(y) = P_0 + \rho g(y_0 - y)
{% end %}

For other fluids, such as air in the atmosphere, a good approximation is $\rho(y) = cP(y)$. That is:

{% math() %}
\frac{dp}{dy} = -kPg
{% end %}

The solution to this differential equation is:

{% math() %}
P(y) = P_0 e^{-kgy} = P_e e^{-y/a}
{% end %}

Where $a = \frac{P_0}{\rho_0 g}$. This pressure function is used in the barometric formula for atmospheric pressure, where in this case $a \approx \pu{8,500 m}$ and $P_0 = \pu{1.01e5 Pa}$.

### Pascal's law

Fluids aren't only able to be acted on by forces, they can also transmit forces. In fact, their incompressible nature makes them highly desirable for this purpose, as used in applications such as hydraulic lifts. **Pascal's Law** states that at constant height, fluid pressure is identical at all points in the fluid:

{% math() %}
P_1 = P_2 \Rightarrow \frac{F_1}{A_1} = \frac{F_2}{A_2}
{% end %}

That is, with $h = \text{const}$, if a force $F_1$ is applied to a fluid along a surface of area $A_1$, then the fluid exerts a force of $F_2$ on any surface of $A_2$ it touches.

### Archimedes' principle

When an object is immersed in a fluid, the fluid exerts an upward **buoyant force** on the object given by:
{% math() %}
F_B = \rho V_\mathrm{disp}g = \rho V_\mathrm{im}g
{% end %}

Where $\rho$ is the fluid's density, $V_\mathrm{disp}$ is the displaced volume of fluid, and $V_\mathrm{im}$ is the submerged volume of the immersed object. Notice that the buoyant force does **not** depend on the immersed object's mass at all!

### Fluid flow

Previously, all examples applied only to fluid statics; fluids that are unchanging in time. For fluids that do change in time - that is, fluids that flow - fluid dynamics is necessary.

For an ideal fluid that is steady, non-viscous, and irrotational, then the _equation of continuity_ applies:

{% math() %}
\rho_1 A_1 v_1 = \rho_2 A_2 v_2
{% end %}

If the fluid is also incompressible, then the equation of continuity simplifies to:

{% math() %}
A_1 v_1 = A_2 v_2
{% end %}

By these definitions, the mass flow rate is a constant given by:

{% math() %}
\frac{dm}{dt} = \rho Av
{% end %}

And the volume flow rate is a constant given by:

{% math() %}
\frac{dV}{dt} = Av
{% end %}

### Bernoulli's equation

For incompressible ideal fluid (i.e. no turbulence, constant density), then **Bernoulli's equation** applies:

{% math() %}
\Delta P + \frac{1}{2} \rho (v_2^2 - v_1^2) + \rho g\Delta y = 0
{% end %}

Where $\Delta P$ is the difference in pressure between the fluid measured at two points, $\Delta y$ is the difference in height between those points, and $v_1, v_2$ are the fluid's respective velocities at those points.

> Note: for fluids that are exposed to the atmosphere, such as a glass of water left on a table, all points where the fluid is in contact with the air have the _same_ pressure of $\pu{1 atm}$. For a fluid whose surface is level and unchanging, then at that point $v = 0$.

## Fields

A field is a model for a quantity spread out over space with a measurable value at each point. Fields can be scalar fields - e.g. a temperature field, like $T(r, t)$ - or vector fields - e.g. a velocity field, like $\mathbf{v}(r, t)$. They are used to model phenomena ranging from electromagnetism to gravity to fluid flow to plasma confinement.

### Addenum: integral notations

We encountered line integrals previously, as well as integrals over areas and volumes. We notated scalar and vector line integrals respectively with:

{% math() %}
\int_C f(x, y, z)~d\ell \quad \text{and} \quad \int_C \mathbf{F} \cdot \mathbf{d\ell}
{% end %}

We will now properly define names for integrals over areas and volumes. An _area integral_ is notated:

{% math() %}
\iint f(x, y)~dA
{% end %}

Meanwhile, a _volume integral_ is notated:

{% math() %}
\iiint f(x, y, z)~dV
{% end %}

In some cases, symmetries allow area and volume integrals to be evaluated without needing to integrate. However, in nontrivial cases, area integrals can be evaluated using double integrals, and volume integrals can be evaluated using triple integrals, though that will not be covered here.

### Flux

Flux is a measure of the flow of a field. Typically, this flow is measured with respect to an imaginary surface $\Sigma$ that encloses some part of the field.

{% math() %}
\phi = \iint_\Sigma \mathbf{v} \cdot d\mathbf{S}
{% end %}

For relatively constant fields, the flux simplifies to:

{% math() %}
\phi = S \mathbf{v} \cos \theta 
{% end %}

Where $S$ is the surface area of the surface.

In addition, if the flux is over a _closed_ surface, then the flux is notated:

{% math() %}
\phi = \oiint_\Sigma \mathbf{v} \cdot d\mathbf{A}
{% end %}

### Gauss's theorem (divergence theorem)

Gauss's theorem states that the flux of a vector field over a surface is equal to the volume integral of its divergence:

{% math() %}
\oiint_\Sigma \mathbf{v} \cdot d\mathbf{A} = \iiint \nabla \cdot \mathbf{v}~dV
{% end %}

The general idea is that integrating over the divergence of a vector field results in the divergence on all the interior points of a surface to cancel out. Therefore, the remaining divergence is located only at the surface, resulting in the flux.

## The continuity equation

The mass flow rate of a fluid with velocity field $\mathbf{v}$ and density $\rho(r, t)$ into a region is given by:

{% math() %}
\frac{dm}{dt}_\mathrm{in} = \frac{d}{dt} \iiint \rho(r, t)~dV
{% end %}

The mass flow rate of a fluid out of a region is given by:

{% math() %}
\frac{dm}{dt}_\mathrm{out} = -\oiint \rho \mathbf{v} \cdot d\mathbf{S}
{% end %}

If we define a new vector field $\mathbf{J}$ from the velocity field:

{% math() %}
\mathbf{J} = \rho \mathbf{v}
{% end %}

Then:

{% math() %}
\frac{dm}{dt}_\mathrm{out} = -\oiint \mathbf{J} \cdot d\mathbf{S}
{% end %}

By conservation of mass, the mass flow rate into and out of a region must be exactly equal. Therefore:

{% math() %}
\frac{dm}{dt}_\mathrm{in} = \frac{dm}{dt}_\mathrm{out}
{% end %}

Or, after substitution with the previous definitions:

{% math() %}
\frac{d}{dt} \iiint \rho(r, t)~dV = -\oiint \mathbf{J} \cdot d\mathbf{S}
{% end %}

By Gauss's theorem, this integral equation can be written as a partial differential equation:

{% math() %}
\frac{\partial \rho}{\partial t} = -\nabla \cdot \mathbf{J}
{% end %}

Or written in another way:

{% math() %}
\frac{\partial \rho}{\partial t} + \nabla \cdot \mathbf{J} = 0
{% end %}

This is the **continuity equation**, a generalized description of the conservation of a physical quantity. It describes a quantity that cannot be created nor destroyed, and can only change due to flow into or out of a region.

Note that for an incompressible fluid the continuity equation simplifies to:

{% math() %}
\nabla \cdot \mathbf{J} = 0
{% end %}

## Flux for other fields

The gravitational field is represented by a vector field $\mathbf{g}$. The flux of $\mathbf{g}$ is given by:

{% math() %}
\oiint \mathbf{g} \cdot d\mathbf{S} = -4\pi GM
{% end %}

This is called **Gauss's law for gravity**, and is useful because it can be used to solve for $\mathbf{g}$ in the case of an arbitrary mass distribution. Recall also that the total mass can be written in terms of the mass density $\rho$:

{% math() %}
M = \iiint \rho~dV
{% end %}

Therefore:

{% math() %}
\oiint \mathbf{g} \cdot d\mathbf{S} = -4\pi G \iiint \rho~dV
{% end %}

If we define a scalar field called the _gravitational potential_ $\varphi$, where $\mathbf{g} = -\nabla \mathbf{g}$, then we can write:

{% math() %}
\nabla \cdot (\nabla \mathbf{g}) = \nabla^2 \phi = 4\pi G\rho
{% end %}

> Note that calling this a scalar potential is not an arbitrary name. The fact that $\mathbf{g} = -\nabla \varphi$ is _directly_ analogous to the relationship between force and potential energy, $\mathbf{F} = -\nabla U$.

Using Gauss's theorem (the divergence theorem) we can equivalently rewrite this integral equation as a partial differential equation:

{% math() %}
\nabla \cdot g = -4\pi G\rho
{% end %}

The same methodology applies to the analysis of the electric field as well. The flux of the electric field is given by:

{% math() %}
\oiint \mathbf{E} \cdot d\mathbf{S} = 4\pi kQ
{% end %}

Which is **Maxwell's 1st equation** in integral form. The equivalent equation for the magnetic field is **Maxwell's 2nd equation** in integral form:

{% math() %}
\oiint \mathbf{B} \cdot d\mathbf{S} = 0
{% end %}

## Waves

Waves are vibrations that propagate through space or along a material. There are two typical forms of waves:

- Transverse waves, such as waves on a vibrating string and electromagnetic waves
- Longitudinal waves, such as fluid waves (such as surface waves on water or sound waves in air) and seismic waves 

A travelling wave in 1D is given by:

{% math() %}
y(x, t) = A \cos(kx - \omega t + \varphi)
{% end %}

Where $k = \frac{2\pi}{\lambda}$ is the _wavenumber_, $\varphi$ is the _phase shift_, $\omega = \frac{2\pi v}{\lambda} = \frac{2\pi}{T} = 2\pi f$ is the _angular frequency_, and $\omega = kv$.

> Note that while $y(x, t)$ models a 1D wave, it is a **multivariable function** so its derivatives are partial derivatives.

All waves are described by the **wave equation**, which is a partial differential equation. The wave equation in 1D is given by:

{% math() %}
\frac{\partial^2 y}{\partial t^2} - c^2 \frac{\partial^2 y}{\partial x^2} = 0
{% end %}

Where $v$ is the speed of propagation of the wave. Specific cases of the wave equations have different $v$:

| Case | Value of $v$ |
|-----|---------|
| Mechanical waves | $v = \sqrt{F_T / \mu}$ where $F_T$ is the tension force and $\mu$ is the linear mass density |
| Electromagnetic waves (such as visible light) | $v = c$ |
| General waves | $v = v(x)$ |

Waves propagate (their wavefront moves forward) at a fixed speed, but this is not necessarily true of the particles they act upon. So we distinguish between the _wavefront speed_ $v$, which is the speed at which the wave itself moves, and the _transverse velocity_ (or _longitudinal velocity_) $v_y$, which is the velocity at which particles that the wave is moving through move. The expressions for transverse (longitudinal) velocity and transverse (longitudinal) acceleration are as follows:

{% math() %}
v_y(x, t) = \frac{\partial y}{\partial t} = -A\omega \sin(kx - \omega t)
{% end %}

{% math() %}
a_y(x, t) = \frac{\partial^2 y}{\partial t^2} = -A\omega^2 \cos(kx - \omega t)
{% end %}

Waves transfer energy. The energy carried (and thus transferred) by a travelling wave is given by:

{% math() %}
P(x, t) = \mu v A^2 \omega^2 \cos^2 (kx - \omega t)
{% end %}

The _average_ power is given by:

{% math() %}
P_\mathrm{avg} = \frac{1}{T} \int_0^T P(t)~dt = \frac{1}{2} \sqrt{\mu F_0} \omega^2 A^2 = \frac{1}{2} \mu v^3 k^2 A^2
{% end %}

(add in the proper equation, remember $v = \sqrt{F/\mu}$)

For a more in-depth discussion of waves, see the [waves and oscillations notes](@/waves-and-oscillations/index.md).

### Principle of Superposition

The wave equation is a second-order _linear_ partial differential equation. Therefore, if one function $f(x \pm ct)$ satisfies the wave equation, and another function $g(x \pm ct)$ also does, then any linear combination $af(x \pm ct) + bg(x \pm ct)$. Physically speaking, waves can pass through each other and add up with each other.

### Interference

Two waves that have different phases, that is $y_1 = f(x + ct + \phi_1)$ and $y_2 = f(x + ct + \phi_2)$. In the sinusoidal case, where $y(x, t) = A\sin(kx - \omega t + \phi_i)$, the resultant wave is:

{% math() %}
\begin{align*}
y(x, t) &= 2A \cos \left(\frac{\phi_2 - \phi_1}{2}\right) \left(kx - \omega t - \frac{\phi_1 + \phi_2}{2}\right) \\ &= 2A \phi_\mathrm{rel} \left(kx - \omega t - \frac{\phi_1 + \phi_2}{2}\right)
\end{align*}
{% end %}

Where $\phi_\mathrm{rel}$ is the relative phase shift:

{% math() %}
\phi_\mathrm{rel} = \cos \left(\frac{\Delta \phi}{2}\right)
{% end %}

Therefore when $\Delta \phi = 0$ (when the waves are in phase) then $\phi_\mathrm{rel} = 1$ which is known as **constructive** interference, and when $\Delta \phi = \pi$ (when the waves are completely out of phase) then $\phi_\mathrm{rel} = 0$ which is known as **destructive** interference.

> Note: this is the case only when the waves have the same amplitude. Otherwise, it is often more helpful to describe waves with complex exponentials i.e. $y(x, t) = Ae^{i(kx - \omega t)}

### Waves in fluids

In a fluid, density is given by:

{% math() %}
\rho(x, t) = -\rho_0 \frac{\partial y}{\partial x}
{% end %}

Pressure is given by:

{% math() %}
P(x, t) = -B \frac{\partial y}{\partial x}
{% end %}

This leads to the following two partial differential equations:

{% math() %}
\frac{\partial y}{\partial x} = -\frac{P(x, t)}{B}
{% end %}

{% math() %}
\frac{\partial y}{\partial x} = -\frac{\rho(x, t)}{\rho_0} 
{% end %}

And the following connection between density and pressure:

{% math() %}
\rho(x, t) = \frac{\rho_0}{B} P(x, t)
{% end %}

If oscilations in a particular fluid result in sinusoidal longitudinal plane waves, then:

{% math() %}
P(x, t) = BkA \sin(kx - \omega t)
{% end %}

{% math() %}
\rho(x, t) = \rho_0 k A\sin(kx - \omega t)
{% end %}

And $P_\mathrm{max} = BkA$, $\rho_\mathrm{max} = \rho_0 kA$, where $A = y_\mathrm{max}$, $k = \frac{\omega}{v}$ as is typical. The speed $v$ is given by:

{% math() %}
v = \sqrt{\frac{B}{\rho_0}}
{% end %}

Finally, the power $\frac{dE}{dt}$ of the fluid wave is given by:

{% math() %}
\frac{dE}{dt} = PAv = BkA^3 \omega \sin^2(kx - \omega t)
{% end %}

And the intensity $I$ is given by:

{% math() %}
I = Pv = BkA^2 \omega \sin^2(kx - \omega t)
{% end %}

The average intensity is given by:

{% math() %}
I_\mathrm{avg} = \frac{1}{T} \int_0^T I(x, t)~dt = \frac{A^2 \omega}{2 v} = \frac{1}{2} \sqrt{B \rho_0} A^2 \omega^2
{% end %}

Note that in the specific case where the waves are longitudinal but radiating outwards spherically, then by conservation of energy, the intensity follows an inverse square law:

{% math() %}
I \propto \frac{1}{r^2}
{% end %}

### Electromagnetic waves

Electromagnetism is completely described by the four Maxwell's equations:

{% math() %}
\begin{align*}
\nabla \cdot \mathbf{E} = \frac{\rho(\mathrm{x}, t)}{\epsilon_0} \\
\nabla \cdot \mathbf{B} = 0 \\
\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t} \\
\nabla \times \mathbf{B} = \mu_0 \mathbf{J} + \epsilon_0 \mu_0 \frac{\partial \mathbf{E}}{\partial t}
\end{align*}
{% end %}

In free space, $\rho = 0$ and $\mathbf{J} = 0$. Therefore, Maxwell's equations transform to two **wave equations**:

{% math() %}
\begin{align*}
\frac{\partial^2 \mathbf{E}}{\partial t^2} = \left(\frac{1}{\sqrt{\epsilon_0 \mu_0}}\right)^2 \nabla^2 \mathbf{E} \\
\frac{\partial^2 \mathbf{B}}{\partial t^2} = \left(\frac{1}{\sqrt{\epsilon_0 \mu_0}}\right)^2 \nabla^2 \mathbf{B}
\end{align*}
{% end %}

This leads to the result that electromagnetic fields propogate through space as waves, and even more surprisingly, $\frac{1}{\sqrt{\epsilon_0 \mu_0}}$ matches the known speed of light, suggesting that light _is_ an electromagnetic wave.

## Dynamics of special relativity

In special relativity, all space and all time is considered relative, and combined into a single continuum of **spacetime**. The spacetime interval is an invariant measure of distances both of space and of time in special relativity:

{% math() %}
ds^2 = \eta_{\mu \nu} dx^\mu dx^\nu = -c^2 dt^2 + dx^2 + dy^2 + dz^2
{% end %}

### Relativistic equations of motion

The relativistic equivalent of Newton's second law is given by:

{% math() %}
\frac{d}{dt} \left(\frac{mv}{\sqrt{1 - \frac{v^2}{c^2}}}) = F(x, t)
{% end %}

Which can be written in terms of a quantity known as **4-momentum** $\mathbf{p}$, which is conserved in all frames:

{% math() %}
\frac{d\mathbf{p}}{dt} = F(x, t)
{% end %}

For more on special relativity, see the [special relativity series](@/special-relativity/index.md)

## Thermodynamics

Thermodynamics is concerned with the flow of energy between and within systems. For instance, consider two bodies in thermal contact with each other. Thermodynamics predicts that the final equilibrium temperature of the two bodies, assuming they are of masses $m_1$ and $m_2$ and had initial temperatures $T_1$ and $T_2$, is given by:

{% math() %}
T_\mathrm{end} = \frac{m_1 T_1 + m_2 T_2}{m_1 + m_2}
{% end %}

The methods of thermodynamics are used for calculating the **state variables** $P, V, T$ (pressure, volume, and temperature) of a thermal body. A specific case commonly studied in thermodynamics would be that of an ideal gas - that is, a gas that obeys the **equation of state** $PV = nRT$, where $n$ is the moles of particles in a gas, and $R$ is the ideal gas constant. An ideal gas expands under a changing temperature according to:

{% math() %}
\Delta V = \beta V \Delta T
{% end %}

where $\beta$ is defined as follows when thermodynamic variable $X$ (e.g. pressure, temperature, etc.) is kept constant:

{% math() %}
\beta = \frac{1}{V} \left(\frac{\partial V}{\partial T}\right)_X
{% end %}

For instance, the thermal expansion at **constant pressure** is given by:

{% math() %}
\beta = \frac{1}{T}
{% end %}

Meanwhile, an ideal gas expands under a changing pressure according to:

{% math() %}
\Delta V = -\kappa V \Delta P
{% end %}

where analogously $\kappa$ is defined as:

{% math() %}
\kappa = -\frac{1}{V} \left(\frac{\partial V}{\partial P}\right)_X
{% end %}

For instance, the compressibility at **constant temperature** is given by:

{% math() %}
\kappa = \frac{1}{P}
{% end %}

### Thermodynamic work

Analogous to mechanical work, thermodynamic work is given by the line integral:

{% math() %}
W = \int_C P(V)~dV
{% end %}

In many cases, this line integral reduces down to a regular integral. For instance, in an ideal gas whose equation of state is given by $PV = Nk_B T$, then:

{% math() %}
P(V) = \frac{Nk_B T}{V}
{% end %}

Therefore the work done as the gas expands from $V_1$ to $V_2$ is given by:

{% math() %}
W = \int_{V_1}^{V_2} \frac{NkT}{V}~dV = Nk_B T \ln \left(\frac{V_2}{V_1}\right)
{% end %}

The **first law of thermodynamics** states that the total change in the internal energy $U$ of a system is related to the line integral of the infinitesimal change in heat $\delta Q$ and the work done by the system by:

{% math() %}
\Delta U = \int_\gamma dQ - \int_\gamma dW
{% end %}

Or in turns of discrete changes:

{% math() %}
\Delta U = \Delta Q - \Delta W
{% end %}

> Note: there are two expressions for the first law of thermodynamics, the Clausius convention (the one used here) and the IUPAC convention, which differ in the sign used.

### Thermodynamic processes

In general, any thermodynamic process can be broken down into a combination of the following distinct types of processes:

- **Isobaric** (constant pressure)
- **Isochoric** (constant volume)
- **Isothermic** (constant temperature)
- **Adiabatic** (constant heat)

The thermodynamic variables of state can be calculated via the following table of relations:

| Isobaric ($P = \text{const.}$) | Isochoric ($V = \text{const.}$) | Isothermic ($T = \text{const.}$) | Adiabatic |
|---|---|---|---|
| $\Delta U = Q - W$ | $\Delta U = Q$ | $\Delta U = 0$ | $\Delta U = -W$ |
| $Q = nC_P \Delta T$ | $Q = nC_V \Delta T$ | $Q = W$ | $Q = 0$ |
| $W = P\Delta V$ | $W = 0$ | $W = nRT \ln \left(\frac{V_2}{V_1}\right)$ | $\frac{C_V}{R} (P_1 V_1 - P_2 V_2)$ |
| $\frac{T_1}{T_2} = \frac{V_1}{V_2}$ | $\frac{P_1}{T_1} = \frac{P_2}{T_2}$ | $\frac{P_1}{V_1} = \frac{P_2}{V_2}$ | $PV^\gamma = \text{const.}$, $TV^{\gamma - 1} = \text{const.}$

### Entropy

**Entropy** is a statistical measure of the disorder of a system. The entropy of a thermodynamic system $S$ can be roughly understood as how far a system has progressed towards a state of thermodynamic equilibrium. In terms of the state variables, entropy can be calculated via:

{% math() %}
\Delta S = mc\int_{T_1}^{T_2} \frac{dQ}{T}
{% end %}

The **second law of thermodynamics** expresses the change in heat as a line integral:

{% math() %}
\Delta Q = \int_\Lambda T~dS
{% end %}

As temperature is a statistical measure of itself, the second law predicts that **it is probabilistically likely entropy will increase in a closed system**. This prevents processes from being reversible; a cup falling off a table is unlikely to return back to the top of the table.
