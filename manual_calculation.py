
# this is a practice test, I learned from Harrison
# there is a complicated loop to manually get the pearson test, i am trying to
#some easy way to get this result

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
        values, x, y, xy, xx, yy = ([] for i in range(6)) #create emply list
    for n in range (0, 77): # for loop to calculate x, y, xy, xx, yy on each row
        x.append(float(affordableunit())[n][1])
        y.append(float(status_index())[n][1])
        xy.append(x[n]*y[n])
        xx.append(x[n]**2)
        yy.append(y[n]**2)
        values.append(x[n], y[n], xy[n], xx[n], yy[n])
    return values
income_unitnum()

def correlation(pearsonlist):
    sx, sy, sxy, sx2, sy2 = [0]*5
    n = len(pearsonlist)
    for row in pearsonlist:
        sx += row[0]
        sy += row[1]
        sxy += row[2]
        sx2 += row[3]
        sy2 += row[4]
    r = (sxy-sx*sy)/ pow((sx2-pow(sx,2)/n)*(sy2-sy**2/n)), 0.5)
    return r

def result():
    print("the pearson correlation r between affordable housing unit numbers/n"
          "and per capital income is " , correlation(income_unitnum()))






