# Enter your code here. Read input from STDIN. Print output to STDOUT

def sum_divisors(N):
    res = 0
    
    # check all numbers upto the square root
    for i in range(2, int(N**(0.5)) + 1):
        
        # divisor found
        if(N%i == 0): 
            
            # if its a square number, only count that number
            if(N//i == i): 
                res += i
            # otherwise count the number and its partner
            else:
                res += i + N//i
                
    # need to include 1 as it is a proper divisor
    return res + 1

# find all abundant numbers up to some limit
abundant = [0] * 28124
for N in range(1, 28123 + 1):
    if(sum_divisors(N) > N): 
        abundant[N] = 1
    
# handle each test case
for _ in range(int(input())):
    T = int(input())
    
    # numbers larger than this are guarenteed to be abundant
    if(T > 28123): 
        print("YES")
        
    # for all other numbers
    else:
        
        # search all pairs of numbers that sum to T
        found = False
        for i in range(1, T//2 + 1):
            
            # if we find a pair
            if(abundant[i] and abundant[T-i]):
                print("YES")
                found = True
                break
        
        # didn't find a pair
        if(not found): print("NO")
        
    
