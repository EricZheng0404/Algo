"""
LeetCode 18. 4sum

Given an array of intergers, return an array of all the unique quadruplets 
such that the addition of four numbers makes up a target.

The time complexity is O(n3):
- sorted() is O(nlogn).
- Every threeSum is O(n2).
- We call threeSum on every element.
- So the overall complexity is O(nlogn + n*n2) = O(n3).
"""

class Solution(object):
    # Implementation 1: We use threeSum and twoSum to solve fourSum
    def fourSum1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # We should have newNums variable rather than nums.sort()
        # BUT I forgot to use newNums and used nums multiple time!!!!!!
        newNums = sorted(nums)
        length = len(nums)
        i = 0
        res = []
        while i < length - 3:
            triplets = self.threeSum(newNums, i + 1, target - newNums[i])
            if triplets:
                for triplet in triplets:
                    triplet.append(newNums[i])
                    res.append(triplet)
            # This loop takes us to the last elements of a series of duplicates
            while i < length - 3 and newNums[i] == newNums[i + 1]:
                i += 1 
            # This takes us to the first non-duplicate
            i += 1
        return res


    def threeSum(self, nums, start, target):
        res = []
        i = start 
        while i < len(nums):
            tuplets = self.twoSum(nums, i + 1, target - nums[i])
            if tuplets:
                for tuplet in tuplets:
                    triplet = [nums[i]] + tuplet
                    res.append(triplet)
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1 
            i += 1
        return res
    
    # The input nums is assumed to be sorted
    def twoSum(self, nums, start=0, target=0):
        l, r = start, len(nums) - 1
        res = []
        while l < r:
            left, right = nums[l], nums[r]
            _sum = left + right
            if _sum < target:
                while l < r and left == nums[l]:
                    l += 1
            elif _sum > target:
                while l < r and right == nums[r]:
                    r -= 1
            else:
                res.append([left, right])
                while l < r and left == nums[l]:
                    l += 1
                while l < r and right == nums[r]:
                    r -= 1
        return res
        

if __name__ == "__main__":
    sol = Solution()

    # Test for twoSum
    nums = [0, 2, 3, 5]
    target = 5
    # print(sol.twoSum(nums,1,target))

    # Test for threeSum
    nums = [-1,0,1,2,-1,-4]
    target = 0
    print(sol.threeSum(nums))
