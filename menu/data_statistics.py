# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 16:40:53 2023

@author: ander
"""

import numpy as np
#import pandas as pd

def print_statistics(tvec, data):
    print(np.sum(data, axis = 0)/len(data))  
    zones = ["Zone 1", "Zone 2", "Zone 3", "Zone 4", "All"]
    stats = ["Minimum", "1. quart.", "2. quart.", "3. quart.", "Maximum"]
    table = np.zeros((len(zones), len(stats)))

    for i, zone in enumerate(zones[:-1]):
        zone_data = data[:, i]
        table[i, 0] = np.min(zone_data)
        table[i, 1:4] = np.percentile(zone_data, [25, 50, 75])
        table[i, -1] = np.max(zone_data)

    all_data = data.flatten()
    table[-1, 0] = np.min(all_data)
    table[-1, 1:4] = np.percentile(all_data, [25, 50, 75])
    table[-1, -1] = np.max(all_data)

    print("{:<10}".format(""), end="")
    for stat in stats:
        print("{:<10}".format(stat), end="")
    print()

    for i, zone in enumerate(zones):
        print("{:<10}".format(zone), end="")
        for j in range(len(stats)):
            print("{:<10.2f}".format(table[i, j]), end="")
        print()
    
    """
    print(data.min())
    print(data.max())
    d = {1:     ["Python",  33.2,   'UP', 'test1', 'test2'],
         2:     ["Java",    23.54,  'DOWN', 'test1', 'test2'],
         3:     ["Ruby",    17.22,  'UP', 'test1', 'test2'],
         4:     ["Lua",     10.55,  'DOWN', 'test1', 'test2'],
         'All': ["Groovy",  9.22,   'DOWN', 'test1', 'test2'],
         
        }
    
    print ("{:<6} {:<12} {:<12} {:<12} {:<12} {:<12}".format('Zone','Minimum','1. quart','2. quart', '3. quart', 'Maximum'))
    for zones, v in d.items():
        min_val, qrtOne, qrtTwo, qrtThree, max_val = v
        print ("{:<6} {:<12} {:<12} {:<12} {:<12} {:<12}".format(zones, min_val, qrtOne, qrtTwo, qrtThree, max_val))
    
    df = pd.concat([tvec, data], axis=1)
    df['datetime'] = pd.to_datetime(df[['year', 'month', 'day', 'hour', 'minute', 'second']])
    df.set_index('datetime', inplace=True)
    
    """
    
    """
    # Compute statistics for each zone and all zones combined
    all_data = np.concatenate(data, axis=0)
    all_stats = np.percentile(all_data, [0, 25, 50, 75, 100], axis=0)
    zone_stats = []
    for zone_data in data:
        zone_stats.append(np.percentile(zone_data, [0, 25, 50, 75, 100], axis=0))
    
    # Print the table header
    print('Zone, Minimum, 1. quart., 2. quart., 3. quart., Maximum')
    
    # Print the statistics for each zone and all zones combined
    for i, stats in enumerate(zone_stats + [all_stats]):
        zone_name = f'All' if i == 4 else f'{i+1}'
        print(f'{zone_name}, {stats[0]:.2f}, {stats[1]:.2f}, {stats[2]:.2f}, {stats[3]:.2f}, {stats[4]:.2f}')
    """

"""
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
result = print_statistics(tvec1, data1)
print('-----------------------------------------------')

"""

