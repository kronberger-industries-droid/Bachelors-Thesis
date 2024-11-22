import numpy as np
import matplotlib.pyplot as plot
import pandas as pd

# Constants
gamma = 1.4  # Specific heat ratio for air
R = 287.05  # Specific gas constant for air [J/(kg*K)]
mu_ref = 1.716e-5  # Reference dynamic viscosity [Pa·s]
T_ref = 273.15  # Reference temperature for viscosity [K]
S = 110.4  # Sutherland's constant [K]

# Input: Stagnation parameters
T0 = 300  # Stagnation temperature [K]
P0 = 101325  # Stagnation pressure [Pa]

# Ranges for Mach number and characteristic length
Mach_numbers = np.linspace(0.1, 5, 100)
Lengths = np.linspace(0.001, 0.1, 100)

def static_temperature(T0, M):
    return T0 / (1 + (gamma - 1) / 2 * M**2)

def static_pressure(P0, T, T0):
    return P0 * (T / T0) ** (gamma / (gamma - 1))

def density(P, T):
    return P / (R * T)

def dynamic_viscosity(T):
    return mu_ref * (T / T_ref) ** 1.5 * (T_ref + S) / (T + S)

def mean_free_path(mu, P, T):
    return (mu / P) * np.sqrt((np.pi * R * T)/2)

def knudsen_number(M, L, T0, P0):
    T = static_temperature(T0, M)
    P = static_pressure(P0, T, T0)
    rho = density(P, T)
    mu = dynamic_viscosity(T)
    lambda_mfp = mean_free_path(mu, rho, T)
    return lambda_mfp / L

Kn = knudsen_number(Mach_numbers, Lengths, T0, P0)
print(pd.DataFrame(Kn).head)
