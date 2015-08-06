#! /usr/bin/env python
#coding=utf-8

def bidagelasi():
    for i in range(1,1000):
        for j in range(2+i,1000):
            for k in range(3+j,1000):
                if ( i + j + k == 1000) and ( i*i + j*j == k*k ) :
                    #and ( i*i + j*j == k*k )
                    print i , ' ', j  ,' ', k
                    print i*j*k
                    break

bidagelasi()
