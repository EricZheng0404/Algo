from typing import List
from collections import defaultdict
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        lookup = defaultdict(list)
        for i, ch in enumerate(s):
            lookup[ch].append(i)
        res = 0
        for word in words:
            i = 0 # Pointer in the word
            j = 0 # # Pointer in s
            while i < len(word) and j < len(s):
                c = word[i]
                # If the character is not in the lookup, aka not in s
                if c not in lookup:
                    break
                # To find the position of c in the lookup table which is greater than
                # or equal to the current j pointer
                pos = self.leftBound(lookup[c], j) # pos in the position of the index
                # If pos are out of the bound the value list, that means c is not 
                # found
                if pos == len(lookup[c]):
                    break
                # If pos is a valid value, we can continue
                i += 1
                j = lookup[c][pos] + 1
            if i == len(word):
                res += 1
        return res
                

    def leftBound(self, arr, target):
        l, r = 0, len(arr) # left close, right open
        while l < r:
            mid = l + (r - l) // 2
            if arr[mid] >= target:
                r = mid
            else:
                l = mid + 1
        return l
