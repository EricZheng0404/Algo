from typing import List
from collections import deque
# Adjacency List Implementation: Directed Weight Graph
class WeightedDigraph:
    # A class nested under WeightDigraph
    class Edge:
        def __init__(self, to: int, weight: int):
            self.to = to
            self.weight = weight
        
        def __repr__(self) -> str:
            return f"To: {self.to}, weight: {self.weight}"
    
    def __init__(self, n: int):
        # typing (on the left) and also initialization (on the right)
        self.graph: List[List[WeightedDigraph.Edge]] = [[] for _ in range(n)] 


    def __repr__(self) -> str:
        result = []
        for i, edges in enumerate(self.graph):
            edge_strs = [f"{edge.to}({edge.weight})" for edge in edges]
            result.append(f"{i}: {', '.join(edge_strs)}")
        return "\n".join(result)
    
    # Add an edge to the adjacency list
    def addEdge(self, from_: int, to: int, weight: int):
        vertex = self.graph[from_]
        # We need to append the new edge to the list.
        # I was thinking using the from as index, but it will defeat the purpose
        # of using adjancency list to save space.
        vertex.append(self.Edge(to, weight)) 
    
    def removeEdge(self, from_: int, to: int):
        vertex = self.graph[from_]
        for edge in vertex:
            if edge.to == to:
                vertex.remove(edge)
                return
    
    def hasEdge(self, from_: int, to: int):
        try:
            for edge in self.graph[from_]:
                if edge.to == to:
                    return True
            return False
        except IndexError as e:
            print(f"Index out of range: {e}")
        except ValueError as e:
            print(f"Value error: {e}")
    
    def weight(self, from_: int, to: int) -> int:
        vertex = self.graph[from_]
        for edge in vertex:
            if edge.to == to:
                return edge.weight
        raise ValueError("No such edge") 
    
    # return all neighbors of a edges
    def neighbors(self, v: int):
        return self.graph[v] 
    
    def size(self):
        return len(self.graph)
    
    def _in_range(self, vertex):
        length = len(self.graph)
        if vertex >= length:
            raise IndexError("Index out of range")


# DFS traversal
# Traversing all nodes
def traverse(graph: WeightedDigraph, s, visited):
    # This is a defensive check, validating the vertex s is within valid bound
    if s < 0 or s >= graph.size(): 
        return
    # This is the base case. If s is visited already, we should immediately return.
    if (visited[s]): 
        return
    visited[s] = True
    # This is pre-order traversal
    print(f"visit: {s}") 
    for e in graph.neighbors(s): # neighbors() function return bunch of edges
        traverse(graph, e.to, visited) # We continue with the children(!!)

# Traversing all paths
# Find the path to the target
# Store all the possible paths to the destination
def findTarget(graph: WeightedDigraph, src, dest, on_path, path, all_paths):
    if src < 0 or src >= graph.size():
        return 
    # print(on_path)
    if on_path[src]:
        return 
    # Pre-order position
    on_path[src] = True # To guarantee there's no cyle in one path
    path.append(src)
    if src == dest:
        # When we backtrack and pop elements from the path, this shallow copy ensures that path added won't change
        all_paths.append(path[:])
    for e in graph.neighbors(src):
        findTarget(graph, e.to, dest, on_path, path, all_paths)
    path.pop()
    on_path[src] = False

# Implmentation 1: BFS the tree, we print out the node val when we visit it
# It doesn't record the steps
def dfs1(graph: WeightedDigraph, s: int):
    visited = [False] * graph.size()
    q = deque([s])
    visited[s] = True
    while q:
        cur = q.popleft()
        print(cur)
        for v in graph.neighbors(cur): 
            if visited[v.to] == False:
                q.append(v.to)
                visited[v.to] = True

# Implementation 2: BFS tree
# It reflect the steps
def dfs2(graph: WeightedDigraph, s: int):
    visited = [False] * graph.size()
    q = deque([s])
    visited[s] = True
    step = 0

    while q:
        sz = len(q)
        for _ in range(sz):
            cur = q.popleft()
            print(f"step: {step}, val is {cur}") # I set this to s before
            for v in graph.neighbors(cur): # I set this to s before
                if not visited[v.to]:
                    q.append(v.to)
                    visited[v.to] = True # I set this False before
        step += 1

# Implementation 3: BFS tree
# It reflects cumulative weight
def dfs3(graph: WeightedDigraph, s: int):
    class State:
        def __init__(self, node, weight):
            self.node = node
            self.weight = weight # I should

    visited = [False] * graph.size()
    q = deque()
    weight = 0
    q.append(State(s, weight))
    visited[s] = True 

    while q: 
        sz = len(q)
        for _ in range(sz):
            cur = q.popleft() # This is a state
            print(f"Node is {cur.node}, weight is {cur.weight}")
            for v in graph.neighbors(cur.node):
                if not visited[v.to]:
                    q.append(State(v.to, cur.weight + v.weight))
                    visited[v.to] = True
    

if __name__ == "__main__":
    """
    0: 1(1)
    1: 2(2)
    2: 0(3), 1(4)
            0 
           / \
          1   4
         / \ /
        2   5
       / \
      0   1
    """
    # We have 6 nodes: 0, 1, 2, 3, 4, 5
    graph = WeightedDigraph(6)
    graph.addEdge(0, 1, 1)
    graph.addEdge(0, 4, 2)
    graph.addEdge(1, 2, 2)
    graph.addEdge(1, 5, 10)
    graph.addEdge(2, 0, 3)
    graph.addEdge(2, 1, 4)
    graph.addEdge(4, 5, 2)
    

    # print(graph.hasEdge(0, 1))  # true
    # print(graph.hasEdge(1, 0))  # false
    # print(graph.hasEdge(6, 10))

    # for edge in graph.neighbors(2):
    #     print(f"{2} -> {edge.to}, weight: {edge.weight}")
    # # 2 -> 0, weight: 3
    # # 2 -> 1, weight: 4

    # graph.removeEdge(0, 1)
    # print(graph.hasEdge(0, 1))  # false

    # DFS traverse the tree
    # visited = [False] * graph.size()
    # traverse(graph, 0, visited)
    
    # Find the target and the path
    # on_path = [False] * graph.size()
    # path = []
    # all_paths = []
    # findTarget(graph, 0, 5, on_path, path, all_paths)
    # print(all_paths)

    # BFS1
    # dfs1(graph, 0) # 0, 1, 4, 2, 5

    # BFS2
    # dfs2(graph, 0)

    # BFS3
    dfs3(graph, 0)