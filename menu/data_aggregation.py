# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 16:40:53 2023

@author: ander
"""

import numpy as np

def aggregate_measurements(tvec, data, period):
    if period == 'hour':
        tvec_hourly = tvec[:, :4]
        print(tvec_hourly)
        tvec_unique, indices = np.unique(tvec_hourly, axis=0, return_inverse=True)
        print(tvec_unique)
        print(indices)
        
        """
          År           måned      dag         time      min         sek
        [[2.008e+03, 1.000e+00, 5.000e+00, 1.500e+01, 8.000e+00, 0.000e+00],
        [2.008e+03, 1.000e+00, 6.000e+00, 1.600e+01, 9.000e+00, 0.000e+00],
        [2.008e+03, 1.000e+00, 7.000e+00, 1.700e+01, 1.000e+01, 0.000e+00],
        """
        
        """
        # Get the hourly timestamp by rounding down the minutes and seconds
        tvec_hourly = tvec[:, :4]
        tvec_hourly[:, 1:] = np.floor(tvec_hourly[:, 1:] / [60, 60])
        # Get the unique hourly timestamps
        tvec_unique, indices = np.unique(tvec_hourly, axis=0, return_inverse=True)
        # Aggregate the data by summing over each unique timestamp
        data_aggregated = np.zeros((len(tvec_unique), data.shape[1]))
        for i in range(len(tvec_unique)):
            data_aggregated[i] = np.sum(data[indices == i], axis=0)
        # Return the aggregated data and the corresponding hourly timestamps
        
        """
    #    return (tvec_unique, data_aggregated)
    elif period == 'day':
        """
        # Get the daily timestamp by rounding down the hours, minutes and seconds
        tvec_daily = tvec[:, :3]
        tvec_daily[:, 2] = np.floor(tvec_daily[:, 2] / 24)
        # Get the unique daily timestamps
        tvec_unique, indices = np.unique(tvec_daily, axis=0, return_inverse=True)
        # Aggregate the data by summing over each unique timestamp
        data_aggregated = np.zeros((len(tvec_unique), data.shape[1]))
        for i in range(len(tvec_unique)):
            data_aggregated[i] = np.sum(data[indices == i], axis=0)
        # Return the aggregated data and the corresponding daily timestamps
        
        """
      #  return (tvec_unique, data_aggregated)
    elif period == 'month':
        """
        # Get the monthly timestamp by rounding down the days, hours, minutes and seconds
        tvec_monthly = tvec[:, :2]
        tvec_monthly[:, 1] = np.floor(tvec_monthly[:, 1] / 30)
        # Get the unique monthly timestamps
        tvec_unique, indices = np.unique(tvec_monthly, axis=0, return_inverse=True)
        # Aggregate the data by summing over each unique timestamp
        data_aggregated = np.zeros((len(tvec_unique), data.shape[1]))
        for i in range(len(tvec_unique)):
            data_aggregated[i] = np.sum(data[indices == i], axis=0)
        # Return the aggregated data and the corresponding monthly timestamps
        
        """
      #  return (tvec_unique, data_aggregated)
    elif period == 'hour of the day':
        """
        # Get the hour of the day as a decimal number
        tvec_hour_of_day = tvec[:, 3] + tvec[:, 4] / 60 + tvec[:, 5] / 3600
        # Aggregate the data by hour of the day
        data_aggregated = np.zeros((24, data.shape[1]))
        for i in range(24):
            data_aggregated[i] = np.mean(data[(tvec_hour_of_day >= i) & (tvec_hour_of_day < i+1)], axis=0)
        # Return the aggregated data and the corresponding start times of the 24 time intervals
        tvec_hourly = tvec[:, :4]
        tvec_hourly[:, 1:] = np.floor(tvec_hourly[:, 1:] / [60, 60])
        tvec_hourly[:, 3] += tvec_hourly[:, 2] * 24
        tvec_unique = np.arange(24) 
        
        """
        
      #  return (tvec_unique, data_aggregated)


tvec1 = [[2.008e+03, 1.000e+00, 5.000e+00, 1.500e+01, 8.000e+00, 0.000e+00],
        [2.008e+03, 1.000e+00, 6.000e+00, 1.600e+01, 9.000e+00, 0.000e+00],
        [2.008e+03, 1.000e+00, 7.000e+00, 1.700e+01, 1.000e+01, 0.000e+00],
        [2.008e+03, 1.000e+00, 8.000e+00, 1.800e+01, 1.100e+01, 0.000e+00],
        [2.008e+03, 1.000e+00, 9.000e+00, 1.900e+01, 1.200e+01, 0.000e+00],
        [2.008e+03, 1.000e+00, 1.000e+01, 2.000e+01, 1.300e+01, 0.000e+00]]

data1 = [[12. ,  0. , 18. , 35.4],
        [14.2,  1.6, 16.5, 33.7],
        [13.5, 31.2, 17. , 34.8],
        [11. ,  2.2, 19. , 35. ],
        [12.5, -1. , 18.5, 34.5],
        [15. , -1. , 17. , 32. ]]



tvec_np = np.array(tvec1)
data_np = np.array(data1)
print(tvec_np)
print(data_np)

print('-----------------------------------------------')
result = aggregate_measurements(tvec_np, data_np, 'hour')
print('-----------------------------------------------')

