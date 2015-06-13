import csv
ff = open("affordable.csv", "r")
bb = csv.reader(ff)

result = []
rownum = 0

for row in bb:
    if rownum == 0:
        heading = row[:]
    elif len(row[0])== 0:
            pass
    else:
        kk = row[0]
        vv = row[1], row[2], row[8]
        result = [kk, vv]
        print(result)
    rownum +=1


ff.close()





