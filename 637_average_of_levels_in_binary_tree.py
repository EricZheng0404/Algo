from typing import List, Optional
from collections import deque
"""
637. Average of Levels in Binary Tree
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        q = deque([root])
        while q:
            levelSum = 0
            size = len(q)
            for _ in range(size):
                curr = q.popleft()
                levelSum += curr.val
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            res.append(levelSum/size)
        return res