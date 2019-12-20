# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return head
        if head.next is None:
            return head.next
        slow = head.next
        fast = slow.next
        while slow != fast:
            if fast is None:
                return fast
            fast = fast.next
            if fast is None:
                return fast
            fast = fast.next
            slow = slow.next
        ptr1 = head
        ptr2 = slow
        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        return ptr1


