from typing import List

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
    
    # return all neighbors of a vertex
    def neighbors(self, v: int):
        return self.graph[v]
    
    def size(self):
        return len(self.graph)
    
    def _in_range(self, vertex):
        length = len(self.graph)
        if vertex >= length:
            raise IndexError("Index out of range")


# DFS traversal
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

# Find the path to the target
# Store all the possible paths to the destination
def findTarget(graph: WeightedDigraph, src, dest, on_path, path, all_paths):
    if src < 0 or src >= graph.size():
        return 
    # print(on_path)
    if on_path[src]:
        return 
    # Pre-order position
    on_path[src] = True
    path.append(src)
    if src == dest:
        all_paths.append(path)
    for e in graph.neighbors(src):
        findTarget(graph, e.to, dest, on_path, path, all_paths)
    path.pop()
    on_path[src] = False
    


if __name__ == "__main__":
    """
    0: 1(1)
    1: 2(2)
    2: 0(3), 1(4)
            0 
           / \
          1   4
         / \
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
    visited = [False] * graph.size()
    # traverse(graph, 0, visited)
    
    # Find the target and the path
    on_path = [False] * graph.size()
    path = []
    all_paths = []
    findTarget(graph, 0, 5, on_path, path, all_paths)
    print(all_paths)