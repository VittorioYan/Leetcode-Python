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
        all_num = []
        def travel(node:TreeNode):
            all_num.append(node.val)
            if node.left:
                travel(node.left)
            if node.right:
                travel(node.right)
        ans = float('inf')
        travel(root)
        for i in range(len(all_num)):
            for j in range(i+1,len(all_num)):
                ans = min(ans,abs(all_num[i]-all_num[j]))
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
