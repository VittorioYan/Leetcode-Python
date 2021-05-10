# Definition for a binary tree node.
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        trace1,trace2 = [],[]
        def travel(node:TreeNode,trace:list):
            if node.left==None and node.right==None:
                trace.append(node.val)
                return
            if node.left:
                travel(node.left,trace)
            if node.right:
                travel(node.right,trace) 
        travel(root1,trace1)
        travel(root2,trace2)
        return trace1==trace2
        # return [1,2,3]==[1,2]

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
res = a.leafSimilar(in_para1,in_para1)
print(res)