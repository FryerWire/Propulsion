
"""
CompressibleFlow Superclass
"""



class CompressibleFlow:
    """
    CompressibleFlow is the superclass that handles the following flow regimes:
    - Isentropic Flow
    - Normal Shock
    - Oblique Shock
    - Fanno Flow
    - Rayleigh Flow
    
    Attributes:
    - input_var (str)   : Name of the input variable
    - input_val (float) : The value of the input variable
    - gamma (float)     : Heat capacity ratio, default at 1.4
    - _mach (float)     : Private Mach number
    - results (dict)    : Flow result summary
    
    Methods:
    - computation() : Child class placeholder method
    - summary       : Shows all flow results as a dictionary
    - __str__()     : Fancy formatter of the values
    """
    
    def __init__(self, input_var: str, input_val: float, gamma: float = 1.4) -> None:
        """
        Constructor to initialize the compressible flow. 
        
        Parameters:
        - input_var (str)   : Name of the input variable
        - input_val (float) : The value of the input variable
        - gamma (float)     : Heat capacity ratio, default at 1.4
        """
        
        self.input_var : str = input_var
        self.input_val : float = input_val
        self.gamma     : float = gamma
        self._mach     : float | None = None
        self.results   : dict = {}
        
        self.computation()
        
        
    def __str__(self) -> str:
        """
        Flow summary printer
        
        Returns:
        - (str) : Summary of the computed results
        """
        
        lines = [f"{self.__class__.__name__} Flow Summary:"]
        for regime, variables in self.summary.items():
            if (not variables):
                continue
            
            lines.append(f"{regime} Flow:")
            for key, value in variables.items():
                lines.append(f"    {key:12s} = {value:.6f}")
            lines.append("")
            
        return "\n".join(lines)
        
    
    @property
    def mach(self) -> float | None:
        """
        Getter for the Mach value
        
        Returns: 
        - (float) | (None) : The current Mach value or 'None' if not assigned.
        """
        
        return self._mach
    
    
    @mach.setter
    def mach(self, value: float) -> None:
        """
        Setter for the Mach number. Validation checker before it is assigned.
        
        Parameters:
        - value (float) : Mach number assigning.
        
        Raises:
        - ValueError : If the Mach number is not positive.
        """
        
        if (value <= 0):
            raise ValueError("Mach number must be positive")
        
        self._mach = value
    
    
    @property
    def summary(self) -> dict[str, dict[str, float]]:
        """
        Summary of the computed flow.
        
        Returns:
        - (dict[str, dict[str, float]]) : Results in dictionary format.
        
        Raises:
        - AttributeError : If 'results' attribute is missing.
        """
        
        if (hasattr(self, "results")):
            return self.results
        else:
            raise AttributeError("Computation has not been run yet.")
        
    
    def computation(self) -> None:
        """
        Superclass placeholder method.
        
        Raises:
        - NotImplementedError : When the superclass 'computation' method is called.
        """
        
        raise NotImplementedError("computation() must be implemeted in the subclass.")
