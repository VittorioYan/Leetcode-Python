from typing import List, Sequence
import collections
import bisect

               
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [[False]*(n+1) for _ in range(2)]
        # 0:Alice,1:Bob
        dp[0][0],dp[0][1] = False,True
        dp[1][0],dp[1][1] = False,True
        square = [1]
        x = 2
        while square[-1]<n:
            square.append(x**2)
            x+=1
        for i in range(2,n+1):
            pos = bisect.bisect_right(square,i)
            for j in range(pos):
                if dp[0][i-square[j]]==False:
                    dp[1][i] = True
                if dp[1][i-square[j]]==False:
                    dp[0][i] = True
        return dp[0][n]
               

a = Solution()
in_para1 = 1
in_para2 = "execution"
resu = a.winnerSquareGame(in_para1)
print(resu)
