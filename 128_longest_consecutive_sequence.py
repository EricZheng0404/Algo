"""
LeetCode 128. Longest Consecutive Sequence
"""

from typing import List

"""
This is a greedy problem. We can use a set to store the numbers. Then we can
iterate through the set and check if the current number is the start of a
consecutive sequence. If it is, we can check the length of the consecutive
sequence.
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0
        for num in numSet:
            if num - 1 not in numSet:
                length = 1
                next = num + 1
                while next in numSet:
                    length += 1
                    next += 1
                res = max(length, res)
        return res