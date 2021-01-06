from typing import List
import collections
import bisect
from functools import lru_cache
# 两种动态规划，貌似都会超时，第二种会好一点因为少计算了一些
# class Solution:
#     def stoneGameV(self, stoneValue: List[int]) -> int:
#         size = len(stoneValue)
#         # dp[i][j] 从i到j能拿到的最大分数
#         dp = [[0]*(size+1) for _ in range(size+1)]
#         s = [0]*(size+1)
#         for i in range(1,size+1):
#             s[i] = s[i-1]+stoneValue[i-1]
#         # print(s)
#         for step in range(2,size+1):
#             for i in range(size):
#                 cur = 0
#                 if i+step>size:
#                     break
#                 for j in range(i+1,i+step):
#                     if s[j]-s[i]<s[i+step]-s[j]:
#                         cur = max(cur,dp[i][j]+s[j]-s[i])
#                     elif s[j]-s[i]>s[i+step]-s[j]:
#                         cur = max(cur,dp[j][i+step]+s[i+step]-s[j])
#                     else:
#                         cur = max(cur,max(dp[i][j],dp[j][i+step])+s[i+step]-s[j])
                    
#                 dp[i][i+step] = cur
#         return dp[0][size]
             
# class Solution:
#     def stoneGameV(self, stoneValue: List[int]) -> int:
#         size = len(stoneValue)
#         # dp[i][j] 从i到j能拿到的最大分数
#         dp = [[0]*(size+1) for _ in range(size+1)]
#         s = [0]*(size+1)
#         for i in range(1,size+1):
#             s[i] = s[i-1]+stoneValue[i-1]
#         # print(s)
#         @lru_cache(None)
#         def dfs(i,j):
#             if i<0 or j>size or j-i<2:
#                 return 0
#             # if dp[i][j]:
#             #     return dp[i][j]
#             cur = 0
#             for k in range(i+1,j):
#                 left = s[k]-s[i]
#                 right = s[j]-s[k]
#                 if left<right:
#                     cur = max(cur,dfs(i,k)+left)
#                 elif left>right:
#                     cur = max(cur,dfs(k,j)+right)
#                 else:
#                     cur = max(cur,max(dfs(k,j),dfs(i,k))+left)
#             dp[i][j] = cur
#             return cur
        
#         return dfs(0,size)
     

# 官方答案
class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        f = [[0] * n for _ in range(n)]
        maxl = [[0] * n for _ in range(n)]
        maxr = [[0] * n for _ in range(n)]

        for left in range(n - 1, -1, -1):
            maxl[left][left] = maxr[left][left] = stoneValue[left]
            total = stoneValue[left]
            suml = 0
            i = left - 1
            for right in range(left + 1, n):
                total += stoneValue[right]
                while i + 1 < right and (suml + stoneValue[i + 1]) * 2 <= total:
                    suml += stoneValue[i + 1]
                    i += 1
                if left <= i:
                    f[left][right] = max(f[left][right], maxl[left][i])
                if i + 1 < right:
                    f[left][right] = max(f[left][right], maxr[i + 2][right])
                if suml * 2 == total:
                    f[left][right] = max(f[left][right], maxr[i + 1][right])
                maxl[left][right] = max(maxl[left][right - 1], total + f[left][right])
                maxr[left][right] = max(maxr[left + 1][right], total + f[left][right])
        
        return f[0][n - 1]


a = Solution()
in_para1 =[39994,3,4,10000,10000,10000,10000,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1000000]
in_para2 = "execution"
resu = a.stoneGameV(in_para1)
print(resu)
