from typing import List, Sequence
import collections
import bisect
import heapq
from sortedcontainers import SortedList
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        mod = 10**9+7
        l = len(group)
        dp = [[0]*(minProfit+1) for _ in range(n+1)]
        for i in range(n+1):dp[i][0] = 1
        for i in range(l):
            for j in range(n,group[i]-1,-1):
                for k in range(minProfit,-1,-1):
                    dp[j][k] += dp[j-group[i]][max(k-profit[i],0)]
                    if (dp[j][k] >= mod):dp[j][k] -= mod
        return dp[-1][-1]

a = Solution()
in_para1 = [2,3,5]
in_para2 = [6,7,8]
resu = a.profitableSchemes(10,5,in_para1,in_para2)
print(resu)
