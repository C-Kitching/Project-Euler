# Enter your code here. Read input from STDIN. Print output to STDOUT

def sieve(N):
    """Sieve of Erasthothenes to determine all primes up to N

    Args:
        N (int): upper bound 

    Returns:
        bool[], int[]: true if i is prime, a list of primes
    """

    # assume all numbers are primes
    is_prime = [True for i in range(N+1)]
    
    # check all numbers starting with 2
    # up to Sqrt(N)
    # becayse if xy = N and x>= Sqrt(N), it must be y<= Sqrt(N)
    # so all factors accounted for
    p = 2
    while(p*p <= N):
        
        # found a prime
        if(is_prime[p]):
            
            # set all mutiple of p as not prime
            for i in range(p*p, N+1, p):
                is_prime[i] = False
    
        p += 1
        
    # build prime array
    primes = []
    for i in range(2, N+1):
        if is_prime[i]: primes.append(i)
        
    return is_prime, primes
    
def count_consecutive_primes(a, b):
    """Starting from n=0, count the number of consecutive primes generated
    by the equation n**2+a*n+b

    Args:
        a (int): param
        b (int): param

    Returns:
        int: number of primes
    """
    
    count = 1
    n = 0
    
    # test all values of n from n=0
    while True:
        p = n**2 + a*n + b
        
        # if result is not prime then stop
        try:
            if not is_prime[p]:
                break
        except:
            print(p)
            exit(1)

        n += 1
        count += 1
        
    return count


# precompute all primes
is_prime, primes = sieve(10000000)
    
# read N
N = int(input())

max_primes = 0
max_a, max_b = 0, 0

# loop over all a and b values
for a in range(-N, N+1):
    for b in primes:
        
        count_primes = count_consecutive_primes(a,b)
        
        # new maximum found
        if count_primes > max_primes:
            max_primes = count_primes
            max_a = a
            max_b = b

# print result
print(max_a, max_b)
            
            
            
            
            
            
            
            
            
            