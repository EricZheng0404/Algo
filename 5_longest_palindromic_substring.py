class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        res = ""
        for i in range(len(s)):
            s1 = self.findPalindrone(s, i, i)
            s2 = self.findPalindrone(s, i, i + 1)
            res = res if len(res) > len(s1) else s1
            res = res if len(res) > len(s2) else s2
        return res
    
    def findPalindrone(self, s, l, r) -> str:
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        # The l and r will end be out of range or not equal and the end of the
        # while loop.
        return s[l + 1:r]