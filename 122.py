from typing import List
import collections
import bisect

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        _min = prices[0]
        ans = 0
        for i in range(1,len(prices)):
            if prices[i]<prices[i-1]:
                ans+=prices[i-1]-_min
                _min = prices[i]
        ans+=prices[-1]-_min
        return ans 
   

a = Solution()
in_para1 = [7,6,4,3,1,2]
in_para2 = "execution"
resu = a.maxProfit(in_para1)
print(resu)
