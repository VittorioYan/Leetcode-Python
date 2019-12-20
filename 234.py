from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        def reverseList(root: ListNode) -> ListNode:
            if not root:
                return root
            cur = root
            last = None
            while cur is not None:
                mid = cur.next
                cur.next = last
                last = cur
                cur = mid
            return last
        slow = ListNode(0)
        slow.next = head
        fast = head
        while fast is not None:
            slow = slow.next
            fast = fast.next
            if fast is None:
                break
            fast = fast.next
        rever = reverseList(slow.next)

        while head is not None and rever is not None:
            if head.val != rever.val:
                return False
            head = head.next
            rever = rever.next

        return True



a = Solution()
in_para1 = [1, 2, 3, 1]
in_para2 = 9
l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(1)
l4 = ListNode(1)
l1.next = l2
l2.next = l3
# l3.next = l4

resu = a.isPalindrome(l1)
print(resu)
