#! /usr/bin/env python
#coding=utf-8

def sqrt_num(n):
    add = sum(range(1,n+1))**2
    print add
    sqrt = sum(map(lambda x: x ** 2, range(1,n+1)))
    print sqrt
    print add-sqrt
    
sqrt_num(100)