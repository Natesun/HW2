import csv
ss = open("status.csv", "r")
yy = csv.reader(ss)

result2 = []
rownum = 0

for row in yy:
    if rownum == 0:
        header = row[:]
    else:
        result2 = [row[1], row[2], row[3],row[4],row[5],row[6],row[7],row[8]]
        print(result2)

    rownum += 1

ss.close()