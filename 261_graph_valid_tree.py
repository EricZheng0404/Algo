from typing import List
from collections import defaultdict
"""
261. Graph Valid Tree

Mistakes:
1. I used a loop in the main function. But to check for connectivity, we only
need to start from one single node.

"""
class Solution1:
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
    
class Solution2:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # If this is a valid tree, the number of edges should 1 less than the number of nodes
        if len(edges) != n - 1:
            return False
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        self.visited = set()
        if not self.traverse(graph, 0, -1):
            return False
        return len(self.visited) == n

    def traverse(self, graph, node, parent):
        self.visited.add(node)
        for neighbor in graph[node]:
            # Because this is an undirected tree, so when we go from node A to node B, there must be 
            # also be node A in node B
            if neighbor == parent:
                continue
            # If any child is visited already, we need to return False
            if neighbor in self.visited:
                return False
            # If any children return False, the result also ripple back to the parent
            if not self.traverse(graph, neighbor, node):
                return False
        return True