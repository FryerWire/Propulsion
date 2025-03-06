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
    Computes all turbojet parameters dynamically.

    Parameters:
    - knowns (dict): Dictionary of known values.

    Returns:
    - Dictionary with computed and known values.
    """

    gamma = knowns.get('gamma', 1.4)
    cp = knowns.get('cp', 1004)
    h = knowns.get('h', 42800e3)

    if 'T0' not in knowns or 'M0' not in knowns:
        raise ValueError("T0 (freestream temperature) and M0 (Mach number) are required inputs.")

    a0_value = np.sqrt(gamma * 287 * knowns['T0'])
    results = knowns.copy()

    # Solve for tau_r and pi_r if M0 is known
    if 'M0' in knowns:
        results['tau_r'] = tau_r(knowns['M0'], gamma)
        results['pi_r'] = pi_r(knowns['M0'], gamma)

    # ✅ Fix: Ensure tau_c is computed even if pi_c is missing
    if 'pi_c' in knowns:
        results['tau_c'] = tau_c(knowns['pi_c'], gamma)
    else:
        print("🚨 WARNING: 'pi_c' is missing, assuming tau_c = 1")
        results['tau_c'] = 1  # Default value if no compression

    # Compute tau_lambda if missing
    if 'tau_lambda' not in results or results['tau_lambda'] == 0:
        if 'Tt4' in knowns and 'T0' in knowns:
            results['tau_lambda'] = knowns['Tt4'] / knowns['T0']

    # Compute tau_t (Ensure tau_c exists before using it)
    if 'tau_lambda' in results and results['tau_lambda'] > 0:
        results['tau_t'] = tau_t(results['tau_lambda'], results['tau_r'], results['tau_c'])

    # Solve for pi_t if tau_t is known
    if 'tau_t' in results:
        results['pi_t'] = pi_t(results['tau_t'], gamma)

    # Compute fuel-to-air ratio f
    if 'tau_lambda' in results and 'tau_c' in results and 'tau_r' in results:
        results['f'] = f(h, cp, knowns['T0'], results['tau_lambda'], results['tau_c'], results['tau_r'])

    # Compute Specific Thrust (F/m0_dot)
    if all(k in results for k in ['M0', 'tau_lambda', 'tau_c', 'tau_r', 'tau_t']):
        results['F_m0_dot'] = a0_value * ((2 / (gamma - 1)) * (results['tau_lambda'] / (results['tau_c'] * results['tau_r'])) * 
                                         (results['tau_t'] * results['tau_c'] * results['tau_r'] - 1)) ** 0.5 - results['M0'] * a0_value

    # Compute Specific Fuel Consumption (S)
    if 'f' in results and 'F_m0_dot' in results:
        results['S'] = (results['f'] / results['F_m0_dot']) * 1000000 if results['F_m0_dot'] != 0 else 0

    # Compute velocities
    if 'M0' in results:
        results['u0'] = u0(results['M0'], a0_value)

    # ✅ Fix: Ensure `tau_c` exists before using it in `u9()`
    if 'tau_lambda' in results:
        results['u9'] = u9(a0_value, results['tau_lambda'], results.get('tau_c', 1), results['tau_r'], results['tau_t'], gamma)

    # ✅ Compute correct Thermal Efficiency (n_th)
    if all(k in results for k in ['u9', 'u0', 'f']):
        results['n_th'] = thermal_efficiency(results['u9'], results['u0'], results['f'], h)

    # ✅ Compute correct Propulsive Efficiency (n_p)
    if all(k in results for k in ['u0', 'u9']):
        results['n_p'] = propulsive_efficiency(results['u0'], results['u9'])

    # ✅ Fix: Compute Total Thrust (F) - Use default mdot if missing
    if 'F_m0_dot' in results:
        mdot_value = knowns.get('mdot', 50)  # Default to 50 kg/s if missing, instead of 0
        if mdot_value > 0 and results['F_m0_dot'] != 0:
            results['F'] = results['F_m0_dot'] * mdot_value
        else:
            if mdot_value <= 0:
                print("🚨 WARNING: mdot is missing or zero, F cannot be computed accurately")
            if results['F_m0_dot'] == 0:
                print("🚨 WARNING: F_m0_dot is zero, check input parameters")
            results['F'] = 0  # Only set to 0 if no valid computation is possible

    # Store speed of sound for reference
    results['a0'] = a0_value

    return results

