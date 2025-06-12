"""
LeetCode 210. Course Schedule II


"""

"""
The key is postorder traversal:
When a node is done visited all its neighbors, we add it to the postorder list.
So, the last node is the topo order is the first one to be added to the 
postorder list.
"""
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = self.buildGraph(numCourses, prerequisites)
        # To avoid repeated visited for a node
        self.visited = [False] * numCourses
        # To detect and avoid cycle for one path
        self.path = [False] * numCourses
        # To store the postorder traversal
        # When a node is done visited all its neighbors, we add it to the 
        # postorder list. So, the last node is the topo order is the first one 
        # to be added to the postorder list.
        self.preorder = []
        self.isCycle = False
        for i in range(numCourses):
            self.backtrack(graph, i)
        # reverse function is in place, it doesn't return anything.
        self.postorder.reverse()
        if self.isCycle:
            return []
        return self.postorder

    def backtrack(self, graph, start):
        if self.path[start]:
            self.isCycle = True
            return 
        if self.isCycle:
            return
        if self.visited[start]:
            return
        self.visited[start] = True
        self.path[start] = True
        for neighbor in graph[start]:
            self.backtrack(graph, neighbor)
        self.path[start] = False
        # Postorder traversal: when a node is done visited all its neighbors,
        # we add it to the postorder list. 
        self.postorder.append(start)
        
    def buildGraph(self, numCourses: int, prerequisites: List[List[int]]) -> List[List[int]]:
        # code as described above
        graph = [[] for _ in range(numCourses)]
        for edge in prerequisites:
            from_ = edge[1]
            to_ = edge[0]
            graph[from_].append(to_)
        return graph

sol = Solution()
n = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
print(sol.findOrder(n, prerequisites))