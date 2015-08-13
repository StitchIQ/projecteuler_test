#! /usr/bin/env python
#coding=utf-8

from decimal import *
getcontext().prec = 1000

def find_round(n):
    for i in range(2,n):
        #print "%.17f" %(1.0/i)
        s = Decimal(1)/Decimal(i)
        print s

def find_same(s):
    s_len = len(s)
    if s_len < 3:
        return None
    for i in range(s_len):
        if s.count(s[i]) == s_len:
            return '(%d)'%s[i]
        for j in range(s.count(s[i])):
            index = s.find(s[i],i+1)
            for k in range(1, index - i+1):
                if s[i:i+k] == s[index:index+k]:
                    print s[i:i+k]
                else:
                    break
            index = s.find(s[i],index+1)

        #if s.count[i] < s_len :
        #    s.count(s[i:index])
            
find_same('123123123')            
#print '3456789'[0:4]
#find_round(1000)