#! /usr/bin/env python
#coding=utf-8

'''
思路：
计算四个角的值：
右上：(2i+1)**2   其中n为 0，1，2 ；最大值为 n/2+1
左上: 右上减去2i
左下：右上减去4i
右下：右上减去6i

'''
def sum_sqar(n):
    total = 1
    for i in range(1, n ,1):
        print i
        total += (2*i +1)**2*4 -12*i
        print total

sum_sqar(1001/2+1)
#669171001
