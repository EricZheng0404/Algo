from typing import List

class Solution:
    """
    I forgot sliding window. 
    To 
    1. When should the window expand?
    2. When should the window shrink?
    3. When do you get a valid answer?
    """
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l, r = 0, 0
        window = set()
        while r < len(nums):
            # Expand the window when r - l < k
            char = nums[r]
            if char in window:
                return True
            window.add(char)
            r += 1

            if r - l > k:
                window.remove(nums[l])
                l += 1
        return False