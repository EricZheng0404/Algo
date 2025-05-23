# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
"""
Leetcode 278: First Bad Version

This is a binary search problem.
We need to find the first bad version.

"""

class Solution:
    """
    Implemention 1: [left, right] search problem
    This is a [left, right] search problem since I set the while loop condition 
    as l <= r.
    The search range is closed interval [left, right].
    The answer is l because even if mid is the bad version, we need to search left.
    Even if there's no bad numbers in the left search range, l will bounce back to 
    mid 

    """
    def firstBadVersion1(self, n: int) -> int:
        # l could be 0, 1. It doesn't matter because search range is  [left, right]
        # 0 can't be the answer.
        l, r = 1, n
        while l <= r:
            mid = l + (r - l) // 2  # I forgot this formula
            # If mid is True, that means we have more bad in the left search range
            if isBadVersion(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l
    
    """
    Implemention 2: [left, right) search problem
    This is a [left, right) search problem since I set the while loop condition 
    as l < r.
    The search range is open interval [left, right).
    The answer is l because even if mid is the bad version, we need to search left.
    Even if there's no bad numbers in the left search range, l will bounce back to 
    mid 
    """
    def firstBadVersion2(self, n: int) -> int:
        l, r = 1, n
        while l < r:
            mid = l + (r - l) // 2
            if isBadVersion(mid):
                r = mid 
            else:
                l = mid + 1
        return l
                
