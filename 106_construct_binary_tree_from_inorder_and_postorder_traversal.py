from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder: 
            return None
        if len(inorder) == 1:
            return TreeNode(inorder[0])
        rootVal = postorder[-1]
        root = TreeNode(rootVal)
        rootIndexInOrder = inorder.index(rootVal)
        root.left = self.buildTree(inorder[0:rootIndexInOrder], \
                    postorder[:rootIndexInOrder])
        root.right = self.buildTree(inorder[rootIndexInOrder + 1:], \
                                    postorder[rootIndexInOrder:-1])
        return root  