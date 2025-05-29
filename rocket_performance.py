
"""
Rocket Performance Class
"""



class RocketPerformance:
    """
    Text
    
    Attributes (**kwargs):
    - m_0 (float)    : Initial mass        [kg]
    - m_f (float)    : Final mass          [kg]
    - m_p (float)    : Payload mass        [kg]
    - m_prop (float) : Propellant mass     [kg]
    - t (float)      : Time                [s]
    - t_b (float)    : Burn Time           [s]
    - I_S (float)    : Specific Impulse    [s]
    - g_0 (float)    : Sea Level Gravity   [m / s^2]
    - gamma (float)  : Heat Capacity Ratio [Unitless]
    """
    
    def __init__(self, **kwargs: float) -> None:
        self.parameters: dict[str, float] = kwargs
        self.g_0: float = kwargs.get('g_0', 9.81)
        self.gamma: float = kwargs.get('gamma', 1.4)
        
        
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
        
    
    
    """
    class RocketPerformance:
        def __init__(self, **kwargs):
            self.parameters = kwargs
            self.g_0 = kwargs.get("g_0", 9.81)
            self.gamma = kwargs.get("gamma", 1.4)

            self.mass = RocketMass(self.parameters)
            self.thrust = RocketThrust(self.parameters, self.g_0)
            self.velocity = RocketVelocity(self.parameters, self.g_0)

    
    
    class RocketMass:
        def __init__(self, parameters: dict[str, float]):
            self.p = parameters

        def propellant_mass(self):
            return self.p["m_0"] - self.p["m_f"]

        def mass_ratio(self):
            return self.p["m_0"] / self.p["m_f"]
            
    
    rp = RocketPerformance(m_0=500, m_f=300, m_p=200, t=60, I_S=280)
    print(rp.mass.propellant_mass())
    print(rp.thrust.total_impulse())
    print(rp.velocity.final_acceleration())
    """
    