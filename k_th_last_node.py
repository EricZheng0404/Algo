# To find the k-th node from the head
# 1-index
# For example, 1 -> 4 -> 3 -> 10 -> 5 -> 6 with k = 2, the result should be 5
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def findFromEnd(head: ListNode, k: int) -> ListNode:
    p1 = head
    for _ in range(k):
        p1 = p1.next 
    
    p2 = head 
    while p1:
        p1 = p1.next # At last, p1 will be None
        p2 = p2.next
    return p2

# 19_remove_nth_node_from_end_of_list
# Remove the n-th node fromo the back.
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        def findNode(head, target):
            p1 = head
            for _ in range(target):
                p1 = p1.next
            p2 = head
            while p1:
                p1 = p1.next
                p2 = p2.next
            return p2
        
        dummy = ListNode(-1)
        dummy.next = head
        # dummy is added as guardrail so that even if we're removing the first 
        # ListNode, we still have a previous node
        prev = findNode(dummy, n + 1) # Should start from dummy instead of head
        prev.next = prev.next.next

        return dummy.next

if __name__ == "__main__":
    # Create linked list: 1 -> 4 -> 3 -> 10 -> 5 -> 6
    head = ListNode(1)
    head.next = ListNode(4)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(2)

    result = findFromEnd(head, 2)
    print(result.val)