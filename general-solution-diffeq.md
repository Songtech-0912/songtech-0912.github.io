+++
title = "A general way to approximately solve any differential equation"
date = 2024-08-03
draft = true
+++

In general, the words "general solution" and "differential equation" don't go together very much. _Most_ differential equations do not have general solutions that can be easily found. Some do not even have _any_ general solution that can be expressed in closed-form (i.e. with a finite number of terms). But there is a way to approximately solve any differential equation analytically, which is not always commonly taught.

<!-- more -->

The idea is to use Taylor series. Remember that since a differential equation gives an expression for the derivative, we can simply continuously differentiate the differential equation to find any nth-order derivative. Then using these values, we can construct a Taylor series. Here is an explanation.

------

The same approach works for partial differential equations with the multivariable Taylor series.

For instance, we can solve the heat equation using this method.

Sometimes, we can see a pattern in this set of repeating terms, indicating that the solution can be expressed in a nice form. If we are really _really_ lucky we might even get a closed-form solution, and once in a blue moon we get a closed-form solution expressed in terms of elementary (i.e. familiar) functions. But usually there isn't a pattern, and we just have to keep computing and computing terms until we get to the accuracy we want. For this, we can use the Taylor error bound to find the number of terms we need:

{% math() %}
\mathcal{e}_n(x) = \frac{M}{(n + 1)!}(x - a)^{n + 1}
{% end %}

For typical cases, computing over a hundred terms, or even a few hundred, is necessary to get good results. With smooth interpolation and shifting the starting point $a$ adaptively every few terms to construct a new Taylor approximation at that point, we can use fewer terms. So what's the point of this? Because _computers_ can do this quickly and efficiently with automatic differentiation, and cache results.
