"""
LeetCode 26

Input:
- A linked of non-descending nodes

Output: 
- A linked of non-descending nodes with duplicate removed

WARNING:
head could be None

I have two implementation:
One is out-place. I declared a new linked list using dummy node. (Whos's the 
saying we always should use dummy node)
The other one is in-place. I did not declare a new linked list, but work with 
the old linked list.
"""
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Sol:
    # Implementation 1: out-place
    def deleteDuplicates1(self, head):
        if not head:
            return head
        dummy = ListNode(head.val)
        p = dummy
        fast = head.next
        while fast:
            if p.val != fast.val:
                p.next = ListNode(fast.val)
                p = p.next
            fast = fast.next
        return dummy
    
    # Implementation 2: in-place
    def deleteDuplicates1(self, head):
        if not head:
            return None
        slow, fast = head, head
        while fast:
            if slow.val != fast.val:
                slow.next = fast
                slow = slow.next
            fast = fast.next
        # Disconnect the last node from the rest of the linked list
        slow.next = None
        return head # We return head here, slow is at the last of the linked list now
    