from typing import List
import collections
import bisect

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        lens = len(s)
        dp = [[0]*(lens) for _ in range(lens)]
        for i in range(lens):
            dp[i][i] = 1
        for i in range(lens-1,-1,-1):
            for j in range(i+1,lens):
                if s[i]==s[j]:
                    dp[i][j] = dp[i+1][j-1]+2
                else:
                    dp[i][j] = max(dp[i+1][j],dp[i][j-1])
        # print(dp)
        return dp[0][lens-1]


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        s = list(s)
        dp = [[1]*n for _ in range(n)]
        for j in range(n-1):
            if s[j]==s[j+1]:
                dp[j][j+1]=2
        for i in range(2,n):
            for j in range(n-i):
                if s[j]==s[j+i]:
                    dp[j][j+i] = max(dp[j][j+i],dp[j+1][j+i-1]+2)
                else:
                    dp[j][j+i] = max(dp[j][j+i-1],dp[j+1][j+i])
        return dp[0][-1]

a = Solution()
in_para1 = "bbbab"
in_para2 = "def"
resu = a.longestPalindromeSubseq(in_para1)
print(resu)
