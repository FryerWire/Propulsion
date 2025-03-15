
"""
Variable Mapping Formatter
Start Date        : 3/5/2025
Modification Date : 3/14/2025
"""



# Variable Mapping ================================================================================
def variable_mapping(gas_constants, known_values, sections = {}):
    """
    Variable Mapping takes in three inputs and remaps them to a global dictionary.
    
    Parameters:
    - gas_constants (dict) : Gas constant dictionary
    - known_values (dict)  : Known values dictionary
    - sections (dict)      : Sections dictionary
    
    Returns:
    - variable_map (dict) : Globa variable dictionary
    
    Examples:
    >>> gas_parameters = {'R': 287, 'g': 1.4, 'cp': 1004}
    >>> sections = {'Isentropic': ['01', '12']}
    >>> knowns = {'F': 123456789, 'M2': 123456789}
    >>> print(map(gas_parameters, knowns))
    """
    
    variable_map = {
        'Gas Constants' : {'gamma': None, 'cp': None},
        'Sections'     : {'Fanno': None, 'Normal': None, 'Raleigh': None, 'Isentropic': None},
        'Machs'        : {},
        
        'States' : {
            'Temperature' : {'T': {}, 'Tt': {}, 'T*': None, 'Tt*': None}, 
            'Pressure'    : {'P': {}, 'Pt': {}, 'P*': None, 'Pt*': None},
            'rho'         : {'rho': {}, 'rhot': {}, 'rho*': None, 'rhot*': None}
        },
        
        'Thermo Ratio' : {
            'Temperature' : {'T1/T0': {}, 'Tt1/Tt0': {}, 'T1/T*': {}, 'Tt1/Tt*': {}},
            'Pressure'     : {'P1/P0': {}, 'Pt1/Pt0': {}, 'P1/P*': {}, 'Pt1/Pt*': {}},
            'rho'          : {'rho1/rho0': {}, 'rhot1/rhot0': {}, 'rho1/rho*': {}, 'rhot1/rhot*': {}},
        },
        
        'Section Ratios' : {'tau': {}, 'pi': {}},
        'Misc'           : {}
    }
    
    # 'var_map' Values being updated --------------------------------------------------------------
    variable_map_list = [gas_constants, sections, known_values]
    for i in range(len(variable_map_list)):
        for key, value in variable_map_list[i].items():
            if (key in variable_map['Gas Constants']):
                variable_map['Gas Constants'][key] = value
                
            elif (key in variable_map['Sections']):
                variable_map['Sections'][key] = value
                
            elif (key.startswith('M')):
                variable_map['Machs'][key] = value
                
            elif (key in variable_map['Sections']):
                variable_map['Sections'][key] = value
                

            # ADD: Need to add P1, Pt, P*, ...
            
            
            # States ------------------------------------------------------------------------------
            elif (key in variable_map['States']['Temperature']):
                variable_map['States']['Temperature'][key] = value
                
            elif (key in variable_map['States']['Pressure']):
                variable_map['States']['Pressure'][key] = value
                
            elif (key in variable_map['States']['rho']):
                variable_map['States']['rho'][key] = value
                
            # Thermo Ratio ------------------------------------------------------------------------
            elif (key in variable_map['Thermo Ratio']['Temperature']):
                variable_map['Thermo Ratio']['Temperature'][key] = value
                
            elif (key in variable_map['Thermo Ratio']['Pressure']):
                variable_map['Thermo Ratio']['Pressure'][key] = value
                
            elif (key in variable_map['Thermo Ratio']['rho']):
                variable_map['Thermo Ratio']['rho'][key] = value
                
            else: 
                variable_map['Misc'][key] = value
    
    return variable_map
    