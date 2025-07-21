class Solution:
    """
    1. Why it has to be r = len(nums) - 1?
    2. Why l < r?

    """
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r: # Terminate at l == r, where we find the peak
            mid = l + (r - l) // 2
            # If the mid itself is the peak, or the mid is greater than its right 
            # neighbor, that means the peak is on the left side
            if nums[mid] > nums[mid + 1]:
                r = mid
            # The peak is on the right
            else:
                l = mid + 1
        return l
