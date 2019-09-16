import csv

import random

allrows = []
alljobs = {}

with open("occupations.csv") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=",")
    for row in readCSV:
        allrows.append(row)

# print (allrows[1])

alljobs[allrows[1][0]] = float(allrows[1][1])

# print (alljobs[allrows[1][0]])

for x in range(1, len(allrows)):
    alljobs[allrows[x][0]] = float(allrows[x][1]) * 10


selector = random.randint(0, 998)

def getjob():
    runsum = 0

    for x in alljobs.keys():
            runsum += alljobs[x]
            if runsum > selector:
                return x

testdict = {}

for x in alljobs.keys():
    testdict[x] = 0


for x in range(1000):
    z = getjob()
    print(z)

    testdict[z] += 1


print(testdict)
