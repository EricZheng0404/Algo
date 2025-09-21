"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        originNode = {}
        # First traversal: Set up and initialize all nodes
        p = head
        while p:
            # if p not in originNode:
                originNode[p] = Node(p.val)
                p = p.next
        # Second traversal: Set up the links
        p = head
        while p:
            if p.next:
                originNode[p].next = originNode[p.next]
            if p.random:
                originNode[p].random = originNode[p.random]
            p = p.next
        # Return the head
        return originNode[head]
        