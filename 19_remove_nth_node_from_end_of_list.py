
"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]
"""
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # dummy could be a safe rail that is the head is the node to be removed, we have dummy 
        dummy = ListNode(-1)
        dummy.next = head
        # To find the (n- 1)th node from the end
        p = self.findPrev(dummy, n + 1)
        p.next = p.next.next
        return dummy.next
        
    # helper function that find the nth node from the end
    def findPrev(self, head, target):
        # Move p1 to n
        p1 = head
        for _ in range(target):
            p1 = p1.next
        p2 = head
        while p1:
            p1 = p1.next
            p2 = p2.next
        return p2