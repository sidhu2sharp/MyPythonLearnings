# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 18:51:24 2021
@description: Program to find most frequently occuring value (smallest if there is a contention)
@author: Siddharth Ranganatha
"""
from collections import Counter

n = int(input())
s = input()
lst = s.split()
lst.sort()
a = sorted(Counter(lst).items(), key=lambda x: x[1], reverse=True)
print(a[0][0])
