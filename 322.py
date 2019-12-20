from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [99999] * (amount + 1)
        for coin in coins:
            if coin <= amount:
                dp[coin] = 1
        for i in range(amount + 1):
            if dp[i] == 99999:
                continue
            for coin in coins:
                if coin + i <= amount:
                    dp[coin + i] = min(dp[coin + i], dp[i] + 1)
        return dp[-1] if dp[-1] != 99999 else -1


a = Solution()
in_para1 = [1]
in_para2 = 1
resu = a.coinChange(in_para1, in_para2)
print(resu)
