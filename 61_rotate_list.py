"""
Leetcode 61: Rotate List

Given the head of a linked list, rotate the list to the right by k places.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
"""
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or head.next is None:
            return head
        # 1. Make a list of this LinkedList
        stk = []
        while head:
            stk.append(head.val)
            head = head.next
        # 2. Reverse the whole list
        stk.reverse()
        # 3. Reverse n and n - k elements
        n = len(stk)
        newK = k % n
        self.reverseArr(stk, 0, newK - 1) # I fumbled this part
        self.reverseArr(stk, newK, n - 1)
        # 4. Make it back to a LinkedList
        dummy = ListNode(-1)
        p = dummy
        for num in stk:
            p.next = ListNode(num)
            p = p.next
        return dummy.next

    def reverseArr(self, arr, i, j):
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1