# LeetCode 2

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
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
        while p1 or p2 or carry > 0:
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