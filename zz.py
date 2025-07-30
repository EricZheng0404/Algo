from typing import List
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        res = 0
        for word in words:

            if self.subsequence(word, s):
                print(word)
                res += 1
        return res

    def subsequence(self, word, s):
        i = 0
        j = 0
        while i < len(word) and j < len(s):
            print(i, j)
            if word[i] == s[j]:
                i += 1
                j += 1
            else:
                j += 1
        return i == len(word)
    
sol = Solution()
print(sol.subsequence("acd", "abcde"))