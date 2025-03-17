
"""
Checking Printer
Start Date        : 3/16/2025
Modification Date : 3/16/2025
"""



# Local Imports ===================================================================================
# Problem Solvers ---------------------------------------------------------------------------------
from Problem_Solvers import edu_answers as ans


# External Imports ================================================================================
import numpy as np



# Answer Checking Function ========================================================================
def answer_checking(needs_checking, answer_call):
    """
    Compares the keys and values of two dictionaries.
    
    Parameters:
    - needs_checking (dict) : Dictionary of the unknown answered to be compared
    - answer_call (str)     : Inputs: L3, L4, Q1, TEST_1, and TEST_2
    
    Returns:
    - Print Statements : Prints the information regarding the comparison of the two dictionaries.
    
    Example:
    >>> answer_checking(needs_checking, 'L3')
    >>> answer_checking(needs_checking, 'L4')
    """
    
    if (answer_call == 'L3'):
        answers = ans.lecture(3)
    elif (answer_call == 'L4'):
        answers = ans.lecture(4)
    elif (answer_call == 'Q1'):
        answers = ans.quiz(1)
    elif (answer_call == 'TEST_1'):
        answers = ans.test(1)
    elif (answer_call == 'TEST_2'):
        answers = ans.test(2)
    else:
        print("Invalid answer call")
        return None
        
    for i, ans_dict in enumerate(answers.get('Sections', [])):
        if (i >= len(needs_checking.get('Sections', []))):
            print(f"\nSection {ans_dict.get('Section Num')} is missing in 'needs_checking' dict\n")
            continue
        
        needs_checking_dict = needs_checking['Sections'][i]
        for key, value in ans_dict.items():
            term_A = "Section: " + str(ans_dict.get('Section Num')) + " "
            term_B = key + " "
            if (key not in needs_checking_dict):
                term_C1 = "MISSING "
                term_D1 = "=" * (50 - len(term_A) - len(term_B) - len(term_C1))

                print(f"\n{term_A + term_B + term_C1 + term_D1}")
                print(f"    needs_checking: {needs_checking_dict.get(key)}")
                print(f"    answers_dict  : {ans_dict.get(key)}\n")

            elif (needs_checking_dict[key] != value):
                term_C2 = "MISMATCHING "
                term_D2 = "=" * (50 - len(term_A) - len(term_B) - len(term_C2))
                
                print(f"\n{term_A + term_B + term_C2 + term_D2}")
                print(f"    needs_checking: {needs_checking_dict.get(key)}")
                print(f"    answers_dict  : {ans_dict.get(key)}")
                print(f"    Percent Error : {round(np.abs((needs_checking_dict.get(key) - ans_dict.get(key)) / ans_dict.get(key)) * 100, 3)}%")
    print()
