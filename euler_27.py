#! /usr/bin/env python
#coding=utf-8
import datetime

'''
思路：
1、根据 n*n + a*n + b从0开始有最多的质数，则b必须为质数
2、从a=-999 b为1000以内的质数暴力计算即可
3、优化：a必须为奇数，则步进可以为2
'''

def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def find_num():
    max_prime = 0
    max_a = 0
    max_b = 0
    b_list = [n for n in range(2,1000) if is_prime(n)]
    for b in b_list:
        for a in range(-999, 1000, 1):
            n = 0
            temp = 0
            while (n**2+ a*n + b) > 0 and is_prime(n**2+ a*n + b):
                n += 1
            if n > max_prime:
                max_a, max_b = a, b
                max_prime = n
    print max_a , ' end ' ,max_b, ' prime is :' ,max_prime
    print 'result is : ', max_a * max_b

start = datetime.datetime.now()
print start
find_num()
print datetime.datetime.now() - start
#-59231 = -61 * 971