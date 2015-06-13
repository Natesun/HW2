import csv
from collections import defa
import csv
data = defaultdict(list)
ss = open("status.csv", "r")
yy = csv.reader(ss)

for row in yy:
    data(row[1]).append(row[2:])

print(data)