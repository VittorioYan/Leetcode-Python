from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        last = ListNode(0)
        res = last
        last.next = head
        while head is not None:
            if head.val == val:
                last.next = head.next
            else:
                last = last.next
            head = head.next
        return res.next


a = Solution()
in_para1 = 19
in_para2 = 10
resu = a.isHappy(in_para1)
print(resu)
