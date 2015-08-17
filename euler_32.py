#! /usr/bin/env python
#coding=utf-8
from datetime import datetime

'''
思路：
1、因100×100 =10000，故总位数和为9的，相乘结果最大为四位数
2、把每个乘数int转换为str，计算乘数和乘积的总位数是否等于9
3、如果等于9，则对于乘数和乘积的每个数据转换为字符列表
4、用1-9的全集减去字符列表，如果全集的长度为0，则符合条件
5、list去重使用set函数
'''


digital = [1,2,3,4,5,6,7,8,9]

def str_int_list(n):
    s = str(n)
    ll =[]
    [ll.append(int(i)) for i in s]
    return ll

#print len(str(100))
def find_pandigital():
    result = []
    for i in range(2,9999):
        for j in range(2,9999):
            tt = i*j
            if tt > 9999 :
                continue
            if len(str(i)) + len(str(j)) + len(str(tt)) == 9:
                i_list = str_int_list(i)
                j_list = str_int_list(j)
                total = str_int_list(tt)
                
                res = list(set(digital)-set(i_list)-set(j_list)- set(total))
                
                if len(res) == 0:
                    print i,' * ',j, ' = ',tt
                    result.append(tt)
    print result
    print sum(set(result))

start =  datetime.now()
find_pandigital()
print datetime.now() -start