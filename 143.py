# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return head
        node_list = []
        cur_node = head
        while cur_node is not None:
            node_list.append(cur_node)
            cur_node = cur_node.next
        node_len = len(node_list)
        cur_node = ListNode(0)
        for i in range(node_len//2):
            cur_node.next = node_list[i]
            cur_node = cur_node.next
            cur_node.next = node_list[-1-i]
            cur_node = cur_node.next
        if node_len % 2 != 0:
            cur_node.next = node_list[node_len//2]
            cur_node = cur_node.next
        cur_node.next = None
        return head

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
res = a.reorderList(in_para1)
print(res)






