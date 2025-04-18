from typing import List
"""
LeetCode 797. All paths from source to target
Given a DAG of n nodes from 0 to n-1, find all possible paths from node 0 to 
node n - 1.

Example 1:
Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]

Exmple 2: 
Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
"""

class Solution:
    def __init__(self):
        self.result = []
        self.path = []

    def traverse(self, graph: List[List[int]], start):
        self.path.append(start) # The path always starts from just the start
        
        n = len(graph) # 4
        if start == n - 1: # if start == 3
            self.result.append(self.path[:])
            # If we reach here, we won't be able to each the 
            # end and touch on self.path.pop() at the end.
            self.path.pop() 
            return
        
        for v in graph[start]:
            self.traverse(graph, v)
        self.path.pop()

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.traverse(graph, 0)
        return self.result

# Example 1, expecting [[0,1,3],[0,2,3]]
sol = Solution()
graph1 = [[1,2],[3],[3],[]]
print("graph1: ", sol.allPathsSourceTarget(graph1))

# Exmaple 2, expecting [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
sol2 = Solution()
graph2 = [[4,3,1],[3,2,4],[3],[4],[]]
print("graph2: ", sol2.allPathsSourceTarget(graph2))
