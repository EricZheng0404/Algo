"""
We have n linked lists. Link them back to one single linkedlist from the least
to the greatest.
"""
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
            value, i, head = heapq.heappop(pq) # Don't forget to pass pq into heap.heappop()
            p.next = head
            if head.next is not None:
                heapq.heappush(pq, (head.next.val, i, head.next))
            p = p.next
        
        return dummy.next 


"""
This is a divide and conquer solution. We divide the lists into two halves, and
then merge the two halves. We do this recursively until we have only one list.
Then we merge the two lists.

Time complexity: O(nlogk), because height of the tree is logk, meaning we have
logk level of merge. All N nodes are merged at each level, so the time 
complexity is O(nlogk).

Space complexity: O(logk), because we have logk level of merge.
"""
class Solution2:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        if n == 0:
            return None
        return self.mergeHelper(lists, 0, n - 1)

    def mergeHelper(self, lists, l, r):
        if l == r:
            return lists[l]
        mid = l + (r - l)//2
        left = self.mergeHelper(lists, l, mid)
        right = self.mergeHelper(lists, mid + 1, r)
        return self.merge2(left, right)

    def merge2(self, lst1: ListNode, lst2: ListNode()):
        if not lst1:
            return lst2
        if not lst2:
            return lst1
        dummy = ListNode(-1)
        p = dummy
        while lst1 and lst2:
            if lst1.val < lst2.val:
                p.next = lst1
                p = p.next
                lst1 = lst1.next
            else:
                p.next = lst2
                p = p.next
                lst2 = lst2.next
        if lst1:
            p.next = lst1
        else:
            p.next = lst2
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

        

        
        