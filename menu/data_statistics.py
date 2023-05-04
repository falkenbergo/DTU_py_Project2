# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 16:40:53 2023

@author: Anders S184198
"""

# Import required libraries
import numpy as np
import pandas as pd

# Define a function to print statistics for the given data
def print_statistics(tvec, data, period):
    # Create a percentile vector for calculating statistics
    percentileVec = np.array([0, 25, 50, 75, 100])

    # Calculate statistics for each column (zone) in the data
    stats = np.array([[np.percentile(data[:, j], p) for p in percentileVec] for j in range(4)])

    # Add a row with the sum of columns
    stats = np.vstack([stats, stats.sum(axis=0)])

    # Convert units by dividing the stats by 1000 until all elements are less than 10000
    divisions = 0
    while np.any(stats > 10000):
        stats /= 1000
        divisions += 1

    # Define the appropriate unit string based on the number of divisions
    prefix = ['', 'k', 'M', 'G', 'T']
    unit = prefix[divisions] + 'Wh' + ' / ' + period

    # Create and format axis to display the statistics
    xLabels = np.array(["Minimum", "1. quart.", "2. quart.", "3. quart.", "Maximum"])
    yLabels = np.array(["1", "2", "3", "4", "All"])

    stat_table = pd.DataFrame(stats, yLabels, xLabels)
    stat_table.columns.name = "Zone"
    stat_table = stat_table.round(3)

    # Center the unit string for a better display
    dashes_line_length = 70 - len(unit) - len("***      ***")
    centered_unit = unit.center(dashes_line_length)

    # Print the formatted statistics table with a header and footer
    print("\n///////////////////////////////////////////////////////\n***{}***\n///////////////////////////////////////////////////////\n{}\n///////////////////////////////////////////////////////\n".format(centered_unit, stat_table))
