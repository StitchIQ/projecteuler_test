#! /usr/bin/env python
#coding=utf-8

def is_prime(n):
    for i in range(2, n/2+1):
        if (n % i == 0 ):
            return False
    return True

print is_prime(13)

def find_prime(n):
    i = 0
    a = 2
    while True:
        if is_prime(a):
            i += 1
            print a
            print i
            if i == n:
                break
        a += 1
        
    print a

find_prime(10001)