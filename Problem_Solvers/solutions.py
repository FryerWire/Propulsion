
"""
Problem Solutions
Start Date        : 3/16/2025
Modification Date : 3/16/2025
"""



# Local Imports ===================================================================================
# Utilities ---------------------------------------------------------------------------------------
from Utilities.unit_converter import unit_conversion as units


# External Imports ================================================================================
import numpy as np 



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
                print(f"\nSection {ans_dict.get('Section Num')}: MISSING =============================")
                print(f"    needs_checking: {key}: {needs_checking_dict.get(key)}")
                print(f"    answers_dict  : {key}: {ans_dict.get(key)}\n")

            elif (needs_checking_dict[key] != value):
                print(f"\nSection {ans_dict.get('Section Num')}: MISMATCHING =========================")
                print(f"    needs_checking: {key}: {needs_checking_dict.get(key)}")
                print(f"    answers_dict  : {key}: {ans_dict.get(key)}")
                print(f"    Percent Error : {len(key) * ' '}: {round(np.abs((needs_checking_dict.get(key) - ans_dict.get(key)) / ans_dict.get(key)) * 100, 3)}%")
