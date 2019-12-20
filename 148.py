# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

import sys


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None:
            return head

        def q_sort(node_list: ListNode):
            if node_list is None:
                return None, None
            small = ListNode(-sys.maxsize)
            big = ListNode(-sys.maxsize)
            mid = ListNode(-sys.maxsize)
            cur_small = small
            cur_big = big
            cur_mid = mid
            flag_val = node_list.val
            cur_node = node_list

            while cur_node is not None:
                if cur_node.val < flag_val:
                    cur_small.next = cur_node
                    cur_small = cur_small.next
                elif cur_node.val > flag_val:
                    cur_big.next = cur_node
                    cur_big = cur_big.next
                else:
                    cur_mid.next = cur_node
                    cur_mid = cur_mid.next
                cur_node = cur_node.next

            cur_small.next = None
            cur_big.next = None
            cur_mid.next = None

            after_s_begin, after_s_end = q_sort(small.next)
            after_b_begin, after_b_end = q_sort(big.next)

            res = ListNode(0)
            cur_res = res
            if after_s_end is not None:
                cur_res.next = after_s_begin
                cur_res = after_s_end
            cur_res.next = mid.next
            cur_res = cur_mid

            if after_b_begin is not None:
                cur_res.next = after_b_begin
                cur_res = after_b_end
            return res.next, cur_res

        res_start, res_end = q_sort(head)
        res_end.next = None

        return res_start


a = Solution()
in_para1 = ListNode(1)
in_para2 = ListNode(1)
in_para3 = ListNode(2)
in_para4 = ListNode(2)
in_para5 = ListNode(3)
in_para1.next = in_para2
in_para2.next = in_para3
in_para3.next = in_para4
in_para4.next = in_para5
in_para5.next = None
resu = a.sortList(in_para1)
print(resu)
