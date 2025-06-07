"""
LeetCode 310. Minimum Height Trees

"""
from collections import deque
from typing import List

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        1. Set up the adjacency list
        2. Put all leaf nodes into the queue and remove them
        3. In the while loop, we continue with removing layers of leaf node
        4. When the nodeSize is less than or equal to 2, we stop
        5. We return the list
        """
        # Edge case: if there's only one node
        if n == 1:
            return [0]
        # Set up the adjancency list (It's not adjacency matrix!!!)
        matrix = [[] for _ in range(n)]
        for edge in edges:
            matrix[edge[0]].append(edge[1])
            matrix[edge[1]].append(edge[0])
        # Put all leaf nodes into the queue
        q = deque() # Contains all the node index
        for i in range(len(matrix)):
            if len(matrix[i]) == 1:
                q.append(i)
        # We remove leaf nodes layer by layer until there're equal to less than 2 nodes
        nodesz = n
        while nodesz > 2:
            sz = len(q)
            nodesz -= sz # We update the nodessz, this is the size after we remove all the elements in the node
            for _ in range(sz):
                curr = q.popleft()
                for neighbor in matrix[curr]:
                    # We need to remove the curr from all its neighbor's adjacency list
                    matrix[neighbor].remove(curr)
                    if len(matrix[neighbor]) == 1:
                        q.append(neighbor)

        return list(q)