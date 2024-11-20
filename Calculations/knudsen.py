import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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

# Meshgrid for 3D plot
M, L = np.meshgrid(Mach_numbers, Lengths)

# Functions to compute properties
def static_temperature(T0, M):
    return T0 / (1 + (gamma - 1) / 2 * M**2)

def static_pressure(P0, T, T0):
    return P0 * (T / T0) ** (gamma / (gamma - 1))

def density(P, T):
    return P / (R * T)

def dynamic_viscosity(T):
    return mu_ref * (T / T_ref) ** 1.5 * (T_ref + S) / (T + S)

def mean_free_path(mu, rho, T):
    return mu / (rho * np.sqrt(2 * R * T / np.pi))

def knudsen_number(M, L, T0, P0):
    T = static_temperature(T0, M)
    P = static_pressure(P0, T, T0)
    rho = density(P, T)
    mu = dynamic_viscosity(T)
    lambda_mfp = mean_free_path(mu, rho, T)
    return lambda_mfp / L

# Calculate Knudsen numbers
Kn = knudsen_number(M, L, T0, P0)

# Plotting
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(M, L, Kn, cmap='viridis')
ax.set_title('Knudsen Number as a Function of Mach Number and Characteristic Length')
ax.set_xlabel('Mach Number')
ax.set_ylabel('Characteristic Length [m]')
ax.set_zlabel('Knudsen Number')
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()
