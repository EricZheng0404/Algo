"""
206. Reversed Linked List
Given the head of a linked list, reverse the list
"""
from typing import Optional
class ListNode:
    def __init__(self, val: int, next = None):
        self.val = val
        self.next = next



class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        # the curr is None at the last iteration
        return prev

class Solution2:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        # 4 -> 5 -> None
        last = self.reverseList(head.next) # last = 5
        head.next.next = head # 4 -> 5 -> 4
        head.next = None # 4 -> None
        return last