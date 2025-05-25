"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        # Be careful with the edge case handling. 
        if m > n:
            return False
        window, need = {}, {}

        # Initialize the need window
        for c in s1:
            need[c] = need.get(c, 0) + 1
        
        l, r, valid = 0, 0, 0

        while r < n:
            c = s2[r]
            r += 1
            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1
            
            # Only start checking when window size equals s1's length
            while r - l >= m:
                if valid == len(need):
                    return True
                d = s2[l]
                l += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return False


if __name__ == "__main__": 
    s1 = "abcdxabcde"
    s2 = "abcdeabcdx"
    print(Solution().checkInclusion(s1, s2))
