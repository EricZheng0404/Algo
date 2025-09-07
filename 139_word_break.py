class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.n = len(s)
        # For faster check for in
        words = set(wordDict)
        self.memo = [-1] * self.n
        return self.dp(s, words, 0)
    
    def dp(self, s, words, start):
        if start == self.n:
            return True
        if self.memo[start] != -1:
            return self.memo[start]
        for word in words:
            if s[start:].startswith(word):
                subProblem = self.dp(s, words, start + len(word))
                if subProblem:
                    self.memo[start] = 1
                    return True
        self.memo[start] = 0
        return False