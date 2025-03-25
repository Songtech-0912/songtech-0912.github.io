+++
title = "Feynmann's technique for integration"
date = 2023-09-11

[extra]
notoc = true
+++

Feynmann's technique is a technique for evaluating certain difficult definite integrals. Note **definite integral** here, it doesn't do anything to help find antiderivatives. In fact, Feynmann's technique is _especially_ helpful with finding definite integrals that have no elementary antiderivative.

<!-- more -->

The formula for Feynmann's technique is surprisingly simple:

{% math() %}
\frac{d}{dt} \int f(x, t) dx = \int \frac{\partial f}{\partial t} f(x, t) dx
{% end %}

And the method is too - just 4 steps:

- Parametrize the integral with $t$ to form a new integral $I(t)$
- Differentiate $I(t)$ under the integral sign to find $I'(t)$
- Integrate the derivative: $I(t) = \int I'(t) dt$
- Solve for $I(1)$

Consider:

{% math() %}
\int \limits_0^1 \ln(x) dx
{% end %}

To use Feynmann's trick, we need to add a second variable $t$ to a convenient place inside our function, making a new function $I(t)$. Here there's really only one place to put it, so we define $I(t)$ as:

{% math() %}
I(t) = \int \limits_0^1 \ln(xt) dx
{% end %}

Now notice $I(1)$ is equal to our original integral:

{% math() %}
I(1) = \int \limits_0^1 \ln(x \cdot 1)dx = \int \limits_0^1 \ln(x) dx
{% end %}

So the key to evaluating our integral is to find out what $I(1)$ is. But surely this isn't easy, you say? Didn't we just make our original integral more complicated?

At first glance, yes. But notice that we can take the derivative of $I$, to get:

{% math() %}
I'(t) = \frac{d}{dt} \int \limits_0^1 \ln(tx) dx = \int \limits_0^1 \frac{\partial}{\partial t}\ln (tx) dx
{% end %}

{% math() %}
I'(t) = \int \limits_0^1 \frac{1}{t} dx = \frac{1}{t}
{% end %}

Now, we can evaluate $I(t)$ by taking the integral of $I'(t)$:

{% math() %}
I(t) = \int I'(t) dt = \ln(t) + C
{% end %}

We can find out $C$ by finding an appropriate value of $t$ that will yield a constant for $I(t)$. This is really the biggest limitation of Feynmann's integral trick - you have to have functions in a form where substituting in a value for $t$ cancels out an integral and leaves you with a number. In our case, we'll skip ahead and just note that $C = -1$. So:

{% math() %}
I(1) = \ln(1) + C = 0 + (-1) = -1
{% end %}
