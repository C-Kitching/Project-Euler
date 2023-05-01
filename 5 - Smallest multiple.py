#!/bin/python3

import sys

def gcd(a, b):
    """Find gcd of 2 numbers with Euclid"""
    while b:
        a, b = b, a%b
    return a

def lcm(a, b):
    """ Find lcm of 2 numbers"""
    return a*b // gcd(a, b)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
    # edge case
    if n == 1: print(1)
    
    else:
        # find lcm of N numbers
        for i in range(2, n+1):
            if i == 2: prev = lcm(1, 2)
            else: prev = lcm(prev, i)
            
        print(prev) 
