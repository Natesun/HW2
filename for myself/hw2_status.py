

import csv
ss = open("status.csv", "r")
yy = csv.reader(ss)

result = []
rownum = 0

for row in yy:
    if rownum == 0:
        header = row[:] #skip the first row
    else:
        result.append(row[1] and row[2] and row[3] and row[4]and row[5] and row[6] and row[7]and row[8])
    rownum += 1
print(result)
ss.close()



