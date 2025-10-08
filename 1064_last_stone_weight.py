import heapq
from typing import List
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)
        while len(heap) >= 2:
            largest = - heapq.heappop(heap)
            secondLargest = - heapq.heappop(heap)
            if largest == secondLargest:
                continue
            if largest > secondLargest:
                newNum = largest - secondLargest
                heapq.heappush(heap, -newNum)
        if len(heap) == 1:
            return -heapq.heappop(heap)
        if len(heap) == 0:
            return 0