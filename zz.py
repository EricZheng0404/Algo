class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reOrder(head):
    stk = []
    p = head
    while p:
        stk.append(p)
        p = p.next
    print(stk)

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

ordered_head = reOrder(head)