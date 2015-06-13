import csv
ss = open("status.csv", "r")
yy = csv.reader(ss)

result2 = {}
rownum = 0
for row in yy:
    if rownum == 0:
        header = row[:]
    else:
        k = row[1]
        v = row[2:]
        result2[k] = v
    rownum += 1

print(result2)
print(len(result2))
ss.close()