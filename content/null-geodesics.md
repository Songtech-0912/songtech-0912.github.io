+++
title = "Null Geodesics"
date = 2023-09-19
+++

It has always been an aim of mine to write a physically-based black hole path tracer. However, before doing that, I thought I would take on an easier challenge - plotting the orbits of photons around Kerr black holes, but with code generalizable to any black hole spacetime.

<!-- more -->

It should be noted that we are using units of $G = c = 1$ here.

First, we need to write out the Kerr metric. The metric is given by:

$$
g_{\mu\nu} = \begin{pmatrix}
	-(1 - \frac{2 M r}{\Sigma}) & 0 & 0 & -\frac{2 M r a \sin^2 \theta}{\Sigma} \\\\
	0 & \frac{\Sigma}{\Delta} & 0 & 0 \\\\
	0 & 0 & \Sigma & 0 \\\\
	-\frac{2 M r a \sin^2 \theta}{\Sigma} & 0 & 0 & (r^2 + a^2 + \frac{2 M r a^2}{\Sigma} \sin^2 \theta) \sin^2 \theta
\end{pmatrix}
$$

Where:

$$
a = \frac{J}{M}
$$
$$
\Sigma = r^2 + a^2 \cos^2 \theta
$$
$$
\Delta = r^2 - 2Mr + a^2
$$

And the inverse metric is given by:

$$
g^{\mu\nu} = \begin{pmatrix}
	-\frac{1}{\Delta} (r^2 + a^2 + \frac{2 M r a^2}{\Sigma} \sin^2 \theta) &
		0 &
		0 &
		-\frac{2 M r a}{\Delta \Sigma} \\\\
	0 & \frac{\Delta}{\Sigma} & 0 & 0 \\\\
	0 & 0 & \frac{1}{\Sigma} & 0 \\\\
	-\frac{2 M r a}{\Delta \Sigma} &
		0 & 
		0 & 
		\frac{1}{\Delta \sin^2 \theta} (1 - \frac{2 M r}{\Sigma})
\end{pmatrix}
$$

So, in code, we have:

```py
def kerr_metric(coords, M=2e30, a=0.97):
    t = coords[0]
    r = coords[1]
    theta = coords[2]
    phi = coords[3]
    sigma = r ** 2 + a ** 2 * torch.cos(theta) ** 2
    delta = r ** 2 - 2 * M * r + a ** 2
    return torch.tensor([
        [-(1 - (2 * M * r) /sigma), 0., 0., -((2 * M * r * a * torch.sin(theta) ** 2) / sigma)],
        [0., sigma / delta, 0., 0.],
        [0., 0., sigma, 0.],
        [-((2 * M * r * a * torch.sin(theta) ** 2) / sigma), 0., 0., (r ** 2 + a ** 2 + (2 * M * r * a ** 2)/sigma * torch.sin(theta) ** 2) * torch.sin(theta) ** 2]
    ])

def kerr_inverse_metric(coords, M=2e30, a=0.97):
    # Based off https://www.roma1.infn.it/teongrav/onde19_20/kerr.pdf
    t = coords[0]
    r = coords[1]
    theta = coords[2]
    phi = coords[3]
    sigma = r ** 2 + a ** 2 * torch.cos(theta) ** 2
    delta = r ** 2 - 2 * M * r + a ** 2
    return torch.tensor([
        [-1 / delta * (r ** 2 + a ** 2 + (2 * M * r * a ** 2) / sigma * torch.sin(theta) ** 2), 0., 0., -(2 * M * r * a) / (sigma * delta)],
        [0., delta / sigma, 0., 0.],
        [0., 0., 1 / sigma, 0.],
        [-(2 * M * r * a) / (sigma * delta), 0., 0., (delta - a ** 2 * torch.sin(theta) ** 2) / (sigma * delta * torch.sin(theta) ** 2)]
    ])
```

Next, we use automatic differentiation to compute the Christoffel symbols of the Kerr metric. As we know, the Christoffel symbols are formed through the derivatives of the metric, so we need to calculate the derivatives of the metric. To do this, we need to calculate the Jacobian of the metric tensor, as the metric tensor is a matrix-valued function, so its derivative is equal to its Jacobian.

This is some code I took from [here](https://github.com/AndreaAntoniali/Riemann-tensor-calculator/blob/main/Riemann_Calculations.ipynb) and modified that calculates the Christoffel symbols in the way outlined:

```py
def calculate_christoffel(jacob, g_inv, dims):
    # based on https://github.com/AndreaAntoniali/Riemann-tensor-calculator/blob/main/Riemann_Calculations.ipynb
    gamma = np.zeros((dims, dims, dims))
    for beta in range(dims):
        for mu in range(dims):
            for nu in range(dims):
                for alpha in range(dims):
                    gamma[beta,mu,nu] = 1/2 * g_inv[alpha][beta] * (jacob[alpha][mu][nu] + jacob[alpha][nu][mu] - jacob[mu][nu][alpha])
    return gamma

def christoffel_at_point_4d(metric, inverse_metric, t, r, theta, phi, dims):
    coord = torch.tensor([t, r, theta, phi], requires_grad=True)
    g_inv = inverse_metric(coord)
    jacobian = torch.autograd.functional.jacobian(metric, coord, create_graph=True)
    return calculate_christoffel(jacobian, g_inv, dims)
```

Now, we can finally solve the geodesic equations. However, firstly, we want to rewrite the typical geodesic equations in a slightly differing form:

$$
\frac{d^2 x^\mu}{ds^2} = -\Gamma^\mu_{\alpha \beta} \frac{dx^\alpha}{ds} \frac{dx^\beta}{ds}
$$

Here, note the use of the Einstein summation convention; $i$ and $j$ are summation (dummy) indices, so we have to fully expand out the summations in our code. The geodesic equation describes a system of equations, one equation each for $(t, r, \theta, \phi)$. Therefore, to simplify our code, we group the equations together as a vector. Additionally, because it is a _second_-order equation, we also need to keep track of the 4 components of velocity, one each for $(v_t, v_r, v_\theta, v_\phi)$. So we have a vector of 8 components that stores all the position and velocity information of our solution to the differential equation:

```py
def kerr_d_ds(X, s, metric=kerr_metric, inverse_metric=kerr_inverse_metric):
        """
        The value of the first and second
        derivatives with respect to an affine
        parameter s
        """
        # Create a new vector to hold the positions and velocities
        u = np.zeros(X.shape)
        # X is a vector with 4 components of position
        # and 4 components of velocity
        x = X[:4]
        velocities = X[4:]
        # Find christoffel symbols given the position and the metric
        # here t is coordinate time, not the affine parameter s, and
        # also not the proper time
        x0, x1, x2, x3 = x
        Gamma = christoffel_at_point_4d(metric, inverse_metric, x0, x1, x2, x3, 4)
        # Given the christoffel symbols, calculate the next position
        for mu in range(4):
            for i in range(4):
                for j in range(4):
                    # Solve for x components
                    # we sum due to the Einstein summation convention
                    u[mu] += -Gamma[mu][i][j] * velocities[i] * velocities[j]
        # Solve for v components
        u[4:] = velocities
        return u
```

We then write a basic RK4 solver to finally solve:

```py
def rk4(f, u0, t0, tf, n):
    t = np.linspace(t0, tf, n+1)
    u = np.zeros((n+1, len(u0)))
    u[0] = u0
    h = t[1]-t[0]
    for i in tqdm(range(n)):
        k1 = h * f(u[i], t[i])    
        k2 = h * f(u[i] + 0.5 * k1, t[i] + 0.5*h)
        k3 = h * f(u[i] + 0.5 * k2, t[i] + 0.5*h)
        k4 = h * f(u[i] + k3, t[i] + h)
        u[i+1] = u[i] + (k1 + 2*(k2 + k3 ) + k4) / 6
    return u, t
```

Now it's time to set up the initial conditions. Our initial radius will be a radius of $6M$, with a polar angle $\theta_0 = \frac{\pi}{4}$ and an azimuthal angle $\phi_0 = 0$. These are arbitrary; so long as the photon doesn't start close to the event horizon, it doesn't matter where it starts. Then, we set our velocities $v_r = c$ (by definition), and $v_\theta = v_\phi = 0$ (also by definition, as the speed of light must be $c$). We then integrate to find the geodesics.
