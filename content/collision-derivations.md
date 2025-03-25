+++
title = "Derivations of formulas for elastic collisions"
date = 2024-02-21

[extra]
notoc = true
+++

This is an in-depth step-by-step derivation for elastic collisions in 1D, a companion guide to the [Classical Dynamics Notes](@/classical-dynamics.md).

<!-- more -->

Elastic collisions are collisions in which there is no loss of total mechanical energy - no emission of heat, light, or sound. While elastic collisions are idealizations, any collision that results in deflection (a "bounce" informally speaking) can approximately modelled as an elastic collision, and so formulas for elastic collisions are still of practical value.

We start with the conservation of energy and the conservation of momentum:

{% math() %}
\frac{1}{2} m_1 v_1(a)^2 + \frac{1}{2} m_2 v_2(a)^2 = \frac{1}{2} m_1 v_1(b)^2 + \frac{1}{2} m_2 v_2(b)^2 
{% end %}
{% math() %}
m_1 v_1(a) + m_2 v_2(a) = m_1 v_1(b) + m_2 v_2(b)
{% end %}

From the first (conservation of energy) equation we can factor out the 1/2 factor to get:

{% math() %}
m_1 v_1(a)^2 + m_2 v_2(a)^2 = m_1 v_1(b)^2 + m_2 v_2(b)^2 
{% end %}

We collect the common masses:

{% math() %}
m_1(v_1(a)^2 - v_1(b)^2) = m_2(v_2(b)^2 - v_2(a)^2)
{% end %}

We now factor using the property $a^2 - b^2 = (a + b)(a - b)$:

{% math() %}
m_1(v_1(a) + v_1(b))(v_1(a) - v_1(b)) = m_2(v_2(b) + v_2(a))(v_2(b) - v_2(a))
{% end %}

Now we can take the second (conservation of momentum) equation and collect the common masses as well:

{% math() %}
m_1 (v_1(a) - v_1(b)) = m_2 (v_2(b) - m_2 v_2(a))
{% end %}

Now we take the conservation of energy equation and divide it by the conservation of momentum equation, to get:
{% math() %}
v_1(a) + v_1(b) = v_2(b) + v_2(a)
{% end %}

Rearranging to make the initial and final velocities return to the LHS of the equation, we get:

{% math() %}
v_1(a) - v_2(a) = v_2(b) - v_1(b)
{% end %}

Or:

{% math() %}
v_1(a) - v_2(a) = -(v_1(b) - v_2(b))
{% end %}

That is, the difference of the initial velocities is equal in magnitude and opposite in direction to the difference final velocities, regardless of the masses of the objects.

To actually solve for $v_1(b)$ and $v_2(b)$ though, we need to perform a substitution. We can do this by taking the previous equation and rewriting it as:

{% math() %}
v_1(b) = v_2(b) - (v_1(a) - v_2(a))
{% end %}

Or equivalently:

{% math() %}
v_1(b) = v_2(b) - v_1(a) + v_2(a)
{% end %}

Now if we return to the conservation of momentum equation:
{% math() %}
m_1 v_1(a) + m_2 v_2(a) = m_1 v_1(b) + m_2 v_2(b)
{% end %}

And plug in that value we got for $v_1(b)$:

{% math() %}
m_1 v_1(a) + m_2 v_2(a) = m_1 (v_2(b) - v_1(a) + v_2(a)) + m_2 v_2(b)
{% end %}

We can distribute to get:

{% math() %}
m_1 v_1(a) + m_2 v_2(a) = m_1 v_2(b) - m_1 v_1(a) + m_1 v_2(a) + m_2 v_2(b)
{% end %}

Or rearranged and cleaned-up:

{% math() %}
2m_1 v_1(a) + v_2(a) (m_2  - m_1) = v_2(b) (m_1 + m_2)
{% end %}

So:
{% math() %}
v_2(b) = \frac{2m_1 v_1(a)}{m_1 + m_2} + v_2(a) \frac{m_2 - m_1}{m_1 + m_2}
{% end %}

We can use a similar approach to solve for $v_2(a)$. Since:

{% math() %}
v_1(a) - v_2(a) = v_2(b) - v_1(b)
{% end %}

We can rearrange to get:

{% math() %}
v_1(b) = v_2(b)-v_1(a)+v_2(a)
{% end %}

But we already found what $v_2(b)$ was. So:

{% math() %}
v_1(b) = \left(\frac{2m_1 v_1(a)}{m_1 + m_2} + v_2(a) \frac{m_2 - m_1}{m_1 + m_2}\right) - v_1(a) + v_2(a)
{% end %}

Which after tedious algebra simplifies to:
{% math() %}
v_1(b) = \frac{2m_2 v_2(a)}{m_1 + m_2} + v_1(a) \frac{m_1 - m_2}{m_1 + m_2}
{% end %}

