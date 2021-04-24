from typing import List
from sortedcontainers import SortedList

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        ans = float('inf')
        pre = -1
        def mid_travel(node:TreeNode):
            nonlocal pre
            nonlocal ans
            if not node:
                return
            mid_travel(node.left)
            if pre!=-1:
                ans = min(ans,node.val-pre)
            pre = node.val
            mid_travel(node.right)

        mid_travel(root)
        return ans


a = Solution()
in_para1 = TreeNode(90)
in_para2 = TreeNode(69)
in_para3 = TreeNode(49)
in_para4 = TreeNode(89)
in_para5 = TreeNode(52)
in_para1.left = in_para2
in_para2.left = in_para3
in_para2.right = in_para4
in_para3.right = in_para5
resu = a.minDiffInBST(in_para1)
print(resu)
