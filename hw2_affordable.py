class Affordable:
    def _init_(self, name, unit):
        self.name= name
        self.unit= unit

import csv
ff = open("affordable.csv", "r")
bb = csv.reader(ff)

result = [Affordable]
rownum = 0
data = []

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





