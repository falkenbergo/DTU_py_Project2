# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 10:50:47 2023

@author: Falkenbergo
"""

import numpy as np

def load_measurements(filename, fmode):
    # Read the file line by line, split each line into values, and remove spaces
    with open(filename) as file:
        lines = []
        line_number = 0
        
        for line in file:
            line_number += 1 # Keep track of line number
            values = line.strip().split(',') # Remove spaces and split each line
            column_number = 0
            
            for value in values:
                column_number += 1 # Keep track of column number
                
                # Trying converting value to a number
                try:
                    float(value)
                
                # If fails, then non-numeric value has been detected
                except ValueError:
                    # Error message: Non-numeric values detected
                    raise ValueError(f"File:\033[38;2;100;255;0m'{filename}'\033[0m \nNon-numeric value:'{value}' detected at line: {line_number}, column: {column_number}")
    
    # Load data and tvec from file
    data = np.loadtxt(filename, delimiter=',', usecols=(6, 7, 8, 9))
    tvec = np.loadtxt(filename, delimiter=',', usecols=(0, 1, 2, 3, 4, 5))

    # Identify corrupted measurements
    corrupted_measurements = (data == -1)

    # =============================================================================
    # fmode - Criteria: How to handle corrupted measurements
    # =============================================================================
    if fmode == 'forward fill':
        # Replace with the latest valid measurement
        for i in range(1, data.shape[0]):
            for j in range(data.shape[1]):
                if corrupted_measurements[i, j]:
                    data[i, j] = data[i - 1, j]

    elif fmode == 'backward fill':
        # Replace with the next valid measurement
        for i in range(data.shape[0] - 2, -1, -1):
            for j in range(data.shape[1]):
                if corrupted_measurements[i, j]:
                    data[i, j] = data[i + 1, j]

    elif fmode == 'drop':
        # Delete corrupted measurements
        valid_rows = np.logical_not(corrupted_measurements).all(axis=1)
        data = data[valid_rows, :]
        tvec = tvec[valid_rows, :]

    else:
        # Error message: Invalid fmode value
        raise ValueError("Invalid fmode value. Use 'forward fill', 'backward fill', or 'drop'.")
    
    return (tvec, data)
