# Enter your code here. Read input from STDIN. Print output to STDOUT

def zellers_congruence(day, month, year):
    """Calculate the week day on a given date"""
    
    # Jan and Feb are month 13 and 14 of the previous year
    if month == 1:
        month = 13
        year -= 1    
    if month == 2:
        month = 14
        year -= 1
    
    q = day
    m = month
    k = year % 100
    j = year // 100
    
    h = (q + 13 * (m + 1) // 5 + k + k // 4 + j // 4 + 5 * j)%7
    
    return h

def check_date_order(date_1, date_2):
    """Check if date_1 is earlier than or equal to date_2"""
    # compare years
    if date_1[0] < date_2[0]: return True
    elif date_1[0] == date_2[0]:
        # compare months
        if date_1[1] < date_2[1]: return True
        elif date_1[1] == date_2[1]:
            # compare days
            if date_1[2] <= date_2[2]: return True 
    return False

for _ in range(int(input())):
    
    # read in data
    date_1 = list(map(int, input().split(" ")))
    date_2 = list(map(int, input().split(" ")))
    
    num_sundays = 0
    
    # while the start date is earlier than the end date
    while check_date_order(date_1, date_2):
        
        # if first of month
        if(date_1[2] == 1):
            # if sunday
            if(zellers_congruence(date_1[2], date_1[1], date_1[0]) == 1):
                num_sundays += 1
            
        # move start date to first of next month
        date_1[2] = 1
        date_1[1] += 1
        if date_1[1] > 12:
            date_1[1] = 1
            date_1[0] += 1
    
    print(num_sundays)
    
    