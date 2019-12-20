from typing import List


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        node_queue = []
        node_queue.append(root)
        res = []
        while node_queue:
            cur_node = node_queue.pop(0)
            if cur_node is None:
                res.append('null')
            else:
                res.append(str(cur_node.val))
                node_queue.append(cur_node.left)
                node_queue.append(cur_node.right)
        pointer = 0
        for i in range(len(res) - 1, -1, -1):
            if res[i] != 'null':
                pointer = i + 1
                break
        return '[' + ','.join(res[:pointer]) + ']'

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 2:
            return None
        data = data[1:-1]

        res = data.split(',')
        n = len(res)
        if n == 0:
            return None

        if res[0] == 'null':
            return None
        root = TreeNode(int(res[0]))
        node_queue = [root]
        pointer = 1
        while pointer < len(res) and node_queue:
            cur_node = node_queue.pop(0)
            if res[pointer] != 'null':
                cur_node.left = TreeNode(int(res[pointer]))
                node_queue.append(cur_node.left)
            pointer += 1
            if pointer < len(res) and res[pointer] != 'null':
                cur_node.right = TreeNode(int(res[pointer]))
                node_queue.append(cur_node.right)
            pointer += 1

        return root


codec = Codec()
in_para1 = [1, 2, 3, 1]
in_para2 = 9
t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
t5 = TreeNode(5)
t1.left = t2
t1.right = t3
t3.left = t4
t3.right = t5
resu = codec.serialize(codec.deserialize('[1,2]'))
print(resu)
