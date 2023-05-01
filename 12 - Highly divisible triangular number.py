# Enter your code here. Read input from STDIN. Print output to STDOUT

def sieve(N):
    """
    Find all primes up to N
    """
    primes = [True for i in range(N+1)]
    p = 2
    while(p*p < N):
        if(primes[p]):
            for i in range(p*p, N+1, p):
                primes[i] = False
        p += 1
        
    res = []
    for p in range(2, N+1):
        if(primes[p]): res.append(p)
        
    return res

def num_divisors(N, primes):
    """
    Determine the number of divisors N has using primes
    If N can be written a^i*b^j*c^k....
    then it has (i+1)*(j+1)*(k+1)... divisors
    """
    res = 1
    for p in primes:
        count = 0
        while(N % p == 0):
            N /= p
            count += 1
        if(count != 0):
            res *= (count + 1)
    if(N > 1): res *= 2
    return res
            
def find_triangle_nums(N):
    """
    Calculate all triangle numbers up to N
    """
    return [n*(n+1)//2 for n in range(1, N+1)]
    
def find_triangle_divisors(triangles, primes):
    """
    Determine the number of divisors of all triangle numbers
    When we encounter a number that has more divisors we store it
    """
    res = {}
    d_max = 0
    for t in triangles:
        d = num_divisors(t, primes)
        if d > d_max:
            d_max = d
            res[d_max] = t
    return res
    
# precomupte everything
primes = sieve(1000)
triangles = find_triangle_nums(100000)
triangle_divisors = find_triangle_divisors(triangles, primes)

# read in input
T = int(input())
for _ in range(T):
    N = int(input())
    
    # loop over dictionary until we find the first triangle with more than N divisors
    for key, value in triangle_divisors.items():
        if key > N: 
            print(value)
            break
