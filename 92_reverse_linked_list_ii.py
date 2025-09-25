# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        l = head
        # We get the prev here
        for _ in range(left - 2):
            l = l.next
        # l.next should be the head for the reversed list
        # Right is the index of the last element (!)
        l.next = self.reverse(l.next, right - left + 1)  
        return head
    
    def reverse(self, head, right):
        if not head or not head.next:
            return head
        prev, curr, next = None, head, head.next
        for _ in range(right):
            curr.next = prev
            prev = curr
            curr = next
            if next.next:
                next = next.next
        # The head is Node(2)
        head.next = curr
        # Prev is Node(4)
        return prev
        
        
        