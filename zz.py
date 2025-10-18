class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.down = None

head = Node(1)
head.down = Node(2)
head.down.next = Node(3)
head.next = Node(4)
head.next.next = Node(5)
head.next.next.down = Node(6)
head.next.next.down.down = Node(7)
head.next.next.down.down.next = Node(8)
head.next.next.down.down.next.next = Node(9)

class Solution:
    def flatten(self, node):
        dummy = Node(-1)
        self.p = dummy
        self.traversal(node)
        return dummy.next
    
    def traversal(self, node):
        if not node:
            return None
        down_node = node.down
        # next_node = node.next
        self.p.next = node
        self.p.down = None
        self.p = self.p.next
        self.traversal(down_node)
        self.traversal(node.next)

sol = Solution()
res = sol.flatten(head)

while res:
    print(res.val)
    res = res.next