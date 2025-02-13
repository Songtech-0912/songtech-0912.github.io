+++
title = "Introduction to multivariable calculus"
date = 2024-08-26
draft = false
+++

This is a guide to multivariable calculus from its fundamentals. We will cover differentiation of multivariable functions, the gradient, divergence, and curl operators, as well as integration in multiple dimensions, on a beginner's level. It is highly recommended to look over this guide before (or at the same time as) learning any advanced topics in math and physics.

<!-- more -->

These notes are shared with the permission of [Dr. Elizabeth Brown](https://faculty.rpi.edu/elisabeth-brown) of Rensselaer Polytechnic Institute., to whom much is appreciated.

## Multivariable functions

A multivariable function is a function of two or more variables. For instance, $f(x, y)$ is a function of two variables and $g(x, y, z)$ is a function of three variables, so both can be considered multivariable function. Meanwhile, $h(x)$ is a function of just one variable, and therefore is not a multivariable function.

The set of $(x_1, x_2, \dots, x_n)$ on which a function of $n$ variables $f(x_1, x_2, \dots, x_n)$ is defined is its **domain**, which are the valid *inputs* to the function. The set of points that can be obtained by evaluating the function is its **range**, which are valid *outputs* to the function.

As an example, consider the function $f(x, y) = \sqrt{4 - x^2 - y^2}$, which can be rewritten $f(x, y) = \sqrt{4 - (x^2 + y^2)}$. Such a function is not defined for $(x^2 + y^2) > 4$ which can also be written $r^2 > 4$. Therefore its domain $\mathcal{D}$ is $(x, y) \in \mathbb{R}^2:\, x^2 + y^2 \leq 4$. Visually speaking, this is all points in the XY plane inside or on a circle of radius $2$ because $r^2 = 4 \to r = 2$. Meanwhile, due to its restricted domain, $f(x, y)$ can only output values between 2 (for $r^2 = 0$) and 0 (for $r^2 = 4$). Therefore the range $\mathcal{R}$ is $0 \leq f(x, y) \leq 2$.

We may plot a function of two variables $f(x, y)$ in 3D space, such that $z = f(x, y)$. From doing so, we create a surface. This is usually done by computer, and is shown below:

{{ wideimg(src="math3d-multivariate-function-plot.png",
   desc="A plot of a multivariable function, shown as a surface in 3D space")
}}


_Created with [Math3D](https://www.math3d.org/)_

Instead a surface plot, we may alternatively make various 2D representations of functions of 2 variables. To do so, we first find the **horizontal traces** (also called _isolines_), which are all curves in which $f(x, y) = C$ where $C$ is a constant. This results in an implicit equation that can be solved to result in the equation of a curve in one variable. Doing this for equally spaced $C$ results in a contour map, as shown:

{{ natural_img(src="https://upload.wikimedia.org/wikipedia/commons/f/fa/Contour2D.svg",
   desc="Contour map, showing level curves of constant height"
)
}}

We can also plot values of $f(x, y)$ for values of constant $x$ or constant $y$ to find **vertical traces**, curves of constant value in one plane. So as a summary:

- **Horizontal traces** are curves of constant height, found by solving for $f(x, y) = C$ where $C$ is a specified constant
- **Vertical traces** are curves of constant $x$ or $y$, found by solving $z = f(C, y)$ or $z = f(x, C)$
- **Level curves** result from finding multiple horizontal traces for equally-spaced $C$
- **Contour maps** (occasionally called _isoline plots_) are the result of level curves drawn on the XY plane

What about for function of more than two variables? With few exceptions, functions of three variables cannot be directly plotted in 3D space because they would require 4D space to plot. However, we can plot _level surfaces_ (also called isosurfaces), which are partially-transparent surfaces of constant value just like level curves, like these:

Functions of more than three variables cannot be plotted at all through conventional means, but specialized data visualization methods can be used to visualize them. However, even if visualization is not possible, the methods of calculus can still be used to analyze them.

## Partial derivatives

Partial derivatives are the equivalent of ordinary derivatives, but for **multivariable functions**. They are found by treating all variables not differentiated with respect to as **constant**. Formally, they are defined using limits just as ordinary derivatives are, and notated with script $\partial$ rather than the normal $d$. For a function $f(x, y)$, the respective definitions of the partial derivatives with respect to $x$ and of $y$ are:

{% math() %}
\begin{align*}
\frac{\partial f}{\partial x} = \frac{f(x + h, y) - f(x, y)}{h} \\
\frac{\partial f}{\partial y} = \frac{f(x, y+h) - f(x, y)}{h}
\end{align*}
{% end %}

The geometric interpretation is that $\dfrac{\partial f}{\partial x}$ is the derivative with respect to $x$ of the trace curve in the XZ plane, and $\dfrac{\partial f}{\partial y}$ is the derrivative with respect to $y$ of the trace curve in the XY plane.

### Partial derivative notation

The Leibniz-style notation $\displaystyle \frac{\partial f}{\partial x}$ can be alternatively written as $\displaystyle \frac{\partial}{\partial x} f(x, y, z)$ and second derivatives are also possible such as $\displaystyle \frac{\partial^2 f}{\partial x^2}$ for the second partial derivative with respect to $x$. We may also consider cases in which we take the partial derivative with respect to one variable, then another, and in such cases we go from **right to left**. As an example $\displaystyle \frac{\partial^2 f}{\partial y \partial x}$ means to take the partial derivative with respect to $x$ first, and then $y$ after that. A way to remember this is that you're applying nested derivative operators, that is, $\dfrac{\partial^2 f}{\partial y \partial x} = \dfrac{\partial}{\partial y} \left(\dfrac{\partial}{\partial x} f(x)\right)$ and therefore if the brackets are removed, the differentiated variables go from right to left.

There is an **alternate notation** for partial derivatives, known as the prime notation. In this notation, $f_x$ is the notation for the partial derivative with respect to $x$ and analagously $f_y$ is the notation for the partial derivatives with respect to $y$. Unlike Leibnitz notation, prime partial derivative notation reads from **left to right**. That is, $f_{x y}$ means to take the partial derivative with respect to $x$ and _then_ to $y$.

In addition, especially in advanced physics, partial derivatives can be denoted by the shorthand $\partial_x f$ and $\partial_y f$. Then we may write $\partial_x \partial_x f$ for the second partial derivative with respect to the variable $x$, or $\partial_x^n f$ for the nth-partial derivative with respect to the variable $y$. This is not as common in mathematics and generally this will not be used here.

There are situations in which one notation is preferred over the other for convenience. The choice ultimately does not matter as they do not change the underlying mathematics.

### A worked example for taking a partial derivatives

Consider the function $f(x, y) = x^3 + e^x y^2 + 2 \sin y$. We wish to compute the (first) partial derivatives with respect to $x$ and $y$. We may use the sum/difference rule in differentiation to first simplify to:

{% math() %}
\begin{align*}
\frac{\partial f}{\partial x} &= \frac{\partial}{\partial x}(x^3) + \frac{\partial}{\partial x}(e^x y^2) + \frac{\partial}{\partial x}(2 \sin y) \\
\frac{\partial f}{\partial y} &= \frac{\partial}{\partial y}(x^3) + \frac{\partial}{\partial y}(e^x y^2) + \frac{\partial}{\partial y}(2 \sin y) 
\end{align*}
{% end %}

Then we may begin to take the partial derivatives with respect to each variable. For the term $\displaystyle \frac{\partial}{\partial x}(e^x y^2)$ we treat y$^2$ as if it was a constant, so we can factor it out via the constant coefficient rule, resulting in $y^2 \displaystyle \frac{\partial}{\partial x}(e^x)$. We may then differentiate as usual, resulting in $y^2 e^x$ (as the derivative of $e^x$ is itself). For the term $\dfrac{\partial}{\partial x} (2 \sin y)$, we notice that $2 \sin y$ does not depend on $x$, therefore its partial derivative is zero. Following the same technique for the partial derivatives with respect to $y$, the solutions are given by:

{% math() %}
\begin{align*}
\frac{\partial f}{\partial x} &= 3x^2 + e^x y^2  \\
\frac{\partial f}{\partial y} &= 2ye^x + 2 \cos y 
\end{align*}
{% end %}

### The gradient operator

In many cases, we wish to find a  vector containing all the partial derivatives of a function. The operator that does this is called the **gradient operator** $\nabla$. Applying the gradient operator on a function $f(x, y, z)$ becomes:

{% math() %}
\nabla f = \left\langle \frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}, \frac{\partial f}{\partial z} \right\rangle
{% end %}

The gradient vector points in the direction of steepest ascent of $f(x, y, z)$.

### The product rule for partial derivatives

The product rule holds true for partial derivatives with minimal modifications. For a function $u(x, y) = f(x, y)\, g(x, y)$, the product rule takes the form:

{% math() %}
\begin{align*}
\frac{\partial u}{\partial x} = f \frac{\partial g}{\partial x} + g \frac{\partial f}{\partial x} \\
\frac{\partial u}{\partial y} = f \frac{\partial g}{\partial y} + g \frac{\partial f}{\partial y}
\end{align*}
{% end %}

### The chain rule for partial derivatives

The chain rule for taking partial derivatives of composite functions _also_ applies for partial derivatives. However, an important thing to remember is that you must sum the derivatives of **all intermediary variables**. For instance, consider the function $u(x, y)$ where $x$ and $y$ are functions of $s$ and $t$, that is, $x(s, t)$ and $y(s, t)$. Then the partial derivatives of $u$ with respect to $s$ and $t$ are respectively given by:

{% math() %}
\begin{align*}
\frac{\partial u}{\partial s} = \frac{\partial u}{\partial x} \frac{\partial x}{\partial s} + \frac{\partial u}{\partial y} \frac{\partial y}{\partial s} \\
\frac{\partial u}{\partial t} = \frac{\partial u}{\partial x} \frac{\partial x}{\partial t} + \frac{\partial u}{\partial y} \frac{\partial y}{\partial t}
\end{align*}
{% end %}

Notice that for both partial derivatives we **must** include all the "middle variables" ($x$ in the first case and $y$ in the second case) that $u$ depends on.

#### The chain rule for paths

Consider a path $\mathbf{r}(t)$. A function that depends on the path $\mathbf{r}$, that is, $F(\mathbf{r}(t))$, may be differentiated with respect to $t$ via $\nabla F \cdot \mathbf{r}'(t)$, as the expansion becomes:

{% math() %}
\frac{\partial F}{\partial t} = \frac{\partial F}{\partial x} \frac{dx}{dt} + \frac{\partial F}{\partial y} \frac{dy}{dt} = \nabla F \cdot \mathbf{r}'(t)
{% end %}

### Clairaut's Theorem

A very useful tip is that taking partial derivatives is **commutative**: the order in which you take mixed partial derivatives **does not matter**:

{% math() %}
\frac{\partial^2}{\partial y \partial x} = \frac{\partial^2}{\partial x \partial y}
{% end %}

In prime notation (remember prime notation goes left to right instead of Leibnitz which goes from right to left) we can write the same as $f_{yx} = f_{xy}$. In addition, this holds true in the general case to **any number of mixed partial derivatives**. Sometimes it is easier to differentiate with respect to one variable than to another variable so this rule can become very useful.

## Applications of partial derivatives

### Linear approximations

A complex function $f(x, y)$ may be approximated in the neighborhood of the point $(a, b)$ by a **tangent plane**, just like a function of one variable can be approximated in the neighborhood of a point by a tangent line. To compute the tangent plane, we first define two tangent vectors to the linear traces as follows:

{% math() %}
\begin{align*}
\mathbf{v} = \left\langle 1, 0, \frac{\partial}{\partial x} (a, b) \right\rangle \\
\mathbf{\omega} = \left\langle 0, 1, \frac{\partial f}{\partial y}(a, b) \right\rangle
\end{align*}
{% end %}

The normal vector becomes $\mathbf{n} = \omega \times \mathbf{v}$ which can be found by calculating the below determinant:

{% math() %}
\omega \times \mathbf{v} = \begin{vmatrix}
\hat{\mathbf{i}} & \hat{\mathbf{j}} & \hat{\mathbf{k}} \\
0 & 1 & \dfrac{\partial f}{\partial y} (a, b) \\
1 & 0 & \dfrac{\partial f}{\partial x} (a, b)
\end{vmatrix}
{% end %}

Therefore, the normal vector is given by:

{% math() %}
\mathbf{n} = \left\langle \frac{\partial f}{\partial x}(a, b), \frac{\partial f}{\partial y}(a, b), 1 \right\rangle
{% end %}

And the equation of the tangent plane is given by $z = \mathbf{n} \cdot (\mathbf{r} - \mathbf{r}_0)$ where $\mathbf{r}_0 = \langle a, b \rangle$, assuming that $f(x, y)$ is smooth (and thus continuous). We may also also write the equation of the tangent plane as an _implicit equation_ as $\mathbf{n} \cdot (\mathbf{r} - \mathbf{r}_0) - z= 0$.

> **When do we actually use the linear approximation?** We use the linear approximation for many applications in physics where we only consider local variations from a point for a function of several variables. For instance, such an approximation may be used to calculate the value of the pressure from a known pressure at a point and given the pressure as a function of $x$ and $y$. In addition, linearity and linearizing functions is very important for solving **differential equations** in mathematics and physics, where a linear approximation allows the problem to be tractable so that an analytical (exact) solution may be found within a local region.

### More on linear approximations

The total change $\Delta f$ in a function $f(x, y)$ from $f(x, y)$ to $f(x + \Delta x, y + \Delta y)$ is given by the linear approximation shown below:

{% math() %}
\Delta f = \dfrac{\partial f}{\partial x} \Delta x + \dfrac{\partial f}{\partial y} \Delta y
{% end %}

The infinitesimal version becomes:

{% math() %}
df = \dfrac{\partial f}{\partial x} \Delta x + \dfrac{\partial f}{\partial y} \Delta y
{% end %}

For a point near a known value of a function and in which the derivatives of a function are known, this can help us evaluate a function, which is very useful in evaluating square roots (for instance, evaluating $\sqrt{4.5}$ by setting $\Delta x = 0.5$ as we know the value of $\sqrt{4}$), trigonometric functions, and other transcendentals.

## Surfaces formed by a function of two variables

We may write a function of two variables as a **surface** with the explicit equation $z = f(x, y)$, or the implicit equation $F(x, y, z) = f(x, y) - z$. The surface is distinct from the function; it is the shape in 3D space produced by the function.

We must distinguish carefully between gradient of a function and the gradient of a surface _formed by_ a function. The gradient of a function $f(x, y)$ takes the form: 

{% math() %}
\left\langle \dfrac{\partial f}{\partial x}, \dfrac{\partial f}{\partial y}\right\rangle
{% end %}

As such, it is a **2D vector** (only $x$ and $y$ components with no $z$-component) that points in the direction of the greatest increase of $f(x, y)$. 

By contrast, the gradient of the surface _formed by_ a function, defined by $F(x, y, z) = f(x, y) - z = 0$ has the _different_ form:

{% math() %}
\begin{matrix*}
\left\langle \dfrac{\partial f}{\partial x}, \dfrac{\partial f}{\partial y}, \dfrac{\partial f}{\partial z}\right\rangle,
&\dfrac{\partial f}{\partial z} = -1
\end{matrix*}
{% end %}

The gradient of the surface is a **3D vector** (that has all three of $x, y, z$ components) and is _always_ normal to the tangent plane at a point $x, y, z$ of the function.

## Optimization in multiple variables

In single-variable calculus, we know that if a function $f(x)$ has a local **extrenum** (maximum or minimum) at $x = c$, then $f'(c) = 0$ or $f'(c) = \mathrm{DNE}$ (does not exist). We call $c$ a _critical point_ of $f(x)$. This is **Fermat's theorem**. Note that the converse is not true: $f'(c) = 0$ or $f'(c) = \mathrm{DNE}$ **does not necessarily mean** that there is a local extrenum.

In similar fashion to single-variable calculus, we define a _local minimum_ of a function of several variables $f(\mathbf{x})$ as the point $\mathbf{p} = (a, b) \in D$ such that $f(\mathbf{x}) > f(\mathbf{p})$ for all $\mathbf{x}$ in a region $|\mathbf{x}| \leq k$, where $D$ is the domain of the function, and $f(\mathbf{x}) = f(x_1, x_2, x_3, \dots x_n)$ is a shorthand notation.  We define a _local maximum_ of $f(\mathbf{x})$ as the point $\mathbf{p} \in D$ such that $f(\mathbf{x}) < f(\mathbf{p})$ for all $\mathbf{x}$ in a region $|\mathbf{x}| \leq k$. Global minima and maxima have almost exactly the same definition other than the fact that $k$ must extend to the bounds of the domain.

Iff a function of several variables $f(\mathbf{x})$ has a local extrenum at $\mathbf{p}$, then $\nabla f(\mathbf{p}) = 0$ or $\nabla f(\mathbf{p}) = \mathrm{DNE}$ and we say $\mathbf{p}$ is a **critical point**. But simply finding the critical point(s) is **insufficient** for determining local extrema. We must either test all points within a radial region (e.g. open disk for a function of two variables) around the point $\mathbf{p}$ (just like the first derivative test) _or_ we must apply the second derivative test.

The second derivative test determines whether a critical point $\mathbf{p} = (a, b)$ is a local minimum, local maximum, or saddle point. To state the second derivative test, we must first define a function $D^2$ that is given by the following:

{% math() %}
D^2(x, y) = 
\begin{vmatrix}
\dfrac{\partial^2 f}{\partial x^2} & \dfrac{\partial^2 f}{\partial x \partial y} \\
\dfrac{\partial^2 f}{\partial y \partial x} & \dfrac{\partial^2 f}{\partial y^2}
\end{vmatrix} = \det
\begin{pmatrix}
\dfrac{\partial^2 f}{\partial x^2} & \dfrac{\partial^2 f}{\partial x \partial y} \\
\dfrac{\partial^2 f}{\partial y \partial x} & \dfrac{\partial^2 f}{\partial y^2}
\end{pmatrix}
{% end %}

Here $D$ is called the **discriminant** and represents the a second-order polynomial centered at $(x, y, z)$, and is the determinant of the **Hessian**, a matrix made of all the second derivatives of a function. The conditions are as follows:

- If $D^2(a, b) > 0$ then $(a, b)$ is either a local maximum or minimum
	- If in addition, $\partial_x^2 f(a, b) > 0$ (second partial derivative with respect to $x$ evaluated at $(a, b)$ is *greater* than zero), then the function is concave up at $(a, b)$ and thus $(a, b)$ is a **local minimum**
	- If in addition, $\partial_x^2 f(a, b) < 0$ (second partial derivative with respect to $x$ evaluated at $(a, b)$ is *less* than zero), then the function is concave up at $(a, b)$ and thus $(a, b)$ is a **local maximum**
- If $D^2(a, b) < 0$ then $(a, b)$ is a **saddle point** (inflection point)
- If $D^2(a, b) = 0$ then the test is **inconclusive** and another test must be used instead

### Multivariable extreme value theorem 

For functions of several variables, the extreme value theorem from single-variable calculus takes a more general form:

> **Extreme value theorem in several variables:** Given a closed domain $D \in \mathbb{R}^2$ of a function $f(x, y)$ with absolute maximum located at $(x_1, y_1)$ and absolute minimum $(x_2, y_2)$ on $D$, the extreme values of $f$ are $f(x_1, y_1)$ and $f(x_2, y_2)$. That is to say, there are three conditions that **must** be satisfied to guarantee the existence of at least one minimum and one maximum: **continuity, boundedness, and a closed domain**. If any of the three are not satisfied, the extreme value theorem **does not hold**.

To additionally guarantee the existence of an **absolute extrema**, a point must satisfy the extreme value theorem _and_ take on a greater (for maxima) or smaller (for minima) value than the boundary point. It is necessary to find all critical points of $f$ and evaluate $f$ on each of them; the critical point that yields the largest value of $f(x, y)$ when evaluated is the **absolute maximum** and the critical point that yields the smallest value of $f(x, y)$ when evaluated is the **absolute minimum**. Remember that the absolute maximum and absolute minimum _may not be a critical point_; it may also be one of the **boundary points**. Therefore, comparing against all boundary points is _essential_ to finding the true absolute maxima and minima.

### Optimization via Lagrange multipliers

In the restricted case where a constraint is applied to a multivariable function, we may use an alternative method called **Lagrange multipliers** for optimization. This may be, for instance, a multivariable function subject to the following condition:

{% math() %}
\text{minimize}\, f\, \mathrm{where}
\begin{cases}
f = f(x, y) \\
g(x, y) = 0
\end{cases}
{% end %}

A feature of this system is that the we may treat the constraint curve as a slice along $f(x)$, i.e. a level curve. The gradient of $f$ evaluated at a point always follows the direction of maximum increase of $f(x)$, and is normal to its surface. The gradient of $g$ is by definition perpendicular to the level curves, and all level curves run tangent to the function, meaning it is _also_ normal to $f$'s surface. This means that the gradient of $f$ is always parallel to the gradient of $g$ and thus the two gradients must be scalar multiples of each other. Thus we have the **Lagrange condition**:

{% math() %}
\nabla f(a, b) = \lambda \nabla g(a, b)
{% end %}

By expansion for the gradient in the case of a function of two variables (and this may be generalized to functions of any number of variables), we have a series of three simultaneous equations that we may evaluate to find the critical points:

{% math() %}
\begin{cases}
\dfrac{\partial f}{\partial x}(a, b) = \lambda \dfrac{\partial f}{\partial x} g(a, b) \\\\
\dfrac{\partial f}{\partial y}(a, b) = \lambda \dfrac{\partial f}{\partial y} g(a, b) \\\\
g(a, b) = 0
\end{cases}
{% end %}

All solution points $(a, b)$ that satisfy the Lagrange system of equations are **critical points**. We may then compare all critical points to obtain the **absolute minimum and maximum**.

As an example, let us find the absolute minimum and maximum of $f(x, y) = x^2 + 2y^2$ on a unit circle, that is, where $g(x, y) = x^2 + y^2 -1$ following the equation of a circle $x^2 + y^2 = 1$ placed in the form $g(x, y) = 0$. To do so, we find that the partial derivatives are $\dfrac{\partial f}{\partial x} = 2x$ and $\dfrac{\partial f}{\partial y} = 4y$. After substitution into the Lagrange multiplier equations previously stated, we find:


{% math() %}
\begin{align*}
2x = \lambda 2x \to 2x(1 - \lambda) = 0 \\
4y = \lambda 2y \to 2y(2 - \lambda) = 0 \\
x^2 + y^2 = 1
\end{align*}
{% end %}

Thus from the first equation we have $\lambda = 1$ and from the second we have $\lambda = 2$. We then substitute $\lambda = 1$ into _both equations_, then subsitute $\lambda = 2$ into _both equations_, to get all solutions. From this way, we find that $x = \pm 1, y = \pm 1$. Thus, we have the four critical points $(0, 1), (0, -1), (1, 0), (-1, 0)$. 

We must now evaluate $f(x, y)$ at the critical points. Doing so, we have $f(0, 1) = 2, f(0, -1) = 2, f(1, 0) = 1, f(-1, 0) = 1$. Therefore, the **maximum value** of $f$ given the constraint is $f = 2$ and the **minimum value** of $f$ given the constraint is $f = 1$.

This demonstrative example is the simplest case; there may be more than one constraint, and a function of more than two variables. Thus the general Lagrange multiplier equations become:

{% math() %}
\begin{cases}
\nabla f &= \displaystyle\sum_{i = 1}^n \lambda_i g_i(\mathbf{x}) \\
g_1(\mathbf{x}) &= 0 \\
g_2(\mathbf{x}) &= 0 \\
g_3(\mathbf{x}) &= 0 \\
&\vdots \\
g_n(\mathbf{x}) &= 0
\end{cases}
{% end %}

## Multiple integration

In single-variable calculus, we integrate to find the sum of a continuous quantity, such as the area under a curve, the displacement from a velocity-time graph, or the surface area of a surface of rotation. In multivariable calculus, we generalize this concept to multiple dimensions, where we can define several types of _multivariate integrals_.

### Double integrals

A double integral, the first type of multivariate integral, is used in any situation where one needs to perform integration over an area. For instance, one can find the *volume* under the surface $z = f(x, y)$ by integrating a function $f(x, y)$ over the domain $R$:

{% math() %}
V = \iint_R f(x, y)\, dA
{% end %}

Or the volume *between* two surfaces $z_2(x, y)$ and $z_1(x, y)$ where $z_2 > z_1$ for all $(x, y)$ as:

{% math() %}
V_\mathrm{between} = \iint_R z_2(x, y) - z_1(x, y)\, dA
{% end %}

One may also find the *area* over an irregular region by performing the double integral shown:

{% math() %}
A = \iint_R dA
{% end %}

To evaluate a double integral, we must first check that the domain is closed (i.e. has a continuous boundary) and bounded (i.e. not infinite). Then we define the domain $R$ as either a vertically-simple or horizontally-simple region. A **vertically-simple region** is a region between constant vertical bounds (bounds at constant x-values). For instance, the region bounded by $-1 \leq x \leq 5$ is a vertically-simple region, because its vertical boundaries $x = -1$ and $x = 5$  are at constant x-values. However, the region bounded by $-3 \leq x \leq 3\cos^2(y)$ is _not_ vertically-simple, because its right vertical bound is not at a constant x-value. It may be helpful to visualize a vertically-simple region as a region between two "walls" on the grid.

Meanwhile, a **horizontally-simple region** is a region between constant horizontal bounds (bounds at constant y-values). For instance, the region bounded by $-6 \leq y \leq 6$ is a horizontally-simple region, because its horizontal boundaries $y = -6$ and $y = 6$ are constant; the region bounded by $-6 \leq y \leq x^2$ is however _not_ horizontally simple.

In the special case that the region is both vertically and horizontally simple, a region is often notated $R = [x_1, x_2] \times [y_1, y_2]$. This means that the integral must be performed with bounds in $x$ of $[x_1, x_2]$ and bounds in $y$ of $[y_1, y_2]$.

Integration is usually done after a region is checked to be either vertically-simple or horizontally simple, as otherwise the integral cannot be computable. For all non-simple regions, it is necessary to divide these regions into several simple vertically and horizontally simple regions, after finding the intersection points, and _then_ integrate.

### Fubini's theorem

After preparing and analyzing the domain, we may use **Fubini's theorem** to solve a double integral. Fubini's theorem says that a double integral over the region $R = [x_1, x_2] \times [y_1, y_2]$ can be evaluated in any of the below ways:

{% math() %}
\iint \limits_R f(x, y)\, dA = \int_{x_1}^{x_2} \int_{y_1}^{y_2} f(x, y)\, dy\,dx= \int_{y_1}^{y_2} \int_{x_1}^{x_2}  f(x, y)\, dx\,dy
{% end %}

Notice how the bounds "sandwich" the integrand inside, and how we can change the order of integration by switching the bounds. Evaluating the resultant iterated integral becomes then a matter of taking the partial integral (integrating while treating all other variables as constant) multiple times until the final answer is reached.

It is _also_ possible for double integrals to have variable bounds. However, note that the bounds and the integration variable _must_ be different. For instance, these two forms are valid:

{% math() %}
\int_0^5 \int_0^{3x^2} f(x, y) dy\, dx, \quad \int_{-1}^1 \int_{-\cos y}^{5\sin^2 y} f(x, y)\, dx\, dy
{% end %}

For the left integral, the variable bound is in $x$ and integrated with respect to $y$; for the right integral, the variable bound is in $y$ and is integrated with respect to $x$. Thus both are perfectly valid. However, the below integral would be invalid:

{% math() %}
\int_{-3}^3 \int_{-x}^x f(x, y) dx\, dy
{% end %}

This is not possible because an integral cannot be integrated over bounds with the same variable as the integration variable. Therefore, the order of integration and bounds must be carefully chosen to ensure that the integral makes sense. A careful choice of the bounds, which may include switching the bounds, may make a very complex or even impossible integral tractable.

### Double integrals in polar coordinates

We often want to find a double integral in polar coordinates when we spot an integral over a function that exhibits radial symmetry - for instance, $f(x, y) = x^2 + y^2$ which is equivalent to $f(r, \theta) =r^2$. In this case, we may use the _polar coordinates_ transformation to evaluate the double integral:

{% math() %}
\iint_R f(x, y)\, dA = \iint_R f(r \cos \theta, r \sin \theta)\, r\, dr \, d\theta 
{% end %}

### Triple integrals

We may extend the same concept of a double integral into integrating over a 3D region (volume) in space for a function of three variables. This gives us a **triple integral**. The triple integral can be used to find the _volume_ of a 3D region:

{% math() %}
V = \iiint_\Omega dV
{% end %}

It can also be used to find the total of some quantity distributed throughout space, for which we write:

{% math() %}
\iiint_\Omega f(x, y, z) \, dV
{% end %}

A triple integral is evaluated using much the same way as a double integral, using Fubini's theorem. That is, for a triple integral defined over $\Omega = [x_1, x_2] \times [y_1, y_2] \times [z_1, z_2]$ we have:

{% math() %}
\iiint_\Omega f(x, y, z) \, dV = \int_{x_1}^{x_2} \int_{y_1}^{y_2} \int_{z_1}^{z_2} f(x, y, z) \, dz\, dy\, dx
{% end %}

Or any of the different orderings possible by switching the order of integration. A triple integral may sometimes be simplified if we know that the bounds in $z$ are $z_1(x, y)$ and $z_2(x, y)$ where $z_2 > z_1$. In this case, we say that the domain is a **z-simple region** and we may rewrite the triple integral in terms of a double integral as follows:

{% math() %}
\iiint_\Omega f(x, y, z) \, dV = \iint \limits_{[x_1, x_2] \times [y_1, y_2]} \left[\int_{z_1(x, y)}^{z_2(x, y)} f(x, y, z) \, dz\right] dA
{% end %}

### Triple integrals in cylindrical and spherical coordinates

We may define alternate coordinate systems in addition to Cartesian coordinates. For instance, we can use spherical coordinates $(r, \theta, \varphi)$ where $r$ is the radial distance,  $\theta$ is the polar angle measuring rotation up and down the XY plane, and $\varphi$ is the azimuthal angle measuring the rotation around XY plane. We often also refer to the XY plane as the **equatorial**. A diagram of the spherical coordinates system is shown as follows:

{{ natural_img(src="https://upload.wikimedia.org/wikipedia/commons/f/f9/Kugelkoord-lokb-e.svg", desc="An illustration of spherical coordinates, where a point in space is denoted by its radial distance r, its planar rotation phi, and its elevation angle theta")}}

_Credit: [Wikipedia](https://commons.wikimedia.org/wiki/File:Coordenadas_esf%C3%A9ricas_01.svg)_

> **Note:** this is the _physics convention_. Mathematicians often use the alternate convention $(r, \varphi, \theta)$ rather than $(r, \theta, \varphi)$, in which $\theta$ and $\varphi$ are swapped. Additionally, the letter $\varphi$ is often written as $\phi$ (they are both the same greek letter, just rendered in different styles).

The coordinate transformations for $(r, \theta, \varphi)$ to $(x, y, z)$ are as follows:

{% math() %}
\begin{align*}
x &= r \sin \theta \cos \varphi \\
y &= r \sin \theta \sin \varphi \\
z &= r \cos \theta
\end{align*}
{% end %}

A volume element in spherical coordinates (using the physics convention), would be an infinitesimal cube with side lengths $dr$, $r d\theta$, and $r \sin \theta d\varphi$. So the volume element is $dV = r^2 \sin \theta \,dr\, d\varphi d\theta$.

We may also use a **cylindrical coordinate system** where we use the coordinates $(r, \theta, z)$. In this case, the coordinate transforms would be:

{% math() %}
\begin{align*}
x &= r \cos \theta \\
y &= r \sin \theta \\
 z&= z
\end{align*}
{% end %}

A volume element in cylindrical coordinates - which can be thought of as a infinitesimal volume cube, again - would then have the side lengths $dr$, $r d\theta$, and $dz$. So the volume element is $dV = r\,dr\,d\theta\,dz$.

## Vector multivariable calculus

Recall the **gradient operator** is the vector of derivative operators on a multivariable _scalar_ function:

{% math() %}
\nabla f = \left\langle \dfrac{\partial f}{\partial x}, \dfrac{\partial f}{\partial y}, \dfrac{\partial f}{\partial z}\right\rangle
{% end %}

We can now define a *vector* multivariable function $\mathbf{F}(x, y, z)$. This is often known as a **vector field**. A vector field is a quantity that extends across all space that returns a vector for every point in space. We may now define several differential operators on vector fields.

First, we have the **divergence**, given by:

{% math() %}
\operatorname{div}(\mathbf{F}) = \nabla \cdot \mathbf{F}
{% end %}

The notation is suggestive of the actual definition of the divergence:

{% math() %}
\begin{align*}
\nabla \cdot \mathbf{F} &= \left\langle \dfrac{\partial}{\partial x}, \dfrac{\partial}{\partial y}, \dfrac{\partial}{\partial z}\right\rangle  \cdot \langle F_x, F_y, F_z \rangle \\
&= \dfrac{\partial F_x}{\partial x} + \dfrac{\partial F_y}{\partial y} + \dfrac{\partial F_z}{\partial z}
\end{align*}
{% end %}

The divergence can be **interpreted** as a measure of the spread of a vector field. A **positive** divergence means that the vector field is spreading **outwards**; a negative divergence means that the vector field is contracting **inwards**. A zero divergence means that the vector field is neither spreading or contracting (or that the amount of spreading and contracting cancel each other out).

Second, we have the **curl**, given by:

{% math() %}
\operatorname{div}(\mathbf{F}) = \nabla \times \mathbf{F}
{% end %}

The curl in three dimensions is defined by:

{% math() %}
\begin{align*}
\nabla \times \mathbf{F} &=
\begin{vmatrix}
\hat{\mathbf{i}} & \hat{\mathbf{j}} & \hat{\mathbf{k}} \\
\dfrac{\partial}{\partial x} & \dfrac{\partial}{\partial y} & \dfrac{\partial}{\partial z} \\
F_x & F_y & F_z
\end{vmatrix} \\
&= \left(\dfrac{\partial F_z}{\partial y} - \dfrac{\partial F_y}{\partial z}\right)\hat{\mathbf{i}} - \left(\dfrac{\partial F_z}{\partial x} - \dfrac{\partial F_x}{\partial z}\right)\hat{\mathbf{j}} + \left(\dfrac{\partial F_y}{\partial x} - \dfrac{\partial F_x}{\partial y}\right)\hat{\mathbf{k}} 
\end{align*}
{% end %}

In two dimensions this reduces to:

{% math() %}
\nabla \times \mathbf{F} = \dfrac{\partial F_x}{\partial y} - \dfrac{\partial F_y}{\partial x}
{% end %}

The interpretation of the curl is that it describes the **rotational tendency of a vector field**. A nonzero curl means that a vector field will tend to make an object placed within it spin (rotate), with the direction of the rotation based on the. A zero curl means that the vector field is **irrotational**.

A vector field can be described as either **conservative** or **non-conservative**. If a vector field has a **nonzero curl** it is guaranteed to be non-conservative (but zero curl does not _always_ imply a field is conservative). A conservative field $\mathbf{F}$ can be written in the form $\mathbf{F} = \nabla \phi$ where $\phi$ is called a **potential field**.

> The descriptive term **conservative** arises from physics, where conservative vector fields obey the conservation of energy (i.e. that energy can never be created or destroyed). All fundamental fields of nature are conservative, but some non-fundamental fields are **non-conservative**.

## Line integrals

We have already seen integration over an area in the form of area integrals, which we evaluated as **double integrals**. We may also define integration over a curve. Where is this useful? We can use a scalar line integral for calculating some quantity of a curved thin object, such as a wire, a spring, or a cable; for instance, the total charge from the charge density, total mass from the mass density, etc. of a wire. Line integrals are also used extensively in physics for defining the energy transferred by a force along a path, among numerous other applications.

> **Note for the advanced reader:** In addition, in complex analysis, line integrals have very specific uses that are important for **contour integration**, which is important for evaluating some very complex integrals, especially those that appear in quantum field theory.

We denote a line integral over a scalar function as:

{% math() %}
\int_C f(x, y, z) \, ds = \int_{t(a)}^{t(b)} f(r(t)) \|\mathbf{r'}(t)\| \, dt
{% end %}

Here, $ds$ is the line element (a very tiny amount of arc length) and $\mathbf{r}(t)$ is the curve that is integrated over. Recall that $\|\mathbf{r}'(t)\|$ is the speed, given by:

{% math() %}
\mathbf{r}'(t) = \sqrt{\left(\dfrac{dx}{dt}\right)^2 + \left(\dfrac{dy}{dt}\right)^2 + \left(\dfrac{dz}{dt}\right)^2}
{% end %}

A line integral over a _vector-valued function_ can similarly be defined, only with a dot product rather than a regular product:

{% math() %}
\int_C \mathbf{F} \cdot d\mathbf{s} = \int_{t(a)}^{t(b)} \mathbf{F}(t) \cdot \mathbf{r}'(t)\, dt
{% end %}

We must _parametrize_ $f(x, y, z)$ to $f(x(t), y(t), z(t))$ (and similarly parametrize $\mathbf{F}(x, y, z)$ into $\mathbf{F}(x(t), y(t), z(t))$ for vector-valued functions) to actually evaluate line integrals. That is to say, we must convert the equation of a curve to a parametric equation. We can then evaluate the line integral to find its solution. For instance, if we were performing a line integral over a circular loop (a common problem in the physics describing a wire-carrying current), we may choose the parametrization:

{% math() %}
\begin{matrix*}
\begin{align*}
x &= \cos(t) \\
y &= \sin(t) \\
\end{align*},
& t &\in [0, 2\pi]
\end{matrix*}
{% end %}

For which we may then find $x'(t)$ and $y'(t)$. In a similar fashion, we may define a 3D _helix_:

{% math() %}
\begin{matrix*}
\begin{align*}
x &= \cos(t) \\
y &= \sin(t) \\
z &= t
\end{align*},
& t &\in [0, 2\pi]
\end{matrix*}
{% end %}

Or a quadratic curve:

{% math() %}\begin{align*}
x &= t \\
y &= at^2 + b t + c \\
\end{align*}
{% end %}

## Concluding notes

While it may seem like we have covered a lot, our exploration of multivariable calculus is in fact only the _beginning_. Multivariable calculus encompasses a very broad range of topics, and generalizes naturally to vector calculus, as well as more advanced applications of calculus, such as tensor calculus and the calculus of variations, as well as the study of partial differential equations. For those readers interested in more advanced topics, please feel free to read the [vector calculus & advanced topics in calculus guide](@/vector-and-advanced-calculus/index.md) as well as the [introductory guide to partial differential equations](@/intro-pdes/index.md) to continue your journey of learning calculus.