# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(-1)
        p = dummy
        p1 = list1
        p2 = list2

        while p1 is not None and p2 is not None:
            # print(f"p1.val is {p1.val}, p2.val is {p2.val}")
            if p1.val < p2.val:
                p.next = p1 
                p1 = p1.next
            else:
                p.next = p2
                p2 = p2.next
            # print(f"p.next.val is now {p.next.val}")
            p = p.next 

        if p1 is not None:
            p.next = p1 
        if p2 is not None:
            p.next = p2
        
        return dummy.next
    
if __name__ == "__main__":
    list1 = ListNode(1)
    list1.next = ListNode(3)
    list1.next.next = ListNode(5)
    list1.next.next.next = ListNode(6)

    list2 = ListNode(2)
    list2.next = ListNode(4)
    list2.next.next = ListNode(7)
    list2.next.next.next = ListNode(8)

    # list1 = 1 -> 3 -> 5 -> 6
    # list2 = 2 -> 4 -> 7 -> 8

    sol = Solution()
    root = sol.mergeTwoLists(list1, list2)
    cur = root

    while cur is not None:
        print(cur.val)
        cur = cur.next

