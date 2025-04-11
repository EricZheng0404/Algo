from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.children = []

# BFS
def traverse_n_ary_tree(root, preorder, postorder):
    if root is None:
        return 
    preorder.append(root.val) # Pre-order traversal
    for child in root.children:
        traverse_n_ary_tree(child, preorder, postorder)
    postorder.append(root.val) # Post-order traversal

# DFS Implementation 1
def levelOrderTraversal1(root):
    if root is None:
        return
    q = deque()
    q.append(root) 

    while q:
        cur = q.popleft()
        print(cur.val)

        for child in cur.children:
            q.append(child)

# DFS Implementation2, with depth
def levelOrderTraversal2(root):
    if root is None:
        return
    q = deque() 
    q.append(root) 
    depth = 1

    while q:
        size = len(q) 
        for i in range(size):
            cur = q.popleft()
            print(f"val is {cur.val}, depth is {depth}")
            for child in cur.children:
                q.append(child)
        
        depth += 1

# DFS Implementation 3
class State:
    def __init__(self, node, depth) -> None:
        self.node = node
        self.depth = depth

def levelOrderTraversal3(root):
    if root is None:
        return
    q = deque()
    q.append(State(root, root.val))

    while q:
        state = q.popleft() 
        cur = state.node
        depth = state.depth
        print(f"depth = {depth}, val = {cur.val}")

        for child in cur.children:
            q.append(State(child, depth + child.val))
        
        

        
#       1
#    /  |  \
#   2   3   4
#  /   / 
# 5   6   
def simpleTree():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node1.children = [node2, node3, node4]
    node2.children = [node5]
    node3.children = [node6]
    return node1

if __name__ == "__main__":
    node1 = simpleTree()
    preorder = []
    postorder = []
    traverse_n_ary_tree(node1, preorder, postorder)
    # print(f"PreOrder: {preorder}") # Output: 1, 2, 5, 3, 6, 4
    # print(f"PostOrder: {postorder}") # Output: 5, 2, 6, 3, 4, 1
    # levelOrderTraversal1(node1) # Output: 1, 2, 3, 4, 5, 6
    # levelOrderTraversal2(node1)
    levelOrderTraversal3(node1)