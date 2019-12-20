
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        node_dict = {}
        new_head = Node(head.val, None, None)
        node_dict[head] = new_head
        old_cur_point = head
        new_cur_point = new_head
        while old_cur_point is not None:
            if old_cur_point.next is not None:
                the_next = old_cur_point.next
                if the_next not in node_dict:
                    the_new = Node(the_next.val, None, None)
                    node_dict[the_next] = the_new
                else:
                    the_new = node_dict[the_next]
            else:
                the_new = None
            new_cur_point.next = the_new

            if old_cur_point.random is not None:
                the_next = old_cur_point.random
                if the_next not in node_dict:
                    the_new = Node(the_next.val, None, None)
                    node_dict[the_next] = the_new
                else:
                    the_new = node_dict[the_next]
            else:
                the_new = None
            new_cur_point.random = the_new

            new_cur_point = new_cur_point.next
            old_cur_point = old_cur_point.next
        return new_head




a = Solution()
# gas_in = [2,3,4]
# cost_in = [3,4,3]
# cost_in = [3,4,5,1,2]
# cost_in = [4,4,1,5,1]
in_para1 = Node(1, None, None)
in_para2 = Node(2, None, None)
in_para1.next = in_para2
in_para1.random = in_para2
in_para2.random = in_para2
res = a.copyRandomList(None)
print(res)
