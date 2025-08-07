class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        i = 0
        length = len(nums)
        res = []
        while i < length - 1:
            tuplets = self.twoSum(nums, i + 1, 0 - nums[i])
            print(tuplets)
            for tuplet in tuplets:
                # res.append(tuplet.append(nums[i]))
                triplet = tuplet + [nums[i]]
                res.append(triplet)
            # Skeip the duplicate of the first number
            # It has to be length - 1
            while i < length - 1 and nums[i] == nums[i + 1]:
                i += 1
            i += 1
        return res

    def twoSum(self, nums, start, target):
        lo = start
        hi = len(nums) - 1
        res = []
        while lo < hi:
            _sum = nums[lo] + nums[hi]
            # We store left and right value at the start of every while loop
            left, right = nums[lo], nums[hi] 
            if _sum < target:
                # If the old left value is the same as the lo value
                # The lo value is updated in every inner while loop
                while lo < hi and left == nums[lo]:
                    lo += 1
            elif _sum > target:
                # If the old right value is the same as the hi value
                # The hi value is updated in every inner while loop
                while lo < hi and right == nums[hi]:
                    hi -= 1
            else:
                res.append([left, right])
                while lo < hi and left == nums[lo]:
                    lo += 1
                while lo < hi and right == nums[hi]:
                    hi -= 1
        return res
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)
        for i in range(n - 2):
            # Skip all the same number
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = n - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    # If there's a match, we want to move to the next unique value
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                elif total < 0:
                    j += 1
                else:
                    k -= 1
        return res