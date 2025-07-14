"""
LeetCode 160: Intersection of two linked lists
Give two heads of two linked lists
Return the node at which two lists interesct.
If there's no intersection, return None
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def getIntersectionNode(headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # I forgot about the edge case where one of the lists is empty
        if not headA or not headB:
            return None
        p1 = headA
        p2 = headB
        while p1 != p2: 
            p1 = p1.next if p1 else headB
            p2 = p2.next if p2 else headA
        return p1


# Test case where two lists are of the same length
# a: 0 -> 1 -> 2
a = ListNode(0)
a.next = ListNode(1)
a.next.next = ListNode(2)
# b: 3 -> 4 -> 5
b = ListNode(3)
b.next = ListNode(4)
b.next.next = ListNode(5)

print(getIntersectionNode(a, b))