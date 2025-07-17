class Solution:
    """
    As long as the number is a 

    Question:
    1. How to deal with labels starting from 1
       n + 1
    
    """
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        # To control the bi-color of two groups
        self.colors = [False] * (n + 1)
        # To avoid infinite group
        self.visited = [False] * (n + 1)
        # The final result
        self.res = True
        # Set up a bi-directional graph
        # The reason why it's bi-directional is because we need all the nodes
        # connected
        graph = [[] for _ in range(n + 1)]
        for dislike in dislikes:
            u = dislike[0]
            v = dislike[1]
            graph[u].append(v)
            graph[v].append(u)
        for node in range(1, n + 1):
            if not self.visited[node]:
                self.traverse(graph, node)
        return self.res

    def traverse(self, graph, node):
        # If we know the result is False, there's no need to further traverse
        if not self.res:
            return
        self.visited[node] = True
        for neighbor in graph[node]:
            # If neighbor has been visited before, we check its color
            if self.visited[neighbor]:
                if self.colors[neighbor] == self.colors[node]:
                    self.res = False
                    return
            # If the neighbor has not been visited 
            else:
                self.colors[neighbor] = not self.colors[node]
                self.visited[neighbor] = True
                # When the node has not been visited, we need to traverse it too
                self.traverse(graph, neighbor)
