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
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        path = []
        self.traverse(graph, 0, len(graph) - 1, res, path)
        return res
    
    def traverse(self, graph, source, target, res, path):
        # when the source is the target, we need to first add it to the path,
        # then return the path
        path.append(source)
        if source == target:
            res.append(path[:])
        for neighbor in graph[source]:
            self.traverse(graph, neighbor, target, res, path)
        path.pop()