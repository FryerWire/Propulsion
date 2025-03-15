
"""
Unit Converter
Start Date        : 3/14/2025
Modification Date : 3/14/2025
"""



# Unit Converter ==================================================================================
def unit_conversion(value, from_unit, to_unit):
    """
    Converters to any unit. 
    
    Parameters:
    - value (float)   : Any float value
    - from_unit (str) : Any string in SI_prefix, imperial_units, temp_to_kelvin, and kelvin_to_temp
    - to_unit (str)   : Any string in SI_prefix, imperial_units, temp_to_kelvin, and kelvin_to_temp
    
    Returns:
    - converted_value (float) : The new unit converted value
    
    Example:
    >>> print(unit_conversion(19, 'C', 'R'))
    """
    
    # Metric --------------------------------------------------------------------------------------
    SI_prefix = {
        'T'  : 1e+12, # Tera
        'G'  : 1e+9,  # Giga
        'M'  : 1e+6,  # Mega
        'k'  : 1e+3,  # Kilo
        'h'  : 1e+2,  # Hecto
        'da' : 1e+1,  # Deca
        'BU' : 1,     # Base Unit
        'd'  : 1e-1,  # Deci
        'c'  : 1e-2,  # Centi
        'm'  : 1e-3,  # Milli
        'u'  : 1e-6,  # Micro
        'n'  : 1e-9,  # Nano
        'p'  : 1e-12  # Pico
    }

    # Imperial Unit Values ------------------------------------------------------------------------
    imperial_units = {
        'inch'  : 0.0254,    # Inch
        'foot'  : 0.3048,    # Foot
        'yard'  : 0.9144,    # Yard
        'mile'  : 1609.34,   # Mile
        'ounce' : 0.0283495, # Ounce
        'pound' : 0.453592,  # Pound
    }

    # Temperature Conversion ----------------------------------------------------------------------
    temp_to_kelvin = {
        'C' : lambda t : t + 273.15,                  # Celsius
        'F' : lambda t : (t - 32) * (5 / 9) + 273.15, # Fahrenheit
        'R' : lambda t : t * (5 / 9),                 # Rankine
        'K' : lambda t : t                            # Kelvin
    }

    kelvin_to_temp = {
        'C' : lambda t : t - 273.15,                  # Celsius
        'F' : lambda t : (t - 273.15) * (9 / 5) + 32, # Fahrenheit
        'R' : lambda t : t * (9 / 5),                 # Rankine
        'K' : lambda t : t                            # Kelvin
    }
    
    
    # Temperature Checks --------------------------------------------------------------------------
    if (from_unit in temp_to_kelvin) and (to_unit in kelvin_to_temp):
        value_in_kelvin = temp_to_kelvin[from_unit](value)
        return kelvin_to_temp[to_unit](value_in_kelvin)

    # 'to' and 'from' Unit Checks -----------------------------------------------------------------
    if (from_unit in SI_prefix):
        from_factor = SI_prefix[from_unit]
    elif (from_unit in imperial_units):
        from_factor = imperial_units[from_unit]
    else:
        raise TypeError("Invalid 'from' Unit")

    if (to_unit in SI_prefix):
        to_factor = SI_prefix[to_unit]
    elif (to_unit in imperial_units):
        to_factor = imperial_units[to_unit]
    else:
        raise TypeError("Invalid 'from' Unit")

    value_in_base_unit = value * from_factor
    converted_value = value_in_base_unit / to_factor

    return converted_value
