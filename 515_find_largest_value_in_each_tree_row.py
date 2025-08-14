from typing import List, Optional
from collections import deque
"""
515. Find Largest Value in Each Tree Row
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return []
        q = deque([root])
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
            res.append(max(level))
        return res

