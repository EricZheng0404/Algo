"""
LeetCode 365. Water and Jug Problem

Question I have: 
1. I don't knoe the termination condition as to when to return 
False
If all possible states are visited (all combinations of (a, b) are in visited), 
and we still can't reach the target, we should return False.

"""
class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        # Edge case: If the target is greater than the sum of the two jugs,
        if x + y < target:
            return False
        
        visited = set()
        # We don't need to use deque here because we don't need to calculate 
        # steps. We only need to check if we can reach the target.
        q = list()
        q.append((0, 0))

        while q:
            a, b = q.pop()
            if a + b == target:
                return True
            if (a, b) in visited:
                continue
            visited.add((a, b))
            # We can empty either of the jugs, or fill either of the jugs,
            q.extend([(a, 0), (0, b), (a, y), (x, b)])
            # We can pour water from one jug to the other.
            # Amount of water we can pour from jug1 to jug2
            water = min(a, y - b)
            q.append((a - water, b + water))
            # Amount of water we can pour from jug2 to jug1
            water = min(x - a, b)
            q.append((a + water, b - water))
        return False