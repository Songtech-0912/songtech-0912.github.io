+++
title = "A proof of the area of a circle"
date = 2023-10-22

[extra]
non_note = true
+++

Circles are one of the most ubiquitous yet most mysterious objects found in math. This is because its area formula involves a seemingly unlikely object - an irrational number. And yet circles are some of the most common shapes in the universe, and finding the area of circles (or circle-derived objects) is a must for so many applications in math and physics. So we need a way to find the area of a circle.

<!-- more -->

To start with, we need to find a way to calculate the circumference of a circle from its radius. To do this, consider two arcs with arc lengths $a$ and $b$ that each have a central angle $d\theta$. As the arcs have such a small angle, we can consider them essentially triangles, and as each has the same angle and have proportional sides, the two are similar. Therefore, $\frac{a}{r_1} \propto \frac{b}{r_2}$ - the ratio between the arc length and the radius is constant. This means that a circle, which is essentially an arc whose arc length is its circumference $C$, also obeys this. Thus, if $C \propto r$, then $C \propto r \cdot k$, where $k$ is any constant, so $C \propto D$, the diameter. Now it's just the choice of whether we want the proportionality constant to be $\frac{C}{D}$ or $\frac{C}{r}$, the math works out either way - for historical reasons, $\frac{C}{D}$ is what we call the circle constant $\pi$, but mathematicians to this day still bicker about which one to use, see <https://tauday.com/tau-manifesto>.

Now that we've defined $\pi = \frac{C}{D}$, or $C = \pi D$, we know that $C = 2\pi r$ by definition. But that still leaves us with the area of a circle. To solve, suppose we cut a tiny sector of a circle. Since the sector is infinitesimal, then we can approximate its area as the area of a sector, where $\ell$ is the arc length:

{% math() %}
dA = \frac{1}{2} r d\ell
{% end %}

Now we simply need to integrate $dA$ to be able to find $A$, the total area. Note that $\int d\ell = C$, because adding up every little arc length adds to the arc length of a circle, i.e. the circumference:

{% math() %}
A = \int \frac{1}{2} r d\ell = \frac{1}{2} rC
{% end %}

Now we know that $C = \pi d = 2\pi r$. Therefore:

{% math() %}
A = \frac{1}{2} r(2\pi r) = \pi r^2
{% end %}

That just leaves determining what that mysterious constant $\pi = C/D$ is. But that will be a topic for another time!
