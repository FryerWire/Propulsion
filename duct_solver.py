
"""
Duct Solver
Start Date        : 3/21/2025
Modification Date : 3/23/2025
"""



# Local Imports ===================================================================================
# Utilities ---------------------------------------------------------------------------------------
from Utilities.unit_converter import unit_conversion as units
from Utilities.fancy_printer import section_printer as fprint

# Flow Solvers ------------------------------------------------------------------------------------
from Flow_Solvers.isentropic_flow import iscentropic_flow_solver as ifs
from Flow_Solvers.normal_shocks import normal_shock_solver as nss
from Flow_Solvers.normal_shocks import Pt1_P1 as test



# Isentropic Duct Solver ==========================================================================
def isentropic_duct():
    return



# Given Data =======================================================================================
sections = [
    {'Section Num': 0, 'Flow Type': 'Isentropic', 'M': 1.8, 'P': units(0.3, 'atm', 'Pa'), 'T': 250},
    {'Section Num': 1, 'Flow Type': 'Normal'},
    {'Section Num': 2, 'Flow Type': 'Isentropic'}
]


# sections = [
#     {'Section Num': 0, 'Flow Type': 'Isentropic', 'M': 1.8, 'P': units(0.3, 'atm', 'Pa'), 'T': 250},
#     {'Section Num': 1, 'Flow Type': 'Normal'}
# ]





for i, section in enumerate(sections):
    print("=========================================================================================")
    section_num = section.get('Section Num')
    flow_type = section.get('Flow Type')
    M = section.get('M') 
    P = section.get('P')
    T = section.get('T')
    A1_A0 = section.get('A1/A0')
    
    # print(f"\n\n{sections}\n\n")
    # fprint(section)
    # print(section)
    
    # fprint({'Sections': [section]})
    
    """
    Try to find M from Area ratio
    """
    
    # Isentropic ----------------------------------------------------------------------------------
    if (flow_type == 'Isentropic'):
        if (M is not None):
            print(f"Section {section_num}: M is explicitly defined as {M}")
            pass
        else:
            if ((i > 0) and (sections[i - 1].get('M') is not None)):
                M = sections[i - 1]['M']
                print(f"Section {section_num}: M is inherited from the previous section as {M}")
            else:
                print(f"Section {section_num}: M is not available")
                continue  # Skip further calculations if M is not available
                
        if (M < 1):
            Pt = P / ifs('M', M)["Subsonic"]["P_Pt"]
            Tt = T / ifs('M', M)["Subsonic"]["T_Tt"]
        else:  
            Pt = P / ifs('M', M)["Supersonic"]["P_Pt"]
            Tt = T / ifs('M', M)["Supersonic"]["T_Tt"]
        
        # Append Pt and Tt to the current section
        section['Pt'] = Pt
        section['Tt'] = Tt
        
        # print(f"\nSection {section_num}: Pt = {units(Pt, 'Pa', 'atm')} [atm], Tt = {Tt}\n")
                

    
    # Normal Shock --------------------------------------------------------------------------------
    elif flow_type == 'Normal':
        if (M is not None):
            print(f"Section {section_num}: M is explicitly defined as {M}")
        else:
            # M = nss('M', M)['M2']
            # section['M'] = M
            # print(f"Section {section_num}: M1 is {M}")
            
            
            if ((i > 0) and (sections[i - 1].get('M') is not None)):
                M0 = sections[i - 1]['M']
                print(f"Section {section_num}: M1 is {M0}")
                M1 = nss('M', M0)['M2']
                print(f"Section {section_num}: M1 is {M1}")
                section['M'] = M1  # Append M to the current section
                
                print(f"Section {section_num}: M is inherited from the previous section as {M}")
            else:
                print(f"Section {section_num}: M is not available")
                pass
            
        # Pressure
        Pt0 = sections[i - 1]['Pt']
        Pt1 = Pt0 * nss('M', M0)['Pt2_Pt1']
        P1 = Pt1 / test(M0, 1.4)
                
        # Temperature
        Tt0 = sections[i - 1]['Tt']
        Tt1 = Tt0 # Iseentropic flow, Tt remains constant
        
        # Append Pt and Tt to the current section
        section['P'] = P1
        section['Pt'] = Pt1
        section['Tt'] = Tt1
        
        # print(f"\n\nPt: {units(Pt, 'Pa', 'atm')} [atm], Tt: {Tt}\n\n")


    
    # Fanno Flow ----------------------------------------------------------------------------------
    elif flow_type == 'Fanno':
        print(f"Section {section_num}: Fanno flow calculations can be performed here")
    
    # Rayleigh Flow --------------------------------------------------------------------------------
    elif flow_type == 'Rayleigh':
        print(f"Section {section_num}: Rayleigh flow calculations can be performed here")
    
    else:
        raise ValueError(f"Section {section_num}: Invalid flow type")
    
# data = {
#     'Sections': [
#         {'Section Num': 0, 'Flow Type': 'Isentropic', 'M': 1.8, 'P': 30397.5, 'T': 250, 'Pt': 174657.8432082955, 'Tt': 411.99999999999994}, 
#         {'Section Num': 1, 'Flow Type': 'Normal', 'M': 1.8, 'Pt': 141941.59964822943, 'Tt': 334.82572543465926}]
# }

data = {
    'Sections': [
        {'Section Num': 0, 'Flow Type': 'Isentropic', 'M': 1.8, 'P': 30397.5, 'T': 250, 'Pt': 174657.8432082955, 'Tt': 411.99999999999994, 'A/A*': 3}
    ]
}
    
fprint(data)

