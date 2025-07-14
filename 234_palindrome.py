"""
234. Palindrome Linked List

Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
"""
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def isPalindrome(self, head):
        p = head
        result = ""
        while p:
            result += str(p.val)
            p = p.next
        return result == result[::-1]
    
class Solution2:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head.next is None:
            return True
        self.left = head
        self.res = True
        self.traverse(head)
        return self.res
    
    def traverse(self, right):
        if right is None:
            return
        self.traverse(right.next)
        # Post-order position checking
        if right.val != self.left.val:
            self.res = False
        # There's no need to worry about left.next would be None
        # Because we only will recurse the length of the list
        self.left = self.left.next
