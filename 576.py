from typing import List
import collections
import bisect
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9+7
        dp = [[[-1]*(n) for _ in range(m)]for __ in range(maxMove+1)]
        def dfs(mv,cm,cn):
            if cm<0 or cn<0 or cm>=m or cn>=n:
                return 1
            if mv==0:
                return 0
            if dp[mv][cm][cn]<0:
                dp[mv][cm][cn]= (dfs(mv-1,cm-1,cn)+\
                                dfs(mv-1,cm+1,cn)+\
                                dfs(mv-1,cm,cn-1)+\
                                dfs(mv-1,cm,cn+1))%MOD
            return dp[mv][cm][cn]
        return dfs(maxMove,startRow,startColumn)



a = Solution()
in_para1 = [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]]
in_para2 = [[0, 1], [2, 3]]
resu = a.findPaths(2,2,2,0,0)
print(resu)
