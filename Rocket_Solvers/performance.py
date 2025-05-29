
"""
Performance Controller Class
"""



# Imports =========================================================================================
# Global Imports ----------------------------------------------------------------------------------
from Rocket_Solvers.mass import Mass
# from Rocket_Solvers.flow import 
# from Rocket_Solvers.force import
# from Rocket_Solvers.impulse import



class Performance:
    """
    Performance controller
    
    Methods:
    - __init__ : 
    """
    
    def __init__(self, **kwargs) -> None:
        """
        Text
        """
        
        self.parameters: dict[str, float] = kwargs
        self.g_0: float = kwargs.get('g_0', 9.81)
        self.gamma: float = kwargs.get('gamma', 1.2)
        
        self.mass = Mass(self.parameters)
        self.force = force(self.parameters)
        self.impulse = impulse(self.parameters)
        self.flow = flow(self.parameters)
        