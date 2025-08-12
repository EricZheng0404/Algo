from typing import List
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = [False] * n
        res = 0
        for i in range(n):
            nodes = []
            if visited[i]:
                continue
            nodes.append(i)
            visited[i] = True
            self.traverse(graph, visited, i, nodes)
            # To calculate the number of edges we have
            sumEdges = 0
            for node in nodes:
                sumEdges += len(graph[node])
            if sumEdges == len(nodes) * (len(nodes) - 1):
                res += 1
        return res
    
    def traverse(self, graph, visited, start, nodes):
        for neighbor in graph[start]:
            if visited[neighbor]:
                continue
            visited[neighbor] = True
            nodes.append(neighbor)
            self.traverse(graph, visited, neighbor, nodes)


        