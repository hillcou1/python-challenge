import os
csvpath = os.path.join('budget_data.csv')

import csv
from statistics import mean

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    financedata = {}
    Changes = []
    RevChange = {}
    Printlist = []

    for row in csvreader:
        if row[0] != 'Date':
            financedata[row[0]] = int(row[1])


    Months = len(financedata)
    TotRev = sum(financedata.values())
    Revenues = tuple(financedata.values())
    Month = tuple(financedata.keys())

    for x in range(1, (len(Revenues))):
        Changes.append((int(Revenues[x])- int(Revenues[x-1])))

    Average = round(mean(Changes))

    for x in range(1, (len(Month))):
        RevChange[Month[x]] = int(Changes[x-1])

    GreatIncrease = max(zip(RevChange.values(), RevChange.keys()))
    GreatDecrease = min(zip(RevChange.values(), RevChange.keys()))

    Printlist.append('Financial Analysis')
    Printlist.append('------------------')
    Printlist.append('Total Months:' + str(Months))
    Printlist.append('Total Revenue' + str(TotRev))
    Printlist.append('Average Revenue Change' + str(Average))
    Printlist.append('Greatest Increase in Revenue' + str(GreatIncrease[1]) + '($'+ str(GreatIncrease[0]) + ')')
    Printlist.append('Greatest Decrease in Revenue' + str(GreatDecrease[1]) + '($'+ str(GreatDecrease[0]) + ')')

    print("\n".join((Printlist)))
