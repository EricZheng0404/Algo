# We have a linked list and an x as inputs.
# Put all the ListNodes less than x before x, and put all the ListNodes greater
# than or equal to x to the right of x

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    # Implentation 1: create new node
    def partition1(self, head, x):
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
            value = p.val # create new node rather than directly link p1.next to p to break cycle
            if value < x:
                p1.next = ListNode(value)
                p1 = p1.next
            else:
                p2.next = ListNode(value)
                p2 = p2.next
            p = p.next

        p1.next = dummy2.next
        return dummy1.next
    
    # Implementation2: Disconnect
    def partition2(self, head, x):
        dummy1 = ListNode(-1)
        dummy2 = ListNode(-1)
        p1, p2 = dummy1, dummy2
        p = head
        
        while p:
            value = p.val # create new node rather than directly link p1.next to p to break cycle
            if value < x:
                p1.next = ListNode(value)
                p1 = p1.next
            else:
                p2.next = ListNode(value)
                p2 = p2.next
            temp = p.next
            p.next = None
            p = temp
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
    # Implementation 1    
    result = sol.partition1(head, 3)
    printval1 = ""
    while result:
        printval1 += str(result.val)
        result = result.next
    print(f"Result1: {printval1}")

    # Implementation 2
    result2 = sol.partition2(head, 3)
    printval2 = ""
    while result2:
        printval2 += str(result2.val)
        result2 = result2.next
    print(f"Result2: {printval2}")



