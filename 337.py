from typing import List
# import sys

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class Solution:
#     def rob(self, root: TreeNode) -> int:
#         if not root:
#             return 0
#         def rob_tree(node:TreeNode,is_rob:bool):
#             l=r=0
#             if is_rob:
#                 if node.left is not None:
#                     l = rob_tree(node.left,False)
#                 if node.right is not None:
#                     r = rob_tree(node.right,False)
#                 return l+r+node.val
#             else:
#                 if node.left is not None:
#                     l = max(rob_tree(node.left,False),rob_tree(node.left,True))
#                 if node.right is not None:
#                     r = max(rob_tree(node.right,False),rob_tree(node.right,True))
#                 return l+r
#         return max(rob_tree(root,True),rob_tree(root,False))
                
class Solution:
    def rob(self, root: TreeNode) -> int:
        def _rob(root):
            if not root: return 0, 0  # 偷，不偷

            left = _rob(root.left)
            right = _rob(root.right)
            # 偷当前节点, 则左右子树都不能偷
            v1 = root.val + left[1] + right[1]
            # 不偷当前节点, 则取左右子树中最大的值
            v2 = max(left) + max(right)
            return v1, v2

        return max(_rob(root))

a = Solution()
in_para1 = TreeNode(3)
in_para2 = TreeNode(4)
in_para3 = TreeNode(5)
in_para4 = TreeNode(1)
in_para5 = TreeNode(3)
in_para6 = TreeNode(1)
in_para1.left = in_para2
in_para1.right = in_para3
in_para2.left = in_para4
in_para2.right = in_para6
in_para3.right = in_para6
resu = a.rob(in_para1)
print(resu)
