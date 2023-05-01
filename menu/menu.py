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

from rich import print as rprint
from rich.panel import Panel
# ============================================================================#
#                            IMPORTED FUNCTIONS                               #
# ============================================================================#

# Import load_measuremnts function
from load_measurements import load_measurements

# Function for loading the data. Showing a loading bar
from loadingBar import process_data

# Layout for dataLoaded and handling for corrupted data
from display_loaded_data_info import display_loaded_data_info

# Import displayMenu function
from displayMenu import displayMenu

# Import aggragate data function
from data_aggregation import aggregate_measurements


# Import statistics function
from data_statistics import print_statistics


#from dataStatistics import dataStatistics
#from dataPlot import dataPlot




def display_loaded_data_info(filename, corrupted_data_method):
    print()
    info_text = f"The file [bold cyan]{filename}[/bold cyan] has been loaded.\nCorrupted data has been handled using [bold cyan]{corrupted_data_method}[/bold cyan] method."
    panel = Panel(info_text, title="Data Loaded", expand=False, border_style="green")
    
    # Using rprint, to utilize another way of using color
    rprint(panel)




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
            # Implement aggregating data and error handling here
            aggregate = np.array(["hour", "day", 'month', 'hours of the day'])
            agg_choise = displayMenu(aggregate)
            if (agg_choise == 1):
                tvec_a, data_a = aggregate_measurements(tvec, data, 'Hour')
               
            elif (agg_choise == 2):
                tvec_a, data_a = aggregate_measurements(tvec, data, 'Day')
                
            elif (agg_choise == 3):
                tvec_a, data_a = aggregate_measurements(tvec, data, 'Month')
                
            elif (agg_choise == 4):
                tvec_a, data_a = aggregate_measurements(tvec, data, 'Hours of the day')
            
            aggregated = True
            print("Data aggregated successfully")
        else:
            print("Please load data first")


# ============================================#
#              Display statistics             #
# ============================================#
    elif choice == 3:
        if data_loaded and aggregated:
            # Implement displaying statistics here
            print("Displaying statistics")
        else:
            print("\033[38;2;255;100;100mERROR:\033[38;2;100;255;0m You must load and aggregate data first.\033[0m\n")

# ============================================#
#       Visualize electricity consumption     #
# ============================================#
    elif choice == 4:
        if data_loaded:
            # Create a pandas DataFrame with the data
            df = pd.DataFrame(data, columns=['Zone 1', 'Zone 2', 'Zone 3', 'Zone 4'])
    
            # Ask the user for the type of plot they want
            plot_type = input("Do you want to plot consumption in each zone or the combined consumption? (Enter 'zone' or 'combined'): ")
    
            if plot_type.lower() == 'zone':
                # Plot consumption for each zone
                if len(df) < 25:
                    df.plot(kind='bar', figsize=(10, 5))
                else:
                    df.plot(kind='line', figsize=(10, 5))
    
            elif plot_type.lower() == 'combined':
                # Plot combined consumption
                combined_df = df.sum(axis=1)
    
                if len(df) < 25:
                    combined_df.plot(kind='bar', figsize=(10, 5))
                else:
                    combined_df.plot(kind='line', figsize=(10, 5))
    
            else:
                print("Invalid input, please enter 'zone' or 'combined'.")
    
            # Set plot labels and title
            plt.xlabel('Time')
            plt.ylabel('Consumption')
            plt.title('Electricity Consumption')
            plt.show()
    
        else:
            print("\033[38;2;255;100;100mERROR:\033[38;2;100;255;0m You must load and aggregate data first.\033[0m\n")

# ============================================#
#                    Quit                     #
# ============================================#
    elif choice == 5:
        print("Exiting the program")
        break
    
    else:
        print("Invalid choice, please try again...")