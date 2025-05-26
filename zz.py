class LinkedNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def recursive(self, head: LinkedNode) -> LinkedNode:
        if head is None:
            return 
        self.recursive(head.next)
        print(head.val)

head = LinkedNode(1)
head.next = LinkedNode(2)
head.next.next = LinkedNode(3)
head.next.next.next = LinkedNode(4)
head.next.next.next.next = LinkedNode(5)

sol = Solution()
sol.recursive(head)