"""
LeetCode 207. Course Schedule

There are a total of numCourses courses you have to take, labeled from 0 to
numCourses - 1. You are given an array prerequisites where prerequisites[i] =
[ai, bi] indicates that you must take course bi first if you want to take course
ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first
take course 1.

Return true if you can finish all courses. Otherwise, return false.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true

Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false

Constraints:
1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
"""
from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = self.makeGraph(prerequisites, numCourses)
        self.n = numCourses
        # Keep track of all the nodes we have visited, we only change this once
        # in pre-order
        self.visited = [False] * self.n 
        # Keep track of one single path
        self.path = [False] * self.n
        self.isCycle = False # We should set True or False in here?
        for i in range(numCourses):
            self.traverse(graph, i) # Darn it! I put 0 here
        return not self.isCycle
    
    def traverse(self, graph, start):
        # Early termination: if we have found a cycle, there's no need to traverse
        # the rest of the graph.
        if self.isCycle:
            return
        # We should set this condition before check visited becuase we need to
        # set isCycle to True if we find a cycle first rather than found visited
        # and return without setting self.isCycle to True.
        if self.path[start]:
            self.isCycle = True
            return
        if self.visited[start]:
            return 
        # Pre-order position, this should be outside of the for loop
        self.visited[start] = True
        self.path[start] = True
        for to_ in graph[start]:
            self.traverse(graph, to_)
        # Post-order position, this should be outside of the for loop
        self.path[start] = False
        return False

    def makeGraph(self, prerequisites, numCourses):
        graph = [[] for _ in range(numCourses)]
        for edge in prerequisites:
            from_ = edge[1]
            to_ = edge[0]
            graph[from_].append(to_)
        return graph

sol = Solution()
print(sol.canFinish(2, [[1,0]]))