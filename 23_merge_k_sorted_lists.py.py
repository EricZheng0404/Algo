# Definition for singly-linked list.
import heapq

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other) -> bool:
        return self.val < other


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        if lists is None or len(lists) == 0:
            return None
        
        dummy = ListNode(1)
        p = dummy
        # Priority queue, min-heap
        pq = []

        # Insert all heads in the lists into the min-heap
        for i, head in enumerate(lists):
            if head is not None:
                heapq.heappush(pq, (head.val, i, head)) # Insert a tuple 
        
        while pq:
            value, i, head = heapq.heappop(pq)
            p.next = head
            if head.next is not None:
                heapq.heappush(pq, (head.next.val, i, head.next))
            p = p.next
        
        return dummy.next 
    
if __name__ == "__main__":
    # Create first linked list: 1 -> 4 -> 5
    list1 = ListNode(1)
    list1.next = ListNode(4)
    list1.next.next = ListNode(5)

    # Create second linked list: 1 -> 3 -> 4
    list2 = ListNode(1)
    list2.next = ListNode(3)
    list2.next.next = ListNode(4)

    # Create third linked list: 2 -> 6
    list3 = ListNode(2)
    list3.next = ListNode(6)

    lists = [list1, list2, list3]

    sol = Solution()
    result = sol.mergeKLists(lists)

    # Print result
    curr = result
    while curr:
        print(curr.val)
        curr = curr.next

        

        
        