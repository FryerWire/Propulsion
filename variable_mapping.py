"""
Variable Mapping Formatter
Start Date        : 3/5/2025
Modification Date : 3/5/2025
"""
def variable_mapping(r_and_s_known):
    ratios_and_sections = {
        "Machs": {"M0": 0, "M1": 0, "M2": 0, "M3": 0, "M4": 0, "M5": 0, "M6": 0, "M7": 0, "M8": 0, "M9": 0},
        "Fuel": {"mf_dot": 0, "m0_dot": 0},
        "Ratios": {
            "T": {"T0": 0, "T1": 0, "T2": 0, "T3": 0, "T4": 0, "T5": 0, "T6": 0, "T7": 0, "T8": 0, "T9": 0},
            "P": {"P0": 0, "P1": 0, "P2": 0, "P3": 0, "P4": 0, "P5": 0, "P6": 0, "P7": 0, "P8": 0, "P9": 0},
            "Tt": {"Tt0": 0, "Tt1": 0, "Tt2": 0, "Tt3": 0, "Tt4": 0, "Tt5": 0, "Tt6": 0, "Tt7": 0, "Tt8": 0, "Tt9": 0},
            "Pt": {"Pt0": 0, "Pt1": 0, "Pt2": 0, "Pt3": 0, "Pt4": 0, "Pt5": 0, "Pt6": 0, "Pt7": 0, "Pt8": 0, "Pt9": 0}
        },
        "Sections": {
            "tau": {"tau_r": 0, "tau_d": 0, "tau_c": 0, "tau_b": 0, "tau_lambda": 0, "tau_t": 0, "tau_n": 0},
            "pi": {"pi_r": 0, "pi_d": 0, "pi_c": 0, "pi_b": 0, "pi_lambda": 0, "pi_t": 0, "pi_n": 0}
        },
        "Misc": {"f": 0, "S": 0, "u9": 0, "n_th": 0, "n_p": 0, "a0": 0, "F_m0_dot": 0}
    }
    
    # Update with known values
    for key, value in r_and_s_known.items():
        found = False
        if key in ratios_and_sections["Machs"]:
            ratios_and_sections["Machs"][key] = value
            found = True
        for category, sub_dict in ratios_and_sections["Ratios"].items():
            if key in sub_dict:
                sub_dict[key] = value
                found = True
        for category, sub_dict in ratios_and_sections["Sections"].items():
            if key in sub_dict:
                sub_dict[key] = value
                found = True
        if key in ratios_and_sections["Fuel"]:
            ratios_and_sections["Fuel"][key] = value
            found = True
        if key in ratios_and_sections["Misc"]:
            ratios_and_sections["Misc"][key] = value
            found = True
        if not found:
            print(f"Warning: Key '{key}' not found in ratios_and_sections.")
    
    return ratios_and_sections