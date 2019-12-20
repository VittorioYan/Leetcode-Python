# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []

        def travel(this_root: TreeNode):
            if not this_root:
                return
            res.append(this_root.val)
            travel(this_root.left)
            travel(this_root.right)

        travel(root)
        return res


a = Solution()
in_para1 = TreeNode(1)
in_para2 = TreeNode(2)
in_para3 = TreeNode(3)
in_para4 = TreeNode(4)
in_para5 = TreeNode(5)
in_para1.right = in_para2
in_para2.left = in_para3
# in_para3.next = in_para4
# in_para4.next = in_para5
# in_para5.next = None
res = a.preorderTraversal(in_para1)
print(res)