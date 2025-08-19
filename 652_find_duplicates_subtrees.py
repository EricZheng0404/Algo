from typing import Optional, List
from collections import defaultdict
"""
652. Find Duplicate Subtrees
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.memo = defaultdict(int)
        self.res = set()
        self.serialize(root)
        return list(self.res)

    def serialize(self, root) -> str:
        if not root: 
            return "#"
        # The serialization of the left ree
        left = self.serialize(root.left)
        # The serialization of the right tree
        right = self.serialize(root.right)
        curr = f"{left}, {right}, {root.val}"
        print(curr)
        count = self.memo[curr]
        # If the count of the currString is zero (this currString is new)
        if count == 1:
            self.res.add(root)
        # This step is necessary whenever what
        self.memo[curr] += 1
        return curr
        