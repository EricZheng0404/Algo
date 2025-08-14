from typing import List
"""
Mistakes:
I added an unnecessary condition in line 20. At the leaf of the backtracking 
tree, start has already increased to self.n, so we won't be able to enter the 
if statement to add the final result.
"""
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        self.mapping = ["", "", "abc", "def", "ghi", "jkl",
                        "mno", "pqrs", "tuv", "wxyz"]
        self.res = []
        # self.usd = []
        self.path = []
        self.n = len(digits)
        self.backtrack(digits, 0)
        return self.res

    def backtrack(self, digits, start):
        # if start >= self.n:
        #     return
        if len(self.path) == self.n:
            self.res.append("".join(self.path))
            return
        possibleLetters = self.mapping[ord(digits[start]) - ord('0')]
        for letter in possibleLetters:
            self.path.append(letter)
            self.backtrack(digits, start + 1)
            self.path.pop()