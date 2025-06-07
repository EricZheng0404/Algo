"""
LeetCode 5. Longest Palindromic Substring

Question I have: I don't know how to handle the case when the length of the
palindrome is even.
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        res = ""
        for i in range(len(s)):
            # The case when the length of the palindrome is odd
            s1 = self.findPalindrone(s, i, i)
            # The case when the length of the palindrome is even
            s2 = self.findPalindrone(s, i, i + 1)
            res = res if len(res) > len(s1) else s1
            res = res if len(res) > len(s2) else s2
        return res
    
    def findPalindrone(self, s, l, r) -> str:
        while l >= 0 and r < len(s) and s[l] == s[r]:
            # Be conscious about the l and r are the center of the palindrome.
            l -= 1 # I put l += 1 here before, and it was wrong.
            r += 1 # I put r -= 1 here before, and it was wrong.
        # The l and r will end up being out of range or not equal and the end of
        # the while loop.
        return s[l + 1:r]