#! /usr/bin/env python
#coding=utf-8

'''
思路是：
1、首先全部读出文件中的数据，返回结果为str
2、把“”全部替换掉
3、按照","，进行分割字符串，得到名字的列表
4、使用sorted排序
5、使用ord函数获取字母编码，减去64得到index
6、直接相加在乘以顺序即可
'''
def name_count():
    with open("p022_names.txt") as file:
        data = file.read()
    name_list = sorted(data.replace('"','').split(','))
    total = 0
    for name in range(len(name_list)):
        temp = 0
        #print name_list[name]
        for char in name_list[name]:
            #print char
            #print ord(char)
            temp += ord(char) - 64
        #print name_list[name],' is : ',temp
        total += temp*(name+1)
    print total
name_count()