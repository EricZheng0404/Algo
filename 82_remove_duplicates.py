"""
LeetCode
"""

class ListNode:
    def __init__(self, val: int, next = None):
        self.val = val
        self.next = next

class Solution(object):
    # Solution 1: Use hash dict
    def deleteDuplicates1(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None:
            return None
        resultDict = {}
        p = head
        while p:
            resultDict[p.val] = resultDict.get(p.val, 0) + 1
            p = p.next
        result = []
        for key, val in resultDict.items():
            if val == 1:
                result.append(key)
        result.sort()
        dummy = ListNode(-1)
        p = dummy
        for i in result:
            p.next = ListNode(i)
            p = p.next
        return dummy.next

    # Implementation 2: Use two new lists
    def deleteDuplicates2(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummyUniq = ListNode(101)
        dummyDuplicate = ListNode(101)
        pUniq, pDuplicate = dummyUniq, dummyDuplicate
        p = head
        while p is not None:
            # if (p.next is not None and p.val == p.next.val) or (p.val == pDuplicate.val):
            if (p.next is not None and p.val == p.next.val) or p.val == pDuplicate.val:
                # if p.next is not None:
                    # print("We are in dup case")
                    # print("p.val is ", p.val)
                    # print("p.next.val is ", p.next.val)
                    pDuplicate.next = p
                    pDuplicate = pDuplicate.next
            else:
                pUniq.next = p
                pUniq = pUniq.next
            p = p.next
            pUniq.next = None
            pDuplicate.next = None
        return dummyUniq.next

    # Implementation 3: Use two pointers
    def deleteDuplicates3(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(101)
        p, q = dummy, head
        while q:
            # We found a duplicate
            if (q.next is not None and q.next.val == q.val):
                # Skip all the duplicates and get to the last duplicate
                while q.next and q.next.val == q.val:
                    q = q.next
                # Skip the last duplicate
                q = q.next
                # If we have reached the end of the list, we need to connect the previous node to None
                # This only happens when the last node is a duplicate
                if q is None:
                    p.next = q
            else:
                p.next = q
                p = p.next
                q = q.next
        return dummy.next
    
if __name__ == "__main__":
    sol = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    sol.deleteDuplicates2(head)

    p = head
    while p is not None:
        print(p.val)
        p = p.next
