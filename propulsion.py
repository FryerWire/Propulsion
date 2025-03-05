
"""
Fanno Flow Calculator
Start Date        : 3/4/2025
Modification Date : 3/4/2025
"""


from fanno_flow import fanno_flow_solver as ffc
import rayleigh_flow as rfc
import isentropic_flow as ifc
import normal_shocks as nsc



# Main Program ====================================================================================
print(ffc("M", 7))