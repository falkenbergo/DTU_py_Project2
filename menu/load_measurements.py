# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 10:50:47 2023

@author: Falkenbergo
"""

import numpy as np

def load_measurements(filename, fmode):
    
    
    # Read the file line by line, split each line into values, and remove space
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
    
    # Load data and tvec(timevector) from file
    # Specific colmns has been choosen for both data and tvec
    data = np.loadtxt(filename, delimiter=',', usecols=(6, 7, 8, 9))
    tvec = np.loadtxt(filename, delimiter=',', usecols=(0, 1, 2, 3, 4, 5))
    
    # Load rows and columns
    dataRows = data.shape[0]
    dataColumns = data.shape[1]
    
    # Identify corrupted measurements that contains -1 and returns boolian array
    corrupted_measurements = (data == -1)
    
    # =============================================================================
    # fmode - Criteria: How to handle corrupted measurements
    # =============================================================================
    
    # If forward fill is chosen
    if fmode == 'forward fill':
        
        # Go through each column
        for j in range(dataColumns):
            
            # Remember the last valid value
            # Use object None
            last_valid_value = None
            
            # Go through each row
            for i in range(dataRows):
                
                # If the measurement is not corrupted
                if not corrupted_measurements[i, j]:
                    
                    # Update the last valid value
                    last_valid_value = data[i, j]
                    
                # If the measurement is corrupted and we have a valid value
                # Makes sure that we have a valid value to assign
                elif last_valid_value is not None:
                    
                    # Replace the corrupted measurement with the last valid value
                    data[i, j] = last_valid_value
    
    # If backward fill is chosen
    elif fmode == 'backward fill':
        
        # Go through each column
        for j in range(dataColumns):
            
            # Remember the next valid value
            # Use object  None
            next_valid_value = None
            
            # Go through each row in reverse order
            # To have access of the measurements in the future
            for i in reversed(range(dataRows)):
                
                # If the measurement is not corrupted
                if not corrupted_measurements[i, j]:
                    
                    # Update the next valid value
                    next_valid_value = data[i, j]
                    
                # If the measurement is corrupted
                # Makes sure that we have a valid value to assign
                elif next_valid_value is not None:
                    # Replace the corrupted measurement with the next valid value
                    data[i, j] = next_valid_value
    
    # If drop is chosen
    elif fmode == 'drop':
        
        # Make a list to store the valid row measurements
        valid_measurements = []
        
        # Go through each row
        for i in range(dataRows):
            
            # If there are no corrupted measurements in the row
            if not corrupted_measurements[i].any():
                
                # Add the row index to the valid_measurements list
                valid_measurements.append(i)
                
        # Keep only the valid rows in data and tvec arrays
        data = data[valid_measurements]
        tvec = tvec[valid_measurements]
    
    
    else:
        # Error message: Invalid fmode value
        raise ValueError(f"Invalid fmode: '\033[38;2;200;150;100m{fmode}\033[0m'. \nUse '\033[38;2;0;255;0mforward fill\033[0m', '\033[38;2;0;255;0mbackward fill\033[0m', or '\033[38;2;0;255;0mdrop\033[0m'.")
    
        
    # Reurn both timevector and data
    return (tvec, data)

tvec, data = load_measurements("test.txt", "backward fill")
print(tvec)
print(data)



