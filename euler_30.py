#! /usr/bin/env python
#coding=utf-8

295245
99999

59049

print [i**5 for i in range(10)]

def five(n):
    total = 0
    for i in range(2,n):
        temp = 0
        for j in str(i):
            temp += int(j)**5
        if i == temp:
            print i
            total += i
    print 'result is : ' ,total

five(1000000)
#443839