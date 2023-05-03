# Enter your code here. Read input from STDIN. Print output to STDOUT

# handle each test case
T = int(input())
for _ in range(T):
    N = int(input())
    
    # perform operation and convert to string
    power = str(2**N)
    
    # loop through digits and add to result
    res = 0
    for digit in power:
        res += int(digit)
        
    print(res)