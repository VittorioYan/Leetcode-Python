# Definition for a binary tree node.
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def increasingBST(self, root):
        dummy = TreeNode(-1)
        self.prev = dummy
        self.inOrder(root)
        return dummy.right
        
    def inOrder(self, root):
        if not root:
            return None
        self.inOrder(root.left)
        root.left = None
        self.prev.right = root
        self.prev = root
        self.inOrder(root.right)


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
res = a.increasingBST(in_para1)
print(res)