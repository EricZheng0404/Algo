"""
206. Reversed Linked List
Given the head of a linked list, reverse the list
"""

class ListNode:
    def __init__(self, val: int, next = None):
        self.val = val
        self.next = next



node0 = ListNode(0)
node0.next = ListNode(1)
node0.next.next = ListNode(2)

cur = node0
while cur:
    print(cur.val)
    cur = cur.next

def reverse(head: ListNode):
    if head is None:
        return None
    cur = head
    prev = None
    while cur:
        next = cur.next
        cur.next = prev 
        next.next = cur 
        prev = cur
        cur = next 
    return cur

newHead = reverse(node0)
print(newHead.val)