+++
title = "Notes on a review of trigonometry"
date = 2023-09-01
+++

These are notes taken during RPI's MATH 1010 course, relating to a review of trigonometry for calculus.

<!-- more -->

It is recommended to use `Ctrl F` or the equivalent search function to find the relevant section, as these notes are quite long.

## Trigonometric functions

Trigonometric functions are functions of **angles**. An angle is positive when measured counterclockwise from the initial ray, and negative when measured counterclockwise from the initial ray. Calculus typically uses **radians**, where $2\pi$ radians is equal to 360 degrees.

| Angle in degree | Angle in radian |
|---|---|
| 0 | 0 |
| $30^\degree$ | $\frac{\pi}{6}$ |
| $45^\degree$ | $\frac{\pi}{4}$ |
| $60^\degree$ | $\frac{\pi}{3}$ |
| $90^\degree$ | $\frac{\pi}{2}$ |

Angles in degrees can be converted to radians by multiplying by:

$$
\frac{\pi}{180}
$$

Similarly, angles in radians can be converted to degrees by multiplying by:

$$
\frac{180}{\pi}
$$
## Trigonometric relations

$$
\tan \theta = \frac{\sin \theta}{\cos \theta}
$$

$$
\csc \theta = \frac{1}{\sin \theta}
$$

$$
\sec \theta = \frac{1}{\cos \theta}
$$

$$
\cot \theta = \frac{1}{\tan \theta}
$$

## The trig song for remembering trig functions

_Mr. Darnbrook, wherever you are - countless students will thank you for this song you taught me 5 years ago..._

One, two three!

Three, two, one!

Two under the bar!

Square root all that's not one!

Square root of three over three!

One, square root of three!

Now that you know the song!

You can sing it again, to me!

*And this is how you get to this:*

| | 30 degrees  / $\frac{\pi}{6}$           | 45 degrees $\frac{\pi}{4}$           | 60 degrees/ $\frac{\pi}{3}$ |
| ------- | -------------------- | -------------------- | -------------------- |
| $\sin$ | $\frac{1}{2}$ | $\frac{\sqrt{2}}{2}$ | $\frac{\sqrt{3}}{2}$ |
| $\cos$ | $\frac{\sqrt{3}}{2}$ | $\frac{\sqrt{2}}{2}$ | $\frac{1}{2}$  |
| $\tan$ | $\frac{\sqrt{3}}{3}$ | $1$  | $\sqrt{3}$           |

**Explanation:**

"One, Two, Three" is the top of the first row of the table

"Three, Two, One" is the top of the second row

"Two under the bar" means to make 2 the denominator of every number (so 1 will become $\frac{1}{2}$, 2 will become $\frac{2}{2}$, you get the idea)

"Square root all that's not one" means to add a square root to every numerator (in rows 1) and 2) that, as you might have guessed, is **not 1**)

"Square root of three over three" is for the first column of the third row ($\tan 30^\circ$)

"One, square root of three" is for the second and third columns of the third row ($\tan 45^\circ$ and $\tan 60^\circ$)

And you've got that done!

## Signs of the trig functions

The trig functions obey:

| Quadrant | Sign |
|-----------|------|
| Quadrant I | **A**ll are positive |
| Quadrant II | **S**ine is positive, rest are negative |
| Quadrant III | **T**angent is positive, rest are negative |
| Quadrant IV | **C**osine is positive, rest are negative |

You can remember this with the acronym **A**ll **S**tudents **T**ake **C**alculus. For (positive) trig angles greater than $2\pi$, we can find the quadrant of the angle by subtracting the greatest multiple of $2\pi$ - for negative, do the same but add the greatest multiple of $2\pi$.

## Reference angles

For all angles in the form:

$$
\theta = \frac{k\pi}{n}
$$

The reference angle is:

$$
\frac{\pi}{n}
$$

For instance, the reference angle of $\frac{5\pi}{6}$ is $\frac{\pi}{6}$.

## Simplifying angles

For any angle that is greater than $\pm 2\pi$:

$$
\sin \theta = \sin(\theta \pm 2n\pi)
$$
$$
\cos \theta = \cos(\theta \pm 2n\pi)
$$
$$
\tan \theta = \tan(\theta \pm 2n\pi)
$$

where $n$ is any positive integer. Therefore, $\sin\left(\frac{9\pi}{4}\right) = \sin\left(\frac{\pi}{4}\right)$, and $\cos \left(-\frac{11\pi}{3}\right) =  \cos \left(-\frac{5\pi}{3}\right)$. This can be used to simplify a very large angle into a much smaller one that can be more easy to work with.

## Finding the trig values of an arbitrary angle

Let's say we want to find the value of the trig functions at $\theta = -\frac{3\pi}{4}$.

First, we know that $-\frac{3\pi}{4}$ is an integer multiple of $\frac{\pi}{4}$, so we know that the reference angle is $\frac{\pi}{4}$.

We can then use the trig song to find the values of the trig functions at $\frac{\pi}{4}$:

$$
\sin \frac{\pi}{4} = \frac{\sqrt{2}}{2}
$$

$$
\cos \frac{\pi}{4} = \frac{\sqrt{2}}{2}
$$

$$
\tan \frac{\pi}{4} = 1
$$

But remember that $-\frac{3\pi}{4}$ is  in the 3rd quadrant, where (using "all students take calculus") only tangent is positive. So we apply the correct signs (-sin, -cos, +tan):

$$
\sin \left(-\frac{3\pi}{4}\right) = -\frac{\sqrt{2}}{2}
$$

$$
\cos \left(-\frac{3\pi}{4}\right) = -\frac{\sqrt{2}}{2}
$$

$$
\cos \left(-\frac{3\pi}{4}\right) = +1 = 1
$$

## Trig identities

The Pythagorean identities are easiest to remember. The first pythagorean identity is:

$$
\sin^2 \theta + \cos^2 \theta = 1
$$

If we divide both sides by $\cos^2 \theta$ we get the second pythagorean identity:

$$
1 + \tan^2 \theta = \sec^2 \theta
$$

Finally, if we add "co" to the second identity (tangent -> "co" tangent, secant -> "co" secant), we get the third:

$$
1 + \cot^2 \theta = \csc^2 \theta
$$

Finally, the half-angle and double-angle formulas are useful:

$$
\cos^2 \theta = \frac{1 + \cos (2\theta)}{2}
$$

$$
\sin^2 \theta = \frac{1 - \cos (2\theta)}{2}
$$

$$
\cos (2\theta) = \cos^2 \theta - \sin^2 \theta
$$

$$
\sin (2\theta) = 2\cos\theta\sin\theta
$$

## Solving trig equations

A solution $\theta$ of $\sin \theta = k$ satisfies the fact that if you know one solution $\theta_1$ of the equation, then:

$$
\theta = \pm \theta_1 + 2\pi n
$$
Similarly, a solution of $\theta_1$ of $\cos \theta = k$ satisfies the fact that if you know one solution $\theta_1$ of the equation, then:

$$
\theta = \pm \theta_1 + 2\pi n
$$

This is because sine and cosine have **infinite** solutions that are distanced $2\pi$ apart. For tangent, if you know one solution, then there are infinite solutions that are distanced $\pi$ apart:

$$
\theta = \pm \theta_1 + \pi n
$$

For example, if we were to solve $\cos \theta = \frac{1}{2}$, the solution would be:

$$
\theta = \pm \frac{\pi}{3} + 2\pi n
$$
The solutions that start from a positive value are equal to:
$$
\theta_+ = \frac{\pi}{3} + 2\pi n = \frac{\pi}{3}, \frac{7\pi}{3}, \frac{13\pi}{3}, \dots
$$
And the solutions that start from a negative value are equal to:
$$
\theta_- = -\frac{\pi}{3} + 2\pi n = \frac{5\pi}{3}, \frac{11\pi}{3}, \frac{17\pi}{3}, \dots
$$

However, only 2 solutions are within $(0, 2\pi)$:

$$
\theta = \frac{\pi}{3}, \frac{5\pi}{3}
$$

## Inverse functions

An **inverse function** is a function that undoes the effect of a function. Given a function $f$ and an inverse function $f^{-1}(x)$, then:

$$
f^{-1}(y) = x
$$
$$
f(x) = y
$$
Note that the "raised to -1" does **not** mean $\frac{1}{f}$. It is a notation to denote the inverse operation.
An inverse function can be found by swapping $x$ and $y$ in a function, and then solving for $y$. The value of $y$ is the inverse function.
An inverse function can only be found if a function _is_ a function (passes vertical line test) and is one-to-one (passes horizontal line test).
Graphically $f^{-1}$ is a reflection of $f$ across $y = x$.

## Inverse trigonometric functions

To find the inverse functions of the trigonometric functions, we must restrict their domain so that on that interval, the trig function is one-to-one.
For example, we restrict $\sin(\theta)$ to $\theta \in [-\frac{\pi}{2}, \frac{\pi}{2}]$, $\cos(\theta)$ to $\theta \in [0, \pi]$, and $\tan (\theta) = [-\frac{\pi}{2}, \frac{\pi}{2}]$.
### Evaluating inverse trigonometric functions

Unlike typical trigonometric functions, inverse trigonometric functions only have **one** possible output for any given input as inverse trig functions are one-to-one.
Say we were to evaluate $\theta = \cos^{-1}(\frac{1}{2})$. To solve this, we swap $\frac{1}{2}$ and $\theta$, then change the inverse cosine to regular cosine, to get:
$$
\cos \theta = \frac{1}{2}, \theta \in [0, \pi]
$$
Evidently, the answer is that $\theta = \frac{\pi}{3}$.  You may wonder where we got the bounds from. The bounds for the output of each inverse trigonometric function are (you should memorize this):

| Function | Bounds of $\theta$ (your answer) |
|----|----|
| $\sin^{-1} (x)$ | $[-\frac{\pi}{2}, \frac{\pi}{2}]$ |
| $\cos^{-1}(x)$ | $[0, \pi]$ |
| $\tan^{-1} (x)$ | $[-\frac{\pi}{2}, \frac{\pi}{2}]$ |

So the format of evaluating inverse trig functions is to swap the $x$ and $\theta$, then set $\theta \in \text{[your bounds]}$, then solve.

When taking the input of an inverse trig function of a trig function of a value, in the form:
$$
x = \sin^{-1}(\sin(\theta))
$$
$$
x = \cos^{-1}(\cos(\theta))
$$
$$
x = \tan^{-1}(\tan(\theta))
$$
If $\theta$ is within the range of the inverse trig function, $x = \theta$; otherwise, it has to be manually computed.
