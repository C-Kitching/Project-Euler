# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

# golden ratio 
phi = (1+5**.5)/2

def first_fib_with_N_digits(N):
    """Given a number of digits N, find the first first Fibonacci number with 
    that many digits
    The formula can be computed using a form a Binets formula for Fibonacci 
    numbers which says that Fn is the closest integer to phi^n/root(5), where
    phi is the golden ratio (1+root(5))/2
    The number of digits in Fn is given by Ceil(log10(Fn)) and it can be shown
    (see attached document) that this means the number of digits in Fn is
    Ceil(n*log(10)-1/2*log(5))
    With this we can show that the first n to contain N digits is
    Ceil((N-1+1/2*log10(5))/log10(phi))

    Args:
        N (int): number of digits
    
    Returns:
        n (int): first F_{n} with N digits
    """
    return math.ceil((N-1+0.5*math.log10(5))/math.log10(phi))
    
    
# handle all test cases
for _ in range(int(input())):
    N = int(input())
    print(first_fib_with_N_digits(N))