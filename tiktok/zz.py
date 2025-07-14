class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return self.val

def remove_duplicates(head: ListNode) -> ListNode:
    if not head:
        return None  
    
    current = head
    while current and current.next: 
        if current.val == current.next.val:  
            current.next = current.next.next  
        current = current.next  
    
    return head

# Example 1
head1 = ListNode(1)
head1.next = ListNode(1)
head1.next.next = ListNode(2)
head1.next.next.next = ListNode(3)
head1.next.next.next.next = ListNode(3)
head1.next.next.next.next.next = ListNode(3)

removed = remove_duplicates(head1)

while removed:
    print(removed.val)
    removed = removed.next