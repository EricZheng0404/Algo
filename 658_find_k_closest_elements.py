class Solution:
    """
    Questions:
    1. What's the purpose of using open ends?
    Because p is not necessarily included in the result.
    For example arr = [0, 1, 2, 4, 5], x = 3. In this case, p = 3 pointing to 4.
    But we should have 2 in the result.
    """
    from typing import List
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        pos = self.leftBound(arr, x)
        # l, r are both open-ended, handling the edge cases that l and r can be 
        # pushed out of the range of arr
        l, r = pos - 1, pos
        while r - l - 1 < k:
            # If there's no more element to the left
            if l == -1:
                r += 1
            # If there's no more element to the right
            elif r == len(arr):
                l -= 1
            elif (x - arr[l]) > (arr[r] - x):
                r += 1
            # Even if (x - arr[l]) == (arr[r] - x), we should expand on the left
            else:
                l -= 1
        return arr[l + 1:r]
    """
    arr is the input arr in findClosestElements
    target is the target number we want to 
    The reason why we use leftBound for the following two reasons:
    1. If the target x doesn't exist, we can find the least value that's greater than
    x.
    2. If there're multiple existences, we can find the most left x and all the x's 
    to its right are all numbers we want to include in the list
    """
    def leftBound(self, arr, target):
        l, r = 0, len(arr)
        while l < r:
            mid = l + (r - l) // 2
            if arr[mid] < target:
                l = mid + 1
            else:
                r = mid
        return l

