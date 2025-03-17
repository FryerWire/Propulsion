
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
from Utilities.fancy_printer import section_printer as fprint

# Problem Solvers ---------------------------------------------------------------------------------
# from Problem_Solvers.solutions import answer_checking as check


# External Imports ================================================================================
import numpy as np



# Main Program ====================================================================================
gas_parameters = {'R': 287, 'g': 1.4, 'cp': 1004}







                  
# # check(TEST_1, TEST_2)
# print(map(TEST_1))
# # fprint(map(TEST_1))
    