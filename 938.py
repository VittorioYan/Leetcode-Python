# Definition for a binary tree node.
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        ans = 0
        def travel(node:TreeNode):
            nonlocal ans
            if low<=node.val<=high:
                ans+=node.val
                # if node.left:
                #     travel(node.right)
                # if node.left:
                #     travel(node.left)
            if node.val >=low:
                if node.left:
                    travel(node.left)
            if node.val <=high:
                if node.right:
                    travel(node.right)   

        travel(root)
        return ans

a = Solution()
in_para1 = TreeNode(10)
in_para2 = TreeNode(5)
in_para3 = TreeNode(15)
in_para4 = TreeNode(3)
in_para5 = TreeNode(7)
in_para6 = TreeNode(18)
in_para1.right = in_para3
in_para1.left = in_para2
in_para2.left = in_para4
in_para2.right = in_para5
in_para3.right = in_para6
res = a.rangeSumBST(in_para1,7,15)
print(res)