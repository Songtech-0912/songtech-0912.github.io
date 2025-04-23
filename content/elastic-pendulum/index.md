+++
title = "Solving the elastic pendulum with Python"
date = 2025-04-22

[extra]
non_note = true
+++

One of the most surprising aspects of physics is how complex even everyday systems happen to be. One apparently-simple system that has a very complex physical description is the **elastic pendulum**, and we will solve it here, with the help of Lagrangian mechanics and Python.

<!-- more -->

> **Note:** If you're unfamiliar with Lagrangian mechanics, or need a refresher, see the [relevant section](@/advanced-classical-mech/index.md#lagrangian-mechanics) on the (advanced) classical mechanics guide.

We consider a block of mass $m$ attached to an ideal string of length $L$, which is itself attached to a spring of variable length $l(t)$ and spring constant $k$ that hangs from the ceiling. We assume that the string is sufficiently short to be approximated as perfectly straight, such that the spring and the string form a straight line. Using a coordinate system centered at the attachment point of the spring, with $+x$ being the downward direction and $+y$ being the rightward direction, the position of the spring would be given by:

{% math() %}
\begin{align*}
x(t) &= l(t) \cos (\theta(t)) + L \cos \theta(t) \\
y(t) &= l(t) \sin (\theta(t)) + L \sin \theta(t) \\
\end{align*}
{% end %}

The kinetic and potential energies would therefore be respectively given by:

{% math() %}
\begin{align*}
K &= \dfrac{1}{2} m(\dot x^2 + \dot y^2) \\
U &= \dfrac{1}{2} k(l(t) + L)^2 -mgy
\end{align*}
{% end %}

Thus the system's Lagrangian $\mathcal{L} = K - U$ would then be given by:

{% math() %}
\begin{align*}
\mathcal{L} &= \dfrac{1}{2} m\big[L^2 \dot \theta^2 + 2 L l \dot \theta^2 + l^2 \dot \theta^2 + \dot l^2\big]^2 \\
&\qquad - \frac{1}{2}k(L + \ell)^2 + m g(L + l) \cos \theta
\end{align*}
{% end %}

We aim to solve for $\theta(t)$ and $l(t)$ via the Euler-Lagrange equations, to be able to numerically-integrate the system and find the trajectories of the mass. There are two Euler-Lagrange equations, one for $\theta(t)$ and one for $l(t)$. They are, respectively:

{% math() %}
\begin{align*}
\dfrac{\partial \mathcal{L}}{\partial \theta} - \dfrac{d}{dt} \left(\dfrac{\partial \mathcal{L}}{\partial \dot \theta}\right) = 0 \\
\dfrac{\partial \mathcal{L}}{\partial l} - \dfrac{d}{dt} \left(\dfrac{\partial \mathcal{L}}{\partial \dot l}\right) = 0 \\
\end{align*}
{% end %}

The partial derivatives, are, respectively:

{% math() %}
\begin{align*}
\dfrac{\partial \mathcal{L}}{\partial \theta}
&= -mg(L + l) \sin \theta \\
\dfrac{\partial \mathcal{L}}{\partial \dot \theta}
&= \dot \theta m (L + l)^2 \\
\dfrac{\partial \mathcal{L}}{\partial l}
&= \dot \theta^2 m(L + l) + m g \cos \theta - k(L + l) \\
\dfrac{\partial \mathcal{L}}{\partial \dot l} 
&= m \dot l
\end{align*}
{% end %}

Thus we have the ODEs given by:

{% math() %}
\begin{gather*}
\ddot \theta m(L + l)^2 = -mg(L + l) \sin \theta \\
\ddot l m = \dot \theta^2 m(L + l) + mg \cos \theta - k(L + l)
\end{gather*}
{% end %}

With a bit of simplification and defining $\omega_0 = \sqrt{k/m}$, we have:

{% math() %}
\begin{gather*}
\ddot \theta = -\dfrac{g\sin \theta}{L + l} \\
\ddot l = \dot \theta^2 (L + l) + g \cos \theta - \omega_0^2(L + l)
\end{gather*}
{% end %}

Note that in the limit as $l \to 0$, this reproduces the equation of a (springless) simple pendulum, $\ddot \theta = -\frac{g}{L} \sin \theta$. But if we don't use any simplifications, this is a system of coupled highly-nonlinear ODEs that cannot be solved analytically. So instead, we will turn to numerical integration. For this, we will need to reduce the system to a first-order system of four ODEs, one each for $l, \theta, v, \omega$, where $v = \dot l$ and $\omega = \dot \theta$, as shown below:

{% math() %}
\begin{align*}
\dot \theta &= \omega \\
\dot \omega &= -\dfrac{g\sin \theta}{L + l} \\
\dot l &= v \\
\dot v &= \omega^2 (L + l) + g \cos \theta - \omega_0^2(L + l)
\end{align*}
{% end %}

This is the time to reach for the power of numerical methods and Python. We'll be using the `solve_ivp` numerical integrator from the [SciPy library](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html) for numerically solving the system of differential equations. We first import the necessary packages:

```python
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# some optional customizations
%matplotlib inline # for Jupyter notebook only
%config InlineBackend.figure_format = 'svg'
plt.rcParams["font.family"] = "serif"
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['figure.autolayout'] = True
plt.rcParams["axes.grid"] = True
```

Then, we set our constants $\omega_0, L, g$:

```python
freq = 0.5 # in Hz i.e. cycles/second
w0 = 2 * pi * freq

oscillator_params = {
    "L": 0.5, # setting L = 0 is equivalent to no string, just spring
    "g": 9.81,
    "w0": w0
}
```

We define our ODE system in the form $\dot{\mathbf{y}} = \mathbf{F}(t, \mathbf{y})$, where $\mathbf{y} = \langle\theta, l, \omega, v\rangle$ and $\dot{\mathbf{y}} = \langle \dot \theta, \dot l, \dot \omega, \dot v \rangle$. The function `oscillator_system()` is $\mathbf{F}(t, \mathbf{y})$ but written in Python:

```python
def oscillator_system(t, state, constants=oscillator_params.values()):
    theta, l, omega, v = state
    L, g, w0 = constants
    # calculate derivatives for next time-step
    theta_dot = omega
    omega_dot = -(g * np.sin(theta)) / (L + l)
    l_dot = v
    v_dot = omega**2 * (L + l) + g * np.cos(theta) - w0**2 * (L + l)
    return theta_dot, l_dot, omega_dot, v_dot
```

Now we solve the ODE, as follows:

```python
def solve_oscillator(first_step=1E-2, max_step=1, t_end=60, method="BDF"):
    # t_end is the time when numerical integration should be stopped, in seconds
    if not first_step:
        first_step = 1E-5 # conservative first step
    if not max_step:
        max_step = 1E-3
    t_span = (0, t_end) # seconds to integrate through
    initial_conditions = {
        "theta_0": np.pi/5, # initial angle (don't exceed pi/2!!!)
        "l_0": 1.5, # equilibrium spring length
        "omega_0": 0.05, # initial angular velocity (not omega0)
        "v_0": 1 # initial spring extension rate
    }
    initial_state = np.array(list(initial_conditions.values()))
    # sol = solve_ivp(oscillator_system, t_span, initial_state, first_step=first_step, max_step=max_step, method=method)
    sol = solve_ivp(oscillator_system, t_span, initial_state, method=method)
    return initial_state, sol
```

Now that we have everything set up, we can run the solver:

```python
osc_initial, osc_sols = solve_oscillator(t_end=20)
sol_t = osc_sols.t
sol_theta, sol_l, sol_omega, sol_v = osc_sols.y
```

And finally, plot the solution:

```python
def show_numerical_sol(initial=osc_initial, constants=oscillator_params.values()):
    L, g, w0 = constants
    theta_0, l_0, omega_0, v_0 = initial
    # parametric equations for x(t) and y(t) from l(t) and theta(t)
    x = lambda l, theta: l * np.cos(theta) + L * np.cos(theta)
    y = lambda l, theta: l * np.sin(theta) + L * np.sin(theta)
    # but convert it back to standard coordinates
    # where +x is rightwards and +y is upwards
    # horizontal_pos = lambda l, theta: y(l, theta)
    # vertical_pos = lambda l, theta: -x(l, theta)
    horizontal_pos = lambda l, theta: l * np.sin(theta) + L * np.sin(theta)
    vertical_pos = lambda l, theta: -(l * np.cos(theta) + L * np.cos(theta))
    x0 = horizontal_pos(l_0, theta_0)
    y0 = vertical_pos(l_0, theta_0)
    plt.title("Trajectory of elastic pendulum with rigid string")
    # plot top of frame
    samples = 50
    plt.plot(np.linspace(-5, 5, samples), np.zeros(samples), label="Top of frame", c="black")
    # plot initial length of pendulum
    # with parametric equation
    s = np.linspace(0, 1)
    plt.plot(x0*s, y0*s)
    # plot location of pendulum bob
    plt.scatter(x0, y0, label="Initial point", c="red", marker="o")
    # now plot the actual solution
    plt.plot(horizontal_pos(sol_l, sol_theta), vertical_pos(sol_l, sol_theta), label="Solution", c="blue", linestyle="dashed")
    plt.legend()
    plt.show()

# make plot!
show_numerical_sol()
```

And here is the result of the trajectory traced out by the elastic pendulum over time:

{{ natural_img(
src="numerical-solution.png"
desc="A plot of the numerical solution to the elastic pendulum"
) }}

We see that the system is certainly nonlinear, and pretty chaotic in nature! Pretty cool, huh?