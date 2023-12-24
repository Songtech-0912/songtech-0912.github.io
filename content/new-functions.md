+++
title = "A new way to define functions"
date = 2023-12-24
+++

When we start to learn about differential equations, one of the first things we're taught about them is that they're often unsolvable - a fact that most students just learn to accept. What we're not often taught is _why_ so many differential equations are considered unsolvable. It turns out, it has everything to do with how we define "solving" a differential equation.

<!-- more -->

Usually, when we talk about solving a differential equations, we refer to a solution that is expressed in terms of elementary functions. For example, consider the differential equation:

$$
\frac{df}{dx} = 2k
$$

The general solution of this differential equation is $f(x) = 2kx + C$. Notice that this solution is _elementary_. That means it is expressed in terms of a finite number of polynomials, power functions, trigonometric functions, exponential functions, and their inverses. These functions lend themselves well to mathematical instruction, given their ubiquity and relative simplicity to understand. But it becomes natural to think: are these functions all the functions that can ever exist?

No! These are a very small subset of all the functions that can exist, and many functions that are smooth, infinitely differentiable, and continuous - in short, functions that lend themselves well to analysis - _aren't_ able to be expressed in terms of elementary functions. It's as if a chef were told to cook with just 2 or 3 ingredients. The chef might know a lot of recipes, but with such few ingredients, the chef can only cook a few of those recipes!

But we don't have to be limited by elementary functions. We can define a much, much larger body of functions in terms of differential equations. Consider, for example, the following differential equation:

$$
\frac{1}{2} k \left(\frac{du}{dx}\right)^2 - Ax^2 = \frac{d^2u}{dx^2}, \quad u(0) = 0, \quad u'(0) = -1
$$

We can use this differential equation to define a new, non-elementary function, which we might name $\text{kin}(x)$ given the differential equation has a kinetic term on the left-hand side. Our function $\text{kin}(x)$ is defined by this differential equation because it is the solution to this differential equation. We can now make any number of functions based on $\text{kin}(x)$, such as:

$$
f(x) = \text{kin}(x) e^{-3x} + \frac{5x^2}{\text{kin}(x)+ 8}
$$
Defining functions with differential equations creates a much, much larger set of functions than the elementary functions.  If we used this much larger set of functions, then **any** differential equation becomes solvable in terms of these functions, their compositions, and their inverses. Isn't that remarkable?

But it makes sense to be a little doubtful of this line of reasoning. Aren't we just creating functions out of thin air this way? To prove that this concept isn't just mathematical sleight of hand, the same idea can be applied towards more familiar functions - such as the transcendental functions. Consider the question of how we would _define_ the exponential function. What about the sine function? Or the cosine function? How to do so isn't immediately obvious, given that these functions, by definition, "transcend" algebra.

However, using differential equations makes this a lot easier. We can define the exponential function with the differential equation:

$$
y' = y, \quad y(0) = 1
$$

Similarly, we can define the sine function with the differential equation:

$$
y'' = -y, \quad y(0) = 0, \quad y'(0) = 1
$$
And we can define the cosine function with the differential equation:

$$
y'' = -y, \quad y(0) = 1, \quad y'(0) = -1
$$

Using compositions of these functions (e.g. defining tangent in terms of sine and cosine), inverses of these functions (e.g. defining $\ln(x)$ as the inverse of $e^x$), or both (e.g. defining $a^x$ with $e^{x \ln a}$), we're able to define all of the common transcendental functions. And crucially, these are solid definitions, because (with a differential equations solver like Runge-Kutta) we can actually compute values for these functions. There is no more need for mere descriptions of a function that fall short of a definition, like "the sine function is a function that oscillates back and forth and repeats every $2\pi$ radians". We can actually rigorously define functions this way. 

They often say that math is a collection of tools invented by mathematicians that we use to reason about our world. Defining functions using differential equations gives us another tool to reveal a fuller picture of the universe - which is quite magical.
