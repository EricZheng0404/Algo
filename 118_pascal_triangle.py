"""
LeetCode 118. Pascal's Triangle

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
"""

from typing import List

class Solution1:
    """
    Solution 1: Iterative
    """
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        if numRows == 1:
            return res
        # res.append([1,1])
        # if numRows == 2:
        #     return res
        for _ in range(numRows - 1):
            last = res[-1]
            curr = []
            for j in range(len(last) - 1):
                curr.append(last[j] + last[j + 1])
            curr.insert(0, 1)
            curr.append(1)
            res.append(curr)
        return res
    
class Solution:
    """
    Solution 2: Recursive
    """
    def generate(self, numRows: int) -> List[List[int]]:
        # Base case: If numRows is 1
        if numRows == 1:
            return [[1]]
        # If not base cae, we first get the prev triangle, and add another row to it.
        prev_triangle = self.generate(numRows - 1)
        bottom_row = prev_triangle[-1]
        curr_row = [1]
        for i in range(len(bottom_row) - 1):
            curr_row.append(bottom_row[i] + bottom_row[i + 1])
        curr_row.append(1)
        prev_triangle.append(curr_row)
        return prev_triangle
    