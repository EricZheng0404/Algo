class Solution:
    """
    Question:
    1. How can we detect an endless cycle?
    Solution: There's a cycle. To use set to detect cycle.
    """
    def isHappy(self, n: int) -> bool:
        # if n == 1:
        #     return True
        numStr = str(n)
        myset = set()
        myset.add(numStr)
        while True:
            num = 0
            for digit in numStr: # Every digit in a char of digit
                num += int(digit) ** 2
            charnum = str(num)
            if charnum in myset:
                return False
            if charnum == "1":
                return True
            myset.add(charnum)
            numStr = charnum
            
