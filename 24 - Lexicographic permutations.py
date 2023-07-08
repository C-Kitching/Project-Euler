# Enter your code here. Read input from STDIN. Print output to STDOUT

word = "abcdefghijklm"

# convert number from decimal to factorial form
def convert_decimal_to_factorial_form(N):
    length = len(word)
    i = 1
    factorial_form = [0]*length
    while N != 0:
        factorial_form[length - i] = N%i
        N //= i
        i += 1
        if(N==1):
            factorial_form[length - i] = 1
            break
    return factorial_form

# determine the Nth permutation of a word
def calculate_N_permutation(N_factorial_form, word):
    
    arr = list(word)
    res = "" # nth permutation to build
    
    # go through each number in the factorial form
    for i in range(len(N_factorial_form)):
        res += arr.pop(N_factorial_form[i])
        
    return res
    
        
        
# read each test case
for _ in range(int(input())):
    N = int(input())
    
    # convert each number to factorial form
    N_factorial_form = convert_decimal_to_factorial_form(N-1)

    # determine Nth permutation
    N_permutation = calculate_N_permutation(N_factorial_form, word)
    
    print(N_permutation)
    