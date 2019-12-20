# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:

        def first_search(node: TreeNode):
            nonlocal k

            if node.left is not None:
                first_search(node.left)
            k -= 1
            if k == 0:
                raise Exception(node.val)
            if node.right is not None:
                first_search(node.right)

        try:
            first_search(root)
        except Exception as error:
            return int(str(error))


a = Solution()
in_para1 = [1, 2, 3, 1]
in_para2 = 9
t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
t3.left = t1
t3.right = t4
t1.right = t2
resu = a.kthSmallest(t3, 1)
print(resu)
