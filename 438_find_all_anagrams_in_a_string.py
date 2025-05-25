"""
Leetcode 438: Find All Anagrams in a String
This is a sliding window problem.
"""
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        lenS, lenP = len(s), len(p)
        # if p > s:
        #     return []
        
        window, need = {}, {}
        for c in p:
            need[c] = need.get(c, 0) + 1
        lenNeed = len(need)
        
        l, r, valid = 0, 0, 0
        res = []
        while r < lenS:
            print(f"Now r is {r}")
            c = s[r]
            r += 1
            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1
            print(f"window is {l} and {r}")
            print(f"window dict is {window}")
            
            while r - l == lenP:
                if valid == lenNeed:
                    res.append(l)
                d = s[l] 
                l += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
            print(f"  shrinking window {l} and {r}")
            print(f"  shrinking dict is {window}")
            print("\n")
        print("We're in here")
        return res
        
if __name__ == "__main__":
    s = "abacbabc"
    p = "abc"
    print(Solution().findAnagrams(s, p))