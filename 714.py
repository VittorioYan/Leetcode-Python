from typing import List

# class Solution:
#     def maxProfit(self, prices: List[int], fee: int) -> int:
#         no_buy = [0]*len(prices)
#         buy = [-50001]*len(prices)
#         buy[0] = -prices[0]-fee
#         for i in range(1,len(prices)):
#             buy[i] = max(buy[i-1],no_buy[i-1]-prices[i]-fee)
#             no_buy[i] = max(no_buy[i-1],buy[i-1]+prices[i])
#         return no_buy[len(prices)-1]

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        no_buy = 0
        no_buy_last = 0
        buy = -50001
        buy_last = -prices[0]-fee
        for i in range(1,len(prices)):
            buy = max(buy_last,no_buy_last-prices[i]-fee)
            no_buy = max(no_buy_last,buy_last+prices[i])
            buy_last = buy
            no_buy_last = no_buy
        return no_buy

a = Solution()
in_para1 = [1,3,5]
in_para2 = 2
resu = a.maxProfit(in_para1,in_para2)
print(resu)
