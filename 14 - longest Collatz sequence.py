# Enter your code here. Read input from STDIN. Print output to STDOUT

cache_limit = int(5e6)
res = [0] * cache_limit
memo = [0] * cache_limit
current_max = [1, 0] # start point and path length of the longest path found so far

# check all start points
for start in range(2, cache_limit):
    
    position = start  # set the start point
    path = []  # track path from start point
    collatz_len = 1
    
    # perform the iteration until the absorbing state
    while(position != 1):
        
        # store current position in path
        path.append(position)
        
        # if we've seen the number before, we know the length 
        if position < cache_limit and memo[position] != 0:
            collatz_len = memo[position] + len(path) - 1
            break
        
        # update rules
        if(position%2 == 0): position //= 2
        else: position = 3*position + 1
        
        
    # store all point in path to memory
    if(collatz_len == 1): collatz_len = len(path)
    for i, p in enumerate(path):
        if(p < cache_limit):
            memo[p] = collatz_len - i
    
    # if we have found a new maximum length path
    if(collatz_len >= current_max[1]):
        current_max = [start, collatz_len]
        res[start] = start
    else:
        res[start] = current_max[0]
    
# read input and print result
T = int(input())
for _ in range(T):
    N = int(input())
    print(res[N])
        
        
