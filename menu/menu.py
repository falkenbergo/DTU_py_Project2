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

# Help to doing plots in "Visualize electricity consumption"
import matplotlib.pyplot as plt
import pandas as pd

# Loadingbar for "Load measurements"
from rich.progress import Progress
from rich.progress import track
from time import sleep

# Visual display of loaded data and corrupted choice
from rich import print as rprint #Needed to ad rprint to handle both printf and rich
from rich.panel import Panel

########### Visual plotting menu 4##########
from rich import box
from rich.console import Console
from rich.table import Table
from rich.text import Text

console = Console()

###########################################


# ============================================================================#
#                            IMPORTED FUNCTIONS                               #
# ============================================================================#

# Import load_measuremnts function
from load_measurements import load_measurements

# Function for loading the data. Showing a loading bar
from loadingBar import process_data

# Layout for dataLoaded and handling for corrupted data
from display_loaded_data_info import display_loaded_data_info

# Import displayMenu function and inputNumber
from displayMenu import displayMenu
from inputNumber import inputNumber

# Import aggragate data function
from data_aggregation import aggregate_measurements


# Import statistics function
from data_statistics import print_statistics


#from dataStatistics import dataStatistics

#Importing plot function
from plotComparison import plotComparison



# ============================================================================#
#                                   Menu                                      #
# ============================================================================#

menuItems = np.array(["Load data", "Aggregate data", "Display statistics", "Visualize electricity consumption", "Quit\n"])
menuDataload = np.array(["Forward fill", "Backward fill", 'Drop'])

data_loaded = False
aggregated = False

while True:
    if data_loaded:
        display_loaded_data_info(filename, corruptedData)
    choice = displayMenu(menuItems)

# =======================================#
#  Enter filename - "Load measurements"  #
# =======================================#

    if choice == 1:
        while True:
            try:
                filename = input('\nPlease enter filename: ')
                if filename.endswith('.txt') or filename.endswith('.csv'):
    
                    # Checking if file is in the working directori
                    if os.path.isfile(filename):
    
                        # =======================================#
                        #  Choose what to do with corrupted data #
                        # =======================================#
    
                        corruptedMenuItems = np.array(["Forward fill", "Backward fill", "Drop corrupted data", "Cancel"])
    
                        while True:
                            print(f"\n\033[38;2;10;150;180mPlease choose how to handle corrupted data:\033[0m")
    
                            corruptedChoice = displayMenu(corruptedMenuItems)
    
                            if corruptedChoice == 1:
                                tvec, data = load_measurements(filename, "forward fill")
                                corruptedData = "forward fill"
                                data_loaded = True
                                break
                            elif corruptedChoice == 2:
                                tvec, data = load_measurements(filename, "backward fill")
                                corruptedData = "backward fill"
                                data_loaded = True
                                break
                            elif corruptedChoice == 3:
                                tvec, data = load_measurements(filename, "drop")
                                corruptedData = "drop"
                                data_loaded = True
                                break
                            elif corruptedChoice == 4:
                                break
                            else:
                                print("Invalid choice, please try again...")


                        break
    
                    else:
                        raise FileNotFoundError(f"\n\033[38;2;255;100;100mERROR:\033[38;2;100;255;0mFilename:'{filename}'\033[0m does not exist in the path. \nPlease try again")
    
                else:
                    raise ValueError(f"\n\033[38;2;255;100;100mERROR:\033[38;2;100;255;0mFilename:'{filename}'\033[0m are missing the filetype .txt or .csv \nPlease try again")
    
            # Prints out if one af the error occurs in loading data
            except (ValueError, FileNotFoundError) as error_loadData:
                print(error_loadData)


  
# ============================================#
#                Aggregate data               #
# ============================================#

    elif choice == 2:
        if data_loaded:
            
            while True:
                # Implement aggregating data and error handling here
                aggregate = np.array([" Consumption per min (no aggregation)"," Consumption per hour", " Consumption per day", " Consumption per month", " Hour-of-day consumption (hourly avg)"," Back"])
                agg_choice = displayMenu(aggregate)

                if (agg_choice == 1):
                    tvec_a, data_a = tvec, data
                    period = 'sec'
                    break

                elif (agg_choice == 2):
                    tvec_a, data_a = aggregate_measurements(tvec, data, 'hour')
                    period = 'hour'
                    break
                   
                elif (agg_choice == 3):
                    tvec_a, data_a = aggregate_measurements(tvec, data, 'day')
                    period = 'day'
                    break
                    
                elif (agg_choice == 4):
                    tvec_a, data_a = aggregate_measurements(tvec, data, 'month')
                    period = 'month'
                    break
                    
                elif (agg_choice == 5):
                    tvec_a, data_a = aggregate_measurements(tvec, data, "hour of the day")
                    period = 'hour of the day'
                    break
                    
                elif (agg_choice == 6):
                    break
                
                else:
                    print("Invalid choice, please try again...")
                    
            
            aggregated = True
            print("Data aggregated successfully")
        else:
            print("Please load data first")



# ============================================#
#              Display statistics             #
# ============================================#
    elif choice == 3:
        if data_loaded & aggregated:
            print("Displaying statistics")
            print_statistics(tvec_a, data_a, period)
        else:
            print("\033[38;2;255;100;100mERROR:\033[38;2;100;255;0m You must load and aggregate data first.\033[0m\n")


# ============================================#
#       Visualize electricity consumption     #
# ============================================#


    elif choice == 4:
        if data_loaded and aggregated:
    
            # Defining boolean plot variables for the zones
            plot = [False, False, False, False]
    
            # Initialize combine_zones variable
            combine_zones = False
    
            while True:
                # Create a table for the plot options menu
                menu_table = Table(title="\n[bold green]Choose what zones to visualize[bold green]", box=box.SQUARE)
    
                # Add columns to the table with specified styles
                menu_table.add_column("Options", justify="right", style="cyan", no_wrap=True)
                menu_table.add_column("Description", style="cyan")
                menu_table.add_column("Status")
    
                # Define the plot options for box
                menuPlot = [
                    "Zone 1",
                    "Zone 2",
                    "Zone 3",
                    "Zone 4",
                    "Combine chosen zones",
                    "Plot the chosen zones",
                    "Back"
                ]
    
                for idx, item in enumerate(menuPlot):
                    if idx < 4:  # Change this condition to match the number of individual zones
                        status = "✅" if plot[idx] else "❌"
                    elif idx == 4:
                        status = "✅" if combine_zones else "❌"
                    else:
                        status = ""
                    menu_table.add_row(str(idx + 1), item, status)
    
                # Print the table to the console
                console.print(menu_table)
    
                # Prompt the user to enter their choice using the inputNumber function
                plotChoice = inputNumber("Enter your choice: ", menuPlot)
    
                # Number of individual zones is 4, then 1,4
                if plotChoice in np.arange(1, 5):  
                    plot[int(plotChoice) - 1] = not plot[int(plotChoice) - 1]
    
                # Handle the "Combine chosen zones" option (option 5) separately
                elif plotChoice == 5:
                    combine_zones = not combine_zones
    
                # Plot the graphs based on the selected zones
                # Update the plotComparison function call to pass the correct period
                elif plotChoice == 6:
                    plotComparison(tvec_a, data_a, plot, combine_zones, period)
    
                # Return to the main menu
                elif plotChoice == 7:
                    break
                else:
                    print("Invalid choice, please try again...")
    
        else:
            print("\033[38;2;255;100;100mERROR:\033[38;2;100;255;0m You must load and aggregate data first.\033[0m\n")

# ============================================#
#                    Quit                     #
# ============================================#
    elif choice == 5:
        print("\nExiting the program")
        break
    
    else:
        print("Invalid choice, please try again...")