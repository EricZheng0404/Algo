from typing import List
from collections import defaultdict
class MagicDictionary:

    def __init__(self):
        self.words = defaultdict(list)

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.words[len(word)].append(word)

    def search(self, searchWord: str) -> bool:
        length = len(searchWord)
        if length not in self.words:
            return False
        wordList = self.words[length]
        for word in wordList:
            diff = 0
            for a, b in zip(searchWord, word):
                if a != b:
                    diff += 1
                    if diff > 1:
                        break
            if diff == 1:
                return True
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)