"""
I was not sure about how to control the going up and down
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        res = [""] * numRows
        row = 0
        goingdown = False
        for char in s:
            res[row] += char
            if row == 0 or row == numRows - 1:
                goingdown = not goingdown
            row += 1 if goingdown else -1
        return "".join(res)