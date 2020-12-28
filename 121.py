from typing import List
import collections
import bisect
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        _min = prices[0]
        ans = 0
        for price in prices[1:]:
            ans = max(ans,price-_min)
            _min = min(_min,price)
        return ans 
   
        # dp = [[-111]*2 for _ in range(len(prices))]
        # dp[0][0],dp[0][1] = 0,-prices[0]
        # for i in range(1,len(prices)):
        #     dp[i][1] = max(dp[i-1][1],max(0,dp[i-1][0])-prices[i])
        #     dp[i][0] =  max(dp[i-1][0],dp[i-1][1]+prices[i])
        

a = Solution()
in_para1 = []
in_para2 = "execution"
resu = a.maxProfit(in_para1)
print(resu)
