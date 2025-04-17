# Return a ListNode with only odd elements

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        result = ""
        cur = self 
        while cur:
            result += f"Node is {cur.val}\n"
            cur = cur.next
        return result

# Implementation 1: breaking links
def deleteEven1(listHead):
    dummy = ListNode()
    p = dummy
    cur = listHead

    while cur:
        if cur.val % 2 != 0:
            p.next = cur 
            p = p.next 
            temp = cur.next # we remember what the next node is
            cur.next = None # We cancel the link from cur to next
            cur = temp # We jump to next
        else:
            cur = cur.next
    return dummy.next 

# Implementation 2: Create new node 
def deleteEven2(listHead):
    dummy = ListNode()
    p = dummy 
    cur = listHead
    while cur:
        value = cur.val
        if value % 2 != 0:
            p.next = ListNode(value)
            p = p.next 
        cur = cur.next
    # p.next = None, we don't need it because next for a ListNode is by default None
    return dummy.next

if __name__ == "__main__":
    # 1 -> 2 -> 3 -> 4 -> 5 -> 6
    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(3)
    list1.next.next.next = ListNode(4)
    list1.next.next.next.next = ListNode(5)
    list1.next.next.next.next.next = ListNode(6)

    head = deleteEven1(list1)

    # cur = head
    # while cur:
    #     print(cur.val)
    #     cur = cur.next

    head2 = deleteEven2(list1)
    print(head2)