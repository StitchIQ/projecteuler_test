#! /usr/bin/env python
#coding=utf-8

def sum_all(n):
    total = 1
    for i  in range(1,n+1):
        total *=i
    print total
    return total

sum_all(100)

def sum_num(n):
    s_num = str(n)
    all = 0
    for s in s_num:
        all += int(s)
    print all

sum_num(sum_all(100))