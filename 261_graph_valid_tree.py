from typing import List
"""
261. Graph Valid Tree
"""
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: return False
        adj_list = [[] for _ in range(n)]
        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])
        seen = {0}
        stack = [0]
        
        while stack:
            node = stack.pop()
            for neighbour in adj_list[node]:
                if neighbour in seen:
                    continue
                seen.add(neighbour)
                stack.append(neighbour)
        
        return len(seen) == n