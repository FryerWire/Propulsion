"""
Turbojet Performance Calculator - Fixed ZeroDivisionError and F Calculation
Start Date        : 3/5/2025
Modification Date : 3/5/2025
"""

import numpy as np
from scipy.optimize import brentq

# Turbojet Performance Relations ==================================================================
def tau_r(M0, gamma=1.4):
    return 1 + ((gamma - 1) / 2) * M0**2

def pi_r(M0, gamma=1.4):
    return tau_r(M0, gamma)**(gamma / (gamma - 1))

def tau_c(pi_c, gamma=1.4):
    return pi_c**((gamma - 1) / gamma)

def tau_t(tau_lambda, tau_r, tau_c):
    return 1 - (tau_r / tau_lambda) * (tau_c - 1)

def pi_t(tau_t, gamma=1.4):
    return tau_t**(gamma / (gamma - 1))

def f(h, cp, T0, tau_lambda, tau_c, tau_r):
    return (cp * T0 * (tau_lambda - tau_c * tau_r)) / h

def S(f, specific_thrust):
    return f / specific_thrust

def u0(M0, a0):
    return M0 * a0

def u9(a0, tau_lambda, tau_c, tau_r, tau_t, gamma=1.4):
    return a0 * np.sqrt((2 / (gamma - 1)) * (tau_lambda / (tau_c * tau_r)) * (tau_t * tau_c * tau_r - 1))

def thermal_efficiency(u9, u0, f, h):
    """ Computes correct thermal efficiency (n_th) """
    return (u9**2 - u0**2) / (2 * f * h) if f > 0 else 0

def propulsive_efficiency(u0, u9):
    """ Computes correct propulsive efficiency (n_p) """
    return (2 * u0) / (u0 + u9) if (u0 + u9) != 0 else 0

def turbojet_solver(knowns):
    """
    Computes turbojet parameters for a given set of known values.
    """

    gamma = knowns.get('gamma', 1.4)
    cp = knowns.get('cp', 1004)
    h = knowns.get('h', 42800e3)
    T0 = knowns.get('T0', 288)
    P0 = knowns.get('P0', 101000)
    M0 = knowns.get('M0', 0)
    
    if 'Tt4' not in knowns:
        raise ValueError("Tt4 (Turbine Total Temperature) is required.")

    Tt4 = knowns['Tt4']
    
    # Compute tau_lambda
    tau_lambda = Tt4 / T0
    
    # Compute tau_r
    tau_r_val = tau_r(M0, gamma)
    
    # Given tau_t (turbine temperature ratio)
    tau_t_val = knowns.get('tau_t', 0.7)  # Given in the problem
    
    # Compute tau_c
    tau_c_val = (1 - tau_t_val * tau_r_val) / (tau_r_val * (1 - 1/tau_lambda))

    # Compute pi_c
    pi_c_val = tau_c_val**(gamma / (gamma - 1))

    # Compute stagnation pressures
    pi_r_val = pi_r(M0, gamma)
    pi_t_val = pi_t(tau_t_val, gamma)
    
    # Fuel-to-air ratio
    f_val = f(h, cp, T0, tau_lambda, tau_c_val, tau_r_val)

    # Compute exit velocity (Static Condition)
    a0_val = np.sqrt(gamma * 287 * T0)
    u9_val = a0_val * np.sqrt(2 * (tau_lambda / (tau_c_val * tau_r_val)) * (tau_t_val * tau_c_val * tau_r_val - 1) / (gamma - 1))

    # Compute Specific Thrust (F/m0_dot)
    F_m0_dot_val = u9_val - M0 * a0_val  # For M0 = 0, this simplifies to u9

    # Compute Thrust
    mdot = knowns.get('mdot', 50)  # Default mdot if missing
    F_val = F_m0_dot_val * mdot if mdot > 0 else 0

    # Compute Thermal and Propulsive Efficiency
    n_th_val = thermal_efficiency(u9_val, M0 * a0_val, f_val, h)
    n_p_val = propulsive_efficiency(M0 * a0_val, u9_val)

    # Store results
    results = {
        "tau_r": tau_r_val,
        "tau_c": tau_c_val,
        "tau_lambda": tau_lambda,
        "tau_t": tau_t_val,
        "pi_r": pi_r_val,
        "pi_c": pi_c_val,
        "pi_t": pi_t_val,
        "f": f_val,
        "F_m0_dot": F_m0_dot_val,
        "F": F_val,
        "u9": u9_val,
        "n_th": n_th_val,
        "n_p": n_p_val,
        "a0": a0_val
    }

    return results

