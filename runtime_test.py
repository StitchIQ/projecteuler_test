#! /usr/bin/env python
#coding=utf-8
from datetime import datetime

def test_time(func):
    def _run_time(n):
        s=datetime.now()
        print "start running time is :", s
        func(n)
        e=datetime.now()
        print "end   running time is :", e
        print "Total running time is :", e-s
    return _run_time