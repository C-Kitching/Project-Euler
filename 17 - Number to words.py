
digits = ['','One ','Two ','Three ','Four ','Five ','Six ','Seven ','Eight ','Nine ',
          'Ten ','Eleven ','Twelve ','Thirteen ','Fourteen ','Fifteen ','Sixteen ','Seventeen ','Eighteen ','Nineteen ']
two_d = ['','','Twenty ','Thirty ','Forty ','Fifty ','Sixty ','Seventy ','Eighty ','Ninety ']
powers = ["", "Thousand ", "Million ", "Billion ", "Trillion "]

def tens(N):
    """Convert a 10s number to words"""
    if N==0: return ""
    if N < 20: return digits[N]
    else: return two_d[N//10] + digits[N%10]

def hundred(N):
    """Convert a 100s number to words"""
    if N==0: return ""
    if N < 100: return tens(N%100)
    else: return digits[N//100] + "Hundred " + tens(N%100)

def number_to_words(N):
    """Convert a number to words"""

    # edge case
    if N == 0: return "Zero"

    c = 0 # track powers
    word = "" # word to build

    while N > 0:
        h = N%1000
        if h != 0: word = hundred(h) + powers[c] + word
        N = N//1000
        c += 1

    return word.rstrip()


for _ in range(int(input())):
    N = int(input())
    print(number_to_words(N))