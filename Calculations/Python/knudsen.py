import numpy as np
import matplotlib.pyplot as plt

# Constants
gamma = 1.4  # Specific heat ratio for air
R = 287.05  # Specific gas constant for air [J/(kg*K)]
mu_ref = 1.716e-5  # Reference dynamic viscosity [Pa·s]
T_ref = 273.15  # Reference temperature for viscosity [K]
S = 110.4  # Sutherland's constant [K]
L = 0.01  # Characteristic length [m]

# Range for stagnation temperature (T0)
T0_range = np.linspace(200, 1200, 500)  # From 200 K to 1200 K

# Fixed Mach numbers
Mach_numbers = [0.5, 1.0, 2.0, 3.0]

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

def knudsen_number(P0, T0, M):
    T = static_temperature(T0, M)
    P = static_pressure(P0, T, T0)
    rho = density(P, T)
    mu = dynamic_viscosity(T)
    lambda_mfp = mean_free_path(mu, rho, T)
    return lambda_mfp / L

P0 = 101325
# Calculate Knudsen numbers for each Mach number over the T0 range
knudsen_data = {M: [knudsen_number(P0,T0, M) for T0 in T0_range] for M in np.linspace(0,1,100)}

print(knudsen_data[1])

# Plotting
plt.figure(figsize=(10, 6))
for M, kn_data in knudsen_data.items():
    plt.plot(T0_range, kn_data, label=f'Mach {M}')

plt.title("Knudsen Number vs Stagnation Temperature (T0)")
plt.xlabel("Stagnation Temperature (T0) [K]")
plt.ylabel("Knudsen Number")
plt.grid(True)
plt.legend()
plt.show()
