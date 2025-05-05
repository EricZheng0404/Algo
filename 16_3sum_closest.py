class Solution:
    def twoSumClosest(self, nums, start, target):
        lo = start
        hi = len(nums) - 1
        delta = float("inf") # target - sum_
        while lo < hi:
            sum_ = nums[lo] + nums[hi]
            if  abs(delta) > abs(sum_ - target):
                delta = target - sum_
            if sum_ < target:
                lo += 1
            elif sum_ > target:
                hi -= 1 # hi is decreasing!!!!!!!!!!
        return target - delta

sol = Solution()
print(sol.twoSumClosest([-1, 2, 1, -4], 0, 1))