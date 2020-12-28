from typing import List
import collections
import bisect
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        size = len(piles)
        dp = [[(0,0)]*size for _ in range(size)]
        for i in range(size):
            dp[i][i] = (piles[i],0)
        for n in range(1,size):
            for i in range(0,size-n):
                if dp[i+1][i+n][1]+piles[i]>dp[i][i+n-1][1]+piles[i+n]:
                    first = dp[i+1][i+n][1]+piles[i]
                    last = dp[i+1][i+n][0]
                else:
                    first = dp[i][i+n-1][1]+piles[i+n]
                    last = dp[i][i+n-1][0]
                dp[i][i+n] = (first,last)
        print(dp)
        return dp[0][-1][0]>dp[0][-1][1]      
        

a = Solution()
in_para1 = [5,3,4,5]
in_para2 = "execution"
resu = a.stoneGame(in_para1)
print(resu)
