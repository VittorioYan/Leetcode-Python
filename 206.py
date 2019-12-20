from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        cur = head
        last = None
        while cur is not None:
            mid = cur.next
            cur.next = last
            last = cur
            cur = mid
        return last

a = Solution()
in_para1 = ListNode(1)
in_para2 = ListNode(2)
in_para3 = ListNode(3)
in_para4 = ListNode(4)
in_para5 = ListNode(5)
in_para1.next = in_para2
in_para2.next = in_para3
in_para3.next = in_para4
in_para4.next = in_para5
in_para5.next = None

resu = a.reverseList(in_para1)
print(resu)
