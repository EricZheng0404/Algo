"""
LeetCode 739: Daily Temperatures
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
"""

from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        s = []
        for i in range(n - 1, -1, -1):
            # On the stack, the numbers are in descending order
            # We pop the numbers that are less than the current temperature
            # For example, if the stack is [75, 74, 73], and the current 
            # temperature is 72,
            # we pop 73 and 74 because they are less than 72.
            while s and temperatures[s[-1]] <= temperatures[i]:
                s.pop()
            res[i] = 0 if not s else s[-1] - i
            # Instead of pushing the actual temperatures, we push the index of
            # the temperatures which is greater than the current temperature
            s.append(i)
        return res