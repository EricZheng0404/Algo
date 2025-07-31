from typing import List
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextGreater = self.monotonic(nums2)
        # num2 : next greater value
        greaterMap = {}
        # Because all values are unique, so we can use dictionary for O(1) lookup
        # num2:next greater number
        for i in range(len(nums2)):
            greaterMap[nums2[i]] = nextGreater[i]
        return [greaterMap[num] for num in nums1]
        
    def monotonic(self, nums):
        n = len(nums)
        res = [0] * n
        s = [] 
        for i in range(n - 1, -1, -1):
            num = nums[i]
            # We get rid of all the number that's less than the num
            while s and s[-1] <= num:
                s.pop()
            # Get the closest number that's greater than the num
            res[i] = -1 if not s else s[-1]
            s.append(num)
        return res
            