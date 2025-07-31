from typing import List
class Solution:
    """
    Ground rules:
    1. The number of left and right parentheses should be the same.
    2. For any substring, the number of left parentheses should be 
    more than right parentheses.
    """
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        self.path = ""
        self.backtracking(n, n)
        return self.res
    """
    left: the number of left parenthesis I can use
    right: the number of right parenthesis I can use
    """
    def backtracking(self, left, right):
        # Base cases
        if left < 0 or right < 0:
            return 
        # At any point, there's no way the number of the left parens
        # can be more than right parens
        if left > right:
            return 
        if left == 0 and right == 0:
            self.res.append(self.path) 
        # Add left parenthesis
        self.path += "("
        self.backtracking(left - 1, right)
        self.path = self.path[:-1]
        # Add right parenthesis
        self.path += ")"
        self.backtracking(left, right - 1)
        self.path = self.path[:-1]

        