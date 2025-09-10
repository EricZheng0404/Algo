class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        self.memo = [[-1] * (n + 1) for _ in range(m + 1)]
        return self.dp(word1, m - 1, word2, n - 1)
    
    # Return the min # of operation for word[...i] and word2[...j]
    def dp(self, word1, i, word2, j):
        # Base case: when word1 is already done, then we only need to iterate through 
        # the rest of word2
        if i == -1:
            return j + 1
        # In the same fashion, when word2 is done, we only need to iterate through 
        # the rest of word1
        if j == -1:
            return i + 1
        if self.memo[i][j] != -1:
            return self.memo[i][j]
        # If the the char in both word1 and word2 are the same, there's no extra 
        # step from the last step
        if word1[i] == word2[j]:
            return self.dp(word1, i - 1, word2, j - 1)
        self.memo[i][j] = min(
            # Delete word1[i], so i can move forward
            self.dp(word1, i - 1, word2, j) + 1,
            # Insert a letter that matches with word2[j], so we can update j
            self.dp(word1, i, word2, j - 1) + 1,
            # Replace so that word1[i] and word2[i] are the same
            self.dp(word1, i - 1, word2, j - 1) + 1,
            )
        return self.memo[i][j]