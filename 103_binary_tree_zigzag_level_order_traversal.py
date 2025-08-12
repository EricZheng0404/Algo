from typing import List, Optional
from collections import deque
"""
103. Binary Tree Zigzag Level Order Traversal
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = deque()
        q.append(root)
        reversed_ = False
        while q:
            level = []
            size = len(q)
            for _ in range(size):
                curr = q.popleft()
                level.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            if reversed_:
                level.reverse()
            reversed_ = not reversed_
            res.append(level)
        return res
            

