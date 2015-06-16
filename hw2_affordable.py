


def affordableunit():
#I am trying to make a list with area number and affordable unit numbers
    import csv
    ff = open("Affordable2.csv", "r")
    bb = csv.reader(ff)
    unit_num = []
    rownum = 0

    for row in bb:
        if rownum == 0:
            pass
        else:
            unit_num.append([row[0], row[8]])
        rownum +=1

    return unit_num
    ff.close()

def status_index():
    import csv
    yy = open("status.csv", "r")
    ss = csv.reader(yy)
    income = []
    rownum1 = 0

    for row in ss:
        if rownum1 == 0:
            pass
        else:
            income.append([row[0], row[7]])
        rownum1 +=1
    return income
    yy.close()
status_index()

def income_unitnum():
    for i in range(6):
        r, x, y, xy, xx, yy = []



