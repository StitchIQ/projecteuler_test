#! /usr/bin/env python
#coding=utf-8

from decimal import *
getcontext().prec = 2000

def find_round(n):
    max_sub = ''
    max_len = 0
    index = 0
    ss = ''
    print 'start'
    for i in range(2,n):
        #print "%.17f" %(1.0/i)
        s = Decimal(1)/Decimal(i)
        #print str(s)
        temp_sub, temp_len = find_same(str(s))
        print i,' s ',temp_sub
        if temp_len > max_len:
           max_sub = temp_sub
           max_len = temp_len
           index = i
           ss = s
        #print 'i is :: ',i
    print ss
    print 'i is %d, sub_str is %s'%(index,max_sub)



def find_same(s):
    s = s.split('.')[-1]
    s_len = len(s)
    if s_len < 3:
        return None, None

    sub_count = 0
    sub_len = 0
    sub_str = ''
    for i in range(s_len):
        if s.count(s[i]) == s_len:
            return '(%s)'%s[i],None
        index = s.find(s[i],i+1)
        for j in range(s.count(s[i])):
            for k in range(1, index - i +1):
                if s[i:i+k] == s[index:index+k]:
                    #print s[i:i+k]
                    if len(s[i:i+k]) > sub_len:
                        sub_count = s.count(s[i:i+k])
                        sub_len = len(s[i:i+k])
                        sub_str = s[i:i+k]
                else:
                    break
            index = s.find(s[i],index+1)
            #print index
    #print 'str :', sub_str, ' count is :', sub_count, 'len is: ',sub_len
    return sub_str, sub_len

#find_same('12123412341234')
#find_same('111111111111')
#print '3456789'[0:4]
#find_round(7)
#for i in range(2,5):
#    print i
print Decimal(1)/Decimal(7)
#find_same(str(Decimal(1)/Decimal(7)))