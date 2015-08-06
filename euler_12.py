#! /usr/bin/env python
#coding=utf-8

def find_factors(n):
    total = 2
    for i in range(2,n):
        if i*i <= n:
            if n % i == 0:
                total += 2
        else:
            break
    return total


#如果所以小于sqrt(该数)的数中有n个因数，那么这个数的因数有2*n个。
#如果该数恰是平方数，那么该数有因数2 *n+1个
def find_div_num(n):
    number = 0
    divisor = 1
    triangle = n*(n+1)/2
    while(divisor*divisor < triangle):
        if (triangle % divisor == 0):
            number +=1
        divisor +=1

    if divisor*divisor == triangle:
        return 2*number +1
    else:
        return 2*number

def find_triangle():
    n = 1
    while(find_div_num(n) <= 500):
        n +=1
    print n
    print n*(n+1)/2
find_triangle()


