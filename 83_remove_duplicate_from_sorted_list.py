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
        """
        This is a two pointer problem.
        We use two pointers to traverse the linked list.
        We use slow pointer to keep track of the last node we need to keep.
        We use fast pointer to traverse the linked list.
        If the value of the fast pointer is not equal to the value of the slow pointer,
        we set the next pointer of the slow pointer to the fast pointer.
        We then move the slow pointer to the next node.
        """
        if not head:
            return None
        slow, fast = head, head
        while fast:
            if slow.val != fast.val:
                slow.next = fast # key difference from array two pointer. 
                # We don't need to update slow first, .next handles it.
                slow = slow.next
            fast = fast.next
        # Disconnect the last node from the rest of the linked list
        slow.next = None
        return head # We return head here, slow is at the last of the linked list now
    