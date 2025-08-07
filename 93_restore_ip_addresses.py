from typing import List
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.res = []
        self.path = []
        self.backtrack(s, 0)
        return self.res
    
    def backtrack(self, s, start):
        # Base case:
        if len(self.path) == 4 and start == len(s):
            self.res.append(".".join(self.path[:]))
            return 
        for i in range(start, len(s)):
            # When the number is greater than 255
            if int(s[start:i + 1]) > 255:
                continue
            # When we have leading zeroes
            if len(s[start:i + 1]) >= 2 and s[start:i + 1][0] == "0":
                continue
            # If we already have more than 4 elements in the list, we can break
            if len(self.path) >= 4:
                break
            self.path.append(s[start:i + 1])
            self.backtrack(s, i + 1)
            self.path.pop()