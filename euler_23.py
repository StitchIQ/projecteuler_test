#! /usr/bin/env python
#coding=utf-8


def get_div(num):
    div = [1]
    i = 2
    while True:
        if i*i <=num:
            if num%i == 0:
                div.append(i)
                if num/i !=i:
                    div.append(num/i)
            i+=1
        else:
            break
    #print div
    return sum(div)

#print get_div(12)

def find_over():
    over_list = []
    for i in range(1, 28124):
        if i < get_div(i):
            over_list.append(i)
    print len(over_list)
    over_num = []
    for i in over_list:
        for j in over_list:
            temp = i+j
            if temp < 28124:
                over_num.append(temp)
                #print i," ",j
    over_num = list(set(over_num))
    print len(over_num)
    length = len(over_num)

    '''
    for i in range(length):
        if over_num[i] + length - i-1 == over_num[-1]:
            print over_num[i]
            print 'i is :' ,i
            break

    ss = 0
    for i in range(length-1,0,-1):
        if over_num[i] + ss != over_num[-1]:
            print over_num[i]
            print 'ii is :' ,i
            break
        ss += 1
    '''
    total = 0
    for i in range(1,28124):
        if i not in over_num:
            total += i
            #print 'i is : ',i
    print 'total is : ',total


find_over()
#4179871