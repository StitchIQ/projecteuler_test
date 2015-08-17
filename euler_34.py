#! /usr/bin/env python
#coding=utf-8

def jiecheng(n):
    if n == 1 or n == 2:
        return n

    multi = 1
    for i in range(1,n+1):
        multi *= i

    return multi

#print jiecheng(9)*9

#print sum(map(jiecheng,range(1,10)))

def str_int_list(n):
    s = str(n)
    ll =[]
    [ll.append(int(i)) for i in s]
    return ll

print str_int_list(409113)
#409113
#3265920
print 145 == sum(map(jiecheng,str_int_list(145)))

for i in range(3,3265920):
    if i == sum(map(jiecheng,str_int_list(i))):
        print i

#40585