
"""
Fancy Printer
Start Date        : 3/14/2025
Modification Date : 3/14/2025
"""



# Fancy Printing ==================================================================================
def fancy_printing(inputted_dict, indent_value = 0, is_top_level = True):
    """
    Fancy printing of any inputted dictionary with aligned colons.
    
    Parameters:
    - inputted_dict (dict) : Any dictionary
    - indent_value (int)   : Recursive indentation
    
    Returns:
    - Print statements
    """

    spacing = ' ' * indent_value
    first_key = True                  # Track first key to avoid extra blank line at the start
    keys = list(inputted_dict.keys()) # Get list of keys to track the last one
    if is_top_level and keys:
        print()

    max_key_length = max((len(key) for key in inputted_dict.keys()), default = 0) if not is_top_level else 0
    for i, (key, value) in enumerate(inputted_dict.items()):
        if is_top_level and not first_key:
            print() # Add a blank line between top-level keys
        first_key = False

        padded_key = key.ljust(max_key_length) if not is_top_level else key
        if is_top_level:
            print(f"{spacing}{padded_key}:", end = "")
        else:
            print(f"{spacing}{padded_key} :", end = "")

        if isinstance(value, dict):
            print() 
            fancy_printing(value, indent_value + 4, is_top_level = False)
        else:
            print(f" {value}")

        if (is_top_level and (i == len(keys) - 1)):
            print()
            