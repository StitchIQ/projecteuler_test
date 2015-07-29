#! /usr/bin/env python
#coding=utf-8
def mulitiples(n):
    sum = 0
    for i in range(n):
        if i%3 == 0 or i%5 ==0:
           sum = sum + i
    return sum

print mulitiples(1000)
