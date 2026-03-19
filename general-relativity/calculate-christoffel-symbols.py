# imports
from sympy import symbols, Symbol, Matrix, Function, simplify, Rational, Eq, diff, Array
from sympy import latex as sympy_to_latex
from sympy import sin, cos, tan, exp
from sympy import csc, sec, cot, asin, acos, atan
from sympy import sinh, cosh, tanh
from sympy import asinh, acosh, atanh
from sympy import log as ln
from sympy.abc import c, G # speed of light and gravity constant
one_half = Rational(1, 2)
from IPython.display import display, Math # for Jupyter notebook/lab only

"""
Predefined functions: you can put all
of these in a single cell or import them
from a separate file prior to any calculations
"""

# calculate the line element ds^2 from the provided metric
def line_element_from_metric(metric, display=True):
    # infinitesimal displacement vector
    dX = Matrix([Symbol("d" + x_i.name) for x_i in coords])
    line_element = [dX.T @ (Matrix(metric) @ dX)][0]
    if display:
        displayed_line_element = Eq(Symbol("ds")**2, line_element[0])
        return displayed_line_element
    else:
        return line_element

# calculate christoffel symbols
def metric_to_inverse(g):
    # since only a matrix has the inv()
    # method we have to do this method
    return Array(Matrix(metric).inv())

# calculate a specific christoffel symbol $\Gamma^\gamma_{\alpha \beta}$
# indices is list-like or tuple in the form (gamma, alpha, beta)
# where gamma, alpha, beta are all coordinates
def calculate_symbol(indices, coords, metric, 
                     metric_inv):
    if len(indices) != 3:
        raise Exception(f"Christoffel symbols have 3 indices, but you supplied {len(indices)}!")
        return
    christoffel = 0
    gamma, alpha, beta = indices
    # check that the provided indices are physical coordinates
    for idx in indices:
        if idx not in coords:
            raise Exception(f"Error: provided coordinate {idx} is not in one of your coordinates {coords}")
            return
    # translate symbols into indices, i.e. x^1 -> 1, x^2 -> 2, x^3 -> 3, etc.
    g, a, b = [coords.index(x) for x in indices]
    X = coords
    dimensions = len(coords)
    # note: summation over k (short for kappa)
    for k in range(dimensions):
        d1 = diff(metric[k][a], X[b])
        d2 = diff(metric[k][b], X[a])
        d3 = diff(metric[a][b], X[k])
        christoffel += one_half * metric_inv[g][k] * (d1 + d2 - d3)
    # returns tuple with Christoffel symbol on first
    # and its evaluated value on the second
    backslash = "\\"
    leftbrace = r"{"
    rightbrace = r"}"
    christoffel_pretty = f"\\Gamma^" + gamma.name \
                + "_" + leftbrace + alpha.name + " " \
                + beta.name + rightbrace
    return Symbol(christoffel_pretty), christoffel

def generate_empty_3D_array(dimensions):
    return [[[0 for _ in range(dimensions)] for _ in range(dimensions)] for _ in range(dimensions)]

def calculate_all_christoffels(coords, metric, inverse_metric):
    dimensions = len(coords)
    # this array holds the actual christoffel symbols
    christoffels_array = generate_empty_3D_array(dimensions)
    # this array holds the LaTeX symbols for the Christoffel symbols
    christoffels_symbolic_array = generate_empty_3D_array(dimensions)
    for g in range(dimensions):
        for a in range(dimensions):
            for b in range(dimensions):
                gamma = coords[g]
                alpha = coords[a]
                beta = coords[b]
                indices = (gamma, alpha, beta)
                # take advantage of symmetry where possible
                if b == a and christoffels_array[g][b][a] != 0:
                    christoffels_array[g][a][b] = christoffels_array[g][b][a]
                    christoffels_symbolic_array[g][a][b] = christoffels_symbolic_array[g][b][a]
                else:
                    christoffel_gab = calculate_symbol(indices, coords, metric, inverse_metric)
                    # christoffel_gab contains both the LaTeX representation 
                    # and the symbolic expression for the computed christoffel
                    # symbol, which we store in 2 separate arrays
                    christoffels_symbolic_array[g][a][b] = christoffel_gab[0]
                    christoffels_array[g][a][b] = christoffel_gab[1]
    # make both display as a SymPy array
    return Array(christoffels_array), Array(christoffels_symbolic_array)

# Print all the nonzero christoffel symbols in the form (Gamma^g_ab = ...)
# the "latex" option here allows returning a LaTeX expression
# rather than a list of equations
def find_nonzero_christoffels(coords, metric, inverse_metric, latex=True):
    christoffels, christoffels_tex_symbols = calculate_all_christoffels(coords, metric, inverse_metric)
    dimensions = len(coords)
    nonzero_christoffels = []
    for g in range(dimensions):
        for a in range(dimensions):
            for b in range(dimensions):
                # ignore diagonal entries or vanishing components
                if a > b or christoffels[g][a][b] == 0:
                    continue
                else:
                    ch_symbol = christoffels[g][a][b]
                    tex_symbol = christoffels_tex_symbols[g][a][b]
                    eq = Eq(tex_symbol, ch_symbol)
                    nonzero_christoffels.append(eq)
    if not latex:
        return nonzero_christoffels
    else:
        latex_str = r"\begin{align}"
        for eq in nonzero_christoffels:
            latex_eq = sympy_to_latex(eq).replace("=", r"&=")
            latex_str += "\n" + latex_eq + r" \\"
        latex_str += "\n" + r"\end{align}"
        return latex_str

def find_geodesic_equations(coords, christoffels_array, affine_parameter=r"\lambda"):
    # `christoffels_array` should be the first element of the
    # output of the function calculate_all_christoffels()
    dimensions = len(coords)
    parameter = Symbol(affine_parameter)
    # 4-position vector as a function of the affine parameter
    X = [Function(coord.name)(parameter) for coord in coords]
    # initialize equations of motion (setting RHS = 0 to start)
    EoMs_lhs = [diff(x_gamma, parameter, 2) for x_gamma in X]
    EoMs_rhs = [0 for _ in range(dimensions)]
    for gamma in range(dimensions):
        for a in range(dimensions):
            for b in range(dimensions):
                # ignore vanishing components
                # TODO: take advantage of symmetries of christoffel symbols
                if christoffels_array[gamma][a][b] == 0:
                    continue
                else:
                    ch_symbol = christoffels_array[gamma][a][b]
                    EoMs_rhs[gamma] += -ch_symbol*diff(X[a], parameter)*diff(X[b], parameter)
    return Eq(Matrix(EoMs_lhs), Matrix(EoMs_rhs))

"""
Example calculation for the 2-sphere metric:

ds^2 = R^2 dtheta^2 + R^2 sin^2(theta) dphi^2
"""

# Coordinates
theta, phi = symbols(r"\theta \phi")
coords = [theta, phi]
# Constants
R = Symbol("R", constant=True, real=True)

# Input metric
metric = Array([
    [R**2, 0],
    [0,    R**2 * sin(theta)**2]
])

inverse_metric = Array(Matrix(metric).inv())

def calculate_symbol_fmt(*indices, coords=coords, 
		g=metric, g_inv=inverse_metric):
    try:
        christoffel = calculate_symbol(*indices, coords, g, g_inv)
        return Eq(christoffel[0], christoffel[1])
    except:
        raise Exception("Christoffel symbol calculation unsuccessful")

# Show christoffel symbol for Gamma^theta_{phi phi} in LaTeX
Chr_theta_phi_phi = calculate_symbol_fmt((theta, phi, phi))
print(sympy_to_latex(Chr_theta_phi_phi)) # outputs LaTeX

# Print all nonzero Christoffel symbols in LaTeX
nonzero_christoffels = find_nonzero_christoffels(coords, metric, inverse_metric)
# Print LaTeX of all nonzero christoffel symbols
print(nonzero_christoffels)

# Now calculate the geodesic equations
chrs = calculate_all_christoffels(coords, metric, inverse_metric)[0]
geodesics = find_geodesic_equations(coords, chrs)
print(sympy_to_latex(chrs)) # outputs LaTeX
