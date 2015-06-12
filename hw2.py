import csv
ff = open("affordable.csv", "r")
bb = csv.reader(ff)

for row in bb:
    print(row)
ff.close()

ss = open ("status.csv", "r")
yy = csv.reader (ss)

for row in yy:
    print(row)
ss.close()

