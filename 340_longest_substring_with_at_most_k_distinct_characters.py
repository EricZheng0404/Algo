class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        l, r = 0, 0
        window = {}
        maxLength = 0
        while r < len(s):
            rightChar = s[r]
            window[rightChar] = window.get(rightChar, 0) + 1
            r += 1

            if len(window) > k:
                leftChar = s[l]
                window[leftChar] -= 1
                if window[leftChar] == 0:
                    del window[leftChar]
                l += 1
            maxLength = max(maxLength, r - l)
        return maxLength