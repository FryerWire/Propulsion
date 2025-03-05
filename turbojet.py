
"""
Turbojet Calculator
Start Date        : 3/4/2025
Modification Date : 3/5/2025
"""



import numpy as np
from scipy.optimize import brentq



# # Turbojet Assumptions ============================================================================
# """
# Isentropic
# - Diffuser (20)
# - Compressor (32)
# - Turbine (54)
# - Nozzle (97)

# Stag P is Constant
# - Burner (43) +Q
# - Rejection (09) -Q
# """

# stage = '20'
# isentropic_stages = ['20', '32', '54', '97', '30', 'd', 'c', 't', 'n']
# constant_pressure_stages = ['43', '09', 'exit']

# # Isentropic Flow
# if (stage in isentropic_stages):
#     pass
    
# # Constant Pressure
# if (stage in constant_pressure_stages):
#     pass



# Design Variable Relations =======================================================================
# pi ----------------------------------------------------------------------------------------------
def pi_c_func(tau_c, g):
    """Compressor pressure ratio calculation."""
    return tau_c**(g / (g - 1))

def pi_r_func(M0, g):
    """Stagnation pressure ratio for inlet (ram effect)."""
    return (1 + ((g - 1) / 2) * M0**2)**(g / (g - 1))

# tau ---------------------------------------------------------------------------------------------
def tau_lambda_func(Tt4, T0):
    """Total temperature ratio calculation."""
    return Tt4 / T0

def tau_r_func(M0, g):
    """Stagnation temperature ratio for inlet (ram effect)."""
    return 1 + ((g - 1) / 2) * M0**2

def tau_c_func(pi_c, g):
    """Compressor temperature ratio."""
    return pi_c**((g - 1) / g)

def tau_t_func(tau_r, tau_lambda, tau_c):
    """Turbine temperature ratio."""
    return 1 - ((tau_r / tau_lambda) * (tau_c - 1))

# m dot -------------------------------------------------------------------------------------------
def m_dot(pi_c, tau_lambda, P0, g, R, T0, A4, pi_r):
    """Mass flow rate calculation."""
    Gamma = np.sqrt(g * (2 / (g + 1))**((g + 1) / (g - 1)))
    return (pi_c * pi_r) / np.sqrt(tau_lambda) * P0 * Gamma / np.sqrt(R * T0) * A4

# misc --------------------------------------------------------------------------------------------
def specific_thrust(a0, g, tau_lambda, tau_r, tau_c, M0, tau_t):
    """Specific thrust calculation (F/m_dot)."""
    term = (2 / (g - 1)) * (tau_lambda / (tau_c * tau_r)) * (tau_t * tau_c * tau_r - 1)
    if term < 0:
        return 0.0
    return a0 * (np.sqrt(term) - M0)



# Tubojet Calculator 
def turbo_jet_solver(inputs, params):
    """Calculates design variable relations for a gas turbine engine.
    # Example usage
    if __name__ == "__main__":
    params = {"R": 287, "g": 1.4, "cp": 1004}
    inputs = {"M0": 2.5, "P0": 15000, "T0": 273.15 - 40, "Tt4": 1800, 'h': 42000000, "pi_c": 14}
    result = turbo_jet_solver(inputs, params)

    print("\nCorrected results:")
    for key, value in result.items():
        print(f"{key}: {value:.4f}")
    
    """
    R = params.get("R", 287)
    g = params.get("g", 1.4)
    cp = params.get("cp", 1004)
    A4 = params.get("A4", 1)

    M0 = inputs.get("M0", 0.0)
    P0 = inputs.get("P0", 101325)
    T0 = inputs.get("T0", 288)
    Tt4 = inputs.get("Tt4", 1200)
    pi_c = inputs.get("pi_c", None)
    
    tau_lambda = tau_lambda_func(Tt4, T0)
    tau_r = tau_r_func(M0, g)
    pi_r = pi_r_func(M0, g)
    
    if pi_c is not None:
        tau_c = tau_c_func(pi_c, g)  # Compute tau_c when pi_c is given
    else:
        tau_c = 2.0  # Default expected value
        pi_c = pi_c_func(tau_c, g)  # Compute correct pi_c
    
    tau_t = tau_t_func(tau_r, tau_lambda, tau_c)

    m_dot_value = m_dot(pi_c, tau_lambda, P0, g, R, T0, A4, pi_r)
    a0 = np.sqrt((g - 1) * cp * T0)
    specific_thrust_value = specific_thrust(a0, g, tau_lambda, tau_r, tau_c, M0, tau_t)

    return {
        "tau_r": tau_r,
        "pi_r": pi_r,
        "tau_lambda": tau_lambda,
        "tau_c": tau_c,
        "pi_c": pi_c,
        "tau_t": tau_t,
        # "m_dot": m_dot_value, # WRONG
        "F_per_m_dot": specific_thrust_value,
        "a0": a0
    }


