from typing import List
import math
"""
1104. Path In Zigzag Labelled Binary Tree
"""
class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        path = []
        while label >= 1:
            path.append(label)
            label = label // 2
            if label == 0:
                break
            depth = int(math.log(label, 2))
            levelRange = self.getLevelRange(depth)
            label = levelRange[1] - (label - levelRange[0])
        path.reverse()
        return path
    

    def log(self, x: int) -> int:
        if x == 0:
            return 0
        return int(math.log(x) / math.log(2))

    def getLevelRange(self, depth):
        p = 2 ** depth
        return [p, p * 2 - 1]