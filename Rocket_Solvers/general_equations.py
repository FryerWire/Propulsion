
"""
Mass Subcontroller of Performance Controller
"""


import numpy as np



class GeneralEquations:
    """
    Variables:
    - m_0 (float) : Wet/Initial mass
    - m_f (float) : Dry/final mass
    - m_p (float) : Propellant mass
    """
    
    def __init__(self, parameters) -> None:
        """Text"""
        
        self.p: dict[str, float] = parameters
                        
    
    def propellant_mass(self) -> float:        
        """
        Propellant Mass: m_p
        
        Variables:
        - m_0 (float) : Wet/initial mass
        - m_f (float) : Dry/final mass
        
        Returns:
        - m_p (float) : Propellant mass
        
        Raises:
        - ValueError: ABC
        """
        
        m_0 = self.p.get('m_0')
        m_f = self.p.get('m_f')
        if ((m_0 is None) or (m_f is None)):
            raise ValueError("'Function' is needs ABC and ABC")
        
        return m_0 - m_f
    
    
    def mass_ratio(self) -> float:        
        """
        Mass Ratio: MR
        
        Variables:
        - m_0 (float) : Wet/initial mass
        - m_f (float) : Dry/final mass
        
        Returns:
        - MR (float) : Mass Ratio
        
        Raises:
        - ValueError: ABC
        """
        
        m_0 = self.p.get('m_0')
        m_f = self.p.get('m_f')
        if ((m_0 is None) or (m_f is None)):
            raise ValueError("'Function' is needs ABC and ABC")
        
        return m_f / m_0
            
    
    def propellant_mass_fraction(self) -> float:
        """
        Propellant Mass Fraction: zeta
        
        Variables:
        - m_0 (float) : Wet/initial mass
        - m_f (float) : Dry/final mass
        
        Returns:
        - zeta (float) : Propellant mass fraction
        
        Raises:
        - ValueError: ABC
        """
        
        m_0 = self.p.get('m_0')
        m_f = self.p.get('m_f')
        if ((m_0 is None) or (m_f is None)):
            raise ValueError("'Function' is needs ABC and ABC")
                
        return (m_0 - m_f) / (m_0 - self.propellant_mass())
    
    
    def propellant_mass_flow_rate(self) -> float:
        """
        Propellant Mass Flow Rate: m_dot
        
        Variables:
        - t (float) : Time
        
        Returns:
        - m_dot (float) : Propellant mass flow rate
        
        Raises:
        - ValueError: ABC
        """
        
        t = self.p['t']
        if (t is None):
            raise ValueError("'Function' is needs ABC and ABC")
        
        return self.propellant_mass() / t
    
    
    def effective_exhaust_velocity(self) -> float:
        """
        Effective Exhaust Velocity: c
        
        Variables:
        - I_S (float) : Specific impulse
        - g_0 (float) : Sea-level gravity
        - F (float)   : Thrust
        
        Returns:
        - c (float) : Effective Exhaust Velocity
        
        Raises:
        - ValueError: ABC
        """
        
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
        Area: A
        
        Parameters:
        - diameter_key (str) : Key name of the diameter.
        
        Variables:
        - D (float) : Diameter
        
        Returns:
        - (float) : Area
        
        Raises:
        - ValueError: ABC
        """
        
        D = self.p.get(diameter_key)
        if (D is None):
            raise KeyError(f"Diameter '{diameter_key}' not found in parameters.")
        
        return np.pi * ((D / 2) ** 2)
            
    
    def thrust(self) -> float:
        """
        Thrust: F
        
        Returns:
        - F (float) : Thrust
        """
        
        return self.propellant_mass_flow_rate() * self.effective_exhaust_velocity()
    
    
    def total_impulse(self) -> float:
        """
        Total Impulse: I_tot
        
        Variables:
        - t (float) : Time
        
        Returns:
        - I_t (float) : Total impulse
        """
        
        t = self.p.get('t')
        if (t is None):
            raise ValueError("'Function' is needs ABC and ABC")
        
        return self.thrust() * t
    
    
    def weight(self) -> float:
        """
        Weigt: w
        
        Variables:
        - m_0 (float) : Wet/initial mass
        - m_p (float) : Propellant mass
        - g_0 (float) : Sea level gravity
        
        Returns:
        - w (float) : Weight
        """
        
        m_0 = self.p.get('m_0')
        m_p = self.p.get('m_p')
        g_0 = self.p.get('g_0')
        if ((m_0 is None) or (m_p is None) or (g_0 is None)):
            raise ValueError("'Function' is needs ABC and ABC")
        
        return (m_0 - m_p) * g_0
    
    
    def impulse_to_weight(self) -> float:
        """
        Impulse-to-Weight: I_t__to__w_0
        
        Returns:
        - I_t__to__w_0 (float) : Total impulse to propellant weight
        """
        
        return self.total_impulse() / self.weight()
    
    
    def final_acceleration(self) -> float:
        """
        Acceleration: a
        
        Variables:
        - m_f (float) : Dry/final mass
        
        Returns:
        - a (float) : Acceleration
        """
        
        m_f = self.p.get('m_f')
        if (m_f is None):
            raise ValueError("'Function' is needs ABC and ABC")
        
        return self.thrust() / self.m_f
    
    
    def characteristic_velocity(self, diameter_key: str) -> float:
        """
        Characteristic Velocity: c*
        
        Parameters:
        - diameter_key (str) : Key for which diameter to use for cross-sectional area
        
        Variables:
        - D (float) : Diameter
        - P_1 (float) : Chamber pressure
        
        Returns:
        - c* (float) : Characteristic velocity
        """
        
        D = self.p.get(diameter_key)
        P_1 = self.p.get('P_1')
        if ((D is None) or (P_1 is None)):
            raise KeyError(f"Diameter '{diameter_key}' not found in parameters.")
        
        return P_1 * self.area(diameter_key) / self.propellant_mass_flow_rate()
    
    
    def pressure_thrust(self, diameter_key: str) -> float:
        """
        Pressure Thrust Term: (P_2 - P_3) * A_2
        
        Parameters:
        - diameter_key (str) : Key for which diameter to use for cross-sectional area
        
        Variables:
        - P_2 (float) : Nozzle exit pressure
        - P_3 (float) : Ambient pressure
        - A_2 (float) : Nozzle exit area
        
        Returns:
        - (P_2 - P_3) * A_2 (float) : Pressure thrust
        """
        
        P_2 = self.p.get('P_2')
        P_3 = self.p.get('P_3')
        D = self.p.get(diameter_key)
        if ((D is None) or (P_2 is None) or (P_3 is None)):
            raise KeyError(f"Diameter '{diameter_key}' not found in parameters.")
        
        A_2 = self.area(diameter_key)
        
        return (P_2 - P_3) * A_2
    
    
    def exit_velocity(self, diameter_key: str) -> float:
        """
        Nozzle Exit Velocity: v_2
        
        Variables:
        - m_dot (float) : Propellant mass flow rate
        - P_2 (float)   : Chamber pressure
        - P_3 (float)   : Ambient pressure
        - A_2 (float)   : Nozzle exit area
        - F (float)     : Thrust
        
        Returns:
        - v_2 (float) : Nozzle exit velocity
        """
        
        F = self.p.get('F')
        P_2 = self.p.get('P_2')
        P_3 = self.p.get('P_3')
        A_2 = self.area(diameter_key)
        m_dot = self.propellant_mass_flow_rate()
        if ((F is None) or (P_2 is None) or (P_3 is None)):
            raise ValueError()
        
        return (F - (P_2 - P_3) * A_2) / m_dot
        
        
    def get_parameter(self, key: str) -> float:
        """
        Retrieves a parameter by key.
        Raises KeyError if the parameter is not found.
        """
        
        if (key not in self.p):
            raise KeyError(f"Mass requires parameter '{key}")
        
        return self.p[key]
    