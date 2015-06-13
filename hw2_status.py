import csv
ss = open("status.csv", "r")
yy = csv.reader(ss)

result2={}
for row in yy:
    key = row[1]
    if key in result2:
        pass
    else:
        result2[key] = row[2:]
    print(result2)
ss.close()