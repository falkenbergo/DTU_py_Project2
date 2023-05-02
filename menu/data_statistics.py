
import numpy as np
#import pandas as pd
import pandas as pd
#from numerize import numerize

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
    print(np.sum(data, axis = 0)/len(data))  
    zones = ["Zone 1", "Zone 2", "Zone 3", "Zone 4", "All"]
    stats = ["Minimum", "1. quart.", "2. quart.", "3. quart.", "Maximum"]
@ -35,6 +71,7 @@ def print_statistics(tvec, data):
        for j in range(len(stats)):
            print("{:<10.2f}".format(table[i, j]), end="")
        print()
    """
    
    """
    print(data.min())
"""