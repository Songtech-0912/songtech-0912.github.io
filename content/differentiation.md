+++
title = "Notes on derivatives for calculus"
date = 2023-09-26
+++

These are notes taken during RPI's MATH 1010 course, on the topic of derivatives and their applications in calculus.

<!-- more -->

Note: some problems are taken Rogawski 4e Calculus Early Transcendentals, the questions are not original work.

## The derivative

The approximate slope of a line is defined by:

{% math() %}
\frac{\Delta f}{\Delta x}
{% end %}

We can express $\Delta f$ as $f(x) - f(a)$, and $\Delta x$ as $x - a$, so we have the slope of a line expressed as:

{% math() %}
\frac{\Delta f}{\Delta x} = \frac{f(x) - f(a)}{x - a}
{% end %}

Using a substitution of variables of $h = x - a$, we can rewrite this definition as:

{% math() %}
\frac{\Delta f}{\Delta x} = \frac{f(a + h) - f(a)}{h}
{% end %}

Now, if we perform another substitution, $x = a$, we get:

{% math() %}
\frac{\Delta f}{\Delta x} = \frac{f(x + h) - f(x)}{h}
{% end %}

This is called the **difference quotient**. By taking the limit of the difference quotient, we find the slope as $\Delta f \rightarrow 0$ and $\Delta x \rightarrow 0$, and we get the true (no longer approximate!) slope of a line:

{% math() %}
\frac{dy}{dx} = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h}
{% end %}

Here, $\frac{dy}{dx}$ is one of the notations for the **derivative** - a function that gives the true slope of the line at any point. We can also notate the derivative with $\frac{df}{dx}$, $\frac{d}{dx} f(x)$, $f'(x)$, or (rarely) $\dot f$.

For instance, suppose we were to compute the derivative of $f(x) = x^2$ at $x = 2$. We have:

{% math() %}
\frac{dy}{dx} = \lim_{h \to 0} \frac{(x + h)^2 - x^2}{h}
{% end %}

Which becomes:

{% math() %}
\lim_{h \to 0} \frac{(x^2 + 2hx + h^2) - x^2}{h}
{% end %}

{% math() %}
\lim_{h \to 0} \frac{2hx + h^2}{h}
{% end %}

{% math() %}
\lim_{h \to 0} 2x + h = 2x
{% end %}

So the derivative $f'(x) = 2x$. Therefore, $f'(2) = 2(2) = 4$. Taking the derivative is a process called **differentiation**.

The **tangent line** to a curve at $x = a$ is expressed by:

{% math() %}
y-y_1 = f'(a) (x- x_1)
{% end %}

And can be computed using the derivative.

## Shorthands for the derivative

Given just the definition of the derivative, the derivative of a constant function $f(x) = C$ is $f'(x) = 0$, and the derivative of a linear function $f(x) = ax + b$ is $f'(x) = a$. The derivative of a power function $f(x) = x^n$ is $f'(x) = nx^{n - 1}$. Derivatives are also _linear_: $\frac{d}{dx} (a f(x) \pm b(g(x)) = a \frac{df}{dx} \pm b \frac{dg}{dx}$.

If the right-hand derivative and left-hand derivative exist but are not **equal** at $x = a$, then $f(x)$ has a **corner** at $x = a$ and is not differentiable at $a$. Differentiability implies continuity, but not the other way around.

## More derivative rules

{% math() %}
\frac{d}{dx} (a^x) = a^x \ln (a)
{% end %}

{% math() %}
\frac{d}{dx} (e^x) = e^x
{% end %}

## Differentiability

If a function is **differentiable** at a point, that implies that:

- It has a **defined** left-hand derivative at the point
- It has a **defined** right-hand derivative at the point
- The left-hand and right-hand derivatives **match**

If a function is differentiable at $x = a$, it is also continuous, and if it is not continuous, then it is **not** differentiable.

## Product rule and quotient rule

The product rule states that:
{% math() %}
(f + g)' = f'g + g'f
{% end %}

The quotient rule states that:

{% math() %}
\left(\frac{f}{g}\right)' = \frac{f'g - g'f}{g^2}
{% end %}

## Higher-order derivative

The nth-order derivative means you are taking the derivative nth times, and is notated with:

{% math() %}
\frac{d^n f}{dx^n}
{% end %}

or (less commonly) $f^{(n)}(x)$.

In general, if a polynomial is of nth degree, every higher-order derivative after the $(n + 1)$ derivative is zero. For example, if our polynomial is $x^8$, then all derivatives above the 9th derivative is zero, so $\frac{d^{100}}{dx^{100}} x^8 = 0$. Additionally, all the higher-order derivatives of $e^x$ are $e^x$.

## Trigonometric derivatives

The fundamental trigonometric derivatives can be derived from the limit definition, and are given by:

{% math() %}
\frac{d}{dx} \sin x = \cos x
{% end %}

{% math() %}
\frac{d}{dx} \cos x = -\sin x
{% end %}

The rest of the trig derivatives can be calculated using trig identities. They are given by:

{% math() %}
\frac{d}{dx} \tan x = \sec^2 x
{% end %}

{% math() %}
\frac{d}{dx} \sec x = \sec x \tan x
{% end %}

{% math() %}
\frac{d}{dx} \csc x = -\csc x \cot x
{% end %}

{% math() %}
\frac{d}{dx} \cot x = -\csc^2 x
{% end %}

## Chain rule

When we have a function $y = f(u)$ where $u = g(x)$, then:

{% math() %}
\frac{dy}{dx} = \frac{df}{du}\frac{du}{dx}
{% end %}

For instance, suppose we want to compute:

{% math() %}
y = \sin(x^3 + 4x^2)
{% end %}

Then $y = \sin(u)$ and $u = x^3 + 4x^2$. Therefore:

{% math() %}
\frac{df}{du} = \cos u = \cos (x^3 + 4x^2)
{% end %}

{% math() %}
\frac{du}{dx} = 3x^2 + 8x
{% end %}

{% math() %}
\frac{dy}{dx} = \frac{df}{du} \frac{du}{dx} = \cos (x^3 + 4x^2)(3x^2 + 8x)
{% end %}

## Implicit differentiation

Consider the equation:

{% math() %}
x^2 + y^2 = 1
{% end %}

Here, $y$ is an implicit function of $x$, that is, $y = y(x)$. But we don't know what $y(x)$ is. We just know that $y$ is a function of $x$, even if we don't know what exactly that function's form is - which is why we call it **implicit**.

If we were to differentiate the entire expression, we have:

{% math() %}
\frac{d}{dx} (x^2 + y^2) = \frac{d}{dx} (1)
{% end %}

The derivative of $x^2$ is easily computed. Meanwhile, we can use the chain rule to differentiate $y^2$:

{% math() %}
\frac{d}{dx} (y^2) = \frac{d}{dx} (y(x)^2) = 2y \frac{dy}{dx}
{% end %}

Because by the chain rule:

{% math() %}
\frac{df}{dx} = \frac{df}{dy}\frac{dy}{dx}
{% end %}

So:

{% math() %}
\frac{d}{dx} (y^2) = \frac{d}{dy} (y^2) \frac{dy}{dx}
{% end %}

Therefore:

{% math() %}
2x + 2y y' = 0
{% end %}

If we solve this in terms of $y'$, we have:

{% math() %}
y'= -\frac{x}{y}
{% end %}

So using implicit differentiation, we are able to find the derivative of $y$, even though we didn't know what exactly the function $y$ was. We can then use that derivative to e.g. find the tangent line to the implicit function, which in this case would be the tangent line to the circle.

Note that derivatives of implicit functions must be checked for domain restrictions (such as division over zero and square root of -1).

We can use implicit differentiation to solve for the derivative of the inverse trig functions:

{% math() %}
y = \sin^{-1}(x)
{% end %}

{% math() %}
\sin(y) = x
{% end %}

{% math() %}
\cos(y) y' = 1
{% end %}

{% math() %}
y' = \frac{1}{\cos y}
{% end %}

But we know that $\cos^2(y) + \sin^2(y) = 1$. Since $\sin(y) = x$, we can say that:

{% math() %}
\cos(y) = \sqrt{1 - x^2}
{% end %}

Therefore, we have:

{% math() %}
y' = \frac{1}{\sqrt{1 - x^2}}
{% end %}

## General exponential function

The general derivative of the exponential function $e^u$ is given by:

{% math() %}
\frac{d}{dx} e^u = e^u \frac{du}{dx}
{% end %}

The derivative of the general exponential function $a^u$ is given by:

{% math() %}
\frac{d}{dx} a^u = a^u \ln(a) \frac{du}{dx}
{% end %}

## Logarithmic function

We want to find the derivative of $\ln(x)$. We can use implicit differentiation to find its derivative:

{% math() %}
y = \ln(x)
{% end %}

{% math() %}
e^y = x
{% end %}

{% math() %}
e^y y' = 1
{% end %}
{% math() %}
y' = \frac{1}{e^y}
{% end %}

But we know that $e^y = x$, therefore:

{% math() %}
y' = \frac{1}{x}
{% end %}

And the general derivative of the natural log function is:

{% math() %}
\frac{d}{dx} \ln(u) = \frac{u'}{u}
{% end %}

The derivative of the general logarithmic function can be found through the change of base formula, and is given by:

{% math() %}
\frac{d}{dx} \log_b (u) = \frac{1}{\ln(b)} \frac{u'}{u}
{% end %}

When doing derivatives of logarithms, using log rules often help simplify a complex logarithm into much simpler logarithms that are easier to evaluate.

## Logarithmic differentiation

Consider the function:

{% math() %}
y = \frac{x(x + 1)^4}{(3x - 1)^{3/2}}
{% end %}

Using log rules, this becomes:

{% math() %}
\ln(y) = \ln(x(x+1)^4) - \ln((3x - 1)^{3/2})
{% end %}

Which we can then simplify to:

{% math() %}
\ln(y) = \ln(x) + 4\ln(x + 1) - \frac{3}{2} \ln(3x -1)
{% end %}

Therefore, differentiating both sides gives us:

{% math() %}
\frac{y'}{y} = \frac{1}{x} + \frac{4}{x + 1} - \frac{9}{2(3x - 1)}
{% end %}

Which we can rewrite as:

{% math() %}
y' = y \left(\frac{1}{x} + \frac{4}{x + 1} - \frac{9}{2(3x - 1)}\right)
{% end %}

If we wanted to, we could replace the $y$ here with our original expression, giving:

{% math() %}
y' = \frac{x(x + 1)^4}{(3x - 1)^{3/2}} \left(\frac{1}{x} + \frac{4}{x + 1} - \frac{9}{2(3x - 1)}\right)
{% end %}

## Related rates

**Related rates** allows us to know how a related variable changes with respect to another variable.

For example, consider $x = y^3 - y$. If we know $\frac{dy}{dt}$, what is $\frac{dx}{dt}$? Well, we can implicitly differentiate to get:

{% math() %}
\frac{d}{dt} x = \frac{d}{dt} (y^3 - y)
{% end %}
{% math() %}
\frac{dx}{dt} = 3y^2 \frac{dy}{dt} - \frac{dy}{dt}
{% end %}

This is our answer! However, typically, we are not presented with the equation that relates two related variables directly, and we must infer it from the question itself.

For example, consider a rectangular box. We want to find $\frac{dx}{dt}$ in terms of other related rates. We can deduce that the volume of a box is given by:

{% math() %}
V = xyz
{% end %}

Thus, if we differentiate both sides:

{% math() %}
\frac{d}{dt} V = \frac{d}{dt} (x y z)
{% end %}

We get:

{% math() %}
\frac{dV}{dt} = yz \frac{dx}{dt} + xz \frac{dy}{dt} + xy \frac{dz}{dt}
{% end %}

Allowing us to find:

{% math() %}
\frac{dx}{dt} = \frac{1}{yz}\left(\frac{dV}{dt} - xz \frac{dy}{dt} + xy \frac{dz}{dt}\right)
{% end %}

## Extreme values

An **absolute** minimum or maximum is when $f(x)$ is at its lowest or highest value respectively for its entire domain. There is only one absolute maximum and one maximum minimum at one function. A **local** minimum or maximum is when $f(x)$ is at its lowest or highest value respectively in an open interval around a specified point.

## Critical points

A **critical point** of $f(x)$ is a point in which $f'(x) = 0$ or undefined within the domain of $f$. Critical points can be saddle points, minima, or maxima.

## Extreme Value Theorem (EVT)

The **EVT** states that if $f(x)$ is continuous on a closed interval $[a, b]$, then both an absolute maximum and absolute minimum exist on the interval. To use the EVT, find all critical points and compare them to the endpoints, and then find the largest and smallest value.

## Rolle's Theorem

**Rolle's Theorem** states that if a function $f(x)$ is continuous on a closed interval $[a, b]$ and differentiable on $(a, b)$, and if $f(a) = f(b)$, then there exists at least point point $x = c$ at which $f'(c) = 0$. It is a special case of the MVT (mean value theorem).

## Mean Value Theorem (MVT)

The **Mean Value Theorem** states that if $f$ is differentiable on $(a, b)$ and continuous on $[a, b]$, then there exists a value $c$ where:

{% math() %}
f'(c) = \frac{f(b) - f(a)}{b - a}
{% end %}

Here, when using the MVT, ensure that the $c$ that is solved for is within the interval! If it is not within the interval, then the MVT does not apply.

## Monotonicity

A **monotonic function** is a function that moves in only one direction, i.e. only increasing or only decreasing. Monotonicity can be determined by the following rules:

- If $f'(x) > 0$ then $f(x)$ is monotonic increasing on $(a, b)$
- If $f'(x) < 0$ then $f(x)$ is monotonic decreasing on $(a, b)$
- Critical points are where functions _may_ (though are not guaranteed to) change monotonicity

## First derivative test

The **first derivative test for local extrema** states that:

- If $f'(x)$ changes sign from $+ \to -$ around $x = c$, $f'(c)$ is a local maximum
- If $f'(x)$ changes sign for $- \to +$ around $x = c$, $f'(c)$ is a local minimum
- If there is no change in sign, $f'(c)$ is neither a maximum nor minimum

Make sure to not just plug in whichever numbers you can compute from the critical points and think you're done! Do not consider critical points that are not in the domain of the original function - for example, if $f(x) = \ln(x)$ and $f'(x) = 1/x$, the point $x = 0$ isn't in the domain of $\ln(x)$ so it is not a valid critical point. Also do not consider functions increasing or increasing on intervals in which they are not defined. For example, the function $f(x) = \frac{e^x}{x}$ cannot be said to be increasing on the interval $(-\infty, e)$ because it has an asymptote at $x = 0$; rather, it can only be said to be increasing on the interval $(-\infty, 0) \cup (0, e)$.

## Concavity & 2nd derivative test

A function is **concave up** if it opens upwards ("smiling"), and **concave down** if it opens downwards ("frowning"). Concavity can be determined through the second derivative: when $f''(x) > 0$, the graph is concave up, and when $f''(x) < 0$, the graph is concave zero.

An **inflection point** is a point a curve changes concavity. That is, at an inflection point, $f''(c) = 0$, and $f''(x)$ switches sign around $x = c$.

The second derivative can also be used to determine local extrema:

- If $f'(c) = 0$ and $f''(c) > 0$ then there is a local max
- If $f'(c) = 0$ and $f''(c) < 0$ then there is a local min
- If $f'(c) = 0$ and $f''(c) = 0$ then the test is inconclusive

## Curve sketching

Using information from the first derivative, second derivative, domain of a function, zeroes, increasing/decreasing intervals, concavity, absolute extrema, local extrema, and asymptotic behavior, the graph of a function can be sketched without needing to explicitly evaluate the function.

## L'Hôpital's Rule

L'Hôpital's Rule states that if a limit is in the form $\frac{f(x)}{g(x)}$ and results in the indeterminate form $\frac{0}{0}$ or $\frac{\infty}{\infty}$, then:

{% math() %}
\lim_{x \to a} \frac{f(x)}{g(x)} = \frac{f'(x)}{g'(x)}
{% end %}

Note that the rule can be applied multiple times until a limit is found.

For the $\frac{0}{\infty}$ form, then the product must be rewritten as a product or quotient. For $0^0, \infty^0, 1^\infty$ then the function $f(x)^{g(x)} = e^{g(x)\ln f(x)}$. For instance, consider the limit:

{% math() %}
\lim_{x \to \infty} x^{1/x^2}
{% end %}

This becomes:

{% math() %}
e^{\lim_{x \to \infty} {\ln(x)/x^2}}
{% end %}

We use L'Hôpital's rule to evaluate the top to get:

{% math() %}
\lim_{x \to \infty} \frac{\ln(x)}{x^2} = 0
{% end %}

So:

{% math() %}
\lim_{x \to \infty} x^{1/x^2} = e^0 = 1
{% end %}

We can also use the rule by turning a limit that is a product functions into a fraction of functions. That is:

{% math() %}
\lim_{x \to a} f(x) g(x) = \lim_{x \to a} \frac{f(x)}{1 / g(x)} = \lim_{x \to a} \frac{g(x)}{1 / f(x)}
{% end %}

## Optimization

Suppose we want to find two numbers $x$ and $y$ such that their sum is 120 and a shape with area $x^2 y$ is as large as possible. That is:

{% math() %}
x + y = 120
{% end %}
{% math() %}
A = x^2 y
{% end %}

To do this, we can solve the first equation for $y$:

{% math() %}
y = 120 - x
{% end %}

Then we can plug it in to the area function:

{% math() %}
A = x^2 (120 - x) = 120x^2 - x^3
{% end %}

We can take the derivative of $A$ to find its maximum:

{% math() %}
\frac{dA}{dx} = 240x - 3x^2
{% end %}

We will consider the domain of the area function - since areas are never negative, $x > 0$ and $y < 0$. So, our critical points must be in that domain.

Here, we set the derivative to zero to get the critical points:

{% math() %}
200x - 3x^2 = 0
{% end %}

Where we have a critical point at $x = \frac{200}{3}$. We can plug that in to solve for $y$:

{% math() %}
y = 120 - x = \frac{160}{3}
{% end %}

So the two numbers are $x = \frac{200}{3}, y = \frac{160}{3}$.

## Linear approximations

From the definition of the derivative we have:

{% math() %}
df = f'(x) dx
{% end %}

Thus:

{% math() %}
\Delta f \approx f'(x) \Delta x
{% end %}

From this, we can find the **linear approximation** of a function at a point $x = a$:

{% math() %}
L(x) = f'(a)(x - a) + f(a)
{% end %}

## Inverse function derivatives

Given a function $f(x)$, the derivative of its inverse is given by:

{% math() %}
\mathrm{inv}'(x) = \frac{1}{f'(\mathrm{inv}(x))}
{% end %}

For instance, consider the function:

{% math() %}
f(x) = \sqrt{x - 4}
{% end %}

First, we want to find the inverse function. To do so, we swap $x$ and $y$:

{% math() %}
x = \sqrt{y - 4}
{% end %}

{% math() %}
x^2 = y - 4
{% end %}

{% math() %}
y = x^2 + 4
{% end %}

{% math() %}
f^{-1} (x) = x^2 + 4
{% end %}

Now, we can find the derivative of our inverse function:

{% math() %}
\mathrm{inv}'(x) = \frac{1}{f'(x^2 + 4)}
{% end %}

{% math() %}
f'(x) = \frac{1}{2\sqrt{x-4}}
{% end %}

{% math() %}
\mathrm{inv}'(x) = \frac{1}{f'(x^2 + 4)}
{% end %}

{% math() %}
\mathrm{inv}'(x) = 2\sqrt{(x^2 + 4) - 4}
{% end %}

We finally obtain:

{% math() %}
\mathrm{inv}'(x) = 2x
{% end %}
