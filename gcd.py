# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 18:51:24 2021

@author: Siddharth Ranganatha
"""


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

if __name__ == "__main__":
    print(gcd(12,8))
