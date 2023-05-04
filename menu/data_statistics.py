
import numpy as np
#import pandas as pd
import pandas as pd
#from numerize import numerize

def print_statistics(tvec, data, period):
    percentileVec = np.array([0, 25, 50, 75, 100])

    stats = np.array([[np.percentile(data[:, j], p) for p in percentileVec] for j in range(4)])

    # Add row with sum of columns
    stats = np.vstack([stats, stats.sum(axis=0)])

    # Convert units
    divisions = 0
    while np.any(stats > 10000):
        stats /= 1000
        divisions += 1

    prefix = ['', 'k', 'M', 'G', 'T']
    unit = prefix[divisions] + 'Wh' + ' / ' + period

    # Create and format DataFrame
    xLabels = np.array(["Minimum", "1. quart.", "2. quart.", "3. quart.", "Maximum"])
    yLabels = np.array(["1", "2", "3", "4", "All"])

    stat_table = pd.DataFrame(stats, yLabels, xLabels)
    stat_table.columns.name = "Zone"
    stat_table = stat_table.round(3)

    # Center unit string
    dashes_line_length = 70 - len(unit) - len("***      ***")
    centered_unit = unit.center(dashes_line_length)

    print("\n-------------------------------------------------------\n***{}***\n-------------------------------------------------------\n{}\n-------------------------------------------------------\n".format(centered_unit, stat_table))

"""
def print_statistics(tvec, data, period):
    
    printTable = np.zeros([5,5])
    percentileVec = np.array([0, 25, 50, 75, 100])
    
    for j in range(4):
        for i in range(5):
            printTable[j, i] = (np.percentile(data[:, j], percentileVec[i]))
            
    for i in range(5):
        printTable[4, i] = np.sum(printTable[0:4, i])
    
    printTable, divisions = convert_unit(printTable)
    print(divisions)
    print(period)
    prefix = ['', 'k', 'M', 'G', 'T'] 
    unit = prefix[divisions] + 'Wh' + ' / ' + period
    centered_unit = unit.center(45 - len("***      ***"))
    print(unit)
    
 #   tableVec = numerize.numerize(tableVec)
    
    xLabels = np.array(["Minimum", "1. quart.", "2. quart.", "3. quart.", "Maximum"])
    yLabels = np.array(["1", "2", "3", "4", "All"])
    stat_table = pd.DataFrame(printTable, yLabels, xLabels)     # Make the panda table ready for printing
    stat_table.columns.name = "Zone"
    stat_table = stat_table.round(3)                            # Round the values to 3 decimals
 #   
    print("\n-------------------------------------------------------\n***       {}        ***\n-------------------------------------------------------\n{}\n-------------------------------------------------------\n".format(centered_unit, stat_table))


def convert_unit(tableVec):
    divisions = 0
    for n in range(len(tableVec[0])):
        for m in range(len(tableVec)):
            if(tableVec[n,m] > 10000):
                tableVec = tableVec / 1000
                divisions =+ 1
    return(tableVec, divisions)
                
    """              
            
