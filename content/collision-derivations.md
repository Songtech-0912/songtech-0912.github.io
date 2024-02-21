+++
title = "Derivations of formulas for elastic collisions"
date = 2024-02-21
+++

This is an in-depth step-by-step derivation for elastic collisions in 1D, a companion guide to the [Classical Dynamics Notes](@/classical-dynamics.md).

<!-- more -->

Elastic collisions are collisions in which there is no loss of total mechanical energy - no emission of heat, light, or sound. While elastic collisions are idealizations, any collision that results in deflection (a "bounce" informally speaking) can approximately modelled as an elastic collision, and so formulas for elastic collisions are still of practical value.

We start with the conservation of energy and the conservation of momentum:

$$
\frac{1}{2} m_1 v_1(a)^2 + \frac{1}{2} m_2 v_2(a)^2 = \frac{1}{2} m_1 v_1(b)^2 + \frac{1}{2} m_2 v_2(b)^2 
$$
$$
m_1 v_1(a) + m_2 v_2(a) = m_1 v_1(b) + m_2 v_2(b)
$$
From the first (conservation of energy) equation we can factor out the 1/2 factor to get:

$$
m_1 v_1(a)^2 + m_2 v_2(a)^2 = m_1 v_1(b)^2 + m_2 v_2(b)^2 
$$
We collect the common masses:

$$
m_1(v_1(a)^2 - v_1(b)^2) = m_2(v_2(b)^2 - v_2(a)^2)
$$
We now factor using the property $a^2 - b^2 = (a + b)(a - b)$:

$$
m_1(v_1(a) + v_1(b))(v_1(a) - v_1(b)) = m_2(v_2(b) + v_2(a))(v_2(b) - v_2(a))
$$
Now we can take the second (conservation of momentum) equation and collect the common masses as well:

$$
m_1 (v_1(a) - v_1(b)) = m_2 (v_2(b) - m_2 v_2(a))
$$

Now we take the conservation of energy equation and divide it by the conservation of momentum equation, to get:
$$
v_1(a) + v_1(b) = v_2(b) + v_2(a)
$$
Rearranging to make the initial and final velocities return to the LHS of the equation, we get:

$$
v_1(a) - v_2(a) = v_2(b) - v_1(b)
$$
Or:

$$
v_1(a) - v_2(a) = -(v_1(b) - v_2(b))
$$
That is, the difference of the initial velocities is equal in magnitude and opposite in direction to the difference final velocities, regardless of the masses of the objects.

To actually solve for $v_1(b)$ and $v_2(b)$ though, we need to perform a substitution. We can do this by taking the previous equation and rewriting it as:

$$
v_1(b) = v_2(b) - (v_1(a) - v_2(a))
$$
Or equivalently:

$$
v_1(b) = v_2(b) - v_1(a) + v_2(a)
$$

Now if we return to the conservation of momentum equation:
$$
m_1 v_1(a) + m_2 v_2(a) = m_1 v_1(b) + m_2 v_2(b)
$$
And plug in that value we got for $v_1(b)$:

$$
m_1 v_1(a) + m_2 v_2(a) = m_1 (v_2(b) - v_1(a) + v_2(a)) + m_2 v_2(b)
$$
We can distribute to get:

$$
m_1 v_1(a) + m_2 v_2(a) = m_1 v_2(b) - m_1 v_1(a) + m_1 v_2(a) + m_2 v_2(b)
$$
Or rearranged and cleaned-up:

$$
2m_1 v_1(a) + v_2(a) (m_2  - m_1) = v_2(b) (m_1 + m_2)
$$
So:
$$
v_2(b) = \frac{2m_1 v_1(a)}{m_1 + m_2} + v_2(a) \frac{m_2 - m_1}{m_1 + m_2}
$$
We can use a similar approach to solve for $v_2(a)$. Since:

$$
v_1(a) - v_2(a) = v_2(b) - v_1(b)
$$

We can rearrange to get:

$$
v_1(b) = v_2(b)-v_1(a)+v_2(a)
$$
But we already found what $v_2(b)$ was. So:

$$
v_1(b) = \left(\frac{2m_1 v_1(a)}{m_1 + m_2} + v_2(a) \frac{m_2 - m_1}{m_1 + m_2}\right) - v_1(a) + v_2(a)
$$
Which after tedious algebra simplifies to:
$$
v_1(b) = \frac{2m_2 v_2(a)}{m_1 + m_2} + v_1(a) \frac{m_1 - m_2}{m_1 + m_2}
$$

