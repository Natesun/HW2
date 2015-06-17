__author__ = 'HongbinSun'
# after parsing from each data sets, get two lists incomelist[]
# and unitnumlist[] with the same order and same length (manually transformed the data)
#now import these two lists and get the r value
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
                income.append(float(row[7]))
            rownum +=1
        return(income)  #gosh I finally know the difference between print and return

incomelist()

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
                unitnum.append(float(row[8]))
            rownum +=1
        return(unitnum)

unitnumlist()
x = incomelist()
y = unitnumlist()
print(x)
print(len(x))
print(y)
print(len(y))

def pearsontest():
    from pydoc import help
    from scipy.stats.stats import pearsonr
    print("the r and p values for pearson's correlation are" , pearsonr(x,y))
pearsontest()

import unittest
from pydoc import help
from scipy.stats.stats import pearsonr

class Testpr(unittest.TestCase):
     def test_basic_equal(self):
         self.assertEqual(len(incomelist()), 77)
         self.assertEqual(len(unitnumlist()), 77)
         self.assertEqual(pearsonr([1,2,3],[1,5,7])[0].round(7), 0.9819805)

if __name__ == '__main__':
    unittest.main()






