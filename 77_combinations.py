"""
77. Combinations

Example:
Input: n = 4, k = 2
Outout: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
When i == 4 on the second level, its backtrack function is backtrack(5, n, k). 
It will not be executed because for i range(5, 5) is empty.
"""
from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.res = []
        self.path = []
        self.backtrack(1, n, k)
        return self.res

    def backtrack(self, start, n, k):

        if len(self.path) == k:
            self.res.append(self.path[:])
            return
        for i in range(start, n + 1):
            self.path.append(i)
            # The reason why we should just pass in n is that we should just 
            # track n numbers, not n + 1 numbers
            self.backtrack(i + 1, n, k) 
            if i == 4:
                print(f"path is {self.path}")
            self.path.pop()