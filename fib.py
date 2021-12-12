# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 18:51:24 2021

@author: Siddharth Ranganatha
"""

def fib(n):
    return n if n in [0, 1] else fib(n - 2) + fib(n - 1)

for i in range(10):
    print(fib(i))