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
        result = [row[0],row[1], row[2], row[8]]
        
        print(result)
    rownum +=1


ff.close()





