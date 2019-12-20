# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []

        def travel(this_root: TreeNode):
            if not this_root:
                return
            travel(this_root.left)
            travel(this_root.right)
            res.append(this_root.val)
        travel(root)
        return res

