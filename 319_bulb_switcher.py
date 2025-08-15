from math import sqrt
"""
319. Bulb Switcher

If a bulb is on, it means it has an odd number of factors.
Only perfect squares have an odd number of factors.
So the number of bulbs that are on is the number of perfect squares
less than or equal to n.
If we have 16 bulbs, the bulbs that are on are 1, 4, 9, 16.
So the number of bulbs that are on is 4.
"""
class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(sqrt(n))