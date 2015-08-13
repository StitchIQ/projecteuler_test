#! /usr/bin/env python
#coding=utf-8


def fabira(n):
    start_1 = 1
    start_2 = 1
    if n < 3:
        return None
    for i in range(3,n):
        f_3 = start_1 + start_2
        if len(str(f_3)) >= 1000 :
            print i
            break
        start_1, start_2 = start_2, f_3
        #print f_3:
    return f_3

print fabira(10000)
#4782
