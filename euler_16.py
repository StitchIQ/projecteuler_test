#! /usr/bin/env python
#coding=utf-8

num = 2**1000
s = str(num)

total = 0
for a in s:
    total += int(a)

print total