from typing import List

# Adjacency List Implementation
class WeightedDigraph:
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
        
def traverse(graph: WeightedDigraph, s, visited):
    if s < 0 or s >= graph.size():
        return
    if (visited[s]):
        return
    visited[s] = True
    print(f"visit: {s}")
    for e in graph.neighbors(s):
        traverse(graph, e.to, visited)

if __name__ == "__main__":
    """
    0: 1(1)
    1: 2(2)
    2: 0(3), 1(4)
    """
    graph = WeightedDigraph(3)
    graph.addEdge(0, 1, 1)
    graph.addEdge(1, 2, 2)
    graph.addEdge(2, 0, 3)
    graph.addEdge(2, 1, 4)

    # print(graph.hasEdge(0, 1))  # true
    # print(graph.hasEdge(1, 0))  # false
    # print(graph.hasEdge(6, 10))

    # for edge in graph.neighbors(2):
    #     print(f"{2} -> {edge.to}, weight: {edge.weight}")
    # # 2 -> 0, weight: 3
    # # 2 -> 1, weight: 4

    # graph.removeEdge(0, 1)
    # print(graph.hasEdge(0, 1))  # false
    visited = [False] * graph.size()

    traverse(graph, 0, visited)
    