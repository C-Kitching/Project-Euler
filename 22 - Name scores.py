# Enter your code here. Read input from STDIN. Print output to STDOUT

def calculate_score(names, name):
    
    # find position in list
    pos = names.index(name) + 1
    
    # calculate name worth
    worth = 0
    for c in name:
        worth += ord(c) - ord('A') + 1
        
    # calculate final score
    return pos*worth


# read the names
names = []
for _ in range(int(input())):
    names.append(str(input()))
    
# sort the names alphabetically
names = sorted(names)

# read queries
for _ in range(int(input())):
    print(calculate_score(names, str(input())))
