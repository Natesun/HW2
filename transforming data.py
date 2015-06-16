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

    import csv
    ss = open("status.csv", "r")
    yy = csv.reader(ss)

    result2 = []
    rownum = 0
    for row in yy:
        if rownum == 0:
            header = row[:] #skip the first row
        else:
            result2.append(row[1])
        rownum += 1
    print(result2)
    print(len(result2))
    result = set(result)
    result2 = set(result2)
    print(result2-result) #transforming data by add more into a second set
    ff.close()
    ss.close()





