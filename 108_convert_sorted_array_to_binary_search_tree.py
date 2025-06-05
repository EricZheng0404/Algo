"""
LeetCode 108. Convert Sorted Array to Binary Search Tree
"""
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
This is subproblem decomposition.
Because the input array is sorted, we can use the middle element as the root of the tree.
Then the left and right subtrees are the left and right subarrays.
We can use the same method to make the left and right subtrees.

This is a close index problem.
So, is there is one element case, it's [x, x] for example. 

Time complexity: O(n)
Space complexity: O(n)
"""
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.makeTree(nums, 0, len(nums) - 1)

    # helper function to make the tree
    def makeTree(self, nums, left, right):
        # base case: if the left index is greater than the right index, means
        # the index range is empty, return None
        if left > right:
            return None
        # find the middle element of the subarray
        mid = left + (right - left) // 2
        root = TreeNode(nums[mid])
        root.left = self.makeTree(nums, left, mid - 1)
        root.right = self.makeTree(nums, mid + 1, right)
        return root