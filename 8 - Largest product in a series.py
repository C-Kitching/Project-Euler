#!/bin/python3

import sys

def digit_product(n):
    """
    Calculate product of digits of a number
    
    n (int) : number
    """
    product = 1
    while(n):
        product *= n%10
        n = n//10
    return product 

def main(): 
    
    # loop test cases
    t = int(input().strip())
    for a0 in range(t):
        # read data for each test case
        n,k = input().strip().split(' ')
        n,k = [int(n),int(k)]
        num = input().strip()
        
        # cast num to string
        s = str(num)
        
        res = 0
        
        # check each sub num
        for i in range(0, len(s) - k + 1):
            sub_num = int(s[i:i+k])
            
            # updata res if bigger found
            res = max(res, digit_product(sub_num))
            
        print(res)
        
if __name__ == "__main__":
    main()
