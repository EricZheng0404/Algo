"""
Leetcode 151: Reverse Words in a String

Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.
"""
from typing import List

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split() # split the string into a list of words
        return " ".join(words[::-1])
    
class Solution2:
    def reverseWords(self, s: str) -> str:
        # The whole purpose of doing this is because we're reversing the string in-place
        # 1. Remove all trailing and redundant between-word spaces and make it a list
        stringList = []
        for char in s:
            if char != " ":
                stringList.append(char)
            elif stringList and stringList[-1] != " ":
                stringList.append(char)
        if stringList[-1] == " ":
            stringList.pop()
        # 2. Reverse the whole list.
        self.reverse(stringList, 0, len(stringList) - 1)
        # 3. Reverse each single word.
        i = 0
        while i < len(stringList):
            for j in range(i, len(stringList)):
                # [j + 1] is out of bound for the last word, 
                # so we need to check if j is the last index first
                # If it's met, then [j + 1] won't be checked.
                if j == len(stringList) - 1 or stringList[j + 1] == " ":
                    self.reverse(stringList, i, j)
                    i = j + 2
                    break
        return "".join(stringList)
        

    # Reverse the list in-place
    def reverse(self, arr:list, i: int, j: int):
        while i <= j: # I forgor this
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
print(Solution().reverseWords("the sky is blue"))