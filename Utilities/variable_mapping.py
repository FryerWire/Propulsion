
"""
Variable Mapping Formatter
Start Date        : 3/5/2025
Modification Date : 3/14/2025
"""



# Variable Mapping ================================================================================
def variable_mapping(gas_constants, sections):
    """
    Variable Mapping takes in two inputs and remaps them to a global dictionary.
    
    Parameters:
    - gas_constants (dict) : Gas constant dictionary
    - sections (list or dict) : Sections list or dictionary, can contain multiple sections
    
    Returns:
    - variable_map (dict) : Global variable dictionary
    
    Examples:
    >>> gas_constants = {'gamma': 1.4, 'cp': 1004}
    >>> sections = [
    >>>     {'Section Num': '01', 'Flow Type': 'Fanno', 'M1': 0.5, 'T': 300, 'F': 123},
    >>>     {'Section Num': '12', 'Flow Type': 'Isentropic', 'M2': 1.2}
    >>> ]
    """
    
    
    variable_map = {
        'Gas Constants' : {'gamma': None, 'cp': None},
        'Sections'      : [] # Changed to a list to hold multiple sections
    }
    
    
    # Default section template --------------------------------------------------------------------
    section_template = {
        'Section Num' : None, 
        'Flow Type'   : None, 
        'Machs'       : {},
        
        'States' : {
            'Temperature' : {'T': {}, 'Tt': {}, 'T*': None, 'Tt*': None}, 
            'Pressure'    : {'P': {}, 'Pt': {}, 'P*': None, 'Pt*': None},
            'rho'         : {'rho': {}, 'rhot': {}, 'rho*': None, 'rhot*': None}
        },
        
        'Thermo Ratio' : {
            'Temperature' : {'T1/T0': {}, 'Tt1/Tt0': {}, 'T1/T*': {}, 'Tt1/Tt*': {}},
            'Pressure'    : {'P1/P0': {}, 'Pt1/Pt0': {}, 'P1/P*': {}, 'Pt1/Pt*': {}},
            'rho'         : {'rho1/rho0': {}, 'rhot1/rhot0': {}, 'rho1/rho*': {}, 'rhot1/rhot*': {}},
        },
        
        'Section Ratios' : {'tau': {}, 'pi': {}},
        'Misc'           : {}
    }
    
    
    # Handle sections input -----------------------------------------------------------------------
    if isinstance(sections, dict) and sections:                      # Single section as dict
        variable_map['Sections'].append(section_template.copy())
        section_idx = 0
    elif isinstance(sections, list) and sections:                    # Multiple sections as list
        for _ in sections:
            variable_map['Sections'].append(section_template.copy())
        section_idx = None                                           # Will determine section by 'Section Num' or index
    else:                                                            # No sections provided
        variable_map['Sections'].append(section_template.copy())
        section_idx = 0
    
    
    # 'var_map' Values being updated --------------------------------------------------------------
    variable_map_list = [gas_constants, sections]
    for i in range(len(variable_map_list)):
        current_input = variable_map_list[i]
        
        if isinstance(current_input, dict):
            for key, value in current_input.items():
                if (key in variable_map['Gas Constants']):
                    variable_map['Gas Constants'][key] = value
                    
                elif (isinstance(current_input, list)): # Handle list of sections
                    continue                            # Skip to list handling below
                
                elif (key in variable_map['Sections'][0]):
                    variable_map['Sections'][0][key] = value
                    
                elif (key.startswith('M')):
                    variable_map['Sections'][0]['Machs'][key] = value
                    
                    
                # States ------------------------------------------------------------------------------
                elif (key in variable_map['Sections'][0]['States']['Temperature']):
                    variable_map['Sections'][0]['States']['Temperature'][key] = value
                    
                elif (key in variable_map['Sections'][0]['States']['Pressure']):
                    variable_map['Sections'][0]['States']['Pressure'][key] = value
                    
                elif (key in variable_map['Sections'][0]['States']['rho']):
                    variable_map['Sections'][0]['States']['rho'][key] = value
                    
                    
                # Thermo Ratio ------------------------------------------------------------------------
                elif (key in variable_map['Sections'][0]['Thermo Ratio']['Temperature']):
                    variable_map['Sections'][0]['Thermo Ratio']['Temperature'][key] = value
                    
                elif (key in variable_map['Sections'][0]['Thermo Ratio']['Pressure']):
                    variable_map['Sections'][0]['Thermo Ratio']['Pressure'][key] = value
                    
                elif (key in variable_map['Sections'][0]['Thermo Ratio']['rho']):
                    variable_map['Sections'][0]['Thermo Ratio']['rho'][key] = value
                    
                    
                else: 
                    variable_map['Sections'][0]['Misc'][key] = value
        
        elif isinstance(current_input, list): # Handle multiple sections
            for idx, section in enumerate(current_input):
                for key, value in section.items():
                    if (key in variable_map['Sections'][idx]):
                        variable_map['Sections'][idx][key] = value
                        
                    elif (key.startswith('M')):
                        variable_map['Sections'][idx]['Machs'][key] = value
                        
                        
                    # States ----------------------------------------------------------------------
                    elif (key in variable_map['Sections'][idx]['States']['Temperature']):
                        variable_map['Sections'][idx]['States']['Temperature'][key] = value
                        
                    elif (key in variable_map['Sections'][idx]['States']['Pressure']):
                        variable_map['Sections'][idx]['States']['Pressure'][key] = value
                        
                    elif (key in variable_map['Sections'][idx]['States']['rho']):
                        variable_map['Sections'][idx]['States']['rho'][key] = value
                        
                        
                    # Thermo Ratio ----------------------------------------------------------------
                    elif (key in variable_map['Sections'][idx]['Thermo Ratio']['Temperature']):
                        variable_map['Sections'][idx]['Thermo Ratio']['Temperature'][key] = value
                        
                    elif (key in variable_map['Sections'][idx]['Thermo Ratio']['Pressure']):
                        variable_map['Sections'][idx]['Thermo Ratio']['Pressure'][key] = value
                        
                    elif (key in variable_map['Sections'][idx]['Thermo Ratio']['rho']):
                        variable_map['Sections'][idx]['Thermo Ratio']['rho'][key] = value
                        
                        
                    else: 
                        variable_map['Sections'][idx]['Misc'][key] = value
    
    return variable_map
