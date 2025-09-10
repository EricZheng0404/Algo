class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        self.memo = [[-1] * (n + 1) for _ in range(m + 1)]
        return self.dp(text1, m, text2, n)
    
    # represents the longest common subsequence for text1[0:i] and text2[0:j]
    def dp(self, text1, i, text2, j): 
        if i == 0 or j == 0: 
            return 0
        if self.memo[i][j] != -1:
            return self.memo[i][j]
        if text1[i - 1] == text2[j - 1]:
            self.memo[i][j] = 1 + self.dp(text1, i - 1, text2, j - 1)
        else:
            self.memo[i][j] = max(self.dp(text1, i - 1, text2, j), 
                                  self.dp(text1, i, text2, j - 1))
        return self.memo[i][j]