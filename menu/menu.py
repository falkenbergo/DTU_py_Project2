# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 10:05:42 2023

@author: Marc
"""

# ============================================================================#
#                                LIBRARIES                                    #
# ============================================================================#

import numpy as np

# Help to register if filename is present in path
import os 

# ============================================================================#
#                            IMPORTED FUNCTIONS                               #
# ============================================================================#

# Import load_measuremnts function
from load_measurements import load_measurements

# Import displayMenu function
from displayMenu import displayMenu


#from dataStatistics import dataStatistics
#from dataPlot import dataPlot

# ============================================================================#
#                                   Menu                                      #
# ============================================================================#

menuItems = np.array(["Load data", "Aggregate data", "Display statistics", "Visualize electricity consumption", "Quit\n"])

data_loaded = False
aggregated = False

while True:
    choice = displayMenu(menuItems)

    if choice == 1:  # Load data
        while True:
            try:
                filename = input('\nPlease enter filename: ')
                if filename.endswith('.txt'):
                    if os.path.isfile(filename):
                        data = load_measurements(filename)
                        data_loaded = True
                        break
                    else:
                        raise FileNotFoundError(f"\n\033[38;2;255;100;100mERROR:\033[38;2;100;255;0mFilename:'{filename}'\033[0m does not exist in the directory. \nPlease try again")
                else:
                    raise ValueError(f"\n\033[38;2;255;100;100mERROR:\033[38;2;100;255;0mFilename:'{filename}'\033[0m Are missing the filetype .txt. \nPlease try again")
            except (ValueError, FileNotFoundError) as error_loadData:
                print(error_loadData)

    elif choice == 2:  # Aggregate data
        if data_loaded:
            # Implement aggregating data and error handling here
            aggregated = True
            print("Data aggregated successfully.")
        else:
            print("Please load data first.")

    elif choice == 3:  # Display statistics
        if data_loaded and aggregated:
            # Implement displaying statistics here
            print("Displaying statistics.")
        else:
            print("Please load and aggregate data first.")

    elif choice == 4:  # Visualize electricity consumption
        if data_loaded and aggregated:
            # Implement visualizing electricity consumption here
            print("Visualizing electricity consumption.")
        else:
            print("Please load and aggregate data first.")

    elif choice == 5:  # Quit
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please try again.")
