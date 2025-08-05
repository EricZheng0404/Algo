from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    The gist of the question is:
    1. To use pre-order traversal list to get the root: which is always the first 
    element in the list.
    2. In turn, to use in-order traversal list to get the size of the left tree for 
    further recursion.
    """
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        # For faster lookup in in-order list
        self.lookup = {}
        for i, num in enumerate(inorder):
            self.lookup[num] = i
        return self.build(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)
    
    # We use preStart, preEnd, inStart, and inEnd to control the level of the recursion
    def build(self, preorder, preStart, preEnd, inorder, inStart, inEnd):
        # Base case: If preStart is less than preEnd, that means there's no elements
        if preStart > preEnd:
            return None
        if inStart > inEnd:
            return None
        # To get the root, which is the start of the pre-order traversal
        rootVal = preorder[preStart] # I made a mistake putting 0 is here
        # Find this rootVal in in-order traversal. This index is not the number of 
        # elements in the left tree
        indexOfRootInInOrder = self.lookup[rootVal]
        root = TreeNode(rootVal)
        # To calculate the size of the left tree
        leftSize = indexOfRootInInOrder - inStart
        root.left = self.build(preorder, preStart + 1, preStart + leftSize,\
        inorder, inStart, indexOfRootInInOrder - 1)
        root.right = self.build(preorder, preStart + leftSize + 1, preEnd, inorder, indexOfRootInInOrder + 1, inEnd)
        return root