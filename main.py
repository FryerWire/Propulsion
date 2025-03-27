
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
from Problem_Solvers.edu_checking_printer import eduprint

# External Imports ================================================================================
import numpy as np



# Main Program ====================================================================================
gas_parameters = {'R': 287, 'g': 1.4, 'cp': 1004}


checking = {'Sections': 
                [
                    {'Section Num': 1, 'Flow Type': 'Isentropic', 'V1': 241, 'P1': 180000, 'T1': 320, 'M1': 0.66, 'Tt1': 410, 'Pt1': 230000, 'Tt0': 410}, 
                    {'Section Num': 2, 'Flow Type': 'Isentropic', 'V2': 290, 'P2': 170000, 'Tt2': 349, 'T2': 307, 'Pt2': 211000, 'A/A*': 3, 'A1/A0': 2}
                ]
            }   

# eduprint(checking, 'L3')

fprint(checking)
