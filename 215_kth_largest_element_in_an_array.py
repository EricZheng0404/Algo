from typing import List
import heapq

"""
Leetcode 215: Kth Largest Element in an Array
This is a heap problem.
The goal is to find the kth largest element in an array.
"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        newNums = [-x for x in nums]
        heapq.heapify(newNums)
        res = 0
        for _ in range(k):
            res = -heapq.heappop(newNums)
        return res