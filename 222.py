# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        last_depth = -1

        def find(node: TreeNode, depth, node_no):
            nonlocal last_depth
            if node.right is None:
                if node.left is not None:
                    raise Exception(node_no * 2)
                if last_depth == -1:
                    last_depth = depth
                else:
                    if depth > last_depth:
                        raise Exception(node_no)
                return

            find(node.right, depth + 1, node_no * 2 + 1)
            find(node.left, depth + 1, node_no * 2)

        try:
            find(root, 1, 1)
            return 2**last_depth-1
        except Exception as err:
            return int(str(err))


a = Solution()
in_para1 = [1, 5, 9, 1, 5, 9]
t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
t1.left = t2
t1.right = t3
# t2.left = t4

in_para2 = 2
resu = a.countNodes(t1)
print(resu)
