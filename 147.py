# Definition for singly-linked list.
import sys

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        def insert_listnode(the_list: ListNode, the_node: ListNode):
            ins_cur_node = the_list
            while ins_cur_node.next is not None:
                if ins_cur_node.val <= the_node.val <= ins_cur_node.next.val:
                    tmp = ins_cur_node.next
                    ins_cur_node.next = the_node
                    the_node.next = tmp
                    return
                ins_cur_node = ins_cur_node.next
            ins_cur_node.next = the_node

        result_head = ListNode(-sys.maxsize)
        cur_head = head
        while cur_head is not None:
            ins_node = cur_head
            cur_head = cur_head.next
            ins_node.next = None
            insert_listnode(result_head, ins_node)

        return result_head.next

a = Solution()
in_para1 = ListNode(4)
in_para2 = ListNode(1)
in_para3 = ListNode(3)
in_para4 = ListNode(2)
in_para5 = ListNode(5)
in_para1.next = in_para2
in_para2.next = in_para3
in_para3.next = in_para4
in_para4.next = in_para5
in_para5.next = None
res = a.insertionSortList(in_para1)
print(res)
