#! /usr/bin/env python
#coding=utf-8
from runtime_test import *

@test_time
def find_back():
    max = 999
    min = 100
    li =[i*j for i in range(max, min, -1) for j in range(max, min, -1)]
    li.sort(reverse=True)
    for result in li:
        s = str(result)
        if s == s[::-1]:
            print s
            return s
@test_time
def find_back2():
    max = 999
    min = 99
    li = []
    for i in range(max, min, -1):
        for j in range(max, min, -1):
            result = i * j
            s = str(result)
            if s == s[::-1]:
                li.append(result)
    li.sort(reverse=True)            
    print li[0]
    
find_back()
find_back2()


