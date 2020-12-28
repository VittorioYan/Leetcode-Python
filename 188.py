from typing import List
import sys
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        def max_profit_inf(prices):
            profit = 0
            for i in range(1, len(prices)):
                tmp = prices[i] - prices[i - 1]
                if tmp > 0: profit += tmp
            return profit
        if not k or not prices:
            return 0
        prices_len = len(prices)
        if k >= prices_len // 2:
            return max_profit_inf(prices)
        dp = [[[-10000]*2 for _ in range(k+1)]for i in range(prices_len)]
        dp[0][1][1] = -prices[0]
        for i in range(prices_len):
            dp[i][1][0] = -10000
            dp[i][0][1] = dp[0][1][0]
            dp[i][0][0] = 0


        for i in range(1, prices_len):
            for j in range(k, 0, -1):
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i])

        print(dp)
        return max(max(dp[-1]))

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        def max_profit_inf(prices):
            profit = 0
            for i in range(1, len(prices)):
                tmp = prices[i] - prices[i - 1]
                if tmp > 0: profit += tmp
            return profit
        if not k or not prices:
            return 0
        prices_len = len(prices)
        if k >= prices_len // 2:
            return max_profit_inf(prices)
        dp = [[-10000]*2 for _ in range(k+1)]
        dp[0][0],dp[1][1] = 0,-prices[0]
        ans = 0
        for i in range(1,len(prices)):
            for j in range(k,0,-1):
                mid = dp[j][1]
                dp[j][1] = max(dp[j][1],dp[j-1][0]-prices[i])
                dp[j][0] =  max(dp[j][0],mid+prices[i])
                ans = max(ans,dp[j][0])
        return ans

a = Solution()
in_para2 = 2
in_para1 = [2,4,1]

resu = a.maxProfit(in_para2, in_para1)
print(resu)
