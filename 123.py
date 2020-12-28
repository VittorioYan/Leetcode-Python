from typing import List
import collections
import bisect

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        k = 2
        dp = [[[-11111]*(k+1) for _ in range(2)]for __ in range(len(prices))]
        dp[0][0][0],dp[0][1][1] = 0,-prices[0]
        for i in range(1,len(prices)):
            dp[i][0][0] = 0
            for j in range(k,0,-1):
                dp[i][1][j] = max(dp[i-1][1][j],dp[i-1][0][j-1]-prices[i])
                dp[i][0][j] =  max(dp[i-1][0][j],dp[i-1][1][j]+prices[i])
        print(dp)
        return max(dp[-1][0])

a = Solution()
in_para1 = [1,2,3,4,5]
in_para2 = "execution"
resu = a.maxProfit(in_para1)
print(resu)
