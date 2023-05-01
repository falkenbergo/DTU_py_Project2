
# -*- coding: utf-8 -*-
"""
Created on Mon May  1 17:56:26 2023

@author: Marc
"""
import matplotlib.pyplot as plt
import numpy as np

#Importing timeFormat function
from timeFormat import timeFormat

def plotComparison(tvec, data, plot, period):
    # Use the format_time function to format the time values based on the period
    formatted_tvec = timeFormat(tvec, period)

    # Define the labels for each zone
    labels = ["Zone 1", "Zone 2", "Zone 3", "Zone 4", "Combined"]

    # Filter the data based on the selected zones
    filtered_data = data[:, np.array(plot, dtype=bool)]

    # Check if the aggregated data contains less than 25 measurements
    use_bar_chart = len(formatted_tvec) < 25

    # Create a figure and axis for the plot
    fig, ax = plt.subplots()

    # Set the title and labels for the axes
    ax.set_title("Electricity Consumption")
    ax.set_xlabel("Time")
    ax.set_ylabel("Consumption")

    # Loop through each zone and plot the data
    for i, zone_label in enumerate(labels):
        if plot[i]:
            if use_bar_chart:
                # Use a bar chart if there are less than 25 measurements
                ax.bar(formatted_tvec, filtered_data[:, i], label=zone_label)
            else:
                # Use a line chart if there are 25 or more measurements
                ax.plot(formatted_tvec, filtered_data[:, i], label=zone_label)

    # Add a legend to the plot
    ax.legend()

    # Rotate the x-axis labels for better readability
    plt.xticks(rotation=45)

    # Show the plot
    plt.show()

    print("formatted_tvec shape:", formatted_tvec.shape, "filtered_data[:, i] shape:", filtered_data[:, i].shape)
