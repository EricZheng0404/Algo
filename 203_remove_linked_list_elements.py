# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        p = dummy
        p.next = head
        while p and p.next:
            while p and p.next and p.next.val == val:
                p.next = p.next.next
            p = p.next
        return dummy.next
