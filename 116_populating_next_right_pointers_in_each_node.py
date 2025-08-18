from typing import Optional
"""
116. Populating Next Right Pointers in Each Node
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        self.traverse(root)
        return root
    
    def traverse(self, root):
        if not root:
            return
        root.left, root.right = root.right, root.left
        self.traverse(root.left)
        self.traverse(root.right)

class Solution2:
    def connect(self, root):
        if not root:
            return root
        self.traverse(root.left, root.right)
        return root

    def traverse(self, left, right):
        if not left or not right:
            return 
        left.next = right
        self.traverse(left.left, left.right)
        self.traverse(right.left, right.right)
        self.traverse(left.right, right.left)