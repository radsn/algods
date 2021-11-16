class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_

    @staticmethod
    def reverse_list(self, head):
        curr = head
        prev = None
        while prev:
            next_ = curr.next
            curr.next_ = prev
            prev = curr
            curr = next_
        return prev

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
reverse_list(head).val
