from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        even_list = ListNode(0)
        last_even = even_list
        last_odd = ListNode(0)
        is_odd = True
        head_memo = head
        while head is not None:
            if is_odd:
                last_odd.next = head
                last_odd = last_odd.next
                is_odd = False
            else:
                last_even.next = head
                last_even = last_even.next
                is_odd = True
            head = head.next
        last_even.next = None
        last_odd.next = even_list.next
        return head_memo


a = Solution()
l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l1.next = l2
l2.next = l3
l3.next = l4

resu = a.oddEvenList(l1)
print(resu)
