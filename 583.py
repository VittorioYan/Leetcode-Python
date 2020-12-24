from typing import List
import collections
import bisect

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1,len2 = len(word1),len(word2)
        dp = [[0]*(len2+1) for _ in range(len1+1)]
        for i in range(1,len1+1):
            for j in range(1,len2+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] =max(dp[i][j-1],dp[i-1][j])
        return len1+len2-2*dp[len1][len2]

a = Solution()
in_para1 = "seaa"
in_para2 = "eata"
resu = a.minDistance(in_para1,in_para2)
print(resu)
