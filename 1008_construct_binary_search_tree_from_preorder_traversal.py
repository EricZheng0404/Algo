from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        # Base case
        # print(preorder)
        if not preorder:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        rootVal = preorder[0]
        root = TreeNode(rootVal)
        # We know at least we have two elements in the list
        leftIndex = 1
        # When doing traversal, always check the boundary first
        while leftIndex < len(preorder) and preorder[leftIndex] < rootVal:
            leftIndex += 1
        # We know at last leftIndex is the index of the first element that's 
        # greater than the root value
        root.left = self.bstFromPreorder(preorder[1:leftIndex])
        root.right = self.bstFromPreorder(preorder[leftIndex:])
        return root
        
        