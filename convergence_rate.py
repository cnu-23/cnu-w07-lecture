# Numerical investigation of properties of quadrature rules
# Example: rate of convergence for composite Gauss-Legendre quadrature

import numpy as np
import matplotlib.pyplot as plt

# We can use the quadrature() function from the Week 6 tutorial
def quadrature(f, xk, wk, a, b):
    '''
    Approximates the integral of f over [a, b],
    using the quadrature rule with weights wk
    and nodes xk.
    
    Input:
    f (function): function to integrate (as a Python function object)
    xk (Numpy array): vector containing all nodes
    wk (Numpy array): vector containing all weights
    a (float): left boundary of the interval
    b (float): right boundary of the interval
    
    Returns:
    I_approx (float): the approximate value of the integral
        of f over [a, b], using the quadrature rule.
    '''
    # Define the shifted and scaled nodes
    yk = (b - a)/2 * (xk + 1) + a
    
    # Compute the weighted sum
    I_approx = (b - a)/2 * np.sum(wk * f(yk))
    
    return I_approx


# The nodes are defined as the roots of the n-th degree Legendre polynomial.
# Calculate nodes and weights for N nodes
N = 2
xk, wk = np.polynomial.legendre.leggauss(N)

# Let's choose an arbitrary function (not a polynomial) with a known integral
def f(x):
    return np.arctan(x)

def F(x):
    '''
    Exact value for the indefinite integral of f(x) = atan(x).
    '''
    return x * np.arctan(x) - 0.5 * np.log(1 + x**2)


# Compute the integral over [0, 3]
a, b = 0, 3