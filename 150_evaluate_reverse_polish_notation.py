"""
LeetCode 150. Evaluate Reverse Polish Notation
"""

from typing import List

class Solution:
    """
    Question:
    1. How to implement the division truncates toward zero?

    """
    def evalRPN(self, tokens: List[str]) -> int:
        res = []
        for token in tokens:
            if token in "+-*/":
                ele2 = res.pop()
                ele1 = res.pop()
                if token == "+":
                    res.append(ele1 + ele2)
                elif token == "-":
                    res.append(ele1 - ele2)
                elif token == "*":
                    res.append(ele1 * ele2)
                else:
                    res.append(int(ele1 / ele2))
            else:
                res.append(int(token))
        return res[0]
