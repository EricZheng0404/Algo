# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        dummy1 = ListNode(-1)
        dummy2 = ListNode(-1)
        p1, p2 = dummy1, dummy2
        p = head
        
        while p:
            value = p.val
            if value < x:
                p1.next = ListNode(value)
                p1 = p1.next
            else:
                p2.next = ListNode(value)
                p2 = p2.next
            p = p.next
            
        p1.next = dummy2.next
        return dummy1.next
    
if __name__ == "__main__":
    # Create linked list: 1 -> 4 -> 3 -> 2 -> 5 -> 2
    head = ListNode(1)
    head.next = ListNode(4)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(2)

    sol = Solution()
    result = sol.partition(head, 3)

    # Print result
    curr = result
    while curr:
        print(curr.val)
        curr = curr.next


