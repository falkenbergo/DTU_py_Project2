# -*- coding: utf-8 -*-
"""
Created on Mon April  29 20:37:36 2023

@author: Marc(s195088)
"""

# ============================================================================#
#                                LIBRARIES                                    #
# ============================================================================#

#Using these libraries to display the correct month with the data 
from datetime import datetime
import calendar

#==============================================================================
#The timeFormat function changes how time is displayed based on the period.
#It formats the time using year, month, day, hour, minute, and second.
#Usage:
#   formatted_tvec = timeFormat(tvec, period)
#Input:
#   tvec: Time values (list with np.array)
#   "period: Time period to format (string)
#Output:
#   formatted_tvec: Formatted time values (list)
#
#- Written by Marc(s195088)
#==============================================================================


def timeFormat(tvec, period):
    # Print input data to check
    print("Input tvec:", tvec)
    print("Input period:", period)

    # Empty list for formatted times
    formatted_tvec = []

    # For month or day, use "year/month/day" format
    if period in ["month", "day"]:
        for row in tvec:
            # Get year, month, and day
            year, month, day = row[:3].astype(int)
            # If month, show month names
            if period == "month":
                month_name = calendar.month_name[month]
                formatted_tvec.append(f"{month_name}")
            else:
                formatted_tvec.append(f"{round(tvec[0][0])}/{month}/{day}")

    # For hour or sec, use "year/month/day - hour:minute:second" format
    elif period in ["hour", "sec"]:
        for row in tvec:
            # Get year, month, day, hour, minute, second
            year, month, day, hour, minute, second = row.astype(int)
            # Add formatted time to list
            formatted_tvec.append(f"{round(tvec[0][0])}/{month}/{day} - {hour}:{minute}:{second}")

    # For 'hour of the day', list hours from 0 to 23
    elif period == "hour of the day":
        formatted_tvec = [str(hour) for hour in range(24)]

    # Print output data to check
    print("Output formatted_tvec:", formatted_tvec)

    # Return formatted time values
    return formatted_tvec
