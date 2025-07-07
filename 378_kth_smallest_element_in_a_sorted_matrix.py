"""
378. Kth Smallest Element in a Sorted Matrix
"""
from typing import List
import heapq
class Solution:
    """
    I misunderstood the question.
    Each single list is non-descending, but each list is not non-descending to each
    other.
    """
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # a priority queue
        pq = []
        n = len(matrix)
        # initialize the priority queue
        for i in range(n):
            heapq.heappush(pq, (matrix[i][0], i, 0))
        res = None
        for _ in range(k):
            curr = heapq.heappop(pq)
            res = curr[0]
            i, j = curr[1], curr[2]
            if j < n - 1:
                heapq.heappush(pq, (matrix[i][j + 1], i, j + 1))
        return res

