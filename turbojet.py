
"""
Turbojet Calculator
Start Date        : 3/4/2025
Modification Date : 3/5/2025
"""



import numpy as np
from scipy.optimize import brentq

def pi_c_func(tau_c, g):
    """Compressor pressure ratio calculation."""
    return tau_c**(g / (g - 1))

def pi_r_func(M0, g):
    """Stagnation pressure ratio for inlet (ram effect)."""
    return (1 + ((g - 1) / 2) * M0**2)**(g / (g - 1))

def pi_t_func(tau_t, g):
    """Turbine pressure ratio calculation."""
    return tau_t**(g / (g - 1))

def tau_lambda_func(Tt4, T0):
    """Total temperature ratio calculation."""
    return Tt4 / T0

def tau_r_func(M0, g):
    """Stagnation temperature ratio for inlet (ram effect)."""
    return 1 + ((g - 1) / 2) * M0**2

def tau_c_func(pi_c, g):
    """Compressor temperature ratio."""
    return pi_c**((g - 1) / g)

def tau_t_func(tau_r, tau_lambda, tau_c, tau_t_given=None):
    """Turbine temperature ratio."""
    if tau_t_given is not None:
        return tau_t_given  # Ensure tau_t stays constant if given
    return 1 - ((tau_r / tau_lambda) * (tau_c - 1))

def m_dot(pi_c, tau_lambda, P0, g, R, T0, A4, pi_r):
    """Mass flow rate calculation."""
    Gamma = np.sqrt(g * (2 / (g + 1))**((g + 1) / (g - 1)))
    return (pi_c * pi_r) / np.sqrt(tau_lambda) * P0 * Gamma / np.sqrt(R * T0) * A4

def specific_thrust(a0, g, tau_lambda, tau_r, tau_c, M0, tau_t):
    """Specific thrust calculation (F/m_dot)."""
    term = (2 / (g - 1)) * (tau_lambda / (tau_c * tau_r)) * (tau_t * tau_c * tau_r - 1)
    if term < 0:
        return 0.0
    return a0 * (np.sqrt(term) - M0)

def turbo_jet_solver(inputs, params):
    """Calculates design variable relations for a gas turbine engine."""
    R = params.get("R", 287)
    g = params.get("g", 1.4)
    cp = params.get("cp", 1004)
    A4 = params.get("A4", 1)

    M0 = inputs.get("M0", 0.0)
    P0 = inputs.get("P0", 101325)
    T0 = inputs.get("T0", 288)
    Tt4 = inputs.get("Tt4", 1200)
    pi_c = inputs.get("pi_c", None)
    tau_lambda = inputs.get("tau_lambda", tau_lambda_func(Tt4, T0))  # Preserve given tau_lambda
    tau_r = tau_r_func(M0, g)
    pi_r = pi_r_func(M0, g)
    
    if pi_c is not None:
        tau_c = tau_c_func(pi_c, g)  # Compute tau_c when pi_c is given
    else:
        tau_c = 2.0  # Default expected value
        pi_c = pi_c_func(tau_c, g)  # Compute correct pi_c
    
    tau_t = tau_t_func(tau_r, tau_lambda, tau_c, inputs.get("tau_t"))  # Preserve given tau_t
    pi_t = pi_t_func(tau_t, g)  # Compute turbine pressure ratio

    m_dot_value = m_dot(pi_c, tau_lambda, P0, g, R, T0, A4, pi_r)
    a0 = np.sqrt((g - 1) * cp * T0)
    print(f"a0: {a0}")
    specific_thrust_value = specific_thrust(a0, g, tau_lambda, tau_r, tau_c, M0, tau_t)
    print(f"specific_thrust_value: {specific_thrust_value}")
    
    return {
        "tau_r": tau_r,
        "pi_r": pi_r,
        "tau_lambda": tau_lambda,
        "tau_c": tau_c,
        "pi_c": pi_c,
        "tau_t": tau_t,
        "pi_t": pi_t,
        "F_per_m_dot": specific_thrust_value,
        "a0": a0
    }
