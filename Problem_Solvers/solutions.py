
"""
Problem Solutions
Start Date        : 3/16/2025
Modification Date : 3/16/2025
"""



# Local Imports ===================================================================================
# Utilities ---------------------------------------------------------------------------------------
from Utilities.unit_converter import unit_conversion as units



# Lecture Solutions ===============================================================================
L3_SOL = {
    'Sections' : [
        {'Section Num': 1, 'Flow Type': 'Isentropic', 'V1': 240, 'P1': 170000, 'T1': 320, 'M1': 0.67, 'Tt1': 349, 'Pt1': 230000},
        {'Section Num': 2, 'Flow Type': 'Isentropic', 'V2': 290, 'P2': 170000, 'Tt2': 349, 'T2': 307, 'Pt2': 211000}
    ]
}

L4_SOL = {
    'Sections' : [
        {'Section Num': 0, 'Flow Type': 'Isentropic', 'M0': 1.8, 'P0': units(0.3, 'atm', 'Pa'), 'T0': 250, 'Pt0': units(1.724, 'atm', 'Pa'), 'Tt0': 412},
        {'Section Num': 1, 'Flow Type': 'Normal', 'M1': 0.6165, 'Pt1': units(1.4, 'atm', 'Pa')},
        {'Section Num': 2, 'Flow Type': 'Isentropic', 'Pt2': units(1.4, 'atm', 'Pa'), 'Tt2': 412, 'M2': 0.168, 'P2': units(1.373, 'atm', 'Pa'), 'T2': 410}
    ]
}



# Quiz Solutions ==================================================================================
Q1_SOL = {
    'Sections' : [
        {'Section Num': 1, 'Flow Type': 'Isentropic', 'T1': 288, 'P1': 100000, 'M1': 0.3, 'Tt1': 273.5},
        {'Section Num': 2, 'Flow Type': 'Isentropic', 'M2': 0.6, 'Tt2': 273.5, 'P2': 48700}
    ]
}



# Testing Solutions ===============================================================================
TEST_1 = {
    'Sections' : [
        {'Section Num': 1, 'Flow Type': 'Isentropic', 'V1': 240, 'P1': 170000, 'T1': 320, 'M1': 0.67, 'Tt1': 349, 'Pt1': 230000},
        {'Section Num': 2, 'Flow Type': 'Isentropic', 'V2': 290, 'P2': 170000, 'Tt2': 349, 'T2': 307, 'Pt2': 211000}
    ]
}

TEST_2 = {
    'Sections' : [
        {'Section Num': 1, 'Flow Type': 'Isentropic', 'V1': 480, 'P1': 170000, 'T1': 320, 'M1': 0.67, 'Tt1': 349, 'Pt1': 738},
        {'Section Num': 2, 'Flow Type': 'Isentropic', 'V2': 290, 'P2': 180, 'Tt2': 349, 'T2': 307, 'Pt2': 211000, 'Z': 10}
    ]
}



# Answer Checking Function ========================================================================
def answer_checking(needs_checking, answers):
    """
    Compares the keys and values of two dictionaries.
    
    Parameters:
    - needs_checking (dict) : Dictionary of the unknown answered to be compared
    - answers (dict)        : Dictionary of the true answers to be compared
                            : L3_SOL, L4_SOL, Q1_SOL, TEST_1, and TEST_2
    
    Returns:
    - Print Statements : Prints the information regarding the comparison of the two dictionaries.
    
    Example:
    >>> dict_A = {
    >>>     'Sections' : [
    >>>         {'Section Num': 1, 'Flow Type': 'Isentropic', 'V1': 240, 'P1': 170000, 'T1': 320, 'M1': 0.67, 'Tt1': 349, 'Pt1': 230000},
    >>>         {'Section Num': 2, 'Flow Type': 'Isentropic', 'V2': 290, 'P2': 170000, 'Tt2': 349, 'T2': 307, 'Pt2': 211000}
    >>>     ]
    >>> }

    >>> dict_B = {
    >>>     'Sections' : [
    >>>         {'Section Num': 1, 'Flow Type': 'Isentropic', 'V1': 480, 'P1': 170000, 'T1': 320, 'M1': 0.67, 'Tt1': 349, 'Pt1': 738},
    >>>         {'Section Num': 2, 'Flow Type': 'Isentropic', 'V2': 290, 'P2': 180, 'Tt2': 349, 'T2': 307, 'Pt2': 211000}
    >>>     ]
    >>> }
    """
    
    for i, ans_dict in enumerate(answers.get('Sections', [])):
        if (i >= len(needs_checking.get('Sections', []))):
            print(f"\nSection {ans_dict.get('Section Num')} is missing in 'needs_checking' dict\n")
            continue
        
        needs_checking_dict = needs_checking['Sections'][i]
        for key, value in ans_dict.items():
            if (key not in needs_checking_dict):
                print("\nMissing Keys with 'answers_dict' with 'needs_checking_dict'!")
                print(f"- {key} from Section {ans_dict.get('Section Num')} is missing!\n")  
                          
            elif (needs_checking_dict[key] != value):
                print("\nMismatching Values of 'answers_dict' with 'needs_checking_dict'!")
                print(f"- {key} from Section {ans_dict.get('Section Num')} do NOT match\n")
