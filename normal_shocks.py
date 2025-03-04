
"""
Normal Shock Calculator
Start Date        : 2/24/2025
Modification Date : 3/4/2025
"""


import numpy as np
from scipy.optimize import brentq


# Normal Shock Relations ==========================================================================
def M2(M, g):
    return float(np.sqrt((2 + (g - 1) * M**2) / (2 * g * M**2 - (g - 1))))

# Pressure Ratios ---------------------------------------------------------------------------------
def P2_P1(M, g):
    return 1 + (2 * g / (g + 1)) * (M**2 - 1)

def Pt1_P1(M, g):
    return (1 + ((g - 1) / 2) * (M ** 2)) ** (g / (g - 1))

def Pt2_Pt1(M, g):
    A = (((g + 1) / 2) * M**2) / (1 + ((g - 1) / 2) * M**2)
    B = 1 / (((2 * g) / (g + 1)) * M**2 - ((g - 1) / (g + 1)))
    return A**(g / (g - 1)) * B**(1 / (g - 1))

def P1_Pt2(M, g):
    return 1 / (Pt2_Pt1(M, g) * Pt1_P1(M, g))

# Density Ratios ---------------------------------------------------------------------------------
def rho2_rho1(M, g):
    return ((g + 1) * M**2) / ((g - 1) * M**2 + 2)

# Temperature Ratios ---------------------------------------------------------------------------------
def T2_T1(M, g):
    return (2 + (g - 1) * M**2) * (2 * g * M**2 - (g - 1)) / ((g + 1)**2 * M**2)


# brentq Function Solvers =========================================================================
def SOLVE_M_from_M2(M, target, g):
    return M2(M, g) - target

# Pressure Ratios ---------------------------------------------------------------------------------
def SOLVE_M_from_Pt2_Pt1(M, target, g):
    return Pt2_Pt1(M, g) - target

def SOLVE_M_from_P2_P1(M, target, g):
    return P2_P1(M, g) - target

def SOLVE_M_from_Pt1_P1(M, target, g):
    return Pt1_P1(M, g) - target

def SOLVE_M_from_P1_Pt2(M, target, g):
    return P1_Pt2(M, g) - target

# Temperature Ratios ------------------------------------------------------------------------------
def SOLVE_M_from_T2_T1(M, target, g):
    return T2_T1(M, g) - target

# Density Ratios ----------------------------------------------------------------------------------
def SOLVE_M_from_rho2_rho1(M, target, g):
    return rho2_rho1(M, g) - target


# Normal Shock Calculator =========================================================================
def normal_shock_solver(input_var, input_value, g = 1.4):
    """
    Calculates all normal shock values given any input.
    
    Parameters:
    - input_var (string)  : 'M', 'M2', 'Pt2_Pt1', 'T2_T1', 'P2_P1', 'P1_Pt2', 'rho2_rho1', and Pt1_P1.
    - input_value (float) : Any postive float value
    - g (float)           : Heat capacity ratio. Set to 1.4 by default.
    
    Returns:
    - normal_shock_data (dict) : Dictionary of all the values for the normal shock.
    
    Example:
    >>> normal_shock_solver("M", 2)
    
    >>> print(normal_shock_solver("M", 3, 1.4)["P1_Pt2"])
    
    >>> normal_shock_data = normal_shock_solver(input_var = "M", input_value = 2.0, g = 1.4)
    >>> for key, value in normal_shock_data.items():
    >>> print(f"{key} = {value:.4f}")
    """
    
    M_min = 1.0 + 1e-6  
    M_max = 10.0         

    normal_shock_data = {}
    # Mach ----------------------------------------------------------------------------------------
    if (input_var == "M"):
        M = input_value
        if (M <= 1.0):
            raise ValueError("M > 1")
        
    elif (input_var == "M2"):
        if (input_value >= 1):
            raise ValueError("0 < M2 < 1")
        M = brentq(SOLVE_M_from_M2, M_min, M_max, args = (input_value, g))
        
    # Pressure ------------------------------------------------------------------------------------
    elif (input_var == "Pt2_Pt1"):
        if (not 0 < input_value < 1):
            raise ValueError("0 < Pt2_Pt1 < 1")
        M = brentq(SOLVE_M_from_Pt2_Pt1, M_min, M_max, args = (input_value, g))
        
    elif (input_var == "P2_P1"):
        if (input_value < 1):
            raise ValueError("P2_P1 > 1")
        M = brentq(SOLVE_M_from_P2_P1, M_min, M_max, args = (input_value, g))
        
    elif (input_var == "Pt1_P1"):
        if (input_value < 1):
            raise ValueError("Pt1_P1 >= 1")
        M = brentq(SOLVE_M_from_Pt1_P1, M_min, M_max, args = (input_value, g))
        
    elif (input_var == "P1_Pt2"):
        if (input_value >= 1):
            raise ValueError("0 < P1_Pt2 < 1")
        M = brentq(SOLVE_M_from_P1_Pt2, M_min, M_max, args = (input_value, g))    
    
    # Temperature ---------------------------------------------------------------------------------
    elif (input_var == "T2_T1"):
        if (input_value < 1):
            raise ValueError("T2_T1 > 1")
        M = brentq(SOLVE_M_from_T2_T1, M_min, M_max, args = (input_value, g))
        
    # Density -------------------------------------------------------------------------------------
    elif (input_var == "rho2_rho1"):
        if (input_value < 1):
            raise ValueError("rho2_rho1 > 1")
        M = brentq(SOLVE_M_from_rho2_rho1, M_min, M_max, args = (input_value, g))
        
    else:
        raise ValueError("Unknown input variable. Use 'M', 'M2', 'Pt2_Pt1', 'T2_T1', 'P2_P1', or 'rho2_rho1'.")

    normal_shock_data["M1"] = M
    normal_shock_data["M2"] = M2(M, g)
    normal_shock_data["P2_P1"] = P2_P1(M, g)
    normal_shock_data["rho2_rho1"] = rho2_rho1(M, g)
    normal_shock_data["T2_T1"] = T2_T1(M, g)
    normal_shock_data["Tt2_Tt1"] = 1.0
    normal_shock_data["Pt2_Pt1"] = Pt2_Pt1(M, g)
    normal_shock_data["Pt1_P1"] = Pt1_P1(M, g)
    normal_shock_data["P1_Pt2"] = P1_Pt2(M, g)

    return normal_shock_data
