# Finite difference approximations to derivatives
# Estimation of order of accuracy

import numpy as np
import matplotlib.pyplot as plt

# Define function for f(x) and f'(x)
def f(x):
    return np.arctan(x)

def f_prime(x):
    return 1 / (1 + x**2)


# Choose a point at which to estimate the derivative
x0 = 1.5