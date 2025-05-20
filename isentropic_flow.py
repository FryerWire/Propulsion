
"""
Isentropic Flow Solver
Subclass of CompressibleFlow
"""



# Imports =========================================================================================
# Local Imports -----------------------------------------------------------------------------------
import numpy as np
from scipy.optimize import brentq


# Global Imports ----------------------------------------------------------------------------------
from compressible_flow import CompressibleFlow



# Isentropic Flow Relations ======================================================================
def A_Astar(M, gamma):
    term = (2 / (gamma + 1)) * (1 + ((gamma - 1) / 2) * (M ** 2))
    return (1 / M) * (term ** ((gamma + 1) / (2 * (gamma - 1))))

# Pressure Ratios ---------------------------------------------------------------------------------
def P_Pt(M, gamma):
    return (1 + ((gamma - 1) / 2) * (M ** 2)) ** (-gamma / (gamma - 1))

def P_Pstar(M, gamma):
    term_1 = 1 + ((gamma - 1) / 2) * (M ** 2)
    term_2 = 1 + ((gamma - 1) / 2)  
    return (term_2 / term_1) ** (gamma / (gamma - 1))  

def Pstar_P0(gamma):
    return (2 / (gamma + 1)) ** (1 / (gamma - 1))

# Density Ratios ----------------------------------------------------------------------------------
def rho_rhot(M, gamma):
    return (1 + ((gamma - 1) / 2) * (M ** 2)) ** (-1 / (gamma - 1))

def rho_rhostar(M, gamma):
    term_1 = 1 + ((gamma - 1) / 2) * (M ** 2)
    term_2 = 1 + ((gamma - 1) / 2) 
    return (term_2 / term_1) ** (1 / (gamma - 1))  

def rhostar_rho0(gamma):
    return (2 / (gamma + 1)) ** (1 / (gamma - 1))

# Temperature Ratios ------------------------------------------------------------------------------
def T_Tt(M, gamma):
    return (1 + ((gamma - 1) / 2) * (M ** 2)) ** (-1)

def T_Tstar(M, gamma):
    term_1 = 1 + ((gamma - 1) / 2) * (M ** 2)
    term_2 = 1 + ((gamma - 1) / 2)  
    return term_2 / term_1

def Tstar_T0(gamma):
    return 2 / (gamma + 1)

# Angles ------------------------------------------------------------------------------------------
def nu(M, gamma):
    if M < 1:
        return 0
    
    term_1 = np.sqrt((gamma + 1) / (gamma - 1))
    term_2 = np.arctan(np.sqrt(((gamma - 1) / (gamma + 1)) * ((M ** 2) - 1)))
    term_3 = np.arctan(np.sqrt((M ** 2) - 1))
    return term_1 * term_2 - term_3

def mu(M):
    if M < 1:
        return 0
    
    return np.arcsin(1 / M)



# brentq Function Solvers =========================================================================
def SOLVE_M_from_A_Astar(M, target, gamma):
    return A_Astar(M, gamma) - target

def SOLVE_M_from_P_Pt(M, target, gamma):
    return P_Pt(M, gamma) - target

def SOLVE_M_from_P_Pstar(M, target, gamma):
    return P_Pstar(M, gamma) - target

def SOLVE_M_from_rho_rhot(M, target, gamma):
    return rho_rhot(M, gamma) - target

def SOLVE_M_from_rho_rhostar(M, target, gamma):
    return rho_rhostar(M, gamma) - target

def SOLVE_M_from_T_Tt(M, target, gamma):
    return T_Tt(M, gamma) - target

def SOLVE_M_from_T_Tstar(M, target, gamma):
    return T_Tstar(M, gamma) - target

def SOLVE_M_from_nu(M, target, gamma):
    return nu(M, gamma) - target

def SOLVE_M_from_mu(M, target):
    return mu(M) - target



# Isentropic Flow Subclass of Compressible Flow ===================================================
class IsentropicFlow(CompressibleFlow):
    """
    IsentropicFlow is the child class of CompressibleFlow.
    Computes the isentropic flow properties from any given input. 
    
    Attributes:
    - Inherits from CompressibleFlow superclass.
    
    Methods:
    - computation() : Computes all isentropic flow values. 
    - __getattr__() : Creates attributes to any given variable. 
    """
    
    def computation(self) -> None:
        """
        Computes flow properties from the 'input_var' and 'input_val'.
        Data is stored in the 'self.results' attribute.
        
        Raises:
        - ValueError : Unknown input_var
        """
        
        gamma     : float = self.gamma
        input_var : str = self.input_var
        input_val : float = self.input_val
        mach_min  : float = 1e-6
        mach_max  : float = 1e6
        data      : dict[str, float] = {}
                
        
        # Flow Solvers ----------------------------------------------------------------------------
        # Mach ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        if (input_var == 'M'):
            self.mach = input_val
            flow_regime: str = 'Subsonic' if (self.mach < 1) else 'Supersonic'
            data[flow_regime]['M'] = self.mach
        
        # Area ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        elif (input_var == "A_Astar"):
            M_sub: float = brentq(SOLVE_M_from_A_Astar, mach_min, 0.999999, args = (input_val, gamma))
            M_sup: float = brentq(SOLVE_M_from_A_Astar, 1.000001, mach_max, args = (input_val, gamma))
            data["Subsonic"]["M"] = M_sub
            data["Supersonic"]["M"] = M_sup

        # Pressure ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        elif (input_var == "P_Pt"):
            self.mach = brentq(SOLVE_M_from_P_Pt, mach_min, mach_max, args = (input_val, gamma))
            flow_regime = "Subsonic" if (self.mach < 1) else "Supersonic"
            data[flow_regime]["M"] = self.mach

        elif (input_var == "P_Pstar"):
            self.mach = brentq(SOLVE_M_from_P_Pstar, mach_min, mach_max, args = (input_val, gamma))
            flow_regime = "Subsonic" if (self.mach < 1) else "Supersonic"
            data[flow_regime]["M"] = self.mach

        # Density +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        elif (input_var == "rho_rhot"):
            self.mach = brentq(SOLVE_M_from_rho_rhot, mach_min, mach_max, args = (input_val, gamma))
            flow_regime = "Subsonic" if (self.mach < 1) else "Supersonic"
            data[flow_regime]["M"] = self.mach

        elif (input_var == "rho_rhostar"):
            self.mach = brentq(SOLVE_M_from_rho_rhostar, mach_min, mach_max, args = (input_val, gamma))
            flow_regime = "Subsonic" if (self.mach < 1) else "Supersonic"
            data[flow_regime]["M"] = self.mach

        # Temperature +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        elif (input_var == "T_Tt"):
            self.mach = brentq(SOLVE_M_from_T_Tt, mach_min, mach_max, args = (input_val, gamma))
            flow_regime = "Subsonic" if (self.mach < 1) else "Supersonic"
            data[flow_regime]["M"] = self.mach

        elif (input_var == "T_Tstar"):
            self.mach = brentq(SOLVE_M_from_T_Tstar, mach_min, mach_max, args = (input_val, gamma))
            flow_regime = "Subsonic" if (self.mach < 1) else "Supersonic"
            data[flow_regime]["M"] = self.mach

        # Angles ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        elif (input_var == "nu"):
            self.mach = brentq(SOLVE_M_from_nu, 1, mach_max, args = (input_val, gamma))
            data["Supersonic"]["M"] = self.mach

        elif (input_var == "mu"):
            self.mach = brentq(SOLVE_M_from_mu, 1, mach_max, args = (input_val,))
            data["Supersonic"]["M"] = self.mach

        else:
            raise ValueError(f"Unknown input_var: {input_var}")


        # Data Organiztion ------------------------------------------------------------------------
        for flow_regime in ["Subsonic", "Supersonic"]:
            if ("M" in data[flow_regime]):
                data[flow_regime]["M"] = float(self.mach)
                data[flow_regime]["A_Astar"] = float(A_Astar(self.mach, gamma))
                data[flow_regime]["P_Pt"] = float(P_Pt(self.mach, gamma))
                data[flow_regime]["P_Pstar"] = float(P_Pstar(self.mach, gamma))
                data[flow_regime]["rho_rhot"] = float(rho_rhot(self.mach, gamma))
                data[flow_regime]["rho_rhostar"] = float(rho_rhostar(self.mach, gamma))
                data[flow_regime]["T_Tt"] = float(T_Tt(self.mach, gamma))
                data[flow_regime]["T_Tstar"] = float(T_Tstar(self.mach, gamma))
                data[flow_regime]["nu"] = float(nu(self.mach, gamma))
                data[flow_regime]["mu"] = float(mu(self.mach))
                
        self.results = data
        
        
        
    def __getattr__(self, attribute_title: str) -> float:
        """
        Creates decorators for each flow property. 
        
        Parameter:
        - attribute_title (str) : Attribute title

        Raises:
        - AttributeError if name not found in any regime.
        
        Examples:
        >>> IF.P_Pt
        >>> IF.T_Tt
        """
        
        for regime in self.results.values():
            if (attribute_title in regime):
                return regime[attribute_title]
            
        raise AttributeError(f"'{self.__class__.__name__}' has no attribute '{attribute_title}'")
