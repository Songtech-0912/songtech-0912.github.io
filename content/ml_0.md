+++
title = "Building a neural network library in Rust, part 0"
date = 2023-05-25
+++

This is the first article in a multi-part series detailing the process of building a neural network library in pure Rust, based off my experience making the [`elara-math`](https://github.com/elaraproject/elara-math) library.

<!-- more -->

## What is a neural network?

Put simply, a neural network is just a mathematical model for predicting a value given existing values. The simplest neural networks, one-layer feedforward neural networks, are basically just a linear function:

{% math() %}
y = \sigma(mx + b)
{% end %}

Here, $x$ is the inputs given to the neural network, and $y$ is the outputs it predicts. $m$ and $b$ are often called the _weights_ and _biases_ of the neural network, and act as parameters to adjust to make the neural network predict different things. $\sigma(x)$ is called an _activation function_, and often is the sigmoid function:

{% math() %}
f(x) = \frac{1}{1 + e^{-x}}
{% end %}

The activation function is used to "squish" any value the neural network predicts, from $-\infty$ to $\infty$, to a value between 0 and 1.

The trick to making a neural network "learn" is to measure a _loss_ - that is, a measure of how much the prediction of a neural network deviates from the expected value. The loss function is typically the **mean squared error**, which looks like this:

{% math() %}
\mathcal{L} = \frac{1}{n} \sum_{i = 0}^n (\hat y - y)^2
{% end %}

Then, we take the gradient of the loss to find out how much a small change in the weights and biases will affect the loss. We then adjust the weights and biases so that the new weights and biases will have a lower loss:

{% math() %}
w = w - \nabla \mathcal{L} \cdot \mu \\
b = b - \nabla \mathcal{L} \cdot \mu
{% end %}

Note that here, $\mu$ is the learning rate, which is how much we want to adjust the neural network given the gradient.

We repeat this process until the loss is as low as desired. The neural network, by this point, should be very accurate in making its predictions.

## How to autodiff

Automatic differentiation is the heart of machine learning, and it involves a technique to automatically calculate the gradient of a function - often, the loss function. To demonstrate this, suppose we had a value $z$, defined as:

{% math() %}
z = 2x + 3y
{% end %}

We want to find the values of $\frac{\partial z}{\partial x}$ and $\frac{\partial z}{\partial y}$. One way to do this is to break down $z$ by rewriting it in terms of two _intermediary variables_ $a$ and $b$:

{% math() %}
a = 2x \\
b = 3y \\
z = a + b
{% end %}

Then:

{% math() %}
\begin{align*}
\frac{\partial z}{\partial x} &= \frac{\partial z}{\partial a}
\frac{\partial a}{\partial x} \\
\frac{\partial z}{\partial y} &= \frac{\partial z}{\partial a}
\frac{\partial a}{\partial y}
\end{align*}
{% end %}

This is really just the multivariable chain rule, and it is the basic technique by which automatic differentiation works. In Rust, this is implemented through a `Value` struct:

```rust
pub struct ValueData {
    pub data: f64,
    pub grad: f64,
    pub uuid: Uuid,
    pub _backward: Option<fn(value: &ValueData)>,
    pub _prev: Vec<Value>,
    pub _op: Option<String>,
}

#[derive(Clone)]
pub struct Value(Rc<RefCell<ValueData>>);
```

And operations are implemented on `Value` in such a way that it transforms the gradient according to the derivative properties every time `Value` is changed. Then, if we set initial values of 1 for $\frac{\partial a}{\partial x}$ and $\frac{\partial a}{\partial y}$, we can find all the partial derivatives of $z$.

Finally, it would be helpful to talk about the difference between forward-mode automatic differentiation, which was shown earlier, and _reverse-mode_ automatic differentiation. Reverse-mode automatic differentiation is simply turning forward-mode upside down, so:

{% math() %}
\begin{align*}
\frac{\partial z}{\partial x} &= \frac{\partial a}{\partial x}
\frac{\partial z}{\partial a} \\
\frac{\partial z}{\partial y} &= \frac{\partial a}{\partial y}
\frac{\partial z}{\partial a}
\end{align*}
{% end %}

This means that while forward-mode yields every output derivative given a single input, reverse-mode yields every input derivative given a single output - drastically speeding up automatic differentiation for training neural networks.

## How to make a neural network in Rust

The key building blocks of a neural network are three components:

- A (preferably fast!) n-dimensional array
- An automatic differentiation library
- A tensor class (in Rust, it would be a struct)

While building my personal neural network library [`elara-math`](https://github.com/elaraproject/elara-math), I aimed to build all three components from scratch in pure Rust, using as few dependencies as possible.

To start with, I built `NdArray`, my n-dimensional array, by heavily referencing [nd_array](https://crates.io/crates/nd_array). The trick both `elara-math` and `nd_array` used for fast n-dimensional arrays is to define `NdArray` like so:

```rust
#[derive(Debug, Clone)]
pub struct NdArray<T: Clone, const N: usize> {
    pub shape: [usize; N],
    pub data: Vec<T>,
}
```

Essentially, the `NdArray` holds a vector containing the elements of the array, and the shape of the array. This means that indexing operations on the `NdArray` are computed as indexing a single flat vector, rather than nested vectors, making `NdArrays` in theory very performant.

However, I intended to get to a working implementation of a `Tensor` as quick as possible. To do this, I used Ramil Aleskerov's excellent [Rustygrad](https://github.com/Mathemmagician/rustygrad) library, which provided a differentiable `Value`datatype. I then implemented tensors with:

```rust
pub struct Tensor<const N: usize>(NdArray<Value, N>);
```

To backpropagate the gradients, I simply implemented a map operation on the underlying `NdArray` of `Values`:

```rust
pub fn backward(&mut self) {
    self.0.mapv(|val: Value| val.backward());
}
```

And to get the gradient, I also used a map to get the gradient of each component `Value` in the `Tensor`:

```rust
pub fn grad(&mut self) -> NdArray<f64, N> {
    let data = self.0.data.clone();
    let gradients = data.into_iter().map(move |val| val.borrow().grad).collect();
    NdArray {
        data: gradients,
        shape: self.0.shape
    }
}
```

Since `Values` already have arithmetic operations implemented, it was comparatively easy to implement the same operations for tensors. For example, implementing elementwise addition was simply:

```rust
impl<const N: usize> Add<&Tensor<N>> for &Tensor<N> {
    type Output = Tensor<N>;
    fn add(self, rhs: &Tensor<N>) -> Self::Output {
        Tensor::new(&self.0 + &rhs.0)
    }
}
```

## Future work

The slight issue with `elara-math` is that at present, it is _very_ slow - much, much slower than PyTorch. This is mainly due to the fact that `Tensor` is essentially an `NdArray` of owned`Values`, and so operations with Tensors are cumbersome and slow, because `Values` have to be allocated and reallocated. A future better implementation would "bake in" the automatic differentation into the tensors, so this is not an issue.
