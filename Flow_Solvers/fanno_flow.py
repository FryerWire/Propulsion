
"""
Fanno Flow Calculator
Start Date        : 3/4/2025
Modification Date : 3/4/2025
"""



import numpy as np
from scipy.optimize import brentq



# Fanno Flow Relations ===========================================================================
def P_Pstar(M, g):
    return (1 / M) * (1 / np.sqrt((2 / (g + 1)) * (1 + ((g - 1) / 2) * M**2)))

def rho_rhostar(M, g):
    return np.sqrt((2 / (g + 1)) * (1 + ((g - 1) / 2) * M**2)) / M

def T_Tstar(M, g):
    return 1 / ((2 / (g + 1)) * (1 + ((g - 1) / 2) * M**2))

def u_ustar(M, g):
    return M / np.sqrt((2 / (g + 1)) * (1 + ((g - 1) / 2) * M**2))

def Pt_Ptstar(M, g):
    return (1 / M) * ((2 / (g + 1)) * (1 + ((g - 1) / 2) * M**2))**((g + 1) / (2 * (g - 1)))

def Tt_Ttstar(M, g):
    return 1.0  

def rhot_rhotstar(M, g):
    return (1 / M) * ((2 / (g + 1)) * (1 + ((g - 1) / 2) * M**2))**((g + 1) / (2 * (g - 1)))

def cfLstar_D(M, g):
    term_1 = ((1 - M**2) / (g * M**2))
    term_2 = ((g + 1) / (2 * g))
    term_3 = np.log(M**2 / ((2 / (g + 1)) * (1 + ((g - 1) / 2) * M**2)))
    return term_1 + term_2 * term_3



# brentq Function Solvers ========================================================================
def SOLVE_M_from_P_Pstar(M, target, g):
    return P_Pstar(M, g) - target

def SOLVE_M_from_rho_rhostar(M, target, g):
    return rho_rhostar(M, g) - target

def SOLVE_M_from_T_Tstar(M, target, g):
    return T_Tstar(M, g) - target

def SOLVE_M_from_u_ustar(M, target, g):
    return u_ustar(M, g) - target

def SOLVE_M_from_Pt_Ptstar(M, target, g):
    return Pt_Ptstar(M, g) - target

def SOLVE_M_from_Tt_Ttstar(M, target, g):
    return Tt_Ttstar(M, g) - target

def SOLVE_M_from_rhot_rhotstar(M, target, g):
    return rhot_rhotstar(M, g) - target

def SOLVE_M_from_cfLstar_D(M, target, g):
    return cfLstar_D(M, g) - target



# Fanno Flow Calculator ==========================================================================
def fanno_flow_solver(input_var, input_value, g = 1.4):
    """
    Calculates all Fanno flow values given any input.
    
    Parameters:
    - input_var (string)  : 'M', 'P_Pstar', 'rho_rhostar', 'T_Tstar', 'u_ustar', 'Pt_Ptstar', 
                            'rhot_rhotstar', 'cfLstar_D'
    - input_value (float) : Any positive float value (except cfLstar_D which can be negative)
    - g (float)           : Heat capacity ratio (default 1.4 for air)
    
    Returns:
    - fanno_flow_data (dict) : Dictionary of all values for Fanno flow
    
    Example:
    >>> fanno_flow_solver("M", 0.5)
    >>> print(fanno_flow_solver("M", 0.5, 1.4)["Subsonic"]["P_Pstar"])
    """

    M_min = 1e-6
    M_max = 100

    fanno_flow_data = {"Subsonic": {}, "Supersonic": {}}
    
    # Mach Number ----------------------------------------------------------------------------------
    if (input_var == 'M'):
        M = input_value
        if (M <= 0):
            raise ValueError("M must be greater than 0")
        regime = "Subsonic" if M < 1 else "Supersonic"
        fanno_flow_data[regime]["M"] = M

    # Pressure Ratio -------------------------------------------------------------------------------
    elif (input_var == 'P_Pstar'):
        if (input_value <= 0):
            raise ValueError("P/P* must be positive")
        M_subsonic = brentq(SOLVE_M_from_P_Pstar, M_min, 0.999999, args=(input_value, g))
        M_supersonic = brentq(SOLVE_M_from_P_Pstar, 1.000001, M_max, args=(input_value, g))
        fanno_flow_data["Subsonic"]["M"] = M_subsonic
        fanno_flow_data["Supersonic"]["M"] = M_supersonic

    # Density Ratio --------------------------------------------------------------------------------
    elif (input_var == 'rho_rhostar'):
        if (input_value <= 0):
            raise ValueError("rho/rho* must be positive")
        M_subsonic = brentq(SOLVE_M_from_rho_rhostar, M_min, 0.999999, args=(input_value, g))
        M_supersonic = brentq(SOLVE_M_from_rho_rhostar, 1.000001, M_max, args=(input_value, g))
        fanno_flow_data["Subsonic"]["M"] = M_subsonic
        fanno_flow_data["Supersonic"]["M"] = M_supersonic

    # Temperature Ratio ----------------------------------------------------------------------------
    elif (input_var == 'T_Tstar'):
        if (input_value <= 0):
            raise ValueError("T/T* must be positive")
        M_subsonic = brentq(SOLVE_M_from_T_Tstar, M_min, 0.999999, args=(input_value, g))
        M_supersonic = brentq(SOLVE_M_from_T_Tstar, 1.000001, M_max, args=(input_value, g))
        fanno_flow_data["Subsonic"]["M"] = M_subsonic
        fanno_flow_data["Supersonic"]["M"] = M_supersonic

    # Velocity Ratio -------------------------------------------------------------------------------
    elif (input_var == 'u_ustar'):
        if (input_value <= 0):
            raise ValueError("u/u* must be positive")
        M_subsonic = brentq(SOLVE_M_from_u_ustar, M_min, 0.999999, args=(input_value, g))
        M_supersonic = brentq(SOLVE_M_from_u_ustar, 1.000001, M_max, args=(input_value, g))
        fanno_flow_data["Subsonic"]["M"] = M_subsonic
        fanno_flow_data["Supersonic"]["M"] = M_supersonic

    # Stagnation Pressure Ratio --------------------------------------------------------------------
    elif (input_var == 'Pt_Ptstar'):
        if (input_value <= 0):
            raise ValueError("Pt/Pt* must be positive")
        M_subsonic = brentq(SOLVE_M_from_Pt_Ptstar, M_min, 0.999999, args=(input_value, g))
        try:
            M_supersonic = brentq(SOLVE_M_from_Pt_Ptstar, 1.000001, M_max, args=(input_value, g))
            fanno_flow_data["Supersonic"]["M"] = M_supersonic
        except ValueError:
            pass 
        fanno_flow_data["Subsonic"]["M"] = M_subsonic

    # Stagnation Density Ratio ---------------------------------------------------------------------
    elif (input_var == 'rhot_rhotstar'):
        if (input_value <= 0):
            raise ValueError("rhot/rhot* must be positive")
        M_subsonic = brentq(SOLVE_M_from_rhot_rhotstar, M_min, 0.999999, args=(input_value, g))
        try:
            M_supersonic = brentq(SOLVE_M_from_rhot_rhotstar, 1.000001, M_max, args=(input_value, g))
            fanno_flow_data["Supersonic"]["M"] = M_supersonic
        except ValueError:
            pass  
        fanno_flow_data["Subsonic"]["M"] = M_subsonic

    # Friction Factor Length-to-Diameter Ratio -----------------------------------------------------
    elif (input_var == 'cfLstar_D'):
        M_subsonic = brentq(SOLVE_M_from_cfLstar_D, M_min, 0.999999, args=(input_value, g))
        M_supersonic = brentq(SOLVE_M_from_cfLstar_D, 1.000001, M_max, args=(input_value, g))
        fanno_flow_data["Subsonic"]["M"] = M_subsonic
        fanno_flow_data["Supersonic"]["M"] = M_supersonic
    
    else:
        raise ValueError("Unknown input variable. Use 'M', 'P_Pstar', 'rho_rhostar', 'T_Tstar', 'u_ustar', "
                        "'Pt_Ptstar', 'rhot_rhotstar', or 'cfLstar_D'.")

    for regime in ["Subsonic", "Supersonic"]:
        if "M" in fanno_flow_data[regime]:
            M = fanno_flow_data[regime]["M"]
            fanno_flow_data[regime]["P_Pstar"] = float(P_Pstar(M, g))
            fanno_flow_data[regime]["rho_rhostar"] = float(rho_rhostar(M, g))
            fanno_flow_data[regime]["T_Tstar"] = float(T_Tstar(M, g))
            fanno_flow_data[regime]["u_ustar"] = float(u_ustar(M, g))
            fanno_flow_data[regime]["Pt_Ptstar"] = float(Pt_Ptstar(M, g))
            fanno_flow_data[regime]["Tt_Ttstar"] = float(Tt_Ttstar(M, g))
            fanno_flow_data[regime]["rhot_rhotstar"] = float(rhot_rhotstar(M, g))
            fanno_flow_data[regime]["cfLstar_D"] = float(cfLstar_D(M, g))

    return fanno_flow_data
