from typing import List, Optional
from collections import deque, defaultdict
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        if root is None:
            return []
        q.append((root, 0))
        colMap = defaultdict(list)
        colMap[0].append(root.val)
        minCol, maxCol = 0, 0
        while q:
            curr, col = q.popleft()
            if curr.left:
                newCol = col - 1
                q.append((curr.left, newCol))
                minCol = min(minCol, newCol)
                colMap[newCol].append(curr.left.val)
            if curr.right:
                newCol = col + 1
                q.append((curr.right, newCol))
                maxCol = max(maxCol, newCol)
                colMap[newCol].append(curr.right.val)
        return [colMap[c] for c in range(minCol, maxCol + 1)]
