# Find the middle node in the linked list
# Even if there're even number of node, the function will return the second middle node
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

if __name__ == "__main__":
    # Create linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    sol = Solution()
    result = sol.middleNode(head)

    # Print result
    print(result.val)  # Should print 3 since it's the middle node