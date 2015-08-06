#! /usr/bin/env python
#coding=utf-8

def Collatz(n):
    col = [n]
    while True:
        if n==1:
            break
        if n % 2 == 0:
            n = n/2
            col.append(n)
        else:
            n = 3*n+1
            col.append(n)
    return col

def find_max_collatz(n):
    index = 0
    for i in range(n,1,-1):
        temp = len(Collatz(i))
        if  temp > index:
            print 'i is ::', i
            index = temp
    print 'index is ::: ', index
    return index

find_max_collatz(1000000)
