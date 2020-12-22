from typing import List
import collections

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0]*(len(cost)+1)
        for i in range(2,len(cost)+1):
            dp[i] = min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])
        return dp[-1]

  

a = Solution()
in_para1 =[1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
in_para2 = "execution"
resu = a.minCostClimbingStairs(in_para1)
print(resu)
