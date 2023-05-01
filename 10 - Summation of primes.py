#!/bin/python3

import sys

def sieve(N):
    """
    Algo to find all primes less than N and their sums to an index
    
    Args: 
        N (int)
        
    Returns:
        Res (int[]) : prime numbers
        sums (int[]) : sum of prime numbers upto index i
    """
    # assume all numbers prime
    prime = [True for i in range(N+1)]
    sums = [0 for i in range(N+1)]
    
    p = 2
    while(p*p <= N):
        # found a prime
        if(prime[p]):
            # update all multiple of p
            for i in range(p*p, N+1, p):
                prime[i] = False
        p += 1
    
    # store all primes
    res = []
    for p in range(2, N+1):
        if prime[p]: 
            res.append(p)
            sums[p] += p
        sums[p] += sums[p-1]   
        
    return res, sums
        
# precompute all primes 
primes, sums = sieve(1000000)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
    print(sums[n])
    
    
    
    
    
    
    
    
    
    
