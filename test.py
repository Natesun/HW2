import csv

out = open("affordable2.csv", "r")
data = csv.reader(out)
unit_num =[]
rownum =0
data = [[row[0],row[8]] for row in data]

print(data)


out = open("data.csv","w")
output = csv.writer
for row in data:
    output.writerow(row)
out.close()

