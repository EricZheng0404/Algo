"""
Leetcode 3: Longest Substring Without Repeating Characters
This is a sliding window problem.

a|b|c|a|b|c|b|b
0|1|2|3|4|5|6|7

exapanding window: 0 1
exapanding window: 0 2
exapanding window: 0 3
exapanding window: 0 4
  shrinking window: 1 4
exapanding window: 1 5
  shrinking window: 2 5
exapanding window: 2 6
  shrinking window: 3 6
exapanding window: 3 7
  shrinking window: 4 7
  shrinking window: 5 7
exapanding window: 5 8
  shrinking window: 6 8
  shrinking window: 7 8

The last window ends at index 7.


"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        l, r = 0, 0
        maxLen = 0
        window = {}

        while r < len(s):
            c = s[r]
            window[c] = window.get(c, 0) + 1
            r += 1
            
            while window[c] > 1:
                d = s[l]
                window[d] -= 1
                # if window[d] == 0:
                #     del window[d]  # Clean up zero counts
                l += 1
            
            maxLen = max(maxLen, r - l)
        
        return maxLen