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

def checkInclusion(s1, s2):
    need, window = {}, {}
    for c in s1:
        need[c] = need.get(c, 0) + 1

    left, right, valid = 0, 0, 0

    while right < len(s2):
        c = s2[right] 
        right += 1
        if c in need:
            window[c] = window.get(c, 0) + 1
            if window[c] == need[c]:
                valid += 1

        while right - left >= len(s1):
            if valid == len(need):
                return True
            d = s2[left]
            left += 1
            if d in need:
                if window[d] == need[d]:
                    valid -= 1
                window[d] = window[d] - 1
    return False




if __name__ == "__main__": 
    s1 = "ab"
    s2 = "eidbaooo"
    print(checkInclusion(s1, s2))
    s3 = "ab"
    s4 = "eidboaoo"
    print(checkInclusion(s3, s4))
