+++
title = "Notes on logarithmic and exponential functions"
date = 2023-09-08
+++

These are notes taken during RPI's MATH 1010 course, relating to a review of exponential and logarithmic functions for calculus.

<!-- more -->

It is recommended to use `Ctrl F` or the equivalent search function to find the relevant section, as these notes are quite long.

## Exponential functions

All exponential functions are in the form $f(x) = b^x$ where $b > 0$ and $b \neq 1$. Note that if $x$ is negative, then $b^{-x} = \left(\frac{1}{b}\right)^x$. All exponential functions go through $(0, 1)$ and never touch the x-axis.

The most commonly-used exponential function is $f(x) = e^x$.

## Logarithmic functions

Logarithmic functions are the inverse of exponential functions. The basic logarithmic function is given by:

{% math() %}
y = \log_b x
{% end %}

Where $b^y = x$. To remember this mapping between exponential functions, you can remember that $b$ is the "basement" (because of its subscript), and it's raised to the "answer" of $y$ to get $x$. Several common logarithmic functions have shorthand notations:

{% math() %}
\ln (x) = \log_e x
{% end %}

{% math() %}
\log(x) = \log_{10} x
{% end %}

## Laws of exponents and logs

The laws of exponents are very useful for simplifying exponential expressions:

{% math() %}
a^x a^y = a^{x + y}
{% end %}

{% math() %}
\frac{a^x}{a^y} = a^{x - y}
{% end %}

{% math() %}
\frac{1}{a^y} = a^{-y}
{% end %}

{% math() %}
(ab)^x = a^x b^x
{% end %}

{% math() %}
(a^x)^y = a^{xy}
{% end %}

{% math() %}
b^x = e^{x \ln b}
{% end %}

{% math() %}
\text{If } a^x = a^y, \text{then } x = y
{% end %}

Similarly, the laws of logs are very useful for simplifying logarithmic expressions:

{% math() %}
\log_b (xy) = \log_b x + \log_b y
{% end %}

{% math() %}
\log_b (x^r) = r \log_b x
{% end %}

{% math() %}
\log_b \left(\frac{x}{y}\right) = \log_b x - \log_b y
{% end %}

{% math() %}
\log_b x = \frac{\ln x}{\ln b}
{% end %}

Be careful! Note that $(\log_b x)^r \neq r \log_b x$!!!
