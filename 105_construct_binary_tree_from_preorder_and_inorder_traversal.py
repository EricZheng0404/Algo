from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.build(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder))

    def build(self, preorder, preStart, preEnd, inorder, inStart, inEnd):
        if preStart > preEnd:
            return None
        root = preorder[preStart]
        indexInOrder = inorder.index(root)
        leftTreeSize = indexInOrder - inStart
        root = TreeNode(root)
        root.left = self.build(preorder, preStart + 1, preStart + leftTreeSize, inorder, inStart, indexInOrder - 1)
        root.right = self.build(preorder, preStart + 1 + leftTreeSize, preEnd, inorder, indexInOrder + 1, inEnd)
        return root        