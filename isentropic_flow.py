
"""
Normal Shock Calculator
Start Date        : 2/24/2025
Modification Date : 3/4/2025
"""



import numpy as np
from scipy.optimize import brentq



# Isentropic Flow Relations ======================================================================
def A_Astar(M, g):
    term = (2 / (g + 1)) * (1 + ((g - 1) / 2) * (M ** 2))
    return (1 / M) * (term ** ((g + 1) / (2 * (g - 1))))

# Pressure Ratios ---------------------------------------------------------------------------------
def P_Pt(M, g):
    return (1 + ((g - 1) / 2) * (M ** 2)) ** (-g / (g - 1))

def P_Pstar(M, g):
    term_1 = 1 + ((g - 1) / 2) * (M ** 2)
    term_2 = 1 + ((g - 1) / 2)  
    return (term_2 / term_1) ** (g / (g - 1))  

def Pstar_P0(g):
    return (2 / (g + 1)) ** (1 / (g - 1))

# Density Ratios ----------------------------------------------------------------------------------
def rho_rhot(M, g):
    return (1 + ((g - 1) / 2) * (M ** 2)) ** (-1 / (g - 1))

def rho_rhostar(M, g):
    term_1 = 1 + ((g - 1) / 2) * (M ** 2)
    term_2 = 1 + ((g - 1) / 2) 
    return (term_2 / term_1) ** (1 / (g - 1))  

def rhostar_rho0(g):
    return (2 / (g + 1)) ** (1 / (g - 1))

# Temperature Ratios ------------------------------------------------------------------------------
def T_Tt(M, g):
    return (1 + ((g - 1) / 2) * (M ** 2)) ** (-1)

def T_Tstar(M, g):
    term_1 = 1 + ((g - 1) / 2) * (M ** 2)
    term_2 = 1 + ((g - 1) / 2)  
    return term_2 / term_1

def Tstar_T0(g):
    return 2 / (g + 1)

# Angles ------------------------------------------------------------------------------------------
def nu(M, g):
    if M < 1:
        return 0
    
    term_1 = np.sqrt((g + 1) / (g - 1))
    term_2 = np.arctan(np.sqrt(((g - 1) / (g + 1)) * ((M ** 2) - 1)))
    term_3 = np.arctan(np.sqrt((M ** 2) - 1))
    return term_1 * term_2 - term_3

def mu(M):
    if M < 1:
        return 0
    
    return np.arcsin(1 / M)



# brentq Function Solvers =========================================================================
def SOLVE_M_from_A_Astar(M, target, g):
    return A_Astar(M, g) - target

def SOLVE_M_from_P_Pt(M, target, g):
    return P_Pt(M, g) - target

def SOLVE_M_from_P_Pstar(M, target, g):
    return P_Pstar(M, g) - target

def SOLVE_M_from_rho_rhot(M, target, g):
    return rho_rhot(M, g) - target

def SOLVE_M_from_rho_rhostar(M, target, g):
    return rho_rhostar(M, g) - target

def SOLVE_M_from_T_Tt(M, target, g):
    return T_Tt(M, g) - target

def SOLVE_M_from_T_Tstar(M, target, g):
    return T_Tstar(M, g) - target

def SOLVE_M_from_nu(M, target, g):
    return nu(M, g) - target

def SOLVE_M_from_mu(M, target):
    return mu(M) - target



# Isentropic Flow Calculator =====================================================================
def iscentropic_flow_solver(input_var, input_value, g = 1.4):
    """
    Calculates all isentropic flow values given any input.
    
    Parameters:
    - input_var (string)  : 'M', 'A_Astar', 'P_Pt', 'P_Pstar', 'rho_rhot', 'rho_rhostar', 'T_Tt', 'T_Tstar', 'nu', 'mu'.
    - input_value (float) : Any positive float value.
    - g (float)           : Heat capacity ratio (default 1.4 for air).
    
    Returns:
    - iscentropic_flow_data (dict) : Dictionary of all the values for isentropic flow.
    
    Example:
    >>> iscentropic_flow_solver("M", 2)

    >>> print(iscentropic_flow_solver("M", 3, 1.4)["Supersonic"]["P1_Pt2"])
    """

    M_min = 1e-6
    M_max = 10

    iscentropic_flow_data = {"Subsonic": {}, "Supersonic": {}}
    
    # Mach Number ----------------------------------------------------------------------------------
    if (input_var == 'M'):
        M = input_value
        if M <= 0:
            raise ValueError("M must be greater than 0")
        regime = "Subsonic" if M < 1 else "Supersonic"
        iscentropic_flow_data[regime]["M"] = M

    # Area Ratio -----------------------------------------------------------------------------------
    elif (input_var == 'A_Astar'):
        if (input_value <= 1):
            raise ValueError("A/A* must be greater than 1")
        
        M_subsonic = brentq(SOLVE_M_from_A_Astar, M_min, 0.999999, args = (input_value, g))
        M_supersonic = brentq(SOLVE_M_from_A_Astar, 1.000001, M_max, args = (input_value, g))
        
        # Subsonic Solution
        iscentropic_flow_data["Subsonic"]["M"] = M_subsonic
        iscentropic_flow_data["Subsonic"]["A_Astar"] = A_Astar(M_subsonic, g)
        iscentropic_flow_data["Subsonic"]["P_Pt"] = P_Pt(M_subsonic, g)
        iscentropic_flow_data["Subsonic"]["P_Pstar"] = P_Pstar(M_subsonic, g)
        iscentropic_flow_data["Subsonic"]["rho_rhot"] = rho_rhot(M_subsonic, g)
        iscentropic_flow_data["Subsonic"]["rho_rhostar"] = rho_rhostar(M_subsonic, g)
        iscentropic_flow_data["Subsonic"]["T_Tt"] = T_Tt(M_subsonic, g)
        iscentropic_flow_data["Subsonic"]["T_Tstar"] = T_Tstar(M_subsonic, g)
        iscentropic_flow_data["Subsonic"]["nu"] = nu(M_subsonic, g)
        iscentropic_flow_data["Subsonic"]["mu"] = mu(M_subsonic)
        
        # Supersonic Solution
        iscentropic_flow_data["Supersonic"]["M"] = M_supersonic
        iscentropic_flow_data["Supersonic"]["A_Astar"] = A_Astar(M_supersonic, g)
        iscentropic_flow_data["Supersonic"]["P_Pt"] = P_Pt(M_supersonic, g)
        iscentropic_flow_data["Supersonic"]["P_Pstar"] = P_Pstar(M_supersonic, g)
        iscentropic_flow_data["Supersonic"]["rho_rhot"] = rho_rhot(M_supersonic, g)
        iscentropic_flow_data["Supersonic"]["rho_rhostar"] = rho_rhostar(M_supersonic, g)
        iscentropic_flow_data["Supersonic"]["T_Tt"] = T_Tt(M_supersonic, g)
        iscentropic_flow_data["Supersonic"]["T_Tstar"] = T_Tstar(M_supersonic, g)
        iscentropic_flow_data["Supersonic"]["nu"] = nu(M_supersonic, g)
        iscentropic_flow_data["Supersonic"]["mu"] = mu(M_supersonic)

    # Pressure Ratios ------------------------------------------------------------------------------
    elif (input_var == 'P_Pt'):
        if not (0 < input_value < 1):
            raise ValueError("0 < P/Pt < 1")
        M = brentq(SOLVE_M_from_P_Pt, M_min, M_max, args = (input_value, g))
        regime = "Subsonic" if M < 1 else "Supersonic"
        iscentropic_flow_data[regime]["M"] = M

    elif (input_var == 'P_Pstar'):
        if (input_value <= 0):
            raise ValueError("P/P* must be positive")
        M = brentq(SOLVE_M_from_P_Pstar, M_min, M_max, args = (input_value, g))
        regime = "Subsonic" if M < 1 else "Supersonic"
        iscentropic_flow_data[regime]["M"] = M

    # Density Ratios ------------------------------------------------------------------------------
    elif (input_var == 'rho_rhot'):
        if not (0 < input_value < 1):
            raise ValueError("0 < rho/rho_t < 1")
        M = brentq(SOLVE_M_from_rho_rhot, M_min, M_max, args = (input_value, g))
        regime = "Subsonic" if M < 1 else "Supersonic"
        iscentropic_flow_data[regime]["M"] = M

    elif (input_var == 'rho_rhostar'):
        if (input_value <= 0):
            raise ValueError("rho/rho* must be positive")
        M = brentq(SOLVE_M_from_rho_rhostar, M_min, M_max, args = (input_value, g))
        regime = "Subsonic" if M < 1 else "Supersonic"
        iscentropic_flow_data[regime]["M"] = M

    # Temperature Ratios --------------------------------------------------------------------------
    elif (input_var == 'T_Tt'):
        if not (0 < input_value < 1):
            raise ValueError("0 < T/Tt < 1")
        M = brentq(SOLVE_M_from_T_Tt, M_min, M_max, args = (input_value, g))
        regime = "Subsonic" if M < 1 else "Supersonic"
        iscentropic_flow_data[regime]["M"] = M

    elif (input_var == 'T_Tstar'):
        if (input_value <= 0):
            raise ValueError("T/T* must be positive")
        M = brentq(SOLVE_M_from_T_Tstar, M_min, M_max, args = (input_value, g))
        regime = "Subsonic" if M < 1 else "Supersonic"
        iscentropic_flow_data[regime]["M"] = M

    # Angles --------------------------------------------------------------------------------------
    elif (input_var == 'nu'):
        if (input_value <= 0):
            raise ValueError("nu must be positive")
        M = brentq(SOLVE_M_from_nu, 1, M_max, args = (input_value, g))
        regime = "Supersonic"  
        iscentropic_flow_data[regime]["M"] = M

    elif (input_var == 'mu'):
        if not (0 < input_value < np.pi / 2):
            raise ValueError("0 < mu < pi/2")
        M = brentq(SOLVE_M_from_mu, 1, M_max, args = (input_value,))
        regime = "Supersonic"  
        iscentropic_flow_data[regime]["M"] = M
    
    else:
        raise ValueError("Unknown input variable. Use 'M', 'A_Astar', 'P_Pt', 'P_Pstar', 'rho_rhot', 'rho_rhostar', 'T_Tt', 'T_Tstar', 'nu', or 'mu'.")

    for regime in ["Subsonic", "Supersonic"]:
        if "M" in iscentropic_flow_data[regime]:
            M = iscentropic_flow_data[regime]["M"]
            iscentropic_flow_data[regime]["A_Astar"] = A_Astar(M, g)
            iscentropic_flow_data[regime]["P_Pt"] = P_Pt(M, g)
            iscentropic_flow_data[regime]["P_Pstar"] = P_Pstar(M, g)
            iscentropic_flow_data[regime]["rho_rhot"] = rho_rhot(M, g)
            iscentropic_flow_data[regime]["rho_rhostar"] = rho_rhostar(M, g)
            iscentropic_flow_data[regime]["T_Tt"] = T_Tt(M, g)
            iscentropic_flow_data[regime]["T_Tstar"] = T_Tstar(M, g)
            iscentropic_flow_data[regime]["nu"] = nu(M, g)
            iscentropic_flow_data[regime]["mu"] = mu(M)

    return iscentropic_flow_data
