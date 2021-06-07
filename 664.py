from typing import List
import collections
import bisect
import heapq
class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        dp = [[0]*(n) for _ in range(n)]
        for i in range(n-1,-1,-1):
            dp[i][i] = 1
            for j in range(i+1,n):
                if s[i]==s[j]:
                    dp[i][j] = dp[i][j-1]
                else:
                    temp = n+1
                    for k in range(i,j):
                        temp = min(temp,dp[i][k]+dp[k+1][j])
                    dp[i][j] = temp
        return dp[0][n-1]

a = Solution()
in_para1 = "aaabbb"
in_para2 = [1,2,4]
resu = a.strangePrinter(in_para1)
print(resu)
