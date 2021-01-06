from typing import List, Sequence
import collections
import bisect

#  Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        new_head = ListNode(0)
        new_head.next = head
        small = ListNode(0)
        cur = new_head
        cur_small = small
        while cur.next:
            if cur.next.val<x:
                cur_small.next = ListNode(cur.next.val)
                cur_small = cur_small.next
                cur.next = cur.next.next
            else:
                cur = cur.next
        cur_small.next = new_head.next
        return small.next
        

a = Solution()
in_para1 = ListNode(9)
# in_para2 = ListNode(4)
# in_para3 = ListNode(3)
# in_para4 = ListNode(2)
# in_para5 = ListNode(5)
# in_para6 = ListNode(2)
# in_para1.next = in_para2
# in_para2.next = in_para3
# in_para3.next = in_para4
# in_para4.next = in_para5
# in_para5.next = in_para6
res = a.partition(in_para1,3)
while res:
    print(res.val,sep='->')
    res = res.next
