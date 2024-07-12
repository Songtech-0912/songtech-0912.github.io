+++
title = "Mass driver interstellar propulsion"
date = 2023-05-20
+++

A very rough sketch of a mass-driver based interstellar propulsion method is discussed and analyzed.

<!-- more -->

The idea is simple:

![Diagram](mass-driver-diagram.svg)

Fuel pellets will be very small ionized spherical pellets composed of inexpensive materials. They will be magnetically accelerated to high speed, then brought on intersecting trajectories, where they will collide. The electricity for the mass driver will be provided by an onboard nuclear reactor. The expelled reaction mass produces thrust, as given by:

{% math() %}
F = v \frac{dm}{dt}
{% end %}

From conservation of momentum, it is evident that the expelled reaction mass will be equal to the sum of all of the fuel pellets' masses. Considering the case of 1 kg per millisecond expelled at an exhaust velocity of 100 km/s, the force generated will be equal to:

{% math() %}
F = 1 \times 10^8 N
{% end %}

The acceleration of such a spacecraft is given by:

{% math() %}
a = \frac{F}{m}
{% end %}

Given a spacecraft with a mass of 10,000 tons, this would produce a comfortable 1g acceleration. And given a continuous 1g acceleration halfway to Proxima Centauri, and 1g deceleration afterward, this would allow for a travel time, in the reference frame of Earth, of 2.86 years, as given by:

{% math() %}
t = \sqrt{\frac{x}{g}}
{% end %}

## Combination with Alcubierre Drive

As the Alcubierre drive acts as a "booster" to the existing velocity of the spacecraft, the spacecraft can accelerate to perhaps $v = 0.1c$, then turn off its mass driver propulsion system and turn on its Alcubierre drive. Afterwards, it can turn off its Alcubierre drive close to its destination, and restart its mass driver propulsion system. Such a journey will allow reaching Alpha Centauri in just 2 months with minimal fuel.
