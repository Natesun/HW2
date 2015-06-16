class Status:
    def _init_(self, index1, index2, index3, index4, index5, index6, index7, index8):
        self.area= index1
        self.housing= index2
        self.poverty= index3
        self.umemployed= index4
        self.education = index5
        self.age= index6
        self.income= index7
        self.hardship = index8

#from Status import *
#def _init_ (self):
       # self.statusfile = list()
        #self.affordablefile = list()
import csv
ss = open("status.csv", "r")
yy = csv.reader(ss)

result = []
rownum = 0

for row in yy:
    if rownum == 0:
        header = row[:] #skip the first row
    else:
        result.append(row[1] and row[2] and row[3] and row[4]and row[5] and row[6] and row[7]and row[8])
    rownum += 1
print(result)
ss.close()