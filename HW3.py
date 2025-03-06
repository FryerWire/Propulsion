
"""
Fanno Flow Calculator
Start Date        : 3/4/2025
Modification Date : 3/4/2025
"""


from fanno_flow import fanno_flow_solver as ffc
import rayleigh_flow as rfc
import isentropic_flow as ifc
import normal_shocks as nsc
from turbojet import turbojet_solver as tjc
from variable_mapping import variable_mapping as map

import numpy as np

# Main Program ====================================================================================
gas_parameters = {'R': 287, 'g': 1.4, 'cp': 1004}


# Problem 1 =======================================================================================
M0 = 222.222 / np.sqrt(1.4 * 287 * 223.15)
# p1_knowns = {'M0': M0, 'T0': 223.15, 'P0': 24000, 'Tt4': 1093.15, 'h': 43300000, 'A': 0.08}


# Problem 2 =======================================================================================
# Design ------------------------------------------------------------------------------------------
p2_knowns = {'P0': 101000, 'T0': 288, 'tau_t': 0.7, 'M0': 0, 'Tt4': 1950}

result = tjc(p2_knowns)



# Fancy Printer ===================================================================================
full_data = dict(map(result)) 
for main_category, sub_dict in full_data.items():
    print(f"\n{main_category}:")
    
    for sub_category, values in sub_dict.items():
        if isinstance(values, dict):  
            print(f"\n  {sub_category}:")
            
            for key, value in values.items():
                print(f"    {key}: {value}")
                
        else: 
            print(f"  {sub_category}: {values}")
