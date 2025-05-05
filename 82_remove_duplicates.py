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