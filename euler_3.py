#! /usr/bin/env python
#coding=utf-8

def find_max_factors2(n):
    half = n / 2
    prime = []
    i = 2
    while True:
        if( n % i ==0 and is_prime(i)):
            prime.append(i)
            n = n/i
            print "n is :%d , i iss: %d" %(n,i)
            i = 2
        i = i + 1
        if n <=2:
            break
    return prime

def is_prime(n):
    for i in range(2, n/2):
        if (n % i == 0 ):
            return False
    return True

def prime_list(n):
    prime = [1]
    t = 2
    if is_prime(n):
        return [1,n]
    for i in range(2, n/2+1):
        if (n % t == 0):
            prime.append(t)
            n /= t
            if is_prime(n):
                prime.append(n)
                break
            #print n
            #print prime
            t = 2
        else:
            t += 1
    #print prime
    return prime

#print is_prime(49)
#print find_max_factors2(13195)
#print find_max_factors2(100)
print find_max_factors2(600851475143)