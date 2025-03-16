
"""
Problem Solutions
Start Date        : 3/16/2025
Modification Date : 3/16/2025
"""



# Local Imports ===================================================================================
# Utilities ---------------------------------------------------------------------------------------
from Utilities.unit_converter import unit_conversion as units



# Lecture Solutions ===============================================================================
L3_SOL = {
    'Sections' : [
        {'Section Num': 1, 'Flow Type': 'Isentropic', 'V1': 240, 'P1': 170000, 'T1': 320, 'M1': 0.67, 'Tt1': 349, 'Pt1': 230000},
        {'Section Num': 2, 'Flow Type': 'Isentropic', 'V2': 290, 'P2': 170000, 'Tt2': 349, 'T2': 307, 'Pt2': 211000}
    ]
}

L4_SOL = {
    'Sections' : [
        {'Section Num': 0, 'Flow Type': 'Isentropic', 'M0': 1.8, 'P0': units(0.3, 'atm', 'Pa'), 'T0': 250, 'Pt0': units(1.724, 'atm', 'Pa'), 'Tt0': 412},
        {'Section Num': 1, 'Flow Type': 'Normal', 'M1': 0.6165, 'Pt1': units(1.4, 'atm', 'Pa')},
        {'Section Num': 2, 'Flow Type': 'Isentropic', 'Pt2': units(1.4, 'atm', 'Pa'), 'Tt2': 412, 'M2': 0.168, 'P2': units(1.373, 'atm', 'units'), 'T2': 410}
    ]
}



# Quiz Solutions ==================================================================================
Q1_SOL = {
    'Sections' : [
        {'Section Num': 1, 'Flow Type': 'Isentropic', 'T1': 288, 'P1': 100000, 'M1': 0.3, 'Tt1': 273.5},
        {'Section Num': 2, 'Flow Type': 'Isentropic', 'M2': 0.6, 'Tt2': 273.5, 'P2': 48700}
    ]
}


