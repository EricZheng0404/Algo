class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        while l <= r:
            # Edge case where all the element are the same
            # [0, 0, 0]
            # In this case, l will check nums[2] == nums[3], which is 
            # Out of range
            while l < r and nums[l] == nums[l + 1]:
                l += 1
            while l < r and nums[r] == nums[r - 1]:
                r -= 1
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return True
            # The left is sorted
            if nums[mid] >= nums[l]:
                if nums[l] <= target and target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target and target <= nums[r]:
                    l = mid + 1
                else: 
                    r = mid - 1
        return False