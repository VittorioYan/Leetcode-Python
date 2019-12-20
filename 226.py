# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def inverse(node:TreeNode):
            if node is None:
                return
            mid_node = node.left
            node.left = node.right
            node.right = mid_node
            inverse(node.right)
            inverse(node.left)
        inverse(root)
        return root

a = Solution()
in_para1 = [1, 2, 3, 1]
in_para2 = 9
t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
t1.left = t2
t1.right = t3
t2.left = t4
resu = a.invertTree(t1)
print(resu)