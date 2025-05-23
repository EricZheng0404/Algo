from typing import List 

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        length = len(s)
        if length == 1:
            return str
        l, r = 0, length - 1
        while l<=r:
            temp = s[l]
            s[l] = s[r]
            s[r] = temp
            l+=1
            r-=1

        