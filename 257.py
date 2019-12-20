from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        result = []
        if not root:
            return result
        def helper(node:TreeNode, path:str):
            path += "->" + str(node.val)
            if node.right is None and node.left is None:
                result.append(path[2:])
                return
            if node.right is not None:
                helper(node.right, path)
            if node.left is not None:
                helper(node.left, path)
        helper(root, "")
        return result



a = Solution()
in_para1 = [1, 2, 3, 1]
in_para2 = 9
t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(5)
t1.left= t2
t1.right = t3
t2.right = t4
resu = a.binaryTreePaths(None)
print(resu)
