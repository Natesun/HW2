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

result = [Status]
rownum = 0

for row in yy:
    if rownum == 0:
        header = row[:]
    else:
        result= (row[1], row[2], row[3],row[4],row[5],row[6],row[7],row[8])
        print(result)
    rownum += 1

ss.close()