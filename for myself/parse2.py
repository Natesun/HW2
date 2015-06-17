__author__ = 'HongbinSun'

def unitnumlist(): #I am making a unitnumlist in the area number order of 77 chicago
    #area to store the affordable housing unit numbers(I admit that I manually
    # transformed a lot, but for now, let us just let it be), I will compare this with
    # incomelist in pearson
    import csv

    with open("affordable2.csv") as csvfile:
        readstatus = csv.reader(csvfile, delimiter=",")
        unitnum = []
        rownum = 0
        for row in readstatus:
            if rownum == 0:
                pass
            else:
                unitnum.append(row[8])
            rownum +=1
        print(unitnum)
        print(len(unitnum))
unitnumlist()
