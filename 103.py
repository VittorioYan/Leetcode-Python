# Definition for a binary tree node.
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        def travel(deep:int,node:TreeNode):
            if deep>=len(ans):
                ans.append([node.val])
            else:
                ans[deep]+=[node.val]
            if node.left!=None:
                travel(deep+1,node.left)
            if node.right!=None:
                travel(deep+1,node.right)

        travel(0,root)
        for i in range(len(ans)):
            if i%2==1:
                ans[i].reverse()
        return ans

a = Solution()
in_para1 = TreeNode(3)
in_para2 = TreeNode(9)
in_para3 = TreeNode(20)
in_para4 = TreeNode(15)
in_para5 = TreeNode(7)
in_para1.right = in_para3
in_para1.left = in_para2
in_para3.left = in_para4
in_para3.right = in_para5
res = a.zigzagLevelOrder(in_para1)
print(res)