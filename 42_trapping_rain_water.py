from typing import List

class Solution:
    def trap1(self, height: List[int]) -> int:
        res = 0
        n = len(height)
        for mid in range(1, n - 1):
            lMax, rMax = 0, 0
            # Find the tallest to the right
            for j in range(mid, n):
                rMax = max(rMax, height[j])
            # Find the tallest to the left
            for j in range(mid, -1, -1):
                lMax = max(lMax, height[j])
            volume = min(lMax, rMax,) - height[mid]
            res += volume
        return res
    
    def trap2(self, height: List[int]) -> int:
        n = len(height)
        if n <= 2:
            return 0
        res = 0

        lMax, rMax = [0] * n, [0] * n
        lMax[0] = height[0]
        rMax[n - 1] = height[n - 1]

        for i in range(1, n):
            lMax[i] = max(height[i], lMax[i - 1])
        for i in range(n - 2, -1, -1):
            rMax[i] = max(rMax[i], rMax[i + 1]) # I fucked up here, I should have used rMax[i + 1] instead of rMax[i]
        print("rMax: ", rMax)
        for i in range(1, n - 1):
            res += min(lMax[i], rMax[i]) - height[i]
        return res
    
sol = Solution()
print(sol.trap2([0,1,0,2,1,0,1,3,2,1,2,1]))