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
        graph = self.makeGraph(prerequisites)
        self.n = numCourses
        # Keep track of all the nodes we have visited, we only change this once
        # in pre-order
        self.visited = [False] * self.n 
        # Keep track of one single path
        self.path = [False] * self.n
        self.isCycle = False # We should set True or False in here?
        for i in range(self.n):
            self.traverse(graph, 0)
        return not self.isCycle
    
    def traverse(self, graph, start):
        if self.isCycle is True:
            return
        if self.visited[start]:
            return 
        if self.path[start]:
            self.isCycle = True
            return
        # Pre-order position, this should be outside of the for loop
        self.visited[start] = True
        self.path[start] = True
        for i in range(len(graph[start])):
            self.traverse(graph, i + 1)
        # Post-order position, this should be outside of the for loop
        self.path[start] = False
        

    def makeGraph(self, prerequisites):
        return [[] for _ in range(len(prerequisites))]
