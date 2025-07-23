from typing import List
class Solution:
    """
    We need to figure out x, f(x), and target.
    In this case, x is the eating speed, f(x) is the total hours of eating, which is
    monotonically inverse witht the eating speed. Target is the hours the guards are 
    away.

    We want to find the left range because we want to find the minimum eating speed.
    """
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l < r:
            mid = l + (r - l) // 2
            # The total eating hours now
            hrs = self.convert(piles, mid)
            if hrs == h:
                r = mid
            # The eating hours are too long, we are eating too slow, need to eat faster
            elif hrs > h:
                l = mid + 1
            # The total eating hours are too short, we're eating too fast.
            elif hrs < h:
                r = mid
        return l

    def convert(self, piles, speed):
        hrs = 0
        for pile in piles:
            hrs += math.ceil(pile/speed)
        return hrs