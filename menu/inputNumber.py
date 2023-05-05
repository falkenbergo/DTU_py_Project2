# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 16:43:39 2023

@author: Marc(s195088)
"""

"""
Edited on April 29th 19:30
Added error handling, if wrong number or letter is prompted
"""

# =============================================================================
# Prompts the user to input a number based on the given prompt and menuItems.
# 
# Usage: 
#     num = inputNumber(prompt, menuItems)
# 
# Parameters:
#     prompt: A string to display as a prompt for user input
#     menuItems: A list or numpy array of menu items
# 
# Returns:
#     value: An integer value representing the user's choice within the range 
#     of menuItems
# 
# Error Handling:
#     If invalid number of menuItems is inputtet, error message will display.
#     Same goes if the value inputtet is not an integer.
#
# - Taken from class lecture
# -   modded: Added error handling, if wrong number or letter is prompted
# 
# =============================================================================


def inputNumber(prompt, menuItems):
    while True:
        try:
            value = int(input(prompt))
            if 1 <= value <= len(menuItems):
                return value
            else:
                print(f"\n\033[38;2;255;100;100mInvalid choice:\033[38;2;100;255;0m Please enter a number between 1-{len(menuItems)}\033[0m")
                
        except ValueError:
            print("\n\033[38;2;255;100;100mInvalid number:\033[38;2;100;255;0m Please enter a number\033[0m")


