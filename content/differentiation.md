+++
title = "Notes on derivatives for calculus"
date = 2023-09-26
+++

These are notes taken during RPI's MATH 1010 course, on the topic of derivatives and their applications in calculus.

<!-- more -->

Note: some problems are taken Rogawski 4e Calculus Early Transcendentals, the questions are not original work.

## The derivative

The approximate slope of a line is defined by:

$$
\frac{\Delta f}{\Delta x}
$$

We can express $\Delta f$ as $f(x) - f(a)$, and $\Delta x$ as $x - a$, so we have the slope of a line expressed as:

$$
\frac{\Delta f}{\Delta x} = \frac{f(x) - f(a)}{x - a}
$$

Using a substitution of variables of $h = x - a$, we can rewrite this definition as:

$$
\frac{\Delta f}{\Delta x} = \frac{f(a + h) - f(a)}{h}
$$

Now, if we perform another substitution, $x = a$, we get:

$$
\frac{\Delta f}{\Delta x} = \frac{f(x + h) - f(x)}{h}
$$

This is called the **difference quotient**. By taking the limit of the difference quotient, we find the slope as $\Delta f \rightarrow 0$ and $\Delta x \rightarrow 0$, and we get the true (no longer approximate!) slope of a line:

$$
\frac{dy}{dx} = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h}
$$

Here, $\frac{dy}{dx}$ is one of the notations for the **derivative** - a function that gives the true slope of the line at any point. We can also notate the derivative with $\frac{df}{dx}$, $\frac{d}{dx} f(x)$, $f'(x)$, or (rarely) $\dot f$.

For instance, suppose we were to compute the derivative of $f(x) = x^2$ at $x = 2$. We have:

$$
\frac{dy}{dx} = \lim_{h \to 0} \frac{(x + h)^2 - x^2}{h}
$$

Which becomes:

$$
\lim_{h \to 0} \frac{(x^2 + 2hx + h^2) - x^2}{h}
$$

$$
\lim_{h \to 0} \frac{2hx + h^2}{h}
$$

$$
\lim_{h \to 0} 2x + h = 2x
$$

So the derivative $f'(x) = 2x$. Therefore, $f'(2) = 2(2) = 4$. Taking the derivative is a process called **differentiation**.

The **tangent line** to a curve at $x = a$ is expressed by:

$$
y-y_1 = f'(a) (x- x_1)
$$

And can be computed using the derivative.

## Shorthands for the derivative

Given just the definition of the derivative, the derivative of a constant function $f(x) = C$ is $f'(x) = 0$, and the derivative of a linear function $f(x) = ax + b$ is $f'(x) = a$. The derivative of a power function $f(x) = x^n$ is $f'(x) = nx^{n - 1}$. Derivatives are also _linear_: $\frac{d}{dx} (a f(x) \pm b(g(x)) = a \frac{df}{dx} \pm b \frac{dg}{dx}$.

If the right-hand derivative and left-hand derivative exist but are not **equal** at $x = a$, then $f(x)$ has a **corner** at $x = a$ and is not differentiable at $a$. Differentiability implies continuity, but not the other way around.

## More derivative rules

$$
\frac{d}{dx} (a^x) = a^x \ln (a)
$$

$$
\frac{d}{dx} (e^x) = e^x
$$

