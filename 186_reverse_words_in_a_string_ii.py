from typing import List
class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        if n == 1:
            return s
        self.reverse(s, 0, n - 1)
        l, r = 0, 0
        while l < n: 
            while r < n and s[r] != " ":
                r += 1
            self.reverse(s, l, r - 1)
            l = r + 1
            r = l
        
    def reverse(self, s, l, r):
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
    
        