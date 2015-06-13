import csv
ff = open("affordable.csv", "r")
bb = csv.reader(ff)
result = {}
rownum = 0

for row in bb:
    if rownum == 0:
        header = row[:]
    else:
        k = row[0]
        v = row[1], row[2], row[8]

        result[k] = v

    rownum +=1
print(result)
print(len(result))
ff.close()





