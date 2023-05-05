

# -*- coding: utf-8 -*-
"""
Created on Thu April  27 07:56:26 2023

@author: Marc(S195088)
"""

#==============================================================================
#Function Description:
#The plotComparison function makes a graph to show how much electricity is used 
#in different areas during a certain time. It uses time values and electricity 
#and other options as input and shows a graph for the chosen areas.

#Usage:
#   plotComparison(tvec, data, plot, combine_zones, period)

#Input:

#   tvec: Time values for the data
#   data: Electricity consumption data for the zones
#   plot: Boolean values indicating which zones to include in the plot (list)
#   combine_zones: Boolean value indicating whether to combine the selected zones or not (bool)
#   period: Time period to format the time values (string)
#Output:
#Plot showing the electricity consumption data for the selected zones over the specified time period
#
#- Written by Marc(s195088)
#==============================================================================


# ============================================================================#
#                                LIBRARIES                                    #
# ============================================================================#
import matplotlib.pyplot as plt
import numpy as np

# Importing timeFormat function
from timeFormat import timeFormat

# ============================================================================#
#                              PLOT FUNCTION                                  #
# ============================================================================#

def plotComparison(tvec, data, plot, combine_zones, period):
    # Use the format_time function to format the time values based on the period
    formatted_tvec = np.array(timeFormat(tvec, period))


    # Define labels for zones
    labels = ["Zone 1", "Zone 2", "Zone 3", "Zone 4"]
    
    # Filter data based on selected zones
    filtered_data = data[:, np.array(plot, dtype=bool)]
    
    # Convert data to kW by dividing by 1000
    filtered_data_kw = filtered_data / 1000
    
    # Check if data contains less than 25 measurements
    use_bar_chart = len(formatted_tvec) < 25
    
    # Create figure and axis for plot
    fig, ax = plt.subplots()
    
    # Set title and labels for axes
    ax.set_title(f"Electricity Consumption - Year {round(tvec[0][0])}")
    ax.set_xlabel(f"Time ({period.capitalize()})")
    ax.set_ylabel(f"Consumption (kWh)")
    
    # Initialize the bottom array for stacking bars
    bottom = np.zeros(len(formatted_tvec))
    
    should_plot_combined = combine_zones and np.sum(plot) > 1
    
    #Initializing arrayt for the selected zones
    selected_zones = []
    
    # Loop through selected zones and plot data
    zone_index = 0
    
# =============================================================================
#This loop goes through"plot". "enumerate" gives index & value. 
#If "selected" is yes, it creates zone label & data, shows with bar/line chart. 
#It adds zone label to "selected_zones" & moves to next index.
# =============================================================================

    for i, selected in enumerate(plot):
        if selected:
            zone_label = labels[i]
            zone_data = filtered_data_kw[:, zone_index]
    
            if not should_plot_combined:
                
                if use_bar_chart:
                    # Use bar chart and stack bars on top of each other
                    ax.bar(formatted_tvec, zone_data, label=zone_label, bottom=bottom)
                    bottom += zone_data  # Update bottom array for stacking
                    print("use bar")
                
                else:
                    # Uses line chart
                    ax.plot(formatted_tvec, zone_data, label=zone_label)
    
            # Add the zone_label to selected_zones
            selected_zones.append(zone_label)
            
            
            # Move to next zone index
            zone_index += 1

    
    if should_plot_combined:
        
        # If using line chart and combine_zones is True then add line for combined data
        combined_data = np.sum(filtered_data_kw, axis=1)
        
        # Shows what zones are combined
        combined_label = f"Combined zones ({', '.join(selected_zones)})"
        
        # Plotting combined data
        ax.plot(formatted_tvec, combined_data, label=combined_label)
    
    # Legend to the plot
    ax.legend()
    
    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45)
    
    # Showing plot
    plt.show()






