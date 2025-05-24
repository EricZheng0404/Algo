"""
Leetcode 76: Minimum Window Substring
This is a sliding window problem.

When should we move to expand the window? What should we update?
Answer:
When the window doesn't contain all the characters. And we should update
the window dictionary.

When should we stop expanding?
When the windows doesn't contain all the characters.

Should we update the result when expanding or shrinking the window?
When shrinking 

"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        if n > m:
            return ""
        need = {}
        window = {}
        res = ""
        # Process the need string
        for c in t:
            need[c] = need.get(c, 0) + 1

        l, r = 0, 0
        valid = 0
        start = 0
        length = float('inf')
        while r < m: # I messed up with the m and n here!
            c = s[r]
            r += 1
            if c in need:
                # The window is the characters that are we need
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1

            # should update valid in here
            while valid == len(need):
                # Update the minimum windows substring while it's still valid before
                # we shrink the window
                while r - l < length:
                    start = l
                    length = r - l
                # As long as we have a valid window, we try to shrink the window.
                # If after the shrinking, the window is not valid anymore, we'd
                # go back to expand
                d = s[l]
                l += 1
                # We update the window when we move right with a needed character 
                # removed from the window
                if d in window:
                    window[d] -= 1
                    if window[d] < need[d]:
                        valid -= 1
                print(f"  Srinking {l} and {r}")
        # Special case, the length is never updated, meaning we never find any 
        # valid window. Then we should just return an empty string
        return "" if length == float('inf') else s[start:start + length]
