# LeetCode 2

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    """
    My confusion was how to separate the cases on:
    What if we have carry after we've done interating through p1 or p2.
    Cases that We have carry but p1 or p2 is not done iterated.
    
    We should take care of this in the while loop because even if this is the case, we still need the same
    algorithm to further calculate carry and digit
    """
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(-1)
        p = dummy
        p1, p2 = l1, l2
        carry = 0
        while p1 or p2 or carry > 0: # If we still have a carry, we need to continue creating new ListNode for it
            val = carry
            if p1:
                val += p1.val
                p1 = p1.next
            if p2:
                val += p2.val
                p2 = p2.next
            carry = val // 10
            val = val % 10
            p.next = ListNode(val)
            p = p.next 
        return dummy.next 
    
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(9)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
l2.next.next.next = ListNode(9)

sol = Solution()
head = sol.addTwoNumbers(l1, l2)
while head:
    print(head.val)
    head = head.next