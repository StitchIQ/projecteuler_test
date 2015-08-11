#! /usr/bin/env python
#coding=utf-8

def get_div(num):
    div = [1]
    i = 2
    while True:
        if i*i <=num:
            if num%i == 0:
                div.append(i)
                div.append(num/i)
            i+=1
        else:
            break
    return sum(div)

print get_div(220)


def get_Amicable():
    total = 0
    for i in range(10001):
        temp = get_div(i)
        if (temp != i) and get_div(temp) == i:
            total += i
            print i , '...' ,temp
    print total

get_Amicable()