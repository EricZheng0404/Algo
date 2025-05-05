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
        p1 = headA
        p2 = headB
        while p1 != p2:
            print(f"p1 is {p1.val if p1 else None}")
            print(f"p2 is {p2.val if p2 else None}")
            print()
            p1 = p1.next if p1 else headB
            p2 = p2.next if p2 else headA
        return p1


# Test case where two lists intersect
# Create the intersection node and shared portion
intersection = ListNode(8)
intersection.next = ListNode(4)
intersection.next.next = ListNode(5)

# Create list A: 4->1->(8->4->5)
headA = ListNode(4)
headA.next = ListNode(1)
headA.next.next = intersection

# Create list B: 5->6->1->(8->4->5)
headB = ListNode(5)
headB.next = ListNode(6)
headB.next.next = ListNode(1)
headB.next.next.next = intersection

# Test the function
# result = getIntersectionNode(headA, headB)
# print(result.val)  # Should print 8


# Test2
# a: 0 -> 1 -> 2
a = ListNode(0)
a.next = ListNode(1)
a.next.next = ListNode(2)
# b: 3 -> 4 -> 5 -> 6
b = ListNode(3)
b.next = ListNode(4)
b.next.next = ListNode(5)
b.next.next.next = ListNode(6)
c = getIntersectionNode(a, b)
print(f"c is {c}")
