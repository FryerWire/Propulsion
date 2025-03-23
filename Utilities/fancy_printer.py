"""
Fancy Printer
Start Date        : 3/16/2025
Modification Date : 3/16/2025
"""



# Section Printing Function =======================================================================
def section_printer(data):
    """
    Prints section data in a formatted style with   delimiters, excluding None or empty values.
    
    Example:
    >>> data = {
    >>>     'Sections': [
    >>>         {'Section Num': 1, 'Flow Type': 'Isentropic', 'V1': 240, 'P1': 170000, 'T1': 320, 'M1': 0.67, 'Tt1': 349, 'Pt1': 230000},
    >>>         {'Section Num': 2, 'Flow Type': 'Isentropic', 'V2': 290, 'P2': 170000, 'Tt2': 349, 'T2': 307, 'Pt2': 211000}
    >>>     ]
    >>> }
    """
    
    def print_if_value(key, value, indent=0):
        """
        Prints only if the value is not None, empty string, or empty dictionary.
        
        Parameters:
        - key (str)   : The key to print
        - value       : The value to check and print
        - indent (int): Number of  s for indentation
        
        Returns:
        - Print Statements
        """
        if value is not None and value != "" and (not isinstance(value, dict) or value):
            print(" " * indent + f"{key}: {value}")
    
    def has_content(d):
        """
        Checks if a dictionary or value has meaningful content.
        
        Parameters:
        - d : The value to check
        
        Returns:
        - bool : True if content exists, False otherwise
        """
        if not isinstance(d, dict):
            return bool(d is not None and d != "")
        return any(has_content(v) for v in d.values())
    
    # Extract sections from the dictionary
    sections = data.get('Sections', [])
    
    # Check for nested 'Sections' in Misc
    for section in sections:
        if 'Misc' in section and 'Sections' in section['Misc']:
            sections = section['Misc']['Sections']
            break
    
    for section in sections:
        # Start with  
        print(" ")
        
        # Section Num
        section_num = section.get("Section Num")
        print_if_value("Section Num", section_num)
        
        # Flow Type
        print_if_value("Flow Type", section.get("Flow Type"), 4)
        
        # Machs (collect any key starting with 'M' and <= 3 chars)
        machs = {k: v for k, v in section.items() if k.startswith('M') and len(k) <= 3}
        if has_content(machs):
            print(" " * 4 + "Machs:")
            for key, value in machs.items():
                print_if_value(key, value, 8)
        
        # States (Temperature, Pressure, rho, Velocity)
        states = {
            "Temperature": {},
            "Pressure": {},
            "rho": {},
            "Velocity": {}
        }
        for key, value in section.items():
            if key.startswith('T') and not key.startswith('Tt'):
                states["Temperature"][key] = value  # Corrected key formatting
            elif key.startswith('Tt'):
                states["Temperature"][key] = value  # Corrected key formatting
            elif key.startswith('P') and not key.startswith('Pt'):
                states["Pressure"][key] = value  # Corrected key formatting
            elif key.startswith('Pt'):
                states["Pressure"][key] = value  # Corrected key formatting
            elif key.startswith('rho'):
                states["rho"][key] = value  # Corrected key formatting
            elif key.startswith('V'):
                states["Velocity"][key] = value  # Corrected key formatting

        # Correct indentation for States
        if any(has_content(states[cat]) for cat in states):
            print(" " * 4 + "States:")
            for category, values in states.items():
                if has_content(values):
                    print(" " * 8 + f"{category}:")
                    for key, value in values.items():
                        print_if_value(key, value, 12)

        # Section Ratios (e.g., A/A*)
        section_ratios = {
            "A/A*": section.get("A/A*")
        }
        if has_content(section_ratios):
            print(" " * 4 + "Section Ratios:")
            for key, value in section_ratios.items():
                print_if_value(key, value, 8)

        # Misc (anything not categorized above)
        categorized_keys = set().union(
            *[states[cat].keys() for cat in states],
            machs.keys(),
            section_ratios.keys(),
            {'Section Num', 'Flow Type'}
        )
        misc = {k: v for k, v in section.items() if k not in categorized_keys}
        if has_content(misc):
            print(" " * 4 + "Misc:")
            for key, value in misc.items():
                print_if_value(key, value, 8)
        
        # End with  
        print(" ")


# data = {
#     'Sections': [
#         {'Section Num': 1, 'Flow Type': 'Isentropic', 'V1': 240, 'P1': 170000, 'T1': 320, 'M1': 0.67, 'Tt1': 349, 'Pt1': 230000},
#         {'Section Num': 2, 'Flow Type': 'Isentropic', 'V2': 290, 'P2': 170000, 'Tt2': 349, 'T2': 307, 'Pt2': 211000}
#     ]
# }

# test = {'Section Num': 0, 'Flow Type': 'Isentropic', 'M': 1.8, 'P': 0.3, 'T': 250}
# # section_printer(test)

# data = {
#     'Sections': [{'Section Num': 0, 'Flow Type': 'Isentropic', 'M': 1.8, 'P': 30397.5, 'T': 250, 'Pt': 174657.8432082955, 'Tt': 411.99999999999994}, {'Section Num': 1, 'Flow Type': 'Normal', 'M': 1.8, 'Pt': 141941.59964822943, 'Tt': 334.82572543465926}]
# }

# [{'Section Num': 0, 'Flow Type': 'Isentropic', 'M': 1.8, 'P': 30397.5, 'T': 250, 'Pt': 174657.8432082955, 'Tt': 411.99999999999994}, {'Section Num': 1, 'Flow Type': 'Normal', 'M': 1.8, 'Pt': 141941.59964822943, 'Tt': 334.82572543465926}]
