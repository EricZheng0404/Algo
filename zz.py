class Node:
    def __init__(self, val):
        self.val = val
        self.children = []

    def add_child(self, child):
        self.children.append(child)
    
    def __str__(self):
        return f"Node({self.val})"

def backtrack(root):
    if root is None:
        return

    for child in root.children:
        # Make a choice
        print(f"I make a choice on the edge between {root} and {child}")

        backtrack(child)

        # Undo the choice
        print(f"I undo the choice on the edge between {root} and {child}")
def dfs(root):
    if root is None:
        return
    
    # Make a choice
    print(f"I make a choice at node {root}")

    for child in root.children:
        dfs(child)

    # Undo the choice
    print(f"I undo the choice at node {root}")
root = Node(1)
root.children = [Node(2), Node(3)]
root.children[0].children = [Node(4), Node(5)]
# backtrack(root)
dfs(root)