
"""
Fanno Flow Calculator
Start Date        : 3/4/2025
Modification Date : 3/4/2025
"""


from fanno_flow import fanno_flow_solver as ffc
import rayleigh_flow as rfc
import isentropic_flow as ifc
import normal_shocks as nsc
from turbojet import turbo_jet_solver as tjc
from variable_mapping import variable_mapping as map



# Main Program ====================================================================================
gas_parameters = {'R': 287, 'g': 1.4, 'cp': 1004}

# Knowns
# knowns = {'M0': 2, 'P0': 10000, 'T0': 273.15 - 45, 'pi_c': 12, 'tau_lambda': 8, 'tau_t': 0.735}
# knowns = {'M0': 1.5, 'P0': 25000, 'T0': 223, 'Tt4': 1900, 'h': 42800000}
# knowns = {'Tt4': 1200, 'T0': 261, 'M0': 0.6, 'tau_c': 2}
# knowns = {'M0': 2, 'pi_c': 9, 'T0': 200, 'Tt4': 1200}
# knowns = {'M0': 2.5, 'P0': 15000, 'T0': 273.15 - 40, 'pi_c': 14, 'Tt4': 1800, 'h': 42000000}
knowns = {'M0': 0.4, 'P0': 95000, 'T0': 283.15, 'm0_dot': 65, 'pi_c': 25, 'tau_lambda': 6, 'h': 428000000}

result = tjc(knowns, gas_parameters)



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
