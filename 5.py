from typing import List
import collections
import bisect

class Solution:
    def longestPalindrome(self, s: str) -> str:
        lens = len(s)
        dp = [[0]*(lens) for _ in range(lens)]
        for i in range(lens):
            dp[i][i] = 1
        _max = s[0]
        for i in range(lens-1,-1,-1):
            for j in range(i+1,lens):
                if s[i]==s[j]:
                    if dp[i+1][j-1]!=0:
                        dp[i][j] = dp[i+1][j-1]+2
                    if j-i==1:
                        dp[i][j] = 2
                    if dp[i][j]>len(_max):
                        _max = s[i:j+1]
        # print(dp)
        return _max
        

a = Solution()
in_para1 = "aacabdkacaa"
in_para2 = "def"
resu = a.longestPalindrome(in_para1)
print(resu)
