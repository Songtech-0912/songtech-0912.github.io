+++
title = "Solving ODEs and PDEs with neural networks"
date = 2023-09-07
+++

Typical numerical methods to solve ordinary differential equations and especially partial differential equations require very fine grids to be able to attain accurate results, and suffer from the curse of dimensionality. This is an alternate method to solve ODEs and PDEs with neural networks, which solves both these issues.

<!-- more -->

We will first explore the ODE case, and then move onto the PDE case.

## ODE case

Given a general ODE in the form:

{% math() %}
\frac{dy}{dx} = f(x, y)
{% end %}

{% math() %}
y(0) = k
{% end %}

A custom loss function can be written as follows:

{% math() %}
L = \frac{1}{n} \sum_{i = 0}^n (y' - f(x, y))^2 + (y(0) - k)^2
{% end %}

If we take the neural network's output prediction to be $N(x, a)$, where $a$ denotes the parameters storing the weights and biases of the model, then we can rewrite the above loss function as:

{% math() %}
L(a, x) = \frac{1}{n} \sum_{i = 0}^n (N'(a, x) - f(x, N(a, x)))^2 + (N(a, 0) - k)^2
{% end %}

Where $N'(a, x)$ can be calculated through automatic differentiation of the model. Then we can optimize with gradient descent given learning rate $\gamma$ to yield:

{% math() %}
a_{n + 1} = a_n - \gamma \nabla L(a, x)
{% end %}

## PDE case

Suppose we want to solve the 1D wave equation:

{% math() %}
\frac{\partial^2 u}{\partial t^2} = c^2 \frac{\partial^2 u}{\partial x^2}
{% end %}

The wave equation, as with any PDE, can be written in the form $F(x, t) = 0$, where:

{% math() %}
F(x, t) = \frac{\partial^2 u}{\partial t^2} - c^2 \frac{\partial^2 u}{\partial x^2}
{% end %}

We also need to specify the initial condition:

{% math() %}
u(x, 0) = u_0(x)
{% end %}

The initial condition describes how the PDE behaves at $t = 0$, and for the wave equation, a common initial condition is that $u_0(x) = \sin(x)$. But the initial condition is not enough to make a solution unique - and we need unique solutions to model real-life phenomena. In addition to the initial condition, we need boundary conditions, which describe how the PDE behaves as you move far away from the center of the PDE:

{% math() %}
\text{BC} = \lim_{x \to \pm \infty} u(x, t)
{% end %}

Note that the previous equation is true for the 1D case, but for 2D, 3D, and higher dimensional cases, the more general interpretation is that:

{% math() %}
\text{BC} = \lim_{r \to \pm \infty} u(x, t)
{% end %}

where $r$ is the radial distance from the origin. For the wave equation, since we're solving on a finite, not infinite, domain, we can replace $\pm \infty$ with the edges of the domain. For instance, if we were solving on $x \in [0, L]$, then the spatial boundary conditions could be that the wave vanishes as $x$ approaches the edges of its domain:

{% math() %}
u(0, t) = 0
{% end %}

{% math() %}
u(L, t) = 0
{% end %}

We want the neural network to learn the solution $u(x, t)$, so we make a general model $\hat u(x, t)$ that should converge to $u(x, t)$ after training:

```py
# Basic model to represent u(x, t)
def model(params, x, t):
    w, b = params
    output = (x * w[0] + t * w[1]) + b
    return sigmoid(output)
```

Thus, given our wave equation, we can define a custom loss function $L(a, x, t)$, where $\hat u$ denotes the model being trained:

{% math() %}
L(x, t) = \frac{1}{n} \sum_{i=0}^n (F(x_i, t_i))^2 + \frac{1}{n} \sum_{i = 0}^n (\hat u(x_i, 0) - u_0(x_i))^2 + \frac{1}{n} \sum_{i = 0}^n (\hat u(0, t) - \mathrm{BC_1})^2 + \frac{1}{n} \sum_{i = 0}^n (\hat u(L, t) - \mathrm{BC_2})^2
{% end %}

Where $u_0(x)$ denotes the initial conditions of the PDE we set. Note here that the $\frac{1}{n} \sum$ term is just taking the mean of $F(x, t)$ as it is an array, not a scalar, when trained. Thus, through the same method of gradient descent, the neural network learns the function $u(x, t)$:

{% math() %}
a_{n + 1} = a_n - \gamma \nabla L(a, x, t)
{% end %}

For a full implementation of both the ODE and PDE examples, see <https://github.com/Songtech-0912/NN-DE-solvers>.
