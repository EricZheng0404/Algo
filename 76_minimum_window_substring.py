"""
Leetcode 76: Minimum Window Substring
This is a sliding window problem.

The problem is to find the minimum window substring of s that contains all the characters of t.
The window is a substring of s that contains all the characters of t.

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
    # We want to find t in s.
    def minWindow(self, s: str, t: str) -> str: 
        m, n = len(s), len(t)
        if n > m: # Let's just be sure about the edge case handling.
            return ""
        need = {}
        window = {}
        # Process the need string
        for c in t:
            need[c] = need.get(c, 0) + 1

        l, r = 0, 0
        # valid is the number of characters that are we need, ie, len(need)
        valid = 0 
        # start is the start index of the minimum window substring
        start = 0
        length = float('inf')
        while r < m: # I messed up with the m and n here!
            c = s[r]
            r += 1
            if c in need:
                # The window is the characters that are we need
                window[c] = window.get(c, 0) + 1
                # As long as we hit ==, we should update valid, because we know
                # at least we have had one element in the window that fulfilled 
                # need.
                if window[c] == need[c]: 
                    valid += 1

            # This is the condition where we can start shrinking the window.
            while valid == len(need):
                # Update the minimum windows substring
                if r - l < length:
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
                    # If the valud of the windows in on brink of just being equal,
                    # then we know for sure it wouldn't be equal if we remove it.
                    # Sp, we should update the valid here.
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        # Special case, the length is never updated, meaning we never find any 
        # valid window. Then we should just return an empty string
        return "" if length == float('inf') else s[start:start + length]
