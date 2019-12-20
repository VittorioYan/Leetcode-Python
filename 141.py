# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        cur_head = head
        while cur_head is not None:
            if cur_head.val is None:
                return True
            cur_head.val = None
            cur_head = cur_head.next



