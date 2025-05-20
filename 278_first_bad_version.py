# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # l could be 0, 1. It doesn't matter because search range is  [left, right]
        # 0 can't be the answer.
        l, r = 1, n
        while l <= r:
            mid = l + (r - l) // 2  # I forgot this formula
            # If mid is True, that means we have more bad in the left search range
            if isBadVersion(mid):
                r = mid
            else:
                l = mid + 1

            return l
