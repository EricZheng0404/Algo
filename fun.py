class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Create a linked list: 0 -> 1 -> 2 -> 3 -> 4
head = ListNode(0)
curr = head
for i in range(1, 5):
    curr.next = ListNode(i)
    curr = curr.next

p1 = head
for _ in range(2):
    print(p1.val)
    p1 = p1.next
print(p1.val)
