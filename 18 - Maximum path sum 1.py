# Enter your code here. Read input from STDIN. Print output to STDOUT

def dfs(tree, depth, col, max_depth, curr_path):
    """DFS the tree to find max path from the root node"""
    
    # add the current node
    curr_path += tree[depth][col] 
    
    # if at bottom, return the path length
    if depth == max_depth:
        return curr_path
    
    # else return the max path length from exploring 2 child nodes
    else:
        return max(dfs(tree, depth + 1, col, max_depth, curr_path), 
                   dfs(tree, depth + 1, col + 1, max_depth, curr_path))

# handle each test case
for _ in range(int(input())):
    N = int(input())
    
    # read in the tree
    tree = []
    for _ in range(N):
        tree.append(list(map(int, input().split(' '))))
        
    # find the max path length
    max_path = dfs(tree, 0, 0, N-1, 0)
    print(max_path)