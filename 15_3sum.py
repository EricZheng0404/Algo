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
            left, right = nums[lo], nums[hi]
            if _sum < target:
                while lo < hi and left == nums[lo]:
                    lo += 1
            elif _sum > target:
                while lo < hi and right == nums[hi]:
                    hi -= 1
            else:
                res.append([left, right])
                while lo < hi and left == nums[lo]:
                    lo += 1
                while lo < hi and right == nums[hi]:
                    hi -= 1
        return res

                
if __name__ == "__main__":
    sol = Solution()
    print(f"first solution: ", sol.twoSum([2, 3, 6, 7, 8], 0, 9))
    print(f"second solution: ", sol.twoSum([2, 3, 6, 7, 8], 1, 9))