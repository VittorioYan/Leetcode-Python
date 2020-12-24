from typing import List
import collections
import bisect

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0]*(amount+1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin,amount+1):
                dp[i] += dp[i-coin]
        return dp[amount]
   

        

a = Solution()
in_para1 =3
in_para2 = [2]
resu = a.change(in_para1,in_para2)
print(resu)
