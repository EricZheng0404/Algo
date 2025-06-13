class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.n = len(s)
        self.res = []
        self.path = []
        self.backtrack(s, 0)
        return self.res

    def backtrack(self, s, start):
        if start == self.n:
            self.res.append(self.path[:])
        for i in range(start, self.n):
            if not self.isPalindrome(s[start:i+1]):
                  continue
            self.path.append(s[start:i + 1])
            self.backtrack(s, i + 1)
            self.path.pop()
            

    def isPalindrome(self, input):
        if not input:
            return False
        return input == input[::-1]