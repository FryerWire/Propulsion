
"""
Main Program
Start Date        : 3/4/2025
Modification Date : 3/14/2025
"""



# Local Imports ===================================================================================
# Flow Solvers File -------------------------------------------------------------------------------
from Flow_Solvers.fanno_flow import fanno_flow_solver as ffc
from Flow_Solvers.isentropic_flow import iscentropic_flow_solver as ifs
from Flow_Solvers.normal_shocks import normal_shock_solver as nss
from Flow_Solvers.rayleigh_flow import rayleigh_flow_solver as rfs

# Utilities ---------------------------------------------------------------------------------------
from Utilities.unit_converter import unit_conversion as unit
from Utilities.variable_mapping import variable_mapping as map
from Utilities.fancy_printer import fancy_printing as fprint



# External Imports ================================================================================
import numpy as np



# Main Program ====================================================================================
gas_parameters = {'R': 287, 'g': 1.4, 'cp': 1004}
                  
sections = [
    {'Section Num': 1, 'Flow Type': 'Isentropic', 'V': 240, 'P': 170000, 'T': 320, 'M': 0.67, 'Tt': 349, 'Pt': 230000},
    {'Section Num': 2, 'Flow Type': 'Isentropic', 'V': 290, 'P': 170000, 'Tt': 349, 'T': 307, 'Pt': 211000}
]

print(map(sections))

# fprint(map(gas_parameters, sections))
