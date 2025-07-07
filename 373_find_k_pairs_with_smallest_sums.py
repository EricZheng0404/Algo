"""
373. Find K Pairs with Smallest Sums

Example:
Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]

We can divide pairs into three categories:
[1,2], [1,4], [1,6]
[7,2], [7,4], [7,6]
[11,2], [11,4], [11,6]

We can use a priority queue to store the pairs.
"""
from typing import List
import heapq

class Solution:
    """
    Priority Queue: (nums1[] + nums2[], nums1[], num2[], i)
    """
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        n = len(nums1)
        pq = []
        for i in range(n):

            heapq.heappush(pq, (nums1[i] + nums2[0], nums1[i], nums2[0], 0))
        
        res = []
        for j in range(k):
            sum_, n1, n2, i = heapq.heappop(pq)
            res.append([n1, n2])
            if i < len(nums2) - 1:
                heapq.heappush(pq, (n1+nums2[i + 1], n1, nums2[i + 1], i + 1))
            
        return res
