from typing import Counter, List
import collections
import bisect
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m,n=len(matrix),len(matrix[0])
        pre=[[0]*(n+1)for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                pre[i+1][j+1]=pre[i][j+1]+pre[i+1][j]+matrix[i][j]-pre[i][j]
        def sumRange(x1,y1,x2,y2):
            return pre[x2][y2]-pre[x1][y2]-pre[x2][y1]+pre[x1][y1]
        ans = float('-inf')
        for i in range(n):
            for j in range(i+1,n+1):
                d = [0]
                for l in range(1,m+1):
                    tmp = sumRange(0,i,l,j)
                    pos = bisect.bisect_left(d,tmp-k)
                    if pos<len(d):
                        ans = max(ans,tmp-d[pos])
                    bisect.insort(d,tmp)
        return ans
        
a = Solution()
in_para1 =[[1,0,1],[0,-2,3]]
in_para2 =2
resu = a.maxSumSubmatrix(in_para1,in_para2)
print(resu)
