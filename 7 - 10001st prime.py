#!/bin/python3

import sys

def sieve():
    """Calculate all primes up to 1000005"""
    
    # assume all  numbers are prime
    n = 1000005
    prime = [True for i in range(n+1)]
    
    # determine which are primes
    p = 2
    while(p*p <= n):
        
        # found a prime number
        if(prime[p]):
            
            # set all multiples of p as not prime
            for i in range(p*p, n+1, p):
                prime[i] = False
                
        p += 1
        
    # build prime array
    res = []
    for p in range(2, n+1):
        if prime[p]: res.append(p)
    
    return res


# pre compute all primes
primes = sieve()
    
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(primes[n-1])
