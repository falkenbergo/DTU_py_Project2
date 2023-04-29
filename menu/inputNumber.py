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
    #     ErrorHandle: If invalid number of menuItems is inputtet, error message will display.
    #     Same goes if the value inputtet is not an integer.
    #
    #  - Taken from class lecture
    # =============================================================================

    # While loop true until valid number input in try
    # If error then it will pass, and code will try again
    while True:
        try:
            value = int(input(prompt))
            if 1 <= value <= len(menuItems):
                return value
            else:
                print(f"Invalid choice, please enter a number between 1 and {len(menuItems)}")
        except ValueError:
            print("Invalid input, please enter a number")
