# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]: 
        curr = head
        while curr:
            # to retain m nodes
            # we only need (m - 1) steps to get to the last node we need to keep
            for _ in range(1, m):
                if curr is None:
                    break
                curr = curr.next
            if curr is None:
                break
            # skip n nodes
            # temp wll be at the last nodes we want to keep
            temp = curr.next
            for _ in range(n):
                if temp is None:
                    break
                temp = temp.next
            curr.next = temp
            curr = temp
        return head
            
        