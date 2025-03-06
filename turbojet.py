
"""
Turbojet Calculator
Start Date        : 3/4/2025
Modification Date : 3/5/2025
"""



import numpy as np



# Tubojet Design Variable Relations ===============================================================
# pi ----------------------------------------------------------------------------------------------
def pi_c_func(tau_c, g):
    """Compressor pressure ratio calculation."""
    return tau_c**(g / (g - 1))

def pi_r_func(M0, g):
    """Stagnation pressure ratio for inlet (ram effect)."""
    return (1 + ((g - 1) / 2) * M0**2)**(g / (g - 1))

def pi_t_func(tau_t, g):
    """Turbine pressure ratio calculation."""
    return tau_t**(g / (g - 1))

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

def tau_t_func(tau_r, tau_lambda, tau_c, tau_t_given=None):
    """Turbine temperature ratio."""
    if tau_t_given is not None:
        return tau_t_given
    return 1 - ((tau_r / tau_lambda) * (tau_c - 1))

# misc --------------------------------------------------------------------------------------------
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



# Tubojet Design Variable Calculator ==============================================================
def turbo_jet_solver(inputs, params):
    """Calculates design variable relations for a gas turbine engine."""
    
    # Default Gas Parameters ----------------------------------------------------------------------
    R = params.get("R", 287)
    g = params.get("g", 1.4)
    cp = params.get("cp", 1004)
    A4 = params.get("A4", 1)
    h = inputs.get("h", 42800000)  

    # Default Input Parameters --------------------------------------------------------------------
    M0 = inputs.get("M0", 0.0)
    P0 = inputs.get("P0", 101325)
    T0 = inputs.get("T0", 288)
    Tt4 = inputs.get("Tt4", 1200)
    pi_c = inputs.get("pi_c", None)

    # Default Values ------------------------------------------------------------------------------
    tau_lambda = tau_lambda_func(Tt4, T0)
    tau_r = tau_r_func(M0, g)
    pi_r = pi_r_func(M0, g)

    if pi_c is not None: # If 'pi_c' is None, then use 'tau_c'
        tau_c = tau_c_func(pi_c, g)
    else: # Default value, no assumptions beyond this
        tau_c = 2.0  
        pi_c = pi_c_func(tau_c, g)

    # Turbine Values ------------------------------------------------------------------------------
    tau_t = tau_t_func(tau_r, tau_lambda, tau_c)
    pi_t = pi_t_func(tau_t, g)

    # Misc Values ---------------------------------------------------------------------------------
    a0 = np.sqrt((g - 1) * cp * T0)
    u0 = M0 * a0
    m_dot_value = m_dot(pi_c, tau_lambda, P0, g, R, T0, A4, pi_r)
    specific_thrust_value = specific_thrust(a0, g, tau_lambda, tau_r, tau_c, M0, tau_t)
    f = ((cp * T0) / h) * (tau_lambda - tau_c * tau_r)
    S = (f / specific_thrust_value) * 1e6 if specific_thrust_value != 0 else 0
    
    # Exhaust -------------------------------------------------------------------------------------
    M9 = np.sqrt((2 / (g - 1)) * (tau_t * tau_c * tau_r - 1))
    T9 = T0 * (tau_lambda / (tau_c * tau_r))
    u9 = (1 / (1 + f)) * (specific_thrust_value + u0)
    
    # Efficiency ----------------------------------------------------------------------------------
    n_th = 1 - (1 / (tau_r * tau_c))
    n_p = 2 / (1 + (u9 / u0)) if u0 != 0 else 0

    # Results dictionary --------------------------------------------------------------------------
    results = {
        "M0": M0,
        "M9": M9,
        "m0_dot": m_dot_value,
        "mf_dot": f * m_dot_value,
        "T0": T0,
        "T9": T9,
        "Tt2": T0 * tau_r,  # After inlet
        "Tt3": T0 * tau_r * tau_c,  # After compressor
        "Tt4": Tt4,
        "P0": P0,
        "tau_r": tau_r,
        "tau_c": tau_c,
        "tau_lambda": tau_lambda,
        "tau_t": tau_t,
        "pi_r": pi_r,
        "pi_c": pi_c,
        "pi_t": pi_t,
        "f": f,
        "S": S,
        "u9": u9,
        "n_th": n_th,
        "n_p": n_p,
        "a0": a0,
        "F_m0_dot": specific_thrust_value
    }

    return results