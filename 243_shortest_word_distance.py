class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        p1 = -1
        p2 = -1
        minDistance = float("inf")
        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                p1 = i
                
            if wordsDict[i] == word2:
                p2 = i
            if p1 != -1 and p2 != -1: # Because the base case would be 0
                minDistance = min(minDistance, abs(p1 - p2))
            
        return minDistance