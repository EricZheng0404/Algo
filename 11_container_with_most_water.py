"""
LeetCode 11: Container with most water

I have implemented the first chunk of the code correct.
The major thing I was not sure was how to update l and r after we calculate the 
volume and update max.
The answer is to update for the end goal. Since we want the maximum volume, we
want higher bars. So, as long as left bars is lower, we update to the next. If 
the right bars is lower, we update the right.

"""

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height) - 1
        _max = 0
        while l < r:
            left, right = height[l], height[r]
            vol = (r - l) * min(height[r], height[l])
            _max = max(_max, vol)
            # If l is lower than r, we should move l
            if height[l] < height[r]: 
                l += 1
            # If r is lower than or equal to l, we should move r
            else:
                r -= 1
        return _max