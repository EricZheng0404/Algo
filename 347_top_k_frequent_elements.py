"""
LeetCode 347. Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
"""

from collections import Counter
from typing import List
import heapq

"""
Solution 1: Using Counter
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums) 
        # most_common(k) returns a list of tuples with the most common elements and their frequencies.
        res = []
        for t in count.most_common(k):
            res.append(t[0])
        return res
    

"""
Solution 2: Using Heap push and pop
"""
class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        newList = Counter(nums) # Return a dictionary with the frequency of each element
        pq = []
        
        for key, freq in newList.items():
            heapq.heappush(pq, (freq, key))
            # We only need to keep the k most frequent elements in the heap.
            # As long as the heap is larger than k, we pop the least frequent element.
            while len(pq) > k: 
                heapq.heappop(pq)
        
        res = []
        while pq:
            # freq, num = heapq.heappop(pq)
            # res.append(num)
            res.append(heapq.heappop(pq)[1]) # tuple is also indexable
        return res