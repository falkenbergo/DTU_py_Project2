# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 16:46:13 2023

@author: Marc(s195088)
"""

    
import numpy as np

from inputNumber import inputNumber

def displayMenu(options):
    
# =============================================================================
# Displays a menu of options, ask  user to choose from the list of options
# and returns the number of the options that was chosen.
# 
# Usage: 
#     choice = displayMenu(options)
# 
# Input:
#     options: Menu options (list with np.array)
# 
# Output:
#     choice: Chosen option (integer)
#
#
#  - Taken from class lecture
# =============================================================================

    for i in range(len(options)):
        print("{:d}.{:s}".format(i+1, options[i]))
        
    # Get a valid menu choice
    choice = 0
    while not(np.any(choice == np.arange(len(options))+1)):
        choice = inputNumber("Please choose an option from the menu: ", options)
        
    return choice
