
"""
Rayleigh Flow Calculator
Subclass of CompressibleFlow
"""



# Imports =========================================================================================
# Local Imports -----------------------------------------------------------------------------------
from scipy.optimize import brentq


# Global Imports ----------------------------------------------------------------------------------
from Flow_Solvers.compressible_flow import CompressibleFlow



# Rayleigh Flow Relations ========================================================================
def u_ustar(M, gamma):
    return ((gamma + 1) * M**2) / (1 + gamma * M**2)

# Pressure Ratios ---------------------------------------------------------------------------------
def P_Pstar(M, gamma):
    return (gamma + 1) / (1 + gamma * M**2)

def Pt_Ptstar(M, gamma):
    term_1 = ((gamma + 1) / (1 + gamma * M**2))
    term_2 = ((2 / (gamma + 1)) * (1 + ((gamma - 1) / 2) * M**2))**(gamma / (gamma - 1))
    return term_1 * term_2

# Density Ratios ----------------------------------------------------------------------------------
def rho_rhostar(M, gamma):
    return (1 + gamma * M**2) / ((gamma + 1) * M**2)

# Temperature Ratios ------------------------------------------------------------------------------
def T_Tstar(M, gamma):
    return ((gamma + 1)**2 * M**2) / (1 + gamma * M**2)**2

def Tt_Ttstar(M, gamma):
    term_1 = ((2 * ((gamma + 1) * M**2)) / (1 + gamma * M**2)**2)
    term_2 = (1 + ((gamma - 1) / 2) * M**2)
    return term_1 * term_2



# brentq Function Solvers ========================================================================
def SOLVE_M_from_u_ustar(M, target, gamma):
    return u_ustar(M, gamma) - target

# Pressure Ratios ---------------------------------------------------------------------------------
def SOLVE_M_from_P_Pstar(M, target, gamma):
    return P_Pstar(M, gamma) - target

def SOLVE_M_from_Pt_Ptstar(M, target, gamma):
    return Pt_Ptstar(M, gamma) - target

# Density Ratios ----------------------------------------------------------------------------------
def SOLVE_M_from_rho_rhostar(M, target, gamma):
    return rho_rhostar(M, gamma) - target

# Temperature Ratios ------------------------------------------------------------------------------
def SOLVE_M_from_T_Tstar(M, target, gamma):
    return T_Tstar(M, gamma) - target

def SOLVE_M_from_Tt_Ttstar(M, target, gamma):
    return Tt_Ttstar(M, gamma) - target



# Rayleigh Flow Subclass of Compressible Flow =====================================================
class RayleighFlow(CompressibleFlow):
    """
    RayleighFlow is the child class of CompressibleFlow.
    Computes the Rayleigh flow properties from any given input. 
    
    Attributes:
    - Inherits from CompressibleFlow superclass.
    
    Methods:
    - computation() : Computes all Rayleigh flow values. 
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
        data      : dict[str, dict[str, float]] = {'Subsonic': {}, 'Supersonic': {}}
        
        
        # Flow Solvers ----------------------------------------------------------------------------
        # Mach ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        if (input_var == 'M'):
            self.mach: float = input_val
            if (self.mach <= 0):
                raise ValueError('M must be greater than 0')
            
            flow_regime: str = 'Subsonic' if (self.mach < 1) else 'Supersonic'
            data[flow_regime]['M'] = self.mach

        # Pressure Ratio -------------------------------------------------------------------------------
        elif (input_var == 'P_Pstar'):
            if (input_val <= 0):
                raise ValueError('P/P* must be positive')
            
            mach_subsonic: float = brentq(SOLVE_M_from_P_Pstar, mach_min, 0.999999, args = (input_val, gamma))
            mach_supersonic: float = brentq(SOLVE_M_from_P_Pstar, 1.000001, mach_max, args = (input_val, gamma))
            data['Subsonic']['M'] = mach_subsonic
            data['Supersonic']['M'] = mach_supersonic

        # Density Ratio --------------------------------------------------------------------------------
        elif (input_var == 'rho_rhostar'):
            if (input_val <= 0):
                raise ValueError('rho/rho* must be positive')
            
            mach_subsonic: float = brentq(SOLVE_M_from_rho_rhostar, mach_min, 0.999999, args = (input_val, gamma))
            mach_supersonic: float = brentq(SOLVE_M_from_rho_rhostar, 1.000001, mach_max, args = (input_val, gamma))
            data['Subsonic']['M'] = mach_subsonic
            data['Supersonic']['M'] = mach_supersonic

        # Temperature Ratio ----------------------------------------------------------------------------
        elif (input_var == 'T_Tstar'):
            if (input_val <= 0):
                raise ValueError('T/T* must be positive')
            
            mach_subsonic: float = brentq(SOLVE_M_from_T_Tstar, mach_min, 0.999999, args = (input_val, gamma))
            mach_supersonic: float = brentq(SOLVE_M_from_T_Tstar, 1.000001, mach_max, args = (input_val, gamma))
            data['Subsonic']['M'] = mach_subsonic
            data['Supersonic']['M'] = mach_supersonic

        # Velocity Ratio -------------------------------------------------------------------------------
        elif (input_var == 'u_ustar'):
            if (input_val <= 0):
                raise ValueError('u/u* must be positive')
            
            mach_subsonic: float = brentq(SOLVE_M_from_u_ustar, mach_min, 0.999999, args = (input_val, gamma))
            mach_supersonic: float = brentq(SOLVE_M_from_u_ustar, 1.000001, mach_max, args = (input_val, gamma))
            data['Subsonic']['M'] = mach_subsonic
            data['Supersonic']['M'] = mach_supersonic

        # Stagnation Pressure Ratio --------------------------------------------------------------------
        elif (input_var == 'Pt_Ptstar'):
            if (input_val <= 0):
                raise ValueError('Pt/Pt* must be positive')
            
            mach_subsonic: float = brentq(SOLVE_M_from_Pt_Ptstar, mach_min, 0.999999, args = (input_val, gamma))
            mach_supersonic: float = brentq(SOLVE_M_from_Pt_Ptstar, 1.000001, mach_max, args = (input_val, gamma))
            data['Subsonic']['M'] = mach_subsonic
            data['Supersonic']['M'] = mach_supersonic

        # Stagnation Temperature Ratio -----------------------------------------------------------------
        elif (input_var == 'Tt_Ttstar'):
            if (input_val <= 0):
                raise ValueError('Tt/Tt* must be positive')
            
            mach_subsonic: float = brentq(SOLVE_M_from_Tt_Ttstar, mach_min, 0.999999, args = (input_val, gamma))
            mach_supersonic: float = brentq(SOLVE_M_from_Tt_Ttstar, 1.000001, mach_max, args = (input_val, gamma))
            data['Subsonic']['M'] = mach_subsonic
            data['Supersonic']['M'] = mach_supersonic
        
        else:
            raise ValueError(f'Unknown input_var: {input_var}')
        
        
        # Data Organiztion ------------------------------------------------------------------------
        for flow_regime in ['Subsonic', 'Supersonic']:
            if ('M' in data[flow_regime]):
                data[flow_regime]['M'] = float(self.mach)
                data[flow_regime]['P_Pstar'] = float(P_Pstar(self.mach, gamma))
                data[flow_regime]['rho_rhostar'] = float(rho_rhostar(self.mach, gamma))
                data[flow_regime]['T_Tstar'] = float(T_Tstar(self.mach, gamma))
                data[flow_regime]['u_ustar'] = float(u_ustar(self.mach, gamma))
                data[flow_regime]['Pt_Ptstar'] = float(Pt_Ptstar(self.mach, gamma))
                data[flow_regime]['Tt_Ttstar'] = float(Tt_Ttstar(self.mach, gamma))
                
        self.results = data
        
        
        
    def __getattr__(self, attribute_title: str) -> float:
        """
        Creates decorators for each flow property. 
        
        Parameter:
        - attribute_title (str) : Attribute title

        Raises:
        - AttributeError if name not found in any regime.
        
        Examples:
        >>> RF.P_Pstar
        >>> RF.Tt_Ttstar
        """
        
        for regime in self.results.values():
            if (attribute_title in regime):
                return regime[attribute_title]
            
        raise AttributeError(f"'{self.__class__.__name__}' has no attribute '{attribute_title}'")
