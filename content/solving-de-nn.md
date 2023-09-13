+++
title = "Solving ODEs and PDEs with neural networks"
date = 2023-09-07
+++

Typical numerical methods to solve ordinary differential equations and especially partial differential equations require very fine grids to be able to attain accurate results, and suffer from the curse of dimensionality. This is an alternate method to solve ODEs and PDEs with neural networks, which solves both these issues.

<!-- more -->

We will first explore the ODE case, and then move onto the PDE case.

## ODE case

Given a general ODE in the form:

$$
\frac{dy}{dx} = f(x, y)
$$

$$
y(0) = k
$$

A custom loss function can be written as follows:

$$
L = (y' - f(x, y))^2 + (y(0) - k)^2
$$

If we take the neural network's output prediction to be $N(x, a)$, where $a$ denotes the parameters storing the weights and biases of the model, then we can rewrite the above loss function as:

$$
L(a, x) = (N'(a, x) - f(x, N(a, x)))^2 + (N(a, 0) - k)^2
$$

Where $N'(a, x)$ can be calculated through automatic differentiation of the model. Then we can optimize with gradient descent given learning rate $\gamma$ to yield:

$$
a_{n + 1} = a_n - \gamma \nabla L(a, x)
$$

## PDE case

Suppose we want to solve the 1D wave equation:

$$
\frac{\partial^2 u}{\partial t^2} = c^2 \frac{\partial^2 u}{\partial x^2}
$$

with the initial condition:

$$
u(x, 0) = u_0(x)
$$

The wave equation, as with any PDE, can be written in the form $F(x, t) = 0$, where:

$$
F(x, t) = \frac{\partial^2 u}{\partial t^2} - c^2 \frac{\partial^2 u}{\partial x^2}
$$

We want the neural network to learn the solution $u(x, t)$, so we make a general model $\hat u(x, t)$ that should converge to $u(x, t)$ after training:

```py
# Basic model to represent u(x, t)
def model(params, x, t):
    w, b = params
    output = (x * w + t * w) + b
    return sigmoid(output)
```

Thus, given our wave equation, we can define a custom loss function $L(a, x, t)$, where $a$ denotes the matrix of weights and biases:

$$
L(a, x, t) = \frac{1}{n} \sum_{i=0}^n (F(x_i, t_i))^2 - \frac{1}{n} \sum_{i = 0}^n (\hat u(x_i, 0) - u_0(x_i))^2
$$

Where $u_0(x)$ denotes the initial conditions of the PDE we set. Note here that the $\frac{1}{n} \sum$ term is just taking the mean of $F(x, t)$ as it is an array, not a scalar, when trained. Thus, through the same method of gradient descent, the neural network learns the function $u(x, t)$:

$$
a_{n + 1} = a_n - \gamma \nabla L(a, x, t)
$$
