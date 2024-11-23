import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Constants
gamma = 1.4  # Specific heat ratio (dimensionless)
R = 287.0  # Specific gas constant (J/kg·K)
T_ref = 273.15  # Reference temperature (K)
mu_ref = 1.716e-5  # Reference dynamic viscosity (kg/m·s)
S = 110.4  # Sutherland's constant (K)
L_c = 1e-6  # Characteristic length (m, reduced to nanoscale applications)

# Functions for fluid properties and Knudsen number computation
def temperature_ratio(T_0, M):
    """
    Calculate the local temperature as a function of stagnation temperature and Mach number.
    Args:
        T_0: Stagnation temperature (K)
        M: Mach number (dimensionless)
    Returns:
        T: Local temperature (K)
    """
    return T_0 / (1 + ((gamma - 1) / 2) * M**2)

def pressure_ratio(P_0, T, T_0):
    """
    Calculate the local pressure as a function of stagnation pressure, temperature, and Mach number.
    Args:
        P_0: Stagnation pressure (Pa)
        T: Local temperature (K)
        T_0: Stagnation temperature (K)
    Returns:
        P: Local pressure (Pa)
    """
    return P_0 * (T / T_0)**(gamma / (gamma - 1))

def density(P, T):
    """
    Calculate the local density using the ideal gas law.
    Args:
        P: Local pressure (Pa)
        T: Local temperature (K)
    Returns:
        rho: Density (kg/m³)
    """
    return P / (R * T)

def viscosity(T):
    """
    Calculate the dynamic viscosity using Sutherland's law.
    Args:
        T: Local temperature (K)
    Returns:
        mu: Dynamic viscosity (kg/m·s)
    """
    return mu_ref * (T / T_ref)**(3/2) * (T_ref + S) / (T + S)

def mean_free_path(mu, P, T):
    """
    Calculate the mean free path of gas molecules.
    Args:
        mu: Dynamic viscosity (kg/m·s)
        P: Local pressure (Pa)
        T: Local temperature (K)
    Returns:
        lambda_: Mean free path (m)
    """
    return mu / (P * np.sqrt(2 * R * T))

def knudsen_number(lambda_, L_c):
    """
    Calculate the Knudsen number.
    Args:
        lambda_: Mean free path (m)
        L_c: Characteristic length (m)
    Returns:
        Kn: Knudsen number (dimensionless)
    """
    return lambda_ / L_c

# Parameters
T_0_range = np.linspace(50 + 273.15, 2000 + 273.15, 100)  # Stagnation temperatures (K)
P_0_range = np.logspace(-1, 6, 100)  # Stagnation pressures (Pa, logarithmic scale from 0.1 Pa to 1 MPa)
M_range = np.linspace(0, 1, 200)  # Mach numbers (dimensionless)

# Storage for maximum Knudsen numbers
max_kn = np.zeros((len(T_0_range), len(P_0_range)))

# Diagnostic Variables
debug_samples = []

# Main loop to calculate Knudsen numbers
for i, T_0 in enumerate(T_0_range):
    for j, P_0 in enumerate(P_0_range):
        kn_values = []
        for M in M_range:
            T = temperature_ratio(T_0, M)
            P = pressure_ratio(P_0, T, T_0)
            rho = density(P, T)
            mu = viscosity(T)
            lambda_ = mean_free_path(mu, P, T)
            Kn = knudsen_number(lambda_, L_c)
            kn_values.append(Kn)

        max_kn[i, j] = max(kn_values)  # Store the maximum Knudsen number for the given T_0 and P_0

        # Store some debug samples
        if i % 10 == 0 and j % 10 == 0:  # Reduce number of diagnostic outputs
            debug_samples.append((T_0, P_0, lambda_, max(kn_values)))

# Print diagnostics
print(f"{'T_0 (K)':>10} {'P_0 (Pa)':>15} {'λ (m)':>15} {'Max Kn':>10}")
for sample in debug_samples:
    print(f"{sample[0]:>10.2f} {sample[1]:>15.2e} {sample[2]:>15.2e} {sample[3]:>10.4f}")

# Define Knudsen regimes and corresponding colors
knudsen_bins = [0, 0.001, 0.1, 10, np.inf]
knudsen_colors = ["#98c1d9", "#e0a899", "#d9796c", "#f4c2c2"]  # Continuum, slip, transition, free-molecular

# Categorize Knudsen numbers into regimes
kn_categorized = np.digitize(max_kn, knudsen_bins) - 1

# Create the heatmap
plt.figure(figsize=(12, 8))
plt.imshow(
    kn_categorized.T,
    origin="lower",
    extent=[T_0_range[0] - 273.15, T_0_range[-1] - 273.15, P_0_range[0] / 1e5, P_0_range[-1] / 1e5],
    aspect="auto",
    cmap=plt.cm.colors.ListedColormap(knudsen_colors),
)

# Add a legend for the regimes
legend_patches = [
    mpatches.Patch(color="#bde0fe", label="Continuum regime (Kn ≤ 0.001)"),
    mpatches.Patch(color="#ffa69e", label="Slip regime (0.001 < Kn ≤ 0.1)"),
    mpatches.Patch(color="#ff686b", label="Transition regime (0.1 < Kn ≤ 10)"),
    mpatches.Patch(color="#ffcccb", label="Free-molecular regime (Kn > 10)"),
]
plt.legend(handles=legend_patches, title="Knudsen Regimes", loc="upper right", fontsize=10, title_fontsize=12)

# Add labels, title, and grid
plt.title("Knudsen Regimes over $T_0$ and $P_0$", fontsize=14)
plt.xlabel("Stagnation Temperature $T_0$ (°C)", fontsize=12)
plt.ylabel("Stagnation Pressure $P_0$ (bar)", fontsize=12)
plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)

# Show the plot
plt.show()
