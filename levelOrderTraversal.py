from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Implementation 1: Simple but cannot determine which level the current node is
def levelOrderTraversal1(root):
    if root is None:
        return 
    q = deque()
    q.append(root)

    while q:
        cur = q.popleft()
        print(cur.val)

        if cur.left:
            q.append(cur.left)
        if cur.right:
            q.append(cur.right)

# Implementation 2
def levelOrderTraversal2(root: TreeNode):
    if root is None:
        return 
    q = deque()
    q.append(root)
    depth = 1 # record the current depth, root node is level 1
    
    while q:
        sz = len(q) # how many nodes in the current level
        for i in range(sz): # we exhaust all the nodes in the queue in each level
            cur = q.popleft()
            print(f"depth = {depth}, val = {cur.val}")

            # add cur's left and right to the queue
            if cur.left is not None:
                q.append(cur.left)
            if cur.right is not None:
                q.append(cur.right)
        depth += 1

# Implementation 3: allowing each node to maintain its own path weight sum
class State:
    def __init__(self, node, depth) -> None:
        self.node = node 
        self.depth = depth 

def levelOrderTraversal3(root: TreeNode):
    if root is None:
        return 
    q = deque() 
    q.append(State(root, root.val)) # the path weight sum of the root node is 1
    
    while q:
        cur = q.popleft() 
        # visit the cur node, and know its path weight sum
        print(f"depth: {cur.depth}, val = {cur.node.val}")

        # add the left and right child node of cur to the queue
        if cur.node.left is not None:
            q.append(State(cur.node.left, cur.depth + cur.node.left.val))
        if cur.node.right is not None:
            q.append(State(cur.node.right, cur.depth + cur.node.right.val))



# The constructed binary tree looks like this:
#     1
#    / \
#   2   3
#  /   / \
# 4   5   6
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.left = TreeNode(5)
root.right.right = TreeNode(6)
# levelOrderTraversal1(root)
# levelOrderTraversal2(root)
levelOrderTraversal3(root)