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

    #for i in range(1, sqrt(n)):
    #    if n % i == 0:
    #        total.append(i)
    #total.append(n)
    #print total
    #print len(total)
    return total

#print find_factors(21)

def find_triangle():
    temp = 0
    for s in range(1,1000000):
        temp += s
        print temp
        if find_factors(temp) >= 500:
            print s
            print temp
            break

find_triangle()
#print 2**38