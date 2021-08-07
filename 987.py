from typing import List, Tuple
import bisect
from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        dic = defaultdict(list)
        def travel(node:TreeNode,pos:Tuple):
            dic[pos].append(node.val)
            width,depth = pos
            if node.left:
                travel(node.left,(width-1,depth+1))
            if node.right:
                travel(node.right,(width+1,depth+1))
        travel(root,(0,0))
        ans = []
        base = sorted(dic.keys())
        flag,cur = -1000000,[]
        for b in base:
            if b[0]!=flag:
                ans.append(cur)
                cur = []
                flag = b[0]
            cur+=sorted(dic[b])
        ans.append(cur)        
        return ans[1:]



a = Solution()
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
in_para2 = 9
resu = a.verticalTraversal(in_para1)
print(resu)
