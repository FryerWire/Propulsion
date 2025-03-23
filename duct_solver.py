"""
Main Program
Start Date        : 3/4/2025
Modification Date : 3/14/2025
"""



# Local Imports ===================================================================================
# Utilities ---------------------------------------------------------------------------------------
from Utilities.unit_converter import unit_conversion as units
from Utilities.fancy_printer import section_printer as fprint

# Flow Solvers ------------------------------------------------------------------------------------
from Flow_Solvers.isentropic_flow import iscentropic_flow_solver as ifs
from Flow_Solvers.normal_shocks import normal_shock_solver as nss



# Isentropic Duct Solver ==========================================================================
def isentropic_duct():
    return



# Given Data =======================================================================================
# sections = [
#     {'Section Num': 0, 'Flow Type': 'Isentropic', 'M': 1.8, 'P': units(0.3, 'atm', 'Pa'), 'T': 250},
#     {'Section Num': 1, 'Flow Type': 'Normal'},
#     {'Section Num': 2, 'Flow Type': 'Isentropic'}
# ]


sections = [
    {'Section Num': 0, 'Flow Type': 'Isentropic', 'M': 1.8, 'P': units(0.3, 'atm', 'Pa'), 'T': 250},
    {'Section Num': 1, 'Flow Type': 'Normal'}
]





for i, section in enumerate(sections):
    print("=========================================================================================")
    section_num = section.get('Section Num')
    flow_type = section.get('Flow Type')
    M = section.get('M') 
    P = section.get('P')
    T = section.get('T')
    
    # print(f"\n\n{sections}\n\n")
    # fprint(section)
    # print(section)
    
    fprint({'Sections': [section]})
    
    # Isentropic ----------------------------------------------------------------------------------
    if (flow_type == 'Isentropic'):
        if (M is not None):
            # print(f"Section {section_num}: M is explicitly defined as {M}")
            pass
        else:
            if ((i > 0) and (sections[i - 1].get('M') is not None)):
                M = sections[i - 1]['M']
                # print(f"Section {section_num}: M is inherited from the previous section as {M}")
            else:
                # print(f"Section {section_num}: M is not available")
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
            if ((i > 0) and (sections[i - 1].get('M') is not None)):
                M = sections[i - 1]['M']
                section['M'] = M  # Append M to the current section
                # print(f"Section {section_num}: M is inherited from the previous section as {M}")
            else:
                # print(f"Section {section_num}: M is not available")
                pass
                
        Pt0 = sections[i - 1]['Pt']
        Tt0 = sections[i - 1]['Tt']
        
        Pt1 = Pt0 * nss('M', M)['Pt2_Pt1']
        Tt1 = Tt0 * nss('M', M)['Pt2_Pt1']
                
        
        # Append Pt and Tt to the current section
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
    
data = {
    'Sections': [{'Section Num': 0, 'Flow Type': 'Isentropic', 'M': 1.8, 'P': 30397.5, 'T': 250, 'Pt': 174657.8432082955, 'Tt': 411.99999999999994}, {'Section Num': 1, 'Flow Type': 'Normal', 'M': 1.8, 'Pt': 141941.59964822943, 'Tt': 334.82572543465926}]
}
    
fprint(data)

