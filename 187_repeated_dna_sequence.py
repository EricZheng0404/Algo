"""
LeetCode 187. Repeated DNA Sequences
"""

from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        # The returned value
        res = set()
        # We need to record all the sequence we've met before
        seen = set()
        for i in range(n - 10 + 1): # The index of the start of the index starts from 0 to the 10th to the last
            # To extract a sequence of length of 10
            sequence = s[i:i+10]
            if sequence in seen:
                res.add(sequence)
            else:
                seen.add(sequence)
        return list(res)
    
print(("a", "b").tostring())