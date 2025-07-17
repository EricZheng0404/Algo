from typing import List
class Solution:
    """
    We traverser through all the nodes in the graph since the graph may not be connected.
    """
    def isBipartite(self, graph: List[List[int]]) -> bool:
        self.n = len(graph)
        # To keep track of the colors: True and False represent two color
        self.colors = [False] * self.n
        # To avoid infinite loop
        self.visited = [False] * self.n
        self.res = True

        for node in range(self.n):
            # Do we need to check self.visited here?
            # self.visited[node] = True
            if not self.visited[node]:
                self.traverse(graph, node)

        return self.res

    def traverse(self, graph, node):
        # Base case: there's no need to check if we know it's not a bipartite
        if not self.res:
            return

        for neighbor in graph[node]:
            # If the neighbor is visited, we need to check if its color is different
            if self.visited[neighbor]:
                if self.colors[neighbor] == self.colors[node]:
                    self.res = False
                    return
            # If the neighbor is not visited, we set it to the opposite color of
            # the node.
            else:
                self.colors[neighbor] = not self.colors[node]
                self.visited[neighbor] = True # I forgot set the visited node to True
                self.traverse(graph, neighbor) # To initialize the DFS