class Affordable:
    def _init_(self, name, unit):
        self.name= name
        self.unit= unit


    import csv
    ff = open("affordable2.csv", "r")
    bb = csv.reader(ff)

    result = []
    rownum = 0
    data = []

    for row in bb:
        if rownum == 0:
            heading = row[:]
        elif len(row[0])== 0:
                pass
        else:
            result.append(row[0])

        rownum +=1
    print(result)
    print(len(result))

from pydoc import help
from scipy.stats.stats import pearson
help(pearson)

pearson(x, y)

do a if statement for repetitive numbers





