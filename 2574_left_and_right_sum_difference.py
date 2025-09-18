class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftRange = [0]
        leftSum = 0
        for i in range(len(nums) - 1):
            leftSum += nums[i]
            leftRange.append(leftSum)
        rightRange = [0]
        rightSum = 0
        for i in range(len(nums)- 1, 0, -1):
            rightSum += nums[i]
            rightRange.append(rightSum)
        rightRange.reverse()
        for i in range(len(leftRange)):
            leftRange[i] = abs(leftRange[i] - rightRange[i])
        return leftRange