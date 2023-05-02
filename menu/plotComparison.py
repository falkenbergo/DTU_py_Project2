# -*- coding: utf-8 -*-
"""
Created on Mon May  1 17:56:26 2023

@author: Marc
"""
import matplotlib.pyplot as plt
import numpy as np

# Importing timeFormat function
from timeFormat import timeFormat


def plotComparison(tvec, data, plot, combine_zones, period):
    # Use the format_time function to format the time values based on the period
    formatted_tvec = timeFormat(tvec, period)

    # Define the labels for each zone
    labels = ["Zone 1", "Zone 2", "Zone 3", "Zone 4"]

    # Filter the data based on the selected zones
    filtered_data = data[:, np.array(plot, dtype=bool)]

    # Convert the data to kW by dividing by 1000
    filtered_data_kw = filtered_data / 1000

    # Check if the aggregated data contains less than 25 measurements
    use_bar_chart = len(formatted_tvec) < 25

    # Create a figure and axis for the plot
    fig, ax = plt.subplots()

    # Set the title and labels for the axes
    ax.set_title("Electricity Consumption")
    ax.set_xlabel("Time")
    ax.set_ylabel("Consumption (kW)")

    # Initialize the bottom array for stacking the bars
    bottom = np.zeros(len(formatted_tvec))

    should_plot_combined = combine_zones and not use_bar_chart and np.sum(plot) > 1

    selected_zones = []
    # Loop through each selected zone and plot the data
    zone_index = 0
    for i, selected in enumerate(plot):
        if selected:
            zone_label = labels[i]
            zone_data = filtered_data_kw[:, zone_index]

            if not should_plot_combined:
                if use_bar_chart:
                    # Use a bar chart and stack the bars on top of each other
                    ax.bar(formatted_tvec, zone_data, label=zone_label, bottom=bottom)
                    bottom += zone_data  # Update the bottom array for stacking
                else:
                    # Use a line chart
                    ax.plot(formatted_tvec, zone_data, label=zone_label)

            selected_zones.append(zone_label)
            zone_index += 1

    if should_plot_combined:
        # If using a line chart and combine_zones is True, add a line for the combined data
        combined_data = np.sum(filtered_data_kw, axis=1)
        # Shows exactly what zones have been combined
        combined_label = f"Combined zones ({', '.join(selected_zones)})"
        ax.plot(formatted_tvec, combined_data, label=combined_label)

    # Add a legend to the plot
    ax.legend()

    # Rotate the x-axis labels for better readability
    plt.xticks(rotation=45)

    # Show the plot
    plt.show()


