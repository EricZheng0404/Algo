"""
LeetCode 853: Car Fleet
There are n cars going to the same destination along a one-lane road. The destination is target miles away.

You are given two integer array position and speed, both of length n, where position[i] is the position of the ith car and speed[i] is the speed of the ith car (in miles per hour).

A car can never pass another car ahead of it, but it can catch up to it and drive bumper to bumper at the same speed. The faster car will slow down to match the slower car's speed. The distance between these two cars is ignored.

A car fleet is some non-empty set of cars driving at the same position and same speed. Note that a single car is also a car fleet.

If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.
"""
from typing import List
class Solution:
    """
    To catch up with the car y, the car x must spend less time to reach the 
    destination (going faster). For example, time [12, 3, 7, 1, 2], the fleets
    are [12], [3, 7], [1, 2].
    """
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        n = len(position)
        for i in range(n):
            cars.append([position[i], speed[i]])
        cars.sort(key = lambda x: x[0])
        time = [((target - car[0]) / car[1]) for car in cars]
        res = 0
        max_time = 0
        # To calculate the local maxima
        for i in range(n - 1, -1, -1):
            if time[i] > max_time:
                res += 1
                max_time = time[i]
        return res
    
class Solution2:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        cars = []
        for i in range(n):
            cars.append([position[i], speed[i]])
        cars.sort(key = lambda x: x[0])
        time = [(target - car[0])/car[1] for car in cars]
        # Use a monotonic stack to catch all the local maximum
        s = []
        for t in time:
            while s and s[-1] <= t:
                s.pop()
            s.append(t)
        return len(s)