"""
LeetCode 127. Word Ladder

The question I had was I thought there would be multiple branches to visit 
the same word. But in fact, we only have one branch to visit the same word,
and that branch is the shortest one to visit the word. That's why we have 
visited set to avoid visiting the same word multiple times.
"""
from collections import deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        # Cause we constantly check if newWord is in wordList, set is more efficient
        wordList = set(wordList) 
        q = deque()
        q.append(beginWord)
        visited = set()
        visited.add(beginWord)
        # The beginWord count as one word
        step = 1
        
        while q:
            sz = len(q)
            for _ in range(sz):
                cur = q.popleft()
                if cur == endWord:
                    return step
                for i in range(len(cur)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        newWord = cur[:i] + c + cur[i + 1:]
                        if newWord in wordList and newWord not in visited:
                            if newWord == endWord:
                                return step + 1
                            q.append(newWord)
                            visited.add(newWord)
            step += 1
        return 0 
