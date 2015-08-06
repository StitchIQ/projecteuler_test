#! /usr/bin/env python
#coding=utf-8

def find_num():
    i = 1
    while True:
        li=map(lambda a:i%a, range(1,21))
        print li
        if len(set(li)) == 1:
            break
        i +=20
        print i
        
    print i
    return i

find_num()



def find_num4():
    i = 1
    for k in (range(1, 21)):
        if i % k > 0:
            for j in range(1, 21):
                if (i*j) % k == 0:
                    i *= j
                    break
    print i

find_num4()    