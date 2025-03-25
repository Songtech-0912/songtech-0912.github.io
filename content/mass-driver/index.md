+++
title = "Mass driver interstellar propulsion"
date = 2023-05-20

[extra]
non_note = true
+++

In this short article, we'll analyze a mass-driver based interstellar propulsion method. This is a good physical example to practice [relativistic mechanics](@/special-relativity/index.md) and [electromagnetic theory](@/electromagnetism/index.md) as well as (my personal opinion!) a fun exercise in general.

<!-- more -->

Let us start with some motivation. We gaze into the night and see the stars above, and it is only natural to want to reach them. Unfortunately, interstellar spaceflight is a tremendous technological challenge - the distances separating the stars are vast, and creating propulsion systems that can make the trip between the stars, which may well take decades or even centuries, requires incredibly advanced physics and engineering that we aren't (presently) capable of. But I want to sketch out a "toy" propulsion system and apply it to interstellar spaceflight as an exercise.

## Design and mathematical analysis

The idea is simple: this propulsion system, known a **mass driver**, consists of fuel pellets that are launched by electromagnets out of the back of the spacecraft. In particular, the fuel pellets would be very small, and ionized prior to launch; let us suppose they are composed of inexpensive materials so we don't have to think about the economics. The pells would be magnetically accelerated to high speed, then brought on intersecting trajectories, where they would collide. The electricity for the mass driver would be provided by an onboard nuclear reactor. We show a very, very basic diagram below:

![Diagram](mass-driver-diagram.svg)

 The expelled reaction mass produces thrust, which, if we just used Newtonian mechanics, would be given by:

{% math() %}
\begin{align*}
F = \dfrac{d}{dt}(mv) &= m\dfrac{dv}{dt} + v \dfrac{dm}{dt} \\
&= ma + v \dfrac{dm}{dt}
\end{align*}
{% end %}

Where $m$ is the expelled mass, and by the conservation of momentum (equivalently, Newton's 3rd law), the thrust force $F$ of the rocket expelling the fuel pellets would be equal to the force from the expelled fuel pellets pushing back on the rocket, so this gives the force accelerating the rocket forwards. Not that here, we just work in one dimension (that is, $F = F(x)$) for simplicity. But of course, when we are talking about interstellar spaceflight, we have speeds that approach a significant fraction of the speed of light, so we have to use the relativistic expression instead. To do so, note that the relativistic expression of the force is given by the derivative of the four-momentum $P = \gamma m v$:

{% math() %}
F = \dfrac{dP}{dt} = \dfrac{d}{dt}(\gamma mv)
{% end %}

Where $\gamma$ is the **Lorentz factor**:

{% math() %}
\gamma = \dfrac{1}{\sqrt{1 - \left(\frac{v}{c}\right)^2}}
{% end %}

Since our mass is non-constant, $m = m(t)$, and since our velocity is non-constant, $\gamma$ (which depends on $v$) is also dependent on time, so we have:

{% math() %}
\dfrac{d}{dt}(\gamma mv) = \dfrac{d}{dt}\gamma(v(t)) m(t) v(t)
{% end %}

This is a bit of a tricky derivative to evaluate as it requires the triple product rule $(fgh)' = f'gh + fg'h + fgh'$. The result is:

{% math() %}
\begin{align*}
F &= \gamma'(t) m v + \gamma m'(t) v + \gamma m v'(t) \\
&= -\dfrac{1}{2} \dfrac{-2(\frac{v}{c})\frac{1}{c}v'(t)}{\left(1 - \left(\frac{v}{c}\right)^2\right)^{3/2}} mv + \gamma m v'(t) + \gamma v \dfrac{dm}{dt} \\
&= \dfrac{v}{c^2} \gamma^3 v'(t) mv + \gamma m v'(t) + \gamma v \dfrac{dm}{dt} \\
&= m a \left(\dfrac{\gamma^3 v^2}{c^2} + \gamma\right) + \gamma v \dfrac{dm}{dt} \\
&= \gamma \left[m a \left(\dfrac{\gamma^2 v^2}{c^2} + 1\right) + v \dfrac{dm}{dt} \right]
\end{align*}
{% end %}

Let's do a sanity check for our math. We can see that for $v \ll c$, then $\dfrac{v}{c} \approx 0$ and $\gamma \approx 1$, so in the Newtonian limit of slow speeds (compared to the speed of light) we recover the expression of the thrust force being $F = ma + v\dfrac{dm}{dt}$. Note that $\dfrac{dm}{dt}$ is called the **mass discharge rate**. We can express this in terms of the _pellet discharge rate_ $R$ and the total pellet mass $m$ (sum of masses of all the pellets being expelled at one time) as follows:

{% math() %}
\dfrac{dm}{dt} = R m
{% end %}

This allows us to rewrite our thrust force equation as:

{% math() %}
F = m \gamma \left[a \left(\dfrac{\gamma^2 v^2}{c^2} + 1\right) + v R \right]
{% end %}

Or, in terms of the percent of the speed of light $\beta \equiv v/c$, we have:

{% math() %}
F = m \gamma \left[a \left(\gamma^2 \beta^2 + 1\right) + \beta c R \right]
{% end %}

Also note that the Lorentz factor $\gamma$ here is a function of velocity, $v$ is the exhaust velocity (the velocity at which the pellets exit from the rocket), and $a$ is the pellets' acceleration as they exit out of the spacecraft. Note that while the pellets' acceleration is the same in all frames (whether relative to the rocket or measured by a distant observer), their velocity $v$ _is_ relative to a distant observer, so to translate the velocity of the pellets to the frame of the rocket, we have:

{% math() %}
v = v_\text{rocket} + v_\text{pellets}
{% end %}

Where $v_\text{pellets}$ is the velocity at which the pellets exit from the rocket relative to the _rocket_. Using these equations, we can determine the thrust force on the rocket given some parameters for the total pellet mass $m$ and pellet discharge rate $R$, assuming that the mass driver runs continuously:

Rocket velocity | Total pellet mass | Pellet discharge rate | Pellet acceleration | Exhaust velocity | Thrust force | 
|-----|-----|----|-----|-----|-----|
| $\pu{300 km/s}$ | 1 kg | 1 pellet/millisecond | 100 m/s | 100 m/s | $\pu{\approx 400 N}$ |
| $\pu{300 km/s}$ | 10 kg | 1 pellet/millisecond | 100 m/s | 100 m/s | $\pu{\approx 4000 N}$ |
| $\pu{300 km/s}$ | 100 kg | 1 pellet/millisecond | 100 m/s | 100 m/s | $\pu{\approx 40,000 N}$ |
| $\pu{300 km/s}$ | 100 kg | 1 pellet/millisecond | 100 m/s | 1 km/s | $\pu{\approx 130,000 N}$ |
| $\pu{3000 km/s}$ | 100 kg | 1 pellet/millisecond | 100 m/s | 1 km/s | $\pu{\approx 400,000 N}$ |
| $\pu{3000 km/s}$ | 1000 kg | 1 pellet/millisecond | 100 m/s | 1 km/s | $\pu{\approx 4E6 N}$ |

> **Note:** The individual pellets don't need to be heavy; launching a lot of light pellets at once has the same effect as launching one big pellet.

The spacecraft would then experience an acceleration $A$ proportional to the thurst force and inversely proportional to its total mass $M = M_0 - m_T(t)$, where $M_0$ is the spacecraft's total mass at launch and $m_T$ is the total mass of all the pellets it carries. $m_T$ depends on time because the spacecraft would get lighter as it uses up its fuel; if the pellet discharge rate is given by $R$ and the mass of a single pellet is given by $m_p$, then $m_T(t) = m_p N_p Rt$, where $N_p$ is the number of pellets carried when the spaceship launches. Thus the acceleration would be given by:

{% math() %}
A(\tau) = \frac{F}{M(\tau)} = \dfrac{F}{M_0 - m_p N_p R\tau}
{% end %}

Note, however, that this acceleration is the relativistic (not Newtonian) acceleration, which is why we used $\tau$ for the proper time. If the acceleration is measured by a _distant_ observer, the thrust force is constant (as long as the spaceship's powerplant and mass driver are working and discharging pellets at the constant rate $R$), but the acceleration isn't. We can solve this issue by working in the spacecraft's rest frame; then, the acceleration reduces to just the plain Newtonian acceleration, but we also need to consider the effects of length contraction, which changes the distance the spaceship covers.

So it is more helpful to set a fixed acceleration we _want_ and then calculate the fueld required, rather than computing the acceleration based on the spacecraft's mass and fuel, which continuously varies throughout the journey. Let's say we want a comfortable $1g$ acceleration throughout the trip - this would nicely reproduce Earth-like gravity. In fact, it would feel _identical_ to standing on the Earth due to the [equivalence principle](https://en.wikipedia.org/wiki/Equivalence_principle). This means that we want our (relativistic) acceleration to be $a = g$. What would be the travel time - both aboard the rocket, and as measured by an observer on Earth - to the nearest star from Earth, [Proxima Centauri](https://en.wikipedia.org/wiki/Proxima_Centauri)?

Proxima Centauri is about 4.25 light-years away from Earth, measured in the Earth's rest frame. For argument's sake, let's say we were to travel in a straight-line path to Proxima Centauri with constant acceleration $a$. Within the Earth's rest frame, an observer would see the spacecraft seemingly accelerating more and more _slowly_. This is because of _time dilation_. We will state - but not prove - that the formulae for the position of the spacecraft as a function of time $t$ within the Earth frame and proper time $\tau$ within the rocket frame are given by:

{% math() %}
\begin{align*}
x(t) &= \dfrac{c^2}{a} \left(\cosh\left(\operatorname{arcsinh} \dfrac{at}{c}\right) - 1\right) \\
x(\tau) &= \dfrac{c}{a} \left(\cosh \dfrac{a\tau}{c} - 1\right), \\
T &= \dfrac{c^2}{a} \sinh \dfrac{a\tau}{c}
\end{align*}
{% end %}

Remember that here, $a$ is the _relativistic acceleration_, meaning that $a = g$ in the rest frame of the _rocket_ only. To convert it to $a_e$, the acceleration measured in the Earth's frame, we would need to use $a_e = a/\gamma^3$. If we let the distance to Proxima Centauri be $L$, then a reasonable choice would be to let the spacecraft accelerate for half the journey and decelerate (which in practice means turning the ship around so its engine fires in reverse) for the other half. If we solve for $x(\tau) = L/2$, we find that the half-trip time takes about 2.3 years in the frame of the _passengers_, where, at the half-trip point, the ship would reach a maximum speed of $0.98 c$! This means that the full trip would take about **4.6 years** in total, at least, to the passengers on board the spacecraft. However, to the Earthbound observer, the journey would actually take **5.4 years**. Indeed, if the Earthbound and rocket-bound observers compare their clocks, _less time_ would have elapsed on the rocket as would have elapsed on Earth. What amount of fuel would be required? _Enormous_ amounts, which we can calculate by rearranging our thrust equation with $A(\tau) = g$, giving us:

{% math() %}
M_0 = F/g + m_p N_p R\tau, \quad \tau \approx \text{4.6 yr}
{% end %}

Assuming that the mass flow rate is adjusted to maintain a constant force, and thus constant acceleration, using the most conservative figures from our above table (a thurst of only 400 N) and (unrealistically) assuming that the ship ends the trip with its mass completely spent (meaning we presume that close to 100% of the ship's mass is fuel), we would need, at perfect efficiencies, an initial (launch) mass of $M_0 \approx \pu{1.45E11 kg}$ or nearly 145 million tons! This is nearly _290 times_ that of the Burj Khalifa, the (as of 2025) highest building on Earth. 

So, is mass driver propulsion an efficient means of space travel? Clearly not! By Einstein's mass-energy equivalence formula, the rest energy of each pellet, which has mass $m$, is famously given by $E_0 = mc^2$. But the amount of energy we release from discharging each pellet is, at _maximum_, $E = \dfrac{1}{2} mv_0^2$, where $v_0$ is the speed of the expelled pellet (we use the Newtonian expression here because $v_0 \ll c$). Thus, the ratio of energy liberated to total rest energy would be given by:

{% math() %}
\dfrac{E}{E_0} = \dfrac{mv_0^2}{2mc^2} = \left(\dfrac{v_0}{c}\right)^2
{% end %}

Which, even at our maximum $v_0 = \pu{1 km/s}$ exhaust velocity, would only be $1 \times 10^{-9}$ percent of the mass-energy contained within the pellets. Nuclear power (fission and fusion), meanwhile, performs much better at a few percent; antimatter tops it off at 100%, but mass drivers don't come even close. _Unless_ if the mass itself _isn't_ carried as fuel, of course. This may seem bizarre, but since photons carry momentum (even though they are massless), using high-energy photons to transfer momentum to a spacecraft with a reflective pusher-plate _does_ have the possibility of being a feasible method of spacecraft propulsion. This would require a powerful interstellar laser array, but otherwise performs similar (in principle) to a mass driver. However, these are technologies that are far, far away.

## Faster than light?

Up to this point, everything we've discussed is in the realm of well-established physics. But what if we venture into the realm of speculative physics? Let us now _assume_ that we have _somehow_ acquired a faster-than-light (FTL) drive, such as an Alcubierre drive. Let's not ask questions about how exactly we got that FTL drive, or how it works, or if it is internally consistent with relativity, only that it exists and works (we are speaking about hypotheticals here).

Now, let us assume that the spacecraft that is heading from Earth to Alpha Centauri uses a hybrid system: it uses its mass driver for some part of its trip, and uses its FTL drive for the rest. This hybrid system improves performance greatly: the FTL drive acts as a "booster" to the existing velocity of the spacecraft, meaning the spacecraft can accelerate to perhaps $v = 0.1c$, then turn off its mass driver propulsion system and turn on its FTL drive. Afterwards, it can turn off its FTL drive close to its destination, and restart its mass driver propulsion system. Such a journey would allow reaching Alpha Centauri in just 2 months with minimal fuel.
