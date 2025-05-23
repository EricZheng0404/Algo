class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow, fast = 0, 0
        while fast < len(nums):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1 # slow will be in the next poistion already
            fast += 1
        for i in range(slow, len(nums)): # so we directly use this index all the way to the end. Using range is more elegant
            nums[i] = 0