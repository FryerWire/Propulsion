
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
from Problem_Solvers.solutions import answer_checking as check


# External Imports ================================================================================
import numpy as np



# Main Program ====================================================================================
gas_parameters = {'R': 287, 'g': 1.4, 'cp': 1004}

# Testing Solutions ===============================================================================
TEST_1 = {
    'Sections' : [
        {'Section Num': 1, 'Flow Type': 'Isentropic', 'V1': 240, 'P1': 170000, 'T1': 320, 'M1': 0.67, 'Tt1': 349, 'Pt1': 230000},
        {'Section Num': 2, 'Flow Type': 'Isentropic', 'V2': 290, 'P2': 170000, 'Tt2': 349, 'T2': 307, 'Pt2': 211000}
    ]
}

TEST_2 = {
    'Sections' : [
        {'Section Num': 1, 'Flow Type': 'Isentropic', 'V1': 480, 'P1': 170000, 'T1': 320, 'M1': 0.67, 'Tt1': 349, 'Pt1': 738},
        {'Section Num': 2, 'Flow Type': 'Isentropic', 'V2': 290, 'P2': 180, 'Tt2': 349, 'T2': 307, 'Pt2': 211000, 'Z': 10}
    ]
}
                  
# check(TEST_1, TEST_2)
# print(map(TEST_1))
fprint(map(TEST_1))
