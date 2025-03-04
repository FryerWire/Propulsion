
"""
Rayleigh Flow Calculator
Start Date        : 3/4/2025
Modification Date : 3/4/2025
"""



from scipy.optimize import brentq



# Rayleigh Flow Relations ========================================================================
def P_Pstar(M, g):
    return (g + 1) / (1 + g * M**2)

def rho_rhostar(M, g):
    return (1 + g * M**2) / ((g + 1) * M**2)

def T_Tstar(M, g):
    return ((g + 1)**2 * M**2) / (1 + g * M**2)**2

def u_ustar(M, g):
    return ((g + 1) * M**2) / (1 + g * M**2)

def Pt_Ptstar(M, g):
    term_1 = ((g + 1) / (1 + g * M**2))
    term_2 = ((2 / (g + 1)) * (1 + ((g - 1) / 2) * M**2))**(g / (g - 1))
    return term_1 * term_2

def Tt_Ttstar(M, g):
    term_1 = ((2 * ((g + 1) * M**2)) / (1 + g * M**2)**2)
    term_2 = (1 + ((g - 1) / 2) * M**2)
    return term_1 * term_2



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



# Rayleigh Flow Calculator =======================================================================
def rayleigh_flow_solver(input_var, input_value, g = 1.4):
    """
    Calculates all Rayleigh flow values given any input.
    
    Parameters:
    - input_var (string)  : 'M', 'P_Pstar', 'rho_rhostar', 'T_Tstar', 'u_ustar', 'Pt_Ptstar', 'Tt_Ttstar'
    - input_value (float) : Any positive float value
    - g (float)           : Heat capacity ratio (default 1.4 for air)
    
    Returns:
    - rayleigh_flow_data (dict) : Dictionary of all values for Rayleigh flow
    
    Example:
    >>> rayleigh_flow_solver("M", 2)
    >>> print(rayleigh_flow_solver("M", 0.5, 1.4)["Subsonic"]["P_Pstar"])
    """

    M_min = 1e-6
    M_max = 10

    rayleigh_flow_data = {"Subsonic": {}, "Supersonic": {}}
    
    # Mach Number ----------------------------------------------------------------------------------
    if (input_var == 'M'):
        M = input_value
        if (M <= 0):
            raise ValueError("M must be greater than 0")
        regime = "Subsonic" if M < 1 else "Supersonic"
        rayleigh_flow_data[regime]["M"] = M

    # Pressure Ratio -------------------------------------------------------------------------------
    elif (input_var == 'P_Pstar'):
        if (input_value <= 0):
            raise ValueError("P/P* must be positive")
        M_subsonic = brentq(SOLVE_M_from_P_Pstar, M_min, 0.999999, args = (input_value, g))
        M_supersonic = brentq(SOLVE_M_from_P_Pstar, 1.000001, M_max, args = (input_value, g))
        
        rayleigh_flow_data["Subsonic"]["M"] = M_subsonic
        rayleigh_flow_data["Supersonic"]["M"] = M_supersonic

    # Density Ratio --------------------------------------------------------------------------------
    elif (input_var == 'rho_rhostar'):
        if (input_value <= 0):
            raise ValueError("rho/rho* must be positive")
        M_subsonic = brentq(SOLVE_M_from_rho_rhostar, M_min, 0.999999, args=(input_value, g))
        M_supersonic = brentq(SOLVE_M_from_rho_rhostar, 1.000001, M_max, args=(input_value, g))
        
        rayleigh_flow_data["Subsonic"]["M"] = M_subsonic
        rayleigh_flow_data["Supersonic"]["M"] = M_supersonic

    # Temperature Ratio ----------------------------------------------------------------------------
    elif (input_var == 'T_Tstar'):
        if (input_value <= 0):
            raise ValueError("T/T* must be positive")
        M_subsonic = brentq(SOLVE_M_from_T_Tstar, M_min, 0.999999, args=(input_value, g))
        M_supersonic = brentq(SOLVE_M_from_T_Tstar, 1.000001, M_max, args=(input_value, g))
        
        rayleigh_flow_data["Subsonic"]["M"] = M_subsonic
        rayleigh_flow_data["Supersonic"]["M"] = M_supersonic

    # Velocity Ratio -------------------------------------------------------------------------------
    elif (input_var == 'u_ustar'):
        if (input_value <= 0):
            raise ValueError("u/u* must be positive")
        M_subsonic = brentq(SOLVE_M_from_u_ustar, M_min, 0.999999, args=(input_value, g))
        M_supersonic = brentq(SOLVE_M_from_u_ustar, 1.000001, M_max, args=(input_value, g))
        
        rayleigh_flow_data["Subsonic"]["M"] = M_subsonic
        rayleigh_flow_data["Supersonic"]["M"] = M_supersonic

    # Stagnation Pressure Ratio --------------------------------------------------------------------
    elif (input_var == 'Pt_Ptstar'):
        if (input_value <= 0):
            raise ValueError("Pt/Pt* must be positive")
        M_subsonic = brentq(SOLVE_M_from_Pt_Ptstar, M_min, 0.999999, args=(input_value, g))
        M_supersonic = brentq(SOLVE_M_from_Pt_Ptstar, 1.000001, M_max, args=(input_value, g))
        
        rayleigh_flow_data["Subsonic"]["M"] = M_subsonic
        rayleigh_flow_data["Supersonic"]["M"] = M_supersonic

    # Stagnation Temperature Ratio -----------------------------------------------------------------
    elif (input_var == 'Tt_Ttstar'):
        if (input_value <= 0):
            raise ValueError("Tt/Tt* must be positive")
        M_subsonic = brentq(SOLVE_M_from_Tt_Ttstar, M_min, 0.999999, args=(input_value, g))
        M_supersonic = brentq(SOLVE_M_from_Tt_Ttstar, 1.000001, M_max, args=(input_value, g))
        
        rayleigh_flow_data["Subsonic"]["M"] = M_subsonic
        rayleigh_flow_data["Supersonic"]["M"] = M_supersonic
    
    else:
        raise ValueError("Unknown input variable. Use 'M', 'P_Pstar', 'rho_rhostar', 'T_Tstar', 'u_ustar', 'Pt_Ptstar', or 'Tt_Ttstar'.")

    for regime in ["Subsonic", "Supersonic"]:
        if "M" in rayleigh_flow_data[regime]:
            M = rayleigh_flow_data[regime]["M"]
            rayleigh_flow_data[regime]["P_Pstar"] = P_Pstar(M, g)
            rayleigh_flow_data[regime]["rho_rhostar"] = rho_rhostar(M, g)
            rayleigh_flow_data[regime]["T_Tstar"] = T_Tstar(M, g)
            rayleigh_flow_data[regime]["u_ustar"] = u_ustar(M, g)
            rayleigh_flow_data[regime]["Pt_Ptstar"] = Pt_Ptstar(M, g)
            rayleigh_flow_data[regime]["Tt_Ttstar"] = Tt_Ttstar(M, g)

    return rayleigh_flow_data
