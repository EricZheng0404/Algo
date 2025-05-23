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
                if window[d] == 0:
                    del window[d]  # Clean up zero counts
                l += 1
            
            maxLen = max(maxLen, r - l)
        
        return maxLen