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

## Differentiability

If a function is **differentiable** at a point, that implies that:

- It has a **defined** left-hand derivative at the point
- It has a **defined** right-hand derivative at the point
- The left-hand and right-hand derivatives **match**

If a function is differentiable at $x = a$, it is also continuous, and if it is not continuous, then it is **not** differentiable.

## Product rule and quotient rule

The product rule states that:
$$
(f + g)' = f'g + g'f
$$

The quotient rule states that:

$$
\left(\frac{f}{g}\right)' = \frac{f'g - g'f}{g^2}
$$

## Higher-order derivative

The nth-order derivative means you are taking the derivative nth times, and is notated with:

$$
\frac{d^n f}{dx^n}
$$

or (less commonly) $f^{(n)}(x)$.

In general, if a polynomial is of nth degree, every higher-order derivative after the $(n + 1)$ derivative is zero. For example, if our polynomial is $x^8$, then all derivatives above the 9th derivative is zero, so $\frac{d^{100}}{dx^{100}} x^8 = 0$. Additionally, all the higher-order derivatives of $e^x$ are $e^x$.

## Trigonometric derivatives

The fundamental trigonometric derivatives can be derived from the limit definition, and are given by:

$$
\frac{d}{dx} \sin x = \cos x
$$

$$
\frac{d}{dx} \cos x = -\sin x
$$

The rest of the trig derivatives can be calculated using trig identities. They are given by:

$$
\frac{d}{dx} \tan x = \sec^2 x
$$

$$
\frac{d}{dx} \sec x = \sec x \tan x
$$

$$
\frac{d}{dx} \csc x = -\csc x \cot x
$$

$$
\frac{d}{dx} \cot x = -\csc^2 x
$$

## Chain rule

When we have a function $y = f(u)$ where $u = g(x)$, then:

$$
\frac{dy}{dx} = \frac{df}{du}\frac{du}{dx}
$$

For instance, suppose we want to compute:

$$
y = \sin(x^3 + 4x^2)
$$

Then $y = \sin(u)$ and $u = x^3 + 4x^2$. Therefore:

$$
\frac{df}{du} = \cos u = \cos (x^3 + 4x^2)
$$

$$
\frac{du}{dx} = 3x^2 + 8x
$$

$$
\frac{dy}{dx} = \frac{df}{du} \frac{du}{dx} = \cos (x^3 + 4x^2)(3x^2 + 8x)
$$

## Implicit differentiation

Consider the equation:

$$
x^2 + y^2 = 1
$$

Here, $y$ is an implicit function of $x$, that is, $y = y(x)$. But we don't know what $y(x)$ is. We just know that $y$ is a function of $x$, even if we don't know what exactly that function's form is - which is why we call it **implicit**.

If we were to differentiate the entire expression, we have:

$$
\frac{d}{dx} (x^2 + y^2) = \frac{d}{dx} (1)
$$

The derivative of $x^2$ is easily computed. Meanwhile, we can use the chain rule to differentiate $y^2$:

$$
\frac{d}{dx} (y^2) = \frac{d}{dx} (y(x)^2) = 2y \frac{dy}{dx}
$$

Because by the chain rule:

$$
\frac{df}{dx} = \frac{df}{dy}\frac{dy}{dx}
$$

So:

$$
\frac{d}{dx} (y^2) = \frac{d}{dy} (y^2) \frac{dy}{dx}
$$

Therefore:

$$
2x + 2y y' = 0
$$

If we solve this in terms of $y'$, we have:

$$
y'= -\frac{x}{y}
$$

So using implicit differentiation, we are able to find the derivative of $y$, even though we didn't know what exactly the function $y$ was. We can then use that derivative to e.g. find the tangent line to the implicit function, which in this case would be the tangent line to the circle.

Note that derivatives of implicit functions must be checked for domain restrictions (such as division over zero and square root of -1).

We can use implicit differentiation to solve for the derivative of the inverse trig functions:

$$
y = \sin^{-1}(x)
$$

$$
\sin(y) = x
$$

$$
\cos(y) y' = 1
$$

$$
y' = \frac{1}{\cos y}
$$

But we know that $\cos^2(y) + \sin^2(y) = 1$. Since $\sin(y) = x$, we can say that:

$$
\cos(y) = \sqrt{1 - x^2}
$$

Therefore, we have:

$$
y' = \frac{1}{\sqrt{1 - x^2}}
$$
