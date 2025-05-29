
"""
Mass Subcontroller of Performance Controller
"""



class Mass:
    """
    Mass subcontroller of the Performance controller.
    
    Methods:
    - __init__                 : 
    - propellant_mass          : 
    - mass_ratio               :
    - propellant_mass_fraction :
    - get_parameters           :
    """
    
    def __init__(self, parameters) -> None:
        """Text"""
        
        self.p: dict[str, float] = parameters
            
            
    
    """
    Convert all the stuff to the subcontroller below
    It is becoming a general equation solver.
    Class will be called GeneralEquations
    """    
            
            
            
    
    def propellant_mass(self) -> float:
        """Propellant Mass: m_prop"""
        return self.parameters['m_0'] - self.parameters['m_f']
    
    
    def mass_ratio(self) -> float:
        """Mass Ratio: MR"""
        return self.parameters['m_f'] / self.parameters['m_0']
    
    
    def propellant_mass_fraction(self) -> float:
        """Propellant Mass Fraction: zeta"""
        return (self.parameters['m_0'] - self.parameters['m_f']) / (self.parameters['m_0'] - self.parameters['m_p'])
    
    
    def propellant_mass_flow_rate(self) -> float:
        """Propellant Mass Flow Rate: m_dot"""
        return self.propellant_mass() / self.parameters['t']
    
    
    def effective_exhaust_velocity(self) -> float:
        """Effective Exhaust Velocity: c"""
        return self.parameters['I_S'] * self.parameters['g_0']
    
    
    def thrust(self) -> float:
        """Thrust: F"""
        return self.propellant_mass_flow_rate() * self.effective_exhaust_velocity()
    
    
    def total_impulse(self) -> float:
        """Total Impulse: I_tot"""
        return self.thrust() * self.parameters['t']
    
    
    def weight(self) -> float:
        """Weigt: w"""
        return (self.parameters['m_0'] - self.parameters['m_p']) * self.parameters['g_0']
    
    
    def impulse_to_weight(self) -> float:
        """Impulse-to-Weight: I_to_w"""
        return self.total_impulse() / self.weight()
    
    
    def final_acceleration(self, in_Gs = False) -> float:
        """
        Final Acceleration: a
        
        ** THIS WILL CHANGE TO THE UNITS CONFIGURATION FOR G'S **
        
        Parameters:
        - in_Gs (bool) : Sets the unit g's
        """
        
        self.in_Gs: bool = in_Gs
        
        if (self.in_Gs):
            return (self.thrust() / self.m_f) / self.g_0
        else:
            return self.thrust() / self.m_f
        
        
        
        
    
    def get_parameter(self, key: str) -> float:
        """
        Retrieves a parameter by key.
        Raises KeyError if the parameter is not found.
        """
        
        if (key not in self.p):
            raise KeyError(f"Mass requires parameter '{key}")
        
        return self.p[key]
    