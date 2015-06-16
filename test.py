from csv import*
def affordableunit():

    unit_num = []
    ff = open("Affordable2.csv")
    bb = reader(ff)
    rownum = 0


    for row in bb:
        if rownum == 0:
            pass
        else:
            unit_num.append([row[0], row[8]])
        rownum +=1

    return unit_num
affordableunit()




