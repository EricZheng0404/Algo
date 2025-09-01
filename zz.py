from typing import List
class Solution:
    def generateBinaryNumbers(self, n: int) -> List[str]:
        self.res = []
        self.path = ""
        self.backtrack(n)
        return self.res
    
    def backtrack(self, n):
        print(f"path is {self.path}")
        if len(self.path) == n:
            self.res.append(self.path[:])
            return
        for i in range(2):
            self.path += str(i)
            self.backtrack(n)
            self.path = self.path[:-1]

print(Solution().generateBinaryNumbers(3))