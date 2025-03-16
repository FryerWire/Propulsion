
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

section_01 = {'Section Num': '01', 'Flow Type': 'Fanno', 'M0': 0.5, 'T0': 300, 'Q': 123}
section_12 = {'Section Num': '12', 'Flow Type': 'Isentropic', 'M1': 1.2, 'Pt1/Pt0': 200, 'Z': 123}
sections = [section_01, section_12]

fprint(map(gas_parameters, sections))
