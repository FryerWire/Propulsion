
"""
Variable Mapping Formatter
Start Date        : 3/5/2025
Modification Date : 3/14/2025
"""



# Variable Mapping ================================================================================
def variable_mapping(sections):
    """
    Variable Mapping takes sections input and remaps them to a structured dictionary.
    
    Parameters:
    - sections (list or dict) : Sections list or dictionary, can contain multiple sections
    
    Returns:
    - variable_map (dict) : Structured variable mapping dictionary
    
    Example:
    >>> sections = [
    >>>     {'Section Num': '01', 'Flow Type': 'Fanno', 'M1': 0.5, 'T': 300, 'F': 123},
    >>>     {'Section Num': '12', 'Flow Type': 'Isentropic', 'M2': 1.2}
    >>> ]
    """

    variable_map = {'Sections': []} # Initialize variable map

    # Default section template --------------------------------------------------------------------
    section_template = {
        'Section Num': None,
        'Flow Type': None,
        'Machs': {},

        'States': {
            'Temperature': {'T': {}, 'Tt': {}, 'T*': None, 'Tt*': None},
            'Pressure': {'P': {}, 'Pt': {}, 'P*': None, 'Pt*': None},
            'rho': {'rho': {}, 'rhot': {}, 'rho*': None, 'rhot*': None}
        },

        'Thermo Ratio': {
            'Temperature': {'T1/T0': {}, 'Tt1/Tt0': {}, 'T1/T*': {}, 'Tt1/Tt*': {}},
            'Pressure': {'P1/P0': {}, 'Pt1/Pt0': {}, 'P1/P*': {}, 'Pt1/Pt*': {}},
            'rho': {'rho1/rho0': {}, 'rhot1/rhot0': {}, 'rho1/rho*': {}, 'rhot1/rhot*': {}}
        },

        'Section Ratios': {'tau': {}, 'pi': {}},
        'Misc': {}
    }

    # Handle sections input -----------------------------------------------------------------------
    if (isinstance(sections, dict) and sections):                                    # Single section
        variable_map['Sections'].append(section_template.copy())
        section_list = [sections]                                                    # Wrap single dict in a list
    elif (isinstance(sections, list) and sections):                                  # Multiple sections
        variable_map['Sections'].extend([section_template.copy() for _ in sections])
        section_list = sections
    else:  # No sections provided
        variable_map['Sections'].append(section_template.copy())
        section_list = [{}]

    # Populate section data -----------------------------------------------------------------------
    for idx, section in enumerate(section_list):
        for key, value in section.items():
            if key in ['Section Num', 'Flow Type']:                 # Handle known section keys
                variable_map['Sections'][idx][key] = value
            elif key.startswith('M'):                               # Mach numbers
                variable_map['Sections'][idx]['Machs'][key] = value

            # States --------------------------------------------------------------------------
            elif key in variable_map['Sections'][idx]['States']['Temperature']:
                variable_map['Sections'][idx]['States']['Temperature'][key] = value

            elif key in variable_map['Sections'][idx]['States']['Pressure']:
                variable_map['Sections'][idx]['States']['Pressure'][key] = value

            elif key in variable_map['Sections'][idx]['States']['rho']:
                variable_map['Sections'][idx]['States']['rho'][key] = value

            # Thermo Ratios -------------------------------------------------------------------
            elif key in variable_map['Sections'][idx]['Thermo Ratio']['Temperature']:
                variable_map['Sections'][idx]['Thermo Ratio']['Temperature'][key] = value

            elif key in variable_map['Sections'][idx]['Thermo Ratio']['Pressure']:
                variable_map['Sections'][idx]['Thermo Ratio']['Pressure'][key] = value

            elif key in variable_map['Sections'][idx]['Thermo Ratio']['rho']:
                variable_map['Sections'][idx]['Thermo Ratio']['rho'][key] = value

            # Misc ----------------------------------------------------------------------------
            else:
                variable_map['Sections'][idx]['Misc'][key] = value

    return variable_map