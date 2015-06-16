__author__ = 'HongbinSun'
def incomelist(): #I am making a incomelist in the area number order of 77 chicago
    #area to store the capital income, I will compare this with unitnumlist in pearson
    import csv

    with open("status.csv") as csvfile:
        readstatus = csv.reader(csvfile, delimiter=",")
        income = []
        rownum = 0
        for row in readstatus:
            if rownum == 0:
                pass
            elif rownum ==77:
                pass
            else:
                income.append(row[7])
            rownum +=1
        print(income)  #gosh I finally know the difference between print and return
        print(len(income))
incomelist()


