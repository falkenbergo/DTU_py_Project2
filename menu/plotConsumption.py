# -*- coding: utf-8 -*-
"""
Created on Mon May  1 17:56:26 2023

@author: Marc
"""

import matplotlib.pyplot as plt

def plotConsumption(tvec_a, data_a):
    if len(tvec_a) < 25:
        # Plot as histogram if less than 25 data points
        plt.hist(data_a, bins=10)
    else:
        # Plot as line chart
        plt.plot(tvec_a, data_a)

    plt.xlabel('Time')
    plt.ylabel('Electricity consumption')
    plt.title('Electricity consumption over time')
    plt.show()
