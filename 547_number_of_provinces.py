from typing import List
"""
547. Number of Provinces
"""
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.n = len(isConnected)
        self.visited = set()
        res = 0
        for i in range(self.n):
            if i in self.visited:
                continue
            # Whenever we find a new start city we've never visited, we know there's another 
            # new province.
            res += 1
            self.visited.add(i)
            self.dfs(isConnected, i)
        return res 

    def dfs(self, isConnected, city):
        for neighbor in range(self.n):
            if isConnected[city][neighbor] == 1 and neighbor not in self.visited:
                self.visited.add(neighbor)
                self.dfs(isConnected, neighbor)
            
