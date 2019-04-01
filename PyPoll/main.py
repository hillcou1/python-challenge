import os
csvpath = os.path.join('election_data.csv')

import csv
from collections import Counter

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    Total_Votes = Counter()
    Candidates = []
    Percentage = []
    Win = []

    for row in csvreader:
        Candidates.append(row[2])

    Total_votes = len(Candidates)

    for name in Candidates:
        Total_Votes[name] += 1

    votes= tuple(Total_Votes.values())
    names = tuple(Total_Votes.keys())
    winner = max(zip(Total_Votes.values(), Total_Votes.keys()))

    for x in votes:
        Percentage.append((int(x)/Total_votes)*100)

    Win.append('Election Results')
    Win.append('-------------------------')
    Win.append('Total Votes' + str(Total_votes))
    Win.append('---------------------------')
    Win.append('Winner:' + winner[1])
    for x in range(len(names)):
        Win.append(names[x] + ':' + str(round(Percentage[x],1)) + '%' + '(' + str(votes[x]) + ')')


    print("\n".join((Win)))
with open(csvpath, 'w') as txtfile:
    txtfile.write("\n".join((Win)))
