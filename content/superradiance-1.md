+++
title = "Simulating superradiance reactors, part 0"
+++

This is to be the beginning of a series of posts focused on creating a preliminary, naive raytracer for simulating superradiance reactors.

<!-- more -->

In years, I may look back and create a much more optimized implementation. However, for the present, I want to document my progress (and the associated pains of progress) with abundant code snippets, in the hope that this information may be of use to someone.

## Why develop black hole superradiance reactors?

Human advancement has gone hand-in-hand with the discovery of new energy sources: from coal, to petroleum, to nuclear fission, and most recently, to renewable sources of energy. Black holes are an untapped energy source, capable of augmenting, and perhaps one day replacing, traditional energy sources.

Due to the effect of frame-dragging predicted through General Relativity, rotating bodies drag spacetime with them, causing objects in the immediate vicinity to co-rotate with the rotating body. Rotating black holes, described by the Kerr metric, contain a region where the effect of frame-dragging is sufficient that even light must co-rotate with the black hole. Such a region is known as the ergosphere, and it is this feature which allows for the possibility of energy extraction from black holes.

My research is centered on black hole energy generation through utilizing the superradiance effect, where light trapped around a rotating black hole would be amplified in the black hole's ergosphere. A reflective cavity enclosing the black hole would cause exponential amplification, and an outlet in the cavity would produce a concentrated super-high-energy beam, capable of then being distributed.  Such reactors would also require the creation and manipulation of artificial kugelblitz black holes, generated from extreme concentrations of energy. Currently, both kugelblitz black holes and superradiant scattering are poorly understood; it is hoped that with computer simulations of superradiance reactors, insights may be gained into both phenomena, and we may be one step closer to realizing black hole energy generation.

## The basic design of the raytracer

The raytracer is designed to follow light rays emitted from a point inside an icospherical shell mirror. The mirror is assumed to be a perfect mirror of approximately 1m radius. The black hole will be of mass $M$, where its mass is given in terms of its effective lifespan $t_\mathrm{ev}$ as:

$$
M = \left(\frac{t_{\mathrm {ev}} \hbar c^4}{5120 \pi G^2}\right)^{1/3}
$$

I assume a black hole of ~1.2 billion kg, with a lifetime of approximately 5,000 years, to be the black hole in question. This black hole would have a schwarzschild radius of $1.78 \times 10^{-18}$ meters, which is approximately equivalent to a proton's radius.

With the basic parameters of the problem defined, I'll now go through the design of the raytracer.

The raytracer uses perhaps the most naive method of raytracing: it shoots a single ray, then records the trajectories of the rays as they reflect in the mirror and travel along Kerr geodesics. The basic algorithm can be described as follows:

```python
mesh = loadmesh("geometry.stl")

ray_origin = np.array([0.0, 0.0, 0.0])

# Rays pointing vertically down
ray_initial_direction = np.array([0.0, 0.0, -1.0])

ray_positions = [ray_origin]
ray_directions = [ray_initial direction]

for i in range(10000):
  # Find the point of intersection accounting for curving
  # of straight path in Kerr spacetime
  intersection_point = KerrIntersection(ray_positions[i - 1], ray_directions[i - 1])
  # New ray origin is intersection point
  ray_positions[i] = intersection_point
  normal = normal_at_point(intersection_point)
  angle = angle_between_vectors(normal, ray_directions[i - 1])
  # We compute the new direction from the angle
  ray_directions[i] = direction_from_angle(angle, intersection_point)

t = np.arange(0, 10000)
plot_3d_path(t, ray_positions);
plot_3d_geom(mesh)
```

Thus, the algorithm requires three pieces:

- A numerical integrator for Kerr geodesics to find the location a ray intersects the mirror as it travels along a Kerr geodesic
- A library with functions to calculate the angle between vectors and find the new ray direction from a given angle
- A 3D model of a icosphere with a cut-out to allow light rays to exit

The next blog posts in this series will cover my implementations of each piece.
