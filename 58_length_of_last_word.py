"""
58. Length of Last Word
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

Example 1:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
"""

class Solution1:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(" ")[-1])
    
class Solution2:
    def lengthOfLastWord(self, s: str) -> int:
        p = len(s)
        length = 0
        while p > 0:
            p -= 1
            if s[p] != " ":
                length += 1
            elif length > 0:
                return length
        return length