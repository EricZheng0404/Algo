class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len1 = len(haystack)
        len2 = len(needle)
        if len2 > len1:
            return -1
        for i in range(len1- len2 + 1):
            if haystack[i:i+len2] == needle:
                return i 
        return -1