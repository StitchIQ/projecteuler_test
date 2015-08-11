
month = [31,28,31,30,31,30,31,31,30,31,30,31]

def get_year(year):
    if (year %4 == 0 and year %100 !=0) or (year%400 ==0):
        return True
    else:
        return False

def count_monday():
    total = 0
    index = 0
    for i in range(1900,2001):
        if get_year(i):
            month[1] = 29
        else:
            month[1] = 28
        for j in range(0,12):
            if total%7 == 6:
                index += 1
                print 'year is %d ; month is : %d'%(i,j+1)
            total += month[j]

    print index
    #print 'total ',total

count_monday()