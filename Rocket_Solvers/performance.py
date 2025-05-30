
"""
Performance Controller Class
"""



# Imports =========================================================================================
# Global Imports ----------------------------------------------------------------------------------
from Rocket_Solvers.general_equations import GeneralEquations



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
        
        self.gen_eq = GeneralEquations(self.parameters)

        