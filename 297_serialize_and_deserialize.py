from collections import deque
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        self.serializeHelper(root, res)
        return "".join(res)
        
    def serializeHelper(self, root, res):
        # Base case: If root is None
        if not root:
            res.append("#")
            res.append(",")
            return # I forgot to return in here
        # Pre-order position
        res.append(str(root.val))
        res.append(",")
        self.serializeHelper(root.left, res)
        self.serializeHelper(root.right, res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        tree = deque(data.split(","))
        return self.deserializeHelper(tree)

    def deserializeHelper(self, tree):
        # Base case: If the list is empty, return
        if not tree:
            return None
        curr = tree.popleft()
        if curr == "#":
            return None
        root = TreeNode(int(curr))
        # We use deque to control the flow
        root.left = self.deserializeHelper(tree)
        root.right = self.deserializeHelper(tree)
        return root
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))