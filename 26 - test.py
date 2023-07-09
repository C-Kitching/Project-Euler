# Enter your code here. Read input from STDIN. Print output to STDOUT

#https://oeis.org/A007732
# This seems relevant

# determine all reciprtical decimals and their length
def find_cycle_lengths():

    reciprocal_cycle_lengths = {}

    for d in range(2, 10001):

        n = 1 # numerator
        r = 1%d # remainder
        
        # build the decimal part
        reciprical_decimal = []
        
        # while remainder is not zero we can build decimal
        while r != 0:
            r *= 10
            
            new_decimal = r//d
            
            # if we ever find the same number twice
            # all numbers between the numbers must repeat
            if(r//d in reciprical_decimal):
                reciprocal_cycle_lengths[d] = len(reciprical_decimal) - reciprical_decimal.index(new_decimal)
                break
            
            r %= d
            reciprical_decimal.append(new_decimal)
        
    return reciprocal_cycle_lengths
    
# comput length of cycle for first 
reciprocal_cycle_lengths = find_cycle_lengths()

# handle each test case
for _ in range(int(input())):
    N = int(input())

    max_length = 0
    for n, l in reciprocal_cycle_lengths.items():
        if n > N:
            print(res)
            break
        if l > max_length:
            max_length = l
            res = n

    
    
    
    
    
    
    
    
    
