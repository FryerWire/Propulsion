
"""
Normal Shock Calculator
Start Date        : 2/24/2025
Modification Date : 3/4/2025
"""


import numpy as np


# Iscentropic Flow Relations ======================================================================
def A_Astar(M, g):
    term_1 = (1 / M) * ((g - 1) / 2) ** (-(g + 1) / (2 * (g - 1)))
    term_2 = (1 + ((g - 1) / 2) * (M ** 2)) * (-g / (g - 1))
    return term_1 * term_2

# def m_dot(M, g, Pt, Tt):
#     term_1 = (Pt / np.sqrt(R * Tt)) * A * np.sqrt(g) * M
#     term_2 = ((1 + ((g - 1) / 2) * (M ** 2)) ** ((g + 1) / (2 - (2 * g))))
#     return term_1 * term_2

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
    term_1 = np.sqrt((g + 1) / (g - 1))
    term_2 = np.arctan(np.sqrt(((g - 1) / (g + 1)) * ((M ** 2) - 1)))
    term_3 = np.arctan(np.sqrt((M ** 2) - 1))
    return term_1 * term_2 - term_3

def mu(M):
    return np.arcsin(1 / M)






