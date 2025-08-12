"""
You are given a map of a server center, represented as a m * n integer matrix 
grid, where 1 means that on that cell there is a server and 0 means that it is 
no server. Two servers are said to communicate if they are on the same row or 
on the same column.

Mistakes:
1. Always check the index first

Return the number of servers that communicate with any other server.

"""
from typing import List
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        rowNum = [0] * m
        colNum = [0] * n
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rowNum[i] += 1
                    colNum[j] += 1
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (rowNum[i] > 1 or colNum[j] > 1):
                    res += 1
        return res