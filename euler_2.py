#! /usr/bin/env python
#coding=utf-8

def fabira(n):
    start_1 = 0
    start_2 = 1
    all = 0
    for i in range(n):
        f_3 = start_1 + start_2
        if f_3 > 4000000:
            break
        if (i-1) % 3 == 0:
            #print 'i', i
            #print 'f_3', f_3
            all = all + f_3
        start_1, start_2 = start_2, f_3
        #print f_3
    return all

print fabira(100)
