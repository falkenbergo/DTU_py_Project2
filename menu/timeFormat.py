# -*- coding: utf-8 -*-
"""
Created on Mon May  1 18:37:37 2023

@author: Marc
"""

from datetime import datetime

def timeFormat(tvec, period):
    # Initialize an empty list to store the formatted time values
    formatted_tvec = []

    # If the period is 'month' or 'day', format the time as "year/month/day"
    if period in ["month", "day"]:
        for row in tvec:
            # Get the year, month, and day values from the row as integers
            year, month, day = row[:3].astype(int)
            # Append the formatted time string to the list
            formatted_tvec.append(f"{year}/{month}/{day}")

    # If the period is 'hour' or 'min_sec', format the time as "year/month/day - hour:minute:second"
    elif period in ["hour", "min_sec"]:
        for row in tvec:
            # Get the year, month, day, hour, minute, and second values from the row as integers
            year, month, day, hour, minute, second = row.astype(int)
            # Append the formatted time string to the list
            formatted_tvec.append(f"{year}/{month}/{day} - {hour}:{minute}:{second}")

    # If the period is 'hour of the day', create a list of hours from 0 to 23 as strings
    elif period == "hour of the day":
        formatted_tvec = [str(hour) for hour in range(24)]

    # Return the list of formatted time values
    return formatted_tvec
