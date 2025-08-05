from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    """
    There's no unique tree we can build
    """
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # Base case
        if not preorder:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        # We know we have two elements in the list at least
        # Root value from pre-order traversal
        rootVal = preorder[0]
        root = TreeNode(rootVal)
        # The start of the left tree in pre-order traversal
        leftRootVal = preorder[1]
        # The index of the vlue in post-order traversal
        indexLeftRootValPostOrder = postorder.index(leftRootVal)
        root.left = self.constructFromPrePost(preorder[1:1 + indexLeftRootValPostOrder + 1], \
                    postorder[:indexLeftRootValPostOrder + 1])
        root.right = self.constructFromPrePost(preorder[1 + indexLeftRootValPostOrder + 1:], postorder[indexLeftRootValPostOrder + 1:-1]) # In slicing, the second element is not included!!!!!!!!!!!!!!
        return root
        