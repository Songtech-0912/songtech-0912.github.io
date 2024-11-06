+++
title = "BLAS unofficial API documentation"
date = 2024-07-14
draft = true
+++

The [BLAS](https://www.netlib.org/blas) (basic linear algebra subprogram) functions for computational linear algebra are at the heart of many scientific computing, machine learning, and data processing applications. Over 40 years of development and refinement have made them some of the most highly-optimized software libraries in the world. However, they can be a bit archaic and cryptic to use, so consider this an unofficial API reference for BLAS.

<!-- more -->

## Quick start

BLAS is divided into three modules or "levels": level 1 for scalar and vector operations, level 2 for vector-matrix operations, and level 3 for matrix-matrix operations. In addition, each of the BLAS functions (called routines in its documentation) comes in three versions, and here is a tabular guide:

| Prefix | Example | Purpose |
|-------|-------|-------|
| `s` | `sgemm` | Single-precision floating-point input |
| `d` | `dgemm` | Double-precision floating-point input |
| `z` | `zgemm` | Complex floating-point input |

In languages that support generic programming, like C++ and Rust, the BLAS routines often omit the prefixes altogether; for instance, `dgemm` and `sgemm` and `zgemm` would simply be one function called `gemm`. For brevity, this will be the convention used; if using C or Fortran, remember to append the correct prefix. In addition, while the original BLAS routines were implemented in Fortran and C, the function signatures will be given in pseudocode reminiscent of a more modern language.

Also, the BLAS functions general do all of their operations in-place. That is, they modify the data you input into them. Why not return a value? For operations involving millions of data points, returning a new value could be computationally extremely expensive. However, the fact that they don't return a value is something that might take a bit getting used to, because unlike most modern math libraries, their API is almost entirely functional. To do a vector-scalar product, for instance, an example would look like this:

```java
// Must be a mutable array as it is written to
var X = [1., 2., 3., 4.]; // 4 elements
var Y = [0., 0., 0., 0.]; // 4 elements
var scalar = 5.0;
// Run the BLAS AXPY function
axpy(4, scalar, X, 1, Y, 1);
// Now result is written to Y
printf(Y);
// shows [5., 10., 15., 20.]
```

Finally, BLAS, in common with most computational linear algebra libraries, stores all vectorized data (i.e. vectors and matrices) as 1D arrays. This is for performance reasons: nesting arrays within arrays reduces performance. However, this means that matrices must be "flattened" by storing their entries line-by-line, and you could choose to store by order of rows (row-major layout) or columns (column-major layout). BLAS chooses the latter. This is an underlying detail that is really only relevant for math library developers; end-users should rarely need to call the BLAS functions. But it is significant to ensure that the user data layout matches that of BLAS so that the BLAS operations are carried out correctly.

As a quick reference, this is all the BLAS functions in one table:

| Name | Operation |
|------|-------|
| `rotg` | Find Givens rotation coefficients |
| `rotmg` | Find modified givens rotation coefficients |
| `rot` | Apply Givens rotation |
| `swap` | Swap $x$ and $y$ |
| `scal` | Scale a vector by a constant |
| `copy` | Copy $x$ into $y$ |
| `axpy` | Perform a scaled sum on a vector |
| `dot` | Calculate the dot product |
| `sdot` | Calculate the dot product with extended precision |
| `nrm2` | Euclidean norm |
| `asum` | Sum of absolute values in a vector |
| `iamax` | Index of max absolute value |
| `sgemv` | Basic matrix-vector multiplication |

(finish this)

The functions are described individually in detail in the following sections.

## Level 1

{{ funcdoc(name="rotg") }}

```java
fn rotg(a: float, b: float, c: float, d: float);
```

This computes the coefficients of the Givens rotation:

{% math() %}
\begin{pmatrix}
c & s \\ -s & c \\
\end{pmatrix}
\begin{pmatrix}
a \\ b
\end{pmatrix} = 
\begin{pmatrix}
r \\ 0
\end{pmatrix}
{% end %}

{{ funcdoc(name="rotmg") }}

{{ funcdoc(name="rot") }}

{{ funcdoc(name="rotm") }}

## Level 2

## Level 3

## Implementations

In addition to the (unoptimized) [BLAS reference implementation](http://www.netlib.org/blas/blas.tgz), there are a multitude of BLAS implementations, many of them free and open-source. Some are specialized towards a certain type of computation, such as those involving sparse matrices or GPU math. Notable implementations include the following:

- Apple Accelerate
- Intel MKL
- OpenBLAS
- CBLAS
- CuBLAS
- ATLAS

<!-- more -->