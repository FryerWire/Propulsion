
"""
Class Answers
Start Date        : 3/16/2025
Modification Date : 3/16/2025
"""



# Local Imports ===================================================================================
# Utilities ---------------------------------------------------------------------------------------
from Utilities.unit_converter import unit_conversion as units



# Lecture Solutions ===============================================================================
def lecture(lecture_num):
    """
    The lecture function takes in a lecture number interger and returns the lecture answer data.
    
    Parameters:
    - lecture_num (int): The lecture number integer.
                        Inputs: 3, 4
    
    Returns:
    - lecture_list (dict): The lecture answer data.
    
    Example:
    >>> lecture(3) -> L3_SOL
    >>> lecture(4) -> L4_SOL
    """
    
    lecture_list = [
        { # Lecture 3
            'Sections' : [
                {'Section Num': 1, 'Flow Type': 'Isentropic', 'V1': 240, 'P1': 170000, 'T1': 320, 'M1': 0.67, 'Tt1': 349, 'Pt1': 230000},
                {'Section Num': 2, 'Flow Type': 'Isentropic', 'V2': 290, 'P2': 170000, 'Tt2': 349, 'T2': 307, 'Pt2': 211000}
            ]
        },
        
        { # Lecture 4
            'Sections' : [
                {'Section Num': 0, 'Flow Type': 'Isentropic', 'M0': 1.8, 'P0': units(0.3, 'atm', 'Pa'), 'T0': 250, 'Pt0': units(1.724, 'atm', 'Pa'), 'Tt0': 412},
                {'Section Num': 1, 'Flow Type': 'Normal', 'M1': 0.6165, 'Pt1': units(1.4, 'atm', 'Pa')},
                {'Section Num': 2, 'Flow Type': 'Isentropic', 'Pt2': units(1.4, 'atm', 'Pa'), 'Tt2': 412, 'M2': 0.168, 'P2': units(1.373, 'atm', 'Pa'), 'T2': 410}
            ]
        }
    ]

    if (lecture_num == 3):
        return lecture_list[0]
    elif (lecture_num == 4):
        return lecture_list[1]
    else:
        return None
    


# Quiz Solutions ==================================================================================
def quiz(quiz_num):
    """
    The quiz function takes in a quiz number interger and returns the quiz answer data.
    
    Parameters:
    - quiz_num (int): The quiz number integer.
                        Inputs: 1

    Returns:
    - quiz_list (dict): The quiz answer data.
    
    Example:
    >>> quiz(1) -> Q1_SOL
    """
    
    quiz_list = [
        { # Quiz 1
            'Sections' : [
                {'Section Num': 1, 'Flow Type': 'Isentropic', 'T1': 288, 'P1': 100000, 'M1': 0.3, 'Tt1': 273.5},
                {'Section Num': 2, 'Flow Type': 'Isentropic', 'M2': 0.6, 'Tt2': 273.5, 'P2': 48700}
            ]
        }
    ]

    if (quiz_num == 1):
        return quiz_list[0]
    else:    
        return None



# Testing Solutions ===============================================================================
def testing(testing_num):
    """
    The testing function takes in a testing number interger and returns the testing answer data.
    
    Parameters:
    - testing_num (int): The testing number integer.
                        Inputs: 1, 2

    Returns:
    - testing_list (dict): The testing answer data.
    
    Example:
    >>> testing(1) -> TEST1_SOL
    """
    
    testing_list = [
        { # Quiz 1
            'Sections' : [
                {'Section Num': 1, 'Flow Type': 'Isentropic', 'V1': 240, 'P1': 170000, 'T1': 320, 'M1': 0.67, 'Tt1': 349, 'Pt1': 230000},
                {'Section Num': 2, 'Flow Type': 'Isentropic', 'V2': 290, 'P2': 170000, 'Tt2': 349, 'T2': 307, 'Pt2': 211000}
            ]
        },
        
        { # Quiz 2
            'Sections' : [
                {'Section Num': 1, 'Flow Type': 'Isentropic', 'V1': 480, 'P1': 170000, 'T1': 320, 'M1': 0.67, 'Tt1': 349, 'Pt1': 738},
                {'Section Num': 2, 'Flow Type': 'Isentropic', 'V2': 290, 'P2': 180, 'Tt2': 349, 'T2': 307, 'Pt2': 211000, 'Z': 10}
            ]
        }
    ]

    if (testing_num == 1):
        return testing_list[0]
    elif (testing_num == 2):
        return testing_list[1]
    else:    
        return None
