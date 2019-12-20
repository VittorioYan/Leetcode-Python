
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

from queue import Queue
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        res_node = Node(node.val, [])
        ori_node_queue = Queue()
        new_node_queue = Queue()
        ori_node_queue.put(node)
        new_node_queue.put(res_node)
        val_dict = {}
        val_dict[node.val] = res_node
        while not ori_node_queue.empty():
            ori_cur_node = ori_node_queue.get()
            new_cur_node = new_node_queue.get()

            for the_node in ori_cur_node.neighbors:
                if the_node.val not in val_dict:
                    ori_node_queue.put(the_node)
                    new_node = Node(the_node.val, [])
                    new_node_queue.put(new_node)
                    new_cur_node.neighbors.append(new_node)
                    val_dict[the_node.val] = new_node
                else:
                    new_cur_node.neighbors.append(val_dict[the_node.val])

        return res_node

a = Solution()
node1 = Node(1, [])
node2 = Node(2, [])
node3 = Node(3, [])
node4 = Node(4, [])
node1.neighbors.append(node2)
node1.neighbors.append(node4)
node2.neighbors.append(node1)
node2.neighbors.append(node3)
node3.neighbors.append(node4)
node3.neighbors.append(node2)
node4.neighbors.append(node1)
node4.neighbors.append(node3)
a.cloneGraph(node1)











