class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        # dict {char: freq} to track the window.
        # The length of the window 
        # When to expand: as long as len(dict) < 2
        # When to shrink: as long as dict > 2
        # When to check the answer: after shrink
        l, r = 0, 0
        window = {}
        maxLength = 0
        while r < len(s):
            char = s[r]
            # if len(window) <= 2:
            window[char] = window.get(char, 0) + 1
            r += 1

            if len(window) > 2:
                leftChar = s[l]
                if window[leftChar] == 1:
                    del window[leftChar]
                else:
                    window[leftChar] -= 1
                l += 1
            maxLength = max(maxLength, r - l)
        return maxLength