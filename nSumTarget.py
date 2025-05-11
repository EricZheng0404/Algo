##############################################################
# nSum Problem.
# Could be applied to 2Sum, 3Sum, 4Sum, etc.
##############################################################

"""
A recursive way to solve nSum problem.

Input:
- nums: a array of numbers
- n: how many numbers in the sum
- start: the start index
- target: the target number of the sum
"""
def nSumTarget(nums, n, start, target):
    sz = len(nums)
    res = []
    # At least 2Sum, and the array size should be be less than the number of sum
    if n < 2 or sz < n:
        return res
    nums.sort()
    # 2Sum is the base case
    if n == 2:
        lo, hi = start, sz - 1
        while lo < hi:
            left, right = nums[lo], nums[hi]
            _sum = left + right
            if _sum < target:
                while lo < hi and nums[lo] == left:
                    lo += 1
            elif _sum > target:
                while lo < hi and nums[hi] == right:
                    hi -= 1
            else:
                res.append([left, right])
                while lo < hi and nums[lo] == left:
                    lo += 1
                while lo < hi and nums[hi] == right:
                    hi -= 1
        return res
    else:
        # When n > 2, recursively calculate the result of (n-1)Sum. So start is at least 2
        for i in range(start, sz):
            # Skip the duplicate elements
            if i > start and nums[i] == nums[i - 1]:
                continue
            subs = nSumTarget(nums, n - 1, i + 1, target - nums[i])
            for sub in subs:
                sub.append(nums[i])
                res.append(sub)
        return res

if __name__ ==  "__main__":
    print(nSumTarget([0, 1, 3], 2, 0, 4))
    print(nSumTarget([1,0,-1,0,-2,2], 4, 0, 0))