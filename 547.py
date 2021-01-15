from typing import List
import collections
import bisect

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        size = len(isConnected)
        flag = [True]*size
        queue = []
        ans,cur = 1,0
        while True:
            flag[cur]=False
            queue.append(cur)
            while queue:
                this_node = queue.pop(0)
                for j in range(size):
                    if isConnected[this_node][j] and flag[j]:
                        queue.append(j)
                        flag[j] = False
            cur = -1
            for i in range(size):
                if flag[i]:
                    cur = i
                    ans+=1
                    break
            if cur==-1:
                return ans
            


a = Solution()
in_para1 = [[1,0,0],[0,1,0],[0,0,1]]
in_para2 = [[0,1,2],[0,2,5]]
resu = a.findCircleNum(in_para1)
print(resu)
