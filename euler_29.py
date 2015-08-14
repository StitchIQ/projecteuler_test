#! /usr/bin/env python
#coding=utf-8

def count_num(a,b):
    total = []
    for i in range(2, a+1):
        for j in range(2, b+1):
            total.append(i**j)
    return len(set(total))

print count_num(100,100)
#print len(set(a**b for a in range(2, 101) for b in range(2, 101)))
