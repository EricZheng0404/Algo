"""
LeetCode 33:
Seach in rotated sorted array

Input: 
- a rotated sorted array
- a target

Output: 
- the index of the target, or -1 if the target doesn't exist
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        while l <= r: # It's <=, not <, because the 
            # mid = l + (r - l) // 2
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            # The mid is in the left part, the left part if sorted
            if nums[mid] >= nums[l]: 
                # The target is in this sorted part
                if nums[l] <= target and target < nums[mid]: 
                    # Because we know mid is not the target
                    r = mid - 1
                # The target is in the non-sorted part
                else: 
                    l = mid + 1
            # The mid is in the right part, the right part is sorted
            else: 
                # The target is in the sorted part
                if nums[mid] < target and target <= nums[r]: 
                    l = mid + 1
                # The target is not in the sorted part
                else: 
                    r = mid - 1 
        return -1


if __name__ == "__main__":
    sol = Solution()
    assert sol.search([4,5,6,7,0,1,2], 0) == 4 # expected output: 4
    assert sol.search([1,2,3,4],2) == 1

