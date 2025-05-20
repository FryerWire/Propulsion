
"""
Isentropic Flow Solver
Subclass of CompressibleFlow
"""



# Imports =========================================================================================
# Local Imports -----------------------------------------------------------------------------------
import numpy as np
from scipy.optimize import brentq


# Global Imports ----------------------------------------------------------------------------------
from Flow_Solvers.compressible_flow import CompressibleFlow



# Normal Shock Relations ==========================================================================
def M2(M, gamma):
    return float(np.sqrt((2 + (gamma - 1) * M**2) / (2 * gamma * M**2 - (gamma - 1))))

# Pressure Ratios ---------------------------------------------------------------------------------
def P2_P1(M, gamma):
    return 1 + (2 * gamma / (gamma + 1)) * (M**2 - 1)

def Pt1_P1(M, gamma):
    return (1 + ((gamma - 1) / 2) * (M ** 2)) ** (gamma / (gamma - 1))

def Pt2_Pt1(M, gamma):
    A = (((gamma + 1) / 2) * M**2) / (1 + ((gamma - 1) / 2) * M**2)
    B = 1 / (((2 * gamma) / (gamma + 1)) * M**2 - ((gamma - 1) / (gamma + 1)))
    return A**(gamma / (gamma - 1)) * B**(1 / (gamma - 1))

def P1_Pt2(M, gamma):
    return 1 / (Pt2_Pt1(M, gamma) * Pt1_P1(M, gamma))

# Density Ratios ---------------------------------------------------------------------------------
def rho2_rho1(M, gamma):
    return ((gamma + 1) * M**2) / ((gamma - 1) * M**2 + 2)

# Temperature Ratios ---------------------------------------------------------------------------------
def T2_T1(M, gamma):
    return (2 + (gamma - 1) * M**2) * (2 * gamma * M**2 - (gamma - 1)) / ((gamma + 1)**2 * M**2)



# brentq Function Solvers =========================================================================
def SOLVE_M_from_M2(M, target, gamma):
    return M2(M, gamma) - target

# Pressure Ratios ---------------------------------------------------------------------------------
def SOLVE_M_from_Pt2_Pt1(M, target, gamma):
    return Pt2_Pt1(M, gamma) - target

def SOLVE_M_from_P2_P1(M, target, gamma):
    return P2_P1(M, gamma) - target

def SOLVE_M_from_Pt1_P1(M, target, gamma):
    return Pt1_P1(M, gamma) - target

def SOLVE_M_from_P1_Pt2(M, target, gamma):
    return P1_Pt2(M, gamma) - target

# Temperature Ratios ------------------------------------------------------------------------------
def SOLVE_M_from_T2_T1(M, target, gamma):
    return T2_T1(M, gamma) - target

# Density Ratios ----------------------------------------------------------------------------------
def SOLVE_M_from_rho2_rho1(M, target, gamma):
    return rho2_rho1(M, gamma) - target



# Normal Shock Subclass of Compressible Flow ======================================================
class NormalShock(CompressibleFlow):
    """
    NormalShock is the child class of CompressibleFlow.
    Computes the normal shock flow properties from any given input.
    
    Attributes:
    - Inherits from CompressibleFlow superclass.
    
    Methods:
    - computation() : Computes all isentropic flow values.
    - __getattr__() : Creates attributes to any given varaible. 
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
        data      : dict[str, dict[str, float]] = {'Normal': {}}
        
        
        # Flow Solvers ----------------------------------------------------------------------------
        # Mach ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        if (input_var == 'M'):
            self.mach = input_val
            if (self.mach <= 1.0):
                raise ValueError('M > 1')
            
        elif (input_var == 'M2'):
            if (input_val >= 1):
                raise ValueError('0 < M2 < 1')
            
            self.mach = brentq(SOLVE_M_from_M2, mach_min, mach_max, args = (input_val, gamma))        
        
        # Pressure ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        elif (input_var == 'Pt2_Pt1'):
            if (not 0 < input_val < 1):
                raise ValueError('0 < Pt2_Pt1 < 1')
            
            self.mach = brentq(SOLVE_M_from_Pt2_Pt1, mach_min, mach_max, args = (input_val, gamma))
            
        elif (input_var == 'P2_P1'):
            if (input_val < 1):
                raise ValueError('P2_P1 > 1')
            
            self.mach = brentq(SOLVE_M_from_P2_P1, mach_min, mach_max, args = (input_val, gamma))
            
        elif (input_var == 'Pt1_P1'):
            if (input_val < 1):
                raise ValueError('Pt1_P1 >= 1')
            
            self.mach = brentq(SOLVE_M_from_Pt1_P1, mach_min, mach_max, args = (input_val, gamma))
            
        elif (input_var == 'P1_Pt2'):
            if (input_val >= 1):
                raise ValueError('0 < P1_Pt2 < 1')
            
            self.mach = brentq(SOLVE_M_from_P1_Pt2, mach_min, mach_max, args = (input_val, gamma))    
        
        # Temperature +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        elif (input_var == 'T2_T1'):
            if (input_val < 1):
                raise ValueError('T2_T1 > 1')
            
            self.mach = brentq(SOLVE_M_from_T2_T1, mach_min, mach_max, args = (input_val, gamma))
            
        # Density +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        elif (input_var == 'rho2_rho1'):
            if (input_val < 1):
                raise ValueError('rho2_rho1 > 1')
            
            self.mach = brentq(SOLVE_M_from_rho2_rho1, mach_min, mach_max, args = (input_val, gamma))
            
        else:
            raise ValueError(f'Unknown input_var: {input_var}')


        # Data Organization -----------------------------------------------------------------------
        data['Normal']['M1'] = self.mach
        for flow_regime in ['Normal']:
            if ('M1' in data[flow_regime]):
                data[flow_regime]['M1'] = float(self.mach)
                data[flow_regime]['M2'] = float(M2(self.mach, gamma))
                data[flow_regime]['P2_P1'] = float(P2_P1(self.mach, gamma))
                data[flow_regime]['rho2_rho1'] = float(rho2_rho1(self.mach, gamma))
                data[flow_regime]['T2_T1'] = float(T2_T1(self.mach, gamma))
                data[flow_regime]['Tt2_Tt1'] = 1.0
                data[flow_regime]['Pt2_Pt1'] = float(Pt2_Pt1(self.mach, gamma))
                data[flow_regime]['Pt1_P1'] = float(Pt1_P1(self.mach, gamma))
                data[flow_regime]['P1_Pt2'] = float(P1_Pt2(self.mach, gamma))
                
        self.results = data



    def __getattr__(self, attribute_title: str) -> float:
        """
        Creates decorators for each flow property. 
        
        Parameter:
        - attribute_title (str) : Attribute title

        Raises:
        - AttributeError if name not found in any regime.
        
        Examples:
        >>> NS.M2
        >>> NS.Pt2_Pt1
        """
        
        for regime in self.results.values():
            if (attribute_title in regime):
                return regime[attribute_title]
            
        raise AttributeError(f"'{self.__class__.__name__}' has no attribute '{attribute_title}'")
    