
"""
Mass Subcontroller of Performance Controller
"""


import numpy as np



class GeneralEquations:
    """
    Text
    """
    
    def __init__(self, parameters) -> None:
        """Text"""
        
        self.p: dict[str, float] = parameters
                        
    
    def propellant_mass(self) -> float:
        """Propellant Mass: m_prop"""
        return self.p['m_0'] - self.p['m_f']
    
    
    def mass_ratio(self) -> float:
        """Mass Ratio: MR"""
        return self.p['m_f'] / self.p['m_0']
    
    
    def propellant_mass_fraction(self) -> float:
        """Propellant Mass Fraction: zeta"""
        return (self.p['m_0'] - self.p['m_f']) / (self.p['m_0'] - self.p['m_p'])
    
    
    def propellant_mass_flow_rate(self) -> float:
        """Propellant Mass Flow Rate: m_dot"""
        return self.propellant_mass() / self.p['t']
    
    
    def effective_exhaust_velocity(self) -> float:
        """Effective Exhaust Velocity: c"""
        
        I_S = self.p.get('I_S')
        g_0 = self.p.get('g_0')
        F = self.p.get('F')
        
        if ((I_S is not None) and (g_0 is not None)):
            return I_S * g_0
        elif (F is not None):
            return F / self.propellant_mass_flow_rate()
        else:
            raise ValueError('Missing Required Variable')
        
        
    def area(self, diameter_key: str) -> float:
        """
        Computes cross-sectional area from any given diameter.
        
        Parameters:
        - diameter_key (str) : Key name of the diameter.
        
        Returns:
        - (float) : Area
        
        Raises:
        - KeyError if the specified diameter is not provided. 
        """
        
        D = self.p.get(diameter_key)
        if (D is None):
            raise KeyError(f"Diameter '{diameter_key}' not found in parameters.")
        
        return np.pi * ((D / 2) ** 2)
            
    
    def thrust(self) -> float:
        """Thrust: F"""
        return self.propellant_mass_flow_rate() * self.effective_exhaust_velocity()
    
    
    def total_impulse(self) -> float:
        """Total Impulse: I_tot"""
        return self.thrust() * self.p['t']
    
    
    def weight(self) -> float:
        """Weigt: w"""
        return (self.p['m_0'] - self.p['m_p']) * self.p['g_0']
    
    
    def impulse_to_weight(self) -> float:
        """Impulse-to-Weight: I_to_w"""
        return self.total_impulse() / self.weight()
    
    
    def final_acceleration(self) -> float:
        return self.thrust() / self.m_f
    
    
    def characteristic_velocity(self, diameter_key: str) -> float:
        """Characteristic Velocity: c*"""
        """
        Characteristic Velocity: c*
        
        Parameters:
        - diameter_key (str) : Key for which diameter to use for cross-sectional area
        
        Returns:
        - (float) : Characteristic Velocity
        """
        
        D = self.p.get(diameter_key)
        if (D is None):
            raise KeyError(f"Diameter '{diameter_key}' not found in parameters.")
        
        return self.p['P'] * self.area(diameter_key) / self.propellant_mass_flow_rate()
    
    
    def pressure_thrust(self, diameter_key: str) -> float:
        """
        Pressure Thrust Term: (P2 - P3) * A
        
        Parameters:
        - diameter_key (str) : Key for which diameter to use for cross-sectional area
        
        Returns:
        - (float) : Pressure thrust
        """
        
        P2 = self.p['P2']
        P3 = self.p['P3']
        D = self.p.get(diameter_key)
        if (D is None):
            raise KeyError(f"Diameter '{diameter_key}' not found in parameters.")
        
        A = self.area(diameter_key)
        
        return (P2 - P3) * A
    
    
    def exit_velocity(self, diameter_key: str) -> float:
        """
        Text
        """
        
        F = self.p['F']
        m_dot = self.propellant_mass_flow_rate()
        P2 = self.p['P2']
        P3 = self.p['P3']
        A2 = self.area(diameter_key)
        
        return (F - (P2 - P3) * A2) / m_dot
        
        
    def get_parameter(self, key: str) -> float:
        """
        Retrieves a parameter by key.
        Raises KeyError if the parameter is not found.
        """
        
        if (key not in self.p):
            raise KeyError(f"Mass requires parameter '{key}")
        
        return self.p[key]
    