# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 16:40:53 2023

@author: ander
"""

import numpy as np

def aggregate_measurements(tvec, data, period):
    if period == 'hour':
        tvec_hourly = tvec[:,0 :4]  #Only look at "hour" row

        tvec_unique, indices = np.unique(tvec_hourly, axis=0, return_inverse=True) #Find unique instances of hour row

        
        # Aggregate the data by summing over each unique timestamp
        data_aggregated = np.zeros((len(tvec_unique), data.shape[1]))
        for i in range(len(tvec_unique)):
            data_aggregated[i] = np.sum(data[indices == i], axis=0)
        
        data_a = data_aggregated
        
        tvec_a = np.hstack((tvec_unique, np.zeros((tvec_unique.shape[0], 2), dtype=tvec_unique.dtype)))
    #    tvec_a = np.hstack((np.zeros((tvec_a.shape[0], 3), dtype=tvec_a.dtype), tvec_a))
        
        print('------------ TVEC Hour --------------')
        print(tvec_a)
        print(len(tvec_a))
        print('--------------------------------')
        
        print('------------ DATA --------------')
        print(data_a)
        print('--------------------------------')
        
        return (tvec_a, data_a)

    elif period == 'day':
        tvec_hourly = tvec[:,1 :3]  #Only look at "hour" row

        tvec_unique, indices = np.unique(tvec_hourly, axis=0, return_inverse=True) #Find unique instances of hour row

        
        # Aggregate the data by summing over each unique timestamp
        data_aggregated = np.zeros((len(tvec_unique), data.shape[1]))
        for i in range(len(tvec_unique)):
            data_aggregated[i] = np.sum(data[indices == i], axis=0)
        
        data_a = data_aggregated
        
        tvec_a = np.hstack((tvec_unique, np.zeros((tvec_unique.shape[0], 3), dtype=tvec_unique.dtype)))
        tvec_a = np.hstack((np.zeros((tvec_a.shape[0], 1), dtype=tvec_a.dtype), tvec_a))
        
        print('------------ TVEC Day --------------')
        print(tvec_a)
        print(len(tvec_a))
        print('--------------------------------')
        
        print('------------ DATA --------------')
        print(data_a)
        print('--------------------------------')
        
        return (tvec_a, data_a)
        
        

    elif period == 'month':
        tvec_hourly = tvec[:,1 :2]  #Only look at "hour" row

        tvec_unique, indices = np.unique(tvec_hourly, axis=0, return_inverse=True) #Find unique instances of hour row

        
        # Aggregate the data by summing over each unique timestamp
        data_aggregated = np.zeros((len(tvec_unique), data.shape[1]))
        for i in range(len(tvec_unique)):
            data_aggregated[i] = np.sum(data[indices == i], axis=0)
        
        data_a = data_aggregated
        
        tvec_a = np.hstack((tvec_unique, np.zeros((tvec_unique.shape[0], 4), dtype=tvec_unique.dtype)))
        tvec_a = np.hstack((np.zeros((tvec_a.shape[0], 1), dtype=tvec_a.dtype), tvec_a))
        
        print('------------ TVEC Month --------------')
        print(tvec_a)
        print(len(tvec_a))
        print('--------------------------------')
        
        print('------------ DATA --------------')
        print(data_a)
        print('--------------------------------')
        
        return (tvec_a, data_a)
        
    elif period == 'hours of the day':
        tvec_hourly = tvec[:,3 :4]  #Only look at "hour" row

        tvec_unique, indices = np.unique(tvec_hourly, axis=0, return_inverse=True) #Find unique instances of hour row

        
        # Aggregate the data by summing over each unique timestamp
        data_aggregated = np.zeros((len(tvec_unique), data.shape[1]))
        for i in range(len(tvec_unique)):
            data_aggregated[i] = np.sum(data[indices == i], axis=0)
        
        data_a = data_aggregated
        
        tvec_a = np.hstack((tvec_unique, np.zeros((tvec_unique.shape[0], 2), dtype=tvec_unique.dtype)))
        tvec_a = np.hstack((np.zeros((tvec_a.shape[0], 3), dtype=tvec_a.dtype), tvec_a))
        
        print('------------ TVEC HOD --------------')
        print(tvec_a)
        print(len(tvec_a))
        print('--------------------------------')
        
        print('------------ DATA --------------')
        print(data_a)
        print('--------------------------------')
        
        return (tvec_a, data_a)



