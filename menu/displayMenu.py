# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 16:46:13 2023

@author: Falkenbergo
"""

    
import numpy as np

from inputNumber import inputNumber

def displayMenu(options):
    
# =============================================================================
#     DISPLAYMENU Displays a menu of options, ask the user to choose
#     and returns the number of the menu item chosen.
#     
#     Usage: choice = displayMenu(options)
#     
#     Input options Menu options (cell array of strings)
#     Output choice Chosen option (integer)
#     
#     Display menu options
#
#  - Taken from class lecture
# =============================================================================

    for i in range(len(options)):
        print("{:d}.{:s}".format(i+1, options[i]))
        
    # Get a valid menu choice
    choice = 0
    while not(np.any(choice == np.arange(len(options))+1)):
        choice = inputNumber("Please choose a menu item: ")
        
    return choice
