# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 16:40:53 2023

@author: ander
"""

import numpy as np

def aggregate_measurements(tvec, data, period):
    if period == 'hour':
        # aggregate by hour
        tvec_a = np.unique(tvec[:,:4], axis=0) # get distinct year/month/day/hour combinations
        data_a = np.zeros((tvec_a.shape[0], 4))
        for i in range(tvec_a.shape[0]):
            idx = np.all(tvec[:,:4] == tvec_a[i], axis=1) # find all rows with matching year/month/day/hour
            data_a[i] = np.sum(data[idx], axis=0) # sum the data for all matching rows
            tvec_a[i, 4:] = [0, 0] # set minute and second to 0 for the beginning of the hour
        
    elif period == 'day':
        # aggregate by day
        tvec_a = np.unique(tvec[:,:3], axis=0) # get distinct year/month/day combinations
        data_a = np.zeros((tvec_a.shape[0], 4))
        for i in range(tvec_a.shape[0]):
            idx = np.all(tvec[:,:3] == tvec_a[i], axis=1) # find all rows with matching year/month/day
            data_a[i] = np.sum(data[idx], axis=0) # sum the data for all matching rows
            tvec_a[i, 3:] = [0, 0, 0] # set hour, minute, and second to 0 for the beginning of the day
        
    elif period == 'month':
        # aggregate by month
        tvec_a = np.unique(tvec[:,:2], axis=0) # get distinct year/month combinations
        data_a = np.zeros((tvec_a.shape[0], 4))
        for i in range(tvec_a.shape[0]):
            idx = np.all(tvec[:,:2] == tvec_a[i], axis=1) # find all rows with matching year/month
            data_a[i] = np.sum(data[idx], axis=0) # sum the data for all matching rows
            tvec_a[i, 2:] = [1, 0, 0, 0] # set day, hour, minute, and second to the beginning of the month
        
    elif period == 'hour of the day':
        # aggregate by hour of the day
        tvec_a = np.zeros((24, 6))
        tvec_a[:, 3] = np.arange(24) # set hour column to 0-23
        data_a = np.zeros((24, 4))
        for i in range(24):
            idx = tvec[:,3] == i # find all rows with matching hour
            data_a[i] = np.mean(data[idx], axis=0) # average the data for all matching rows
            tvec_a[i, 3:] = [i, 0, 0] # set minute and second to 0 for the beginning of the hour
        
    else:
        raise ValueError('Invalid period: {}'.format(period))
    
    return (tvec_a, data_a)


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

result = aggregate_measurements(tvec_np, data_np, 'day')
print('-----------------------------------------------')
print(result)
print('-----------------------------------------------')