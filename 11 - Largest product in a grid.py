#!/bin/python3

import sys


grid = []
for grid_i in range(20):
    grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
    grid.append(grid_t)

max_sum = 0 
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if(i < 17):
            a = grid[i][j] * grid[i+1][j] * grid[i+2][j] * grid[i+3][j]
        if(j < 17):
            b = grid[i][j] * grid[i][j+1] * grid[i][j+2] * grid[i][j+3]
        if(i < 17 and j < 17):
            c = grid[i][j] * grid[i+1][j+1] * grid[i+2][j+2] * grid[i+3][j+3]
            d = grid[i][19-j] * grid[i+1][18-j] * grid[i+2][17-j] * grid[i+3][16-j]
        
        max_sum = max(max_sum, max(a, b, c, d))
        
print(max_sum)
