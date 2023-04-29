# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 16:43:39 2023

@author: Falkenbergo
"""


def inputNumber(prompt):
# =============================================================================
#     INPUTNUMBER Prompts user to input a number
#     
#     Usage: num = inputNumber(prompt) Displays prompt and asks user
#     number. Repeats until user inputs a valid number.
#
#  - Taken from class lecture
# =============================================================================

    # While loop true until valid number input in try
    # If error then it will pass, and code will try again
    while True:
        try:
            num = float(input(prompt))
            break
        except ValueError:
            pass
    
    # Return float number in varible num
    return num