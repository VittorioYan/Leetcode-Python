from typing import List
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rightSideView(self, root: TreeNode) -> List[int]:
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        colored_depth = -1
        res = []
        if not root:
            return res

        def search(node: TreeNode, depth: int):
            if node is None:
                return
            nonlocal colored_depth
            if depth > colored_depth:
                colored_depth = depth
                res.append(node.val)
            search(node.right, depth+1)
            search(node.left, depth+1)
        search(root, 0)
        return res

a = Solution()
in_para1 = TreeNode(1)
in_para2 = TreeNode(2)
in_para3 = TreeNode(3)
in_para4 = TreeNode(4)
in_para5 = TreeNode(5)
in_para1.left = in_para2
in_para1.right = in_para3
in_para2.right = in_para5
in_para3.right = in_para4
in_para5.left = TreeNode(7)
resu = a.rightSideView(in_para1)
print(resu)