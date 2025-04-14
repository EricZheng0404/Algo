# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    # LeetCode 141:
    # Input: a linked list with possible a cycle node
    # Output: True if the linkedlist has a cycle, False if not
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow, fast = head, head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next.next
            if slow == fast:
                return True
        return False
    
    # LeetCode 142:
    # To identify the cycle node
    # If there's a cycle in the input linkedlist, output the cycle node
    # If not, return None
    def detectCycleNode(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next
            if slow == fast: 
                break
        # if fast can arrive to None, that means there's no cycle
        if fast is None or fast.next is None:
            return None
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow



if __name__ == "__main__":
    # Create linked list with cycle: 3 -> 2 -> 0 -> -4 -> (points back to 2)
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0) 
    head.next.next.next = ListNode(-4)
    head.next.next.next.next = head.next  # Create cycle pointing to node with val 2

    # Create solution instance
    sol = Solution()
    
    # Test case 1: List with cycle
    result1 = sol.hasCycle(head)
    assert result1 == True
    # print(f"result is {sol.detectCycleNode(head).val}")

    # Test case 2: List without cycle
    # List: 1 -> 2 -> 3 -> 4 -> null
    head2 = ListNode(1)
    head2.next = ListNode(2)
    head2.next.next = ListNode(3)
    head2.next.next.next = ListNode(4)
    
    result2 = sol.hasCycle(head2)
    assert result2 == False
    # print(f"result is {sol.detectCycleNode(head2)}")


    

        