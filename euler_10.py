#! /usr/bin/env python
#coding=utf-8
from runtime_test import test_time

def is_prime(n):
    if n <= 1:  
        return False 
    i = 2
    while i*i <= n:  
        if n % i == 0:  
            return False 
        i += 1 
    return True

def is_prime2(n):
    for i in range(2, n/2+1):
        if (n % i == 0):
            return False
    return True

@test_time
def sum_prime(m):
    sum = 0
    for i in range(2, 2000000):
        if is_prime(i):
            sum += i
    print sum

sum_prime(10)