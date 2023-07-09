# Enter your code here. Read input from STDIN. Print output to STDOUT

# In order to do this we make use of the factorial number system
# For example the number 463 in base 10 can be weitten as 3:4:1:0:1:0, meaning 3_{5}4_{4}1_{3}0_{2}1_{1}0_{0}
# which is 3*5! + 4*4! + 1*3! + 0*2! + 1*1! + 0*0! = 463
# Note that the rightmost digit as at most 0, the second can be 0,1, the third 0,1,2 etc. 
# Numbers in factorial form directly correspond to permutations
# For example if you want the 2982nd permutation of the number 0-6, you first convert 2982 to factorial form 4:0:4:1:0:0:0
# The first number is at the 4th position of (0123456) i.e 4
# Then you remove that number so we have (012356)
# The next number is at the 0 position of (012356) i.e 0
# We repeat like this to build up 4062135, the 2982nd permutation of the numbers 0-6

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
    