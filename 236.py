# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == p:
            return root
        if root == q:
            return root
        if root is None:
            return None
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        if (l == q and r == p) or (l == p and r == q):
            return root
        if l is not None:
            return l
        if r is not None:
            return r


a = Solution()
in_para1 = [1, 2, 3, 1]
in_para2 = 9
t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
t1.left = t2
t1.right = t3
t2.left = t4
resu = a.lowestCommonAncestor(t1,t2,t4)
print(resu.val)
