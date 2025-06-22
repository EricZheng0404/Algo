"""
933. Number of Recent Calls
"""
from collections import deque
class RecentCounter:
    """
    1. If we want to remove the first element a lot, a deque is way more efficient than
    a list.
    2. Removing elements while iteratings through a list could lead to undefined behavior.
    """
    def __init__(self):
        self.nums = deque()
        self.min = None
        self.max = None

    def ping(self, t: int) -> int:
        self.min = t - 3000
        self.max = t
        self.nums.append(t)
        
        while self.nums[0] < self.min:
            self.nums.popleft()
        return len(self.nums)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)