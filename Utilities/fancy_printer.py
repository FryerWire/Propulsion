
"""
Fancy Printer
Start Date        : 3/14/2025
Modification Date : 3/14/2025
"""



# Helper Function =================================================================================
def has_valid_content(dictionary):
    """
    Recursively check if a dictionary has any non-None, non-empty values.
    
    Parameters:
    - dictionary (dict): Any dictionary
    
    Returns
    - Boolean (bool) : True if not empty
    """
    
    if not isinstance(dictionary, dict):
        return True
    
    for value in dictionary.values():
        if value is None:
            continue
        if isinstance(value, dict):
            if value and has_valid_content(value):
                return True
        elif isinstance(value, (list, set)):
            if value:
                return True
        else:
            return True
        
    return False



# Fancy Printing ==================================================================================
def fancy_printing(inputted_dict, indent_level = 0, is_top_level = False):
    """
    Fancy printing of any inputted dictionary with aligned colons and spaces between sections.
    Only prints sections with non-empty, non-None values.
    
    Parameters:
    - inputted_dict (dict) : Any dictionary
    - indent_value (int)   : Recursive indentation
    - is_top_level (bool)  : Flag to indicate top-level call for initial spacing
    
    Returns:
    - Prints
    """
    
    tab = "\t"
    
    if (is_top_level and (indent_level == 0)):
        print()
    
    valid_items = [(k, v) for k, v in inputted_dict.items() if has_valid_content(v)]
    for i, (key, value) in enumerate(valid_items):
        base_indent = tab * indent_level
        
        if isinstance(value, dict):
            print(f"{base_indent}{key}:")
            fancy_printing(value, indent_level + 1)
                
        elif isinstance(value, (list, set)):
            print(f"{base_indent}{key}:")
            for item in value:
                print(f"{base_indent}{tab}{item}")
                    
        else:
            print(f"{base_indent}{key} : {str(value)}")
        
        if ((indent_level == 0) and (i < len(valid_items) - 1)):
            print()

    if ((indent_level == 0) and valid_items):
        print()
