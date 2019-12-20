from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[-999999] * 3 for _ in range(n + 1)]
        dp[0][2] = 0
        for i in range(1, n + 1):
            dp[i][0] = max(dp[i - 1][1] + prices[i - 1], dp[i - 1][0])
            dp[i][1] = max(dp[i - 1][2] - prices[i - 1], dp[i - 1][1])
            dp[i][2] = max(dp[i - 1][0], dp[i - 1][2])
        return max(dp[n][0], dp[n][1], dp[n][2])


a = Solution()
in_para1 = [1, 2, 3, 0, 2]
in_para2 = 9
resu = a.maxProfit(in_para1)
print(resu)
