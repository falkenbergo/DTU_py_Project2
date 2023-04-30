# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 11:28:01 2023

@author: ander
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 16:40:53 2023

@author: ander
"""

import numpy as np

def print_statistics(tvec, data):
    # Define the zones based on the first element of each row in tvec
    zones = np.unique(tvec[:, 0])
    
    # Print the header row of the table
    print("{:5s} {:>10s} {:>10s} {:>10s} {:>10s} {:>10s}".format(
        "Zone", "Minimum", "1. quart.", "2. quart.", "3. quart.", "Maximum"))
    
    # Compute the statistics for each zone
    for i, zone in enumerate(zones):
        # Select the rows corresponding to the current zone
        mask = tvec[:, 0] == zone
        zone_data = data[mask]
        
        # Compute the statistics for the current zone
        stats = np.percentile(zone_data, [0, 25, 50, 75, 100], axis=0)
        
        # Print the statistics for the current zone
        print("{:5d} {:10.2f} {:10.2f} {:10.2f} {:10.2f} {:10.2f}".format(
            i + 1,
            np.min(data[:,i]),
            np.percentile(data[:,i], 25),
            np.percentile(data[:,i], 50),
            np.percentile(data[:,i], 75),
            np.max(data[:,i])))
    
    # Compute the statistics for all zones combined
    all_stats = np.percentile(data, [0, 25, 50, 75, 100], axis=0)
    
    # Print the statistics for all zones combined
    print("{:5s} {:10.2f} {:10.2f} {:10.2f} {:10.2f} {:10.2f}".format(
        "All", all_stats[0], all_stats[1], all_stats[2], all_stats[3], all_stats[4]))




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

result = print_statistics(tvec_np, data_np)
print('-----------------------------------------------')
print(result)
print('-----------------------------------------------')

