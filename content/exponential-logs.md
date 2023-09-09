+++
title = "Notes on logarithmic and exponential functions"
+++

These are notes taken during RPI's MATH 1010 course, relating to a review of exponential and logarithmic functions for calculus.

<!-- more -->

It is recommended to use `Ctrl F` or the equivalent search function to find the relevant section, as these notes are quite long.

## Exponential functions

All exponential functions are in the form $f(x) = b^x$ where $b > 0$ and $b \neq 1$. Note that if $x$ is negative, then $b^{-x} = \left(\frac{1}{b}\right)^x$. All exponential functions go through $(0, 1)$ and never touch the x-axis.

The most commonly-used exponential function is $f(x) = e^x$.

## Logarithmic functions

Logarithmic functions are the inverse of exponential functions. The basic logarithmic function is given by:

$$
y = \log_b x
$$

Where $b^y = x$. To remember this mapping between exponential functions, you can remember that $b$ is the "basement" (because of its subscript), and it's raised to the "answer" of $y$ to get $x$. Several common logarithmic functions have shorthand notations:

$$
\ln (x) = \log_e x
$$

$$
\log(x) = \log_{10} x
$$

## Laws of exponents and logs

The laws of exponents are very useful for simplifying exponential expressions:

$$
a^x a^y = a^{x + y}
$$

$$
\frac{a^x}{a^y} = a^{x - y}
$$

$$
\frac{1}{a^y} = a^{-y}
$$

$$
(ab)^x = a^x b^x
$$

$$
(a^x)^y = a^{xy}
$$

$$
b^x = e^{x \ln b}
$$

$$
\text{If } a^x = a^y, \text{then } x = y
$$

Similarly, the laws of logs are very useful for simplifying logarithmic expressions:

$$
\log_b (xy) = \log_b x + \log_b y
$$

$$
\log_b (x^r) = r \log_b x
$$

$$
\log_b \left(\frac{x}{y}\right) = \log_b x - \log_b y
$$

$$
\log_b x = \frac{\ln x}{\ln b}
$$

Be careful! Note that $(\log_b x)^r \neq r \log_b x$!!!
