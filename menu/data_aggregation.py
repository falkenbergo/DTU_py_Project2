# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 16:40:53 2023

@author: Anders S184198
"""

import numpy as np

def aggregate_measurements(tvec, data, period):
    if period == 'hour':
        #Only look at "hour" colum
        tvec_hourly = tvec[:,0 :4]  

        #Find unique instances of hour row
        tvec_unique, indices = np.unique(tvec_hourly, axis=0, return_inverse=True) 
        
        # Aggregate the data by summing over each unique timestamp
        data_a = np.zeros((len(tvec_unique), data.shape[1]))
        for i in range(len(tvec_unique)):
            data_a[i] = np.sum(data[indices == i], axis=0)
        
        # Add four columns of zeros to replace the removed once
        tvec_a = np.hstack((tvec_unique, np.zeros((tvec_unique.shape[0], 2), dtype=tvec_unique.dtype)))

        return (tvec_a, data_a)

    elif period == 'day':
        #Only look at "day" colum
        tvec_hourly = tvec[:,0 :3]  

        #Find unique instances of hour row
        tvec_unique, indices = np.unique(tvec_hourly, axis=0, return_inverse=True) 

        
        # Aggregate the data by summing over each unique timestamp
        data_a = np.zeros((len(tvec_unique), data.shape[1]))
        for i in range(len(tvec_unique)):
            data_a[i] = np.sum(data[indices == i], axis=0)
        
        # Add three columns of zeros to replace the removed once
        tvec_a = np.hstack((tvec_unique, np.zeros((tvec_unique.shape[0], 3), dtype=tvec_unique.dtype)))
        
        return (tvec_a, data_a)
        
        
    elif period == 'month':
        #Only look at "month" colum
        tvec_hourly = tvec[:,0 :2]  

        #Find unique instances of hour month
        tvec_unique, indices = np.unique(tvec_hourly, axis=0, return_inverse=True) 
        
        # Aggregate the data by summing over each unique timestamp
        data_a = np.zeros((len(tvec_unique), data.shape[1]))
        for i in range(len(tvec_unique)):
            data_a[i] = np.sum(data[indices == i], axis=0)
        
        # Add four columns of zeros to replace the removed once
        tvec_a = np.hstack((tvec_unique, np.zeros((tvec_unique.shape[0], 4), dtype=tvec_unique.dtype)))

        return (tvec_a, data_a)
        
    elif period == 'hour of the day':
        #Only look at "hours of the day" colum
        tvec_hourly = tvec[:, [0, 3]]  

        #Find unique instances of hour in a day
        tvec_unique, indices = np.unique(tvec_hourly, axis=0, return_inverse=True) 

        
        # Aggregate the data by summing over each unique timestamp
        data_a = np.zeros((len(tvec_unique), data.shape[1]))
        for i in range(len(tvec_unique)):
            data_a[i] = np.sum(data[indices == i], axis=0)
        
        # Add two columns of zeros to replace mins and secs
        tvec_a = np.hstack((tvec_unique, np.zeros((tvec_unique.shape[0], 2), dtype=tvec_unique.dtype)))
        
        # Add two columns of zeros to replace days and months
        tvec_a = np.insert(tvec_a, 1, np.zeros((tvec_unique.shape[0]), dtype=tvec_unique.dtype), axis=1)
        tvec_a = np.insert(tvec_a, 1, np.zeros((tvec_unique.shape[0]), dtype=tvec_unique.dtype), axis=1)
        
        return (tvec_a, data_a)



